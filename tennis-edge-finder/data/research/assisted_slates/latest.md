# ASSISTED SLATE -- 2026-10-28T12:31Z (`SL-20261028T123129Z-f6f011d0`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

398 open matches not seen started, 1019 markets. Skipped: {"scheduled_start_over_24h_past": 16, "no_match_winner_listed": 1, "first_ball_already_observed": 3}. Sources: shadow board 2026-10-28T12:14:03.068139+00:00, Model 4 2026-10-28T12:15:41.627298+00:00, Gen-1 ledger 2026-10-28T12:13:58.141325+00:00, external 2026-10-28T11:49:31.158856+00:00, capture 20261028T114709Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-10-28 13:00Z**
* Recommended RUN TENNIS time: **2026-10-28 12:15Z**  (**OVERDUE -- run now**)
* Final price/status check time: **2026-10-28 12:50Z**
* Number of matches in window: 2 (Remy Bertola vs Denis Shapovalov, Nuno Borges vs Casper Ruud)

* **2 main-tour match(es) have NO verified start status** (STATUS_AMBIGUOUS): BET blocked until a live status check.

Slate built 2026-10-28T12:31Z. Refresh due by: 2026-10-28 12:15Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 59, "HIGH_REVIEW": 99, "NORMAL": 453, "REVIEW": 119, "UNPRICED": 289}; match winners: {"EXTREME": 54, "HIGH_REVIEW": 79, "NORMAL": 296, "REVIEW": 79, "UNPRICED": 288}; quote freshness at build: {"AGING": 730}.

## Luis Britto / Marcelo Zormann vs Anthony Genov / Younes Lalami Laaroussi -- ATP Challenger Guayaquil R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-27 22:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-27T22:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT27BRIZORGENLAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luis Britto / Marcelo Zormann (`KXATPCHALLENGERDOUBLES-26OCT27BRIZORGENLAL-BRIZOR`) | 0.13 / 0.79 (50) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anthony Genov / Younes Lalami Laaroussi (`KXATPCHALLENGERDOUBLES-26OCT27BRIZORGENLAL-GENLAL`) | 0.05 / 0.58 (1) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Leylah Fernandez vs Elise Mertens -- WTA Tokyo R16

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-28 04:30Z
* Current expected start: 2026-10-28 04:30Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-27 08:23Z
* Recommended handicap-by time: 2026-10-28 03:45Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-28T04:00:00+00:00 as not a valid time; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-28T04:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:210722:220367:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leylah Fernandez (`KXWTAMATCH-26OCT27FERMER-FER`) | 0.47 / 0.48 (14) | 47.5% | 46.9% | 34.4% | 38.3% [36.3%-43.3%] | -- | -- | -- | -- | PASS | -0.7 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elise Mertens (`KXWTAMATCH-26OCT27FERMER-MER`) | 0.52 / 0.53 (8275) | 52.5% | 53.1% | 65.6% | 61.7% [56.7%-63.7%] | -- | -- | -- | -- | SHADOW_BET | +0.7 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4828.0, B 3838.0; serve-point win A 59.3%, B 40.1%; Elo A 1978.3, B 1978.5; model uncertainty 0.0348
* Form inputs: days since last match A 1, B 2; matches on record A 406, B 807; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.020, surface_dev_loose -0.005, surface_dev_tight +0.010
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT27FERMER-23` Over 22.5 games: 0.47/0.48 mid 47.5%, model 57.9% (projection_v2.0 (prediction ledger)) -- gap +10.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT27FERMER-18` Over 17.5 games: 0.79/0.87 mid 83.0%, model 90.2% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT27FERMER-2-FER` Will Leylah Annie Fernandez win set 2 in the Leylah Annie Fernandez vs Elise Mertens match: 0.02/0.99 mid 50.5%, model 47.9% (projection_v2.0 (prediction ledger)) -- gap -2.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26OCT27FERMER-28` Over 27.5 games: 0.19/0.58 mid 38.5%, model 36.9% (projection_v2.0 (prediction ledger)) -- gap -1.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT27FERMER-1-FER` Will Leylah Annie Fernandez win set 1 in the Leylah Annie Fernandez vs Elise Mertens match: 0.48/0.51 mid 49.5%, model 47.9% (projection_v2.0 (prediction ledger)) -- gap -1.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT27FERMER-2-MER` Will Elise Mertens win set 2 in the Leylah Annie Fernandez vs Elise Mertens match: 0.02/0.99 mid 50.5%, model 52.1% (projection_v2.0 (prediction ledger)) -- gap +1.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT27FERMER-1-MER` Will Elise Mertens win set 1 in the Leylah Annie Fernandez vs Elise Mertens match: 0.49/0.53 mid 51.0%, model 52.1% (projection_v2.0 (prediction ledger)) -- gap +1.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Petr Bar Biryukov vs Fajing Sun -- ATP Challenger Ningbo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-28T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111806:209951:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Petr Bar Biryukov (`KXATPCHALLENGERMATCH-26OCT27BARSUN-BAR`) | 0.34 / 0.35 (1713) | 34.5% | 40.5% | 31.4% | 35.7% [33.6%-38.4%] | -- | -- | -- | -- | PASS | +6.0 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Fajing Sun (`KXATPCHALLENGERMATCH-26OCT27BARSUN-SUN`) | 0.65 / 0.66 (4949) | 65.5% | 59.5% | 68.6% | 64.3% [61.6%-66.4%] | -- | -- | -- | -- | PASS | -6.0 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4232.0, B 4200.0; serve-point win A 68.1%, B 29.9%; Elo A 1539.3, B 1556.5; model uncertainty 0.0242
* Form inputs: days since last match A 11, B 9; matches on record A 242, B 526; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.004, surface_dev_loose -0.004, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Naoya Honda vs Liam Broady -- ATP Challenger Ningbo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-28T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106281:211897:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liam Broady (`KXATPCHALLENGERMATCH-26OCT27HONBRO-BRO`) | 0.74 / 0.80 (42) | 77.0% | 75.8% | 87.5% | 85.6% [84.7%-86.7%] | -- | -- | -- | -- | SHADOW_BET | -1.2 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Naoya Honda (`KXATPCHALLENGERMATCH-26OCT27HONBRO-HON`) | 0.20 / 0.23 (8) | 21.5% | 24.2% | 12.4% | 14.4% [13.3%-15.3%] | -- | -- | -- | -- | PASS | +2.8 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1551.0, B 4440.0; serve-point win A 58.2%, B 36.4%; Elo A 1354.9, B 1639.6; model uncertainty 0.0101
* Form inputs: days since last match A 44, B 9; matches on record A 70, B 947; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.006, surface_dev_loose -0.006, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tristan Schoolkate vs Jie Cui -- ATP Challenger Ningbo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-28T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200666:209262:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jie Cui (`KXATPCHALLENGERMATCH-26OCT27SCHCUI-CUI`) | 0.36 / 0.39 (212) | 37.5% | 36.4% | 39.6% | 37.7% [34.5%-39.1%] | -- | -- | -- | -- | PASS | -1.1 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tristan Schoolkate (`KXATPCHALLENGERMATCH-26OCT27SCHCUI-SCH`) | 0.61 / 0.64 (74) | 62.5% | 63.6% | 60.4% | 62.3% [60.9%-65.5%] | -- | -- | -- | -- | PASS | +1.1 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6055.0, B 3672.0; serve-point win A 68.8%, B 34.1%; Elo A 1701.7, B 1581.1; model uncertainty 0.0231
* Form inputs: days since last match A 9, B 9; matches on record A 421, B 334; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.014, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Yi Zhou vs Jake Delaney -- ATP Challenger Ningbo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-28T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:117359:212044:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jake Delaney (`KXATPCHALLENGERMATCH-26OCT27ZHODEL-DEL`) | 0.17 / 0.21 (29) | 19.0% | 19.8% | 25.7% | 24.2% [23.4%-25.6%] | -- | -- | -- | -- | SHADOW_BET | +0.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yi Zhou (`KXATPCHALLENGERMATCH-26OCT27ZHODEL-ZHO`) | 0.80 / 0.83 (65) | 81.5% | 80.2% | 74.3% | 75.8% [74.4%-76.5%] | -- | -- | -- | -- | PASS | -1.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3697.0, B 3181.0; serve-point win A 72.0%, B 35.1%; Elo A 1641.8, B 1414.5; model uncertainty 0.0107
* Form inputs: days since last match A 9, B 9; matches on record A 180, B 340; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.000, surface_dev_loose +0.007, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Yannick Hanfmann vs Jan-Lennard Struff -- ATP Basel R32

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-27 14:00Z
* Current expected start: 2026-10-28 11:40Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-28 10:55Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1300_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-27T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105526:105870:2026-10-27`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yannick Hanfmann (`KXATPMATCH-26OCT27HANSTR-HAN`) | 0.34 / 0.35 (64856) | 34.5% | 51.7% | 57.1% | 54.7% [50.5%-56.6%] | -- | -- | -- | -- | SHADOW_BET | +17.2 pp | HIGH_REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jan-Lennard Struff (`KXATPMATCH-26OCT27HANSTR-STR`) | 0.66 / 0.67 (26628) | 66.5% | 48.3% | 42.9% | 45.3% [43.4%-49.5%] | -- | -- | -- | -- | PASS | -18.2 pp | HIGH_REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5488.0, B 5412.0; serve-point win A 68.5%, B 31.9%; Elo A 1791.3, B 1818.1; model uncertainty 0.0306
* Form inputs: days since last match A 2, B 2; matches on record A 704, B 1071; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT27HANSTR-HAN  (YES = Yannick Hanfmann)
Model: 52%
Kalshi: 34%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.009, surface_dev_loose -0.000, surface_dev_tight -0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPSETWINNER-26OCT27HANSTR-1-HAN` Will Yannick Hanfmann win set 1 in the Yannick Hanfmann vs Jan-Lennard Struff match: 0.30/0.31 mid 30.5%, model 51.1% (projection_v2.0 (prediction ledger)) -- gap +20.6 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT27HANSTR-1-STR` Will Jan-Lennard Struff win set 1 in the Yannick Hanfmann vs Jan-Lennard Struff match: 0.69/0.70 mid 69.5%, model 48.9% (projection_v2.0 (prediction ledger)) -- gap -20.6 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT27HANSTR-STR2` Will Jan-Lennard Struff win at least 1.5 more games than Yannick Hanfmann?: 0.50/0.62 mid 56.0%, model 39.7% (projection_v2.0 (prediction ledger)) -- gap -16.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT27HANSTR-STR20` Will Jan-Lennard Struff win the Yannick Hanfmann vs Jan-Lennard Struff match by a set score of 2-0?: 0.34/0.41 mid 37.5%, model 23.9% (projection_v2.0 (prediction ledger)) -- gap -13.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT27HANSTR-STR5` Will Jan-Lennard Struff win at least 4.5 more games than Yannick Hanfmann?: 0.18/0.30 mid 24.0%, model 10.5% (projection_v2.0 (prediction ledger)) -- gap -13.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT27HANSTR-HAN2` Will Yannick Hanfmann win at least 1.5 more games than Jan-Lennard Struff?: 0.23/0.39 mid 31.0%, model 43.0% (projection_v2.0 (prediction ledger)) -- gap +12.0 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT27HANSTR-HAN20` Will Yannick Hanfmann win the Yannick Hanfmann vs Jan-Lennard Struff match by a set score of 2-0?: 0.13/0.19 mid 16.0%, model 26.2% (projection_v2.0 (prediction ledger)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT27HANSTR-2-HAN` Will Yannick Hanfmann win set 2 in the Yannick Hanfmann vs Jan-Lennard Struff match: 0.41/0.42 mid 41.5%, model 51.1% (projection_v2.0 (prediction ledger)) -- gap +9.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT27HANSTR-2-STR` Will Jan-Lennard Struff win set 2 in the Yannick Hanfmann vs Jan-Lennard Struff match: 0.58/0.59 mid 58.5%, model 48.9% (projection_v2.0 (prediction ledger)) -- gap -9.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT27HANSTR-25` Over 24.5 games: 0.62/0.63 mid 62.5%, model 57.9% (projection_v2.0 (prediction ledger)) -- gap -4.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT27HANSTR-HAN21` Will Yannick Hanfmann win the Yannick Hanfmann vs Jan-Lennard Struff match by a set score of 2-1?: 0.20/0.22 mid 21.0%, model 25.6% (projection_v2.0 (prediction ledger)) -- gap +4.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT27HANSTR-30` Over 29.5 games: 0.41/0.43 mid 42.0%, model 38.5% (projection_v2.0 (prediction ledger)) -- gap -3.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT27HANSTR-20` Over 19.5 games: 0.80/0.97 mid 88.5%, model 87.7% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT27HANSTR-STR21` Will Jan-Lennard Struff win the Yannick Hanfmann vs Jan-Lennard Struff match by a set score of 2-1?: 0.23/0.26 mid 24.5%, model 24.4% (projection_v2.0 (prediction ledger)) -- gap -0.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Laura Mair vs Katarina Zavatska -- WTA 125K Courmayeur R32

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-28 15:10Z
* Current expected start: 2026-10-28 11:53Z
* Source: COURT_PROGRESSION: preceding match on Centre Court in progress (set 2 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-28 11:08Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA125 (WTA_125) · surface ? · scheduled 2026-10-28T15:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:215290:220827:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Laura Mair (`KXWTACHALLENGERMATCH-26OCT28MAIZAV-MAI`) | 0.18 / 0.19 (2113) | 18.5% | 18.1% | 28.7% | 24.4% [21.9%-26.1%] | -- | 18.6% | 18.6% | MODEL_LONE_OUTLIER | SHADOW_BET | -0.4 pp | NORMAL | AGING | A / LIMITED | ALL_AGREE | VERIFIED |
| Katarina Zavatska (`KXWTACHALLENGERMATCH-26OCT28MAIZAV-ZAV`) | 0.82 / 0.83 (8018) | 82.5% | 81.9% | 71.3% | 75.6% [73.9%-78.1%] | -- | 81.3% | 81.3% | MODEL_LONE_OUTLIER | PASS | -0.6 pp | NORMAL | AGING | A / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 2387.0, B 4227.0; serve-point win A 50.4%, B 42.8%; Elo A 1462.8, B 1722.0; model uncertainty 0.0207
* Form inputs: days since last match A 15, B 19; matches on record A 242, B 498; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; STATUS_AMBIGUOUS

## Elsa Jacquemot vs Caroline Werner -- WTA 125K Courmayeur R32

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-28 15:10Z
* Current expected start: 2026-10-28 12:18Z
* Source: COURT_PROGRESSION: preceding match on Grandstand in progress (set 1 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-28 11:33Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA125 (WTA_125) · surface ? · scheduled 2026-10-28T15:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221039:espn:espn:4384:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elsa Jacquemot (`KXWTACHALLENGERMATCH-26OCT28JACWER-JAC`) | 0.75 / 0.76 (173) | 75.5% | 76.4% | 65.0% | 72.0% [72.0%-72.0%] | 73.5% | 75.2% | 75.2% | MODEL_LONE_OUTLIER | PASS | +0.9 pp | NORMAL | AGING | D / POOR | EXTERNAL_STALE | VERIFIED |
| Caroline Werner (`KXWTACHALLENGERMATCH-26OCT28JACWER-WER`) | 0.23 / 0.25 (4056) | 24.0% | 23.6% | 35.0% | 28.0% [28.0%-28.0%] | 26.5% | 25.1% | 25.1% | MODEL_LONE_OUTLIER | PASS | -0.4 pp | NORMAL | AGING | D / POOR | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4592.0, B 0.0; serve-point win A 58.3%, B 47.1%; Elo A 1779.0, B 1618.5; model uncertainty 0.0
* Form inputs: days since last match A 15, B 16; matches on record A 402, B 24; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; STATUS_AMBIGUOUS; EXTERNAL_PRICE_STALE

## Janice Tjen / Venus Williams vs Lyudmyla Kichenok / Makoto Ninomiya -- WTA Guangzhou QF

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-28 08:00Z
* Current expected start: 2026-10-28 12:18Z
* Source: COURT_PROGRESSION: preceding match on Center Court in progress (set 1 of best-of-3); confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-28 11:33Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-28T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28TJEWILKICNIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lyudmyla Kichenok / Makoto Ninomiya (`KXWTADOUBLES-26OCT28TJEWILKICNIN-KICNIN`) | 0.40 / 0.41 (47) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Janice Tjen / Venus Williams (`KXWTADOUBLES-26OCT28TJEWILKICNIN-TJEWIL`) | 0.58 / 0.60 (415) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Remy Bertola vs Denis Shapovalov -- ATP Basel R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-27 14:00Z
* Current expected start: 2026-10-28 13:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-28 12:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1380_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-10-27T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:133430:200329:2026-10-27`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Remy Bertola (`KXATPMATCH-26OCT27BERSHA-BER`) | 0.27 / 0.28 (92670) | 27.5% | 18.2% | 23.4% | 20.4% [18.7%-21.9%] | -- | -- | -- | -- | PASS | -9.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Denis Shapovalov (`KXATPMATCH-26OCT27BERSHA-SHA`) | 0.73 / 0.74 (14006) | 73.5% | 81.8% | 76.6% | 79.6% [78.1%-81.3%] | -- | -- | -- | -- | SHADOW_BET | +8.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4831.0, B 4653.0; serve-point win A 60.0%, B 32.8%; Elo A 1607.7, B 1933.0; model uncertainty 0.0159
* Form inputs: days since last match A 2, B 23; matches on record A 471, B 580; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.004, surface_dev_loose -0.003, surface_dev_tight +0.007
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT27BERSHA-SHA4` Will Denis Shapovalov win at least 3.5 more games than Remy Bertola?: 0.47/0.48 mid 47.5%, model 57.9% (projection_v2.0 (prediction ledger)) -- gap +10.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT27BERSHA-BER2` Will Remy Bertola win at least 1.5 more games than Denis Shapovalov?: 0.19/0.23 mid 21.0%, model 13.5% (projection_v2.0 (prediction ledger)) -- gap -7.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT27BERSHA-1-SHA` Will Denis Shapovalov win set 1 in the Remy Bertola vs Denis Shapovalov match: 0.65/0.66 mid 65.5%, model 72.8% (projection_v2.0 (prediction ledger)) -- gap +7.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT27BERSHA-1-BER` Will Remy Bertola win set 1 in the Remy Bertola vs Denis Shapovalov match: 0.33/0.34 mid 33.5%, model 27.2% (projection_v2.0 (prediction ledger)) -- gap -6.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT27BERSHA-BER20` Will Remy Bertola win the Remy Bertola vs Denis Shapovalov match by a set score of 2-0?: 0.12/0.14 mid 13.0%, model 7.4% (projection_v2.0 (prediction ledger)) -- gap -5.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT27BERSHA-18` Over 17.5 games: 0.91/0.94 mid 92.5%, model 87.6% (projection_v2.0 (prediction ledger)) -- gap -4.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT27BERSHA-2-SHA` Will Denis Shapovalov win set 2 in the Remy Bertola vs Denis Shapovalov match: 0.66/0.70 mid 68.0%, model 72.8% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT27BERSHA-SHA20` Will Denis Shapovalov win the Remy Bertola vs Denis Shapovalov match by a set score of 2-0?: 0.48/0.49 mid 48.5%, model 53.0% (projection_v2.0 (prediction ledger)) -- gap +4.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT27BERSHA-SHA21` Will Denis Shapovalov win the Remy Bertola vs Denis Shapovalov match by a set score of 2-1?: 0.23/0.26 mid 24.5%, model 28.8% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT27BERSHA-23` Over 22.5 games: 0.53/0.54 mid 53.5%, model 49.4% (projection_v2.0 (prediction ledger)) -- gap -4.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT27BERSHA-2-BER` Will Remy Bertola win set 2 in the Remy Bertola vs Denis Shapovalov match: 0.29/0.32 mid 30.5%, model 27.2% (projection_v2.0 (prediction ledger)) -- gap -3.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT27BERSHA-BER21` Will Remy Bertola win the Remy Bertola vs Denis Shapovalov match by a set score of 2-1?: 0.12/0.14 mid 13.0%, model 10.8% (projection_v2.0 (prediction ledger)) -- gap -2.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT27BERSHA-SHA7` Will Denis Shapovalov win at least 6.5 more games than Remy Bertola?: 0.07/0.19 mid 13.0%, model 14.6% (projection_v2.0 (prediction ledger)) -- gap +1.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT27BERSHA-28` Over 27.5 games: 0.27/0.35 mid 31.0%, model 31.0% (projection_v2.0 (prediction ledger)) -- gap +0.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nuno Borges vs Casper Ruud -- ATP Basel R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-28 14:00Z
* Current expected start: 2026-10-28 13:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-28 12:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-60_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-10-28T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:132686:134770:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nuno Borges (`KXATPMATCH-26OCT28BORRUU-BOR`) | 0.37 / 0.38 (56015) | 37.5% | 39.7% | 40.1% | 39.6% [36.8%-41.9%] | 36.1% | 37.5% | 36.8% | MODEL_LONE_OUTLIER | PASS | +2.2 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Casper Ruud (`KXATPMATCH-26OCT28BORRUU-RUU`) | 0.62 / 0.63 (5282) | 62.5% | 60.3% | 59.9% | 60.4% [58.1%-63.2%] | 63.9% | 62.5% | 63.2% | MODEL_LONE_OUTLIER | PASS | -2.2 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5889.0, B 5162.0; serve-point win A 66.6%, B 31.2%; Elo A 1862.6, B 1946.6; model uncertainty 0.0255
* Form inputs: days since last match A 2, B 2; matches on record A 551, B 718; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.023, surface_pool_high +0.023, surface_dev_loose +0.010, surface_dev_tight -0.014
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT28BORRUU-23` Over 22.5 games: 0.52/0.54 mid 53.0%, model 65.5% (projection_v2.0 (prediction ledger)) -- gap +12.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT28BORRUU-RUU6` Will Casper Ruud win at least 5.5 more games than Nuno Borges?: 0.15/0.19 mid 17.0%, model 7.8% (projection_v2.0 (prediction ledger)) -- gap -9.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT28BORRUU-28` Over 27.5 games: 0.34/0.36 mid 35.0%, model 44.0% (projection_v2.0 (prediction ledger)) -- gap +9.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT28BORRUU-RUU3` Will Casper Ruud win at least 2.5 more games than Nuno Borges?: 0.50/0.51 mid 50.5%, model 42.4% (projection_v2.0 (prediction ledger)) -- gap -8.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT28BORRUU-RUU20` Will Casper Ruud win the Nuno Borges vs Casper Ruud match by a set score of 2-0?: 0.38/0.41 mid 39.5%, model 32.4% (projection_v2.0 (prediction ledger)) -- gap -7.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT28BORRUU-RUU21` Will Casper Ruud win the Nuno Borges vs Casper Ruud match by a set score of 2-1?: 0.21/0.23 mid 22.0%, model 27.9% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT28BORRUU-BOR21` Will Nuno Borges win the Nuno Borges vs Casper Ruud match by a set score of 2-1?: 0.14/0.18 mid 16.0%, model 21.1% (projection_v2.0 (prediction ledger)) -- gap +5.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT28BORRUU-18` Over 17.5 games: 0.90/0.94 mid 92.0%, model 96.4% (projection_v2.0 (prediction ledger)) -- gap +4.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT28BORRUU-1-BOR` Will Nuno Borges win set 1 in the Nuno Borges vs Casper Ruud match: 0.38/0.41 mid 39.5%, model 43.1% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT28BORRUU-2-BOR` Will Nuno Borges win set 2 in the Nuno Borges vs Casper Ruud match: 0.37/0.42 mid 39.5%, model 43.1% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT28BORRUU-2-RUU` Will Casper Ruud win set 2 in the Nuno Borges vs Casper Ruud match: 0.58/0.62 mid 60.0%, model 56.9% (projection_v2.0 (prediction ledger)) -- gap -3.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT28BORRUU-1-RUU` Will Casper Ruud win set 1 in the Nuno Borges vs Casper Ruud match: 0.59/0.60 mid 59.5%, model 56.9% (projection_v2.0 (prediction ledger)) -- gap -2.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT28BORRUU-BOR2` Will Nuno Borges win at least 1.5 more games than Casper Ruud?: 0.28/0.32 mid 30.0%, model 31.7% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT28BORRUU-BOR20` Will Nuno Borges win the Nuno Borges vs Casper Ruud match by a set score of 2-0?: 0.18/0.21 mid 19.5%, model 18.5% (projection_v2.0 (prediction ledger)) -- gap -1.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE

## Elizara Yaneva vs Oksana Selekhmeteva -- WTA 125K Courmayeur R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-28 17:00Z
* Current expected start: 2026-10-28 14:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-28 13:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · surface ? · scheduled 2026-10-28T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221407:260664:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oksana Selekhmeteva (`KXWTACHALLENGERMATCH-26OCT28YANSEL-SEL`) | 0.39 / 0.40 (362) | 39.5% | 50.5% | 33.9% | 44.1% [38.4%-57.4%] | 39.1% | 40.0% | 40.0% | MODEL_LONE_OUTLIER | WATCH | +11.1 pp | REVIEW | AGING | A / LIMITED | EXTERNAL_STALE | VERIFIED |
| Elizara Yaneva (`KXWTACHALLENGERMATCH-26OCT28YANSEL-YAN`) | 0.60 / 0.61 (300) | 60.5% | 49.5% | 66.1% | 55.9% [42.6%-61.6%] | 60.9% | 60.3% | 60.3% | MODEL_LONE_OUTLIER | PASS | -11.1 pp | REVIEW | AGING | A / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 2860.0, B 4338.0; serve-point win A 53.7%, B 46.2%; Elo A 1773.9, B 1878.4; model uncertainty 0.095
* Form inputs: days since last match A 12, B 15; matches on record A 110, B 353; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Jakub Filip vs Pavlos Tsitsipas -- M15 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210409:210623:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jakub Filip (`KXITFMATCH-26OCT28FILTSI-FIL`) | 0.76 / 0.79 (301) | 77.5% | 70.8% | 83.6% | 76.8% [70.6%-80.2%] | 76.0% | -- | 76.0% | KALSHI_LONE_OUTLIER | PASS | -6.8 pp | NORMAL | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Pavlos Tsitsipas (`KXITFMATCH-26OCT28FILTSI-TSI`) | 0.23 / 0.24 (65) | 23.5% | 29.2% | 16.4% | 23.2% [19.8%-29.4%] | 24.0% | -- | 24.0% | KALSHI_LONE_OUTLIER | WATCH | +5.8 pp | NORMAL | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1554.0, B 1989.0; serve-point win A 62.7%, B 41.5%; Elo A 1309.2, B 1177.4; model uncertainty 0.0478
* Form inputs: days since last match A 72, B 184; matches on record A 92, B 86; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.016, surface_dev_loose +0.015, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Digvijay Pratap Singh vs Daniel Khazime -- M15 Fergana R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28SINKHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Khazime (`KXITFMATCH-26OCT28SINKHA-KHA`) | -- / 0.01 (164845) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Digvijay Pratap Singh (`KXITFMATCH-26OCT28SINKHA-SIN`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Borna Gojo vs Dino Prizmic -- ATP Challenger Brest R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 14:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-28T14:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:127339:209976:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Borna Gojo (`KXATPCHALLENGERMATCH-26OCT28GOJPRI-GOJ`) | 0.42 / 0.45 (247) | 43.5% | 38.1% | 46.1% | 44.1% [40.3%-46.1%] | 40.1% | 38.5% | 39.3% | MODEL_LONE_OUTLIER | WATCH | -5.4 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Dino Prizmic (`KXATPCHALLENGERMATCH-26OCT28GOJPRI-PRI`) | 0.57 / 0.58 (127) | 57.5% | 61.9% | 53.9% | 55.9% [53.9%-59.7%] | 59.9% | 60.6% | 60.3% | MODEL_LONE_OUTLIER | PASS | +4.4 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3589.0, B 4419.0; serve-point win A 64.3%, B 33.2%; Elo A 1759.4, B 1839.6; model uncertainty 0.0292
* Form inputs: days since last match A 6, B 7; matches on record A 474, B 254; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.019, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Lourdes Ayala vs Jazmin Ortenzi -- WTA 125K Curitiba R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-28 17:30Z
* Current expected start: 2026-10-28 14:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-28 13:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Clay · scheduled 2026-10-28T17:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220446:236968:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lourdes Ayala (`KXWTACHALLENGERMATCH-26OCT28AYAORT-AYA`) | 0.04 / 0.05 (6022) | 4.5% | 3.3% | 2.0% | 4.9% [2.9%-8.2%] | 5.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.2 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jazmin Ortenzi (`KXWTACHALLENGERMATCH-26OCT28AYAORT-ORT`) | 0.95 / 0.96 (7) | 95.5% | 96.7% | 98.0% | 95.1% [91.8%-97.1%] | 95.0% | 96.7% | 96.7% | MODEL_LONE_OUTLIER | PASS | +1.2 pp | NORMAL | AGING | B / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 813.0, B 3121.0; serve-point win A 44.4%, B 41.8%; Elo A 1245.8, B 1679.1; model uncertainty 0.0268
* Form inputs: days since last match A 2, B 2; matches on record A 107, B 366; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.001, surface_pool_high -0.001, surface_dev_loose -0.006, surface_dev_tight +0.007
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE

## Alice Tubello vs Luna Maria Cinalli -- WTA 125K Curitiba R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-28 17:30Z
* Current expected start: 2026-10-28 14:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-28 13:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Clay · scheduled 2026-10-28T17:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220554:260711:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luna Maria Cinalli (`KXWTACHALLENGERMATCH-26OCT28TUBCIN-CIN`) | 0.09 / 0.10 (3979) | 9.5% | 7.1% | 8.5% | 11.8% [10.5%-13.7%] | 11.1% | 9.2% | 10.1% | MODEL_LONE_OUTLIER | WATCH | -2.4 pp | NORMAL | AGING | C / LIMITED | ALL_AGREE | VERIFIED |
| Alice Tubello (`KXWTACHALLENGERMATCH-26OCT28TUBCIN-TUB`) | 0.91 / 0.92 (5645) | 91.5% | 92.8% | 91.5% | 88.2% [86.3%-89.5%] | 88.9% | 91.0% | 89.9% | MODEL_LONE_OUTLIER | PASS | +1.4 pp | NORMAL | AGING | C / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 2580.0, B 795.0; serve-point win A 59.4%, B 51.6%; Elo A 1712.6, B 1389.7; model uncertainty 0.016
* Form inputs: days since last match A 2, B 184; matches on record A 333, B 34; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.014, surface_dev_loose +0.008, surface_dev_tight -0.008
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Felix Balshaw / Matteo Martineau vs Samir Hamza Reguig / Nicolas Ifi -- ATP Challenger Brest R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-28T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28BALMARHAMIFI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felix Balshaw / Matteo Martineau (`KXATPCHALLENGERDOUBLES-26OCT28BALMARHAMIFI-BALMAR`) | 0.93 / 0.95 (1124) | 94.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Samir Hamza Reguig / Nicolas Ifi (`KXATPCHALLENGERDOUBLES-26OCT28BALMARHAMIFI-HAMIFI`) | 0.05 / 0.06 (4845) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Nino Ehrenschneider vs Mario Gonzalez Fernandez -- M25 Malta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208605:209510:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nino Ehrenschneider (`KXITFMATCH-26OCT28EHRGON-EHR`) | 0.59 / 0.60 (9592) | 59.5% | 43.4% | 47.4% | 46.4% [44.3%-47.9%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -16.1 pp | HIGH_REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mario Gonzalez Fernandez (`KXITFMATCH-26OCT28EHRGON-GON`) | 0.40 / 0.41 (3902) | 40.5% | 56.6% | 52.6% | 53.6% [52.1%-55.7%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +16.1 pp | HIGH_REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3493.0, B 2442.0; serve-point win A 57.6%, B 41.1%; Elo A 1374.1, B 1419.2; model uncertainty 0.0182
* Form inputs: days since last match A 184, B 65; matches on record A 129, B 236; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28EHRGON-GON  (YES = Mario Gonzalez Fernandez)
Model: 57%
Kalshi: 40%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.021, surface_dev_loose -0.016, surface_dev_tight +0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Klara Blazkova vs Aleksandra Pozarenko -- W15 Taby R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28BLAPOZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Klara Blazkova (`KXITFWMATCH-26OCT28BLAPOZ-BLA`) | 0.87 / 0.90 (10) | 88.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aleksandra Pozarenko (`KXITFWMATCH-26OCT28BLAPOZ-POZ`) | 0.08 / 0.13 (22) | 10.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Clement Tabur vs Filippo Romano -- ATP Challenger Brest R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 15:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-28T15:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202127:211542:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filippo Romano (`KXATPCHALLENGERMATCH-26OCT28TABROM-ROM`) | 0.27 / 0.28 (647) | 27.5% | 35.2% | 34.2% | 33.3% [32.4%-33.8%] | 28.4% | 27.6% | 28.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +7.7 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Clement Tabur (`KXATPCHALLENGERMATCH-26OCT28TABROM-TAB`) | 0.72 / 0.73 (1217) | 72.5% | 64.8% | 65.8% | 66.7% [66.2%-67.6%] | 71.6% | 72.5% | 72.1% | MODEL_LONE_OUTLIER | PASS | -7.7 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4921.0, B 4268.0; serve-point win A 66.6%, B 36.4%; Elo A 1643.8, B 1503.6; model uncertainty 0.0067
* Form inputs: days since last match A 8, B 9; matches on record A 500, B 168; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.001, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Flavio Cobolli vs Matteo Berrettini -- ATP Vienna R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-28 15:30Z
* Current expected start: 2026-10-28 15:30Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-28 14:45Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-29T04:00:00+00:00 as not a valid time; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Clay · scheduled 2026-10-28T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126610:207925:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Berrettini (`KXATPMATCH-26OCT28COBBER-BER`) | 0.50 / 0.51 (1351) | 50.5% | 51.6% | 49.5% | 49.5% [47.6%-51.9%] | -- | -- | -- | -- | PASS | +1.1 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Flavio Cobolli (`KXATPMATCH-26OCT28COBBER-COB`) | 0.51 / 0.52 (23564) | 51.5% | 48.4% | 50.5% | 50.5% [48.1%-52.4%] | -- | -- | -- | -- | PASS | -3.1 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6575.0, B 4151.0; serve-point win A 66.1%, B 33.6%; Elo A 1972.2, B 1971.4; model uncertainty 0.0219
* Form inputs: days since last match A 4, B 2; matches on record A 454, B 563; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.019, surface_dev_loose +0.019, surface_dev_tight -0.024
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT28COBBER-BER21` Will Matteo Berrettini win the Flavio Cobolli vs Matteo Berrettini match by a set score of 2-1?: 0.01/0.27 mid 14.0%, model 25.5% (projection_v2.0 (prediction ledger)) -- gap +11.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT28COBBER-COB21` Will Flavio Cobolli win the Flavio Cobolli vs Matteo Berrettini match by a set score of 2-1?: 0.01/0.29 mid 15.0%, model 24.4% (projection_v2.0 (prediction ledger)) -- gap +9.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT28COBBER-BER20` Will Matteo Berrettini win the Flavio Cobolli vs Matteo Berrettini match by a set score of 2-0?: 0.01/0.35 mid 18.0%, model 26.1% (projection_v2.0 (prediction ledger)) -- gap +8.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT28COBBER-25` Over 24.5 games: 0.48/0.49 mid 48.5%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap +7.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT28COBBER-COB20` Will Flavio Cobolli win the Flavio Cobolli vs Matteo Berrettini match by a set score of 2-0?: 0.01/0.34 mid 17.5%, model 23.9% (projection_v2.0 (prediction ledger)) -- gap +6.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT28COBBER-30` Over 29.5 games: 0.26/0.32 mid 29.0%, model 35.2% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT28COBBER-20` Over 19.5 games: 0.78/0.82 mid 80.0%, model 84.8% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT28COBBER-BER5` Will Matteo Berrettini win at least 4.5 more games than Flavio Cobolli?: 0.14/0.20 mid 17.0%, model 14.4% (projection_v2.0 (prediction ledger)) -- gap -2.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT28COBBER-COB2` Will Flavio Cobolli win at least 1.5 more games than Matteo Berrettini?: 0.41/0.44 mid 42.5%, model 40.3% (projection_v2.0 (prediction ledger)) -- gap -2.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT28COBBER-2-BER` Will Matteo Berrettini win set 2 in the Flavio Cobolli vs Matteo Berrettini match: 0.05/0.94 mid 49.5%, model 51.1% (projection_v2.0 (prediction ledger)) -- gap +1.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT28COBBER-1-COB` Will Flavio Cobolli win set 1 in the Flavio Cobolli vs Matteo Berrettini match: 0.47/0.52 mid 49.5%, model 48.9% (projection_v2.0 (prediction ledger)) -- gap -0.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT28COBBER-2-COB` Will Flavio Cobolli win set 2 in the Flavio Cobolli vs Matteo Berrettini match: 0.05/0.94 mid 49.5%, model 48.9% (projection_v2.0 (prediction ledger)) -- gap -0.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT28COBBER-BER2` Will Matteo Berrettini win at least 1.5 more games than Flavio Cobolli?: 0.43/0.45 mid 44.0%, model 43.5% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT28COBBER-1-BER` Will Matteo Berrettini win set 1 in the Flavio Cobolli vs Matteo Berrettini match: 0.49/0.53 mid 51.0%, model 51.1% (projection_v2.0 (prediction ledger)) -- gap +0.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jakub Mensik vs Adrian Mannarino -- ATP Vienna R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-28 17:50Z
* Current expected start: 2026-10-28 15:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-28 14:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-140_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Clay · scheduled 2026-10-28T17:50:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105173:210150:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Mannarino (`KXATPMATCH-26OCT28MENMAN-MAN`) | 0.18 / 0.19 (24624) | 18.5% | 23.8% | 15.9% | 15.6% [11.5%-22.2%] | 19.1% | 19.1% | 19.1% | MODEL_LONE_OUTLIER | PASS | +5.3 pp | NORMAL | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Jakub Mensik (`KXATPMATCH-26OCT28MENMAN-MEN`) | 0.81 / 0.82 (22860) | 81.5% | 76.2% | 84.1% | 84.4% [77.8%-88.5%] | 80.9% | 81.0% | 80.9% | MODEL_LONE_OUTLIER | WATCH | -5.3 pp | NORMAL | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5142.0, B 5560.0; serve-point win A 66.8%, B 38.9%; Elo A 1903.0, B 1604.2; model uncertainty 0.0536
* Form inputs: days since last match A 189, B 3; matches on record A 251, B 1322; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose +0.041, surface_dev_tight -0.042
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT28MENMAN-MEN20` Will Jakub Mensik win the Jakub Mensik vs Adrian Mannarino match by a set score of 2-0?: 0.58/0.59 mid 58.5%, model 46.6% (projection_v2.0 (prediction ledger)) -- gap -11.9 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data LIMITED
  * `KXATPGSPREAD-26OCT28MENMAN-MEN5` Will Jakub Mensik win at least 4.5 more games than Adrian Mannarino?: 0.45/0.46 mid 45.5%, model 34.9% (projection_v2.0 (prediction ledger)) -- gap -10.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data LIMITED
  * `KXATPGTOTAL-26OCT28MENMAN-23` Over 22.5 games: 0.45/0.46 mid 45.5%, model 54.0% (projection_v2.0 (prediction ledger)) -- gap +8.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
  * `KXATPSETWINNER-26OCT28MENMAN-2-MAN` Will Adrian Mannarino win set 2 in the Jakub Mensik vs Adrian Mannarino match: 0.23/0.26 mid 24.5%, model 31.8% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXATPEXACTMATCH-26OCT28MENMAN-MEN21` Will Jakub Mensik win the Jakub Mensik vs Adrian Mannarino match by a set score of 2-1?: 0.21/0.24 mid 22.5%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
  * `KXATPGSPREAD-26OCT28MENMAN-MEN2` Will Jakub Mensik win at least 1.5 more games than Adrian Mannarino?: 0.75/0.79 mid 77.0%, model 70.0% (projection_v2.0 (prediction ledger)) -- gap -7.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
  * `KXATPGTOTAL-26OCT28MENMAN-28` Over 27.5 games: 0.26/0.30 mid 28.0%, model 34.8% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
  * `KXATPSETWINNER-26OCT28MENMAN-1-MAN` Will Adrian Mannarino win set 1 in the Jakub Mensik vs Adrian Mannarino match: 0.24/0.26 mid 25.0%, model 31.8% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT28MENMAN-1-MEN` Will Jakub Mensik win set 1 in the Jakub Mensik vs Adrian Mannarino match: 0.74/0.76 mid 75.0%, model 68.2% (projection_v2.0 (prediction ledger)) -- gap -6.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT28MENMAN-2-MEN` Will Jakub Mensik win set 2 in the Jakub Mensik vs Adrian Mannarino match: 0.72/0.77 mid 74.5%, model 68.2% (projection_v2.0 (prediction ledger)) -- gap -6.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXATPEXACTMATCH-26OCT28MENMAN-MAN21` Will Adrian Mannarino win the Jakub Mensik vs Adrian Mannarino match by a set score of 2-1?: 0.08/0.10 mid 9.0%, model 13.8% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
  * `KXATPGTOTAL-26OCT28MENMAN-18` Over 17.5 games: 0.83/0.88 mid 85.5%, model 90.3% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
  * `KXATPGSPREAD-26OCT28MENMAN-MEN8` Will Jakub Mensik win at least 7.5 more games than Adrian Mannarino?: 0.06/0.09 mid 7.5%, model 4.6% (projection_v2.0 (prediction ledger)) -- gap -2.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26OCT28MENMAN-MAN20` Will Adrian Mannarino win the Jakub Mensik vs Adrian Mannarino match by a set score of 2-0?: 0.07/0.09 mid 8.0%, model 10.1% (projection_v2.0 (prediction ledger)) -- gap +2.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE

## Linda Klimovicova vs Noma Noha Akugue -- WTA 125K Courmayeur R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-28 18:10Z
* Current expected start: 2026-10-28 15:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-28 14:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · surface ? · scheduled 2026-10-28T18:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221626:223333:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Linda Klimovicova (`KXWTACHALLENGERMATCH-26OCT28KLINOH-KLI`) | 0.42 / 0.43 (769) | 42.5% | 45.7% | 44.3% | 46.4% [45.8%-48.4%] | -- | 41.4% | 41.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +3.2 pp | NORMAL | AGING | A / LIMITED | ALL_AGREE | VERIFIED |
| Noma Noha Akugue (`KXWTACHALLENGERMATCH-26OCT28KLINOH-NOH`) | 0.57 / 0.58 (384) | 57.5% | 54.3% | 55.7% | 53.6% [51.6%-54.2%] | -- | 58.9% | 58.9% | MODEL_LONE_OUTLIER | PASS | -3.2 pp | NORMAL | AGING | A / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 2873.0, B 4975.0; serve-point win A 57.8%, B 41.3%; Elo A 1759.0, B 1749.0; model uncertainty 0.013
* Form inputs: days since last match A 16, B 15; matches on record A 261, B 345; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE

## Gabriela Knutson vs Alina Charaeva -- WTA 125K Courmayeur R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-28 17:30Z
* Current expected start: 2026-10-28 15:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-28 14:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · surface ? · scheduled 2026-10-28T17:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT28KNUCHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alina Charaeva (`KXWTACHALLENGERMATCH-26OCT28KNUCHA-CHA`) | 0.62 / 0.63 (709) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gabriela Knutson (`KXWTACHALLENGERMATCH-26OCT28KNUCHA-KNU`) | 0.37 / 0.38 (577) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## John Bothma vs Aaron Funk -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212630:213011:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| John Bothma (`KXITFMATCH-26OCT28BOTFUN-BOT`) | 0.13 / 0.14 (675) | 13.5% | 47.4% | 63.0% | 58.8% [57.9%-59.2%] | -- | -- | -- | -- | PASS | +33.9 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aaron Funk (`KXITFMATCH-26OCT28BOTFUN-FUN`) | 0.85 / 0.86 (1) | 85.5% | 52.6% | 37.0% | 41.2% [40.8%-42.1%] | -- | -- | -- | -- | PASS | -32.9 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 278.0, B 1147.0; serve-point win A 65.5%, B 34.0%; Elo A 1245.5, B 1191.5; model uncertainty 0.0066
* Form inputs: days since last match A 191, B 205; matches on record A 10, B 39; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28BOTFUN-BOT  (YES = John Bothma)
Model: 47%
Kalshi: 14%
Gap: +34 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.001, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sven Corbinais vs Sebastian Heinrich -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211457:214180:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sven Corbinais (`KXITFMATCH-26OCT28CORHEI-COR`) | 0.82 / 0.85 (5) | 83.5% | 39.5% | 22.8% | 41.6% [40.5%-42.7%] | 78.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -44.0 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sebastian Heinrich (`KXITFMATCH-26OCT28CORHEI-HEI`) | 0.14 / 0.16 (1) | 15.0% | 60.5% | 77.2% | 58.4% [57.3%-59.5%] | 21.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +45.5 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 528.0, B 91.0; serve-point win A 54.2%, B 43.8%; Elo A 1204.8, B 1253.5; model uncertainty 0.0109
* Form inputs: days since last match A 247, B 401; matches on record A 24, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28CORHEI-HEI  (YES = Sebastian Heinrich)
Model: 60%
Kalshi: 15%
Gap: +45 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Max Geissinger vs Mahmoud chetouane -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28GEICHE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mahmoud chetouane (`KXITFMATCH-26OCT28GEICHE-CHE`) | 0.39 / 0.40 (5290) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Max Geissinger (`KXITFMATCH-26OCT28GEICHE-GEI`) | 0.60 / 0.61 (6398) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Igor Piasek vs Borys Zgola -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210169:213569:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Igor Piasek (`KXITFMATCH-26OCT28PIAZGO-PIA`) | -- / 0.01 (7895) | -- | 62.0% | 46.4% | 66.9% [66.9%-68.8%] | -- | -- | -- | -- | PASS | -- | UNPRICED | AGING | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Borys Zgola (`KXITFMATCH-26OCT28PIAZGO-ZGO`) | 0.99 / -- (0) | -- | 38.0% | 53.6% | 33.1% [31.2%-33.1%] | -- | -- | -- | -- | PASS | -- | UNPRICED | AGING | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 38.0, B 63.0; serve-point win A 61.7%, B 40.6%; Elo A 1233.0, B 1102.3; model uncertainty 0.0095
* Form inputs: days since last match A 450, B 219; matches on record A 2, B 14; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jay Singh vs Nicolas Garcia Longo -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28SINGAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Garcia Longo (`KXITFMATCH-26OCT28SINGAR-GAR`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jay Singh (`KXITFMATCH-26OCT28SINGAR-SIN`) | -- / 0.01 (195618) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anastasia Gasanova vs Ekaterina Dotsenko -- W50 Istanbul R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28GASDOT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Dotsenko (`KXITFWMATCH-26OCT28GASDOT-DOT`) | 0.70 / 0.71 (364) | 70.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anastasia Gasanova (`KXITFWMATCH-26OCT28GASDOT-GAS`) | 0.29 / 0.30 (8833) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ada Gergec vs Nahjime Dho -- W15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:252572:270164:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nahjime Dho (`KXITFWMATCH-26OCT28GERDHO-DHO`) | 0.59 / 0.60 (9004) | 59.5% | 72.7% | 51.6% | 66.6% [65.7%-67.6%] | 89.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.2 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ada Gergec (`KXITFWMATCH-26OCT28GERDHO-GER`) | 0.40 / 0.41 (14763) | 40.5% | 27.3% | 48.4% | 33.4% [32.4%-34.3%] | 10.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.2 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 67.0, B 464.0; serve-point win A 47.3%, B 48.2%; Elo A 1164.1, B 1287.0; model uncertainty 0.0096
* Form inputs: days since last match A 233, B 303; matches on record A 7, B 9; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cindy Langlais vs Pauline Gloeckner -- W15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:265207:270117:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pauline Gloeckner (`KXITFWMATCH-26OCT28LANGLO-GLO`) | 0.08 / 0.09 (3841) | 8.5% | 25.2% | 24.5% | 38.0% [33.1%-41.5%] | 5.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +16.7 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Cindy Langlais (`KXITFWMATCH-26OCT28LANGLO-LAN`) | 0.91 / 0.92 (4516) | 91.5% | 74.8% | 75.5% | 62.0% [58.5%-66.9%] | 95.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -16.7 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 854.0, B 368.0; serve-point win A 57.6%, B 47.4%; Elo A 1299.2, B 1241.2; model uncertainty 0.0425
* Form inputs: days since last match A 184, B 226; matches on record A 38, B 10; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28LANGLO-GLO  (YES = Pauline Gloeckner)
Model: 25%
Kalshi: 8%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Urszula Radwanska vs Anna Kubareva -- W50 Istanbul R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:201524:215707:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Kubareva (`KXITFWMATCH-26OCT28RADKUB-KUB`) | 0.65 / 0.66 (6575) | 65.5% | 49.5% | 81.9% | 66.1% [48.4%-74.4%] | 63.0% | -- | 63.0% | MODEL_LONE_OUTLIER | PASS | -16.0 pp | HIGH_REVIEW | AGING | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Urszula Radwanska (`KXITFWMATCH-26OCT28RADKUB-RAD`) | 0.34 / 0.35 (6931) | 34.5% | 50.5% | 18.1% | 33.9% [25.6%-51.6%] | 37.0% | -- | 37.0% | KALSHI_LONE_OUTLIER | WATCH | +16.0 pp | HIGH_REVIEW | AGING | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1581.0, B 2121.0; serve-point win A 52.7%, B 47.4%; Elo A 1514.8, B 1482.6; model uncertainty 0.1302
* Form inputs: days since last match A 86, B 205; matches on record A 840, B 345; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28RADKUB-RAD  (YES = Urszula Radwanska)
Model: 50%
Kalshi: 34%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Federico Cina vs Nicolai Budkov Kjaer -- ATP Challenger Brest R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 15:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-28T15:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:149282:210748:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolai Budkov Kjaer (`KXATPCHALLENGERMATCH-26OCT28CINBUD-BUD`) | 0.56 / 0.57 (3699) | 56.5% | 50.4% | 53.0% | 51.5% [50.0%-52.5%] | 55.4% | 56.5% | 56.0% | MODEL_LONE_OUTLIER | PASS | -6.1 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Federico Cina (`KXATPCHALLENGERMATCH-26OCT28CINBUD-CIN`) | 0.43 / 0.44 (1638) | 43.5% | 49.6% | 47.0% | 48.5% [47.5%-50.0%] | 44.6% | 44.1% | 44.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.1 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3861.0, B 4310.0; serve-point win A 63.9%, B 36.0%; Elo A 1695.1, B 1688.0; model uncertainty 0.0124
* Form inputs: days since last match A 9, B 9; matches on record A 174, B 180; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.010, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Daniel Altmaier vs Jiri Lehecka -- ATP Basel R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-28 16:00Z
* Current expected start: 2026-10-28 16:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-28 15:15Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-29T04:00:00+00:00 as not a valid time; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-10-28T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:127157:208103:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Altmaier (`KXATPMATCH-26OCT28ALTLEH-ALT`) | 0.15 / 0.17 (19533) | 16.0% | 19.5% | 14.5% | 16.0% [14.6%-17.4%] | -- | -- | -- | -- | PASS | +3.5 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jiri Lehecka (`KXATPMATCH-26OCT28ALTLEH-LEH`) | 0.83 / 0.85 (3315) | 84.0% | 80.5% | 85.5% | 84.0% [82.6%-85.4%] | -- | -- | -- | -- | PASS | -3.5 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5885.0, B 5638.0; serve-point win A 63.9%, B 29.0%; Elo A 1741.8, B 1980.7; model uncertainty 0.0139
* Form inputs: days since last match A 2, B 5; matches on record A 731, B 459; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.006, surface_dev_loose -0.014, surface_dev_tight +0.014
* Derivatives listed: 6 (GAME_SPREAD, MATCH_WINNER, TOTAL_GAMES); 6 carry a model probability
  * `KXATPGTOTAL-26OCT28ALTLEH-26` Over 25.5 games: 0.33/0.36 mid 34.5%, model 43.2% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT28ALTLEH-21` Over 20.5 games: 0.63/0.65 mid 64.0%, model 70.6% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT28ALTLEH-LEH5` Will Jiri Lehecka win at least 4.5 more games than Daniel Altmaier?: 0.36/0.38 mid 37.0%, model 32.0% (projection_v2.0 (prediction ledger)) -- gap -5.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT28ALTLEH-LEH2` Will Jiri Lehecka win at least 1.5 more games than Daniel Altmaier?: 0.76/0.79 mid 77.5%, model 74.2% (projection_v2.0 (prediction ledger)) -- gap -3.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT28ALTLEH-16` Over 15.5 games: 0.96/0.99 mid 97.5%, model 99.0% (projection_v2.0 (prediction ledger)) -- gap +1.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE

## Leyre Romero Gormaz vs Antonia Vergara Rivera -- WTA 125K Curitiba R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-28 18:40Z
* Current expected start: 2026-10-28 16:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-28 15:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Clay · scheduled 2026-10-28T18:40:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220742:254733:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leyre Romero Gormaz (`KXWTACHALLENGERMATCH-26OCT28ROMVER-ROM`) | 0.93 / 0.94 (106) | 93.5% | 83.4% | 57.5% | 64.2% [60.6%-72.2%] | 91.4% | 93.5% | 92.5% | MODEL_LONE_OUTLIER | PASS | -10.1 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Antonia Vergara Rivera (`KXWTACHALLENGERMATCH-26OCT28ROMVER-VER`) | 0.06 / 0.07 (2600) | 6.5% | 16.6% | 42.5% | 35.8% [27.8%-39.4%] | 8.6% | 6.3% | 7.5% | MODEL_LONE_OUTLIER | WATCH | +10.1 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4018.0, B 3116.0; serve-point win A 55.2%, B 52.0%; Elo A 1738.0, B 1528.1; model uncertainty 0.0582
* Form inputs: days since last match A 2, B 46; matches on record A 427, B 98; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE

## Federico Arnaboldi vs Wojciech Marek -- M15 Selva Gardena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206467:207457:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Federico Arnaboldi (`KXITFMATCH-26OCT28ARNMAR-ARN`) | 0.66 / 0.68 (180) | 67.0% | 70.0% | 75.7% | 61.2% [52.0%-70.1%] | 61.5% | -- | 61.5% | ALL_THREE_DISAGREE | PASS | +3.0 pp | NORMAL | AGING | F / POOR | EXTERNAL_OUTLIER | AMBIGUOUS |
| Wojciech Marek (`KXITFMATCH-26OCT28ARNMAR-MAR`) | 0.32 / 0.34 (1575) | 33.0% | 30.0% | 24.3% | 38.8% [29.9%-47.9%] | 38.5% | -- | 38.5% | ALL_THREE_DISAGREE | PASS | -3.0 pp | NORMAL | AGING | F / POOR | EXTERNAL_OUTLIER | AMBIGUOUS |

* Serve evidence (points): A 3466.0, B 160.0; serve-point win A 62.5%, B 41.6%; Elo A 1392.6, B 1326.2; model uncertainty 0.0904
* Form inputs: days since last match A 30, B 1549; matches on record A 335, B 84; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.090, surface_pool_high -0.091, surface_dev_loose -0.000, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matthew Asciak vs Vladyslav Orlov -- M25 Malta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105536:200550:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthew Asciak (`KXITFMATCH-26OCT28ASCORL-ASC`) | 0.05 / 0.07 (749) | 6.0% | 16.6% | 40.7% | 24.1% [19.5%-28.3%] | 13.8% | -- | 13.8% | KALSHI_LONE_OUTLIER | PASS | +10.6 pp | REVIEW | AGING | F / POOR | AGREES_WITH_MODEL | VERIFIED |
| Vladyslav Orlov (`KXITFMATCH-26OCT28ASCORL-ORL`) | 0.92 / 0.95 (1702) | 93.5% | 83.4% | 59.3% | 75.9% [71.7%-80.5%] | 86.2% | -- | 86.2% | KALSHI_LONE_OUTLIER | PASS | -10.1 pp | REVIEW | AGING | F / POOR | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 60.0, B 3570.0; serve-point win A 55.2%, B 37.3%; Elo A 1187.8, B 1391.2; model uncertainty 0.0441
* Form inputs: days since last match A 366, B 184; matches on record A 30, B 550; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.039, surface_pool_high +0.042, surface_dev_loose +0.008, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Asylkozhaev / Bessonov vs Omarkhanov / Shin -- M15 Fergana R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28ASYBESOMASHI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Asylkozhaev / Bessonov (`KXITFDOUBLES-26OCT28ASYBESOMASHI-ASYBES`) | 0.52 / 0.66 (10) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Omarkhanov / Shin (`KXITFDOUBLES-26OCT28ASYBESOMASHI-OMASHI`) | 0.34 / 0.45 (44) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Brand / Sadzik vs Bieldiugin / Mashtakov -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28BRASADBIEMAS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bieldiugin / Mashtakov (`KXITFDOUBLES-26OCT28BRASADBIEMAS-BIEMAS`) | 0.04 / 0.83 (18) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Brand / Sadzik (`KXITFDOUBLES-26OCT28BRASADBIEMAS-BRASAD`) | 0.10 / 0.91 (2) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alberto Bronzetti vs Alex Blanchar -- M25 Malta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208216:211715:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Blanchar (`KXITFMATCH-26OCT28BROBLA-BLA`) | 0.04 / 0.47 (2) | 25.5% | 29.8% | 43.3% | 49.0% [47.9%-51.0%] | 24.7% | -- | 24.7% | KALSHI_LONE_OUTLIER | PASS | +4.3 pp | NORMAL | AGING | F / POOR | AGREES_WITH_KALSHI | AMBIGUOUS |
| Alberto Bronzetti (`KXITFMATCH-26OCT28BROBLA-BRO`) | 0.50 / 0.88 (1) | 69.0% | 70.2% | 56.7% | 51.0% [49.0%-52.1%] | 75.3% | -- | 75.3% | KALSHI_LONE_OUTLIER | PASS | +1.2 pp | NORMAL | AGING | F / POOR | EXTERNAL_OUTLIER | AMBIGUOUS |

* Serve evidence (points): A 922.0, B 0.0; serve-point win A 60.7%, B 43.3%; Elo A 1273.3, B 1269.3; model uncertainty 0.0156
* Form inputs: days since last match A 212, B 1458; matches on record A 54, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.021, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Caripi / Longwe-Smit vs Hopp / Thomson -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28CARLONHOPTHO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Caripi / Longwe-Smit (`KXITFDOUBLES-26OCT28CARLONHOPTHO-CARLON`) | 0.03 / 0.91 (2) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hopp / Thomson (`KXITFDOUBLES-26OCT28CARLONHOPTHO-HOPTHO`) | 0.04 / 0.81 (10) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Cherie Ligniere / Farkxodov vs Burtsev / Filaretov -- M15 Fergana R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28CHEFARBURFIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Burtsev / Filaretov (`KXITFDOUBLES-26OCT28CHEFARBURFIL-BURFIL`) | 0.65 / 0.97 (5) | 81.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cherie Ligniere / Farkxodov (`KXITFDOUBLES-26OCT28CHEFARBURFIL-CHEFAR`) | 0.02 / 0.20 (7) | 11.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Davide Ciaschetti vs Lorenzo Bocchi -- M15 Selva Gardena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28CIABOC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Bocchi (`KXITFMATCH-26OCT28CIABOC-BOC`) | 0.98 / 0.99 (541) | 98.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Davide Ciaschetti (`KXITFMATCH-26OCT28CIABOC-CIA`) | 0.01 / 0.02 (5484) | 1.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Duhan / Murtaza vs Krivoshchekov / Serazhetdinov -- M15 Fergana R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28DUHMURKRISER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Duhan / Murtaza (`KXITFDOUBLES-26OCT28DUHMURKRISER-DUHMUR`) | 0.98 / 0.99 (1035) | 98.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Krivoshchekov / Serazhetdinov (`KXITFDOUBLES-26OCT28DUHMURKRISER-KRISER`) | -- / 0.05 (233) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE

## Matthew Howse vs Leyton Rivera -- M25 Malta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28HOWRIV:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthew Howse (`KXITFMATCH-26OCT28HOWRIV-HOW`) | 0.07 / 0.08 (3849) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leyton Rivera (`KXITFMATCH-26OCT28HOWRIV-RIV`) | 0.92 / 0.93 (7000) | 92.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jones / Jones vs Kozlovsky / Rat -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28JONJONKOZRAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jones / Jones (`KXITFDOUBLES-26OCT28JONJONKOZRAT-JONJON`) | 0.03 / 0.91 (2) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kozlovsky / Rat (`KXITFDOUBLES-26OCT28JONJONKOZRAT-KOZRAT`) | 0.03 / 0.91 (7) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mae Malige vs Roan Jones -- M25 Sheffield R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210422:211898:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Roan Jones (`KXITFMATCH-26OCT28MALJON-JON`) | 0.78 / 0.79 (8264) | 78.5% | 14.2% | 25.0% | 22.1% [19.8%-23.3%] | 37.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -64.3 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mae Malige (`KXITFMATCH-26OCT28MALJON-MAL`) | 0.21 / 0.22 (553) | 21.5% | 85.8% | 75.0% | 77.9% [76.7%-80.2%] | 62.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +64.3 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2579.0, B 195.0; serve-point win A 60.2%, B 47.9%; Elo A 1450.4, B 1224.8; model uncertainty 0.0177
* Form inputs: days since last match A 51, B 443; matches on record A 139, B 6; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28MALJON-MAL  (YES = Mae Malige)
Model: 86%
Kalshi: 22%
Gap: +64 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.012, surface_pool_high +0.015, surface_dev_loose +0.008, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mathieu Scaglia vs Daniel Masur -- M25 Malta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:109054:200289:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Masur (`KXITFMATCH-26OCT28SCAMAS-MAS`) | 0.65 / 0.66 (8630) | 65.5% | 81.7% | 82.6% | 82.3% [79.2%-86.4%] | 91.5% | -- | 91.5% | KALSHI_LONE_OUTLIER | PASS | +16.2 pp | HIGH_REVIEW | AGING | C / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Mathieu Scaglia (`KXITFMATCH-26OCT28SCAMAS-SCA`) | 0.34 / 0.35 (3905) | 34.5% | 18.3% | 17.4% | 17.7% [13.6%-20.8%] | 8.5% | -- | 8.5% | KALSHI_LONE_OUTLIER | WATCH | -16.2 pp | HIGH_REVIEW | AGING | C / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 1056.0, B 4231.0; serve-point win A 58.5%, B 34.4%; Elo A 1291.9, B 1563.3; model uncertainty 0.0362
* Form inputs: days since last match A 268, B 37; matches on record A 108, B 772; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28SCAMAS-MAS  (YES = Daniel Masur)
Model: 82%
Kalshi: 66%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: SUPPORTS_MODEL_DIRECTION
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.031, surface_pool_high +0.031, surface_dev_loose +0.001, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Petros Tsitsipas vs Georgii Kravchenko -- M25 Malta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202065:206662:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Georgii Kravchenko (`KXITFMATCH-26OCT28TSIKRA-KRA`) | 0.87 / 0.88 (4858) | 87.5% | 79.2% | 91.3% | 85.9% [79.5%-89.0%] | 89.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -8.3 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Petros Tsitsipas (`KXITFMATCH-26OCT28TSIKRA-TSI`) | 0.12 / 0.13 (6143) | 12.5% | 20.8% | 8.7% | 14.1% [10.9%-20.5%] | 11.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.3 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2371.0, B 3083.0; serve-point win A 57.6%, B 36.0%; Elo A 1270.9, B 1444.6; model uncertainty 0.0478
* Form inputs: days since last match A 191, B 16; matches on record A 165, B 390; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.012, surface_dev_loose -0.006, surface_dev_tight +0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Uzhylovskyi / Ho Yap vs Chang / Taguchi -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28UZHHOYCHATAG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chang / Taguchi (`KXITFDOUBLES-26OCT28UZHHOYCHATAG-CHATAG`) | 0.90 / 0.96 (1) | 93.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Uzhylovskyi / Ho Yap (`KXITFDOUBLES-26OCT28UZHHOYCHATAG-UZHHOY`) | 0.03 / 0.06 (7) | 4.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Isabella Angelina Abendroth vs Emma Sophie Glaser -- W15 Essen R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28ABEGLA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isabella Angelina Abendroth (`KXITFWMATCH-26OCT28ABEGLA-ABE`) | 0.63 / 0.68 (36) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Emma Sophie Glaser (`KXITFWMATCH-26OCT28ABEGLA-GLA`) | 0.31 / 0.34 (3) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nahia Berecoechea vs Oceane Babel -- W75 Poitiers R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221746:222171:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oceane Babel (`KXITFWMATCH-26OCT28BERBAB-BAB`) | 0.05 / 0.08 (54) | 6.5% | 23.4% | 35.8% | 35.3% [31.0%-38.9%] | 34.3% | -- | 34.3% | MODEL_LONE_OUTLIER | WATCH | +16.9 pp | HIGH_REVIEW | AGING | B / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Nahia Berecoechea (`KXITFWMATCH-26OCT28BERBAB-BER`) | 0.92 / 0.95 (2) | 93.5% | 76.6% | 64.2% | 64.7% [61.1%-69.0%] | 65.7% | -- | 65.7% | MODEL_LONE_OUTLIER | PASS | -16.9 pp | HIGH_REVIEW | AGING | B / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 1894.0, B 1826.0; serve-point win A 54.3%, B 51.1%; Elo A 1547.8, B 1437.7; model uncertainty 0.0396
* Form inputs: days since last match A 198, B 184; matches on record A 250, B 160; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28BERBAB-BAB  (YES = Oceane Babel)
Model: 23%
Kalshi: 6%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: SUPPORTS_MODEL_DIRECTION
Data quality: B (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.044, surface_dev_tight -0.035
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kate Bierhoff vs Weronika Ewald -- W35 Malta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260541:269798:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kate Bierhoff (`KXITFWMATCH-26OCT28BIEEWA-BIE`) | 0.04 / 0.05 (6039) | 4.5% | 2.9% | 14.6% | 13.4% [12.1%-14.9%] | 7.2% | -- | 7.2% | KALSHI_LONE_OUTLIER | PASS | -1.6 pp | NORMAL | AGING | F / POOR | ALL_AGREE | VERIFIED |
| Weronika Ewald (`KXITFWMATCH-26OCT28BIEEWA-EWA`) | 0.95 / 0.96 (5559) | 95.5% | 97.2% | 85.4% | 86.6% [85.1%-87.9%] | 92.8% | -- | 92.8% | KALSHI_LONE_OUTLIER | PASS | +1.6 pp | NORMAL | AGING | F / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 123.0, B 2476.0; serve-point win A 46.6%, B 39.1%; Elo A 1272.3, B 1594.6; model uncertainty 0.0142
* Form inputs: days since last match A 429, B 184; matches on record A 5, B 129; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.015, surface_dev_loose -0.003, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vladlena Bokova vs Venla Ahti -- W15 Taby R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28BOKAHT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Venla Ahti (`KXITFWMATCH-26OCT28BOKAHT-AHT`) | 0.34 / 0.53 (3) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vladlena Bokova (`KXITFWMATCH-26OCT28BOKAHT-BOK`) | 0.42 / 0.58 (3) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rikke De Koning vs Sara Saad -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28DEKSAA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rikke De Koning (`KXITFWMATCH-26OCT28DEKSAA-DEK`) | 0.92 / 0.93 (5) | 92.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sara Saad (`KXITFWMATCH-26OCT28DEKSAA-SAA`) | 0.07 / 0.08 (610) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Polina Kuharenko vs Alisa Vasileva -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:252519:263626:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Kuharenko (`KXITFWMATCH-26OCT28KUHVAS-KUH`) | 0.85 / 0.88 (5) | 86.5% | 90.1% | 93.1% | 87.0% [79.9%-90.5%] | -- | -- | -- | -- | PASS | +3.6 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alisa Vasileva (`KXITFWMATCH-26OCT28KUHVAS-VAS`) | 0.12 / 0.15 (114) | 13.5% | 9.9% | 6.9% | 13.0% [9.5%-20.1%] | -- | -- | -- | -- | PASS | -3.6 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1767.0, B 965.0; serve-point win A 60.4%, B 49.4%; Elo A 1462.7, B 1206.1; model uncertainty 0.0529
* Form inputs: days since last match A 233, B 268; matches on record A 55, B 124; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.003, surface_dev_loose +0.016, surface_dev_tight -0.017
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Iva Marinkovic vs Maileen Nuudi -- W15 Taby R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216119:267845:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iva Marinkovic (`KXITFWMATCH-26OCT28MARNUU-MAR`) | 0.46 / 0.47 (6111) | 46.5% | 40.9% | 36.0% | 42.6% [40.1%-46.3%] | 37.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.6 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maileen Nuudi (`KXITFWMATCH-26OCT28MARNUU-NUU`) | 0.54 / 0.55 (9948) | 54.5% | 59.1% | 64.0% | 57.4% [53.7%-59.9%] | 62.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.6 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 542.0, B 207.0; serve-point win A 55.5%, B 42.8%; Elo A 1321.3, B 1363.9; model uncertainty 0.0312
* Form inputs: days since last match A 184, B 184; matches on record A 17, B 244; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.026, surface_pool_high +0.037, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Angelica Raggi vs Lucie Petruzelova -- W35 Malta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216051:221219:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucie Petruzelova (`KXITFWMATCH-26OCT28RAGPET-PET`) | 0.41 / 0.56 (1) | 48.5% | 20.8% | 25.1% | 23.5% [22.7%-25.6%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -27.8 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Angelica Raggi (`KXITFWMATCH-26OCT28RAGPET-RAG`) | 0.49 / 0.53 (1) | 51.0% | 79.2% | 74.9% | 76.5% [74.4%-77.3%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +28.2 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2349.0, B 1518.0; serve-point win A 55.8%, B 50.3%; Elo A 1503.9, B 1281.7; model uncertainty 0.0147
* Form inputs: days since last match A 191, B 198; matches on record A 320, B 141; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28RAGPET-RAG  (YES = Angelica Raggi)
Model: 79%
Kalshi: 51%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.008, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alisa Ziatdinova vs Kristina Belkova -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:269937:270317:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kristina Belkova (`KXITFWMATCH-26OCT28ZIABEL-BEL`) | 0.55 / 0.56 (4531) | 55.5% | 40.5% | 24.7% | 37.9% [35.9%-39.5%] | -- | -- | -- | -- | PASS | -15.0 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alisa Ziatdinova (`KXITFWMATCH-26OCT28ZIABEL-ZIA`) | 0.44 / 0.45 (4760) | 44.5% | 59.5% | 75.3% | 62.1% [60.6%-64.1%] | -- | -- | -- | -- | PASS | +15.0 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 165.0, B 614.0; serve-point win A 53.7%, B 48.1%; Elo A 1269.4, B 1196.6; model uncertainty 0.0179
* Form inputs: days since last match A 338, B 219; matches on record A 3, B 16; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arda Azkara vs Volodymyr Iakubenko -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207907:212246:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arda Azkara (`KXITFMATCH-26OCT28AZKIAK-AZK`) | 0.72 / 0.73 (100) | 72.5% | 61.3% | 58.5% | 63.4% [61.9%-65.3%] | -- | -- | -- | -- | PASS | -11.2 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Volodymyr Iakubenko (`KXITFMATCH-26OCT28AZKIAK-IAK`) | 0.23 / 0.29 (100) | 26.0% | 38.7% | 41.5% | 36.6% [34.7%-38.1%] | -- | -- | -- | -- | WATCH | +12.7 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1640.0, B 1388.0; serve-point win A 63.8%, B 38.5%; Elo A 1428.4, B 1301.7; model uncertainty 0.017
* Form inputs: days since last match A 86, B 191; matches on record A 90, B 47; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.005, surface_dev_loose +0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Joaquin Benoit vs Pieter De Lange -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28BENDEL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joaquin Benoit (`KXITFMATCH-26OCT28BENDEL-BEN`) | 0.17 / 0.29 (6) | 23.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pieter De Lange (`KXITFMATCH-26OCT28BENDEL-DEL`) | 0.71 / 0.80 (6) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matisse Bobichon vs Otto Virtanen -- ATP Challenger Brest R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-28T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202261:212969:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matisse Bobichon (`KXATPCHALLENGERMATCH-26OCT28BOBVIR-BOB`) | 0.15 / 0.17 (4272) | 16.0% | 13.5% | 16.6% | 14.8% [12.6%-16.6%] | 17.1% | 16.1% | 16.6% | MODEL_LONE_OUTLIER | PASS | -2.5 pp | NORMAL | AGING | B / ADEQUATE | ALL_AGREE | VERIFIED |
| Otto Virtanen (`KXATPCHALLENGERMATCH-26OCT28BOBVIR-VIR`) | 0.84 / 0.85 (13882) | 84.5% | 86.5% | 83.4% | 85.2% [83.4%-87.4%] | 82.9% | 84.1% | 83.5% | MARKETS_AGREE | PASS | +2.0 pp | NORMAL | AGING | B / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 1900.0, B 5215.0; serve-point win A 62.0%, B 28.9%; Elo A 1441.6, B 1772.7; model uncertainty 0.02
* Form inputs: days since last match A 16, B 10; matches on record A 65, B 433; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.017, surface_dev_loose -0.005, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## CHARLES CHEN vs Lilian Marmousez -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208421:212465:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CHARLES CHEN (`KXITFMATCH-26OCT28CHEMAR-CHE`) | 0.05 / 0.07 (1) | 6.0% | 12.1% | 7.4% | 8.9% [7.2%-11.6%] | 10.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +6.1 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lilian Marmousez (`KXITFMATCH-26OCT28CHEMAR-MAR`) | 0.92 / 0.95 (12) | 93.5% | 87.9% | 92.6% | 91.1% [88.4%-92.8%] | 89.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.6 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1264.0, B 2574.0; serve-point win A 57.2%, B 33.6%; Elo A 1191.2, B 1554.5; model uncertainty 0.0219
* Form inputs: days since last match A 198, B 156; matches on record A 48, B 272; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.017, surface_pool_high +0.027, surface_dev_loose +0.002, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tuncay Duran vs Andrea Bacaloni -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210513:211407:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea Bacaloni (`KXITFMATCH-26OCT28DURBAC-BAC`) | 0.08 / 0.18 (15) | 13.0% | 12.7% | 10.1% | 14.8% [10.9%-20.2%] | 15.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.3 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tuncay Duran (`KXITFMATCH-26OCT28DURBAC-DUR`) | 0.69 / 0.93 (3) | 81.0% | 87.3% | 89.9% | 85.2% [79.8%-89.0%] | 84.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.3 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2111.0, B 858.0; serve-point win A 64.3%, B 44.5%; Elo A 1429.3, B 1169.8; model uncertainty 0.0464
* Form inputs: days since last match A 86, B 226; matches on record A 111, B 103; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.012, surface_pool_high +0.012, surface_dev_loose +0.004, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Louis Larue vs Liam Gavrielides -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209887:211646:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liam Gavrielides (`KXITFMATCH-26OCT28LARGAV-GAV`) | 0.88 / 0.91 (1158) | 89.5% | 74.8% | 87.8% | 75.8% [66.6%-80.7%] | 86.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -14.7 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Louis Larue (`KXITFMATCH-26OCT28LARGAV-LAR`) | 0.09 / 0.12 (1315) | 10.5% | 25.2% | 12.2% | 24.2% [19.3%-33.4%] | 13.3% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +14.7 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1651.0, B 1215.0; serve-point win A 57.2%, B 37.7%; Elo A 1266.6, B 1347.7; model uncertainty 0.0707
* Form inputs: days since last match A 198, B 184; matches on record A 45, B 143; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.025, surface_dev_loose -0.023, surface_dev_tight +0.025
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Fnu Nidunjianzan vs Giovanni Ciocca -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210473:214317:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giovanni Ciocca (`KXITFMATCH-26OCT28NIDCIO-CIO`) | 0.05 / 0.14 (155) | 9.5% | 28.9% | 33.1% | 31.8% [30.9%-32.7%] | 15.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +19.4 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Fnu Nidunjianzan (`KXITFMATCH-26OCT28NIDCIO-NID`) | 0.84 / 0.90 (100) | 87.0% | 71.0% | 66.8% | 68.2% [67.3%-69.1%] | 84.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.9 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 348.0, B 297.0; serve-point win A 63.3%, B 41.0%; Elo A 1320.7, B 1185.9; model uncertainty 0.0091
* Form inputs: days since last match A 39, B 184; matches on record A 60, B 6; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28NIDCIO-CIO  (YES = Giovanni Ciocca)
Model: 29%
Kalshi: 10%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Toufik Sahtali vs Daniil Varaksa -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200086:214446:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Toufik Sahtali (`KXITFMATCH-26OCT28SAHVAR-SAH`) | 0.99 / -- (0) | -- | 79.1% | 82.2% | 70.1% [69.1%-71.0%] | 95.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | AGING | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Daniil Varaksa (`KXITFMATCH-26OCT28SAHVAR-VAR`) | -- / 0.01 (3199) | -- | 20.9% | 17.8% | 29.9% [29.0%-30.9%] | 4.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | AGING | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 3339.0, B 62.0; serve-point win A 60.0%, B 46.2%; Elo A 1404.3, B 1261.0; model uncertainty 0.0094
* Form inputs: days since last match A 184, B 240; matches on record A 92, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marat Salbiev vs Oskari Eerola -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210601:214324:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oskari Eerola (`KXITFMATCH-26OCT28SALEER-EER`) | 0.21 / 0.22 (3129) | 21.5% | 34.7% | 33.2% | 33.7% [32.9%-33.8%] | -- | -- | -- | -- | PASS | +13.2 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marat Salbiev (`KXITFMATCH-26OCT28SALEER-SAL`) | 0.78 / 0.79 (3608) | 78.5% | 65.3% | 66.8% | 66.3% [66.2%-67.1%] | -- | -- | -- | -- | PASS | -13.2 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 81.0, B 633.0; serve-point win A 58.5%, B 44.5%; Elo A 1259.1, B 1139.7; model uncertainty 0.0045
* Form inputs: days since last match A 338, B 226; matches on record A 1, B 17; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Benito Sanchez Martinez vs Cesar Bouchelaghem -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209917:210726:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cesar Bouchelaghem (`KXITFMATCH-26OCT28SANBOU-BOU`) | 0.15 / 0.16 (520) | 15.5% | 46.8% | 69.1% | 56.6% [49.5%-61.1%] | 46.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +31.3 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Benito Sanchez Martinez (`KXITFMATCH-26OCT28SANBOU-SAN`) | 0.84 / 0.85 (106) | 84.5% | 53.2% | 30.9% | 43.4% [38.9%-50.5%] | 53.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -31.3 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 681.0, B 2340.0; serve-point win A 61.6%, B 39.0%; Elo A 1423.3, B 1431.8; model uncertainty 0.0581
* Form inputs: days since last match A 23, B 184; matches on record A 38, B 80; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28SANBOU-BOU  (YES = Cesar Bouchelaghem)
Model: 47%
Kalshi: 16%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.035, surface_dev_loose -0.020, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yassine Smiej vs Nicolas Tepmahc -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208164:208168:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yassine Smiej (`KXITFMATCH-26OCT28SMITEP-SMI`) | 0.19 / 0.23 (53) | 21.0% | 16.0% | 7.4% | 12.5% [8.6%-20.2%] | 21.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.0 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nicolas Tepmahc (`KXITFMATCH-26OCT28SMITEP-TEP`) | 0.77 / 0.83 (1) | 80.0% | 84.0% | 92.6% | 87.5% [79.8%-91.4%] | 78.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.0 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1258.0, B 3348.0; serve-point win A 48.6%, B 44.0%; Elo A 1114.3, B 1365.3; model uncertainty 0.0578
* Form inputs: days since last match A 191, B 184; matches on record A 47, B 237; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.006, surface_pool_high -0.000, surface_dev_loose -0.003, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Benoit Torcq vs Adrien Burdet -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208853:212498:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrien Burdet (`KXITFMATCH-26OCT28TORBUR-BUR`) | 0.37 / 0.57 (3) | 47.0% | 42.8% | 35.9% | 47.9% [44.9%-50.0%] | -- | -- | -- | -- | PASS | -4.2 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Benoit Torcq (`KXITFMATCH-26OCT28TORBUR-TOR`) | 0.38 / 0.61 (1) | 49.5% | 57.2% | 64.1% | 52.1% [50.0%-55.1%] | -- | -- | -- | -- | PASS | +7.7 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 391.0, B 480.0; serve-point win A 60.7%, B 40.7%; Elo A 1158.1, B 1163.6; model uncertainty 0.0257
* Form inputs: days since last match A 184, B 184; matches on record A 20, B 27; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Manon Leonard vs Amandine Hesse -- W75 Poitiers R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:203281:215807:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amandine Hesse (`KXITFWMATCH-26OCT28LEOHES-HES`) | 0.07 / 0.08 (6682) | 7.5% | 42.9% | 31.1% | 35.9% [30.1%-50.5%] | 28.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +35.4 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Manon Leonard (`KXITFWMATCH-26OCT28LEOHES-LEO`) | 0.92 / 0.93 (5195) | 92.5% | 57.1% | 68.9% | 64.1% [49.5%-69.9%] | 72.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -35.4 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3201.0, B 2021.0; serve-point win A 54.7%, B 46.6%; Elo A 1624.9, B 1575.8; model uncertainty 0.1021
* Form inputs: days since last match A 135, B 17; matches on record A 348, B 777; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28LEOHES-HES  (YES = Amandine Hesse)
Model: 43%
Kalshi: 8%
Gap: +35 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.051, surface_pool_high +0.049, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Benjamin Kittay / Takeru Yuzuki vs Martin Damm Jr / Michael Vrbensky -- ATP Challenger Brest R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 16:50Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-28T16:50:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28KITYUZDAMVRB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martin Damm Jr / Michael Vrbensky (`KXATPCHALLENGERDOUBLES-26OCT28KITYUZDAMVRB-DAMVRB`) | 0.47 / 0.50 (28) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Benjamin Kittay / Takeru Yuzuki (`KXATPCHALLENGERDOUBLES-26OCT28KITYUZDAMVRB-KITYUZ`) | 0.48 / 0.51 (19) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Taylor Fritz vs Rinky Hijikata -- ATP Basel R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-27 14:00Z
* Current expected start: 2026-10-28 17:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-28 16:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1620_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-10-27T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126203:208014:2026-10-27`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Taylor Fritz (`KXATPMATCH-26OCT27FRIHIJ-FRI`) | 0.86 / 0.87 (6048) | 86.5% | 81.1% | 88.4% | 86.9% [85.7%-88.1%] | -- | -- | -- | -- | PASS | -5.4 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rinky Hijikata (`KXATPMATCH-26OCT27FRIHIJ-HIJ`) | 0.13 / 0.14 (29903) | 13.5% | 18.9% | 11.6% | 13.1% [11.9%-14.3%] | -- | -- | -- | -- | PASS | +5.4 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6643.0, B 6001.0; serve-point win A 69.5%, B 37.7%; Elo A 2052.9, B 1806.9; model uncertainty 0.0124
* Form inputs: days since last match A 2, B 2; matches on record A 764, B 465; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.003, surface_dev_loose +0.002, surface_dev_tight -0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT27FRIHIJ-FRI8` Will Taylor Fritz win at least 7.5 more games than Rinky Hijikata?: 0.02/0.44 mid 23.0%, model 4.2% (projection_v2.0 (prediction ledger)) -- gap -18.9 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT27FRIHIJ-FRI2` Will Taylor Fritz win at least 1.5 more games than Rinky Hijikata?: 0.36/0.87 mid 61.5%, model 75.3% (projection_v2.0 (prediction ledger)) -- gap +13.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT27FRIHIJ-FRI20` Will Taylor Fritz win the Taylor Fritz vs Rinky Hijikata match by a set score of 2-0?: 0.64/0.66 mid 65.0%, model 52.2% (projection_v2.0 (prediction ledger)) -- gap -12.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT27FRIHIJ-FRI5` Will Taylor Fritz win at least 4.5 more games than Rinky Hijikata?: 0.45/0.46 mid 45.5%, model 36.2% (projection_v2.0 (prediction ledger)) -- gap -9.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT27FRIHIJ-2-FRI` Will Taylor Fritz win set 2 in the Taylor Fritz vs Rinky Hijikata match: 0.47/0.80 mid 63.5%, model 72.2% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT27FRIHIJ-28` Over 27.5 games: 0.21/0.29 mid 25.0%, model 33.7% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT27FRIHIJ-FRI21` Will Taylor Fritz win the Taylor Fritz vs Rinky Hijikata match by a set score of 2-1?: 0.19/0.23 mid 21.0%, model 29.0% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT27FRIHIJ-2-HIJ` Will Rinky Hijikata win set 2 in the Taylor Fritz vs Rinky Hijikata match: 0.19/0.22 mid 20.5%, model 27.8% (projection_v2.0 (prediction ledger)) -- gap +7.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT27FRIHIJ-23` Over 22.5 games: 0.45/0.47 mid 46.0%, model 52.6% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT27FRIHIJ-1-FRI` Will Taylor Fritz win set 1 in the Taylor Fritz vs Rinky Hijikata match: 0.77/0.80 mid 78.5%, model 72.2% (projection_v2.0 (prediction ledger)) -- gap -6.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT27FRIHIJ-1-HIJ` Will Rinky Hijikata win set 1 in the Taylor Fritz vs Rinky Hijikata match: 0.21/0.22 mid 21.5%, model 27.8% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT27FRIHIJ-HIJ21` Will Rinky Hijikata win the Taylor Fritz vs Rinky Hijikata match by a set score of 2-1?: 0.05/0.07 mid 6.0%, model 11.1% (projection_v2.0 (prediction ledger)) -- gap +5.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT27FRIHIJ-18` Over 17.5 games: 0.84/0.88 mid 86.0%, model 90.9% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT27FRIHIJ-HIJ20` Will Rinky Hijikata win the Taylor Fritz vs Rinky Hijikata match by a set score of 2-0?: 0.05/0.07 mid 6.0%, model 7.7% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Daniel Aleksandar Amarandei vs Manuel Plunger -- M15 Selva Gardena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211708:214198:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Aleksandar Amarandei (`KXITFMATCH-26OCT28AMAPLU-AMA`) | 0.18 / 0.20 (3) | 19.0% | 63.0% | 64.3% | 57.3% [55.7%-59.9%] | 21.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +44.0 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Manuel Plunger (`KXITFMATCH-26OCT28AMAPLU-PLU`) | 0.80 / 0.82 (1) | 81.0% | 37.0% | 35.7% | 42.7% [40.1%-44.3%] | 78.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -44.0 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 329.0, B 306.0; serve-point win A 59.4%, B 43.1%; Elo A 1275.8, B 1230.7; model uncertainty 0.0209
* Form inputs: days since last match A 205, B 499; matches on record A 7, B 39; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28AMAPLU-AMA  (YES = Daniel Aleksandar Amarandei)
Model: 63%
Kalshi: 19%
Gap: +44 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Liam Hignett vs Alexis Canter -- M25 Sheffield R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:134545:210723:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexis Canter (`KXITFMATCH-26OCT28HIGCAN-CAN`) | 0.36 / 0.42 (56) | 39.0% | 49.2% | 54.1% | 40.8% [38.8%-43.3%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.2 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Liam Hignett (`KXITFMATCH-26OCT28HIGCAN-HIG`) | 0.51 / 0.62 (1) | 56.5% | 50.8% | 45.9% | 59.2% [56.7%-61.2%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 249.0, B 415.0; serve-point win A 60.1%, B 40.1%; Elo A 1209.4, B 1128.1; model uncertainty 0.0226
* Form inputs: days since last match A 247, B 184; matches on record A 6, B 185; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alex Kobelt vs Maximilian Figl -- M15 Selva Gardena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206895:211904:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maximilian Figl (`KXITFMATCH-26OCT28KOBFIG-FIG`) | 0.46 / 0.48 (46) | 47.0% | 70.0% | 69.2% | 63.8% [61.5%-67.7%] | 48.1% | -- | 48.1% | MODEL_LONE_OUTLIER | PASS | +23.0 pp | HIGH_REVIEW | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Alex Kobelt (`KXITFMATCH-26OCT28KOBFIG-KOB`) | 0.51 / 0.53 (121) | 52.0% | 30.0% | 30.8% | 36.1% [32.3%-38.6%] | 51.9% | -- | 51.9% | MODEL_LONE_OUTLIER | PASS | -22.0 pp | HIGH_REVIEW | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 619.0, B 1358.0; serve-point win A 63.8%, B 32.0%; Elo A 1103.5, B 1191.5; model uncertainty 0.0312
* Form inputs: days since last match A 205, B 184; matches on record A 32, B 60; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28KOBFIG-FIG  (YES = Maximilian Figl)
Model: 70%
Kalshi: 47%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.009, surface_dev_loose -0.008, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jelle Sels vs Viktor Durasovic -- M25 Sheffield R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:125847:126340:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Viktor Durasovic (`KXITFMATCH-26OCT28SELDUR-DUR`) | 0.89 / 0.90 (3768) | 89.5% | 62.3% | 59.0% | 57.5% [55.6%-59.0%] | 61.5% | -- | 61.5% | MODEL_LONE_OUTLIER | PASS | -27.2 pp | EXTREME (DATA_WARNING) | AGING | A / LIMITED | AGREES_WITH_MODEL | VERIFIED |
| Jelle Sels (`KXITFMATCH-26OCT28SELDUR-SEL`) | 0.10 / 0.11 (7541) | 10.5% | 37.8% | 41.0% | 42.5% [41.0%-44.4%] | 38.5% | -- | 38.5% | MODEL_LONE_OUTLIER | WATCH | +27.2 pp | EXTREME (DATA_WARNING) | AGING | A / LIMITED | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 4452.0, B 3973.0; serve-point win A 61.2%, B 36.3%; Elo A 1507.5, B 1544.6; model uncertainty 0.0172
* Form inputs: days since last match A 128, B 16; matches on record A 689, B 730; data quality A

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28SELDUR-SEL  (YES = Jelle Sels)
Model: 38%
Kalshi: 10%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_MODEL
Data quality: A (LIMITED)
Reasons: STALE_PLAYER_DATA, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Julia Avdeeva vs Eliz Maloney -- W75 Glasgow R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216340:222919:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julia Avdeeva (`KXITFWMATCH-26OCT28AVDMAL-AVD`) | 0.69 / 0.70 (59) | 69.5% | 84.3% | 78.2% | 77.0% [71.3%-82.2%] | 80.5% | -- | 80.5% | EXTERNAL_LONE_OUTLIER | PASS | +14.8 pp | REVIEW | AGING | C / LIMITED | AGREES_WITH_MODEL | VERIFIED |
| Eliz Maloney (`KXITFWMATCH-26OCT28AVDMAL-MAL`) | 0.29 / 0.30 (1) | 29.5% | 15.7% | 21.8% | 23.0% [17.8%-28.7%] | 19.5% | -- | 19.5% | EXTERNAL_LONE_OUTLIER | WATCH | -13.8 pp | REVIEW | AGING | C / LIMITED | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 2898.0, B 886.0; serve-point win A 65.4%, B 42.5%; Elo A 1616.2, B 1415.2; model uncertainty 0.0547
* Form inputs: days since last match A 16, B 205; matches on record A 331, B 211; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.047, surface_pool_high -0.058, surface_dev_loose +0.010, surface_dev_tight -0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sophia Biolay vs Emma Slavikova -- W15 Essen R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221192:239126:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sophia Biolay (`KXITFWMATCH-26OCT28BIOSLA-BIO`) | 0.77 / 0.78 (3573) | 77.5% | 81.9% | 87.0% | 80.5% [74.8%-85.5%] | 79.4% | -- | 79.4% | KALSHI_LONE_OUTLIER | PASS | +4.4 pp | NORMAL | AGING | C / LIMITED | ALL_AGREE | VERIFIED |
| Emma Slavikova (`KXITFWMATCH-26OCT28BIOSLA-SLA`) | 0.22 / 0.23 (3235) | 22.5% | 18.1% | 13.0% | 19.6% [14.5%-25.2%] | 20.6% | -- | 20.6% | KALSHI_LONE_OUTLIER | PASS | -4.4 pp | NORMAL | AGING | C / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 766.0, B 1128.0; serve-point win A 56.0%, B 50.8%; Elo A 1461.2, B 1260.0; model uncertainty 0.0535
* Form inputs: days since last match A 254, B 184; matches on record A 133, B 137; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.004, surface_dev_loose +0.011, surface_dev_tight -0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Josy Daems vs Francesca Parcelli -- W15 Essen R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28DAEPAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Josy Daems (`KXITFWMATCH-26OCT28DAEPAR-DAE`) | 0.59 / 0.63 (51) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Francesca Parcelli (`KXITFWMATCH-26OCT28DAEPAR-PAR`) | 0.37 / 0.41 (29) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Drazic / Mattel vs Abanda / Vickery -- W75 Poitiers R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28DRAMATABAVIC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Abanda / Vickery (`KXITFWDOUBLES-26OCT28DRAMATABAVIC-ABAVIC`) | 0.31 / 0.51 (52) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Drazic / Mattel (`KXITFWDOUBLES-26OCT28DRAMATABAVIC-DRAMAT`) | 0.41 / 0.61 (64) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Valentina Steiner vs Mariam Bolkvadze -- W75 Glasgow R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213734:260296:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mariam Bolkvadze (`KXITFWMATCH-26OCT28STEBOL-BOL`) | 0.61 / 0.63 (80) | 62.0% | 83.2% | 61.1% | 70.0% [66.6%-76.1%] | 78.6% | -- | 78.6% | KALSHI_LONE_OUTLIER | PASS | +21.2 pp | HIGH_REVIEW | AGING | B / LIMITED | AGREES_WITH_MODEL | VERIFIED |
| Valentina Steiner (`KXITFWMATCH-26OCT28STEBOL-STE`) | 0.37 / 0.38 (1) | 37.5% | 16.8% | 38.9% | 30.0% [23.9%-33.4%] | 21.4% | -- | 21.4% | KALSHI_LONE_OUTLIER | WATCH | -20.7 pp | HIGH_REVIEW | AGING | B / LIMITED | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 1525.0, B 1814.0; serve-point win A 47.8%, B 45.1%; Elo A 1511.4, B 1733.1; model uncertainty 0.0474
* Form inputs: days since last match A 34, B 20; matches on record A 78, B 553; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28STEBOL-BOL  (YES = Mariam Bolkvadze)
Model: 83%
Kalshi: 62%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_MODEL
Data quality: B (LIMITED)
Reasons: SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.005, surface_dev_loose -0.023, surface_dev_tight +0.019
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anouck Vrancken Peeters vs Elena Malygina -- W75 Glasgow R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216116:259758:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Malygina (`KXITFWMATCH-26OCT28VRAMAL-MAL`) | 0.90 / 0.91 (5435) | 90.5% | 49.1% | 57.4% | 53.2% [50.5%-55.3%] | 71.1% | -- | 71.1% | MODEL_LONE_OUTLIER | PASS | -41.4 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Anouck Vrancken Peeters (`KXITFWMATCH-26OCT28VRAMAL-VRA`) | 0.09 / 0.10 (78) | 9.5% | 50.9% | 42.6% | 46.8% [44.7%-49.5%] | 28.9% | -- | 28.9% | MODEL_LONE_OUTLIER | WATCH | +41.4 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 3125.0, B 2298.0; serve-point win A 56.0%, B 44.2%; Elo A 1645.0, B 1620.4; model uncertainty 0.0237
* Form inputs: days since last match A 191, B 33; matches on record A 236, B 440; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28VRAMAL-VRA  (YES = Anouck Vrancken Peeters)
Model: 51%
Kalshi: 10%
Gap: +41 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: SUPPORTS_MODEL_DIRECTION
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.026, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gabriela CE vs Solana Sierra -- WTA 125K Curitiba R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-28 19:50Z
* Current expected start: 2026-10-28 17:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-28 16:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Clay · scheduled 2026-10-28T19:50:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:206194:221333:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriela CE (`KXWTACHALLENGERMATCH-26OCT28GABSIE-GAB`) | 0.24 / 0.25 (1631) | 24.5% | 14.2% | 27.4% | 23.6% [20.1%-26.1%] | 26.0% | 25.1% | 25.6% | MARKETS_AGREE | PASS | -10.3 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Solana Sierra (`KXWTACHALLENGERMATCH-26OCT28GABSIE-SIE`) | 0.75 / 0.76 (134) | 75.5% | 85.8% | 72.6% | 76.4% [73.9%-79.9%] | 74.0% | 74.9% | 74.5% | MARKETS_AGREE | PASS | +10.3 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2412.0, B 3289.0; serve-point win A 50.6%, B 41.3%; Elo A 1584.9, B 1836.7; model uncertainty 0.0303
* Form inputs: days since last match A 2, B 35; matches on record A 781, B 329; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.012, surface_pool_high +0.025, surface_dev_loose -0.012, surface_dev_tight +0.021
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE

## Oliver Tarvet vs Vladislav Melnic -- M25 Sheffield R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207331:210472:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vladislav Melnic (`KXITFMATCH-26OCT28TARMEL-MEL`) | 0.02 / 0.03 (446) | 2.5% | 4.5% | 6.3% | 5.9% [5.1%-7.4%] | -- | -- | -- | -- | WATCH | +2.0 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oliver Tarvet (`KXITFMATCH-26OCT28TARMEL-TAR`) | 0.97 / 0.98 (3226) | 97.5% | 95.5% | 93.7% | 94.1% [92.6%-94.9%] | -- | -- | -- | -- | PASS | -2.0 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1816.0, B 1486.0; serve-point win A 69.0%, B 44.4%; Elo A 1714.8, B 1225.1; model uncertainty 0.0118
* Form inputs: days since last match A 23, B 198; matches on record A 88, B 80; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.003, surface_dev_loose +0.003, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Joaquin Aguilar Cardozo vs Miguel Tobon -- ATP Challenger Guayaquil R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:101495:212051:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joaquin Aguilar Cardozo (`KXATPCHALLENGERMATCH-26OCT28AGUTOB-AGU`) | 0.62 / 0.63 (401) | 62.5% | 52.6% | 56.8% | 55.2% [54.1%-56.3%] | 62.5% | 61.1% | -- | INSUFFICIENT_INPUTS | PASS | -9.9 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Miguel Tobon (`KXATPCHALLENGERMATCH-26OCT28AGUTOB-TOB`) | 0.38 / 0.39 (2004) | 38.5% | 47.4% | 43.2% | 44.8% [43.7%-45.9%] | 37.5% | 37.0% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +8.9 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2869.0, B 3281.0; serve-point win A 57.8%, B 42.7%; Elo A 1478.1, B 1454.2; model uncertainty 0.0106
* Form inputs: days since last match A 212, B 94; matches on record A 113, B 423; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

## Andres Andrade / Abdullah Shelbayh vs Trey Hilderbrand / Bogdan Pavel -- ATP Challenger Sioux Falls R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28ANDSHEHILPAV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andres Andrade / Abdullah Shelbayh (`KXATPCHALLENGERDOUBLES-26OCT28ANDSHEHILPAV-ANDSHE`) | 0.43 / 0.47 (28) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Trey Hilderbrand / Bogdan Pavel (`KXATPCHALLENGERDOUBLES-26OCT28ANDSHEHILPAV-HILPAV`) | 0.52 / 0.55 (26) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Luca Castagnola vs Jake Fellows -- M15 Selva Gardena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209337:212654:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luca Castagnola (`KXITFMATCH-26OCT28CASFEL-CAS`) | 0.64 / 0.65 (71) | 64.5% | 46.4% | 43.2% | 31.0% [25.7%-34.8%] | 65.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -18.1 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jake Fellows (`KXITFMATCH-26OCT28CASFEL-FEL`) | 0.33 / 0.35 (3) | 34.0% | 53.6% | 56.8% | 69.0% [65.2%-74.3%] | 34.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +19.6 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2820.0, B 104.0; serve-point win A 58.0%, B 41.3%; Elo A 1272.5, B 1422.8; model uncertainty 0.0456
* Form inputs: days since last match A 156, B 184; matches on record A 211, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28CASFEL-FEL  (YES = Jake Fellows)
Model: 54%
Kalshi: 34%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.038, surface_pool_high -0.053, surface_dev_loose -0.000, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## John Chin vs Matt Kuhar -- M15 Pembroke R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208386:210675:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| John Chin (`KXITFMATCH-26OCT28CHIKUH-CHI`) | 0.15 / 0.35 (0) | 25.0% | 21.8% | 33.6% | 31.8% [30.7%-32.7%] | 30.3% | -- | 30.3% | MODEL_LONE_OUTLIER | PASS | -3.2 pp | NORMAL | AGING | D / POOR | EXTERNAL_OUTLIER | VERIFIED |
| Matt Kuhar (`KXITFMATCH-26OCT28CHIKUH-KUH`) | 0.61 / 0.85 (2) | 73.0% | 78.2% | 66.4% | 68.2% [67.3%-69.3%] | 69.7% | -- | 69.7% | MODEL_LONE_OUTLIER | PASS | +5.2 pp | NORMAL | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 154.0, B 2644.0; serve-point win A 53.8%, B 40.2%; Elo A 1119.6, B 1249.2; model uncertainty 0.0101
* Form inputs: days since last match A 65, B 184; matches on record A 24, B 138; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lorenzo Claverie vs Joao Lucas Reis Da Silva -- ATP Challenger Guayaquil R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206307:209936:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Claverie (`KXATPCHALLENGERMATCH-26OCT28CLAREI-CLA`) | 0.19 / 0.20 (852) | 19.5% | 14.9% | 23.5% | 21.8% [20.8%-22.4%] | 22.3% | 20.7% | 21.5% | KALSHI_LONE_OUTLIER | PASS | -4.6 pp | NORMAL | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Joao Lucas Reis Da Silva (`KXATPCHALLENGERMATCH-26OCT28CLAREI-REI`) | 0.80 / 0.81 (6253) | 80.5% | 85.1% | 76.5% | 78.2% [77.6%-79.2%] | 77.7% | 80.0% | 78.9% | MODEL_LONE_OUTLIER | PASS | +4.6 pp | NORMAL | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 547.0, B 5028.0; serve-point win A 63.0%, B 28.3%; Elo A 1425.9, B 1658.1; model uncertainty 0.008
* Form inputs: days since last match A 94, B 23; matches on record A 98, B 480; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high -0.000, surface_dev_loose +0.002, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER

## Jeffrey Fradkin vs Noah Schachter -- M15 Pembroke R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208132:213376:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jeffrey Fradkin (`KXITFMATCH-26OCT28FRASCH-FRA`) | 0.28 / 0.30 (1) | 29.0% | 33.2% | 42.9% | 38.4% [37.0%-39.9%] | 31.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.2 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Noah Schachter (`KXITFMATCH-26OCT28FRASCH-SCH`) | 0.69 / 0.71 (0) | 70.0% | 66.8% | 57.1% | 61.6% [60.1%-63.0%] | 68.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.2 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 804.0, B 2699.0; serve-point win A 59.6%, B 37.0%; Elo A 1145.1, B 1243.3; model uncertainty 0.0146
* Form inputs: days since last match A 184, B 184; matches on record A 13, B 184; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Evan Galea vs Samuel De Felipe Garcia -- M25 Malta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206645:214127:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Samuel De Felipe Garcia (`KXITFMATCH-26OCT28GALDEF-DEF`) | 0.91 / 0.94 (1307) | 92.5% | 52.1% | 73.9% | 39.7% [37.8%-42.7%] | 88.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -40.4 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Evan Galea (`KXITFMATCH-26OCT28GALDEF-GAL`) | 0.06 / 0.08 (159) | 7.0% | 47.9% | 26.1% | 60.3% [57.3%-62.2%] | 11.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +40.9 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 65.0, B 273.0; serve-point win A 58.3%, B 41.3%; Elo A 1203.9, B 1116.2; model uncertainty 0.0245
* Form inputs: days since last match A 366, B 415; matches on record A 2, B 6; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28GALDEF-GAL  (YES = Evan Galea)
Model: 48%
Kalshi: 7%
Gap: +41 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniel Elahi Galan vs Mateo Del Pino -- ATP Challenger Guayaquil R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:123755:210182:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mateo Del Pino (`KXATPCHALLENGERMATCH-26OCT28GALDEL-DEL`) | 0.06 / 0.07 (3614) | 6.5% | 10.9% | 23.4% | 13.2% [7.9%-16.2%] | 6.4% | 7.5% | -- | INSUFFICIENT_INPUTS | WATCH | +4.4 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daniel Elahi Galan (`KXATPCHALLENGERMATCH-26OCT28GALDEL-GAL`) | 0.93 / 0.94 (643) | 93.5% | 89.1% | 76.6% | 86.8% [83.8%-92.1%] | 93.6% | 95.3% | 95.3% | MODEL_LONE_OUTLIER | PASS | -4.4 pp | NORMAL | AGING | C / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5003.0, B 1424.0; serve-point win A 64.1%, B 45.4%; Elo A 1658.2, B 1203.7; model uncertainty 0.0416
* Form inputs: days since last match A 9, B 184; matches on record A 773, B 94; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.011, surface_dev_loose +0.001, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

## Alexis Galarneau / Hans Hach Verdugo vs Charles Barry / Ben Jones -- ATP Challenger Sioux Falls R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28GALHACBARJON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charles Barry / Ben Jones (`KXATPCHALLENGERDOUBLES-26OCT28GALHACBARJON-BARJON`) | 0.05 / 0.95 (217) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexis Galarneau / Hans Hach Verdugo (`KXATPCHALLENGERDOUBLES-26OCT28GALHACBARJON-GALHAC`) | 0.05 / 0.95 (217) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Carel Aubriel Ngounoue vs Richard Mallory -- M15 Pembroke R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28NGOMAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Richard Mallory (`KXITFMATCH-26OCT28NGOMAL-MAL`) | 0.24 / 0.62 (1) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Carel Aubriel Ngounoue (`KXITFMATCH-26OCT28NGOMAL-NGO`) | 0.44 / 0.73 (10) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Giovanni Oradini vs Jacopo Bilardo -- M15 Selva Gardena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132831:211323:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jacopo Bilardo (`KXITFMATCH-26OCT28ORABIL-BIL`) | 0.21 / 0.25 (308) | 23.0% | 22.3% | 20.5% | 20.8% [19.4%-22.4%] | 24.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.7 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Giovanni Oradini (`KXITFMATCH-26OCT28ORABIL-ORA`) | 0.75 / 0.76 (104) | 75.5% | 77.7% | 79.5% | 79.1% [77.6%-80.7%] | 75.3% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +2.2 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2852.0, B 1994.0; serve-point win A 63.2%, B 42.7%; Elo A 1436.6, B 1207.5; model uncertainty 0.0152
* Form inputs: days since last match A 37, B 212; matches on record A 337, B 72; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high +0.000, surface_dev_loose +0.006, surface_dev_tight -0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kacper Szymkowiak vs Kaipo Marshall -- M15 Pembroke R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209868:212852:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kaipo Marshall (`KXITFMATCH-26OCT28SZYMAR-MAR`) | 0.11 / 0.13 (15) | 12.0% | 10.0% | 23.6% | 19.4% [18.3%-20.5%] | 17.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.0 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kacper Szymkowiak (`KXITFMATCH-26OCT28SZYMAR-SZY`) | 0.81 / 0.89 (451) | 85.0% | 90.0% | 76.4% | 80.5% [79.5%-81.7%] | 83.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.0 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1216.0, B 365.0; serve-point win A 63.3%, B 46.6%; Elo A 1370.4, B 1116.1; model uncertainty 0.0111
* Form inputs: days since last match A 233, B 263; matches on record A 41, B 21; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carlos Maria Zarate vs Alan Magadan -- ATP Challenger Guayaquil R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209246:212785:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alan Magadan (`KXATPCHALLENGERMATCH-26OCT28ZARMAG-MAG`) | 0.34 / 0.35 (4890) | 34.5% | 38.5% | 41.3% | 40.3% [38.3%-41.3%] | 37.5% | 36.5% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +4.0 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carlos Maria Zarate (`KXATPCHALLENGERMATCH-26OCT28ZARMAG-ZAR`) | 0.65 / 0.66 (2000) | 65.5% | 61.5% | 58.7% | 59.7% [58.7%-61.7%] | 62.5% | 63.7% | -- | INSUFFICIENT_INPUTS | PASS | -4.0 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2826.0, B 2346.0; serve-point win A 60.9%, B 41.3%; Elo A 1469.0, B 1381.8; model uncertainty 0.015
* Form inputs: days since last match A 9, B 39; matches on record A 87, B 84; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.020, surface_dev_loose +0.000, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

## Esther Adeshina vs Azzurra Cremonini -- W35 Malta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221959:270307:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Esther Adeshina (`KXITFWMATCH-26OCT28ADECRE-ADE`) | 0.97 / 0.98 (627) | 97.5% | 93.7% | 79.6% | 79.6% [79.6%-80.3%] | 90.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Azzurra Cremonini (`KXITFWMATCH-26OCT28ADECRE-CRE`) | 0.02 / 0.03 (381) | 2.5% | 6.3% | 20.4% | 20.4% [19.7%-20.4%] | 9.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3059.0, B 47.0; serve-point win A 59.6%, B 51.9%; Elo A 1488.6, B 1250.4; model uncertainty 0.0039
* Form inputs: days since last match A 126, B 366; matches on record A 115, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.007, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lois Bernstein vs Laetitia Pulchartova -- W15 Taby R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28BERPUL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lois Bernstein (`KXITFWMATCH-26OCT28BERPUL-BER`) | 0.44 / 0.47 (4) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Laetitia Pulchartova (`KXITFWMATCH-26OCT28BERPUL-PUL`) | 0.53 / 0.55 (6) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anastasia Bertacchi vs Alyssa Reguer -- W35 Malta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:234474:264130:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasia Bertacchi (`KXITFWMATCH-26OCT28BERREG-BER`) | 0.58 / 0.73 (27) | 65.5% | 58.0% | 47.9% | 48.9% [47.3%-52.7%] | 64.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.5 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alyssa Reguer (`KXITFWMATCH-26OCT28BERREG-REG`) | 0.33 / 0.42 (228) | 37.5% | 42.0% | 52.1% | 51.1% [47.3%-52.7%] | 35.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.5 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1382.0, B 2738.0; serve-point win A 53.8%, B 47.7%; Elo A 1369.6, B 1371.4; model uncertainty 0.0267
* Form inputs: days since last match A 102, B 184; matches on record A 81, B 233; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.016, surface_dev_loose -0.011, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ana Giraldi Requena vs Maryia Magro -- W35 Malta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216198:270309:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ana Giraldi Requena (`KXITFWMATCH-26OCT28GIRMAG-GIR`) | 0.74 / 0.82 (21) | 78.0% | 63.9% | 33.8% | 49.5% [46.2%-53.2%] | -- | -- | -- | -- | PASS | -14.1 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maryia Magro (`KXITFWMATCH-26OCT28GIRMAG-MAG`) | 0.18 / 0.21 (31) | 19.5% | 36.0% | 66.2% | 50.5% [46.8%-53.8%] | -- | -- | -- | -- | PASS | +16.6 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 883.0, B 165.0; serve-point win A 52.0%, B 50.7%; Elo A 1269.3, B 1259.9; model uncertainty 0.0348
* Form inputs: days since last match A 345, B 317; matches on record A 195, B 3; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28GIRMAG-MAG  (YES = Maryia Magro)
Model: 36%
Kalshi: 20%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.021, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valentini Grammatikopoulou vs Kseniia Ruchkina -- W35 Malta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:204394:270274:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentini Grammatikopoulou (`KXITFWMATCH-26OCT28GRARUC-GRA`) | 0.52 / 0.59 (180) | 55.5% | 60.3% | 56.4% | 62.1% [50.5%-74.9%] | 56.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kseniia Ruchkina (`KXITFWMATCH-26OCT28GRARUC-RUC`) | 0.41 / 0.44 (63) | 42.5% | 39.7% | 43.6% | 37.9% [25.1%-49.5%] | 43.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2942.0, B 507.0; serve-point win A 53.1%, B 48.8%; Elo A 1508.1, B 1408.6; model uncertainty 0.1216
* Form inputs: days since last match A 107, B 331; matches on record A 724, B 10; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.088, surface_pool_high -0.105, surface_dev_loose +0.005, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ella Haavisto vs Katarina Kujovic -- W15 Taby R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216107:268778:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ella Haavisto (`KXITFWMATCH-26OCT28HAAKUJ-HAA`) | 0.62 / 0.66 (3) | 64.0% | 78.2% | 67.5% | 66.0% [63.6%-69.4%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +14.2 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katarina Kujovic (`KXITFWMATCH-26OCT28HAAKUJ-KUJ`) | 0.33 / 0.34 (37) | 33.5% | 21.8% | 32.5% | 34.0% [30.6%-36.4%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.7 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1672.0, B 711.0; serve-point win A 57.3%, B 48.5%; Elo A 1414.5, B 1299.8; model uncertainty 0.0293
* Form inputs: days since last match A 240, B 296; matches on record A 139, B 15; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.033, surface_pool_high -0.025, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Caijsa Wilda Hennemann vs Maja Radenkovic -- W15 Taby R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216385:222041:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Caijsa Wilda Hennemann (`KXITFWMATCH-26OCT28HENRAD-HEN`) | 0.90 / 0.94 (5) | 92.0% | 93.8% | 83.2% | 86.9% [81.1%-90.5%] | -- | -- | -- | -- | PASS | +1.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Maja Radenkovic (`KXITFWMATCH-26OCT28HENRAD-RAD`) | 0.06 / 0.09 (274) | 7.5% | 6.2% | 16.8% | 13.1% [9.6%-18.9%] | -- | -- | -- | -- | PASS | -1.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 2350.0, B 0.0; serve-point win A 59.6%, B 51.9%; Elo A 1608.5, B 1286.2; model uncertainty 0.0469
* Form inputs: days since last match A 184, B 919; matches on record A 313, B 120; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.035, surface_pool_high -0.058, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Martianova vs Zuzanna Bednarz -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:242443:267932:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zuzanna Bednarz (`KXITFWMATCH-26OCT28MARBED-BED`) | 0.72 / 0.76 (142) | 74.0% | 59.1% | 56.9% | 61.6% [59.5%-62.6%] | -- | -- | -- | -- | PASS | -14.9 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Sofia Martianova (`KXITFWMATCH-26OCT28MARBED-MAR`) | 0.26 / 0.28 (78) | 27.0% | 40.9% | 43.1% | 38.4% [37.4%-40.5%] | -- | -- | -- | -- | PASS | +13.9 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1528.0, B 49.0; serve-point win A 53.0%, B 45.3%; Elo A 1262.9, B 1344.5; model uncertainty 0.0153
* Form inputs: days since last match A 184, B 1087; matches on record A 53, B 52; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Samaira Pahwa vs Anja Wildgruber -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222668:270152:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Samaira Pahwa (`KXITFWMATCH-26OCT28PAHWIL-PAH`) | 0.44 / 0.48 (50) | 46.0% | 37.5% | 68.0% | 44.7% [39.5%-50.0%] | -- | -- | -- | -- | PASS | -8.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anja Wildgruber (`KXITFWMATCH-26OCT28PAHWIL-WIL`) | 0.51 / 0.57 (3) | 54.0% | 62.5% | 32.0% | 55.3% [50.0%-60.5%] | -- | -- | -- | -- | PASS | +8.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 110.0, B 2380.0; serve-point win A 53.4%, B 44.2%; Elo A 1255.8, B 1305.7; model uncertainty 0.0526
* Form inputs: days since last match A 191, B 184; matches on record A 3, B 348; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.053, surface_pool_high -0.052, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Victoria Pohle vs Arina Kostina -- W15 Essen R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260433:270226:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arina Kostina (`KXITFWMATCH-26OCT28POHKOS-KOS`) | 0.44 / 0.48 (30) | 46.0% | 31.3% | 61.0% | 45.8% [43.6%-46.8%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -14.7 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Victoria Pohle (`KXITFWMATCH-26OCT28POHKOS-POH`) | 0.52 / 0.57 (494) | 54.5% | 68.7% | 39.0% | 54.2% [53.2%-56.4%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +14.2 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1323.0, B 153.0; serve-point win A 56.3%, B 47.3%; Elo A 1367.6, B 1322.1; model uncertainty 0.0159
* Form inputs: days since last match A 198, B 422; matches on record A 46, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.011, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Viktoriia Sedenkova vs Sara Milanese -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28SEDMIL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Milanese (`KXITFWMATCH-26OCT28SEDMIL-MIL`) | 0.60 / 0.64 (14) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Viktoriia Sedenkova (`KXITFWMATCH-26OCT28SEDMIL-SED`) | 0.37 / 0.41 (81) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Joanna Strzelecka vs Vittoria Paganetti -- W35 Malta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28STRPAG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vittoria Paganetti (`KXITFWMATCH-26OCT28STRPAG-PAG`) | 0.97 / 0.98 (101) | 97.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Joanna Strzelecka (`KXITFWMATCH-26OCT28STRPAG-STR`) | 0.03 / 0.04 (914) | 3.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Antonina Sushkova vs Silvia Alletti -- W35 Malta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:266849:267666:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Silvia Alletti (`KXITFWMATCH-26OCT28SUSALL-ALL`) | 0.01 / 0.02 (2810) | 1.5% | 14.2% | 39.4% | 40.5% [40.5%-40.5%] | 4.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +12.7 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Antonina Sushkova (`KXITFWMATCH-26OCT28SUSALL-SUS`) | 0.98 / 0.99 (7183) | 98.5% | 85.8% | 60.6% | 59.5% [59.5%-59.6%] | 95.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.7 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 527.0, B 45.0; serve-point win A 56.5%, B 51.5%; Elo A 1288.5, B 1220.1; model uncertainty 0.0002
* Form inputs: days since last match A 254, B 415; matches on record A 11, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Federica Urgesi vs Ann Akasha Ceuca -- W35 Malta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223415:261097:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ann Akasha Ceuca (`KXITFWMATCH-26OCT28URGCEU-CEU`) | 0.06 / 0.09 (30) | 7.5% | 24.2% | 52.7% | 45.2% [34.9%-49.5%] | 10.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +16.7 pp | HIGH_REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Federica Urgesi (`KXITFWMATCH-26OCT28URGCEU-URG`) | 0.91 / 0.94 (5) | 92.5% | 75.8% | 47.3% | 54.8% [50.5%-65.1%] | 89.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -16.7 pp | HIGH_REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2635.0, B 2679.0; serve-point win A 55.9%, B 49.3%; Elo A 1586.9, B 1457.1; model uncertainty 0.0729
* Form inputs: days since last match A 37, B 184; matches on record A 169, B 120; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28URGCEU-CEU  (YES = Ann Akasha Ceuca)
Model: 24%
Kalshi: 8%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.016, surface_dev_loose +0.011, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hubert Hurkacz vs Holger Rune -- ATP Basel R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-28 16:00Z
* Current expected start: 2026-10-28 18:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-28 17:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+150_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-10-28T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:128034:208029:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hubert Hurkacz (`KXATPMATCH-26OCT28HURRUN-HUR`) | 0.64 / 0.65 (22444) | 64.5% | 58.0% | 59.4% | 57.1% [56.2%-59.5%] | 63.9% | 64.3% | 64.3% | MODEL_LONE_OUTLIER | PASS | -6.5 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Holger Rune (`KXATPMATCH-26OCT28HURRUN-RUN`) | 0.35 / 0.36 (10302) | 35.5% | 42.0% | 40.6% | 42.9% [40.5%-43.8%] | 36.1% | 36.0% | 36.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.5 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5432.0, B 3079.0; serve-point win A 69.1%, B 32.6%; Elo A 1992.8, B 1965.0; model uncertainty 0.0166
* Form inputs: days since last match A 15, B 2; matches on record A 689, B 446; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.009, surface_dev_loose -0.005, surface_dev_tight +0.009
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT28HURRUN-HUR6` Will Hubert Hurkacz win at least 5.5 more games than Holger Rune?: 0.04/0.35 mid 19.5%, model 6.5% (projection_v2.0 (prediction ledger)) -- gap -13.0 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT28HURRUN-HUR20` Will Hubert Hurkacz win the Hubert Hurkacz vs Holger Rune match by a set score of 2-0?: 0.40/0.42 mid 41.0%, model 30.6% (projection_v2.0 (prediction ledger)) -- gap -10.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT28HURRUN-HUR3` Will Hubert Hurkacz win at least 2.5 more games than Holger Rune?: 0.47/0.49 mid 48.0%, model 39.6% (projection_v2.0 (prediction ledger)) -- gap -8.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT28HURRUN-28` Over 27.5 games: 0.37/0.39 mid 38.0%, model 44.9% (projection_v2.0 (prediction ledger)) -- gap +6.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT28HURRUN-23` Over 22.5 games: 0.60/0.61 mid 60.5%, model 66.8% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT28HURRUN-2-RUN` Will Holger Rune win set 2 in the Hubert Hurkacz vs Holger Rune match: 0.36/0.41 mid 38.5%, model 44.7% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT28HURRUN-RUN21` Will Holger Rune win the Hubert Hurkacz vs Holger Rune match by a set score of 2-1?: 0.15/0.17 mid 16.0%, model 22.1% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT28HURRUN-1-RUN` Will Holger Rune win set 1 in the Hubert Hurkacz vs Holger Rune match: 0.38/0.40 mid 39.0%, model 44.7% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT28HURRUN-1-HUR` Will Hubert Hurkacz win set 1 in the Hubert Hurkacz vs Holger Rune match: 0.60/0.61 mid 60.5%, model 55.3% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT28HURRUN-2-HUR` Will Hubert Hurkacz win set 2 in the Hubert Hurkacz vs Holger Rune match: 0.58/0.63 mid 60.5%, model 55.3% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT28HURRUN-HUR21` Will Hubert Hurkacz win the Hubert Hurkacz vs Holger Rune match by a set score of 2-1?: 0.22/0.24 mid 23.0%, model 27.4% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT28HURRUN-RUN2` Will Holger Rune win at least 1.5 more games than Hubert Hurkacz?: 0.28/0.31 mid 29.5%, model 33.8% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT28HURRUN-18` Over 17.5 games: 0.93/0.96 mid 94.5%, model 96.9% (projection_v2.0 (prediction ledger)) -- gap +2.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT28HURRUN-RUN20` Will Holger Rune win the Hubert Hurkacz vs Holger Rune match by a set score of 2-0?: 0.18/0.21 mid 19.5%, model 20.0% (projection_v2.0 (prediction ledger)) -- gap +0.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Paul Jubb vs Matt Ponchet -- M25 Sheffield R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206703:210328:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Paul Jubb (`KXITFMATCH-26OCT28JUBPON-JUB`) | 0.94 / 0.95 (587) | 94.5% | 86.2% | 86.6% | 87.6% [86.2%-88.4%] | 92.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.3 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matt Ponchet (`KXITFMATCH-26OCT28JUBPON-PON`) | 0.05 / 0.06 (2) | 5.5% | 13.8% | 13.5% | 12.4% [11.6%-13.8%] | 7.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +8.3 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3778.0, B 1205.0; serve-point win A 66.2%, B 42.4%; Elo A 1600.0, B 1253.5; model uncertainty 0.0109
* Form inputs: days since last match A 65, B 233; matches on record A 383, B 56; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.005, surface_dev_loose +0.008, surface_dev_tight -0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maximilian Marterer vs Johannus Monday -- M25 Sheffield R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:109739:208902:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maximilian Marterer (`KXITFMATCH-26OCT28MARMON-MAR`) | 0.40 / 0.41 (42) | 40.5% | 51.0% | 34.5% | 42.3% [36.4%-64.4%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.5 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Johannus Monday (`KXITFMATCH-26OCT28MARMON-MON`) | 0.54 / 0.58 (3) | 56.0% | 49.0% | 65.5% | 57.7% [35.6%-63.6%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.0 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3468.0, B 3169.0; serve-point win A 67.3%, B 33.0%; Elo A 1678.1, B 1617.6; model uncertainty 0.1399
* Form inputs: days since last match A 436, B 65; matches on record A 679, B 179; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.038, surface_pool_high -0.047, surface_dev_loose -0.014, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sophie Bekker vs Ella Seidel -- W75 Glasgow R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:230870:264392:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sophie Bekker (`KXITFWMATCH-26OCT28BEKSEI-BEK`) | 0.05 / 0.06 (39) | 5.5% | 1.1% | 33.5% | 5.3% [4.2%-6.9%] | 8.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ella Seidel (`KXITFWMATCH-26OCT28BEKSEI-SEI`) | 0.94 / 0.95 (742) | 94.5% | 99.0% | 66.5% | 94.7% [93.1%-95.8%] | 91.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 19.0, B 4408.0; serve-point win A 46.6%, B 35.9%; Elo A 1244.3, B 1748.3; model uncertainty 0.0133
* Form inputs: days since last match A 443, B 57; matches on record A 10, B 283; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.016, surface_dev_loose -0.000, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dada-Mascoll / Okutoyi vs Cho / Savic -- W75 Glasgow R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28DADOKUCHOSAV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cho / Savic (`KXITFWDOUBLES-26OCT28DADOKUCHOSAV-CHOSAV`) | 0.05 / 0.90 (8) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dada-Mascoll / Okutoyi (`KXITFWDOUBLES-26OCT28DADOKUCHOSAV-DADOKU`) | 0.11 / 0.91 (2) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Gina Marie Dittmann vs Marine Partaud -- W75 Poitiers R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206277:222273:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gina Marie Dittmann (`KXITFWMATCH-26OCT28DITPAR-DIT`) | 0.59 / 0.63 (53) | 61.0% | 58.2% | 54.8% | 56.9% [52.1%-61.1%] | -- | -- | -- | -- | PASS | -2.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Marine Partaud (`KXITFWMATCH-26OCT28DITPAR-PAR`) | 0.38 / 0.39 (50) | 38.5% | 41.8% | 45.2% | 43.1% [38.9%-47.9%] | -- | -- | -- | -- | PASS | +3.3 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1885.0, B 367.0; serve-point win A 54.2%, B 47.3%; Elo A 1412.4, B 1363.2; model uncertainty 0.0447
* Form inputs: days since last match A 205, B 905; matches on record A 115, B 456; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.042, surface_pool_high +0.042, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofya Lansere vs Romane Longueville -- W75 Glasgow R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216139:245079:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofya Lansere (`KXITFWMATCH-26OCT28LANLON-LAN`) | 0.92 / 0.93 (2896) | 92.5% | 95.4% | 96.0% | 93.0% [88.1%-95.5%] | 87.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.9 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Romane Longueville (`KXITFWMATCH-26OCT28LANLON-LON`) | 0.08 / 0.09 (579) | 8.5% | 4.6% | 4.0% | 7.0% [4.5%-11.9%] | 12.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.9 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3253.0, B 1160.0; serve-point win A 57.9%, B 54.8%; Elo A 1643.0, B 1266.8; model uncertainty 0.0372
* Form inputs: days since last match A 26, B 226; matches on record A 351, B 68; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.006, surface_pool_high +0.007, surface_dev_loose +0.009, surface_dev_tight -0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Learner Tien vs Alex de Minaur -- ATP Vienna R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-28 13:30Z
* Current expected start: 2026-10-28 19:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-28 18:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+330_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Clay · scheduled 2026-10-28T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200282:210530:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex de Minaur (`KXATPMATCH-26OCT28TIEDE-DE`) | 0.51 / 0.52 (33135) | 51.5% | 64.4% | 70.2% | 70.2% [68.4%-72.3%] | 52.2% | 51.3% | 51.7% | MODEL_LONE_OUTLIER | WATCH | +12.9 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Learner Tien (`KXATPMATCH-26OCT28TIEDE-TIE`) | 0.48 / 0.49 (3195) | 48.5% | 35.6% | 29.8% | 29.8% [27.7%-31.6%] | 47.8% | 48.6% | 48.2% | MODEL_LONE_OUTLIER | PASS | -12.9 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5484.0, B 6412.0; serve-point win A 58.6%, B 38.5%; Elo A 1802.2, B 1938.9; model uncertainty 0.0197
* Form inputs: days since last match A 2, B 2; matches on record A 250, B 689; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.018, surface_dev_loose +0.013, surface_dev_tight -0.008
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT28TIEDE-DE5` Will Alex de Minaur win at least 4.5 more games than Learner Tien?: 0.06/0.94 mid 50.0%, model 29.7% (projection_v2.0 (prediction ledger)) -- gap -20.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT28TIEDE-TIE2` Will Learner Tien win at least 1.5 more games than Alex de Minaur?: 0.42/0.44 mid 43.0%, model 29.2% (projection_v2.0 (prediction ledger)) -- gap -13.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT28TIEDE-DE2` Will Alex de Minaur win at least 1.5 more games than Learner Tien?: 0.45/0.46 mid 45.5%, model 57.8% (projection_v2.0 (prediction ledger)) -- gap +12.3 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT28TIEDE-TIE20` Will Learner Tien win the Learner Tien vs Alex de Minaur match by a set score of 2-0?: 0.27/0.29 mid 28.0%, model 16.2% (projection_v2.0 (prediction ledger)) -- gap -11.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT28TIEDE-1-DE` Will Alex de Minaur win set 1 in the Learner Tien vs Alex de Minaur match: 0.49/0.52 mid 50.5%, model 59.7% (projection_v2.0 (prediction ledger)) -- gap +9.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT28TIEDE-2-DE` Will Alex de Minaur win set 2 in the Learner Tien vs Alex de Minaur match: 0.48/0.54 mid 51.0%, model 59.7% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT28TIEDE-2-TIE` Will Learner Tien win set 2 in the Learner Tien vs Alex de Minaur match: 0.46/0.52 mid 49.0%, model 40.3% (projection_v2.0 (prediction ledger)) -- gap -8.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT28TIEDE-DE21` Will Alex de Minaur win the Learner Tien vs Alex de Minaur match by a set score of 2-1?: 0.19/0.22 mid 20.5%, model 28.7% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT28TIEDE-1-TIE` Will Learner Tien win set 1 in the Learner Tien vs Alex de Minaur match: 0.47/0.49 mid 48.0%, model 40.3% (projection_v2.0 (prediction ledger)) -- gap -7.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT28TIEDE-24` Over 23.5 games: 0.44/0.45 mid 44.5%, model 51.1% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT28TIEDE-DE20` Will Alex de Minaur win the Learner Tien vs Alex de Minaur match by a set score of 2-0?: 0.28/0.31 mid 29.5%, model 35.6% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT28TIEDE-19` Over 18.5 games: 0.78/0.81 mid 79.5%, model 82.9% (projection_v2.0 (prediction ledger)) -- gap +3.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT28TIEDE-29` Over 28.5 games: 0.27/0.29 mid 28.0%, model 30.6% (projection_v2.0 (prediction ledger)) -- gap +2.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT28TIEDE-TIE21` Will Learner Tien win the Learner Tien vs Alex de Minaur match by a set score of 2-1?: 0.18/0.22 mid 20.0%, model 19.4% (projection_v2.0 (prediction ledger)) -- gap -0.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Bocchi / Ciurnelli vs Motta / Taddia -- M15 Selva Gardena QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28BOCCIUMOTTAD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bocchi / Ciurnelli (`KXITFDOUBLES-26OCT28BOCCIUMOTTAD-BOCCIU`) | 0.44 / 0.62 (65) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Motta / Taddia (`KXITFDOUBLES-26OCT28BOCCIUMOTTAD-MOTTAD`) | 0.32 / 0.50 (50) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Busquets Brau / Eldin vs Barsukov / Ehrenschneider -- M25 Malta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28BUSELDBAREHR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barsukov / Ehrenschneider (`KXITFDOUBLES-26OCT28BUSELDBAREHR-BAREHR`) | 0.86 / 0.91 (2) | 88.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Busquets Brau / Eldin (`KXITFDOUBLES-26OCT28BUSELDBAREHR-BUSELD`) | 0.05 / 0.09 (35) | 7.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## bautista de la Pena vs Mateo Barreiros Reyes -- M15 João Pessoa R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-28T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207595:214016:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mateo Barreiros Reyes (`KXITFMATCH-26OCT28DELBAR-BAR`) | 0.74 / 0.78 (598) | 76.0% | 84.1% | 94.0% | 83.9% [76.6%-89.9%] | 73.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| bautista de la Pena (`KXITFMATCH-26OCT28DELBAR-DEL`) | 0.22 / 0.23 (1) | 22.5% | 15.9% | 6.0% | 16.2% [10.1%-23.4%] | 26.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 803.0, B 1996.0; serve-point win A 55.2%, B 37.2%; Elo A 1120.6, B 1320.5; model uncertainty 0.0662
* Form inputs: days since last match A 226, B 492; matches on record A 15, B 128; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.006, surface_dev_loose -0.018, surface_dev_tight +0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dhokia / Jones vs Horwood / Lawlor -- M25 Sheffield QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28DHOJONHORLAW:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dhokia / Jones (`KXITFDOUBLES-26OCT28DHOJONHORLAW-DHOJON`) | 0.66 / 0.82 (138) | 74.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Horwood / Lawlor (`KXITFDOUBLES-26OCT28DHOJONHORLAW-HORLAW`) | 0.15 / 0.29 (35) | 22.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Lechner / Trombini vs Colombo / Massellani -- M15 Selva Gardena QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28LECTROCOLMAS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Colombo / Massellani (`KXITFDOUBLES-26OCT28LECTROCOLMAS-COLMAS`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lechner / Trombini (`KXITFDOUBLES-26OCT28LECTROCOLMAS-LECTRO`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ignacio Monzon vs Rafael Augusto Garcia Finetto -- M15 João Pessoa R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-28T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133820:214312:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rafael Augusto Garcia Finetto (`KXITFMATCH-26OCT28MONGAR-GAR`) | 0.04 / 0.05 (449) | 4.5% | 27.3% | 40.5% | 39.5% [38.4%-40.0%] | -- | -- | -- | -- | PASS | +22.8 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ignacio Monzon (`KXITFMATCH-26OCT28MONGAR-MON`) | 0.95 / 0.98 (3955) | 96.5% | 72.7% | 59.5% | 60.5% [60.0%-61.6%] | -- | -- | -- | -- | PASS | -23.8 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3341.0, B 92.0; serve-point win A 56.9%, B 47.6%; Elo A 1356.6, B 1281.6; model uncertainty 0.0081
* Form inputs: days since last match A 114, B 338; matches on record A 427, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28MONGAR-GAR  (YES = Rafael Augusto Garcia Finetto)
Model: 27%
Kalshi: 4%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.005, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rocco Valente vs Jadielson Silva De Araujo Fio -- M15 João Pessoa R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28VALFIO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jadielson Silva De Araujo Fio (`KXITFMATCH-26OCT28VALFIO-FIO`) | 0.05 / 0.06 (6) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rocco Valente (`KXITFMATCH-26OCT28VALFIO-VAL`) | 0.90 / 0.97 (631) | 93.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Busuttil Fitzpatrick / Kuijt vs Fehr / Perera Vega -- W35 Malta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28BUSKUIFEHPER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Busuttil Fitzpatrick / Kuijt (`KXITFWDOUBLES-26OCT28BUSKUIFEHPER-BUSKUI`) | 0.94 / 0.96 (288) | 95.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fehr / Perera Vega (`KXITFWDOUBLES-26OCT28BUSKUIFEHPER-FEHPER`) | 0.06 / 0.16 (1) | 11.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Milena Maria Ciocan vs Tilwith Di Girolami -- W15 Essen R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:228910:270134:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Milena Maria Ciocan (`KXITFWMATCH-26OCT28CIODIG-CIO`) | 0.14 / 0.15 (4) | 14.5% | 8.6% | 22.8% | 23.6% [22.0%-25.2%] | -- | -- | -- | -- | PASS | -5.9 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tilwith Di Girolami (`KXITFWMATCH-26OCT28CIODIG-DIG`) | 0.83 / 0.84 (156) | 83.5% | 91.4% | 77.2% | 76.4% [74.8%-78.0%] | -- | -- | -- | -- | PASS | +7.9 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 217.0, B 1533.0; serve-point win A 49.4%, B 40.3%; Elo A 1236.2, B 1440.2; model uncertainty 0.0164
* Form inputs: days since last match A 240, B 184; matches on record A 6, B 202; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.017, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Joy De Zeeuw vs Lisa Peer -- W35 Malta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260226:266558:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joy De Zeeuw (`KXITFWMATCH-26OCT28DEZPEE-DEZ`) | 0.92 / 0.96 (1574) | 94.0% | 89.8% | 63.9% | 72.8% [71.9%-74.6%] | 90.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lisa Peer (`KXITFWMATCH-26OCT28DEZPEE-PEE`) | 0.05 / 0.07 (352) | 6.0% | 10.2% | 36.1% | 27.2% [25.4%-28.1%] | 9.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2042.0, B 154.0; serve-point win A 61.6%, B 48.1%; Elo A 1406.8, B 1230.4; model uncertainty 0.0133
* Form inputs: days since last match A 394, B 17; matches on record A 70, B 7; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose -0.000, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zoe Doldan vs Luna Morini -- W15 Neuquén R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-28T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221064:269847:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zoe Doldan (`KXITFWMATCH-26OCT28DOLMOR-DOL`) | 0.63 / 0.64 (1) | 63.5% | 43.1% | 50.0% | 46.8% [46.8%-46.8%] | 64.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.4 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Luna Morini (`KXITFWMATCH-26OCT28DOLMOR-MOR`) | 0.36 / 0.37 (42) | 36.5% | 56.9% | 50.0% | 53.2% [53.2%-53.2%] | 35.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +20.4 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 53.2%, B 45.5%; Elo A 1244.4, B 1263.9; model uncertainty 0.0
* Form inputs: days since last match A 737, B 3117; matches on record A 1, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28DOLMOR-MOR  (YES = Luna Morini)
Model: 57%
Kalshi: 36%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ana Julieta Lopez Ocampos vs Abril Pajello -- W15 Neuquén R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-28T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:266726:269888:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ana Julieta Lopez Ocampos (`KXITFWMATCH-26OCT28LOPPAJ-LOP`) | 0.82 / 0.85 (3) | 83.5% | 72.2% | 50.0% | 51.1% [51.1%-51.1%] | 83.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.3 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Abril Pajello (`KXITFWMATCH-26OCT28LOPPAJ-PAJ`) | 0.13 / 0.15 (27) | 14.0% | 27.8% | 50.0% | 48.9% [48.9%-48.9%] | 17.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.8 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 56.1%, B 48.3%; Elo A 1218.6, B 1210.5; model uncertainty 0.0
* Form inputs: days since last match A 723, B 968; matches on record A 2, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pia Lovric vs Elaine Genovese -- W35 Malta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:209712:222458:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elaine Genovese (`KXITFWMATCH-26OCT28LOVGEN-GEN`) | 0.07 / 0.08 (259) | 7.5% | 9.7% | 40.5% | 23.0% [21.8%-24.3%] | 9.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.2 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pia Lovric (`KXITFWMATCH-26OCT28LOVGEN-LOV`) | 0.91 / 0.94 (72) | 92.5% | 90.3% | 59.6% | 77.0% [75.7%-78.2%] | 90.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.2 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1631.0, B 171.0; serve-point win A 56.7%, B 53.0%; Elo A 1467.6, B 1239.3; model uncertainty 0.0121
* Form inputs: days since last match A 17, B 366; matches on record A 300, B 127; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose +0.000, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Greta Petrillo vs Anja Stankovic -- W35 Malta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:244087:260941:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Greta Petrillo (`KXITFWMATCH-26OCT28PETSTA-PET`) | 0.06 / 0.09 (75) | 7.5% | 9.6% | 42.6% | 21.4% [21.2%-21.4%] | 10.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Anja Stankovic (`KXITFWMATCH-26OCT28PETSTA-STA`) | 0.89 / 0.93 (28) | 91.0% | 90.4% | 57.4% | 78.6% [78.6%-78.8%] | 89.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 2297.0; serve-point win A 51.4%, B 38.7%; Elo A 1271.8, B 1499.8; model uncertainty 0.0008
* Form inputs: days since last match A 1080, B 247; matches on record A 4, B 192; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carola Celina Sosa vs Melissa Boyden -- W15 Neuquén R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-28T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222274:260707:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Melissa Boyden (`KXITFWMATCH-26OCT28SOSBOY-BOY`) | 0.85 / 0.88 (432) | 86.5% | 77.8% | 52.7% | 69.5% [68.0%-73.1%] | 84.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.7 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carola Celina Sosa (`KXITFWMATCH-26OCT28SOSBOY-SOS`) | 0.13 / 0.14 (34) | 13.5% | 22.2% | 47.3% | 30.5% [26.9%-31.9%] | 15.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.7 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 230.0, B 765.0; serve-point win A 50.1%, B 44.2%; Elo A 1088.7, B 1254.1; model uncertainty 0.0252
* Form inputs: days since last match A 282, B 198; matches on record A 35, B 91; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.014, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tamara Sramkova vs Lara Wagner -- W35 Malta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28SRAWAG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tamara Sramkova (`KXITFWMATCH-26OCT28SRAWAG-SRA`) | 0.52 / 0.53 (51) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lara Wagner (`KXITFWMATCH-26OCT28SRAWAG-WAG`) | 0.45 / 0.48 (5) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jialin Tian vs Clarissa Gai -- W35 Malta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28TIAGAI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Clarissa Gai (`KXITFWMATCH-26OCT28TIAGAI-GAI`) | 0.09 / 0.13 (26) | 11.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jialin Tian (`KXITFWMATCH-26OCT28TIAGAI-TIA`) | 0.88 / 0.91 (1715) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lian Tran vs Annemarie Lazar -- W15 Essen R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220560:241728:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Annemarie Lazar (`KXITFWMATCH-26OCT28TRALAZ-LAZ`) | 0.09 / 0.12 (5) | 10.5% | 10.1% | 64.1% | 22.3% [14.9%-29.6%] | 12.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.4 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lian Tran (`KXITFWMATCH-26OCT28TRALAZ-TRA`) | 0.88 / 0.91 (4) | 89.5% | 89.9% | 35.9% | 77.7% [70.4%-85.1%] | 87.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.4 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1204.0, B 404.0; serve-point win A 58.1%, B 51.5%; Elo A 1505.4, B 1200.5; model uncertainty 0.0737
* Form inputs: days since last match A 184, B 247; matches on record A 307, B 57; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.012, surface_pool_high -0.016, surface_dev_loose -0.008, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Boris Arias / Ignacio Carou vs Emilio Camacho / Angel Veliz -- ATP Challenger Guayaquil R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-28T19:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28ARICARCAMVEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Boris Arias / Ignacio Carou (`KXATPCHALLENGERDOUBLES-26OCT28ARICARCAMVEL-ARICAR`) | 0.81 / 0.88 (370) | 84.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Emilio Camacho / Angel Veliz (`KXATPCHALLENGERDOUBLES-26OCT28ARICARCAMVEL-CAMVEL`) | 0.12 / 0.18 (207) | 15.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Alvaro Guillen Meza vs Alex Hernandez -- ATP Challenger Guayaquil R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-28T19:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28GUIHER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alvaro Guillen Meza (`KXATPCHALLENGERMATCH-26OCT28GUIHER-GUI`) | 0.63 / 0.64 (178) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alex Hernandez (`KXATPCHALLENGERMATCH-26OCT28GUIHER-HER`) | 0.35 / 0.36 (321) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Aidan Mayo vs Maks Kasnikowski -- ATP Challenger Sioux Falls R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-28T19:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208854:209874:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maks Kasnikowski (`KXATPCHALLENGERMATCH-26OCT28MAYKAS-KAS`) | 0.60 / 0.61 (925) | 60.5% | 59.9% | 60.4% | 60.4% [59.9%-61.3%] | 60.9% | 60.6% | 60.8% | MARKETS_AGREE | PASS | -0.6 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Aidan Mayo (`KXATPCHALLENGERMATCH-26OCT28MAYKAS-MAY`) | 0.39 / 0.40 (2119) | 39.5% | 40.1% | 39.6% | 39.6% [38.7%-40.1%] | 39.1% | 39.6% | 39.3% | MARKETS_AGREE | PASS | +0.6 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3705.0, B 4951.0; serve-point win A 62.8%, B 35.2%; Elo A 1548.0, B 1623.1; model uncertainty 0.0074
* Form inputs: days since last match A 9, B 16; matches on record A 256, B 325; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.005, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Jeffrey John Wolf vs Daniel Milavsky -- ATP Challenger Sioux Falls R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-28T19:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28WOLMIL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Milavsky (`KXATPCHALLENGERMATCH-26OCT28WOLMIL-MIL`) | 0.32 / 0.33 (1667) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jeffrey John Wolf (`KXATPCHALLENGERMATCH-26OCT28WOLMIL-WOL`) | 0.67 / 0.68 (421) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Lucrezia Stefanini vs Ayla Aksu -- WTA 125K Courmayeur R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-28 22:30Z
* Current expected start: 2026-10-28 19:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-28 18:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · surface ? · scheduled 2026-10-28T22:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:213767:214593:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ayla Aksu (`KXWTACHALLENGERMATCH-26OCT28STEAKS-AKS`) | 0.29 / 0.31 (918) | 30.0% | 37.8% | 59.0% | 47.3% [36.4%-53.2%] | 31.2% | 32.6% | -- | INSUFFICIENT_INPUTS | WATCH | +7.8 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lucrezia Stefanini (`KXWTACHALLENGERMATCH-26OCT28STEAKS-STE`) | 0.69 / 0.71 (706) | 70.0% | 62.2% | 41.0% | 52.7% [46.8%-63.6%] | 68.8% | 67.9% | -- | INSUFFICIENT_INPUTS | PASS | -7.8 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4432.0, B 2415.0; serve-point win A 52.9%, B 49.4%; Elo A 1882.0, B 1731.1; model uncertainty 0.0843
* Form inputs: days since last match A 12, B 2; matches on record A 613, B 583; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Bozemoj / Pel vs Brady / Wright -- M25 Sheffield QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28BOZPELBRAWRI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bozemoj / Pel (`KXITFDOUBLES-26OCT28BOZPELBRAWRI-BOZPEL`) | 0.67 / 0.83 (147) | 75.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Brady / Wright (`KXITFDOUBLES-26OCT28BOZPELBRAWRI-BRAWRI`) | 0.12 / 0.28 (34) | 20.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Matisse Farzam vs Stephen Slocombe -- M15 Pembroke R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212859:213723:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matisse Farzam (`KXITFMATCH-26OCT28FARSLO-FAR`) | 0.85 / 0.87 (66) | 86.0% | 78.8% | 81.5% | 61.2% [59.2%-65.2%] | 82.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stephen Slocombe (`KXITFMATCH-26OCT28FARSLO-SLO`) | 0.13 / 0.14 (371) | 13.5% | 21.2% | 18.6% | 38.8% [34.8%-40.8%] | 17.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 255.0, B 127.0; serve-point win A 62.5%, B 43.6%; Elo A 1276.9, B 1213.2; model uncertainty 0.03
* Form inputs: days since last match A 352, B 240; matches on record A 9, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Volodymyr Gurenko vs Darian King -- M15 Pembroke R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105985:213628:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Volodymyr Gurenko (`KXITFMATCH-26OCT28GURKIN-GUR`) | 0.04 / 0.05 (107) | 4.5% | 18.8% | 31.9% | 16.1% [12.2%-19.4%] | 7.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +14.3 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Darian King (`KXITFMATCH-26OCT28GURKIN-KIN`) | 0.93 / 0.96 (2) | 94.5% | 81.2% | 68.1% | 84.0% [80.6%-87.8%] | 92.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.3 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 650.0, B 841.0; serve-point win A 54.9%, B 38.3%; Elo A 1258.1, B 1622.9; model uncertainty 0.0362
* Form inputs: days since last match A 184, B 263; matches on record A 13, B 633; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kian Vakili vs Gray Voelzke -- M15 Pembroke R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210704:213882:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kian Vakili (`KXITFMATCH-26OCT28VAKVOE-VAK`) | 0.64 / 0.67 (35) | 65.5% | 62.6% | 73.4% | 62.8% [61.9%-64.5%] | 63.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.9 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gray Voelzke (`KXITFMATCH-26OCT28VAKVOE-VOE`) | 0.32 / 0.33 (37) | 32.5% | 37.4% | 26.6% | 37.2% [35.5%-38.1%] | 36.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.9 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 173.0, B 817.0; serve-point win A 65.0%, B 37.6%; Elo A 1201.5, B 1115.5; model uncertainty 0.0129
* Form inputs: days since last match A 184, B 177; matches on record A 16, B 16; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Niels Peter Van Noord vs Keshav Chopra -- M15 Pembroke R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207725:208844:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Keshav Chopra (`KXITFMATCH-26OCT28VANCHO-CHO`) | 0.87 / 0.90 (241) | 88.5% | 62.6% | 49.0% | 53.1% [52.0%-53.6%] | 85.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -25.9 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Niels Peter Van Noord (`KXITFMATCH-26OCT28VANCHO-VAN`) | 0.10 / 0.14 (7) | 12.0% | 37.4% | 51.0% | 46.9% [46.4%-47.9%] | 14.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +25.4 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 458.0, B 1264.0; serve-point win A 59.7%, B 37.8%; Elo A 1205.8, B 1232.7; model uncertainty 0.0077
* Form inputs: days since last match A 240, B 65; matches on record A 13, B 89; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28VANCHO-VAN  (YES = Niels Peter Van Noord)
Model: 37%
Kalshi: 12%
Gap: +25 pp
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
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Buchler / Honic vs Maslenkova / Saner -- W15 Taby R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28BUCHONMASSAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Buchler / Honic (`KXITFWDOUBLES-26OCT28BUCHONMASSAN-BUCHON`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maslenkova / Saner (`KXITFWDOUBLES-26OCT28BUCHONMASSAN-MASSAN`) | 0.06 / 0.89 (3) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Oceane Dodin vs Georgina Hays -- W75 Poitiers R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206219:246516:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oceane Dodin (`KXITFWMATCH-26OCT28DODHAY-DOD`) | 0.95 / 0.97 (938) | 96.0% | 98.1% | 91.6% | 94.9% [94.2%-95.6%] | 94.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Georgina Hays (`KXITFWMATCH-26OCT28DODHAY-HAY`) | 0.04 / 0.05 (557) | 4.5% | 1.9% | 8.4% | 5.1% [4.4%-5.8%] | 5.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1969.0, B 333.0; serve-point win A 65.3%, B 50.5%; Elo A 1748.1, B 1221.1; model uncertainty 0.007
* Form inputs: days since last match A 35, B 464; matches on record A 714, B 89; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.004, surface_dev_loose +0.004, surface_dev_tight -0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eckersten / Nicander vs Bosman / Veldman -- W15 Taby R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28ECKNICBOSVEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bosman / Veldman (`KXITFWDOUBLES-26OCT28ECKNICBOSVEL-BOSVEL`) | 0.06 / 0.91 (2) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eckersten / Nicander (`KXITFWDOUBLES-26OCT28ECKNICBOSVEL-ECKNIC`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Grekul / Norin vs Hofmann / Jankowska -- W15 Taby R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28GRENORHOFJAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Grekul / Norin (`KXITFWDOUBLES-26OCT28GRENORHOFJAN-GRENOR`) | 0.05 / 0.91 (3) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hofmann / Jankowska (`KXITFWDOUBLES-26OCT28GRENORHOFJAN-HOFJAN`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hietaranta / Steiner vs Iyer / Pringle -- W75 Glasgow R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28HIESTEIYEPRI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hietaranta / Steiner (`KXITFWDOUBLES-26OCT28HIESTEIYEPRI-HIESTE`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Iyer / Pringle (`KXITFWDOUBLES-26OCT28HIESTEIYEPRI-IYEPRI`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tinsley / Williams vs Aikawa / Vismane -- W75 Glasgow R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28TINWILAIKVIS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aikawa / Vismane (`KXITFWDOUBLES-26OCT28TINWILAIKVIS-AIKVIS`) | 0.64 / 0.95 (10) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tinsley / Williams (`KXITFWDOUBLES-26OCT28TINWILAIKVIS-TINWIL`) | 0.05 / 0.17 (62) | 11.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Eva Vedder vs Hannah Klugman -- W75 Glasgow R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220770:263872:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hannah Klugman (`KXITFWMATCH-26OCT28VEDKLU-KLU`) | 0.75 / 0.77 (367) | 76.0% | 58.4% | 58.3% | 58.3% [49.5%-62.3%] | 74.3% | -- | 74.3% | MODEL_LONE_OUTLIER | PASS | -17.6 pp | HIGH_REVIEW | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Eva Vedder (`KXITFWMATCH-26OCT28VEDKLU-VED`) | 0.24 / 0.25 (3) | 24.5% | 41.6% | 41.7% | 41.7% [37.7%-50.5%] | 25.7% | -- | 25.7% | MODEL_LONE_OUTLIER | WATCH | +17.1 pp | HIGH_REVIEW | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3271.0, B 1658.0; serve-point win A 57.9%, B 40.5%; Elo A 1579.8, B 1636.2; model uncertainty 0.0642
* Form inputs: days since last match A 16, B 121; matches on record A 431, B 78; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28VEDKLU-VED  (YES = Eva Vedder)
Model: 42%
Kalshi: 24%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: B (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.041, surface_pool_high -0.040, surface_dev_loose -0.020, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bilardo / Rottoli vs Fellin / Orlando Fellin -- M15 Selva Gardena QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28BILROTFELORL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bilardo / Rottoli (`KXITFDOUBLES-26OCT28BILROTFELORL-BILROT`) | 0.63 / 0.84 (156) | 73.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fellin / Orlando Fellin (`KXITFDOUBLES-26OCT28BILROTFELORL-FELORL`) | 0.07 / 0.27 (34) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Julian Cundom vs Dante Pagani -- M15 João Pessoa R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-28T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208424:213677:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julian Cundom (`KXITFMATCH-26OCT28CUNPAG-CUN`) | 0.40 / 0.44 (168) | 42.0% | 42.6% | 52.1% | 43.1% [37.5%-47.3%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.6 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dante Pagani (`KXITFMATCH-26OCT28CUNPAG-PAG`) | 0.57 / 0.58 (101) | 57.5% | 57.4% | 47.9% | 56.9% [52.7%-62.5%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.1 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 948.0, B 964.0; serve-point win A 52.5%, B 46.1%; Elo A 1203.3, B 1287.0; model uncertainty 0.0489
* Form inputs: days since last match A 142, B 184; matches on record A 49, B 23; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.021, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tomas Farjat vs Giovanni Branchetti -- M15 João Pessoa R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28FARBRA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giovanni Branchetti (`KXITFMATCH-26OCT28FARBRA-BRA`) | 0.48 / 0.52 (1) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tomas Farjat (`KXITFMATCH-26OCT28FARBRA-FAR`) | 0.47 / 0.48 (48) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matic / Thurner vs Aleksandar Amarandei / Figl -- M15 Selva Gardena QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28MATTHUALEFIG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aleksandar Amarandei / Figl (`KXITFDOUBLES-26OCT28MATTHUALEFIG-ALEFIG`) | 0.42 / 0.62 (65) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matic / Thurner (`KXITFDOUBLES-26OCT28MATTHUALEFIG-MATTHU`) | 0.32 / 0.52 (52) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Carolyn Ansari vs Teah Chavez -- W75 Toronto R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:258199:260374:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carolyn Ansari (`KXITFWMATCH-26OCT28ANSCHA-ANS`) | 0.54 / 0.55 (1) | 54.5% | 85.7% | 82.2% | 78.9% [77.7%-80.8%] | 56.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +31.2 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Teah Chavez (`KXITFWMATCH-26OCT28ANSCHA-CHA`) | 0.42 / 0.46 (195) | 44.0% | 14.3% | 17.8% | 21.1% [19.2%-22.3%] | 43.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -29.7 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4315.0, B 494.0; serve-point win A 57.4%, B 50.6%; Elo A 1585.3, B 1366.2; model uncertainty 0.0153
* Form inputs: days since last match A 36, B 92; matches on record A 181, B 22; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28ANSCHA-ANS  (YES = Carolyn Ansari)
Model: 86%
Kalshi: 55%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mika Buchnik vs Mia Robinson -- W15 Sumter SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:238205:269950:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mika Buchnik (`KXITFWMATCH-26OCT28BUCROB-BUC`) | 0.60 / 0.63 (200) | 61.5% | 67.9% | 30.5% | 51.1% [50.0%-51.1%] | 60.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.4 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mia Robinson (`KXITFWMATCH-26OCT28BUCROB-ROB`) | 0.38 / 0.41 (44) | 39.5% | 32.1% | 69.5% | 48.9% [48.9%-50.0%] | 39.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.4 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 770.0, B 0.0; serve-point win A 54.0%, B 49.5%; Elo A 1345.0, B 1340.3; model uncertainty 0.0054
* Form inputs: days since last match A 352, B 716; matches on record A 53, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chiara Di Genova vs Marilouise Van Zyl -- W15 Sumter SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221414:233728:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chiara Di Genova (`KXITFWMATCH-26OCT28DIGVAN-DIG`) | 0.59 / 0.62 (47) | 60.5% | 46.1% | 53.7% | 53.2% [52.1%-54.3%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -14.4 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marilouise Van Zyl (`KXITFWMATCH-26OCT28DIGVAN-VAN`) | 0.38 / 0.39 (4) | 38.5% | 53.9% | 46.3% | 46.8% [45.7%-47.9%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +15.4 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 146.0, B 222.0; serve-point win A 53.2%, B 46.1%; Elo A 1310.8, B 1291.2; model uncertainty 0.0106
* Form inputs: days since last match A 527, B 520; matches on record A 69, B 32; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28DIGVAN-VAN  (YES = Marilouise Van Zyl)
Model: 54%
Kalshi: 38%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jasmijn Gimbrere vs Clervie Ngounoue -- W75 Toronto R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222276:238064:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jasmijn Gimbrere (`KXITFWMATCH-26OCT28GIMNGO-GIM`) | 0.08 / 0.11 (799) | 9.5% | 20.6% | 45.3% | 35.6% [25.8%-39.6%] | 11.7% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +11.1 pp | REVIEW | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Clervie Ngounoue (`KXITFWMATCH-26OCT28GIMNGO-NGO`) | 0.89 / 0.93 (7054) | 91.0% | 79.4% | 54.7% | 64.4% [60.4%-74.2%] | 88.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.6 pp | REVIEW | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2502.0, B 2509.0; serve-point win A 53.6%, B 40.2%; Elo A 1481.1, B 1704.5; model uncertainty 0.0691
* Form inputs: days since last match A 38, B 65; matches on record A 319, B 153; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Camila Eluney Kilapi vs Alisa Danilova -- W15 Neuquén R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28KILDAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alisa Danilova (`KXITFWMATCH-26OCT28KILDAN-DAN`) | 0.86 / 0.88 (36) | 87.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Camila Eluney Kilapi (`KXITFWMATCH-26OCT28KILDAN-KIL`) | 0.13 / 0.14 (24) | 13.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ellery Mendell vs Anita Sahdiieva -- W15 Sumter SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221370:268805:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ellery Mendell (`KXITFWMATCH-26OCT28MENSAH-MEN`) | 0.35 / 0.36 (52) | 35.5% | 17.3% | 38.5% | 37.4% [36.4%-37.4%] | 35.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -18.2 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Anita Sahdiieva (`KXITFWMATCH-26OCT28MENSAH-SAH`) | 0.62 / 0.63 (67) | 62.5% | 82.7% | 61.6% | 62.6% [62.6%-63.6%] | 64.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +20.2 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 1325.0; serve-point win A 50.8%, B 42.2%; Elo A 1297.3, B 1390.1; model uncertainty 0.0051
* Form inputs: days since last match A 807, B 184; matches on record A 2, B 111; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28MENSAH-SAH  (YES = Anita Sahdiieva)
Model: 83%
Kalshi: 62%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amandine Monnot vs Mathilde Lollia -- W75 Poitiers R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221443:221486:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mathilde Lollia (`KXITFWMATCH-26OCT28MONLOL-LOL`) | 0.18 / 0.21 (59) | 19.5% | 16.0% | 17.4% | 19.9% [17.1%-27.5%] | 20.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.5 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amandine Monnot (`KXITFWMATCH-26OCT28MONLOL-MON`) | 0.78 / 0.81 (762) | 79.5% | 84.0% | 82.6% | 80.1% [72.5%-82.9%] | 79.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.5 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3095.0, B 2163.0; serve-point win A 60.1%, B 47.4%; Elo A 1633.0, B 1429.9; model uncertainty 0.0521
* Form inputs: days since last match A 52, B 13; matches on record A 268, B 177; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.014, surface_dev_loose +0.014, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Nahiara Nappi vs Sofia Finchelstein -- W15 Neuquén R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28NAPFIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Finchelstein (`KXITFWMATCH-26OCT28NAPFIN-FIN`) | 0.41 / 0.44 (170) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sofia Nahiara Nappi (`KXITFWMATCH-26OCT28NAPFIN-NAP`) | 0.56 / 0.60 (131) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Madison Sieg vs Kisa Yoshioka -- W75 Toronto R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215616:221020:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Madison Sieg (`KXITFWMATCH-26OCT28SIEYOS-SIE`) | 0.75 / 0.79 (790) | 77.0% | 78.0% | 74.4% | 73.1% [70.9%-74.4%] | 76.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.0 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kisa Yoshioka (`KXITFWMATCH-26OCT28SIEYOS-YOS`) | 0.21 / 0.23 (26) | 22.0% | 22.0% | 25.6% | 26.9% [25.6%-29.1%] | 23.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -0.0 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2163.0, B 1530.0; serve-point win A 56.0%, B 49.8%; Elo A 1525.1, B 1360.1; model uncertainty 0.0178
* Form inputs: days since last match A 43, B 191; matches on record A 228, B 159; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.013, surface_dev_loose +0.009, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amelie Smejkalova vs Jensen Diianni -- W15 Sumter SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223359:270383:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jensen Diianni (`KXITFWMATCH-26OCT28SMEDII-DII`) | 0.18 / 0.19 (35) | 18.5% | 28.0% | 34.8% | 39.4% [37.3%-40.4%] | 21.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +9.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amelie Smejkalova (`KXITFWMATCH-26OCT28SMEDII-SME`) | 0.78 / 0.82 (62) | 80.0% | 72.0% | 65.2% | 60.6% [59.6%-62.7%] | 78.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 297.0, B 180.0; serve-point win A 52.7%, B 51.7%; Elo A 1371.4, B 1299.6; model uncertainty 0.0155
* Form inputs: days since last match A 352, B 254; matches on record A 68, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.010, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aiken Tejada vs Sofia Simon Padros -- W15 Neuquén R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-28T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:266453:270327:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Simon Padros (`KXITFWMATCH-26OCT28TEJSIM-SIM`) | 0.66 / 0.68 (54) | 67.0% | 86.7% | 36.4% | 73.1% [70.4%-74.0%] | 64.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +19.6 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aiken Tejada (`KXITFWMATCH-26OCT28TEJSIM-TEJ`) | 0.31 / 0.32 (4) | 31.5% | 13.4% | 63.6% | 26.9% [26.0%-29.6%] | 35.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -18.1 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 55.0, B 54.0; serve-point win A 48.8%, B 42.9%; Elo A 1065.7, B 1244.6; model uncertainty 0.0177
* Form inputs: days since last match A 359, B 359; matches on record A 19, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28TEJSIM-SIM  (YES = Sofia Simon Padros)
Model: 87%
Kalshi: 67%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.009, surface_dev_loose +0.004, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mac Kiger / John-Patrick Smith vs Jason Jung / Joshua Sheehy -- ATP Challenger Sioux Falls R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 20:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-28T20:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28KIGSMIJUNSHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jason Jung / Joshua Sheehy (`KXATPCHALLENGERDOUBLES-26OCT28KIGSMIJUNSHE-JUNSHE`) | 0.38 / 0.44 (87) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mac Kiger / John-Patrick Smith (`KXATPCHALLENGERDOUBLES-26OCT28KIGSMIJUNSHE-KIGSMI`) | 0.56 / 0.61 (87) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Luis David Martinez / Jeevan Nedunchezhiyan vs Mitchell Krueger / Christopher Papa -- ATP Challenger Sioux Falls R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 20:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-28T20:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28MARNEDKRUPAP:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mitchell Krueger / Christopher Papa (`KXATPCHALLENGERDOUBLES-26OCT28MARNEDKRUPAP-KRUPAP`) | 0.05 / 0.95 (217) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luis David Martinez / Jeevan Nedunchezhiyan (`KXATPCHALLENGERDOUBLES-26OCT28MARNEDKRUPAP-MARNED`) | 0.05 / 0.95 (217) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Pedro Henrique Chabalgoity vs Lorenzo Gagliardo -- M15 João Pessoa R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-28T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207682:214014:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pedro Henrique Chabalgoity (`KXITFMATCH-26OCT28CHAGAG-CHA`) | 0.14 / 0.15 (106) | 14.5% | 28.0% | 26.5% | 38.0% [33.9%-40.7%] | 19.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.5 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lorenzo Gagliardo (`KXITFMATCH-26OCT28CHAGAG-GAG`) | 0.84 / 0.86 (42) | 85.0% | 72.0% | 73.5% | 62.1% [59.3%-66.1%] | 80.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.0 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 336.0, B 780.0; serve-point win A 52.3%, B 43.3%; Elo A 1252.7, B 1316.6; model uncertainty 0.0341
* Form inputs: days since last match A 359, B 233; matches on record A 5, B 97; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hugo Gaston vs Daniil Glinka -- ATP Challenger Brest R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-28T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200384:206750:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Gaston (`KXATPCHALLENGERMATCH-26OCT28GASGLI-GAS`) | 0.64 / 0.65 (6872) | 64.5% | 53.6% | 44.9% | 48.5% [45.4%-55.1%] | 62.5% | 63.7% | 63.7% | MODEL_LONE_OUTLIER | PASS | -10.9 pp | REVIEW | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Daniil Glinka (`KXATPCHALLENGERMATCH-26OCT28GASGLI-GLI`) | 0.35 / 0.36 (375) | 35.5% | 46.4% | 55.1% | 51.5% [44.9%-54.6%] | 37.5% | 36.4% | 36.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.9 pp | REVIEW | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5258.0, B 5303.0; serve-point win A 62.3%, B 38.4%; Elo A 1733.6, B 1654.3; model uncertainty 0.0481
* Form inputs: days since last match A 8, B 23; matches on record A 529, B 386; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Barth / Nizetic vs Angelina Abendroth / Angelique Abendroth -- W15 Essen QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28BARNIZANGANG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Angelina Abendroth / Angelique Abendroth (`KXITFWDOUBLES-26OCT28BARNIZANGANG-ANGANG`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Barth / Nizetic (`KXITFWDOUBLES-26OCT28BARNIZANGANG-BARNIZ`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Iveta Dapkute vs Louanne Djafari -- W15 Taby R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:210158:260307:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iveta Dapkute (`KXITFWMATCH-26OCT28DAPDJA-DAP`) | 0.66 / 0.67 (2696) | 66.5% | 88.4% | 51.1% | 76.5% [74.0%-78.1%] | 74.3% | -- | 74.3% | MODEL_LONE_OUTLIER | PASS | +21.9 pp | HIGH_REVIEW | AGING | F / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Louanne Djafari (`KXITFWMATCH-26OCT28DAPDJA-DJA`) | 0.32 / 0.33 (0) | 32.5% | 11.6% | 48.9% | 23.5% [21.9%-26.0%] | 25.7% | -- | 25.7% | MODEL_LONE_OUTLIER | PASS | -20.9 pp | HIGH_REVIEW | AGING | F / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 792.0, B 165.0; serve-point win A 57.9%, B 51.1%; Elo A 1404.3, B 1179.4; model uncertainty 0.0207
* Form inputs: days since last match A 184, B 268; matches on record A 203, B 7; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28DAPDJA-DAP  (YES = Iveta Dapkute)
Model: 88%
Kalshi: 66%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: SUPPORTS_MODEL_DIRECTION
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.025, surface_pool_high +0.016, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Schuknecht / Schweika vs Barth / Groen -- W15 Essen QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28SCHSCHBARGRO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barth / Groen (`KXITFWDOUBLES-26OCT28SCHSCHBARGRO-BARGRO`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Schuknecht / Schweika (`KXITFWDOUBLES-26OCT28SCHSCHBARGRO-SCHSCH`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Victoria Eigelsbach / Solakov vs Burchak / Raschdorf -- W15 Essen QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28VICSOLBURRAS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Burchak / Raschdorf (`KXITFWDOUBLES-26OCT28VICSOLBURRAS-BURRAS`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Victoria Eigelsbach / Solakov (`KXITFWDOUBLES-26OCT28VICSOLBURRAS-VICSOL`) | 0.05 / 0.91 (3) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nauhany Vitoria Leme Da Silva vs Luisina Giovannini -- WTA 125K Curitiba R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-29 00:00Z
* Current expected start: 2026-10-28 21:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-28 20:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Clay · scheduled 2026-10-29T00:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:236972:267382:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luisina Giovannini (`KXWTACHALLENGERMATCH-26OCT28LEMGIO-GIO`) | 0.70 / 0.72 (1061) | 71.0% | 83.6% | 88.1% | 81.8% [77.0%-84.4%] | -- | -- | -- | -- | WATCH | +12.6 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nauhany Vitoria Leme Da Silva (`KXWTACHALLENGERMATCH-26OCT28LEMGIO-LEM`) | 0.28 / 0.29 (1964) | 28.5% | 16.4% | 11.8% | 18.2% [15.6%-23.0%] | -- | -- | -- | -- | PASS | -12.1 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 774.0, B 3057.0; serve-point win A 53.6%, B 39.0%; Elo A 1541.0, B 1759.9; model uncertainty 0.0368
* Form inputs: days since last match A 2, B 2; matches on record A 31, B 200; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.007, surface_dev_loose -0.007, surface_dev_tight +0.003
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE

## Leon Achurra Correa vs Paul Colin -- M15 Pembroke R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28ACHCOL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leon Achurra Correa (`KXITFMATCH-26OCT28ACHCOL-ACH`) | 0.03 / 0.04 (9) | 3.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Paul Colin (`KXITFMATCH-26OCT28ACHCOL-COL`) | 0.95 / 0.97 (278) | 96.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leo Borg vs Liam Delicata -- M25 Malta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209863:212094:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leo Borg (`KXITFMATCH-26OCT28BORDEL-BOR`) | 0.80 / 0.82 (229) | 81.0% | 93.5% | 93.5% | 91.3% [89.8%-93.1%] | 76.8% | -- | 76.8% | ALL_THREE_DISAGREE | PASS | +12.4 pp | REVIEW | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Liam Delicata (`KXITFMATCH-26OCT28BORDEL-DEL`) | 0.17 / 0.20 (100) | 18.5% | 6.6% | 6.5% | 8.7% [6.9%-10.2%] | 23.2% | -- | 23.2% | ALL_THREE_DISAGREE | PASS | -11.9 pp | REVIEW | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3869.0, B 547.0; serve-point win A 62.0%, B 49.4%; Elo A 1470.5, B 1079.3; model uncertainty 0.0164
* Form inputs: days since last match A 184, B 184; matches on record A 287, B 21; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.000, surface_dev_loose +0.009, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tito Chavez vs Emile Hudd -- M25 Norman OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209163:214377:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tito Chavez (`KXITFMATCH-26OCT28CHAHUD-CHA`) | 0.26 / 0.28 (4) | 27.0% | 11.8% | 16.8% | 17.4% [16.0%-18.6%] | 30.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.2 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Emile Hudd (`KXITFMATCH-26OCT28CHAHUD-HUD`) | 0.70 / 0.71 (86) | 70.5% | 88.2% | 83.2% | 82.5% [81.4%-84.0%] | 69.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +17.8 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 239.0, B 3294.0; serve-point win A 54.5%, B 36.3%; Elo A 1230.0, B 1492.8; model uncertainty 0.0132
* Form inputs: days since last match A 184, B 65; matches on record A 5, B 173; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28CHAHUD-HUD  (YES = Emile Hudd)
Model: 88%
Kalshi: 70%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cretu / Corneliu Gadoiu vs Braynin / Kravchenko -- M25 Malta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28CRECORBRAKRA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Braynin / Kravchenko (`KXITFDOUBLES-26OCT28CRECORBRAKRA-BRAKRA`) | 0.14 / 0.91 (2) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cretu / Corneliu Gadoiu (`KXITFDOUBLES-26OCT28CRECORBRAKRA-CRECOR`) | 0.05 / 0.18 (30) | 11.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sean Daryabeigi vs LUCIANO EMANUEL AMBROGI -- M25 Norman OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210377:211737:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LUCIANO EMANUEL AMBROGI (`KXITFMATCH-26OCT28DARAMB-AMB`) | 0.34 / 0.35 (37) | 34.5% | 89.4% | 69.9% | 83.9% [83.3%-85.0%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +54.9 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sean Daryabeigi (`KXITFMATCH-26OCT28DARAMB-DAR`) | 0.63 / 0.64 (0) | 63.5% | 10.6% | 30.1% | 16.1% [15.0%-16.7%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -52.9 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 141.0, B 4093.0; serve-point win A 53.9%, B 36.5%; Elo A 1190.9, B 1496.6; model uncertainty 0.0086
* Form inputs: days since last match A 492, B 9; matches on record A 4, B 273; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28DARAMB-AMB  (YES = LUCIANO EMANUEL AMBROGI)
Model: 89%
Kalshi: 34%
Gap: +55 pp
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
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juan Sebastian Dominguez Collado vs Aydan Gomez Osorio -- M15 Pembroke R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28DOMGOM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Sebastian Dominguez Collado (`KXITFMATCH-26OCT28DOMGOM-DOM`) | 0.67 / 0.75 (100) | 71.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aydan Gomez Osorio (`KXITFMATCH-26OCT28DOMGOM-GOM`) | 0.24 / 0.29 (4) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hernando Jose Escurra Isnardi vs Joao Victor Couto Loureiro -- M15 João Pessoa R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200622:208533:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joao Victor Couto Loureiro (`KXITFMATCH-26OCT28ESCCOU-COU`) | 0.54 / 0.59 (100) | 56.5% | 60.2% | 59.5% | 57.1% [55.1%-60.0%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.7 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hernando Jose Escurra Isnardi (`KXITFMATCH-26OCT28ESCCOU-ESC`) | 0.40 / 0.44 (245) | 42.0% | 39.8% | 40.5% | 42.9% [40.0%-44.9%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.2 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 505.0, B 2307.0; serve-point win A 61.2%, B 36.8%; Elo A 1174.9, B 1215.8; model uncertainty 0.0245
* Form inputs: days since last match A 39, B 205; matches on record A 61, B 139; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valentin Garay vs Bastian Malla -- M15 João Pessoa R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:109334:212864:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentin Garay (`KXITFMATCH-26OCT28GARMAL-GAR`) | 0.09 / 0.10 (6) | 9.5% | 16.8% | 17.0% | 19.0% [16.6%-20.5%] | 13.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.3 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Bastian Malla (`KXITFMATCH-26OCT28GARMAL-MAL`) | 0.88 / 0.92 (128) | 90.0% | 83.2% | 83.0% | 81.0% [79.5%-83.4%] | 86.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.8 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 583.0, B 1148.0; serve-point win A 54.6%, B 38.1%; Elo A 1206.8, B 1450.1; model uncertainty 0.0196
* Form inputs: days since last match A 37, B 198; matches on record A 25, B 430; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.004, surface_dev_loose -0.011, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sander Jong vs Asahi Harazaki -- M25 Norman OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210093:211551:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Asahi Harazaki (`KXITFMATCH-26OCT28JONHAR-HAR`) | 0.17 / 0.19 (3) | 18.0% | 22.8% | 40.5% | 23.2% [20.2%-25.9%] | 20.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sander Jong (`KXITFMATCH-26OCT28JONHAR-JON`) | 0.79 / 0.82 (112) | 80.5% | 77.2% | 59.5% | 76.8% [74.1%-79.8%] | 79.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.3 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1243.0, B 353.0; serve-point win A 65.6%, B 40.3%; Elo A 1532.2, B 1292.5; model uncertainty 0.0288
* Form inputs: days since last match A 9, B 457; matches on record A 129, B 16; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lazar Markovic vs Brendan McDonald -- M15 Pembroke R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28MARMCD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lazar Markovic (`KXITFMATCH-26OCT28MARMCD-MAR`) | 0.25 / 0.27 (0) | 26.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Brendan McDonald (`KXITFMATCH-26OCT28MARMCD-MCD`) | 0.72 / 0.76 (68) | 74.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alejandro Melero Kretzer vs Aidan Mchugh -- M25 Norman OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202420:212024:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aidan Mchugh (`KXITFMATCH-26OCT28MELMCH-MCH`) | 0.86 / 0.87 (86) | 86.5% | 88.3% | 78.5% | 84.7% [84.1%-85.6%] | 85.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alejandro Melero Kretzer (`KXITFMATCH-26OCT28MELMCH-MEL`) | 0.10 / 0.12 (8) | 11.0% | 11.7% | 21.5% | 15.3% [14.4%-15.9%] | 14.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 272.0, B 3842.0; serve-point win A 55.1%, B 35.7%; Elo A 1195.6, B 1511.0; model uncertainty 0.0076
* Form inputs: days since last match A 457, B 296; matches on record A 38, B 477; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Neos / Tsitsipas vs Orlov / Scaglia -- M25 Malta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28NEOTSIORLSCA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Neos / Tsitsipas (`KXITFDOUBLES-26OCT28NEOTSIORLSCA-NEOTSI`) | 0.54 / 0.72 (89) | 63.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Orlov / Scaglia (`KXITFDOUBLES-26OCT28NEOTSIORLSCA-ORLSCA`) | 0.23 / 0.40 (41) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Pedro Petroski Rocha vs Tyler Mercier -- M15 Pembroke R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28PETMER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tyler Mercier (`KXITFMATCH-26OCT28PETMER-MER`) | 0.55 / 0.59 (66) | 57.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pedro Petroski Rocha (`KXITFMATCH-26OCT28PETMER-PET`) | 0.41 / 0.43 (0) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Michaela Bayerlova vs Anastasia Kulikova -- W75 Toronto R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214741:215693:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michaela Bayerlova (`KXITFWMATCH-26OCT28BAYKUL-BAY`) | 0.14 / 0.17 (100) | 15.5% | 18.2% | 27.9% | 25.7% [22.8%-27.9%] | 17.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +2.7 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anastasia Kulikova (`KXITFWMATCH-26OCT28BAYKUL-KUL`) | 0.81 / 0.85 (20) | 83.0% | 81.8% | 72.1% | 74.3% [72.1%-77.2%] | 82.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.2 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1530.0, B 1819.0; serve-point win A 51.1%, B 42.1%; Elo A 1338.0, B 1539.8; model uncertainty 0.0255
* Form inputs: days since last match A 115, B 30; matches on record A 350, B 416; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.022, surface_dev_loose -0.025, surface_dev_tight +0.017
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andrea Cabio vs Valentina Ryser -- W75 Toronto R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220489:267458:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea Cabio (`KXITFWMATCH-26OCT28CABRYS-CAB`) | 0.10 / 0.11 (10) | 10.5% | 5.4% | 17.5% | 13.0% [10.7%-14.7%] | 13.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valentina Ryser (`KXITFWMATCH-26OCT28CABRYS-RYS`) | 0.88 / 0.90 (350) | 89.0% | 94.6% | 82.5% | 87.1% [85.3%-89.3%] | 86.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.6 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 318.0, B 3017.0; serve-point win A 51.3%, B 36.4%; Elo A 1271.2, B 1611.7; model uncertainty 0.0199
* Form inputs: days since last match A 233, B 50; matches on record A 22, B 392; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.017, surface_dev_loose -0.003, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cascino / Feng vs Babel / Berecoechea -- W75 Poitiers QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28CASFENBABBER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Babel / Berecoechea (`KXITFWDOUBLES-26OCT28CASFENBABBER-BABBER`) | 0.06 / 0.20 (3) | 13.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cascino / Feng (`KXITFWDOUBLES-26OCT28CASFENBABBER-CASFEN`) | 0.75 / 0.91 (2) | 83.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Thara Gowda vs Anna Rogers -- W75 Toronto R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28GOWROG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thara Gowda (`KXITFWMATCH-26OCT28GOWROG-GOW`) | 0.46 / 0.48 (66) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anna Rogers (`KXITFWMATCH-26OCT28GOWROG-ROG`) | 0.51 / 0.54 (176) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maria Kononova vs Barbora Palicova -- W100 New Braunfels TX R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215236:223323:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Kononova (`KXITFWMATCH-26OCT28KONPAL-KON`) | 0.03 / 0.05 (118) | 4.0% | 10.6% | 21.3% | 20.5% [17.6%-24.5%] | 5.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.6 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Barbora Palicova (`KXITFWMATCH-26OCT28KONPAL-PAL`) | 0.95 / 0.97 (261) | 96.0% | 89.4% | 78.7% | 79.5% [75.5%-82.4%] | 94.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.6 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 370.0, B 2850.0; serve-point win A 50.9%, B 39.7%; Elo A 1343.3, B 1576.8; model uncertainty 0.0345
* Form inputs: days since last match A 254, B 16; matches on record A 139, B 350; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.029, surface_pool_high +0.040, surface_dev_loose -0.011, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Shihomi Li Xuan Leong vs Alina Shcherbinina -- W35 Norman OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221278:263622:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shihomi Li Xuan Leong (`KXITFWMATCH-26OCT28LEOSHC-LEO`) | 0.20 / 0.23 (73) | 21.5% | 54.2% | 61.6% | 55.3% [55.3%-56.4%] | 21.9% | -- | 21.9% | MODEL_LONE_OUTLIER | PASS | +32.7 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Alina Shcherbinina (`KXITFWMATCH-26OCT28LEOSHC-SHC`) | 0.76 / 0.82 (852) | 79.0% | 45.8% | 38.4% | 44.7% [43.6%-44.7%] | 78.1% | -- | 78.1% | MODEL_LONE_OUTLIER | PASS | -33.2 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 969.0, B 127.0; serve-point win A 54.0%, B 46.8%; Elo A 1368.6, B 1330.3; model uncertainty 0.0054
* Form inputs: days since last match A 345, B 254; matches on record A 52, B 55; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28LEOSHC-LEO  (YES = Shihomi Li Xuan Leong)
Model: 54%
Kalshi: 22%
Gap: +33 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adla Lopez vs Alice Battesti -- W15 Sumter SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221963:262884:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alice Battesti (`KXITFWMATCH-26OCT28LOPBAT-BAT`) | 0.72 / 0.73 (17) | 72.5% | 72.7% | 40.5% | 57.4% [55.3%-59.5%] | 72.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Adla Lopez (`KXITFWMATCH-26OCT28LOPBAT-LOP`) | 0.27 / 0.28 (73) | 27.5% | 27.3% | 59.5% | 42.6% [40.5%-44.7%] | 27.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 402.0; serve-point win A 52.2%, B 43.3%; Elo A 1282.3, B 1335.2; model uncertainty 0.021
* Form inputs: days since last match A 1374, B 464; matches on record A 2, B 57; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.021, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Christasha McNeil vs Carolina Gomez -- W35 Norman OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222312:266937:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carolina Gomez (`KXITFWMATCH-26OCT28MCNGOM-GOM`) | 0.46 / 0.51 (15) | 48.5% | 24.2% | 42.6% | 29.8% [29.7%-29.8%] | -- | -- | -- | -- | PASS | -24.3 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Christasha McNeil (`KXITFWMATCH-26OCT28MCNGOM-MCN`) | 0.50 / 0.54 (203) | 52.0% | 75.8% | 57.4% | 70.2% [70.2%-70.3%] | -- | -- | -- | -- | PASS | +23.8 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1523.0, B 0.0; serve-point win A 58.1%, B 47.1%; Elo A 1474.0, B 1325.3; model uncertainty 0.0004
* Form inputs: days since last match A 359, B 835; matches on record A 49, B 40; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28MCNGOM-MCN  (YES = Christasha McNeil)
Model: 76%
Kalshi: 52%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Veronika Miroshnichenko vs Kristina Liutova -- W100 New Braunfels TX R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28MIRLIU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kristina Liutova (`KXITFWMATCH-26OCT28MIRLIU-LIU`) | 0.88 / 0.89 (446) | 88.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Veronika Miroshnichenko (`KXITFWMATCH-26OCT28MIRLIU-MIR`) | 0.11 / 0.14 (827) | 12.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bella Payne vs Kristina Paskauskas -- W35 Norman OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:258195:270080:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kristina Paskauskas (`KXITFWMATCH-26OCT28PAYPAS-PAS`) | 0.58 / 0.60 (97) | 59.0% | 41.1% | 28.8% | 43.1% [39.0%-46.8%] | -- | -- | -- | -- | PASS | -17.9 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Bella Payne (`KXITFWMATCH-26OCT28PAYPAS-PAY`) | 0.38 / 0.42 (18) | 40.0% | 58.9% | 71.2% | 56.9% [53.2%-61.0%] | -- | -- | -- | -- | PASS | +18.9 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1424.0, B 382.0; serve-point win A 55.5%, B 46.1%; Elo A 1457.4, B 1437.4; model uncertainty 0.0391
* Form inputs: days since last match A 95, B 331; matches on record A 30, B 101; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28PAYPAS-PAY  (YES = Bella Payne)
Model: 59%
Kalshi: 40%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kristina Penickova vs Astra Sharma -- W100 New Braunfels TX R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206292:266381:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kristina Penickova (`KXITFWMATCH-26OCT28PENSHA-PEN`) | 0.30 / 0.32 (297) | 31.0% | 30.0% | 50.0% | 38.7% [28.9%-44.3%] | 33.6% | -- | 33.6% | KALSHI_LONE_OUTLIER | WATCH | -1.0 pp | NORMAL | AGING | B / LIMITED | ALL_AGREE | VERIFIED |
| Astra Sharma (`KXITFWMATCH-26OCT28PENSHA-SHA`) | 0.69 / 0.70 (343) | 69.5% | 70.0% | 50.0% | 61.3% [55.7%-71.1%] | 66.4% | -- | 66.4% | KALSHI_LONE_OUTLIER | PASS | +0.5 pp | NORMAL | AGING | B / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 1178.0, B 2800.0; serve-point win A 56.7%, B 39.3%; Elo A 1497.9, B 1638.0; model uncertainty 0.0771
* Form inputs: days since last match A 63, B 42; matches on record A 39, B 423; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.030, surface_dev_loose +0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arantxa Rus vs Mayu Crossley -- W100 New Braunfels TX R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:201551:260714:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mayu Crossley (`KXITFWMATCH-26OCT28RUSCRO-CRO`) | 0.41 / 0.44 (22) | 42.5% | 37.6% | 53.7% | 41.6% [28.8%-48.4%] | 41.9% | -- | 41.9% | MODEL_LONE_OUTLIER | PASS | -4.9 pp | NORMAL | AGING | D / POOR | ALL_AGREE | VERIFIED |
| Arantxa Rus (`KXITFWMATCH-26OCT28RUSCRO-RUS`) | 0.56 / 0.58 (43) | 57.0% | 62.4% | 46.3% | 58.4% [51.6%-71.2%] | 58.1% | -- | 58.1% | MODEL_LONE_OUTLIER | PASS | +5.4 pp | NORMAL | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4567.0, B 1575.0; serve-point win A 56.5%, B 45.8%; Elo A 1695.7, B 1546.6; model uncertainty 0.098
* Form inputs: days since last match A 37, B 352; matches on record A 1205, B 81; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.021, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juliana Nicole Singeorzan vs Kallista Liu -- W15 Sumter SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264180:270414:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kallista Liu (`KXITFWMATCH-26OCT28SINLIU-LIU`) | 0.73 / 0.78 (219) | 75.5% | 74.9% | 58.0% | 57.5% [56.4%-58.0%] | -- | -- | -- | -- | PASS | -0.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Juliana Nicole Singeorzan (`KXITFWMATCH-26OCT28SINLIU-SIN`) | 0.22 / 0.25 (7) | 23.5% | 25.1% | 42.0% | 42.5% [42.0%-43.6%] | -- | -- | -- | -- | PASS | +1.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 123.0, B 1064.0; serve-point win A 49.8%, B 45.1%; Elo A 1242.3, B 1290.6; model uncertainty 0.0079
* Form inputs: days since last match A 254, B 205; matches on record A 2, B 41; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.011, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anastasia Sysoeva vs Malwina Rowinska -- W15 Sumter SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221688:260764:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Malwina Rowinska (`KXITFWMATCH-26OCT28SYSROW-ROW`) | 0.68 / 0.71 (139) | 69.5% | 18.7% | 32.9% | 29.1% [27.8%-30.5%] | 69.7% | -- | 69.7% | MODEL_LONE_OUTLIER | PASS | -50.8 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Anastasia Sysoeva (`KXITFWMATCH-26OCT28SYSROW-SYS`) | 0.29 / 0.31 (0) | 30.0% | 81.3% | 67.1% | 70.9% [69.5%-72.2%] | 30.3% | -- | 30.3% | MODEL_LONE_OUTLIER | PASS | +51.3 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 115.0, B 297.0; serve-point win A 54.9%, B 51.7%; Elo A 1348.6, B 1193.6; model uncertainty 0.0135
* Form inputs: days since last match A 345, B 205; matches on record A 106, B 27; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28SYSROW-SYS  (YES = Anastasia Sysoeva)
Model: 81%
Kalshi: 30%
Gap: +51 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.014, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lily Taylor vs Kennedy Drenser-Hagmann -- W35 Norman OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259576:270322:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kennedy Drenser-Hagmann (`KXITFWMATCH-26OCT28TAYDRE-DRE`) | 0.50 / 0.52 (102) | 51.0% | 53.9% | 33.5% | 49.5% [46.8%-51.1%] | -- | -- | -- | -- | PASS | +2.9 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lily Taylor (`KXITFWMATCH-26OCT28TAYDRE-TAY`) | 0.47 / 0.50 (5) | 48.5% | 46.1% | 66.5% | 50.5% [48.9%-53.2%] | -- | -- | -- | -- | PASS | -2.4 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 405.0, B 140.0; serve-point win A 54.4%, B 44.8%; Elo A 1358.7, B 1365.8; model uncertainty 0.0213
* Form inputs: days since last match A 443, B 93; matches on record A 31, B 5; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carmen Andreea Herea vs Carole Monnet -- WTA 125K Queretaro R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-29 00:10Z
* Current expected start: 2026-10-28 21:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-28 20:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Clay · scheduled 2026-10-29T00:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220733:260142:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carmen Andreea Herea (`KXWTACHALLENGERMATCH-26OCT28HERMON-HER`) | 0.21 / 0.22 (242) | 21.5% | 31.7% | 45.7% | 36.3% [30.5%-41.0%] | -- | -- | -- | -- | SHADOW_BET | +10.2 pp | REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carole Monnet (`KXWTACHALLENGERMATCH-26OCT28HERMON-MON`) | 0.76 / 0.78 (0) | 77.0% | 68.3% | 54.3% | 63.7% [59.0%-69.5%] | -- | -- | -- | -- | PASS | -8.7 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 799.0, B 3719.0; serve-point win A 49.5%, B 47.0%; Elo A 1528.7, B 1659.6; model uncertainty 0.0522
* Form inputs: days since last match A 2, B 14; matches on record A 107, B 521; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.020, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Jarno Jans / Joran Vliegen vs Maxwell Exsted / Cooper Woestendick -- ATP Challenger Sioux Falls R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-28T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28JANVLIEXSWOE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maxwell Exsted / Cooper Woestendick (`KXATPCHALLENGERDOUBLES-26OCT28JANVLIEXSWOE-EXSWOE`) | 0.23 / 0.35 (102) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jarno Jans / Joran Vliegen (`KXATPCHALLENGERDOUBLES-26OCT28JANVLIEXSWOE-JANVLI`) | 0.64 / 0.77 (100) | 70.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jody Maginley / Karl Poling vs Tom Hands / Matthew Summers -- ATP Challenger Sioux Falls R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-28T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28MAGPOLHANSUM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tom Hands / Matthew Summers (`KXATPCHALLENGERDOUBLES-26OCT28MAGPOLHANSUM-HANSUM`) | 0.51 / 0.62 (96) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jody Maginley / Karl Poling (`KXATPCHALLENGERDOUBLES-26OCT28MAGPOLHANSUM-MAGPOL`) | 0.38 / 0.49 (95) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Matylda Burylo vs Micol Salvadori -- W15 Taby R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222845:266406:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matylda Burylo (`KXITFWMATCH-26OCT28BURSAL-BUR`) | 0.73 / 0.77 (165) | 75.0% | 53.9% | 30.6% | 48.9% [45.2%-53.7%] | 69.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -21.1 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Micol Salvadori (`KXITFWMATCH-26OCT28BURSAL-SAL`) | 0.21 / 0.25 (2) | 23.0% | 46.1% | 69.4% | 51.1% [46.3%-54.8%] | 30.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +23.1 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 498.0, B 242.0; serve-point win A 54.9%, B 45.9%; Elo A 1246.2, B 1228.4; model uncertainty 0.0425
* Form inputs: days since last match A 240, B 198; matches on record A 42, B 28; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28BURSAL-SAL  (YES = Micol Salvadori)
Model: 46%
Kalshi: 23%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.011, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daems / Reusch vs Kostina / Sachenko -- W15 Essen R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28DAEREUKOSSAC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daems / Reusch (`KXITFWDOUBLES-26OCT28DAEREUKOSSAC-DAEREU`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kostina / Sachenko (`KXITFWDOUBLES-26OCT28DAEREUKOSSAC-KOSSAC`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Francesco Maestrelli vs Gabriel Diallo -- ATP Challenger Brest R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 21:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-28T21:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208353:209113:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriel Diallo (`KXATPCHALLENGERMATCH-26OCT28MAEDIA-DIA`) | 0.74 / 0.75 (31) | 74.5% | 73.1% | 65.0% | 68.5% [66.8%-70.2%] | 73.1% | 75.0% | 75.0% | MODEL_LONE_OUTLIER | PASS | -1.4 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Francesco Maestrelli (`KXATPCHALLENGERMATCH-26OCT28MAEDIA-MAE`) | 0.25 / 0.26 (1662) | 25.5% | 26.9% | 35.0% | 31.5% [29.8%-33.2%] | 26.9% | 25.4% | 25.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +1.4 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5113.0, B 5049.0; serve-point win A 64.6%, B 30.3%; Elo A 1593.9, B 1812.0; model uncertainty 0.0171
* Form inputs: days since last match A 10, B 10; matches on record A 367, B 302; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.009, surface_dev_loose +0.005, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Joaquin Aguilar Cardozo / Franco Roncadelli vs Karol Drzewiecki / Piotr Matuszewski -- ATP Challenger Guayaquil R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-28T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28AGURONDRZMAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joaquin Aguilar Cardozo / Franco Roncadelli (`KXATPCHALLENGERDOUBLES-26OCT28AGURONDRZMAT-AGURON`) | 0.32 / 0.37 (32) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Karol Drzewiecki / Piotr Matuszewski (`KXATPCHALLENGERDOUBLES-26OCT28AGURONDRZMAT-DRZMAT`) | 0.62 / 0.65 (39) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Felix Corwin vs Noah Zamora -- M25 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200228:212235:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felix Corwin (`KXITFMATCH-26OCT28CORZAM-COR`) | 0.43 / 0.45 (250) | 44.0% | 50.7% | 46.9% | 49.0% [47.4%-51.0%] | 43.9% | -- | 43.9% | MODEL_LONE_OUTLIER | WATCH | +6.7 pp | NORMAL | AGING | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Noah Zamora (`KXITFMATCH-26OCT28CORZAM-ZAM`) | 0.52 / 0.53 (53) | 52.5% | 49.3% | 53.1% | 51.0% [49.0%-52.6%] | 56.1% | -- | 56.1% | ALL_THREE_DISAGREE | PASS | -3.2 pp | NORMAL | AGING | C / LIMITED | EXTERNAL_OUTLIER | VERIFIED |

* Serve evidence (points): A 3058.0, B 1609.0; serve-point win A 59.3%, B 40.8%; Elo A 1407.6, B 1410.4; model uncertainty 0.0182
* Form inputs: days since last match A 198, B 212; matches on record A 371, B 41; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nikola Djosic vs Tanishk Konduri -- M25 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212149:214433:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikola Djosic (`KXITFMATCH-26OCT28DJOKON-DJO`) | 0.39 / 0.41 (232) | 40.0% | 37.7% | 34.2% | 35.7% [34.7%-36.7%] | 39.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.3 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tanishk Konduri (`KXITFMATCH-26OCT28DJOKON-KON`) | 0.58 / 0.59 (53) | 58.5% | 62.3% | 65.8% | 64.3% [63.3%-65.3%] | 60.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1050.0, B 349.0; serve-point win A 56.8%, B 40.8%; Elo A 1244.8, B 1342.9; model uncertainty 0.0104
* Form inputs: days since last match A 212, B 219; matches on record A 33, B 5; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zachary Fuchs / Brandon Perez vs Alan Magadan / Federico Zeballos -- ATP Challenger Guayaquil R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-28T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28FUCPERMAGZEB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zachary Fuchs / Brandon Perez (`KXATPCHALLENGERDOUBLES-26OCT28FUCPERMAGZEB-FUCPER`) | 0.33 / 0.38 (29) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alan Magadan / Federico Zeballos (`KXATPCHALLENGERDOUBLES-26OCT28FUCPERMAGZEB-MAGZEB`) | 0.61 / 0.64 (47) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Oliver OKONKWO vs Noah Johnston -- M25 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209115:213654:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Noah Johnston (`KXITFMATCH-26OCT28OKOJOH-JOH`) | 0.49 / 0.51 (1) | 50.0% | 40.8% | 53.0% | 51.5% [51.0%-51.5%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oliver OKONKWO (`KXITFMATCH-26OCT28OKOJOH-OKO`) | 0.48 / 0.49 (49) | 48.5% | 59.2% | 46.9% | 48.5% [48.5%-49.0%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.7 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1037.0, B 305.0; serve-point win A 62.7%, B 39.1%; Elo A 1250.3, B 1257.4; model uncertainty 0.0026
* Form inputs: days since last match A 30, B 352; matches on record A 43, B 11; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bruno (2002) Oliveira / Natan Rodrigues vs Gonzalo Villanueva / Carlos Maria Zarate -- ATP Challenger Guayaquil R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-28T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28OLIRODVILZAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bruno (2002) Oliveira / Natan Rodrigues (`KXATPCHALLENGERDOUBLES-26OCT28OLIRODVILZAR-OLIROD`) | 0.54 / 0.58 (48) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gonzalo Villanueva / Carlos Maria Zarate (`KXATPCHALLENGERDOUBLES-26OCT28OLIRODVILZAR-VILZAR`) | 0.40 / 0.45 (30) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Luca Preda vs David Fix -- M25 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210153:212203:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| David Fix (`KXITFMATCH-26OCT28PREFIX-FIX`) | 0.27 / 0.28 (748) | 27.5% | 16.3% | 26.2% | 24.4% [22.4%-26.2%] | 31.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.2 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luca Preda (`KXITFMATCH-26OCT28PREFIX-PRE`) | 0.68 / 0.73 (411) | 70.5% | 83.7% | 73.9% | 75.5% [73.8%-77.6%] | 68.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.2 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1752.0, B 838.0; serve-point win A 58.7%, B 48.7%; Elo A 1434.4, B 1235.7; model uncertainty 0.019
* Form inputs: days since last match A 338, B 436; matches on record A 54, B 57; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.017, surface_dev_loose +0.000, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luciana Agudelo vs Josefina Estevez -- W15 Neuquén R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-28T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260717:270250:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luciana Agudelo (`KXITFWMATCH-26OCT28AGUEST-AGU`) | 0.08 / 0.11 (166) | 9.5% | 33.9% | 29.1% | 44.6% [41.5%-45.7%] | 14.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +24.4 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Josefina Estevez (`KXITFWMATCH-26OCT28AGUEST-EST`) | 0.89 / 0.92 (303) | 90.5% | 66.1% | 70.9% | 55.4% [54.3%-58.5%] | 85.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -24.4 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 79.0, B 732.0; serve-point win A 47.3%, B 49.6%; Elo A 1262.7, B 1294.6; model uncertainty 0.0211
* Form inputs: days since last match A 366, B 289; matches on record A 2, B 55; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28AGUEST-AGU  (YES = Luciana Agudelo)
Model: 34%
Kalshi: 10%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.011, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arabarco / Pajello vs Morini / Portoman -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28ARAPAJMORPOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arabarco / Pajello (`KXITFWDOUBLES-26OCT28ARAPAJMORPOR-ARAPAJ`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Morini / Portoman (`KXITFWDOUBLES-26OCT28ARAPAJMORPOR-MORPOR`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Reese Brantmeier vs Hina Inoue -- W75 Toronto R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222034:222080:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Reese Brantmeier (`KXITFWMATCH-26OCT28BRAINO-BRA`) | 0.85 / 0.89 (240) | 87.0% | 56.2% | 22.9% | 37.7% [31.2%-46.8%] | 85.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -30.8 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hina Inoue (`KXITFWMATCH-26OCT28BRAINO-INO`) | 0.11 / 0.14 (2278) | 12.5% | 43.8% | 77.1% | 62.3% [53.2%-68.8%] | 14.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +31.3 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 133.0, B 2804.0; serve-point win A 59.6%, B 41.5%; Elo A 1565.6, B 1638.6; model uncertainty 0.078
* Form inputs: days since last match A 31, B 191; matches on record A 89, B 325; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28BRAINO-INO  (YES = Hina Inoue)
Model: 44%
Kalshi: 12%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.071, surface_pool_high -0.048, surface_dev_loose +0.001, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chukwumelije Clarke vs Allura Zamarripa -- W100 New Braunfels TX R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221440:269864:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chukwumelije Clarke (`KXITFWMATCH-26OCT28CLAZAM-CLA`) | 0.46 / 0.47 (98) | 46.5% | 34.0% | 49.5% | 48.4% [45.7%-50.5%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.5 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Allura Zamarripa (`KXITFWMATCH-26OCT28CLAZAM-ZAM`) | 0.53 / 0.54 (380) | 53.5% | 66.0% | 50.5% | 51.6% [49.5%-54.3%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +12.5 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 633.0, B 454.0; serve-point win A 52.2%, B 44.7%; Elo A 1421.4, B 1433.3; model uncertainty 0.024
* Form inputs: days since last match A 198, B 134; matches on record A 15, B 107; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.021, surface_dev_loose +0.011, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kayla Cross vs Linea Bajraliu -- W75 Toronto R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:239436:259996:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Linea Bajraliu (`KXITFWMATCH-26OCT28CROBAJ-BAJ`) | 0.41 / 0.45 (15) | 43.0% | 26.1% | 59.5% | 41.6% [27.0%-50.0%] | 44.8% | -- | 44.8% | MODEL_LONE_OUTLIER | PASS | -16.9 pp | HIGH_REVIEW | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Kayla Cross (`KXITFWMATCH-26OCT28CROBAJ-CRO`) | 0.54 / 0.56 (19) | 55.0% | 73.9% | 40.5% | 58.4% [50.0%-73.0%] | 55.2% | -- | 55.2% | MODEL_LONE_OUTLIER | WATCH | +18.9 pp | HIGH_REVIEW | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2619.0, B 1577.0; serve-point win A 57.7%, B 47.1%; Elo A 1641.7, B 1450.1; model uncertainty 0.1151
* Form inputs: days since last match A 44, B 113; matches on record A 237, B 46; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28CROBAJ-CRO  (YES = Kayla Cross)
Model: 74%
Kalshi: 55%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.021, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Foretz / Martynov vs Marie Dittmann / Otzipka -- W75 Poitiers R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28FORMARMAROTZ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Foretz / Martynov (`KXITFWDOUBLES-26OCT28FORMARMAROTZ-FORMAR`) | 0.34 / 0.53 (53) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marie Dittmann / Otzipka (`KXITFWDOUBLES-26OCT28FORMARMAROTZ-MAROTZ`) | 0.40 / 0.60 (7) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Thea Frodin vs Xinyu Gao -- W100 New Braunfels TX R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214386:264140:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thea Frodin (`KXITFWMATCH-26OCT28FROGAO-FRO`) | 0.40 / 0.41 (34) | 40.5% | 10.3% | 22.1% | 16.6% [13.2%-18.4%] | 40.9% | -- | 40.9% | MODEL_LONE_OUTLIER | PASS | -30.2 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Xinyu Gao (`KXITFWMATCH-26OCT28FROGAO-GAO`) | 0.57 / 0.60 (1) | 58.5% | 89.7% | 77.9% | 83.4% [81.7%-86.8%] | 59.1% | -- | 59.1% | MODEL_LONE_OUTLIER | WATCH | +31.2 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1232.0, B 3203.0; serve-point win A 50.9%, B 39.6%; Elo A 1374.0, B 1711.8; model uncertainty 0.0257
* Form inputs: days since last match A 57, B 25; matches on record A 36, B 419; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28FROGAO-GAO  (YES = Xinyu Gao)
Model: 90%
Kalshi: 58%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: B (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, SURFACE_DATA_THIN, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.001, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jenny Lim vs Francisca Jorge -- W75 Poitiers R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216055:247647:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisca Jorge (`KXITFWMATCH-26OCT28LIMJOR-JOR`) | 0.64 / 0.66 (78) | 65.0% | 72.1% | 57.9% | 61.5% [58.9%-68.9%] | 65.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.1 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jenny Lim (`KXITFWMATCH-26OCT28LIMJOR-LIM`) | 0.32 / 0.35 (38) | 33.5% | 27.9% | 42.1% | 38.5% [31.1%-41.1%] | 34.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -5.6 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2154.0, B 3145.0; serve-point win A 53.0%, B 42.6%; Elo A 1542.2, B 1661.5; model uncertainty 0.0499
* Form inputs: days since last match A 198, B 13; matches on record A 185, B 460; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.025, surface_pool_high +0.021, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuki Naito vs Anne Christine Lutkemeyer -- W100 New Braunfels TX R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28NAILUT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anne Christine Lutkemeyer (`KXITFWMATCH-26OCT28NAILUT-LUT`) | 0.26 / 0.29 (123) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yuki Naito (`KXITFWMATCH-26OCT28NAILUT-NAI`) | 0.70 / 0.73 (3) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carson Tanguilig vs Jule Niemeier -- W75 Toronto R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215898:221624:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jule Niemeier (`KXITFWMATCH-26OCT28TANNIE-NIE`) | 0.50 / 0.55 (378) | 52.5% | 69.3% | 37.9% | 56.4% [45.7%-72.6%] | 53.8% | -- | 53.8% | MODEL_LONE_OUTLIER | WATCH | +16.8 pp | HIGH_REVIEW | AGING | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Carson Tanguilig (`KXITFWMATCH-26OCT28TANNIE-TAN`) | 0.44 / 0.47 (28) | 45.5% | 30.7% | 62.1% | 43.6% [27.4%-54.3%] | 46.2% | -- | 46.2% | MODEL_LONE_OUTLIER | PASS | -14.8 pp | REVIEW | AGING | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1314.0, B 3031.0; serve-point win A 51.8%, B 44.4%; Elo A 1444.9, B 1599.2; model uncertainty 0.1345
* Form inputs: days since last match A 191, B 52; matches on record A 33, B 381; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28TANNIE-NIE  (YES = Jule Niemeier)
Model: 69%
Kalshi: 52%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.042, surface_pool_high +0.053, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sophie Williams vs Yael Saffar -- W15 Sumter SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221633:270469:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yael Saffar (`KXITFWMATCH-26OCT28WILSAF-SAF`) | 0.77 / 0.80 (2) | 78.5% | 69.7% | 67.6% | 62.6% [61.6%-63.6%] | 76.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sophie Williams (`KXITFWMATCH-26OCT28WILSAF-WIL`) | 0.20 / 0.23 (8) | 21.5% | 30.3% | 32.4% | 37.4% [36.4%-38.4%] | 23.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 117.0, B 288.0; serve-point win A 51.1%, B 45.0%; Elo A 1266.4, B 1353.0; model uncertainty 0.0102
* Form inputs: days since last match A 366, B 191; matches on record A 35, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Renata Zarazua vs Lexington Reed -- W100 New Braunfels TX R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213887:239186:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lexington Reed (`KXITFWMATCH-26OCT28ZARREE-REE`) | 0.10 / 0.12 (1671) | 11.0% | 3.7% | 15.7% | 10.2% [6.8%-13.6%] | 13.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.3 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Renata Zarazua (`KXITFWMATCH-26OCT28ZARREE-ZAR`) | 0.89 / 0.90 (245) | 89.5% | 96.3% | 84.4% | 89.8% [86.5%-93.2%] | 86.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.8 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4923.0, B 144.0; serve-point win A 62.1%, B 51.5%; Elo A 1765.5, B 1375.5; model uncertainty 0.0336
* Form inputs: days since last match A 18, B 331; matches on record A 698, B 98; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.029, surface_pool_high -0.034, surface_dev_loose +0.000, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bilicic / Wriedt vs Degroot / Simons -- M15 Pembroke R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28BILWRIDEGSIM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bilicic / Wriedt (`KXITFDOUBLES-26OCT28BILWRIDEGSIM-BILWRI`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Degroot / Simons (`KXITFDOUBLES-26OCT28BILWRIDEGSIM-DEGSIM`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dobek / Van Orderlain vs Bicknell / Cicma -- M15 Pembroke R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28DOBVANBICCIC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bicknell / Cicma (`KXITFDOUBLES-26OCT28DOBVANBICCIC-BICCIC`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dobek / Van Orderlain (`KXITFDOUBLES-26OCT28DOBVANBICCIC-DOBVAN`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alastair Gray vs Emanuel Ivanisevic -- M25 Norman OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202400:212924:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alastair Gray (`KXITFMATCH-26OCT28GRAIVA-GRA`) | 0.89 / 0.93 (1) | 91.0% | 93.5% | 94.8% | 91.4% [89.5%-94.1%] | 89.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.5 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Emanuel Ivanisevic (`KXITFMATCH-26OCT28GRAIVA-IVA`) | 0.06 / 0.09 (6) | 7.5% | 6.5% | 5.2% | 8.6% [5.9%-10.5%] | 10.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.0 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3694.0, B 679.0; serve-point win A 66.8%, B 45.1%; Elo A 1601.1, B 1225.7; model uncertainty 0.0228
* Form inputs: days since last match A 44, B 170; matches on record A 326, B 19; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Theo Papamalamis vs Alex Rybakov -- M25 Norman OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126206:210494:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theo Papamalamis (`KXITFMATCH-26OCT28PAPRYB-PAP`) | 0.44 / 0.49 (610) | 46.5% | 45.1% | 53.6% | 41.8% [31.2%-46.4%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.4 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alex Rybakov (`KXITFMATCH-26OCT28PAPRYB-RYB`) | 0.51 / 0.54 (1) | 52.5% | 54.9% | 46.4% | 58.2% [53.6%-68.8%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +2.4 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1714.0, B 3082.0; serve-point win A 59.0%, B 40.1%; Elo A 1462.3, B 1614.4; model uncertainty 0.0761
* Form inputs: days since last match A 296, B 9; matches on record A 89, B 499; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Johan Alexander Rodriguez vs Giles Hussey -- M25 Norman OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28RODHUS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giles Hussey (`KXITFMATCH-26OCT28RODHUS-HUS`) | 0.65 / 0.67 (83) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Johan Alexander Rodriguez (`KXITFMATCH-26OCT28RODHUS-ROD`) | 0.30 / 0.35 (30) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ilia Snitari vs Walid Ahouda -- M25 Norman OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208206:209943:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Walid Ahouda (`KXITFMATCH-26OCT28SNIAHO-AHO`) | 0.39 / 0.43 (152) | 41.0% | 23.4% | 40.7% | 24.5% [22.7%-26.2%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -17.6 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Ilia Snitari (`KXITFMATCH-26OCT28SNIAHO-SNI`) | 0.55 / 0.58 (122) | 56.5% | 76.5% | 59.3% | 75.5% [73.8%-77.3%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +20.1 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 804.0, B 208.0; serve-point win A 61.6%, B 44.0%; Elo A 1452.1, B 1236.1; model uncertainty 0.0174
* Form inputs: days since last match A 156, B 387; matches on record A 219, B 36; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28SNIAHO-SNI  (YES = Ilia Snitari)
Model: 77%
Kalshi: 56%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Laura Brunkel vs Dana Guzman -- W35 Norman OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221834:264966:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Laura Brunkel (`KXITFWMATCH-26OCT28BRUGUZ-BRU`) | 0.04 / 0.06 (1514) | 5.0% | 25.0% | 28.3% | 27.4% [25.6%-29.6%] | 6.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +20.0 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dana Guzman (`KXITFWMATCH-26OCT28BRUGUZ-GUZ`) | 0.92 / 0.96 (206) | 94.0% | 75.0% | 71.7% | 72.6% [70.4%-74.4%] | 93.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.0 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 865.0, B 812.0; serve-point win A 51.1%, B 43.9%; Elo A 1392.0, B 1563.9; model uncertainty 0.0201
* Form inputs: days since last match A 450, B 254; matches on record A 29, B 42; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28BRUGUZ-BRU  (YES = Laura Brunkel)
Model: 25%
Kalshi: 5%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuliya Hatouka vs Jenna DeFalco -- W35 Norman OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216013:221914:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jenna DeFalco (`KXITFWMATCH-26OCT28HATDEF-DEF`) | 0.37 / 0.42 (34) | 39.5% | 23.4% | 29.1% | 27.3% [26.4%-28.6%] | 40.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -16.1 pp | HIGH_REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuliya Hatouka (`KXITFWMATCH-26OCT28HATDEF-HAT`) | 0.56 / 0.62 (172) | 59.0% | 76.6% | 70.9% | 72.7% [71.4%-73.6%] | 59.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +17.6 pp | HIGH_REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2126.0, B 1687.0; serve-point win A 53.8%, B 51.6%; Elo A 1650.5, B 1461.4; model uncertainty 0.0113
* Form inputs: days since last match A 205, B 184; matches on record A 378, B 247; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28HATDEF-HAT  (YES = Yuliya Hatouka)
Model: 77%
Kalshi: 59%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gloriana Nahum vs Capucine Jauffret -- W35 Norman OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:263981:264230:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Capucine Jauffret (`KXITFWMATCH-26OCT28NAHJAU-JAU`) | 0.39 / 0.44 (45) | 41.5% | 46.7% | 49.5% | 41.0% [37.4%-43.1%] | -- | -- | -- | -- | PASS | +5.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gloriana Nahum (`KXITFWMATCH-26OCT28NAHJAU-NAH`) | 0.54 / 0.59 (60) | 56.5% | 53.3% | 50.5% | 59.0% [56.9%-62.6%] | -- | -- | -- | -- | PASS | -3.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 868.0, B 767.0; serve-point win A 51.8%, B 48.8%; Elo A 1441.3, B 1349.1; model uncertainty 0.0284
* Form inputs: days since last match A 478, B 63; matches on record A 33, B 24; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Salakthip Ounmuang vs Yara Bartashevich -- W35 Norman OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28OUNBAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yara Bartashevich (`KXITFWMATCH-26OCT28OUNBAR-BAR`) | 0.57 / 0.62 (64) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Salakthip Ounmuang (`KXITFWMATCH-26OCT28OUNBAR-OUN`) | 0.35 / 0.37 (39) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hynek Barton / Maks Kasnikowski vs Daniel Milavsky / Braden Shick -- ATP Challenger Sioux Falls R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-28T22:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28BARKASMILSHI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hynek Barton / Maks Kasnikowski (`KXATPCHALLENGERDOUBLES-26OCT28BARKASMILSHI-BARKAS`) | 0.06 / 0.94 (850) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daniel Milavsky / Braden Shick (`KXATPCHALLENGERDOUBLES-26OCT28BARKASMILSHI-MILSHI`) | 0.06 / 0.94 (850) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Mees Rottgering vs Kaylan Bigun -- ATP Challenger Sioux Falls R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 22:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-28T22:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210744:212219:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kaylan Bigun (`KXATPCHALLENGERMATCH-26OCT28ROTBIG-BIG`) | 0.22 / 0.23 (1257) | 22.5% | 13.1% | 14.7% | 14.4% [13.5%-16.2%] | 24.3% | 23.2% | 23.2% | MODEL_LONE_OUTLIER | PASS | -9.4 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Mees Rottgering (`KXATPCHALLENGERMATCH-26OCT28ROTBIG-ROT`) | 0.77 / 0.78 (3569) | 77.5% | 86.9% | 85.3% | 85.6% [83.8%-86.5%] | 75.7% | 78.0% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +9.4 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2684.0, B 2053.0; serve-point win A 63.7%, B 45.0%; Elo A 1621.0, B 1305.5; model uncertainty 0.0139
* Form inputs: days since last match A 9, B 9; matches on record A 122, B 94; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.003, surface_dev_loose +0.009, surface_dev_tight -0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Selena Janicijevic vs Elizabeth Mandlik -- WTA 125K Queretaro R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-29 02:00Z
* Current expected start: 2026-10-28 23:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-28 22:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Clay · scheduled 2026-10-29T02:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:216097:221911:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Selena Janicijevic (`KXWTACHALLENGERMATCH-26OCT28JANMAN-JAN`) | 0.34 / 0.35 (2) | 34.5% | 41.2% | 50.0% | 49.5% [44.2%-51.6%] | -- | -- | -- | -- | SHADOW_BET | +6.8 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elizabeth Mandlik (`KXWTACHALLENGERMATCH-26OCT28JANMAN-MAN`) | 0.65 / 0.68 (111) | 66.5% | 58.8% | 50.0% | 50.5% [48.4%-55.8%] | -- | -- | -- | -- | PASS | -7.8 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4073.0, B 3798.0; serve-point win A 53.6%, B 44.8%; Elo A 1600.3, B 1612.5; model uncertainty 0.0372
* Form inputs: days since last match A 1, B 64; matches on record A 365, B 367; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.021, surface_dev_loose +0.005, surface_dev_tight -0.016
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Julian Alonso vs Alejandro Arcila -- M25 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:103031:213137:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julian Alonso (`KXITFMATCH-26OCT28ALOARC-ALO`) | 0.66 / 0.71 (1) | 68.5% | 73.7% | 80.2% | 77.2% [72.4%-80.9%] | -- | -- | -- | -- | PASS | +5.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alejandro Arcila (`KXITFMATCH-26OCT28ALOARC-ARC`) | 0.28 / 0.29 (3201) | 28.5% | 26.3% | 19.8% | 22.8% [19.1%-27.6%] | -- | -- | -- | -- | PASS | -2.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 791.0, B 475.0; serve-point win A 64.9%, B 40.1%; Elo A 1419.0, B 1221.4; model uncertainty 0.0423
* Form inputs: days since last match A 296, B 408; matches on record A 376, B 10; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.036, surface_pool_high -0.048, surface_dev_loose +0.006, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bojicic Ono / Pagotto vs Bini / Braga -- M15 João Pessoa R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28BOJPAGBINBRA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bini / Braga (`KXITFDOUBLES-26OCT28BOJPAGBINBRA-BINBRA`) | 0.31 / 0.49 (49) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bojicic Ono / Pagotto (`KXITFDOUBLES-26OCT28BOJPAGBINBRA-BOJPAG`) | 0.45 / 0.62 (7) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## William Jansen vs Xavier Calvelo -- M25 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-28T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28JANCAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xavier Calvelo (`KXITFMATCH-26OCT28JANCAL-CAL`) | 0.13 / 0.15 (6) | 14.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| William Jansen (`KXITFMATCH-26OCT28JANCAL-JAN`) | 0.82 / 0.86 (1) | 84.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andrew Johnson vs Xavi Palomar -- M25 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213965:214015:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrew Johnson (`KXITFMATCH-26OCT28JOHPAL-JOH`) | 0.86 / 0.90 (72) | 88.0% | 93.3% | 96.2% | 90.6% [86.5%-94.0%] | 85.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.3 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xavi Palomar (`KXITFMATCH-26OCT28JOHPAL-PAL`) | 0.11 / 0.12 (237) | 11.5% | 6.7% | 3.8% | 9.4% [5.9%-13.5%] | 14.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.8 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1199.0, B 617.0; serve-point win A 60.3%, B 50.9%; Elo A 1478.3, B 1152.8; model uncertainty 0.0378
* Form inputs: days since last match A 63, B 191; matches on record A 22, B 12; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.004, surface_dev_loose +0.013, surface_dev_tight -0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ofek Shimanov vs Alexander Rozin -- M25 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210645:tml:R0KK:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Rozin (`KXITFMATCH-26OCT28SHIROZ-ROZ`) | 0.70 / 0.74 (1) | 72.0% | 52.1% | 59.7% | 57.2% [56.2%-58.7%] | -- | -- | -- | -- | PASS | -19.9 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ofek Shimanov (`KXITFMATCH-26OCT28SHIROZ-SHI`) | 0.25 / 0.29 (100) | 27.0% | 47.9% | 40.3% | 42.8% [41.3%-43.8%] | -- | -- | -- | -- | PASS | +20.9 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 305.0, B 119.0; serve-point win A 59.6%, B 39.9%; Elo A 1258.9, B 1310.8; model uncertainty 0.0128
* Form inputs: days since last match A 232, B 107; matches on record A 58, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28SHIROZ-SHI  (YES = Ofek Shimanov)
Model: 48%
Kalshi: 27%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Akli / Sieg vs Alexander / Mercier -- W75 Toronto R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28AKLSIEALEMER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Akli / Sieg (`KXITFWDOUBLES-26OCT28AKLSIEALEMER-AKLSIE`) | 0.68 / 0.91 (2) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander / Mercier (`KXITFWDOUBLES-26OCT28AKLSIEALEMER-ALEMER`) | 0.05 / 0.25 (33) | 15.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ariana Arseneault vs Sara Saito -- W75 Toronto R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220502:260170:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ariana Arseneault (`KXITFWMATCH-26OCT28ARSSAI-ARS`) | 0.54 / 0.55 (60) | 54.5% | 41.0% | 61.6% | 51.6% [37.9%-58.0%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.5 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sara Saito (`KXITFWMATCH-26OCT28ARSSAI-SAI`) | 0.44 / 0.45 (94) | 44.5% | 59.0% | 38.4% | 48.4% [42.0%-62.1%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +14.5 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2049.0, B 3341.0; serve-point win A 52.3%, B 46.0%; Elo A 1496.9, B 1574.9; model uncertainty 0.1003
* Form inputs: days since last match A 37, B 30; matches on record A 129, B 198; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.032, surface_dev_loose +0.016, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Liv Boulard vs Harmony Tan -- W75 Poitiers R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211552:260185:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liv Boulard (`KXITFWMATCH-26OCT28BOUTAN-BOU`) | 0.04 / 0.06 (34) | 5.0% | 3.2% | 5.0% | 6.3% [5.1%-7.3%] | 8.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.8 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Harmony Tan (`KXITFWMATCH-26OCT28BOUTAN-TAN`) | 0.91 / 0.95 (3) | 93.0% | 96.8% | 95.0% | 93.7% [92.7%-94.9%] | 91.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.8 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 476.0, B 3731.0; serve-point win A 48.9%, B 37.0%; Elo A 1244.6, B 1710.5; model uncertainty 0.0111
* Form inputs: days since last match A 114, B 14; matches on record A 50, B 652; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.012, surface_pool_high +0.010, surface_dev_loose -0.003, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Boyden / Moyano vs Abril Bruno / Victoria Gobbi Monllau -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28BOYMOYABRVIC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Abril Bruno / Victoria Gobbi Monllau (`KXITFWDOUBLES-26OCT28BOYMOYABRVIC-ABRVIC`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Boyden / Moyano (`KXITFWDOUBLES-26OCT28BOYMOYABRVIC-BOYMOY`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Savannah Broadus vs Akasha Urhobo -- W100 New Braunfels TX R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221221:259857:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Savannah Broadus (`KXITFWMATCH-26OCT28BROURH-BRO`) | 0.30 / 0.32 (29) | 31.0% | 23.3% | 34.0% | 33.1% [27.0%-37.5%] | 31.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.7 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Akasha Urhobo (`KXITFWMATCH-26OCT28BROURH-URH`) | 0.66 / 0.70 (557) | 68.0% | 76.7% | 66.0% | 66.9% [62.5%-73.0%] | 68.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.7 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 898.0, B 3335.0; serve-point win A 53.1%, B 41.4%; Elo A 1496.9, B 1625.7; model uncertainty 0.0525
* Form inputs: days since last match A 65, B 65; matches on record A 63, B 174; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.042, surface_pool_high +0.039, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Combs / De Los Reyes vs Fagan / Mendell -- W15 Sumter SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28COMDELFAGMEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Combs / De Los Reyes (`KXITFWDOUBLES-26OCT28COMDELFAGMEN-COMDEL`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fagan / Mendell (`KXITFWDOUBLES-26OCT28COMDELFAGMEN-FAGMEN`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Koreshkova / Simunyu vs Diianni / Lucia Diianni -- W15 Sumter SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28KORSIMDIILUC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diianni / Lucia Diianni (`KXITFWDOUBLES-26OCT28KORSIMDIILUC-DIILUC`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Koreshkova / Simunyu (`KXITFWDOUBLES-26OCT28KORSIMDIILUC-KORSIM`) | 0.05 / 0.91 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## McAdoo / Ngounoue vs Chavez / Nicholson -- W75 Toronto R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28MCANGOCHANIC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chavez / Nicholson (`KXITFWDOUBLES-26OCT28MCANGOCHANIC-CHANIC`) | 0.05 / 0.18 (30) | 11.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| McAdoo / Ngounoue (`KXITFWDOUBLES-26OCT28MCANGOCHANIC-MCANGO`) | 0.76 / 0.91 (2) | 83.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ella McDonald vs Elvina Kalieva -- W100 New Braunfels TX R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220722:259591:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elvina Kalieva (`KXITFWMATCH-26OCT28MCDKAL-KAL`) | 0.46 / 0.50 (82) | 48.0% | 73.7% | 63.0% | 63.5% [60.5%-69.3%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +25.7 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ella McDonald (`KXITFWMATCH-26OCT28MCDKAL-MCD`) | 0.50 / 0.53 (101) | 51.5% | 26.3% | 37.0% | 36.5% [30.6%-39.5%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -25.2 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1341.0, B 3992.0; serve-point win A 53.1%, B 42.1%; Elo A 1577.6, B 1683.1; model uncertainty 0.0444
* Form inputs: days since last match A 127, B 18; matches on record A 146, B 365; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28MCDKAL-KAL  (YES = Elvina Kalieva)
Model: 74%
Kalshi: 48%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.039, surface_pool_high +0.030, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Meabe / Zornada vs Doldan / Celina Sosa -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28MEAZORDOLCEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Doldan / Celina Sosa (`KXITFWDOUBLES-26OCT28MEAZORDOLCEL-DOLCEL`) | 0.05 / 0.23 (32) | 14.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Meabe / Zornada (`KXITFWDOUBLES-26OCT28MEAZORDOLCEL-MEAZOR`) | 0.70 / 0.91 (2) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Osuigwe / Smith vs Kha / Kunz -- W100 New Braunfels TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28OSUSMIKHAKUN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kha / Kunz (`KXITFWDOUBLES-26OCT28OSUSMIKHAKUN-KHAKUN`) | 0.05 / 0.06 (26) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Osuigwe / Smith (`KXITFWDOUBLES-26OCT28OSUSMIKHAKUN-OSUSMI`) | 0.88 / 0.96 (62) | 92.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Julieta Pareja vs Diae El Jardi -- W100 New Braunfels TX R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-28T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215696:264075:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diae El Jardi (`KXITFWMATCH-26OCT28PARELJ-ELJ`) | 0.03 / 0.04 (401) | 3.5% | 3.4% | 31.1% | 14.4% [9.4%-18.6%] | 4.3% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -0.1 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Julieta Pareja (`KXITFWMATCH-26OCT28PARELJ-PAR`) | 0.96 / 0.97 (535) | 96.5% | 96.6% | 68.9% | 85.6% [81.5%-90.6%] | 95.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.1 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1273.0, B 1043.0; serve-point win A 66.5%, B 47.6%; Elo A 1696.0, B 1249.2; model uncertainty 0.0459
* Form inputs: days since last match A 49, B 162; matches on record A 63, B 45; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high +0.000, surface_dev_loose +0.004, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Diego Hidalgo / Mariano Kestelboim vs Arklon Huertas Del Pino Cordova / Alexander Merino -- ATP Challenger Guayaquil R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 23:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-28T23:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28HIDKESHUEMER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diego Hidalgo / Mariano Kestelboim (`KXATPCHALLENGERDOUBLES-26OCT28HIDKESHUEMER-HIDKES`) | 0.05 / 0.95 (216) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arklon Huertas Del Pino Cordova / Alexander Merino (`KXATPCHALLENGERDOUBLES-26OCT28HIDKESHUEMER-HUEMER`) | 0.05 / 0.95 (216) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Gagliardo / Valente vs Braga / Jose Gutierrez -- M15 João Pessoa R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 23:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-28T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28GAGVALBRAJOS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Braga / Jose Gutierrez (`KXITFDOUBLES-26OCT28GAGVALBRAJOS-BRAJOS`) | 0.44 / 0.63 (67) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gagliardo / Valente (`KXITFDOUBLES-26OCT28GAGVALBRAJOS-GAGVAL`) | 0.31 / 0.50 (50) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Oskar Brostrom Poulsen / Nikola Slavic vs Miguel Angel Reyes-Varela / Reese Stalder -- ATP Challenger Sioux Falls R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-28 23:50Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-28T23:50:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28POUSLAREYSTA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oskar Brostrom Poulsen / Nikola Slavic (`KXATPCHALLENGERDOUBLES-26OCT28POUSLAREYSTA-POUSLA`) | 0.48 / 0.52 (236) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Miguel Angel Reyes-Varela / Reese Stalder (`KXATPCHALLENGERDOUBLES-26OCT28POUSLAREYSTA-REYSTA`) | 0.48 / 0.52 (236) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## LUCCA LIU vs Ryan Colby -- M15 Mazatlan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210242:213175:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ryan Colby (`KXITFMATCH-26OCT28LIUCOL-COL`) | 0.48 / 0.53 (53) | 50.5% | 53.7% | 45.8% | 54.2% [51.6%-57.3%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.2 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| LUCCA LIU (`KXITFMATCH-26OCT28LIUCOL-LIU`) | 0.46 / 0.49 (49) | 47.5% | 46.3% | 54.2% | 45.8% [42.7%-48.4%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.2 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 620.0, B 1404.0; serve-point win A 54.8%, B 44.5%; Elo A 1281.6, B 1337.1; model uncertainty 0.0285
* Form inputs: days since last match A 226, B 184; matches on record A 16, B 39; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elijah Strode vs Maxwell McKennon -- M15 Mazatlan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208297:210565:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maxwell McKennon (`KXITFMATCH-26OCT28STRMCK-MCK`) | 0.58 / 0.62 (198) | 60.0% | 67.8% | 68.5% | 66.7% [65.2%-68.2%] | -- | -- | -- | -- | PASS | +7.8 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elijah Strode (`KXITFMATCH-26OCT28STRMCK-STR`) | 0.38 / 0.40 (2) | 39.0% | 32.2% | 31.6% | 33.3% [31.8%-34.8%] | -- | -- | -- | -- | PASS | -6.8 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 869.0, B 3096.0; serve-point win A 65.6%, B 30.6%; Elo A 1288.4, B 1399.2; model uncertainty 0.0152
* Form inputs: days since last match A 471, B 184; matches on record A 57, B 140; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Burgic / Podhajecka vs Collins / Penickova -- W100 New Braunfels TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28BURPODCOLPEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Burgic / Podhajecka (`KXITFWDOUBLES-26OCT28BURPODCOLPEN-BURPOD`) | 0.05 / 0.23 (32) | 14.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Collins / Penickova (`KXITFWDOUBLES-26OCT28BURPODCOLPEN-COLPEN`) | 0.70 / 0.96 (40) | 83.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Dartron / Rouvroy vs Cabio / Taylor -- W75 Toronto R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28DARROUCABTAY:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cabio / Taylor (`KXITFWDOUBLES-26OCT28DARROUCABTAY-CABTAY`) | 0.05 / 0.10 (27) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dartron / Rouvroy (`KXITFWDOUBLES-26OCT28DARROUCABTAY-DARROU`) | 0.85 / 0.91 (2) | 88.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Finchelstein / Morena Medinaceli Lobos vs Markus / Jose Sanchez Uribe -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28FINMORMARJOS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Finchelstein / Morena Medinaceli Lobos (`KXITFWDOUBLES-26OCT28FINMORMARJOS-FINMOR`) | 0.05 / 0.58 (200) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Markus / Jose Sanchez Uribe (`KXITFWDOUBLES-26OCT28FINMORMARJOS-MARJOS`) | 0.17 / 0.91 (21) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Montserrat Marron Baruqui vs Ipek Oz -- W50 Morelia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213998:270445:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Montserrat Marron Baruqui (`KXITFWMATCH-26OCT28MAROZX-MAR`) | 0.03 / 0.04 (187) | 3.5% | 8.2% | 21.2% | 25.2% [18.9%-33.9%] | -- | -- | -- | -- | PASS | +4.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Ipek Oz (`KXITFWMATCH-26OCT28MAROZX-OZX`) | 0.96 / 0.97 (244) | 96.5% | 91.8% | 78.8% | 74.8% [66.1%-81.1%] | -- | -- | -- | -- | PASS | -4.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 273.0, B 2398.0; serve-point win A 48.9%, B 40.7%; Elo A 1300.5, B 1480.2; model uncertainty 0.0751
* Form inputs: days since last match A 233, B 50; matches on record A 4, B 487; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.063, surface_pool_high +0.087, surface_dev_loose -0.008, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bor Artnak vs Patrik Munkhammar -- M25 Norman OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 00:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210107:212894:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bor Artnak (`KXITFMATCH-26OCT28ARTMUN-ART`) | 0.76 / 0.77 (423) | 76.5% | 80.6% | 67.3% | 78.6% [75.8%-82.0%] | -- | -- | -- | -- | PASS | +4.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Patrik Munkhammar (`KXITFMATCH-26OCT28ARTMUN-MUN`) | 0.23 / 0.24 (32) | 23.5% | 19.4% | 32.7% | 21.4% [18.0%-24.2%] | -- | -- | -- | -- | PASS | -4.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3186.0, B 765.0; serve-point win A 59.9%, B 46.7%; Elo A 1494.0, B 1216.1; model uncertainty 0.0307
* Form inputs: days since last match A 40, B 296; matches on record A 251, B 18; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alec Deckers vs Marko Mesarovic -- M25 Norman OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 00:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207793:211670:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alec Deckers (`KXITFMATCH-26OCT28DECMES-DEC`) | 0.69 / 0.70 (2) | 69.5% | 75.5% | 55.8% | 71.3% [67.8%-75.0%] | -- | -- | -- | -- | PASS | +6.0 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marko Mesarovic (`KXITFMATCH-26OCT28DECMES-MES`) | 0.29 / 0.30 (168) | 29.5% | 24.5% | 44.2% | 28.7% [25.0%-32.2%] | -- | -- | -- | -- | PASS | -5.0 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2380.0, B 489.0; serve-point win A 68.8%, B 36.8%; Elo A 1440.3, B 1239.8; model uncertainty 0.036
* Form inputs: days since last match A 65, B 263; matches on record A 184, B 18; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kriish Tyagi vs Luca Pow -- M25 Norman OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 00:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210523:213806:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luca Pow (`KXITFMATCH-26OCT28TYAPOW-POW`) | 0.66 / 0.69 (231) | 67.5% | 68.0% | 74.1% | 59.7% [52.1%-66.1%] | -- | -- | -- | -- | PASS | +0.6 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kriish Tyagi (`KXITFMATCH-26OCT28TYAPOW-TYA`) | 0.30 / 0.33 (54) | 31.5% | 31.9% | 25.9% | 40.3% [33.9%-47.9%] | -- | -- | -- | -- | WATCH | +0.5 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 842.0, B 1328.0; serve-point win A 57.9%, B 38.5%; Elo A 1384.8, B 1389.0; model uncertainty 0.0701
* Form inputs: days since last match A 163, B 67; matches on record A 21, B 40; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tyler Zink vs Charlie Swaine -- M25 Norman OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 00:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208342:213590:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charlie Swaine (`KXITFMATCH-26OCT28ZINSWA-SWA`) | 0.10 / 0.11 (6) | 10.5% | 8.3% | 28.6% | 13.6% [13.6%-13.6%] | -- | -- | -- | -- | PASS | -2.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Tyler Zink (`KXITFMATCH-26OCT28ZINSWA-ZIN`) | 0.87 / 0.89 (102) | 88.0% | 91.7% | 71.4% | 86.5% [86.5%-86.5%] | -- | -- | -- | -- | PASS | +3.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 4139.0, B 0.0; serve-point win A 66.5%, B 44.3%; Elo A 1601.9, B 1285.8; model uncertainty 0.0
* Form inputs: days since last match A 165, B 744; matches on record A 197, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arina Bulatova vs Maria Berlanga Bandera -- W35 Norman OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 00:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221288:256712:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Berlanga Bandera (`KXITFWMATCH-26OCT28BULBER-BER`) | 0.50 / 0.58 (41) | 54.0% | 8.4% | 48.9% | 14.8% [14.2%-15.4%] | -- | -- | -- | -- | PASS | -45.6 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Arina Bulatova (`KXITFWMATCH-26OCT28BULBER-BUL`) | 0.41 / 0.47 (55) | 44.0% | 91.6% | 51.1% | 85.2% [84.6%-85.8%] | -- | -- | -- | -- | PASS | +47.6 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1763.0, B 48.0; serve-point win A 56.7%, B 53.6%; Elo A 1528.7, B 1210.1; model uncertainty 0.0062
* Form inputs: days since last match A 191, B 478; matches on record A 154, B 22; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28BULBER-BUL  (YES = Arina Bulatova)
Model: 92%
Kalshi: 44%
Gap: +48 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Reina Goto vs Aspen Schuman -- W35 Norman OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 00:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260737:260767:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Reina Goto (`KXITFWMATCH-26OCT28GOTSCH-GOT`) | 0.48 / 0.52 (91) | 50.0% | 48.9% | 48.4% | 47.9% [46.3%-48.9%] | -- | -- | -- | -- | PASS | -1.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aspen Schuman (`KXITFWMATCH-26OCT28GOTSCH-SCH`) | 0.47 / 0.50 (364) | 48.5% | 51.1% | 51.6% | 52.1% [51.1%-53.7%] | -- | -- | -- | -- | PASS | +2.6 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1864.0, B 437.0; serve-point win A 54.5%, B 45.2%; Elo A 1462.3, B 1474.8; model uncertainty 0.0133
* Form inputs: days since last match A 191, B 352; matches on record A 48, B 46; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Evialina Laskevich vs Mia Kupres -- W35 Norman OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 00:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222184:222377:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mia Kupres (`KXITFWMATCH-26OCT28LASKUP-KUP`) | 0.25 / 0.27 (155) | 26.0% | 19.4% | 54.8% | 24.4% [22.7%-27.0%] | -- | -- | -- | -- | PASS | -6.6 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Evialina Laskevich (`KXITFWMATCH-26OCT28LASKUP-LAS`) | 0.72 / 0.73 (92) | 72.5% | 80.6% | 45.2% | 75.6% [73.0%-77.3%] | -- | -- | -- | -- | PASS | +8.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 737.0, B 144.0; serve-point win A 57.7%, B 48.8%; Elo A 1693.5, B 1475.4; model uncertainty 0.0214
* Form inputs: days since last match A 254, B 94; matches on record A 167, B 64; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Martina Okalova vs Edda Mamedova -- W35 Norman OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 00:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214862:239422:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Edda Mamedova (`KXITFWMATCH-26OCT28OKAMAM-MAM`) | 0.63 / 0.65 (71) | 64.0% | 72.5% | 87.8% | 66.6% [52.1%-77.4%] | -- | -- | -- | -- | PASS | +8.5 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Martina Okalova (`KXITFWMATCH-26OCT28OKAMAM-OKA`) | 0.33 / 0.35 (144) | 34.0% | 27.5% | 12.2% | 33.4% [22.6%-47.9%] | -- | -- | -- | -- | PASS | -6.5 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1467.0, B 879.0; serve-point win A 49.3%, B 46.2%; Elo A 1512.5, B 1515.2; model uncertainty 0.1263
* Form inputs: days since last match A 95, B 254; matches on record A 201, B 91; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Micah Braswell vs Alexandr Cozbinov -- M25 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126612:209334:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Micah Braswell (`KXITFMATCH-26OCT28BRACOZ-BRA`) | 0.72 / 0.77 (872) | 74.5% | 69.7% | 71.9% | 69.7% [67.9%-72.8%] | -- | -- | -- | -- | PASS | -4.8 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Alexandr Cozbinov (`KXITFMATCH-26OCT28BRACOZ-COZ`) | 0.20 / 0.26 (100) | 23.0% | 30.3% | 28.1% | 30.3% [27.3%-32.1%] | -- | -- | -- | -- | PASS | +7.3 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1914.0, B 274.0; serve-point win A 62.3%, B 41.7%; Elo A 1518.9, B 1373.8; model uncertainty 0.0242
* Form inputs: days since last match A 268, B 219; matches on record A 89, B 247; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.013, surface_dev_loose +0.005, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nikita Filin vs Andreja Petrovic -- M25 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209914:212570:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikita Filin (`KXITFMATCH-26OCT28FILPET-FIL`) | 0.70 / 0.72 (1117) | 71.0% | 18.9% | 57.8% | 27.3% [23.3%-31.8%] | -- | -- | -- | -- | PASS | -52.1 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Andreja Petrovic (`KXITFMATCH-26OCT28FILPET-PET`) | 0.27 / 0.29 (153) | 28.0% | 81.1% | 42.2% | 72.7% [68.2%-76.7%] | -- | -- | -- | -- | PASS | +53.1 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 201.0, B 2276.0; serve-point win A 54.5%, B 38.8%; Elo A 1207.6, B 1408.7; model uncertainty 0.0425
* Form inputs: days since last match A 352, B 184; matches on record A 12, B 54; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28FILPET-PET  (YES = Andreja Petrovic)
Model: 81%
Kalshi: 28%
Gap: +53 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose +0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matthew Forbes vs Preston Stearns -- M25 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210475:212733:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthew Forbes (`KXITFMATCH-26OCT28FORSTE-FOR`) | 0.56 / 0.57 (62) | 56.5% | 71.4% | 52.4% | 60.1% [58.2%-61.8%] | -- | -- | -- | -- | PASS | +14.9 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Preston Stearns (`KXITFMATCH-26OCT28FORSTE-STE`) | 0.39 / 0.43 (22) | 41.0% | 28.6% | 47.6% | 39.9% [38.2%-41.8%] | -- | -- | -- | -- | PASS | -12.4 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 594.0, B 667.0; serve-point win A 68.2%, B 36.4%; Elo A 1361.1, B 1269.8; model uncertainty 0.0177
* Form inputs: days since last match A 65, B 352; matches on record A 18, B 22; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.005, surface_dev_loose -0.001, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Neo Niedner vs Jack Anthrop -- M25 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210102:210294:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jack Anthrop (`KXITFMATCH-26OCT28NIEANT-ANT`) | 0.81 / 0.85 (266) | 83.0% | 89.5% | 84.6% | 85.8% [85.1%-86.6%] | -- | -- | -- | -- | PASS | +6.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Neo Niedner (`KXITFMATCH-26OCT28NIEANT-NIE`) | 0.14 / 0.17 (123) | 15.5% | 10.5% | 15.4% | 14.2% [13.4%-14.9%] | -- | -- | -- | -- | PASS | -5.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 286.0, B 1030.0; serve-point win A 55.4%, B 34.9%; Elo A 1127.9, B 1442.4; model uncertainty 0.0076
* Form inputs: days since last match A 450, B 352; matches on record A 26, B 77; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.003, surface_dev_loose -0.005, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jo-Yee Chan vs Maria Fernanda Pantoja Espino -- W50 Morelia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28CHAPAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jo-Yee Chan (`KXITFWMATCH-26OCT28CHAPAN-CHA`) | 0.69 / 0.92 (2) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maria Fernanda Pantoja Espino (`KXITFWMATCH-26OCT28CHAPAN-PAN`) | 0.03 / 0.31 (2) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Justina Mikulskyte vs Caterina Odorizzi -- W50 Morelia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:212303:222613:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Justina Mikulskyte (`KXITFWMATCH-26OCT28MIKODO-MIK`) | 0.92 / 0.97 (215) | 94.5% | 95.2% | 93.4% | 92.7% [91.1%-94.1%] | -- | -- | -- | -- | PASS | +0.7 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Caterina Odorizzi (`KXITFWMATCH-26OCT28MIKODO-ODO`) | 0.03 / 0.05 (24) | 4.0% | 4.8% | 6.6% | 7.3% [5.9%-8.9%] | -- | -- | -- | -- | WATCH | +0.8 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3227.0, B 1069.0; serve-point win A 59.1%, B 53.3%; Elo A 1579.4, B 1147.2; model uncertainty 0.0147
* Form inputs: days since last match A 42, B 184; matches on record A 492, B 126; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.008, surface_dev_loose +0.005, surface_dev_tight -0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ingrid Carolina Millan Acosta vs Cadence Brace -- W50 Morelia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216311:223335:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cadence Brace (`KXITFWMATCH-26OCT28MILBRA-BRA`) | 0.91 / 0.97 (876) | 94.0% | 95.8% | 84.3% | 87.3% [86.2%-88.1%] | -- | -- | -- | -- | PASS | +1.8 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Ingrid Carolina Millan Acosta (`KXITFWMATCH-26OCT28MILBRA-MIL`) | 0.04 / 0.06 (13) | 5.0% | 4.2% | 15.7% | 12.7% [11.9%-13.9%] | -- | -- | -- | -- | PASS | -0.8 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 792.0, B 2165.0; serve-point win A 43.4%, B 43.7%; Elo A 1280.9, B 1646.4; model uncertainty 0.0098
* Form inputs: days since last match A 233, B 42; matches on record A 18, B 222; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Malaika Rapolu vs Maria Sholokhova -- W50 Morelia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222837:233718:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Malaika Rapolu (`KXITFWMATCH-26OCT28RAPSHO-RAP`) | 0.73 / 0.79 (170) | 76.0% | 66.3% | 16.7% | 41.5% [28.2%-66.6%] | -- | -- | -- | -- | PASS | -9.7 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Sholokhova (`KXITFWMATCH-26OCT28RAPSHO-SHO`) | 0.19 / 0.23 (321) | 21.0% | 33.7% | 83.3% | 58.5% [33.4%-71.8%] | -- | -- | -- | -- | PASS | +12.7 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1761.0, B 1181.0; serve-point win A 53.6%, B 49.6%; Elo A 1619.4, B 1517.5; model uncertainty 0.1921
* Form inputs: days since last match A 41, B 457; matches on record A 134, B 85; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.021, surface_dev_loose -0.021, surface_dev_tight +0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alycia Parks vs Kimberly Birrell -- WTA Tokyo R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-28 04:30Z
* Current expected start: 2026-10-29 01:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-29 00:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1260_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-28T04:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214040:219917:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kimberly Birrell (`KXWTAMATCH-26OCT27PARBIR-BIR`) | 0.60 / 0.61 (4726) | 60.5% | 58.7% | 57.8% | 59.3% [58.3%-60.3%] | -- | -- | -- | -- | PASS | -1.8 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alycia Parks (`KXWTAMATCH-26OCT27PARBIR-PAR`) | 0.39 / 0.40 (6906) | 39.5% | 41.3% | 42.2% | 40.7% [39.7%-41.7%] | -- | -- | -- | -- | PASS | +1.8 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5263.0, B 5020.0; serve-point win A 57.8%, B 40.5%; Elo A 1781.0, B 1874.5; model uncertainty 0.0102
* Form inputs: days since last match A 2, B 3; matches on record A 442, B 478; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT27PARBIR-22` Over 21.5 games: 0.51/0.52 mid 51.5%, model 63.6% (projection_v2.0 (prediction ledger)) -- gap +12.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT27PARBIR-2-PAR` Will Alycia Parks win set 2 in the Alycia Parks vs Kimberly Birrell match: 0.26/0.49 mid 37.5%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT27PARBIR-2-BIR` Will Kimberly Birrell win set 2 in the Alycia Parks vs Kimberly Birrell match: 0.37/0.87 mid 62.0%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap -6.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26OCT27PARBIR-17` Over 16.5 games: 0.85/0.94 mid 89.5%, model 94.6% (projection_v2.0 (prediction ledger)) -- gap +5.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT27PARBIR-27` Over 26.5 games: 0.28/0.58 mid 43.0%, model 40.3% (projection_v2.0 (prediction ledger)) -- gap -2.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT27PARBIR-1-BIR` Will Kimberly Birrell win set 1 in the Alycia Parks vs Kimberly Birrell match: 0.57/0.59 mid 58.0%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap -2.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT27PARBIR-1-PAR` Will Alycia Parks win set 1 in the Alycia Parks vs Kimberly Birrell match: 0.40/0.44 mid 42.0%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Matteo Covato vs Gerardo Delgado -- M15 Mazatlan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28COVDEL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Covato (`KXITFMATCH-26OCT28COVDEL-COV`) | 0.87 / 0.95 (115) | 91.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gerardo Delgado (`KXITFMATCH-26OCT28COVDEL-DEL`) | 0.05 / 0.10 (6) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rafael De Alba vs Oswaldo Alejandro Reyes Tirado -- M15 Mazatlan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208908:213783:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rafael De Alba (`KXITFMATCH-26OCT28DEAREY-DEA`) | 0.51 / 0.56 (100) | 53.5% | 50.5% | 50.0% | 47.4% [46.9%-51.1%] | -- | -- | -- | -- | PASS | -3.0 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oswaldo Alejandro Reyes Tirado (`KXITFMATCH-26OCT28DEAREY-REY`) | 0.43 / 0.45 (45) | 44.0% | 49.5% | 50.0% | 52.6% [48.9%-53.1%] | -- | -- | -- | -- | PASS | +5.5 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1439.0, B 411.0; serve-point win A 56.7%, B 43.4%; Elo A 1198.5, B 1215.7; model uncertainty 0.0211
* Form inputs: days since last match A 184, B 184; matches on record A 35, B 9; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Frazier Rengifo vs Jesse Flores -- M15 Mazatlan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132374:200105:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jesse Flores (`KXITFMATCH-26OCT28RENFLO-FLO`) | 0.71 / 0.73 (3) | 72.0% | 67.2% | 64.9% | 61.6% [60.1%-63.5%] | -- | -- | -- | -- | PASS | -4.8 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Frazier Rengifo (`KXITFMATCH-26OCT28RENFLO-REN`) | 0.27 / 0.29 (171) | 28.0% | 32.8% | 35.1% | 38.5% [36.5%-39.9%] | -- | -- | -- | -- | PASS | +4.8 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 468.0, B 2047.0; serve-point win A 59.9%, B 36.6%; Elo A 1234.6, B 1309.5; model uncertainty 0.0171
* Form inputs: days since last match A 184, B 184; matches on record A 29, B 190; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jenson Brooksby vs Dylan Dietrich -- ATP Challenger Sioux Falls R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-29T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202385:210157:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jenson Brooksby (`KXATPCHALLENGERMATCH-26OCT28BRODIE-BRO`) | 0.54 / 0.55 (36) | 54.5% | 68.3% | 38.6% | 59.0% [51.0%-66.1%] | -- | -- | -- | -- | WATCH | +13.8 pp | REVIEW | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dylan Dietrich (`KXATPCHALLENGERMATCH-26OCT28BRODIE-DIE`) | 0.44 / 0.46 (1228) | 45.0% | 31.7% | 61.4% | 41.0% [33.9%-49.0%] | -- | -- | -- | -- | PASS | -13.3 pp | REVIEW | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3795.0, B 1479.0; serve-point win A 65.0%, B 38.8%; Elo A 1850.5, B 1640.5; model uncertainty 0.0756
* Form inputs: days since last match A 9, B 30; matches on record A 294, B 66; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.024, surface_dev_loose -0.020, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Charlton / Hudd vs Nasridinov / Snitari -- M25 Norman OK R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28CHAHUDNASSNI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charlton / Hudd (`KXITFDOUBLES-26OCT28CHAHUDNASSNI-CHAHUD`) | 0.05 / 0.95 (38) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nasridinov / Snitari (`KXITFDOUBLES-26OCT28CHAHUDNASSNI-NASSNI`) | 0.05 / 0.95 (38) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Frusina / Papamalamis vs Kalina / Jeff Planinsek -- M25 Norman OK R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28FRUPAPKALJEF:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Frusina / Papamalamis (`KXITFDOUBLES-26OCT28FRUPAPKALJEF-FRUPAP`) | 0.39 / 0.63 (67) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kalina / Jeff Planinsek (`KXITFDOUBLES-26OCT28FRUPAPKALJEF-KALJEF`) | 0.31 / 0.55 (55) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Andre Souza vs Pedro Sakamoto -- M15 João Pessoa R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-29T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106203:214328:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pedro Sakamoto (`KXITFMATCH-26OCT28SOUSAK-SAK`) | 0.91 / 0.97 (319) | 94.0% | 89.0% | 87.7% | 83.9% [82.3%-85.8%] | -- | -- | -- | -- | PASS | -5.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Andre Souza (`KXITFMATCH-26OCT28SOUSAK-SOU`) | 0.04 / 0.05 (1409) | 4.5% | 11.0% | 12.3% | 16.1% [14.2%-17.7%] | -- | -- | -- | -- | PASS | +6.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 167.0, B 3163.0; serve-point win A 54.0%, B 36.6%; Elo A 1236.0, B 1521.4; model uncertainty 0.0174
* Form inputs: days since last match A 219, B 30; matches on record A 4, B 717; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.017, surface_dev_loose -0.006, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amanda Carolina Nava Elkin vs Anastasia Tikhonova -- W50 Morelia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221073:222158:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amanda Carolina Nava Elkin (`KXITFWMATCH-26OCT28NAVTIK-NAV`) | 0.04 / 0.05 (26) | 4.5% | 2.5% | 8.6% | 7.1% [5.6%-8.6%] | -- | -- | -- | -- | WATCH | -2.0 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anastasia Tikhonova (`KXITFWMATCH-26OCT28NAVTIK-TIK`) | 0.91 / 0.95 (2) | 93.0% | 97.5% | 91.4% | 92.9% [91.4%-94.4%] | -- | -- | -- | -- | PASS | +4.5 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 845.0, B 2660.0; serve-point win A 48.2%, B 36.9%; Elo A 1099.1, B 1574.6; model uncertainty 0.015
* Form inputs: days since last match A 233, B 24; matches on record A 106, B 387; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.004, surface_dev_loose -0.008, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Miriana Tona vs Ana Carmen Zamburek -- W50 Morelia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:210847:221979:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miriana Tona (`KXITFWMATCH-26OCT28TONZAM-TON`) | 0.74 / 0.76 (121) | 75.0% | 78.1% | 62.5% | 62.5% [55.3%-70.3%] | -- | -- | -- | -- | PASS | +3.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ana Carmen Zamburek (`KXITFWMATCH-26OCT28TONZAM-ZAM`) | 0.23 / 0.26 (523) | 24.5% | 21.9% | 37.5% | 37.5% [29.7%-44.7%] | -- | -- | -- | -- | PASS | -2.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2556.0, B 216.0; serve-point win A 57.7%, B 48.1%; Elo A 1438.5, B 1347.5; model uncertainty 0.0751
* Form inputs: days since last match A 51, B 359; matches on record A 410, B 27; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.068, surface_pool_high -0.072, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ingrid Neel / Giuliana Olmos vs Tereza Mihalikova / Olivia Nicholls -- WTA Tokyo QF

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-29 04:30Z
* Current expected start: 2026-10-29 02:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-29 01:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-29T04:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28NEEOLMMIHNIC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tereza Mihalikova / Olivia Nicholls (`KXWTADOUBLES-26OCT28NEEOLMMIHNIC-MIHNIC`) | 0.48 / 0.51 (150) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ingrid Neel / Giuliana Olmos (`KXWTADOUBLES-26OCT28NEEOLMMIHNIC-NEEOLM`) | 0.48 / 0.52 (394) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Rodrigo Alujas vs Tarun Karra -- M15 Mazatlan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 02:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T02:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212286:213598:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rodrigo Alujas (`KXITFMATCH-26OCT28ALUKAR-ALU`) | 0.83 / 0.88 (952) | 85.5% | 80.7% | 75.0% | 72.0% [71.0%-75.1%] | -- | -- | -- | -- | PASS | -4.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tarun Karra (`KXITFMATCH-26OCT28ALUKAR-KAR`) | 0.12 / 0.14 (130) | 13.0% | 19.4% | 25.0% | 28.0% [24.9%-29.0%] | -- | -- | -- | -- | PASS | +6.3 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2335.0, B 201.0; serve-point win A 59.8%, B 46.7%; Elo A 1295.7, B 1132.3; model uncertainty 0.0207
* Form inputs: days since last match A 191, B 226; matches on record A 83, B 8; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ian Lucca Cervantes Tomas vs Joaquin Guilleme -- M15 Mazatlan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 02:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T02:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212486:213603:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ian Lucca Cervantes Tomas (`KXITFMATCH-26OCT28CERGUI-CER`) | 0.16 / 0.23 (26) | 19.5% | 27.2% | 30.6% | 28.8% [26.6%-30.6%] | -- | -- | -- | -- | PASS | +7.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Joaquin Guilleme (`KXITFMATCH-26OCT28CERGUI-GUI`) | 0.76 / 0.81 (102) | 78.5% | 72.8% | 69.4% | 71.2% [69.4%-73.4%] | -- | -- | -- | -- | PASS | -5.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 529.0, B 925.0; serve-point win A 56.8%, B 38.5%; Elo A 1159.9, B 1323.6; model uncertainty 0.0202
* Form inputs: days since last match A 401, B 289; matches on record A 24, B 17; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Brunkel / Noel vs Lahey / Vagramov -- W35 Norman OK R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 02:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T02:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28BRUNOELAHVAG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brunkel / Noel (`KXITFWDOUBLES-26OCT28BRUNOELAHVAG-BRUNOE`) | 0.05 / 0.12 (28) | 8.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lahey / Vagramov (`KXITFWDOUBLES-26OCT28BRUNOELAHVAG-LAHVAG`) | 0.84 / 0.96 (40) | 90.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Judith Hernandez Miranda vs Julia Garcia -- W50 Morelia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 02:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T02:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222049:222665:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julia Garcia (`KXITFWMATCH-26OCT28HERGAR-GAR`) | 0.90 / 0.97 (363) | 93.5% | 85.9% | 89.5% | 71.3% [64.6%-79.7%] | -- | -- | -- | -- | PASS | -7.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Judith Hernandez Miranda (`KXITFWMATCH-26OCT28HERGAR-HER`) | 0.03 / 0.07 (20) | 5.0% | 14.1% | 10.5% | 28.7% [20.3%-35.4%] | -- | -- | -- | -- | PASS | +9.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 185.0, B 492.0; serve-point win A 49.4%, B 42.6%; Elo A 1268.5, B 1405.9; model uncertainty 0.0753
* Form inputs: days since last match A 184, B 471; matches on record A 110, B 33; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.033, surface_pool_high -0.035, surface_dev_loose -0.009, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Albuquerque Dietrich / Eduardo Lino vs Noatto / Tosetto -- M15 João Pessoa R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28ALBEDUNOATOS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Albuquerque Dietrich / Eduardo Lino (`KXITFDOUBLES-26OCT28ALBEDUNOATOS-ALBEDU`) | 0.05 / 0.95 (38) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Noatto / Tosetto (`KXITFDOUBLES-26OCT28ALBEDUNOATOS-NOATOS`) | 0.05 / 0.95 (38) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Hammond / Hornung vs Aunion Duran / Klimas -- M25 Las Vegas NV R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28HAMHORAUNKLI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aunion Duran / Klimas (`KXITFDOUBLES-26OCT28HAMHORAUNKLI-AUNKLI`) | 0.32 / 0.58 (59) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hammond / Hornung (`KXITFDOUBLES-26OCT28HAMHORAUNKLI-HAMHOR`) | 0.36 / 0.62 (65) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Konduri / Latak vs Edwards / Shugar -- M25 Las Vegas NV R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28KONLATEDWSHU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Edwards / Shugar (`KXITFDOUBLES-26OCT28KONLATEDWSHU-EDWSHU`) | 0.05 / 0.95 (38) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Konduri / Latak (`KXITFDOUBLES-26OCT28KONLATEDWSHU-KONLAT`) | 0.05 / 0.94 (1) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mikovic / Palomar vs Corwin / Overmyer -- M25 Las Vegas NV R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28MIKPALCOROVE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Corwin / Overmyer (`KXITFDOUBLES-26OCT28MIKPALCOROVE-COROVE`) | 0.22 / 0.45 (45) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mikovic / Palomar (`KXITFDOUBLES-26OCT28MIKPALCOROVE-MIKPAL`) | 0.49 / 0.73 (92) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## OKONKWO / Vance vs Alcantara / Calvelo -- M25 Las Vegas NV R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28OKOVANALCCAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alcantara / Calvelo (`KXITFDOUBLES-26OCT28OKOVANALCCAL-ALCCAL`) | 0.05 / 0.94 (1) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| OKONKWO / Vance (`KXITFDOUBLES-26OCT28OKOVANALCCAL-OKOVAN`) | 0.05 / 0.94 (1) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Chan / Gibbs vs Castillo Meza / Odorizzi -- W50 Morelia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 03:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28CHAGIBCASODO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Castillo Meza / Odorizzi (`KXITFWDOUBLES-26OCT28CHAGIBCASODO-CASODO`) | 0.10 / 0.24 (32) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Chan / Gibbs (`KXITFWDOUBLES-26OCT28CHAGIBCASODO-CHAGIB`) | 0.71 / 0.90 (0) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hitt / Vyas vs Giordano / Hrda -- W50 Morelia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 03:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28HITVYAGIOHRD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giordano / Hrda (`KXITFWDOUBLES-26OCT28HITVYAGIOHRD-GIOHRD`) | 0.61 / 0.82 (138) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hitt / Vyas (`KXITFWDOUBLES-26OCT28HITVYAGIOHRD-HITVYA`) | 0.13 / 0.34 (37) | 23.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Ellen Perez / Demi Schuurs vs Storm Hunter / Maya Joint -- WTA Tokyo QF

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-29 07:00Z
* Current expected start: 2026-10-29 04:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-29 03:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-29T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29PERSCHHUNJOI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Storm Hunter / Maya Joint (`KXWTADOUBLES-26OCT29PERSCHHUNJOI-HUNJOI`) | 0.43 / 0.52 (60) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ellen Perez / Demi Schuurs (`KXWTADOUBLES-26OCT29PERSCHHUNJOI-PERSCH`) | 0.43 / 0.52 (9) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Rapolu / Sholokhova vs Marron Baruqui / Carolina Nava Elkin -- W50 Morelia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28RAPSHOMARCAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marron Baruqui / Carolina Nava Elkin (`KXITFWDOUBLES-26OCT28RAPSHOMARCAR-MARCAR`) | 0.05 / 0.06 (26) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rapolu / Sholokhova (`KXITFWDOUBLES-26OCT28RAPSHOMARCAR-RAPSHO`) | 0.90 / 0.96 (73) | 93.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Gabriela Dabrowski / Luisa Stefani vs Hao-Ching Chan / Miyu (1994) Kato -- WTA Tokyo QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 04:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-30T04:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-29T04:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28DABSTECHAKAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hao-Ching Chan / Miyu (1994) Kato (`KXWTADOUBLES-26OCT28DABSTECHAKAT-CHAKAT`) | 0.05 / 0.94 (1) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gabriela Dabrowski / Luisa Stefani (`KXWTADOUBLES-26OCT28DABSTECHAKAT-DABSTE`) | 0.05 / 0.94 (1) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Asia Muhammad / Shuai Zhang vs Sara Errani / Jasmine Paolini -- WTA Tokyo QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 04:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-30T04:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-29T04:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28MUHZHAERRPAO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Errani / Jasmine Paolini (`KXWTADOUBLES-26OCT28MUHZHAERRPAO-ERRPAO`) | 0.07 / 0.93 (4) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Asia Muhammad / Shuai Zhang (`KXWTADOUBLES-26OCT28MUHZHAERRPAO-MUHZHA`) | 0.07 / 0.92 (10) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sloane Stephens vs Rose Marie Nijkamp -- W100 New Braunfels TX R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 04:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T04:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:201585:260225:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rose Marie Nijkamp (`KXITFWMATCH-26OCT28STENIJ-NIJ`) | 0.08 / 0.10 (551) | 9.0% | 11.8% | 55.3% | 25.6% [11.5%-36.4%] | -- | -- | -- | -- | WATCH | +2.9 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sloane Stephens (`KXITFWMATCH-26OCT28STENIJ-STE`) | 0.90 / 0.92 (145) | 91.0% | 88.1% | 44.7% | 74.4% [63.6%-88.5%] | -- | -- | -- | -- | PASS | -2.9 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2061.0, B 1080.0; serve-point win A 57.3%, B 51.5%; Elo A 1813.0, B 1447.9; model uncertainty 0.1244
* Form inputs: days since last match A 40, B 191; matches on record A 685, B 54; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.033, surface_pool_high -0.036, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jil Teichmann vs Zeynep Sonmez -- WTA Guangzhou R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-28 08:00Z
* Current expected start: 2026-10-29 05:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-29 04:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1260_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-28T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213525:220309:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zeynep Sonmez (`KXWTAMATCH-26OCT28TEISON-SON`) | 0.66 / 0.68 (7160) | 67.0% | 64.2% | 68.4% | 65.0% [62.5%-66.5%] | -- | -- | -- | -- | PASS | -2.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jil Teichmann (`KXWTAMATCH-26OCT28TEISON-TEI`) | 0.32 / 0.33 (2) | 32.5% | 35.8% | 31.6% | 35.0% [33.5%-37.5%] | -- | -- | -- | -- | WATCH | +3.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2567.0, B 4355.0; serve-point win A 54.3%, B 42.9%; Elo A 1766.8, B 1834.7; model uncertainty 0.0197
* Form inputs: days since last match A 1, B 1; matches on record A 583, B 430; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.010, surface_dev_loose -0.010, surface_dev_tight +0.010
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT28TEISON-22` Over 21.5 games: 0.45/0.46 mid 45.5%, model 60.6% (projection_v2.0 (prediction ledger)) -- gap +15.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT28TEISON-2-TEI` Will Jil Teichmann win set 2 in the Jil Teichmann vs Zeynep Sonmez match: 0.07/0.50 mid 28.5%, model 40.4% (projection_v2.0 (prediction ledger)) -- gap +11.9 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT28TEISON-17` Over 16.5 games: 0.82/0.91 mid 86.5%, model 92.6% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT28TEISON-27` Over 26.5 games: 0.23/0.58 mid 40.5%, model 37.6% (projection_v2.0 (prediction ledger)) -- gap -2.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT28TEISON-1-SON` Will Zeynep Sonmez win set 1 in the Jil Teichmann vs Zeynep Sonmez match: 0.61/0.64 mid 62.5%, model 59.6% (projection_v2.0 (prediction ledger)) -- gap -2.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT28TEISON-1-TEI` Will Jil Teichmann win set 1 in the Jil Teichmann vs Zeynep Sonmez match: 0.36/0.39 mid 37.5%, model 40.4% (projection_v2.0 (prediction ledger)) -- gap +2.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT28TEISON-2-SON` Will Zeynep Sonmez win set 2 in the Jil Teichmann vs Zeynep Sonmez match: 0.27/0.94 mid 60.5%, model 59.6% (projection_v2.0 (prediction ledger)) -- gap -0.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Claire Liu vs Katerina Siniakova -- WTA Guangzhou R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-29 08:00Z
* Current expected start: 2026-10-29 05:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-29 04:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-29T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211701:214906:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Claire Liu (`KXWTAMATCH-26OCT29LIUSIN-LIU`) | 0.31 / 0.35 (1126) | 33.0% | 29.3% | 29.3% | 29.3% [28.4%-31.6%] | -- | -- | -- | -- | PASS | -3.6 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katerina Siniakova (`KXWTAMATCH-26OCT29LIUSIN-SIN`) | 0.65 / 0.69 (520) | 67.0% | 70.7% | 70.7% | 70.7% [68.4%-71.6%] | -- | -- | -- | -- | PASS | +3.6 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3837.0, B 4278.0; serve-point win A 53.4%, B 42.5%; Elo A 1772.0, B 1926.9; model uncertainty 0.0162
* Form inputs: days since last match A 1, B 3; matches on record A 458, B 725; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT29LIUSIN-26` Over 25.5 games: 0.31/0.95 mid 63.0%, model 40.3% (projection_v2.0 (prediction ledger)) -- gap -22.7 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT29LIUSIN-1-LIU` Will Claire Liu win set 1 in the Claire Liu vs Katerina Siniakova match: 0.02/0.98 mid 50.0%, model 35.9% (projection_v2.0 (prediction ledger)) -- gap -14.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT29LIUSIN-1-SIN` Will Katerina Siniakova win set 1 in the Claire Liu vs Katerina Siniakova match: 0.02/0.98 mid 50.0%, model 64.1% (projection_v2.0 (prediction ledger)) -- gap +14.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT29LIUSIN-2-LIU` Will Claire Liu win set 2 in the Claire Liu vs Katerina Siniakova match: 0.01/0.99 mid 50.0%, model 35.9% (projection_v2.0 (prediction ledger)) -- gap -14.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT29LIUSIN-2-SIN` Will Katerina Siniakova win set 2 in the Claire Liu vs Katerina Siniakova match: 0.02/0.99 mid 50.5%, model 64.1% (projection_v2.0 (prediction ledger)) -- gap +13.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT29LIUSIN-21` Over 20.5 games: 0.03/0.98 mid 50.5%, model 63.1% (projection_v2.0 (prediction ledger)) -- gap +12.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT29LIUSIN-16` Over 15.5 games: 0.90/0.94 mid 92.0%, model 95.9% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Herman Hoeyeraal vs Philip Sekulic -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208382:210340:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Herman Hoeyeraal (`KXITFMATCH-26OCT28HOESEK-HOE`) | 0.26 / 0.30 (119) | 28.0% | 17.8% | 28.7% | 21.2% [19.4%-23.5%] | -- | -- | -- | -- | PASS | -10.2 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Philip Sekulic (`KXITFMATCH-26OCT28HOESEK-SEK`) | 0.69 / 0.72 (56) | 70.5% | 82.2% | 71.3% | 78.8% [76.5%-80.6%] | -- | -- | -- | -- | WATCH | +11.7 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1265.0, B 4045.0; serve-point win A 60.3%, B 32.3%; Elo A 1277.8, B 1560.3; model uncertainty 0.0206
* Form inputs: days since last match A 114, B 36; matches on record A 32, B 272; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.011, surface_dev_loose +0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pann / Patel vs Marinkov / O'Connell -- M25 Tamworth QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28PANPATMAROCO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marinkov / O'Connell (`KXITFDOUBLES-26OCT28PANPATMAROCO-MAROCO`) | 0.04 / 0.96 (11) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pann / Patel (`KXITFDOUBLES-26OCT28PANPATMAROCO-PANPAT`) | 0.04 / 0.96 (11) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Tai Leonard Sach vs Ymerali Ibraimi -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212740:214192:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ymerali Ibraimi (`KXITFMATCH-26OCT28SACIBR-IBR`) | 0.24 / 0.29 (21) | 26.5% | 27.4% | 17.7% | 30.8% [25.1%-38.4%] | -- | -- | -- | -- | PASS | +0.9 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tai Leonard Sach (`KXITFMATCH-26OCT28SACIBR-SAC`) | 0.69 / 0.74 (13) | 71.5% | 72.6% | 82.3% | 69.2% [61.7%-74.9%] | -- | -- | -- | -- | PASS | +1.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2265.0, B 660.0; serve-point win A 62.7%, B 42.0%; Elo A 1397.6, B 1311.9; model uncertainty 0.066
* Form inputs: days since last match A 233, B 219; matches on record A 74, B 11; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.000, surface_dev_loose +0.009, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Harrison Satara vs Blake Ellis -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:134329:214483:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blake Ellis (`KXITFMATCH-26OCT28SATELL-ELL`) | 0.81 / 0.89 (55) | 85.0% | 80.2% | 49.0% | 77.0% [72.1%-81.6%] | -- | -- | -- | -- | PASS | -4.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Harrison Satara (`KXITFMATCH-26OCT28SATELL-SAT`) | 0.10 / 0.15 (72) | 12.5% | 19.8% | 51.0% | 22.9% [18.4%-27.9%] | -- | -- | -- | -- | PASS | +7.3 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 310.0, B 2473.0; serve-point win A 61.6%, B 31.5%; Elo A 1317.4, B 1570.8; model uncertainty 0.0476
* Form inputs: days since last match A 219, B 44; matches on record A 5, B 391; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.015, surface_dev_loose +0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anton Shepp vs Zane Stevens -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209394:213204:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anton Shepp (`KXITFMATCH-26OCT28SHESTE-SHE`) | 0.63 / 0.73 (54) | 68.0% | 86.9% | 91.2% | 80.8% [76.6%-84.8%] | -- | -- | -- | -- | PASS | +18.9 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zane Stevens (`KXITFMATCH-26OCT28SHESTE-STE`) | 0.24 / 0.32 (69) | 28.0% | 13.2% | 8.8% | 19.1% [15.2%-23.4%] | -- | -- | -- | -- | PASS | -14.8 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2073.0, B 477.0; serve-point win A 68.6%, B 40.4%; Elo A 1440.8, B 1238.6; model uncertainty 0.0409
* Form inputs: days since last match A 38, B 352; matches on record A 69, B 11; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28SHESTE-SHE  (YES = Anton Shepp)
Model: 87%
Kalshi: 68%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vaidehee Chaudhari vs Lucia Gale -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28CHAGAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vaidehee Chaudhari (`KXITFWMATCH-26OCT28CHAGAL-CHA`) | 0.86 / 0.96 (2) | 91.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucia Gale (`KXITFWMATCH-26OCT28CHAGAL-GAL`) | 0.03 / 0.10 (27) | 6.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Fernanda Pantoja Espino / Villanueva Couto vs Avataneo / Harvey -- W50 Morelia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28FERVILAVAHAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Avataneo / Harvey (`KXITFWDOUBLES-26OCT28FERVILAVAHAR-AVAHAR`) | 0.05 / 0.95 (1) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fernanda Pantoja Espino / Villanueva Couto (`KXITFWDOUBLES-26OCT28FERVILAVAHAR-FERVIL`) | 0.05 / 0.95 (1) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Malkin / Carolina Millan Acosta vs Guadalupe Regalado Macias / Senties -- W50 Morelia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28MALCARGUASEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guadalupe Regalado Macias / Senties (`KXITFWDOUBLES-26OCT28MALCARGUASEN-GUASEN`) | 0.05 / 0.13 (28) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Malkin / Carolina Millan Acosta (`KXITFWDOUBLES-26OCT28MALCARGUASEN-MALCAR`) | 0.80 / 0.96 (40) | 88.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Hikaru Sato vs Renee Alame -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221141:266383:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Renee Alame (`KXITFWMATCH-26OCT28SATALA-ALA`) | 0.10 / 0.30 (35) | 20.0% | 13.0% | 23.8% | 21.0% [18.8%-22.1%] | -- | -- | -- | -- | PASS | -7.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hikaru Sato (`KXITFWMATCH-26OCT28SATALA-SAT`) | 0.71 / 0.84 (6) | 77.5% | 87.0% | 76.2% | 79.0% [77.9%-81.2%] | -- | -- | -- | -- | PASS | +9.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1807.0, B 291.0; serve-point win A 60.7%, B 47.9%; Elo A 1465.8, B 1228.7; model uncertainty 0.0166
* Form inputs: days since last match A 191, B 261; matches on record A 175, B 9; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.004, surface_dev_loose +0.007, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Katie Swan vs Laquisa Khan -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215042:260762:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Laquisa Khan (`KXITFWMATCH-26OCT28SWAKHA-KHA`) | 0.03 / 0.06 (21) | 4.5% | 3.8% | 3.7% | 5.5% [4.1%-7.7%] | -- | -- | -- | -- | PASS | -0.7 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katie Swan (`KXITFWMATCH-26OCT28SWAKHA-SWA`) | 0.89 / 0.97 (279) | 93.0% | 96.2% | 96.3% | 94.5% [92.3%-95.9%] | -- | -- | -- | -- | PASS | +3.2 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2343.0, B 1323.0; serve-point win A 63.1%, B 50.4%; Elo A 1722.0, B 1287.6; model uncertainty 0.0178
* Form inputs: days since last match A 33, B 219; matches on record A 387, B 93; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.006, surface_pool_high -0.005, surface_dev_loose +0.006, surface_dev_tight -0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Belle Thompson vs Dayeon Back -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220432:259858:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dayeon Back (`KXITFWMATCH-26OCT28THOBAC-BAC`) | 0.80 / 0.88 (66) | 84.0% | 91.6% | 92.4% | 90.0% [86.1%-92.0%] | -- | -- | -- | -- | PASS | +7.6 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Belle Thompson (`KXITFWMATCH-26OCT28THOBAC-THO`) | 0.07 / 0.14 (29) | 10.5% | 8.4% | 7.6% | 10.0% [8.0%-13.9%] | -- | -- | -- | -- | PASS | -2.1 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1699.0, B 3370.0; serve-point win A 47.7%, B 42.0%; Elo A 1312.7, B 1649.3; model uncertainty 0.0295
* Form inputs: days since last match A 219, B 35; matches on record A 114, B 295; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.005, surface_dev_loose -0.009, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Naomi Osaka vs Mia Pohankova -- WTA Tokyo R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-29 04:30Z
* Current expected start: 2026-10-29 05:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-29 04:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+60_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-29T04:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211768:266376:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naomi Osaka (`KXWTAMATCH-26OCT28OSAPOH-OSA`) | 0.78 / 0.79 (6804) | 78.5% | 75.5% | 71.6% | 77.3% [73.7%-83.8%] | 76.2% | -- | 76.2% | ALL_THREE_DISAGREE | PASS | -3.0 pp | NORMAL | AGING | B / ADEQUATE | ALL_AGREE | VERIFIED |
| Mia Pohankova (`KXWTAMATCH-26OCT28OSAPOH-POH`) | 0.21 / 0.22 (863) | 21.5% | 24.5% | 28.4% | 22.7% [16.2%-26.4%] | 23.8% | -- | 23.8% | ALL_THREE_DISAGREE | PASS | +3.0 pp | NORMAL | AGING | B / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 2986.0, B 1596.0; serve-point win A 64.7%, B 40.8%; Elo A 2137.0, B 1860.0; model uncertainty 0.0506
* Form inputs: days since last match A 1, B 1; matches on record A 517, B 63; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.022, surface_pool_high -0.024, surface_dev_loose -0.005, surface_dev_tight +0.001
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT28OSAPOH-17` Over 16.5 games: 0.17/0.98 mid 57.5%, model 94.3% (projection_v2.0 (prediction ledger)) -- gap +36.8 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT28OSAPOH-2-POH` Will Mia Pohankova win set 2 in the Naomi Osaka vs Mia Pohankova match: 0.15/0.90 mid 52.5%, model 32.2% (projection_v2.0 (prediction ledger)) -- gap -20.3 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT28OSAPOH-2-OSA` Will Naomi Osaka win set 2 in the Naomi Osaka vs Mia Pohankova match: 0.15/0.87 mid 51.0%, model 67.8% (projection_v2.0 (prediction ledger)) -- gap +16.8 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT28OSAPOH-22` Over 21.5 games: 0.44/0.46 mid 45.0%, model 60.2% (projection_v2.0 (prediction ledger)) -- gap +15.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT28OSAPOH-27` Over 26.5 games: 0.18/0.86 mid 52.0%, model 37.1% (projection_v2.0 (prediction ledger)) -- gap -14.9 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT28OSAPOH-1-OSA` Will Naomi Osaka win set 1 in the Naomi Osaka vs Mia Pohankova match: 0.71/0.74 mid 72.5%, model 67.8% (projection_v2.0 (prediction ledger)) -- gap -4.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT28OSAPOH-1-POH` Will Mia Pohankova win set 1 in the Naomi Osaka vs Mia Pohankova match: 0.26/0.30 mid 28.0%, model 32.2% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Cazacu / Uta vs Dahlberg / Velcz -- M25 Norman OK R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T05:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28CAZUTADAHVEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cazacu / Uta (`KXITFDOUBLES-26OCT28CAZUTADAHVEL-CAZUTA`) | 0.05 / 0.26 (33) | 15.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dahlberg / Velcz (`KXITFDOUBLES-26OCT28CAZUTADAHVEL-DAHVEL`) | 0.69 / 0.95 (38) | 82.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Chavez / Melero Kretzer vs Montsi / Nhavene -- M25 Norman OK R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T05:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28CHAMELMONNHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chavez / Melero Kretzer (`KXITFDOUBLES-26OCT28CHAMELMONNHA-CHAMEL`) | 0.05 / 0.95 (38) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Montsi / Nhavene (`KXITFDOUBLES-26OCT28CHAMELMONNHA-MONNHA`) | 0.05 / 0.94 (1) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Bartashevich / Kamper vs Epps / Szabo -- W35 Norman OK R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T05:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28BARKAMEPPSZA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bartashevich / Kamper (`KXITFWDOUBLES-26OCT28BARKAMEPPSZA-BARKAM`) | 0.05 / 0.95 (1) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Epps / Szabo (`KXITFWDOUBLES-26OCT28BARKAMEPPSZA-EPPSZA`) | 0.05 / 0.96 (40) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nahum / Ounmuang vs Laskevich / Mamedova -- W35 Norman OK R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 05:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T05:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28NAHOUNLASMAM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Laskevich / Mamedova (`KXITFWDOUBLES-26OCT28NAHOUNLASMAM-LASMAM`) | 0.56 / 0.81 (0) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nahum / Ounmuang (`KXITFWDOUBLES-26OCT28NAHOUNLASMAM-NAHOUN`) | 0.19 / 0.34 (37) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Enzo Aguiard vs Jeremy Beale -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200003:212174:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Enzo Aguiard (`KXITFMATCH-26OCT28AGUBEA-AGU`) | 0.62 / 0.71 (100) | 66.5% | 63.6% | 87.8% | 58.1% [54.1%-64.1%] | -- | -- | -- | -- | PASS | -2.9 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Jeremy Beale (`KXITFMATCH-26OCT28AGUBEA-BEA`) | 0.25 / 0.33 (137) | 29.0% | 36.4% | 12.2% | 41.9% [35.9%-45.9%] | -- | -- | -- | -- | PASS | +7.4 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1732.0, B 133.0; serve-point win A 62.2%, B 40.5%; Elo A 1500.5, B 1467.2; model uncertainty 0.05
* Form inputs: days since last match A 44, B 1122; matches on record A 58, B 207; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Isaac Becroft vs Moerani Bouzige -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207728:208653:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isaac Becroft (`KXITFMATCH-26OCT28BECBOU-BEC`) | 0.61 / 0.64 (13) | 62.5% | 30.7% | 33.2% | 33.7% [32.3%-37.0%] | -- | -- | -- | -- | PASS | -31.8 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Moerani Bouzige (`KXITFMATCH-26OCT28BECBOU-BOU`) | 0.34 / 0.37 (21) | 35.5% | 69.3% | 66.8% | 66.3% [63.0%-67.7%] | -- | -- | -- | -- | WATCH | +33.8 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1698.0, B 3261.0; serve-point win A 59.6%, B 36.4%; Elo A 1311.2, B 1424.3; model uncertainty 0.0235
* Form inputs: days since last match A 184, B 44; matches on record A 106, B 315; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28BECBOU-BOU  (YES = Moerani Bouzige)
Model: 69%
Kalshi: 36%
Gap: +34 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.009, surface_dev_loose -0.009, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matthew Dellavedova vs Lachlan Vickery -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202354:212956:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthew Dellavedova (`KXITFMATCH-26OCT28DELVIC-DEL`) | 0.90 / 0.96 (348) | 93.0% | 91.3% | 88.2% | 84.8% [84.1%-85.8%] | -- | -- | -- | -- | PASS | -1.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lachlan Vickery (`KXITFMATCH-26OCT28DELVIC-VIC`) | 0.04 / 0.05 (100) | 4.5% | 8.7% | 11.8% | 15.2% [14.2%-15.9%] | -- | -- | -- | -- | PASS | +4.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3884.0, B 133.0; serve-point win A 64.1%, B 46.4%; Elo A 1455.0, B 1158.7; model uncertainty 0.0088
* Form inputs: days since last match A 36, B 254; matches on record A 451, B 10; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.006, surface_dev_loose +0.004, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sam Ryan Ziegann vs Chase Ferguson -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207994:208160:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chase Ferguson (`KXITFMATCH-26OCT28RYAFER-FER`) | 0.65 / 0.71 (52) | 68.0% | 73.5% | 71.1% | 75.7% [74.5%-77.3%] | -- | -- | -- | -- | PASS | +5.5 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sam Ryan Ziegann (`KXITFMATCH-26OCT28RYAFER-RYA`) | 0.29 / 0.32 (29) | 30.5% | 26.5% | 28.9% | 24.3% [22.7%-25.5%] | -- | -- | -- | -- | PASS | -4.0 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1167.0, B 3171.0; serve-point win A 59.9%, B 35.1%; Elo A 1190.8, B 1420.1; model uncertainty 0.0142
* Form inputs: days since last match A 51, B 212; matches on record A 87, B 111; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose -0.008, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matias Soto vs Mauricio Schtulmann Gasca -- M15 Mazatlan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207130:214271:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mauricio Schtulmann Gasca (`KXITFMATCH-26OCT28SOTSCH-SCH`) | 0.05 / 0.08 (114) | 6.5% | 15.9% | 23.8% | 21.1% [20.7%-21.9%] | -- | -- | -- | -- | PASS | +9.4 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matias Soto (`KXITFMATCH-26OCT28SOTSCH-SOT`) | 0.87 / 0.97 (476) | 92.0% | 84.1% | 76.2% | 78.9% [78.1%-79.3%] | -- | -- | -- | -- | PASS | -7.9 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4186.0, B 64.0; serve-point win A 63.5%, B 44.2%; Elo A 1586.6, B 1360.7; model uncertainty 0.0061
* Form inputs: days since last match A 9, B 205; matches on record A 288, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tahlia Kokkinis vs Alana Subasic -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260667:261049:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tahlia Kokkinis (`KXITFWMATCH-26OCT28KOKSUB-KOK`) | 0.61 / 0.75 (44) | 68.0% | 71.1% | 66.5% | 62.5% [57.9%-65.0%] | -- | -- | -- | -- | PASS | +3.1 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alana Subasic (`KXITFWMATCH-26OCT28KOKSUB-SUB`) | 0.20 / 0.33 (37) | 26.5% | 28.9% | 33.6% | 37.5% [35.0%-42.1%] | -- | -- | -- | -- | PASS | +2.4 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1935.0, B 2964.0; serve-point win A 57.8%, B 46.4%; Elo A 1514.8, B 1463.4; model uncertainty 0.0352
* Form inputs: days since last match A 162, B 184; matches on record A 101, B 101; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Funa Kozaki vs Monique Barry -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216260:222667:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Monique Barry (`KXITFWMATCH-26OCT28KOZBAR-BAR`) | 0.40 / 0.60 (6) | 50.0% | 31.9% | 41.0% | 39.5% [36.4%-43.6%] | -- | -- | -- | -- | PASS | -18.1 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Funa Kozaki (`KXITFWMATCH-26OCT28KOZBAR-KOZ`) | 0.41 / 0.55 (3) | 48.0% | 68.1% | 59.0% | 60.5% [56.4%-63.6%] | -- | -- | -- | -- | PASS | +20.1 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 166.0, B 1840.0; serve-point win A 56.5%, B 47.1%; Elo A 1405.1, B 1331.5; model uncertainty 0.0361
* Form inputs: days since last match A 191, B 219; matches on record A 222, B 209; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28KOZBAR-KOZ  (YES = Funa Kozaki)
Model: 68%
Kalshi: 48%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.031, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eva Lopez vs Erika Sema -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:202454:270357:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eva Lopez (`KXITFWMATCH-26OCT28LOPSEM-LOP`) | 0.04 / 0.14 (59) | 9.0% | 15.5% | 13.0% | 22.1% [19.9%-22.9%] | -- | -- | -- | -- | PASS | +6.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Erika Sema (`KXITFWMATCH-26OCT28LOPSEM-SEM`) | 0.80 / 0.94 (50) | 87.0% | 84.5% | 87.0% | 77.9% [77.1%-80.1%] | -- | -- | -- | -- | PASS | -2.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 148.0, B 1873.0; serve-point win A 51.7%, B 40.6%; Elo A 1274.2, B 1485.0; model uncertainty 0.0148
* Form inputs: days since last match A 345, B 184; matches on record A 3, B 930; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose -0.007, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## I Wen Wan vs Yuno Kitahara -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:263881:267449:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuno Kitahara (`KXITFWMATCH-26OCT28WANKIT-KIT`) | 0.23 / 0.42 (43) | 32.5% | 79.6% | 78.2% | 72.3% [69.5%-75.7%] | -- | -- | -- | -- | PASS | +47.1 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| I Wen Wan (`KXITFWMATCH-26OCT28WANKIT-WAN`) | 0.51 / 0.72 (5) | 61.5% | 20.4% | 21.8% | 27.7% [24.3%-30.5%] | -- | -- | -- | -- | PASS | -41.1 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 553.0, B 2068.0; serve-point win A 49.0%, B 44.8%; Elo A 1276.4, B 1428.6; model uncertainty 0.0314
* Form inputs: days since last match A 240, B 191; matches on record A 26, B 119; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28WANKIT-KIT  (YES = Yuno Kitahara)
Model: 80%
Kalshi: 32%
Gap: +47 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.009, surface_dev_loose -0.004, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Fanny Stollar / Fang-Hsien Wu vs I-Hsuan Cho / Yi Tsen Cho -- WTA Guangzhou QF

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-29 08:00Z
* Current expected start: 2026-10-29 06:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-29 05:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29STOFANCHOCHO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I-Hsuan Cho / Yi Tsen Cho (`KXWTADOUBLES-26OCT29STOFANCHOCHO-CHOCHO`) | 0.48 / 0.54 (112) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fanny Stollar / Fang-Hsien Wu (`KXWTADOUBLES-26OCT29STOFANCHOCHO-STOFAN`) | 0.45 / 0.52 (56) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Maria Timofeeva vs Xinran Sun -- WTA Guangzhou R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-29 08:00Z
* Current expected start: 2026-10-29 06:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-29 05:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-90_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-29T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:221237:270082:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xinran Sun (`KXWTAMATCH-26OCT29TIMSUN-SUN`) | 0.35 / 0.36 (1815) | 35.5% | 25.1% | 61.1% | 40.5% [24.4%-53.7%] | 37.7% | -- | 37.7% | ALL_THREE_DISAGREE | WATCH | -10.3 pp | REVIEW | AGING | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Maria Timofeeva (`KXWTAMATCH-26OCT29TIMSUN-TIM`) | 0.64 / 0.65 (430) | 64.5% | 74.9% | 38.9% | 59.5% [46.3%-75.6%] | 62.3% | -- | 62.3% | ALL_THREE_DISAGREE | PASS | +10.3 pp | REVIEW | AGING | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3737.0, B 1001.0; serve-point win A 55.7%, B 49.3%; Elo A 1821.3, B 1659.4; model uncertainty 0.1467
* Form inputs: days since last match A 2, B 23; matches on record A 361, B 25; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.041, surface_pool_high -0.053, surface_dev_loose -0.010, surface_dev_tight +0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTASETWINNER-26OCT29TIMSUN-2-SUN` Will Xinran Sun win set 2 in the Maria Timofeeva vs Xinran Sun match: 0.02/0.98 mid 50.0%, model 32.8% (projection_v2.0 (prediction ledger)) -- gap -17.2 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT29TIMSUN-2-TIM` Will Maria Timofeeva win set 2 in the Maria Timofeeva vs Xinran Sun match: 0.02/0.99 mid 50.5%, model 67.2% (projection_v2.0 (prediction ledger)) -- gap +16.8 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26OCT29TIMSUN-26` Over 25.5 games: 0.03/0.49 mid 26.0%, model 37.7% (projection_v2.0 (prediction ledger)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT29TIMSUN-21` Over 20.5 games: 0.48/0.49 mid 48.5%, model 60.1% (projection_v2.0 (prediction ledger)) -- gap +11.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT29TIMSUN-1-SUN` Will Xinran Sun win set 1 in the Maria Timofeeva vs Xinran Sun match: 0.35/0.40 mid 37.5%, model 32.8% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT29TIMSUN-1-TIM` Will Maria Timofeeva win set 1 in the Maria Timofeeva vs Xinran Sun match: 0.61/0.65 mid 63.0%, model 67.2% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26OCT29TIMSUN-16` Over 15.5 games: 0.89/0.94 mid 91.5%, model 94.7% (projection_v2.0 (prediction ledger)) -- gap +3.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; LOW_DATA_QUALITY; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alvarez / LIU vs De Alba / Sau Franco -- M15 Mazatlan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28ALVLIUDEASAU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alvarez / LIU (`KXITFDOUBLES-26OCT28ALVLIUDEASAU-ALVLIU`) | 0.11 / 0.37 (39) | 24.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| De Alba / Sau Franco (`KXITFDOUBLES-26OCT28ALVLIUDEASAU-DEASAU`) | 0.55 / 0.82 (138) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Cooper / McKennon vs Flores / Quesada Perez -- M15 Mazatlan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28COOMCKFLOQUE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cooper / McKennon (`KXITFDOUBLES-26OCT28COOMCKFLOQUE-COOMCK`) | 0.43 / 0.71 (86) | 57.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Flores / Quesada Perez (`KXITFDOUBLES-26OCT28COOMCKFLOQUE-FLOQUE`) | 0.24 / 0.51 (51) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Lucca Cervantes Tomas / Alejandro Reyes Tirado vs Alujas / Salvestre -- M15 Mazatlan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28LUCALEALUSAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alujas / Salvestre (`KXITFDOUBLES-26OCT28LUCALEALUSAL-ALUSAL`) | 0.54 / 0.80 (125) | 67.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucca Cervantes Tomas / Alejandro Reyes Tirado (`KXITFDOUBLES-26OCT28LUCALEALUSAL-LUCALE`) | 0.15 / 0.40 (41) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Markus Malaszszak vs Hugo Hashimoto -- M15 Yanagawa City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212308:213074:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Hashimoto (`KXITFMATCH-26OCT28MALHAS-HAS`) | 0.69 / 0.78 (4) | 73.5% | 48.8% | 51.6% | 48.9% [48.9%-49.5%] | -- | -- | -- | -- | PASS | -24.7 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Markus Malaszszak (`KXITFMATCH-26OCT28MALHAS-MAL`) | 0.22 / 0.26 (149) | 24.0% | 51.2% | 48.4% | 51.0% [50.5%-51.1%] | -- | -- | -- | -- | PASS | +27.2 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1157.0, B 204.0; serve-point win A 57.5%, B 42.7%; Elo A 1255.9, B 1247.2; model uncertainty 0.0027
* Form inputs: days since last match A 184, B 212; matches on record A 40, B 5; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28MALHAS-MAL  (YES = Markus Malaszszak)
Model: 51%
Kalshi: 24%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hikaru Shiraishi vs Yu Tanaka -- M15 Yanagawa City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202113:212092:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hikaru Shiraishi (`KXITFMATCH-26OCT28SHITAN-SHI`) | 0.58 / 0.64 (40) | 61.0% | 81.1% | 87.2% | 77.7% [73.3%-81.8%] | -- | -- | -- | -- | PASS | +20.1 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yu Tanaka (`KXITFMATCH-26OCT28SHITAN-TAN`) | 0.35 / 0.40 (129) | 37.5% | 18.9% | 12.8% | 22.3% [18.2%-26.7%] | -- | -- | -- | -- | PASS | -18.6 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2976.0, B 455.0; serve-point win A 63.2%, B 43.6%; Elo A 1438.1, B 1256.0; model uncertainty 0.0422
* Form inputs: days since last match A 44, B 485; matches on record A 210, B 10; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28SHITAN-SHI  (YES = Hikaru Shiraishi)
Model: 81%
Kalshi: 61%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.004, surface_dev_tight -0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kosuke Shibano vs Taiyo Yamanaka -- M15 Yanagawa City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208277:213624:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kosuke Shibano (`KXITFMATCH-26OCT28SHIYAM-SHI`) | 0.14 / 0.20 (131) | 17.0% | 33.4% | 28.8% | 35.3% [31.9%-37.8%] | -- | -- | -- | -- | PASS | +16.4 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Taiyo Yamanaka (`KXITFMATCH-26OCT28SHIYAM-YAM`) | 0.75 / 0.83 (150) | 79.0% | 66.6% | 71.2% | 64.7% [62.2%-68.0%] | -- | -- | -- | -- | PASS | -12.4 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 684.0, B 2208.0; serve-point win A 57.5%, B 39.2%; Elo A 1195.7, B 1281.4; model uncertainty 0.0291
* Form inputs: days since last match A 191, B 163; matches on record A 18, B 184; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28SHIYAM-SHI  (YES = Kosuke Shibano)
Model: 33%
Kalshi: 17%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.019, surface_dev_loose -0.014, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuta Tomida vs Yua Taka -- M15 Yanagawa City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212196:212616:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yua Taka (`KXITFMATCH-26OCT28TOMTAK-TAK`) | 0.27 / 0.35 (3) | 31.0% | 36.1% | 30.8% | 43.7% [37.5%-49.0%] | -- | -- | -- | -- | PASS | +5.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuta Tomida (`KXITFMATCH-26OCT28TOMTAK-TOM`) | 0.61 / 0.69 (63) | 65.0% | 63.9% | 69.2% | 56.3% [51.0%-62.5%] | -- | -- | -- | -- | PASS | -1.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1470.0, B 485.0; serve-point win A 58.3%, B 44.4%; Elo A 1221.5, B 1205.9; model uncertainty 0.0571
* Form inputs: days since last match A 191, B 261; matches on record A 44, B 21; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose +0.021, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jumpei Yamasaki vs Noritaka Koizumi -- M15 Yanagawa City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126135:212476:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Noritaka Koizumi (`KXITFMATCH-26OCT28YAMKOI-KOI`) | 0.25 / 0.29 (58) | 27.0% | 30.6% | 22.3% | 39.0% [33.8%-42.9%] | -- | -- | -- | -- | PASS | +3.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jumpei Yamasaki (`KXITFMATCH-26OCT28YAMKOI-YAM`) | 0.69 / 0.75 (100) | 72.0% | 69.4% | 77.7% | 61.0% [57.1%-66.2%] | -- | -- | -- | -- | PASS | -2.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1642.0, B 190.0; serve-point win A 64.1%, B 39.9%; Elo A 1349.8, B 1285.6; model uncertainty 0.0454
* Form inputs: days since last match A 184, B 212; matches on record A 360, B 8; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.019, surface_dev_loose +0.009, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Garcia / Carmen Zamburek vs Dominguez Garcia / Alessia Monteleone -- W50 Morelia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28GARCARDOMALE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dominguez Garcia / Alessia Monteleone (`KXITFWDOUBLES-26OCT28GARCARDOMALE-DOMALE`) | 0.05 / 0.06 (26) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Garcia / Carmen Zamburek (`KXITFWDOUBLES-26OCT28GARCARDOMALE-GARCAR`) | 0.89 / 0.96 (33) | 92.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Hoole / Pham vs Dong / Leonard Sach -- M25 Tamworth QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28HOOPHADONLEO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dong / Leonard Sach (`KXITFDOUBLES-26OCT28HOOPHADONLEO-DONLEO`) | 0.13 / 0.42 (43) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hoole / Pham (`KXITFDOUBLES-26OCT28HOOPHADONLEO-HOOPHA`) | 0.50 / 0.80 (125) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Satara / Stevens vs Hoeyeraal / Padgham -- M25 Tamworth QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28SATSTEHOEPAD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hoeyeraal / Padgham (`KXITFDOUBLES-26OCT28SATSTEHOEPAD-HOEPAD`) | 0.54 / 0.82 (138) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Satara / Stevens (`KXITFDOUBLES-26OCT28SATSTEHOEPAD-SATSTE`) | 0.11 / 0.38 (40) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Yujia Huang vs Yushan Shao -- W35 Kunshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264207:269253:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yujia Huang (`KXITFWMATCH-26OCT28HUASHA-HUA`) | 0.44 / 0.95 (6) | 69.5% | 51.2% | 52.1% | 55.3% [54.2%-56.4%] | -- | -- | -- | -- | PASS | -18.3 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yushan Shao (`KXITFWMATCH-26OCT28HUASHA-SHA`) | 0.04 / 0.54 (3) | 29.0% | 48.8% | 47.9% | 44.7% [43.6%-45.8%] | -- | -- | -- | -- | PASS | +19.8 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1640.0, B 1123.0; serve-point win A 55.4%, B 44.9%; Elo A 1447.1, B 1398.2; model uncertainty 0.0106
* Form inputs: days since last match A 24, B 22; matches on record A 88, B 29; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28HUASHA-SHA  (YES = Yushan Shao)
Model: 49%
Kalshi: 29%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yufei Ren vs Yu Jun Lin -- W35 Kunshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260913:268787:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yu Jun Lin (`KXITFWMATCH-26OCT28RENLIN-LIN`) | 0.33 / 0.45 (60) | 39.0% | 13.3% | 16.1% | 19.6% [17.8%-22.3%] | -- | -- | -- | -- | PASS | -25.7 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yufei Ren (`KXITFWMATCH-26OCT28RENLIN-REN`) | 0.49 / 0.70 (7) | 59.5% | 86.7% | 83.9% | 80.4% [77.7%-82.2%] | -- | -- | -- | -- | PASS | +27.2 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3240.0, B 515.0; serve-point win A 57.7%, B 50.6%; Elo A 1578.1, B 1346.6; model uncertainty 0.0223
* Form inputs: days since last match A 30, B 11; matches on record A 186, B 14; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28RENLIN-REN  (YES = Yufei Ren)
Model: 87%
Kalshi: 60%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.007, surface_dev_loose +0.011, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daria Zelinskaya vs Chengyiyi Yuan -- W35 Kunshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215134:239158:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chengyiyi Yuan (`KXITFWMATCH-26OCT28ZELYUA-YUA`) | 0.53 / 0.95 (5) | 74.0% | 42.3% | 37.6% | 41.2% [38.1%-47.4%] | -- | -- | -- | -- | PASS | -31.7 pp | EXTREME (DATA_WARNING) | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daria Zelinskaya (`KXITFWMATCH-26OCT28ZELYUA-ZEL`) | 0.04 / 0.44 (3) | 24.0% | 57.7% | 62.4% | 58.8% [52.6%-61.9%] | -- | -- | -- | -- | PASS | +33.7 pp | EXTREME (DATA_WARNING) | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2491.0, B 2947.0; serve-point win A 58.3%, B 43.1%; Elo A 1503.1, B 1478.6; model uncertainty 0.0461
* Form inputs: days since last match A 108, B 31; matches on record A 171, B 239; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28ZELYUA-ZEL  (YES = Daria Zelinskaya)
Model: 58%
Kalshi: 24%
Gap: +34 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Wushuang Zheng vs Daria KHOMUTSIANSKAYA -- W35 Kunshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213821:222944:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria KHOMUTSIANSKAYA (`KXITFWMATCH-26OCT28ZHEKHO-KHO`) | 0.05 / 0.95 (1) | 50.0% | 77.7% | 98.7% | 93.1% [74.3%-96.8%] | -- | -- | -- | -- | PASS | +27.7 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Wushuang Zheng (`KXITFWMATCH-26OCT28ZHEKHO-ZHE`) | 0.04 / 0.96 (1) | 50.0% | 22.3% | 1.3% | 6.9% [3.2%-25.7%] | -- | -- | -- | -- | PASS | -27.7 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2161.0, B 3178.0; serve-point win A 52.2%, B 42.0%; Elo A 1552.0, B 1665.8; model uncertainty 0.1124
* Form inputs: days since last match A 22, B 282; matches on record A 302, B 171; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28ZHEKHO-KHO  (YES = Daria KHOMUTSIANSKAYA)
Model: 78%
Kalshi: 50%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.002, surface_dev_loose -0.011, surface_dev_tight +0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elena Rybakina vs Yulia Putintseva -- WTA Tokyo R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-28 04:30Z
* Current expected start: 2026-10-29 08:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-29 07:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1650_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-28T04:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:201709:214981:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yulia Putintseva (`KXWTAMATCH-26OCT27RYBPUT-PUT`) | 0.11 / 0.13 (11389) | 12.0% | 12.2% | 10.6% | 10.8% [10.1%-12.0%] | -- | -- | -- | -- | PASS | +0.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elena Rybakina (`KXWTAMATCH-26OCT27RYBPUT-RYB`) | 0.88 / 0.89 (9253) | 88.5% | 87.8% | 89.4% | 89.2% [88.0%-89.9%] | -- | -- | -- | -- | PASS | -0.7 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6087.0, B 4366.0; serve-point win A 64.8%, B 44.3%; Elo A 2251.3, B 1900.2; model uncertainty 0.0094
* Form inputs: days since last match A 3, B 1; matches on record A 593, B 862; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.007, surface_dev_loose +0.004, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTASETWINNER-26OCT27RYBPUT-2-RYB` Will Elena Rybakina win set 2 in the Elena Rybakina vs Yulia Putintseva match: 0.27/0.97 mid 62.0%, model 78.2% (projection_v2.0 (prediction ledger)) -- gap +16.2 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT27RYBPUT-20` Over 19.5 games: 0.47/0.48 mid 47.5%, model 60.5% (projection_v2.0 (prediction ledger)) -- gap +13.0 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT27RYBPUT-15` Over 14.5 games: 0.91/0.95 mid 93.0%, model 97.9% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT27RYBPUT-25` Over 24.5 games: 0.24/0.54 mid 39.0%, model 34.3% (projection_v2.0 (prediction ledger)) -- gap -4.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT27RYBPUT-1-PUT` Will Yulia Putintseva win set 1 in the Elena Rybakina vs Yulia Putintseva match: 0.17/0.19 mid 18.0%, model 21.8% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT27RYBPUT-1-RYB` Will Elena Rybakina win set 1 in the Elena Rybakina vs Yulia Putintseva match: 0.80/0.84 mid 82.0%, model 78.2% (projection_v2.0 (prediction ledger)) -- gap -3.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT27RYBPUT-2-PUT` Will Yulia Putintseva win set 2 in the Elena Rybakina vs Yulia Putintseva match: 0.03/0.48 mid 25.5%, model 21.8% (projection_v2.0 (prediction ledger)) -- gap -3.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Anna Bondar vs Kaitlin Quevedo -- WTA Guangzhou R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-28 08:00Z
* Current expected start: 2026-10-29 08:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-29 07:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1440_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-28T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214388:259733:2026-10-28`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Bondar (`KXWTAMATCH-26OCT28BONQUE-BON`) | 0.52 / 0.53 (5306) | 52.5% | 50.9% | 53.1% | 51.5% [49.5%-52.6%] | -- | -- | -- | -- | PASS | -1.6 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kaitlin Quevedo (`KXWTAMATCH-26OCT28BONQUE-QUE`) | 0.47 / 0.48 (3117) | 47.5% | 49.1% | 46.9% | 48.4% [47.4%-50.5%] | -- | -- | -- | -- | PASS | +1.6 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5196.0, B 3270.0; serve-point win A 59.4%, B 40.8%; Elo A 1746.7, B 1770.4; model uncertainty 0.0156
* Form inputs: days since last match A 2, B 1; matches on record A 724, B 229; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.021, surface_dev_loose -0.010, surface_dev_tight +0.010
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT28BONQUE-23` Over 22.5 games: 0.44/0.45 mid 44.5%, model 57.9% (projection_v2.0 (prediction ledger)) -- gap +13.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT28BONQUE-18` Over 17.5 games: 0.79/0.87 mid 83.0%, model 90.1% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT28BONQUE-2-BON` Will Anna Bondar win set 2 in the Anna Bondar vs Kaitlin Quevedo match: 0.26/0.89 mid 57.5%, model 50.6% (projection_v2.0 (prediction ledger)) -- gap -6.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT28BONQUE-2-QUE` Will Kaitlin Quevedo win set 2 in the Anna Bondar vs Kaitlin Quevedo match: 0.26/0.84 mid 55.0%, model 49.4% (projection_v2.0 (prediction ledger)) -- gap -5.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26OCT28BONQUE-28` Over 27.5 games: 0.22/0.58 mid 40.0%, model 36.7% (projection_v2.0 (prediction ledger)) -- gap -3.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT28BONQUE-1-BON` Will Anna Bondar win set 1 in the Anna Bondar vs Kaitlin Quevedo match: 0.52/0.55 mid 53.5%, model 50.6% (projection_v2.0 (prediction ledger)) -- gap -2.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT28BONQUE-1-QUE` Will Kaitlin Quevedo win set 1 in the Anna Bondar vs Kaitlin Quevedo match: 0.45/0.49 mid 47.0%, model 49.4% (projection_v2.0 (prediction ledger)) -- gap +2.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Polina Kudermetova / Maria Timofeeva vs Eri Hozumi / Andreja Klepac -- WTA Guangzhou QF

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-29 08:00Z
* Current expected start: 2026-10-29 08:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-29 07:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT29KUDTIMHOZKLE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eri Hozumi / Andreja Klepac (`KXWTADOUBLES-26OCT29KUDTIMHOZKLE-HOZKLE`) | 0.65 / 0.68 (80) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Polina Kudermetova / Maria Timofeeva (`KXWTADOUBLES-26OCT29KUDTIMHOZKLE-KUDTIM`) | 0.31 / 0.34 (7) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Arevalo / Delgado vs Matta / Peck -- M15 Mazatlan QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28AREDELMATPEC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arevalo / Delgado (`KXITFDOUBLES-26OCT28AREDELMATPEC-AREDEL`) | 0.04 / 0.95 (1) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matta / Peck (`KXITFDOUBLES-26OCT28AREDELMATPEC-MATPEC`) | 0.04 / 0.95 (1) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sora Fukuda vs Takuya Kumasaka -- M15 Yanagawa City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126335:207998:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sora Fukuda (`KXITFMATCH-26OCT28FUKKUM-FUK`) | 0.35 / 0.38 (169) | 36.5% | 52.4% | 56.7% | 52.1% [49.0%-55.1%] | -- | -- | -- | -- | PASS | +15.9 pp | HIGH_REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Takuya Kumasaka (`KXITFMATCH-26OCT28FUKKUM-KUM`) | 0.61 / 0.64 (3) | 62.5% | 47.6% | 43.3% | 47.9% [44.9%-51.0%] | -- | -- | -- | -- | PASS | -14.9 pp | REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1862.0, B 3065.0; serve-point win A 60.6%, B 39.9%; Elo A 1391.3, B 1411.9; model uncertainty 0.0308
* Form inputs: days since last match A 184, B 79; matches on record A 277, B 226; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28FUKKUM-FUK  (YES = Sora Fukuda)
Model: 52%
Kalshi: 36%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.031, surface_pool_high -0.031, surface_dev_loose +0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hyu Kawanishi vs Shinji Hazawa -- M15 Yanagawa City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206923:213213:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shinji Hazawa (`KXITFMATCH-26OCT28KAW2HAZ2-HAZ2`) | 0.46 / 0.55 (100) | 50.5% | 65.8% | 59.6% | 57.6% [55.1%-59.6%] | -- | -- | -- | -- | PASS | +15.3 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hyu Kawanishi (`KXITFMATCH-26OCT28KAW2HAZ2-KAW2`) | 0.40 / 0.48 (112) | 44.0% | 34.2% | 40.4% | 42.4% [40.4%-44.9%] | -- | -- | -- | -- | PASS | -9.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 267.0, B 3455.0; serve-point win A 59.8%, B 37.0%; Elo A 1311.5, B 1358.1; model uncertainty 0.0224
* Form inputs: days since last match A 212, B 184; matches on record A 5, B 227; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28KAW2HAZ2-HAZ2  (YES = Shinji Hazawa)
Model: 66%
Kalshi: 50%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.005, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ko Suzuki vs Yuto Oki -- M15 Yanagawa City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:120545:212639:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuto Oki (`KXITFMATCH-26OCT28SUZOKI-OKI`) | 0.79 / 0.89 (202) | 84.0% | 75.8% | 75.1% | 67.1% [64.2%-69.9%] | -- | -- | -- | -- | PASS | -8.2 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ko Suzuki (`KXITFMATCH-26OCT28SUZOKI-SUZ`) | 0.08 / 0.16 (34) | 12.0% | 24.2% | 24.9% | 32.9% [30.1%-35.8%] | -- | -- | -- | -- | PASS | +12.2 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 489.0, B 1766.0; serve-point win A 56.3%, B 38.3%; Elo A 1174.4, B 1280.4; model uncertainty 0.0285
* Form inputs: days since last match A 338, B 212; matches on record A 136, B 42; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.028, surface_pool_high +0.024, surface_dev_loose -0.015, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Takahata / TANGE vs Cheng CHEN / Connel -- M15 Yanagawa City QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28TAKTANCHECON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cheng CHEN / Connel (`KXITFDOUBLES-26OCT28TAKTANCHECON-CHECON`) | 0.41 / 0.71 (86) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Takahata / TANGE (`KXITFDOUBLES-26OCT28TAKTANCHECON-TAKTAN`) | 0.24 / 0.53 (53) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Back / Yamazaki vs Liu / Uchijima -- W35 Sydney QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28BACYAMLIUUCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Back / Yamazaki (`KXITFWDOUBLES-26OCT28BACYAMLIUUCH-BACYAM`) | 0.64 / 0.97 (139) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Liu / Uchijima (`KXITFWDOUBLES-26OCT28BACYAMLIUUCH-LIUUCH`) | 0.05 / 0.31 (36) | 18.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Anchisa Chanta vs Arina Varaksina -- W15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223005:255662:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anchisa Chanta (`KXITFWMATCH-26OCT28CHAVAR-CHA`) | 0.63 / 0.80 (4) | 71.5% | 89.9% | 94.1% | 89.3% [86.9%-91.4%] | -- | -- | -- | -- | PASS | +18.4 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Arina Varaksina (`KXITFWMATCH-26OCT28CHAVAR-VAR`) | 0.16 / 0.30 (3) | 23.0% | 10.1% | 5.9% | 10.7% [8.6%-13.1%] | -- | -- | -- | -- | PASS | -12.9 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2474.0, B 586.0; serve-point win A 57.2%, B 52.4%; Elo A 1599.6, B 1277.4; model uncertainty 0.0223
* Form inputs: days since last match A 184, B 191; matches on record A 171, B 27; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28CHAVAR-CHA  (YES = Anchisa Chanta)
Model: 90%
Kalshi: 72%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.002, surface_pool_high -0.008, surface_dev_loose +0.005, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hosoki / Nishimoto vs Sato / Tse -- W35 Sydney QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28HOSNISSATTSE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hosoki / Nishimoto (`KXITFWDOUBLES-26OCT28HOSNISSATTSE-HOSNIS`) | 0.05 / 0.96 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sato / Tse (`KXITFWDOUBLES-26OCT28HOSNISSATTSE-SATTSE`) | 0.05 / 0.97 (116) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Khan / McKenzie vs Chaudhari / Hoedt -- W35 Sydney QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28KHAMCKCHAHOE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chaudhari / Hoedt (`KXITFWDOUBLES-26OCT28KHAMCKCHAHOE-CHAHOE`) | 0.05 / 0.97 (138) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Khan / McKenzie (`KXITFWDOUBLES-26OCT28KHAMCKCHAHOE-KHAMCK`) | 0.05 / 0.96 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alexandra Malova vs Aditi Rawat -- W15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28MALRAW:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandra Malova (`KXITFWMATCH-26OCT28MALRAW-MAL`) | 0.80 / 0.96 (22) | 88.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aditi Rawat (`KXITFWMATCH-26OCT28MALRAW-RAW`) | 0.03 / 0.15 (79) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jeong Moon vs Kamonwan Yodpetch -- W15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222213:259907:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jeong Moon (`KXITFWMATCH-26OCT28MOOYOD-MOO`) | 0.04 / 0.16 (6) | 10.0% | 29.0% | 42.6% | 43.1% [42.6%-44.1%] | -- | -- | -- | -- | PASS | +19.1 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kamonwan Yodpetch (`KXITFWMATCH-26OCT28MOOYOD-YOD`) | 0.83 / 0.97 (279) | 90.0% | 71.0% | 57.4% | 56.9% [55.9%-57.4%] | -- | -- | -- | -- | PASS | -19.1 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1191.0, B 1037.0; serve-point win A 51.0%, B 44.8%; Elo A 1280.5, B 1326.6; model uncertainty 0.008
* Form inputs: days since last match A 219, B 184; matches on record A 51, B 72; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28MOOYOD-MOO  (YES = Jeong Moon)
Model: 29%
Kalshi: 10%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aruzhan Sagandykova vs Violet Apisah -- W15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221802:270061:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Violet Apisah (`KXITFWMATCH-26OCT28SAGAPI-API`) | 0.44 / 0.67 (75) | 55.5% | 31.4% | 31.6% | 45.8% [43.7%-46.8%] | -- | -- | -- | -- | PASS | -24.1 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Aruzhan Sagandykova (`KXITFWMATCH-26OCT28SAGAPI-SAG`) | 0.25 / 0.50 (14) | 37.5% | 68.6% | 68.4% | 54.2% [53.2%-56.3%] | -- | -- | -- | -- | PASS | +31.1 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1744.0, B 122.0; serve-point win A 57.3%, B 46.3%; Elo A 1403.7, B 1379.7; model uncertainty 0.0157
* Form inputs: days since last match A 32, B 2820; matches on record A 45, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28SAGAPI-SAG  (YES = Aruzhan Sagandykova)
Model: 69%
Kalshi: 38%
Gap: +31 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Saily Prashantkumar Thakkar vs Nagi Hanatani -- W15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211544:263658:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nagi Hanatani (`KXITFWMATCH-26OCT28THAHAN-HAN`) | 0.74 / 0.97 (301) | 85.5% | 83.8% | 48.9% | 65.6% [63.1%-71.3%] | -- | -- | -- | -- | PASS | -1.7 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Saily Prashantkumar Thakkar (`KXITFWMATCH-26OCT28THAHAN-THA`) | 0.04 / 0.12 (28) | 8.0% | 16.2% | 51.1% | 34.4% [28.7%-36.9%] | -- | -- | -- | -- | PASS | +8.2 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 301.0, B 1219.0; serve-point win A 48.8%, B 43.8%; Elo A 1183.5, B 1328.0; model uncertainty 0.0407
* Form inputs: days since last match A 184, B 184; matches on record A 11, B 446; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.029, surface_pool_high +0.020, surface_dev_loose -0.010, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Becroft / Shepp vs Beale / Vujic -- M25 Tamworth QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT28BECSHEBEAVUJ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Beale / Vujic (`KXITFDOUBLES-26OCT28BECSHEBEAVUJ-BEAVUJ`) | 0.26 / 0.57 (58) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Becroft / Shepp (`KXITFDOUBLES-26OCT28BECSHEBEAVUJ-BECSHE`) | 0.37 / 0.68 (78) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Meng Yi Chen vs Junhan Zhang -- W35 Kunshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221903:260694:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Meng Yi Chen (`KXITFWMATCH-26OCT28CHEZHA-CHE`) | 0.12 / 0.27 (9) | 19.5% | 42.0% | 42.1% | 46.3% [44.2%-48.4%] | -- | -- | -- | -- | PASS | +22.5 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Junhan Zhang (`KXITFWMATCH-26OCT28CHEZHA-ZHA`) | 0.69 / 0.82 (138) | 75.5% | 58.0% | 57.9% | 53.7% [51.6%-55.8%] | -- | -- | -- | -- | PASS | -17.5 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1394.0, B 2226.0; serve-point win A 56.2%, B 42.3%; Elo A 1382.4, B 1384.4; model uncertainty 0.0209
* Form inputs: days since last match A 233, B 30; matches on record A 162, B 95; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28CHEZHA-CHE  (YES = Meng Yi Chen)
Model: 42%
Kalshi: 20%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.011, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tiana Tian Deng vs Sijia Wei -- W35 Kunshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221096:260528:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tiana Tian Deng (`KXITFWMATCH-26OCT28DENWEI-DEN`) | 0.04 / 0.39 (11) | 21.5% | 6.6% | 17.9% | 10.5% [9.4%-12.3%] | -- | -- | -- | -- | PASS | -14.9 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sijia Wei (`KXITFWMATCH-26OCT28DENWEI-WEI`) | 0.62 / 0.97 (279) | 79.5% | 93.5% | 82.1% | 89.5% [87.7%-90.6%] | -- | -- | -- | -- | PASS | +13.9 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 853.0, B 2150.0; serve-point win A 48.4%, B 40.3%; Elo A 1288.7, B 1716.7; model uncertainty 0.0147
* Form inputs: days since last match A 114, B 23; matches on record A 41, B 308; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.005, surface_dev_loose -0.005, surface_dev_tight +0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Priska Madelyn Nugroho vs Yuhan Wang -- W35 Kunshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221187:264205:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Priska Madelyn Nugroho (`KXITFWMATCH-26OCT28NUGWAN-NUG`) | 0.38 / 0.67 (5) | 52.5% | 64.5% | 60.0% | 64.6% [63.1%-67.0%] | -- | -- | -- | -- | PASS | +12.0 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuhan Wang (`KXITFWMATCH-26OCT28NUGWAN-WAN`) | 0.37 / 0.56 (9) | 46.5% | 35.5% | 40.0% | 35.4% [33.0%-36.9%] | -- | -- | -- | -- | PASS | -11.0 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2457.0, B 1724.0; serve-point win A 56.0%, B 46.8%; Elo A 1567.2, B 1428.1; model uncertainty 0.0198
* Form inputs: days since last match A 212, B 27; matches on record A 235, B 44; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yidi Yang vs JiaYi Wang -- W35 Kunshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215820:265692:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| JiaYi Wang (`KXITFWMATCH-26OCT28YANWAN-WAN`) | 0.05 / 0.46 (11) | 25.5% | 41.1% | 59.0% | 50.5% [42.1%-54.8%] | -- | -- | -- | -- | PASS | +15.6 pp | HIGH_REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yidi Yang (`KXITFWMATCH-26OCT28YANWAN-YAN`) | 0.49 / 0.96 (4) | 72.5% | 58.9% | 41.0% | 49.5% [45.2%-57.9%] | -- | -- | -- | -- | PASS | -13.6 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3495.0, B 2216.0; serve-point win A 55.4%, B 46.3%; Elo A 1589.5, B 1510.1; model uncertainty 0.0636
* Form inputs: days since last match A 24, B 29; matches on record A 317, B 72; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28YANWAN-WAN  (YES = JiaYi Wang)
Model: 41%
Kalshi: 26%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.011, surface_dev_loose -0.016, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Shaheed Alam vs Maxime Janvier -- M15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126125:207180:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shaheed Alam (`KXITFMATCH-26OCT28ALAJAN-ALA`) | 0.06 / 0.95 (1) | 50.5% | 8.2% | 14.2% | 11.6% [10.6%-12.6%] | -- | -- | -- | -- | PASS | -42.2 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maxime Janvier (`KXITFMATCH-26OCT28ALAJAN-JAN`) | 0.06 / 0.96 (1) | 51.0% | 91.8% | 85.8% | 88.4% [87.4%-89.4%] | -- | -- | -- | -- | PASS | +40.8 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 112.0, B 4068.0; serve-point win A 56.0%, B 33.1%; Elo A 1109.9, B 1467.8; model uncertainty 0.0099
* Form inputs: days since last match A 443, B 44; matches on record A 17, B 773; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT28ALAJAN-JAN  (YES = Maxime Janvier)
Model: 92%
Kalshi: 51%
Gap: +41 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kosuke Ogura vs Madhwin Kamath -- M15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202124:209979:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Madhwin Kamath (`KXITFMATCH-26OCT28OGUKAM-KAM`) | 0.06 / 0.95 (1) | 50.5% | 44.3% | 34.0% | 39.8% [35.4%-43.9%] | -- | -- | -- | -- | PASS | -6.2 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kosuke Ogura (`KXITFMATCH-26OCT28OGUKAM-OGU`) | 0.06 / 0.96 (1) | 51.0% | 55.7% | 66.0% | 60.2% [56.1%-64.6%] | -- | -- | -- | -- | PASS | +4.7 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3125.0, B 843.0; serve-point win A 61.2%, B 40.0%; Elo A 1235.7, B 1186.8; model uncertainty 0.0421
* Form inputs: days since last match A 191, B 184; matches on record A 245, B 53; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.019, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lidia Podgorichani vs Yeri Hong -- W15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259946:270097:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yeri Hong (`KXITFWMATCH-26OCT28PODHON-HON`) | 0.51 / 0.76 (9) | 63.5% | 54.2% | 86.4% | 66.6% [63.6%-71.8%] | -- | -- | -- | -- | PASS | -9.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lidia Podgorichani (`KXITFWMATCH-26OCT28PODHON-POD`) | 0.20 / 0.40 (41) | 30.0% | 45.8% | 13.6% | 33.4% [28.2%-36.4%] | -- | -- | -- | -- | PASS | +15.8 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 317.0, B 172.0; serve-point win A 52.6%, B 46.6%; Elo A 1211.6, B 1309.3; model uncertainty 0.0409
* Form inputs: days since last match A 184, B 184; matches on record A 27, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28PODHON-POD  (YES = Lidia Podgorichani)
Model: 46%
Kalshi: 30%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stevens / Thompson vs Katsumi / Kozaki -- W35 Sydney QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT28STETHOKATKOZ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katsumi / Kozaki (`KXITFWDOUBLES-26OCT28STETHOKATKOZ-KATKOZ`) | 0.27 / 0.60 (62) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stevens / Thompson (`KXITFWDOUBLES-26OCT28STETHOKATKOZ-STETHO`) | 0.32 / 0.66 (73) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Yingqun Sun vs Remika Ohashi -- W15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260957:264029:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Remika Ohashi (`KXITFWMATCH-26OCT28SUNOHA-OHA`) | 0.07 / 0.31 (6) | 19.0% | 34.1% | 26.6% | 41.0% [36.0%-45.8%] | -- | -- | -- | -- | PASS | +15.1 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yingqun Sun (`KXITFWMATCH-26OCT28SUNOHA-SUN`) | 0.68 / 0.84 (6) | 76.0% | 65.9% | 73.4% | 59.0% [54.2%-64.0%] | -- | -- | -- | -- | PASS | -10.1 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1826.0, B 421.0; serve-point win A 56.8%, B 46.3%; Elo A 1387.9, B 1357.0; model uncertainty 0.0488
* Form inputs: days since last match A 184, B 191; matches on record A 99, B 44; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT28SUNOHA-OHA  (YES = Remika Ohashi)
Model: 34%
Kalshi: 19%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sevil Yuldasheva vs Thasaporn Naklo -- W15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-29T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:219874:220597:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thasaporn Naklo (`KXITFWMATCH-26OCT28YULNAK-NAK`) | 0.83 / 0.96 (22) | 89.5% | 83.7% | 75.1% | 79.1% [77.6%-80.3%] | -- | -- | -- | -- | PASS | -5.8 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sevil Yuldasheva (`KXITFWMATCH-26OCT28YULNAK-YUL`) | 0.03 / 0.15 (8) | 9.0% | 16.3% | 24.9% | 20.9% [19.7%-22.4%] | -- | -- | -- | -- | PASS | +7.3 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 808.0, B 2173.0; serve-point win A 51.4%, B 41.2%; Elo A 1209.3, B 1456.9; model uncertainty 0.0133
* Form inputs: days since last match A 184, B 184; matches on record A 155, B 166; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.004, surface_dev_loose -0.007, surface_dev_tight +0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Fukuda / Okabe vs Hashimoto / Fu Wong -- M15 Yanagawa City QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29FUKOKAHASFUW:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fukuda / Okabe (`KXITFDOUBLES-26OCT29FUKOKAHASFUW-FUKOKA`) | 0.01 / 0.99 (70) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hashimoto / Fu Wong (`KXITFDOUBLES-26OCT29FUKOKAHASFUW-HASFUW`) | 0.01 / 0.99 (70) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Katayama / Tanaka vs Kawachi / Yamanaka -- M15 Yanagawa City QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29KATTANKAWYAM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katayama / Tanaka (`KXITFDOUBLES-26OCT29KATTANKAWYAM-KATTAN`) | -- / 0.99 (50) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kawachi / Yamanaka (`KXITFDOUBLES-26OCT29KATTANKAWYAM-KAWYAM`) | -- / 0.99 (50) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE

## Komagata / Koyama vs Koizumi / Taka -- M15 Yanagawa City QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-29T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29KOMKOYKOITAK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Koizumi / Taka (`KXITFDOUBLES-26OCT29KOMKOYKOITAK-KOITAK`) | -- / 0.99 (50) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Komagata / Koyama (`KXITFDOUBLES-26OCT29KOMKOYKOITAK-KOMKOY`) | -- / 0.99 (50) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE

## Lilli Tagger vs Magda Linette -- WTA Guangzhou R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-29 08:00Z
* Current expected start: 2026-10-29 11:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-29 10:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-29T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202663:260172:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Magda Linette (`KXWTAMATCH-26OCT29TAGLIN-LIN`) | 0.29 / 0.30 (1515) | 29.5% | 41.1% | 33.1% | 42.9% [38.4%-50.5%] | 30.9% | -- | 30.9% | MODEL_LONE_OUTLIER | SHADOW_BET | +11.6 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Lilli Tagger (`KXWTAMATCH-26OCT29TAGLIN-TAG`) | 0.69 / 0.71 (2976) | 70.0% | 58.9% | 66.9% | 57.1% [49.5%-61.6%] | 69.1% | -- | 69.1% | MODEL_LONE_OUTLIER | PASS | -11.1 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2552.0, B 4278.0; serve-point win A 61.7%, B 40.1%; Elo A 1804.5, B 1879.0; model uncertainty 0.0606
* Form inputs: days since last match A 5, B 1; matches on record A 132, B 912; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose +0.005, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT29TAGLIN-17` Over 16.5 games: 0.24/0.94 mid 59.0%, model 95.8% (projection_v2.0 (prediction ledger)) -- gap +36.8 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT29TAGLIN-22` Over 21.5 games: 0.51/0.53 mid 52.0%, model 65.4% (projection_v2.0 (prediction ledger)) -- gap +13.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT29TAGLIN-1-TAG` Will Lilli Tagger win set 1 in the Lilli Tagger vs Magda Linette match: 0.64/0.68 mid 66.0%, model 55.9% (projection_v2.0 (prediction ledger)) -- gap -10.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT29TAGLIN-1-LIN` Will Magda Linette win set 1 in the Lilli Tagger vs Magda Linette match: 0.33/0.36 mid 34.5%, model 44.1% (projection_v2.0 (prediction ledger)) -- gap +9.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT29TAGLIN-27` Over 26.5 games: 0.03/0.98 mid 50.5%, model 41.8% (projection_v2.0 (prediction ledger)) -- gap -8.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT29TAGLIN-2-LIN` Will Magda Linette win set 2 in the Lilli Tagger vs Magda Linette match: 0.02/0.98 mid 50.0%, model 44.1% (projection_v2.0 (prediction ledger)) -- gap -5.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT29TAGLIN-2-TAG` Will Lilli Tagger win set 2 in the Lilli Tagger vs Magda Linette match: 0.02/0.99 mid 50.5%, model 55.9% (projection_v2.0 (prediction ledger)) -- gap +5.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; WIDE_SPREAD

## Alex Michelsen vs Arthur Fils -- ATP Basel R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-29 13:00Z
* Current expected start: 2026-10-29 13:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-29 12:15Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-29T04:00:00+00:00 as not a valid time; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-10-29T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:209950:210506:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arthur Fils (`KXATPMATCH-26OCT29MICFIL-FIL`) | 0.65 / 0.67 (19542) | 66.0% | 59.9% | 58.7% | 59.7% [56.3%-63.5%] | 65.2% | -- | 65.2% | MARKETS_AGREE | PASS | -6.1 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Alex Michelsen (`KXATPMATCH-26OCT29MICFIL-MIC`) | 0.33 / 0.35 (21464) | 34.0% | 40.1% | 41.3% | 40.3% [36.5%-43.7%] | 34.8% | -- | 34.8% | MARKETS_AGREE | WATCH | +6.1 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5733.0, B 4398.0; serve-point win A 64.6%, B 33.4%; Elo A 1956.7, B 2038.9; model uncertainty 0.0356
* Form inputs: days since last match A 5, B 4; matches on record A 316, B 335; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.024, surface_pool_high +0.034, surface_dev_loose -0.004, surface_dev_tight +0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT29MICFIL-18` Over 17.5 games: 0.13/0.97 mid 55.0%, model 94.8% (projection_v2.0 (prediction ledger)) -- gap +39.8 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29MICFIL-FIL6` Will Arthur Fils win at least 5.5 more games than Alex Michelsen?: 0.14/0.41 mid 27.5%, model 10.1% (projection_v2.0 (prediction ledger)) -- gap -17.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29MICFIL-MIC2` Will Alex Michelsen win at least 1.5 more games than Arthur Fils?: 0.26/0.66 mid 46.0%, model 32.6% (projection_v2.0 (prediction ledger)) -- gap -13.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT29MICFIL-23` Over 22.5 games: 0.50/0.52 mid 51.0%, model 62.5% (projection_v2.0 (prediction ledger)) -- gap +11.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29MICFIL-1-FIL` Will Arthur Fils win set 1 in the Alex Michelsen vs Arthur Fils match: 0.60/0.74 mid 67.0%, model 56.6% (projection_v2.0 (prediction ledger)) -- gap -10.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT29MICFIL-FIL3` Will Arthur Fils win at least 2.5 more games than Alex Michelsen?: 0.52/0.55 mid 53.5%, model 43.7% (projection_v2.0 (prediction ledger)) -- gap -9.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT29MICFIL-28` Over 27.5 games: 0.05/0.97 mid 51.0%, model 42.0% (projection_v2.0 (prediction ledger)) -- gap -9.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29MICFIL-MIC21` Will Alex Michelsen win the Alex Michelsen vs Arthur Fils match by a set score of 2-1?: 0.07/0.18 mid 12.5%, model 21.3% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29MICFIL-2-FIL` Will Arthur Fils win set 2 in the Alex Michelsen vs Arthur Fils match: 0.01/0.98 mid 49.5%, model 56.6% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT29MICFIL-2-MIC` Will Alex Michelsen win set 2 in the Alex Michelsen vs Arthur Fils match: 0.02/0.98 mid 50.0%, model 43.4% (projection_v2.0 (prediction ledger)) -- gap -6.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29MICFIL-FIL21` Will Arthur Fils win the Alex Michelsen vs Arthur Fils match by a set score of 2-1?: 0.16/0.29 mid 22.5%, model 27.8% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29MICFIL-1-MIC` Will Alex Michelsen win set 1 in the Alex Michelsen vs Arthur Fils match: 0.37/0.41 mid 39.0%, model 43.4% (projection_v2.0 (prediction ledger)) -- gap +4.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29MICFIL-MIC20` Will Alex Michelsen win the Alex Michelsen vs Arthur Fils match by a set score of 2-0?: 0.08/0.23 mid 15.5%, model 18.8% (projection_v2.0 (prediction ledger)) -- gap +3.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29MICFIL-FIL20` Will Arthur Fils win the Alex Michelsen vs Arthur Fils match by a set score of 2-0?: 0.19/0.49 mid 34.0%, model 32.1% (projection_v2.0 (prediction ledger)) -- gap -1.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ben Shelton vs Jerome Kym -- ATP Basel R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-29 13:00Z
* Current expected start: 2026-10-29 13:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-29 12:15Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-29T04:00:00+00:00 as not a valid time; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-10-29T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208843:210097:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jerome Kym (`KXATPMATCH-26OCT29SHEKYM-KYM`) | 0.26 / 0.27 (1482) | 26.5% | 19.5% | 32.5% | 25.3% [21.7%-28.4%] | 27.4% | -- | 27.4% | MODEL_LONE_OUTLIER | PASS | -7.0 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Ben Shelton (`KXATPMATCH-26OCT29SHEKYM-SHE`) | 0.73 / 0.74 (244) | 73.5% | 80.5% | 67.5% | 74.7% [71.6%-78.3%] | 72.6% | -- | 72.6% | MODEL_LONE_OUTLIER | PASS | +7.0 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 6529.0, B 3871.0; serve-point win A 73.6%, B 33.8%; Elo A 2079.3, B 1729.5; model uncertainty 0.0335
* Form inputs: days since last match A 17, B 16; matches on record A 315, B 277; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.000, surface_dev_loose -0.008, surface_dev_tight -0.003
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT29SHEKYM-20` Over 19.5 games: 0.05/0.97 mid 51.0%, model 83.7% (projection_v2.0 (prediction ledger)) -- gap +32.7 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29SHEKYM-SHE20` Will Ben Shelton win the Ben Shelton vs Jerome Kym match by a set score of 2-0?: 0.01/0.56 mid 28.5%, model 51.4% (projection_v2.0 (prediction ledger)) -- gap +22.9 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29SHEKYM-2-SHE` Will Ben Shelton win set 2 in the Ben Shelton vs Jerome Kym match: 0.01/0.98 mid 49.5%, model 71.7% (projection_v2.0 (prediction ledger)) -- gap +22.2 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT29SHEKYM-2-KYM` Will Jerome Kym win set 2 in the Ben Shelton vs Jerome Kym match: 0.01/0.98 mid 49.5%, model 28.3% (projection_v2.0 (prediction ledger)) -- gap -21.2 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT29SHEKYM-30` Over 29.5 games: 0.05/0.97 mid 51.0%, model 32.5% (projection_v2.0 (prediction ledger)) -- gap -18.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29SHEKYM-KYM20` Will Jerome Kym win the Ben Shelton vs Jerome Kym match by a set score of 2-0?: 0.02/0.48 mid 25.0%, model 8.0% (projection_v2.0 (prediction ledger)) -- gap -17.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29SHEKYM-KYM21` Will Jerome Kym win the Ben Shelton vs Jerome Kym match by a set score of 2-1?: 0.02/0.50 mid 26.0%, model 11.5% (projection_v2.0 (prediction ledger)) -- gap -14.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29SHEKYM-SHE21` Will Ben Shelton win the Ben Shelton vs Jerome Kym match by a set score of 2-1?: 0.01/0.30 mid 15.5%, model 29.1% (projection_v2.0 (prediction ledger)) -- gap +13.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29SHEKYM-SHE3` Will Ben Shelton win at least 2.5 more games than Jerome Kym?: 0.54/0.56 mid 55.0%, model 61.8% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29SHEKYM-KYM2` Will Jerome Kym win at least 1.5 more games than Ben Shelton?: 0.17/0.23 mid 20.0%, model 13.8% (projection_v2.0 (prediction ledger)) -- gap -6.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29SHEKYM-1-KYM` Will Jerome Kym win set 1 in the Ben Shelton vs Jerome Kym match: 0.31/0.34 mid 32.5%, model 28.3% (projection_v2.0 (prediction ledger)) -- gap -4.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT29SHEKYM-1-SHE` Will Ben Shelton win set 1 in the Ben Shelton vs Jerome Kym match: 0.66/0.69 mid 67.5%, model 71.7% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT29SHEKYM-25` Over 24.5 games: 0.50/0.52 mid 51.0%, model 49.6% (projection_v2.0 (prediction ledger)) -- gap -1.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29SHEKYM-SHE6` Will Ben Shelton win at least 5.5 more games than Jerome Kym?: 0.09/0.16 mid 12.5%, model 12.3% (projection_v2.0 (prediction ledger)) -- gap -0.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Valentin Vacherot vs Rafael Jodar -- ATP Basel R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-29 13:00Z
* Current expected start: 2026-10-29 13:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-28 11:38Z
* Recommended handicap-by time: 2026-10-29 12:15Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-29T04:00:00+00:00 as not a valid time; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-10-29T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200473:212588:2026-10-29`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rafael Jodar (`KXATPMATCH-26OCT29VACJOD-JOD`) | 0.71 / 0.74 (32298) | 72.5% | 72.0% | 68.0% | 68.5% [67.6%-68.9%] | 71.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.5 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valentin Vacherot (`KXATPMATCH-26OCT29VACJOD-VAC`) | 0.27 / 0.29 (42905) | 28.0% | 28.0% | 32.0% | 31.5% [31.1%-32.4%] | 28.2% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | -0.0 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4676.0, B 5268.0; serve-point win A 62.8%, B 32.4%; Elo A 1885.1, B 2021.5; model uncertainty 0.0064
* Form inputs: days since last match A 2, B 10; matches on record A 423, B 140; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.001, surface_dev_tight +0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT29VACJOD-VAC2` Will Valentin Vacherot win at least 1.5 more games than Rafael Jodar?: 0.20/0.97 mid 58.5%, model 21.7% (projection_v2.0 (prediction ledger)) -- gap -36.8 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29VACJOD-2-JOD` Will Rafael Jodar win set 2 in the Valentin Vacherot vs Rafael Jodar match: 0.01/0.98 mid 49.5%, model 65.1% (projection_v2.0 (prediction ledger)) -- gap +15.6 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29VACJOD-JOD20` Will Rafael Jodar win the Valentin Vacherot vs Rafael Jodar match by a set score of 2-0?: 0.01/0.54 mid 27.5%, model 42.4% (projection_v2.0 (prediction ledger)) -- gap +14.9 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29VACJOD-2-VAC` Will Valentin Vacherot win set 2 in the Valentin Vacherot vs Rafael Jodar match: 0.01/0.98 mid 49.5%, model 34.9% (projection_v2.0 (prediction ledger)) -- gap -14.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT29VACJOD-JOD7` Will Rafael Jodar win at least 6.5 more games than Valentin Vacherot?: 0.06/0.36 mid 21.0%, model 8.1% (projection_v2.0 (prediction ledger)) -- gap -12.9 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29VACJOD-JOD21` Will Rafael Jodar win the Valentin Vacherot vs Rafael Jodar match by a set score of 2-1?: 0.09/0.29 mid 19.0%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap +10.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT29VACJOD-23` Over 22.5 games: 0.47/0.49 mid 48.0%, model 57.8% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT29VACJOD-JOD4` Will Rafael Jodar win at least 3.5 more games than Valentin Vacherot?: 0.51/0.53 mid 52.0%, model 44.1% (projection_v2.0 (prediction ledger)) -- gap -7.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT29VACJOD-28` Over 27.5 games: 0.29/0.33 mid 31.0%, model 38.0% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT29VACJOD-18` Over 17.5 games: 0.86/0.88 mid 87.0%, model 92.8% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29VACJOD-VAC20` Will Valentin Vacherot win the Valentin Vacherot vs Rafael Jodar match by a set score of 2-0?: 0.02/0.29 mid 15.5%, model 12.2% (projection_v2.0 (prediction ledger)) -- gap -3.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT29VACJOD-1-JOD` Will Rafael Jodar win set 1 in the Valentin Vacherot vs Rafael Jodar match: 0.65/0.69 mid 67.0%, model 65.1% (projection_v2.0 (prediction ledger)) -- gap -1.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT29VACJOD-1-VAC` Will Valentin Vacherot win set 1 in the Valentin Vacherot vs Rafael Jodar match: 0.32/0.34 mid 33.0%, model 34.9% (projection_v2.0 (prediction ledger)) -- gap +1.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT29VACJOD-VAC21` Will Valentin Vacherot win the Valentin Vacherot vs Rafael Jodar match by a set score of 2-1?: 0.09/0.20 mid 14.5%, model 15.8% (projection_v2.0 (prediction ledger)) -- gap +1.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Francisco Cabral / James Tracy vs Henry Bernet / Dominic Stricker -- ATP Basel QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-29 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-29T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT29CABTRABERSTR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Henry Bernet / Dominic Stricker (`KXATPDOUBLES-26OCT29CABTRABERSTR-BERSTR`) | 0.32 / 0.38 (777) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Francisco Cabral / James Tracy (`KXATPDOUBLES-26OCT29CABTRABERSTR-CABTRA`) | 0.58 / 0.67 (58) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Tommy Paul vs Luciano Darderi -- ATP Vienna R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-29 15:00Z
* Current expected start: 2026-10-29 15:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: 2026-10-29 14:15Z

* Status notes: NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source)

ATP (TOUR_500_250) · Clay · scheduled 2026-10-29T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT29PAUDAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luciano Darderi (`KXATPMATCH-26OCT29PAUDAR-DAR`) | 0.19 / 0.21 (324) | 20.0% | 43.8% | -- | -- [-----] | -- | -- | -- | -- | -- | +23.8 pp | HIGH_REVIEW (DATA_WARNING) | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Tommy Paul (`KXATPMATCH-26OCT29PAUDAR-PAU`) | 0.79 / 0.80 (4000) | 79.5% | 56.2% | -- | -- [-----] | -- | -- | -- | -- | -- | -23.3 pp | HIGH_REVIEW (DATA_WARNING) | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 63.3%, B 37.9%; Elo A 1998.1, B 1994.2; model uncertainty None
* Form inputs: days since last match A 4, B 2; matches on record A 729, B 438; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT29PAUDAR-DAR  (YES = Luciano Darderi)
Model: 44%
Kalshi: 20%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: EVENT_MAPPING_RISK, NO_EXTERNAL_REFERENCE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Warnings: BET_BLOCKED_START_STATUS; NO_EXTERNAL_PRICE

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
