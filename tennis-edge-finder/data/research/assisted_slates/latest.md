# ASSISTED SLATE -- 2026-10-19T08:37Z (`SL-20261019T083721Z-d1c5aa19`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

263 open matches not seen started, 1056 markets. Skipped: {"no_match_winner_listed": 5, "first_ball_already_observed": 4, "scheduled_start_over_24h_past": 1}. Sources: shadow board 2026-10-19T06:08:59.066995+00:00, Model 4 2026-10-19T06:09:32.153680+00:00, Gen-1 ledger 2026-10-19T06:08:55.837342+00:00, external 2026-10-19T08:24:16.307618+00:00, capture 20261019T082157Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-10-19 09:00Z**
* Recommended RUN TENNIS time: **2026-10-19 08:15Z**  (**OVERDUE -- run now**)
* Final price/status check time: **2026-10-19 08:50Z**
* Number of matches in window: 6 (Pierre-Hugues Herbert vs Maxim Mrva, Marin Cilic vs Nikoloz Basilashvili, Kamilla Rakhimova vs Marie Bouzkova, Federico Cina vs Jaume Munar, Vitaliy Sachko vs Borna Gojo, Kyrian Jacquet vs Michael Mmoh)

* **24 main-tour match(es) have NO verified start status** (START_UNKNOWN, STATUS_AMBIGUOUS): BET blocked until a live status check.

Slate built 2026-10-19T08:37Z. Refresh due by: 2026-10-19 08:15Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 40, "HIGH_REVIEW": 96, "NORMAL": 493, "REVIEW": 130, "UNPRICED": 297}; match winners: {"EXTREME": 31, "HIGH_REVIEW": 55, "NORMAL": 163, "REVIEW": 39, "UNPRICED": 238}; quote freshness at build: {"FRESH": 759}.

## Terence Atmane vs Rinky Hijikata -- ATP Almaty R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-20T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208014:209279:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Terence Atmane (`KXATPMATCH-26OCT18ATMHIJ-ATM`) | 0.46 / 0.48 (22509) | 47.0% | 47.2% | 54.9% | 52.9% [48.5%-54.4%] | -- | -- | -- | -- | WATCH | +0.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rinky Hijikata (`KXATPMATCH-26OCT18ATMHIJ-HIJ`) | 0.53 / 0.54 (17558) | 53.5% | 52.8% | 45.1% | 47.1% [45.6%-51.5%] | -- | -- | -- | -- | PASS | -0.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4446.0, B 5282.0; serve-point win A 65.7%, B 33.7%; Elo A 1764.1, B 1794.6; model uncertainty 0.0292
* Form inputs: days since last match A 13, B 11; matches on record A 397, B 434; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18ATMHIJ-24` Over 23.5 games: 0.45/0.46 mid 45.5%, model 56.3% (projection_v2.0 (prediction ledger)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18ATMHIJ-ATM6` Will Terence Atmane win at least 5.5 more games than Rinky Hijikata?: 0.01/0.29 mid 15.0%, model 5.7% (projection_v2.0 (prediction ledger)) -- gap -9.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18ATMHIJ-29` Over 28.5 games: 0.27/0.34 mid 30.5%, model 39.1% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18ATMHIJ-19` Over 18.5 games: 0.83/0.88 mid 85.5%, model 91.2% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18ATMHIJ-ATM3` Will Terence Atmane win at least 2.5 more games than Rinky Hijikata?: 0.34/0.37 mid 35.5%, model 31.0% (projection_v2.0 (prediction ledger)) -- gap -4.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18ATMHIJ-HIJ21` Will Rinky Hijikata win the Terence Atmane vs Rinky Hijikata match by a set score of 2-1?: 0.20/0.23 mid 21.5%, model 25.9% (projection_v2.0 (prediction ledger)) -- gap +4.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18ATMHIJ-HIJ20` Will Rinky Hijikata win the Terence Atmane vs Rinky Hijikata match by a set score of 2-0?: 0.29/0.33 mid 31.0%, model 26.9% (projection_v2.0 (prediction ledger)) -- gap -4.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18ATMHIJ-ATM21` Will Terence Atmane win the Terence Atmane vs Rinky Hijikata match by a set score of 2-1?: 0.19/0.22 mid 20.5%, model 24.0% (projection_v2.0 (prediction ledger)) -- gap +3.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18ATMHIJ-ATM20` Will Terence Atmane win the Terence Atmane vs Rinky Hijikata match by a set score of 2-0?: 0.25/0.28 mid 26.5%, model 23.2% (projection_v2.0 (prediction ledger)) -- gap -3.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18ATMHIJ-HIJ2` Will Rinky Hijikata win at least 1.5 more games than Terence Atmane?: 0.45/0.48 mid 46.5%, model 45.6% (projection_v2.0 (prediction ledger)) -- gap -0.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ATMHIJ-1-HIJ` Will Rinky Hijikata win set 1 in the Terence Atmane vs Rinky Hijikata match: 0.49/0.53 mid 51.0%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap +0.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ATMHIJ-1-ATM` Will Terence Atmane win set 1 in the Terence Atmane vs Rinky Hijikata match: 0.46/0.51 mid 48.5%, model 48.1% (projection_v2.0 (prediction ledger)) -- gap -0.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ATMHIJ-2-ATM` Will Terence Atmane win set 2 in the Terence Atmane vs Rinky Hijikata match: 0.46/0.51 mid 48.5%, model 48.1% (projection_v2.0 (prediction ledger)) -- gap -0.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ATMHIJ-2-HIJ` Will Rinky Hijikata win set 2 in the Terence Atmane vs Rinky Hijikata match: 0.49/0.54 mid 51.5%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap +0.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD

## N. Sriram Balaji / Evan King vs Anirudh Chandrasekar / Ray Ho -- ATP Almaty R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-18 10:21Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18BALKINCHARAY:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N. Sriram Balaji / Evan King (`KXATPDOUBLES-26OCT18BALKINCHARAY-BALKIN`) | 0.27 / 0.88 (25) | 57.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anirudh Chandrasekar / Ray Ho (`KXATPDOUBLES-26OCT18BALKINCHARAY-CHARAY`) | 0.11 / 0.79 (2) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mattia Bellucci vs Tomas Martin Etcheverry -- ATP Almaty R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-20T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144869:208233:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mattia Bellucci (`KXATPMATCH-26OCT18BELETC-BEL`) | 0.50 / 0.51 (3000) | 50.5% | 57.8% | 48.5% | 50.0% [49.5%-51.5%] | -- | -- | -- | -- | PASS | +7.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tomas Martin Etcheverry (`KXATPMATCH-26OCT18BELETC-ETC`) | 0.48 / 0.50 (35399) | 49.0% | 42.2% | 51.4% | 50.0% [48.5%-50.5%] | -- | -- | -- | -- | PASS | -6.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4439.0, B 5437.0; serve-point win A 67.4%, B 34.3%; Elo A 1795.9, B 1757.3; model uncertainty 0.0097
* Form inputs: days since last match A 11, B 8; matches on record A 394, B 635; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.000, surface_dev_loose +0.010, surface_dev_tight -0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18BELETC-25` Over 24.5 games: 0.43/0.46 mid 44.5%, model 55.6% (projection_v2.0 (prediction ledger)) -- gap +11.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18BELETC-30` Over 29.5 games: 0.22/0.29 mid 25.5%, model 35.3% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18BELETC-ETC20` Will Tomas Martin Etcheverry win the Mattia Bellucci vs Tomas Martin Etcheverry match by a set score of 2-0?: 0.26/0.30 mid 28.0%, model 20.0% (projection_v2.0 (prediction ledger)) -- gap -8.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18BELETC-ETC2` Will Tomas Martin Etcheverry win at least 1.5 more games than Mattia Bellucci?: 0.42/0.44 mid 43.0%, model 35.1% (projection_v2.0 (prediction ledger)) -- gap -7.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18BELETC-20` Over 19.5 games: 0.75/0.79 mid 77.0%, model 84.8% (projection_v2.0 (prediction ledger)) -- gap +7.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18BELETC-BEL5` Will Mattia Bellucci win at least 4.5 more games than Tomas Martin Etcheverry?: 0.17/0.29 mid 23.0%, model 16.7% (projection_v2.0 (prediction ledger)) -- gap -6.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18BELETC-BEL21` Will Mattia Bellucci win the Mattia Bellucci vs Tomas Martin Etcheverry match by a set score of 2-1?: 0.20/0.23 mid 21.5%, model 27.3% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BELETC-1-BEL` Will Mattia Bellucci win set 1 in the Mattia Bellucci vs Tomas Martin Etcheverry match: 0.48/0.52 mid 50.0%, model 55.2% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BELETC-1-ETC` Will Tomas Martin Etcheverry win set 1 in the Mattia Bellucci vs Tomas Martin Etcheverry match: 0.48/0.51 mid 49.5%, model 44.8% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BELETC-2-BEL` Will Mattia Bellucci win set 2 in the Mattia Bellucci vs Tomas Martin Etcheverry match: 0.48/0.53 mid 50.5%, model 55.2% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BELETC-2-ETC` Will Tomas Martin Etcheverry win set 2 in the Mattia Bellucci vs Tomas Martin Etcheverry match: 0.47/0.52 mid 49.5%, model 44.8% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT18BELETC-BEL2` Will Mattia Bellucci win at least 1.5 more games than Tomas Martin Etcheverry?: 0.45/0.47 mid 46.0%, model 48.9% (projection_v2.0 (prediction ledger)) -- gap +2.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18BELETC-ETC21` Will Tomas Martin Etcheverry win the Mattia Bellucci vs Tomas Martin Etcheverry match by a set score of 2-1?: 0.19/0.22 mid 20.5%, model 22.1% (projection_v2.0 (prediction ledger)) -- gap +1.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18BELETC-BEL20` Will Mattia Bellucci win the Mattia Bellucci vs Tomas Martin Etcheverry match by a set score of 2-0?: 0.28/0.31 mid 29.5%, model 30.5% (projection_v2.0 (prediction ledger)) -- gap +1.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sander Gille / Sem Verbeek vs Yuki Bhambri / Ryan Seggerman -- ATP Almaty R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-19 07:38Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18GILVERBHASEG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuki Bhambri / Ryan Seggerman (`KXATPDOUBLES-26OCT18GILVERBHASEG-BHASEG`) | 0.29 / 0.71 (1) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sander Gille / Sem Verbeek (`KXATPDOUBLES-26OCT18GILVERBHASEG-GILVER`) | 0.31 / 0.54 (6) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Rinky Hijikata / Adam Walton vs Alexander Bublik / Zangar Nurlanuly -- ATP Almaty R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-18 10:21Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18HIJWALBUBNUR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Bublik / Zangar Nurlanuly (`KXATPDOUBLES-26OCT18HIJWALBUBNUR-BUBNUR`) | 0.20 / 0.27 (2) | 23.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rinky Hijikata / Adam Walton (`KXATPDOUBLES-26OCT18HIJWALBUBNUR-HIJWAL`) | 0.72 / 0.77 (100) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nathaniel Lammons / Jackson Withrow vs Jakob Schnaitter / Mark Wallner -- ATP Almaty R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-18 10:21Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18LAMWITSCHWAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nathaniel Lammons / Jackson Withrow (`KXATPDOUBLES-26OCT18LAMWITSCHWAL-LAMWIT`) | 0.40 / 0.44 (100) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jakob Schnaitter / Mark Wallner (`KXATPDOUBLES-26OCT18LAMWITSCHWAL-SCHWAL`) | 0.54 / 0.60 (150) | 57.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Fabian Marozsan vs Timofey Skatov -- ATP Almaty R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-18 10:21Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:206681:207608:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fabian Marozsan (`KXATPMATCH-26OCT18MARSKA-MAR`) | 0.73 / 0.74 (2455) | 73.5% | 73.8% | 70.9% | 72.6% [71.7%-73.8%] | -- | -- | -- | -- | PASS | +0.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Timofey Skatov (`KXATPMATCH-26OCT18MARSKA-SKA`) | 0.24 / 0.25 (3035) | 24.5% | 26.2% | 29.1% | 27.4% [26.2%-28.3%] | -- | -- | -- | -- | WATCH | +1.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4574.0, B 4414.0; serve-point win A 66.3%, B 38.8%; Elo A 1778.2, B 1562.5; model uncertainty 0.0103
* Form inputs: days since last match A 10, B 12; matches on record A 439, B 455; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.004, surface_dev_loose +0.012, surface_dev_tight -0.008
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT18MARSKA-MAR5` Will Fabian Marozsan win at least 4.5 more games than Timofey Skatov?: 0.46/0.47 mid 46.5%, model 34.3% (market_conditioned_v1 (model4_board_v1)) -- gap -12.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18MARSKA-23` Over 22.5 games: 0.42/0.44 mid 43.0%, model 54.4% (market_conditioned_v1 (model4_board_v1)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18MARSKA-28` Over 27.5 games: 0.20/0.29 mid 24.5%, model 35.1% (market_conditioned_v1 (model4_board_v1)) -- gap +10.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18MARSKA-18` Over 17.5 games: 0.79/0.86 mid 82.5%, model 90.4% (market_conditioned_v1 (model4_board_v1)) -- gap +7.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18MARSKA-MAR21` Will Fabian Marozsan win the Fabian Marozsan vs Timofey Skatov match by a set score of 2-1?: 0.20/0.24 mid 22.0%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap +7.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18MARSKA-MAR20` Will Fabian Marozsan win the Fabian Marozsan vs Timofey Skatov match by a set score of 2-0?: 0.50/0.52 mid 51.0%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap -6.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18MARSKA-SKA21` Will Timofey Skatov win the Fabian Marozsan vs Timofey Skatov match by a set score of 2-1?: 0.08/0.14 mid 11.0%, model 14.9% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MARSKA-1-SKA` Will Timofey Skatov win set 1 in the Fabian Marozsan vs Timofey Skatov match: 0.28/0.33 mid 30.5%, model 33.5% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MARSKA-2-MAR` Will Fabian Marozsan win set 2 in the Fabian Marozsan vs Timofey Skatov match: 0.67/0.72 mid 69.5%, model 66.5% (projection_v2.0 (prediction ledger)) -- gap -3.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MARSKA-2-SKA` Will Timofey Skatov win set 2 in the Fabian Marozsan vs Timofey Skatov match: 0.28/0.33 mid 30.5%, model 33.5% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MARSKA-1-MAR` Will Fabian Marozsan win set 1 in the Fabian Marozsan vs Timofey Skatov match: 0.67/0.71 mid 69.0%, model 66.5% (projection_v2.0 (prediction ledger)) -- gap -2.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT18MARSKA-MAR2` Will Fabian Marozsan win at least 1.5 more games than Timofey Skatov?: 0.68/0.73 mid 70.5%, model 69.0% (market_conditioned_v1 (model4_board_v1)) -- gap -1.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18MARSKA-SKA20` Will Timofey Skatov win the Fabian Marozsan vs Timofey Skatov match by a set score of 2-0?: 0.08/0.14 mid 11.0%, model 11.2% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lucas Miedler / Neil Oberleitner vs Amir Omarkhanov / Beibit Zhukayev -- ATP Almaty R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-18 10:21Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18MIEOBEOMAZHU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucas Miedler / Neil Oberleitner (`KXATPDOUBLES-26OCT18MIEOBEOMAZHU-MIEOBE`) | 0.87 / 0.89 (300) | 88.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Amir Omarkhanov / Beibit Zhukayev (`KXATPDOUBLES-26OCT18MIEOBEOMAZHU-OMAZHU`) | 0.09 / 0.12 (1) | 10.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Zangar Nurlanuly vs Tomas Machac -- ATP Almaty R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-18 10:21Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207830:tml:N0GN:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomas Machac (`KXATPMATCH-26OCT18NURMAC-MAC`) | 0.95 / 0.96 (685) | 95.5% | 98.1% | 88.3% | 96.2% [94.8%-97.6%] | -- | -- | -- | -- | PASS | +2.6 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zangar Nurlanuly (`KXATPMATCH-26OCT18NURMAC-NUR`) | 0.04 / 0.05 (13585) | 4.5% | 1.9% | 11.7% | 3.8% [2.4%-5.2%] | -- | -- | -- | -- | PASS | -2.6 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 195.0, B 3439.0; serve-point win A 54.0%, B 29.4%; Elo A 1329.8, B 1926.2; model uncertainty 0.014
* Form inputs: days since last match A 69, B 9; matches on record A 4, B 440; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.014, surface_dev_loose +0.000, surface_dev_tight -0.001
* Derivatives listed: 13 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 13 carry a model probability
  * `KXATPGTOTAL-26OCT18NURMAC-19` Over 18.5 games: 0.43/0.47 mid 45.0%, model 59.8% (market_conditioned_v1 (model4_board_v1)) -- gap +14.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data POOR
  * `KXATPGSPREAD-26OCT18NURMAC-MAC7` Will Tomas Machac win at least 6.5 more games than Zangar Nurlanuly?: 0.42/0.49 mid 45.5%, model 33.5% (market_conditioned_v1 (model4_board_v1)) -- gap -12.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data POOR
  * `KXATPGTOTAL-26OCT18NURMAC-24` Over 23.5 games: 0.12/0.19 mid 15.5%, model 25.1% (market_conditioned_v1 (model4_board_v1)) -- gap +9.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPSETWINNER-26OCT18NURMAC-1-MAC` Will Tomas Machac win set 1 in the Zangar Nurlanuly vs Tomas Machac match: 0.74/0.92 mid 83.0%, model 91.9% (projection_v2.0 (prediction ledger)) -- gap +8.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT18NURMAC-2-NUR` Will Zangar Nurlanuly win set 2 in the Zangar Nurlanuly vs Tomas Machac match: 0.05/0.25 mid 15.0%, model 8.1% (projection_v2.0 (prediction ledger)) -- gap -6.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT18NURMAC-1-NUR` Will Zangar Nurlanuly win set 1 in the Zangar Nurlanuly vs Tomas Machac match: 0.07/0.20 mid 13.5%, model 8.1% (projection_v2.0 (prediction ledger)) -- gap -5.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPEXACTMATCH-26OCT18NURMAC-MAC21` Will Tomas Machac win the Zangar Nurlanuly vs Tomas Machac match by a set score of 2-1?: 0.07/0.13 mid 10.0%, model 13.7% (projection_v2.0 (prediction ledger)) -- gap +3.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPGSPREAD-26OCT18NURMAC-MAC4` Will Tomas Machac win at least 3.5 more games than Zangar Nurlanuly?: 0.80/0.91 mid 85.5%, model 81.9% (market_conditioned_v1 (model4_board_v1)) -- gap -3.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPGSPREAD-26OCT18NURMAC-MAC10` Will Tomas Machac win at least 9.5 more games than Zangar Nurlanuly?: 0.01/0.11 mid 6.0%, model 3.1% (market_conditioned_v1 (model4_board_v1)) -- gap -2.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPEXACTMATCH-26OCT18NURMAC-MAC20` Will Tomas Machac win the Zangar Nurlanuly vs Tomas Machac match by a set score of 2-0?: 0.81/0.85 mid 83.0%, model 84.5% (projection_v2.0 (prediction ledger)) -- gap +1.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPSETWINNER-26OCT18NURMAC-2-MAC` Will Tomas Machac win set 2 in the Zangar Nurlanuly vs Tomas Machac match: 0.89/0.93 mid 91.0%, model 91.9% (projection_v2.0 (prediction ledger)) -- gap +0.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data POOR
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jean-Julien Rojer / Theodore Winegar vs Facundo Diaz Acosta / Thiago Agustin Tirante -- ATP Almaty R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-18 10:21Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18ROJWINDIATIR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Facundo Diaz Acosta / Thiago Agustin Tirante (`KXATPDOUBLES-26OCT18ROJWINDIATIR-DIATIR`) | 0.13 / 0.70 (72) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jean-Julien Rojer / Theodore Winegar (`KXATPDOUBLES-26OCT18ROJWINDIATIR-ROJWIN`) | 0.31 / 0.90 (66) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Stefanos Tsitsipas vs Aleksandar Kovacevic -- ATP Almaty R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-20T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126774:206499:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aleksandar Kovacevic (`KXATPMATCH-26OCT18TSIKOV-KOV`) | 0.20 / 0.21 (100) | 20.5% | 27.2% | 32.6% | 30.5% [23.5%-35.1%] | -- | -- | -- | -- | SHADOW_BET | +6.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stefanos Tsitsipas (`KXATPMATCH-26OCT18TSIKOV-TSI`) | 0.78 / 0.79 (1385) | 78.5% | 72.8% | 67.4% | 69.5% [64.9%-76.5%] | -- | -- | -- | -- | PASS | -5.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5084.0, B 4809.0; serve-point win A 73.1%, B 32.2%; Elo A 1952.1, B 1756.9; model uncertainty 0.0581
* Form inputs: days since last match A 4, B 11; matches on record A 801, B 399; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.039, surface_pool_high -0.046, surface_dev_loose -0.008, surface_dev_tight +0.013
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18TSIKOV-23` Over 22.5 games: 0.52/0.54 mid 53.0%, model 65.5% (projection_v2.0 (prediction ledger)) -- gap +12.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18TSIKOV-28` Over 27.5 games: 0.27/0.32 mid 29.5%, model 41.7% (projection_v2.0 (prediction ledger)) -- gap +12.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18TSIKOV-TSI20` Will Stefanos Tsitsipas win the Stefanos Tsitsipas vs Aleksandar Kovacevic match by a set score of 2-0?: 0.53/0.57 mid 55.0%, model 43.2% (projection_v2.0 (prediction ledger)) -- gap -11.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18TSIKOV-TSI4` Will Stefanos Tsitsipas win at least 3.5 more games than Aleksandar Kovacevic?: 0.47/0.48 mid 47.5%, model 36.5% (projection_v2.0 (prediction ledger)) -- gap -11.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18TSIKOV-1-KOV` Will Aleksandar Kovacevic win set 1 in the Stefanos Tsitsipas vs Aleksandar Kovacevic match: 0.25/0.29 mid 27.0%, model 34.3% (projection_v2.0 (prediction ledger)) -- gap +7.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18TSIKOV-1-TSI` Will Stefanos Tsitsipas win set 1 in the Stefanos Tsitsipas vs Aleksandar Kovacevic match: 0.71/0.75 mid 73.0%, model 65.7% (projection_v2.0 (prediction ledger)) -- gap -7.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18TSIKOV-2-KOV` Will Aleksandar Kovacevic win set 2 in the Stefanos Tsitsipas vs Aleksandar Kovacevic match: 0.25/0.30 mid 27.5%, model 34.3% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18TSIKOV-2-TSI` Will Stefanos Tsitsipas win set 2 in the Stefanos Tsitsipas vs Aleksandar Kovacevic match: 0.70/0.75 mid 72.5%, model 65.7% (projection_v2.0 (prediction ledger)) -- gap -6.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT18TSIKOV-TSI7` Will Stefanos Tsitsipas win at least 6.5 more games than Aleksandar Kovacevic?: 0.08/0.12 mid 10.0%, model 3.5% (projection_v2.0 (prediction ledger)) -- gap -6.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18TSIKOV-KOV21` Will Aleksandar Kovacevic win the Stefanos Tsitsipas vs Aleksandar Kovacevic match by a set score of 2-1?: 0.06/0.12 mid 9.0%, model 15.4% (projection_v2.0 (prediction ledger)) -- gap +6.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18TSIKOV-TSI21` Will Stefanos Tsitsipas win the Stefanos Tsitsipas vs Aleksandar Kovacevic match by a set score of 2-1?: 0.22/0.26 mid 24.0%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap +5.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18TSIKOV-KOV2` Will Aleksandar Kovacevic win at least 1.5 more games than Stefanos Tsitsipas?: 0.09/0.18 mid 13.5%, model 18.8% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18TSIKOV-18` Over 17.5 games: 0.90/0.97 mid 93.5%, model 97.0% (projection_v2.0 (prediction ledger)) -- gap +3.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18TSIKOV-KOV20` Will Aleksandar Kovacevic win the Stefanos Tsitsipas vs Aleksandar Kovacevic match by a set score of 2-0?: 0.08/0.11 mid 9.5%, model 11.7% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Daniel Altmaier vs Titouan Droguet -- ATP Lyon R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-20T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:127157:208169:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Altmaier (`KXATPMATCH-26OCT18ALTDRO-ALT`) | 0.33 / 0.34 (100) | 33.5% | 36.1% | 33.4% | 34.8% [33.8%-37.6%] | -- | -- | -- | -- | PASS | +2.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Titouan Droguet (`KXATPMATCH-26OCT18ALTDRO-DRO`) | 0.65 / 0.66 (3) | 65.5% | 63.9% | 66.6% | 65.2% [62.4%-66.2%] | -- | -- | -- | -- | PASS | -1.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5348.0, B 5236.0; serve-point win A 61.2%, B 36.0%; Elo A 1805.7, B 1873.4; model uncertainty 0.0191
* Form inputs: days since last match A 9, B 27; matches on record A 705, B 393; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.010, surface_dev_tight +0.015
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18ALTDRO-18` Over 17.5 games: 0.65/0.98 mid 81.5%, model 91.7% (projection_v2.0 (prediction ledger)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18ALTDRO-23` Over 22.5 games: 0.49/0.53 mid 51.0%, model 58.3% (projection_v2.0 (prediction ledger)) -- gap +7.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18ALTDRO-DRO20` Will Titouan Droguet win the Daniel Altmaier vs Titouan Droguet match by a set score of 2-0?: 0.40/0.44 mid 42.0%, model 35.3% (projection_v2.0 (prediction ledger)) -- gap -6.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18ALTDRO-DRO4` Will Titouan Droguet win at least 3.5 more games than Daniel Altmaier?: 0.44/0.47 mid 45.5%, model 39.2% (projection_v2.0 (prediction ledger)) -- gap -6.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18ALTDRO-DRO21` Will Titouan Droguet win the Daniel Altmaier vs Titouan Droguet match by a set score of 2-1?: 0.21/0.26 mid 23.5%, model 28.6% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18ALTDRO-ALT21` Will Daniel Altmaier win the Daniel Altmaier vs Titouan Droguet match by a set score of 2-1?: 0.13/0.17 mid 15.0%, model 19.6% (projection_v2.0 (prediction ledger)) -- gap +4.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18ALTDRO-ALT2` Will Daniel Altmaier win at least 1.5 more games than Titouan Droguet?: 0.21/0.31 mid 26.0%, model 29.3% (projection_v2.0 (prediction ledger)) -- gap +3.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ALTDRO-2-DRO` Will Titouan Droguet win set 2 in the Daniel Altmaier vs Titouan Droguet match: 0.60/0.65 mid 62.5%, model 59.4% (projection_v2.0 (prediction ledger)) -- gap -3.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18ALTDRO-28` Over 27.5 games: 0.17/0.53 mid 35.0%, model 38.1% (projection_v2.0 (prediction ledger)) -- gap +3.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ALTDRO-1-ALT` Will Daniel Altmaier win set 1 in the Daniel Altmaier vs Titouan Droguet match: 0.36/0.40 mid 38.0%, model 40.6% (projection_v2.0 (prediction ledger)) -- gap +2.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ALTDRO-1-DRO` Will Titouan Droguet win set 1 in the Daniel Altmaier vs Titouan Droguet match: 0.60/0.64 mid 62.0%, model 59.4% (projection_v2.0 (prediction ledger)) -- gap -2.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ALTDRO-2-ALT` Will Daniel Altmaier win set 2 in the Daniel Altmaier vs Titouan Droguet match: 0.35/0.41 mid 38.0%, model 40.6% (projection_v2.0 (prediction ledger)) -- gap +2.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18ALTDRO-ALT20` Will Daniel Altmaier win the Daniel Altmaier vs Titouan Droguet match by a set score of 2-0?: 0.17/0.19 mid 18.0%, model 16.5% (projection_v2.0 (prediction ledger)) -- gap -1.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Benjamin Bonzi vs Cameron Norrie -- ATP Lyon R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-20T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111815:126127:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benjamin Bonzi (`KXATPMATCH-26OCT18BONNOR-BON`) | 0.44 / 0.45 (21) | 44.5% | 38.7% | 47.5% | 42.5% [39.6%-44.5%] | -- | -- | -- | -- | PASS | -5.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Cameron Norrie (`KXATPMATCH-26OCT18BONNOR-NOR`) | 0.53 / 0.55 (10829) | 54.0% | 61.3% | 52.5% | 57.5% [55.5%-60.4%] | -- | -- | -- | -- | PASS | +7.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4477.0, B 5008.0; serve-point win A 62.4%, B 35.3%; Elo A 1728.7, B 1884.8; model uncertainty 0.0245
* Form inputs: days since last match A 20, B 10; matches on record A 770, B 657; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight +0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18BONNOR-28` Over 27.5 games: 0.17/0.35 mid 26.0%, model 39.7% (projection_v2.0 (prediction ledger)) -- gap +13.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18BONNOR-18` Over 17.5 games: 0.66/0.98 mid 82.0%, model 93.0% (projection_v2.0 (prediction ledger)) -- gap +11.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18BONNOR-23` Over 22.5 games: 0.49/0.51 mid 50.0%, model 59.9% (projection_v2.0 (prediction ledger)) -- gap +9.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18BONNOR-BON20` Will Benjamin Bonzi win the Benjamin Bonzi vs Cameron Norrie match by a set score of 2-0?: 0.24/0.27 mid 25.5%, model 18.0% (projection_v2.0 (prediction ledger)) -- gap -7.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18BONNOR-BON2` Will Benjamin Bonzi win at least 1.5 more games than Cameron Norrie?: 0.34/0.43 mid 38.5%, model 31.7% (projection_v2.0 (prediction ledger)) -- gap -6.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18BONNOR-NOR21` Will Cameron Norrie win the Benjamin Bonzi vs Cameron Norrie match by a set score of 2-1?: 0.20/0.23 mid 21.5%, model 28.1% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BONNOR-1-NOR` Will Cameron Norrie win set 1 in the Benjamin Bonzi vs Cameron Norrie match: 0.51/0.56 mid 53.5%, model 57.6% (projection_v2.0 (prediction ledger)) -- gap +4.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BONNOR-2-BON` Will Benjamin Bonzi win set 2 in the Benjamin Bonzi vs Cameron Norrie match: 0.44/0.49 mid 46.5%, model 42.4% (projection_v2.0 (prediction ledger)) -- gap -4.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BONNOR-2-NOR` Will Cameron Norrie win set 2 in the Benjamin Bonzi vs Cameron Norrie match: 0.51/0.56 mid 53.5%, model 57.6% (projection_v2.0 (prediction ledger)) -- gap +4.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BONNOR-1-BON` Will Benjamin Bonzi win set 1 in the Benjamin Bonzi vs Cameron Norrie match: 0.44/0.48 mid 46.0%, model 42.4% (projection_v2.0 (prediction ledger)) -- gap -3.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT18BONNOR-NOR4` Will Cameron Norrie win at least 3.5 more games than Benjamin Bonzi?: 0.38/0.39 mid 38.5%, model 35.7% (projection_v2.0 (prediction ledger)) -- gap -2.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18BONNOR-BON21` Will Benjamin Bonzi win the Benjamin Bonzi vs Cameron Norrie match by a set score of 2-1?: 0.18/0.21 mid 19.5%, model 20.7% (projection_v2.0 (prediction ledger)) -- gap +1.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18BONNOR-NOR20` Will Cameron Norrie win the Benjamin Bonzi vs Cameron Norrie match by a set score of 2-0?: 0.31/0.34 mid 32.5%, model 33.2% (projection_v2.0 (prediction ledger)) -- gap +0.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ugo Humbert vs Corentin Moutet -- ATP Lyon R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-20T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144895:200005:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ugo Humbert (`KXATPMATCH-26OCT18HUMMOU-HUM`) | 0.70 / 0.72 (533) | 71.0% | 44.8% | 46.5% | 43.5% [40.0%-50.5%] | -- | -- | -- | -- | PASS | -26.2 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Corentin Moutet (`KXATPMATCH-26OCT18HUMMOU-MOU`) | 0.27 / 0.29 (6551) | 28.0% | 55.2% | 53.5% | 56.5% [49.5%-60.0%] | -- | -- | -- | -- | PASS | +27.2 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4602.0, B 4547.0; serve-point win A 61.8%, B 37.1%; Elo A 1731.6, B 1830.1; model uncertainty 0.0525
* Form inputs: days since last match A 9, B 47; matches on record A 613, B 584; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT18HUMMOU-MOU  (YES = Corentin Moutet)
Model: 55%
Kalshi: 28%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.040, surface_pool_high -0.035, surface_dev_loose -0.030, surface_dev_tight +0.040
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT18HUMMOU-HUM4` Will Ugo Humbert win at least 3.5 more games than Corentin Moutet?: 0.51/0.53 mid 52.0%, model 23.5% (projection_v2.0 (prediction ledger)) -- gap -28.5 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18HUMMOU-MOU2` Will Corentin Moutet win at least 1.5 more games than Ugo Humbert?: 0.17/0.25 mid 21.0%, model 48.0% (projection_v2.0 (prediction ledger)) -- gap +27.0 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18HUMMOU-HUM20` Will Ugo Humbert win the Ugo Humbert vs Corentin Moutet match by a set score of 2-0?: 0.47/0.49 mid 48.0%, model 21.7% (projection_v2.0 (prediction ledger)) -- gap -26.3 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18HUMMOU-1-HUM` Will Ugo Humbert win set 1 in the Ugo Humbert vs Corentin Moutet match: 0.65/0.68 mid 66.5%, model 46.5% (projection_v2.0 (prediction ledger)) -- gap -20.0 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18HUMMOU-1-MOU` Will Corentin Moutet win set 1 in the Ugo Humbert vs Corentin Moutet match: 0.32/0.36 mid 34.0%, model 53.5% (projection_v2.0 (prediction ledger)) -- gap +19.5 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18HUMMOU-2-HUM` Will Ugo Humbert win set 2 in the Ugo Humbert vs Corentin Moutet match: 0.63/0.69 mid 66.0%, model 46.5% (projection_v2.0 (prediction ledger)) -- gap -19.5 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18HUMMOU-2-MOU` Will Corentin Moutet win set 2 in the Ugo Humbert vs Corentin Moutet match: 0.31/0.37 mid 34.0%, model 53.5% (projection_v2.0 (prediction ledger)) -- gap +19.5 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18HUMMOU-MOU20` Will Corentin Moutet win the Ugo Humbert vs Corentin Moutet match by a set score of 2-0?: 0.10/0.15 mid 12.5%, model 28.6% (projection_v2.0 (prediction ledger)) -- gap +16.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18HUMMOU-HUM7` Will Ugo Humbert win at least 6.5 more games than Corentin Moutet?: 0.18/0.21 mid 19.5%, model 3.9% (projection_v2.0 (prediction ledger)) -- gap -15.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18HUMMOU-MOU21` Will Corentin Moutet win the Ugo Humbert vs Corentin Moutet match by a set score of 2-1?: 0.09/0.14 mid 11.5%, model 26.6% (projection_v2.0 (prediction ledger)) -- gap +15.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18HUMMOU-23` Over 22.5 games: 0.45/0.46 mid 45.5%, model 59.8% (projection_v2.0 (prediction ledger)) -- gap +14.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18HUMMOU-18` Over 17.5 games: 0.61/0.98 mid 79.5%, model 92.4% (projection_v2.0 (prediction ledger)) -- gap +12.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18HUMMOU-28` Over 27.5 games: 0.10/0.49 mid 29.5%, model 39.3% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18HUMMOU-HUM21` Will Ugo Humbert win the Ugo Humbert vs Corentin Moutet match by a set score of 2-1?: 0.20/0.24 mid 22.0%, model 23.2% (projection_v2.0 (prediction ledger)) -- gap +1.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hamad Medjedovic vs Brandon Nakashima -- ATP Lyon R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-20T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:206909:209098:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hamad Medjedovic (`KXATPMATCH-26OCT18MEDNAK-MED`) | 0.28 / 0.29 (100) | 28.5% | 45.7% | 39.9% | 46.1% [43.7%-49.5%] | -- | -- | -- | -- | PASS | +17.2 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Brandon Nakashima (`KXATPMATCH-26OCT18MEDNAK-NAK`) | 0.70 / 0.72 (25557) | 71.0% | 54.3% | 60.1% | 53.9% [50.5%-56.3%] | -- | -- | -- | -- | PASS | -16.7 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3408.0, B 5558.0; serve-point win A 65.8%, B 33.3%; Elo A 1922.3, B 1847.6; model uncertainty 0.0291
* Form inputs: days since last match A 10, B 7; matches on record A 284, B 456; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT18MEDNAK-MED  (YES = Hamad Medjedovic)
Model: 46%
Kalshi: 28%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.019, surface_dev_tight -0.019
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT18MEDNAK-NAK20` Will Brandon Nakashima win the Hamad Medjedovic vs Brandon Nakashima match by a set score of 2-0?: 0.45/0.49 mid 47.0%, model 28.0% (projection_v2.0 (prediction ledger)) -- gap -19.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18MEDNAK-NAK4` Will Brandon Nakashima win at least 3.5 more games than Hamad Medjedovic?: 0.44/0.46 mid 45.0%, model 27.0% (projection_v2.0 (prediction ledger)) -- gap -18.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18MEDNAK-MED2` Will Hamad Medjedovic win at least 1.5 more games than Brandon Nakashima?: 0.18/0.25 mid 21.5%, model 37.8% (projection_v2.0 (prediction ledger)) -- gap +16.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MEDNAK-2-MED` Will Hamad Medjedovic win set 2 in the Hamad Medjedovic vs Brandon Nakashima match: 0.31/0.36 mid 33.5%, model 47.1% (projection_v2.0 (prediction ledger)) -- gap +13.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MEDNAK-2-NAK` Will Brandon Nakashima win set 2 in the Hamad Medjedovic vs Brandon Nakashima match: 0.64/0.69 mid 66.5%, model 52.9% (projection_v2.0 (prediction ledger)) -- gap -13.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MEDNAK-1-MED` Will Hamad Medjedovic win set 1 in the Hamad Medjedovic vs Brandon Nakashima match: 0.32/0.36 mid 34.0%, model 47.1% (projection_v2.0 (prediction ledger)) -- gap +13.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18MEDNAK-18` Over 17.5 games: 0.68/0.98 mid 83.0%, model 95.6% (projection_v2.0 (prediction ledger)) -- gap +12.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18MEDNAK-23` Over 22.5 games: 0.51/0.53 mid 52.0%, model 64.2% (projection_v2.0 (prediction ledger)) -- gap +12.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MEDNAK-1-NAK` Will Brandon Nakashima win set 1 in the Hamad Medjedovic vs Brandon Nakashima match: 0.63/0.67 mid 65.0%, model 52.9% (projection_v2.0 (prediction ledger)) -- gap -12.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18MEDNAK-MED21` Will Hamad Medjedovic win the Hamad Medjedovic vs Brandon Nakashima match by a set score of 2-1?: 0.08/0.15 mid 11.5%, model 23.5% (projection_v2.0 (prediction ledger)) -- gap +12.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18MEDNAK-MED20` Will Hamad Medjedovic win the Hamad Medjedovic vs Brandon Nakashima match by a set score of 2-0?: 0.07/0.15 mid 11.0%, model 22.2% (projection_v2.0 (prediction ledger)) -- gap +11.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18MEDNAK-28` Over 27.5 games: 0.28/0.37 mid 32.5%, model 43.4% (projection_v2.0 (prediction ledger)) -- gap +10.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18MEDNAK-NAK21` Will Brandon Nakashima win the Hamad Medjedovic vs Brandon Nakashima match by a set score of 2-1?: 0.22/0.26 mid 24.0%, model 26.4% (projection_v2.0 (prediction ledger)) -- gap +2.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Joao Silva vs Alexander Ritschard -- ATP Challenger Lisbon Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106310:133197:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Ritschard (`KXATPCHALLENGERMATCH-26OCT18SILRIT-RIT`) | 0.99 / -- (0) | -- | 94.4% | 86.5% | 91.9% [90.7%-93.1%] | -- | -- | -- | -- | PASS | -- | UNPRICED | FRESH | D / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Joao Silva (`KXATPCHALLENGERMATCH-26OCT18SILRIT-SIL`) | -- / 0.01 (86515) | -- | 5.6% | 13.5% | 8.1% [6.9%-9.3%] | -- | -- | -- | -- | PASS | -- | UNPRICED | FRESH | D / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 103.0, B 1877.0; serve-point win A 54.5%, B 33.0%; Elo A 1308.3, B 1736.4; model uncertainty 0.012
* Form inputs: days since last match A 92, B 41; matches on record A 4, B 519; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.012, surface_dev_loose -0.002, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; MODEL_ROW_STALE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE

## Stan Wawrinka vs Martin Landaluce -- ATP Lyon R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-20T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:104527:212021:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martin Landaluce (`KXATPMATCH-26OCT18WAWLAN-LAN`) | 0.60 / 0.62 (32922) | 61.0% | 60.9% | 60.4% | 53.5% [36.5%-56.5%] | -- | -- | -- | -- | PASS | -0.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stan Wawrinka (`KXATPMATCH-26OCT18WAWLAN-WAW`) | 0.38 / 0.39 (220) | 38.5% | 39.1% | 39.6% | 46.5% [43.5%-63.5%] | -- | -- | -- | -- | PASS | +0.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3775.0, B 3597.0; serve-point win A 62.7%, B 35.1%; Elo A 1798.5, B 1699.1; model uncertainty 0.0998
* Form inputs: days since last match A 30, B 699; matches on record A 1173, B 115; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.020, surface_dev_tight +0.025
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT18WAWLAN-LAN6` Will Martin Landaluce win at least 5.5 more games than Stan Wawrinka?: 0.10/0.37 mid 23.5%, model 12.7% (projection_v2.0 (prediction ledger)) -- gap -10.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data POOR
  * `KXATPGTOTAL-26OCT18WAWLAN-18` Over 17.5 games: 0.70/0.98 mid 84.0%, model 93.2% (projection_v2.0 (prediction ledger)) -- gap +9.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPGTOTAL-26OCT18WAWLAN-23` Over 22.5 games: 0.51/0.52 mid 51.5%, model 60.2% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPGTOTAL-26OCT18WAWLAN-28` Over 27.5 games: 0.28/0.37 mid 32.5%, model 40.0% (projection_v2.0 (prediction ledger)) -- gap +7.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPEXACTMATCH-26OCT18WAWLAN-LAN21` Will Martin Landaluce win the Stan Wawrinka vs Martin Landaluce match by a set score of 2-1?: 0.20/0.24 mid 22.0%, model 28.0% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPEXACTMATCH-26OCT18WAWLAN-WAW21` Will Stan Wawrinka win the Stan Wawrinka vs Martin Landaluce match by a set score of 2-1?: 0.12/0.19 mid 15.5%, model 20.9% (projection_v2.0 (prediction ledger)) -- gap +5.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPEXACTMATCH-26OCT18WAWLAN-LAN20` Will Martin Landaluce win the Stan Wawrinka vs Martin Landaluce match by a set score of 2-0?: 0.33/0.39 mid 36.0%, model 32.8% (projection_v2.0 (prediction ledger)) -- gap -3.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPGSPREAD-26OCT18WAWLAN-WAW2` Will Stan Wawrinka win at least 1.5 more games than Martin Landaluce?: 0.31/0.36 mid 33.5%, model 32.0% (projection_v2.0 (prediction ledger)) -- gap -1.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPEXACTMATCH-26OCT18WAWLAN-WAW20` Will Stan Wawrinka win the Stan Wawrinka vs Martin Landaluce match by a set score of 2-0?: 0.16/0.22 mid 19.0%, model 18.2% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPSETWINNER-26OCT18WAWLAN-1-LAN` Will Martin Landaluce win set 1 in the Stan Wawrinka vs Martin Landaluce match: 0.56/0.60 mid 58.0%, model 57.3% (projection_v2.0 (prediction ledger)) -- gap -0.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT18WAWLAN-1-WAW` Will Stan Wawrinka win set 1 in the Stan Wawrinka vs Martin Landaluce match: 0.40/0.44 mid 42.0%, model 42.7% (projection_v2.0 (prediction ledger)) -- gap +0.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT18WAWLAN-2-WAW` Will Stan Wawrinka win set 2 in the Stan Wawrinka vs Martin Landaluce match: 0.39/0.45 mid 42.0%, model 42.7% (projection_v2.0 (prediction ledger)) -- gap +0.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPGSPREAD-26OCT18WAWLAN-LAN3` Will Martin Landaluce win at least 2.5 more games than Stan Wawrinka?: 0.46/0.47 mid 46.5%, model 45.9% (projection_v2.0 (prediction ledger)) -- gap -0.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPSETWINNER-26OCT18WAWLAN-2-LAN` Will Martin Landaluce win set 2 in the Stan Wawrinka vs Martin Landaluce match: 0.54/0.61 mid 57.5%, model 57.3% (projection_v2.0 (prediction ledger)) -- gap -0.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data POOR
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Guido Andreozzi / Manuel Guinard vs Michael Geerts / Joran Vliegen -- ATP Brussels R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-18 14:42Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18ANDGUIGEEVLI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guido Andreozzi / Manuel Guinard (`KXATPDOUBLES-26OCT18ANDGUIGEEVLI-ANDGUI`) | 0.26 / 0.77 (1) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Michael Geerts / Joran Vliegen (`KXATPDOUBLES-26OCT18ANDGUIGEEVLI-GEEVLI`) | 0.11 / 0.89 (1) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sander Arends / Luke Johnson vs Orlando Luz / Rafael Matos -- ATP Brussels R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-18 14:42Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18AREJOHLUZMAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sander Arends / Luke Johnson (`KXATPDOUBLES-26OCT18AREJOHLUZMAT-AREJOH`) | 0.11 / 0.71 (1) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Orlando Luz / Rafael Matos (`KXATPDOUBLES-26OCT18AREJOHLUZMAT-LUZMAT`) | 0.26 / 0.85 (1) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nicolas Barrientos / David Pel vs Marcelo Melo / John-Patrick Smith -- ATP Brussels R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-18 14:42Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18BARPELMELSMI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Barrientos / David Pel (`KXATPDOUBLES-26OCT18BARPELMELSMI-BARPEL`) | 0.11 / 0.90 (12) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marcelo Melo / John-Patrick Smith (`KXATPDOUBLES-26OCT18BARPELMELSMI-MELSMI`) | 0.11 / 0.90 (12) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jacob Fearnley vs Hugo Gaston -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-18 14:42Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200384:207985:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jacob Fearnley (`KXATPMATCH-26OCT18FEAGAS-FEA`) | 0.60 / 0.62 (26121) | 61.0% | 58.6% | 55.6% | 55.6% [53.6%-57.2%] | -- | -- | -- | -- | PASS | -2.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hugo Gaston (`KXATPMATCH-26OCT18FEAGAS-GAS`) | 0.37 / 0.38 (22) | 37.5% | 41.4% | 44.4% | 44.4% [42.8%-46.4%] | -- | -- | -- | -- | SHADOW_BET | +3.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4058.0, B 4582.0; serve-point win A 61.0%, B 40.6%; Elo A 1773.0, B 1728.8; model uncertainty 0.0179
* Form inputs: days since last match A 20, B 13; matches on record A 178, B 502; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose -0.005, surface_dev_tight +0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18FEAGAS-28` Over 27.5 games: 0.17/0.29 mid 23.0%, model 36.9% (projection_v2.0 (prediction ledger)) -- gap +13.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18FEAGAS-23` Over 22.5 games: 0.46/0.47 mid 46.5%, model 57.7% (projection_v2.0 (prediction ledger)) -- gap +11.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18FEAGAS-18` Over 17.5 games: 0.64/0.95 mid 79.5%, model 90.3% (projection_v2.0 (prediction ledger)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18FEAGAS-FEA21` Will Jacob Fearnley win the Jacob Fearnley vs Hugo Gaston match by a set score of 2-1?: 0.17/0.24 mid 20.5%, model 27.5% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18FEAGAS-GAS21` Will Hugo Gaston win the Jacob Fearnley vs Hugo Gaston match by a set score of 2-1?: 0.12/0.19 mid 15.5%, model 21.8% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18FEAGAS-FEA20` Will Jacob Fearnley win the Jacob Fearnley vs Hugo Gaston match by a set score of 2-0?: 0.33/0.39 mid 36.0%, model 31.1% (projection_v2.0 (prediction ledger)) -- gap -4.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18FEAGAS-FEA4` Will Jacob Fearnley win at least 3.5 more games than Hugo Gaston?: 0.40/0.42 mid 41.0%, model 36.2% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18FEAGAS-2-FEA` Will Jacob Fearnley win set 2 in the Jacob Fearnley vs Hugo Gaston match: 0.56/0.61 mid 58.5%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap -2.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18FEAGAS-2-GAS` Will Hugo Gaston win set 2 in the Jacob Fearnley vs Hugo Gaston match: 0.39/0.44 mid 41.5%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap +2.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18FEAGAS-1-GAS` Will Hugo Gaston win set 1 in the Jacob Fearnley vs Hugo Gaston match: 0.39/0.45 mid 42.0%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18FEAGAS-1-FEA` Will Jacob Fearnley win set 1 in the Jacob Fearnley vs Hugo Gaston match: 0.55/0.59 mid 57.0%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap -1.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18FEAGAS-GAS20` Will Hugo Gaston win the Jacob Fearnley vs Hugo Gaston match by a set score of 2-0?: 0.15/0.23 mid 19.0%, model 19.6% (projection_v2.0 (prediction ledger)) -- gap +0.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18FEAGAS-GAS2` Will Hugo Gaston win at least 1.5 more games than Jacob Fearnley?: 0.33/0.36 mid 34.5%, model 34.7% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tallon Griekspoor vs Max Schoenhaus -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-18 14:42Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:134868:212268:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tallon Griekspoor (`KXATPMATCH-26OCT18GRISCH-GRI`) | 0.76 / 0.77 (1019) | 76.5% | 80.0% | 72.1% | 83.3% [77.7%-89.4%] | -- | -- | -- | -- | WATCH | +3.5 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Max Schoenhaus (`KXATPMATCH-26OCT18GRISCH-SCH`) | 0.23 / 0.24 (6030) | 23.5% | 20.0% | 27.9% | 16.7% [10.6%-22.3%] | -- | -- | -- | -- | PASS | -3.5 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4445.0, B 1578.0; serve-point win A 71.4%, B 35.6%; Elo A 1871.5, B 1465.9; model uncertainty 0.0584
* Form inputs: days since last match A 10, B 34; matches on record A 677, B 52; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.023, surface_pool_high -0.028, surface_dev_loose +0.002, surface_dev_tight -0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18GRISCH-18` Over 17.5 games: 0.69/0.95 mid 82.0%, model 93.6% (projection_v2.0 (prediction ledger)) -- gap +11.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18GRISCH-GRI7` Will Tallon Griekspoor win at least 6.5 more games than Max Schoenhaus?: 0.02/0.32 mid 17.0%, model 7.6% (projection_v2.0 (prediction ledger)) -- gap -9.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18GRISCH-23` Over 22.5 games: 0.49/0.51 mid 50.0%, model 56.6% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18GRISCH-28` Over 27.5 games: 0.26/0.35 mid 30.5%, model 36.2% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18GRISCH-GRI21` Will Tallon Griekspoor win the Tallon Griekspoor vs Max Schoenhaus match by a set score of 2-1?: 0.22/0.26 mid 24.0%, model 29.2% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18GRISCH-GRI4` Will Tallon Griekspoor win at least 3.5 more games than Max Schoenhaus?: 0.51/0.52 mid 51.5%, model 48.6% (projection_v2.0 (prediction ledger)) -- gap -2.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18GRISCH-SCH20` Will Max Schoenhaus win the Tallon Griekspoor vs Max Schoenhaus match by a set score of 2-0?: 0.08/0.13 mid 10.5%, model 8.2% (projection_v2.0 (prediction ledger)) -- gap -2.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18GRISCH-GRI20` Will Tallon Griekspoor win the Tallon Griekspoor vs Max Schoenhaus match by a set score of 2-0?: 0.51/0.54 mid 52.5%, model 50.8% (projection_v2.0 (prediction ledger)) -- gap -1.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18GRISCH-SCH21` Will Max Schoenhaus win the Tallon Griekspoor vs Max Schoenhaus match by a set score of 2-1?: 0.08/0.13 mid 10.5%, model 11.8% (projection_v2.0 (prediction ledger)) -- gap +1.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18GRISCH-2-SCH` Will Max Schoenhaus win set 2 in the Tallon Griekspoor vs Max Schoenhaus match: 0.26/0.33 mid 29.5%, model 28.7% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT18GRISCH-SCH2` Will Max Schoenhaus win at least 1.5 more games than Tallon Griekspoor?: 0.08/0.20 mid 14.0%, model 14.5% (projection_v2.0 (prediction ledger)) -- gap +0.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18GRISCH-2-GRI` Will Tallon Griekspoor win set 2 in the Tallon Griekspoor vs Max Schoenhaus match: 0.68/0.74 mid 71.0%, model 71.3% (projection_v2.0 (prediction ledger)) -- gap +0.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18GRISCH-1-GRI` Will Tallon Griekspoor win set 1 in the Tallon Griekspoor vs Max Schoenhaus match: 0.69/0.74 mid 71.5%, model 71.3% (projection_v2.0 (prediction ledger)) -- gap -0.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18GRISCH-1-SCH` Will Max Schoenhaus win set 1 in the Tallon Griekspoor vs Max Schoenhaus match: 0.26/0.31 mid 28.5%, model 28.7% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mariano Navone vs Juan Manuel Cerundolo -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-18 14:42Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207678:208363:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Manuel Cerundolo (`KXATPMATCH-26OCT18NAVCER-CER`) | 0.39 / 0.40 (7950) | 39.5% | 46.6% | 36.5% | 40.4% [38.9%-42.9%] | -- | -- | -- | -- | PASS | +7.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mariano Navone (`KXATPMATCH-26OCT18NAVCER-NAV`) | 0.60 / 0.61 (2643) | 60.5% | 53.4% | 63.5% | 59.6% [57.1%-61.1%] | -- | -- | -- | -- | PASS | -7.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5176.0, B 5332.0; serve-point win A 61.9%, B 38.8%; Elo A 1725.4, B 1754.7; model uncertainty 0.0199
* Form inputs: days since last match A 10, B 8; matches on record A 410, B 506; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.015, surface_dev_loose -0.001, surface_dev_tight -0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18NAVCER-18` Over 17.5 games: 0.65/0.95 mid 80.0%, model 91.8% (projection_v2.0 (prediction ledger)) -- gap +11.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18NAVCER-NAV6` Will Mariano Navone win at least 5.5 more games than Juan Manuel Cerundolo?: 0.05/0.42 mid 23.5%, model 11.8% (projection_v2.0 (prediction ledger)) -- gap -11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18NAVCER-23` Over 22.5 games: 0.49/0.50 mid 49.5%, model 59.3% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18NAVCER-NAV3` Will Mariano Navone win at least 2.5 more games than Juan Manuel Cerundolo?: 0.48/0.50 mid 49.0%, model 39.7% (projection_v2.0 (prediction ledger)) -- gap -9.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18NAVCER-NAV20` Will Mariano Navone win the Mariano Navone vs Juan Manuel Cerundolo match by a set score of 2-0?: 0.34/0.39 mid 36.5%, model 27.4% (projection_v2.0 (prediction ledger)) -- gap -9.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18NAVCER-CER21` Will Juan Manuel Cerundolo win the Mariano Navone vs Juan Manuel Cerundolo match by a set score of 2-1?: 0.13/0.19 mid 16.0%, model 23.8% (projection_v2.0 (prediction ledger)) -- gap +7.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18NAVCER-CER2` Will Juan Manuel Cerundolo win at least 1.5 more games than Mariano Navone?: 0.29/0.35 mid 32.0%, model 39.5% (projection_v2.0 (prediction ledger)) -- gap +7.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18NAVCER-1-CER` Will Juan Manuel Cerundolo win set 1 in the Mariano Navone vs Juan Manuel Cerundolo match: 0.40/0.44 mid 42.0%, model 47.7% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18NAVCER-2-CER` Will Juan Manuel Cerundolo win set 2 in the Mariano Navone vs Juan Manuel Cerundolo match: 0.39/0.45 mid 42.0%, model 47.7% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18NAVCER-1-NAV` Will Mariano Navone win set 1 in the Mariano Navone vs Juan Manuel Cerundolo match: 0.56/0.59 mid 57.5%, model 52.3% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18NAVCER-2-NAV` Will Mariano Navone win set 2 in the Mariano Navone vs Juan Manuel Cerundolo match: 0.54/0.61 mid 57.5%, model 52.3% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18NAVCER-28` Over 27.5 games: 0.17/0.52 mid 34.5%, model 38.7% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18NAVCER-NAV21` Will Mariano Navone win the Mariano Navone vs Juan Manuel Cerundolo match by a set score of 2-1?: 0.20/0.24 mid 22.0%, model 26.1% (projection_v2.0 (prediction ledger)) -- gap +4.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18NAVCER-CER20` Will Juan Manuel Cerundolo win the Mariano Navone vs Juan Manuel Cerundolo match by a set score of 2-0?: 0.16/0.22 mid 19.0%, model 22.8% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dino Prizmic vs Damir Dzumhur -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-18 14:42Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:106000:209976:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Damir Dzumhur (`KXATPMATCH-26OCT18PRIDZU-DZU`) | 0.30 / 0.32 (29622) | 31.0% | 23.2% | 30.3% | 29.4% [28.5%-31.2%] | -- | -- | -- | -- | PASS | -7.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dino Prizmic (`KXATPMATCH-26OCT18PRIDZU-PRI`) | 0.68 / 0.69 (379) | 68.5% | 76.8% | 69.7% | 70.6% [68.8%-71.5%] | -- | -- | -- | -- | PASS | +8.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3904.0, B 4752.0; serve-point win A 63.0%, B 42.6%; Elo A 1827.6, B 1664.3; model uncertainty 0.0138
* Form inputs: days since last match A 27, B 13; matches on record A 223, B 1058; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight -0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18PRIDZU-18` Over 17.5 games: 0.59/0.88 mid 73.5%, model 86.0% (projection_v2.0 (prediction ledger)) -- gap +12.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18PRIDZU-PRI21` Will Dino Prizmic win the Dino Prizmic vs Damir Dzumhur match by a set score of 2-1?: 0.20/0.24 mid 22.0%, model 29.5% (projection_v2.0 (prediction ledger)) -- gap +7.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18PRIDZU-23` Over 22.5 games: 0.43/0.44 mid 43.5%, model 50.5% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18PRIDZU-DZU2` Will Damir Dzumhur win at least 1.5 more games than Dino Prizmic?: 0.19/0.27 mid 23.0%, model 18.0% (projection_v2.0 (prediction ledger)) -- gap -5.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18PRIDZU-PRI7` Will Dino Prizmic win at least 6.5 more games than Damir Dzumhur?: 0.19/0.22 mid 20.5%, model 16.2% (projection_v2.0 (prediction ledger)) -- gap -4.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18PRIDZU-DZU20` Will Damir Dzumhur win the Dino Prizmic vs Damir Dzumhur match by a set score of 2-0?: 0.11/0.17 mid 14.0%, model 9.8% (projection_v2.0 (prediction ledger)) -- gap -4.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18PRIDZU-PRI20` Will Dino Prizmic win the Dino Prizmic vs Damir Dzumhur match by a set score of 2-0?: 0.40/0.48 mid 44.0%, model 47.3% (projection_v2.0 (prediction ledger)) -- gap +3.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18PRIDZU-1-PRI` Will Dino Prizmic win set 1 in the Dino Prizmic vs Damir Dzumhur match: 0.63/0.68 mid 65.5%, model 68.8% (projection_v2.0 (prediction ledger)) -- gap +3.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18PRIDZU-1-DZU` Will Damir Dzumhur win set 1 in the Dino Prizmic vs Damir Dzumhur match: 0.32/0.36 mid 34.0%, model 31.2% (projection_v2.0 (prediction ledger)) -- gap -2.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18PRIDZU-2-DZU` Will Damir Dzumhur win set 2 in the Dino Prizmic vs Damir Dzumhur match: 0.32/0.36 mid 34.0%, model 31.2% (projection_v2.0 (prediction ledger)) -- gap -2.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18PRIDZU-2-PRI` Will Dino Prizmic win set 2 in the Dino Prizmic vs Damir Dzumhur match: 0.64/0.68 mid 66.0%, model 68.8% (projection_v2.0 (prediction ledger)) -- gap +2.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT18PRIDZU-PRI4` Will Dino Prizmic win at least 3.5 more games than Damir Dzumhur?: 0.52/0.53 mid 52.5%, model 55.1% (projection_v2.0 (prediction ledger)) -- gap +2.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18PRIDZU-28` Over 27.5 games: 0.18/0.48 mid 33.0%, model 31.1% (projection_v2.0 (prediction ledger)) -- gap -1.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18PRIDZU-DZU21` Will Damir Dzumhur win the Dino Prizmic vs Damir Dzumhur match by a set score of 2-1?: 0.09/0.16 mid 12.5%, model 13.4% (projection_v2.0 (prediction ledger)) -- gap +0.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Toby Samuel vs Zizou Bergs -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-18 14:42Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200267:210389:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zizou Bergs (`KXATPMATCH-26OCT18SAMBER-BER`) | 0.68 / 0.69 (20114) | 68.5% | 46.0% | 28.0% | 36.1% [30.6%-44.0%] | -- | -- | -- | -- | PASS | -22.5 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Toby Samuel (`KXATPMATCH-26OCT18SAMBER-SAM`) | 0.31 / 0.33 (31403) | 32.0% | 54.0% | 72.0% | 63.8% [56.0%-69.4%] | -- | -- | -- | -- | WATCH | +22.0 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2684.0, B 5362.0; serve-point win A 62.9%, B 37.9%; Elo A 1804.6, B 1810.8; model uncertainty 0.0666
* Form inputs: days since last match A 20, B 4; matches on record A 136, B 552; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT18SAMBER-SAM  (YES = Toby Samuel)
Model: 54%
Kalshi: 32%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, SCHEDULED_START_PASSED, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.019, surface_dev_loose +0.042, surface_dev_tight -0.029
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT18SAMBER-BER2` Will Zizou Bergs win at least 1.5 more games than Toby Samuel?: 0.61/0.63 mid 62.0%, model 38.8% (projection_v2.0 (prediction ledger)) -- gap -23.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18SAMBER-SAM2` Will Toby Samuel win at least 1.5 more games than Zizou Bergs?: 0.24/0.28 mid 26.0%, model 46.7% (projection_v2.0 (prediction ledger)) -- gap +20.7 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18SAMBER-BER20` Will Zizou Bergs win the Toby Samuel vs Zizou Bergs match by a set score of 2-0?: 0.37/0.44 mid 40.5%, model 22.4% (projection_v2.0 (prediction ledger)) -- gap -18.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SAMBER-1-SAM` Will Toby Samuel win set 1 in the Toby Samuel vs Zizou Bergs match: 0.33/0.39 mid 36.0%, model 52.6% (projection_v2.0 (prediction ledger)) -- gap +16.6 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SAMBER-1-BER` Will Zizou Bergs win set 1 in the Toby Samuel vs Zizou Bergs match: 0.61/0.65 mid 63.0%, model 47.3% (projection_v2.0 (prediction ledger)) -- gap -15.7 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SAMBER-2-SAM` Will Toby Samuel win set 2 in the Toby Samuel vs Zizou Bergs match: 0.35/0.41 mid 38.0%, model 52.6% (projection_v2.0 (prediction ledger)) -- gap +14.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT18SAMBER-BER5` Will Zizou Bergs win at least 4.5 more games than Toby Samuel?: 0.26/0.33 mid 29.5%, model 15.4% (projection_v2.0 (prediction ledger)) -- gap -14.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18SAMBER-SAM20` Will Toby Samuel win the Toby Samuel vs Zizou Bergs match by a set score of 2-0?: 0.10/0.18 mid 14.0%, model 27.7% (projection_v2.0 (prediction ledger)) -- gap +13.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18SAMBER-SAM21` Will Toby Samuel win the Toby Samuel vs Zizou Bergs match by a set score of 2-1?: 0.10/0.17 mid 13.5%, model 26.2% (projection_v2.0 (prediction ledger)) -- gap +12.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SAMBER-2-BER` Will Zizou Bergs win set 2 in the Toby Samuel vs Zizou Bergs match: 0.55/0.64 mid 59.5%, model 47.3% (projection_v2.0 (prediction ledger)) -- gap -12.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18SAMBER-26` Over 25.5 games: 0.36/0.41 mid 38.5%, model 48.7% (projection_v2.0 (prediction ledger)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18SAMBER-21` Over 20.5 games: 0.60/0.68 mid 64.0%, model 72.8% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18SAMBER-31` Over 30.5 games: 0.15/0.41 mid 28.0%, model 24.2% (projection_v2.0 (prediction ledger)) -- gap -3.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18SAMBER-BER21` Will Zizou Bergs win the Toby Samuel vs Zizou Bergs match by a set score of 2-1?: 0.21/0.26 mid 23.5%, model 23.6% (projection_v2.0 (prediction ledger)) -- gap +0.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jan-Lennard Struff vs Marcos Giron -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-18 14:42Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105526:106218:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcos Giron (`KXATPMATCH-26OCT18STRGIR-GIR`) | 0.40 / 0.41 (10269) | 40.5% | 52.3% | 49.0% | 49.5% [44.2%-53.4%] | -- | -- | -- | -- | SHADOW_BET | +11.8 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jan-Lennard Struff (`KXATPMATCH-26OCT18STRGIR-STR`) | 0.59 / 0.60 (598) | 59.5% | 47.6% | 51.0% | 50.5% [46.6%-55.8%] | -- | -- | -- | -- | PASS | -11.8 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4788.0, B 4538.0; serve-point win A 66.0%, B 33.5%; Elo A 1780.4, B 1807.1; model uncertainty 0.0462
* Form inputs: days since last match A 8, B 10; matches on record A 1054, B 707; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.029, surface_pool_high -0.039, surface_dev_loose -0.010, surface_dev_tight +0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT18STRGIR-STR6` Will Jan-Lennard Struff win at least 5.5 more games than Marcos Giron?: 0.05/0.34 mid 19.5%, model 5.9% (projection_v2.0 (prediction ledger)) -- gap -13.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18STRGIR-STR20` Will Jan-Lennard Struff win the Jan-Lennard Struff vs Marcos Giron match by a set score of 2-0?: 0.35/0.38 mid 36.5%, model 23.5% (projection_v2.0 (prediction ledger)) -- gap -13.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18STRGIR-STR3` Will Jan-Lennard Struff win at least 2.5 more games than Marcos Giron?: 0.44/0.46 mid 45.0%, model 32.0% (projection_v2.0 (prediction ledger)) -- gap -13.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18STRGIR-19` Over 18.5 games: 0.66/0.95 mid 80.5%, model 91.5% (projection_v2.0 (prediction ledger)) -- gap +11.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18STRGIR-GIR2` Will Marcos Giron win at least 1.5 more games than Jan-Lennard Struff?: 0.31/0.36 mid 33.5%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18STRGIR-2-GIR` Will Marcos Giron win set 2 in the Jan-Lennard Struff vs Marcos Giron match: 0.40/0.44 mid 42.0%, model 51.6% (projection_v2.0 (prediction ledger)) -- gap +9.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18STRGIR-2-STR` Will Jan-Lennard Struff win set 2 in the Jan-Lennard Struff vs Marcos Giron match: 0.56/0.60 mid 58.0%, model 48.4% (projection_v2.0 (prediction ledger)) -- gap -9.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18STRGIR-1-GIR` Will Marcos Giron win set 1 in the Jan-Lennard Struff vs Marcos Giron match: 0.40/0.45 mid 42.5%, model 51.6% (projection_v2.0 (prediction ledger)) -- gap +9.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18STRGIR-24` Over 23.5 games: 0.47/0.48 mid 47.5%, model 56.5% (projection_v2.0 (prediction ledger)) -- gap +9.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18STRGIR-GIR21` Will Marcos Giron win the Jan-Lennard Struff vs Marcos Giron match by a set score of 2-1?: 0.15/0.19 mid 17.0%, model 25.8% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18STRGIR-1-STR` Will Jan-Lennard Struff win set 1 in the Jan-Lennard Struff vs Marcos Giron match: 0.55/0.59 mid 57.0%, model 48.4% (projection_v2.0 (prediction ledger)) -- gap -8.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18STRGIR-29` Over 28.5 games: 0.27/0.38 mid 32.5%, model 39.5% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18STRGIR-GIR20` Will Marcos Giron win the Jan-Lennard Struff vs Marcos Giron match by a set score of 2-0?: 0.17/0.23 mid 20.0%, model 26.6% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18STRGIR-STR21` Will Jan-Lennard Struff win the Jan-Lennard Struff vs Marcos Giron match by a set score of 2-1?: 0.21/0.25 mid 23.0%, model 24.2% (projection_v2.0 (prediction ledger)) -- gap +1.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sara Bejlek vs Xiyu Wang -- WTA Ningbo R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-19 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-20T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-10-19T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:216016:239383:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Bejlek (`KXWTAMATCH-26OCT19BEJWAN-BEJ`) | 0.50 / 0.51 (9962) | 50.5% | 41.8% | 34.4% | 38.9% [36.9%-43.6%] | -- | -- | -- | -- | PASS | -8.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xiyu Wang (`KXWTAMATCH-26OCT19BEJWAN-WAN`) | 0.49 / 0.50 (8413) | 49.5% | 58.2% | 65.6% | 61.1% [56.4%-63.1%] | -- | -- | -- | -- | SHADOW_BET | +8.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3433.0, B 3839.0; serve-point win A 52.4%, B 46.0%; Elo A 1879.6, B 1889.0; model uncertainty 0.0337
* Form inputs: days since last match A 7, B 6; matches on record A 270, B 431; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high -0.000, surface_dev_loose -0.015, surface_dev_tight +0.021
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT19BEJWAN-22` Over 21.5 games: 0.48/0.49 mid 48.5%, model 61.2% (projection_v2.0 (prediction ledger)) -- gap +12.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT19BEJWAN-27` Over 26.5 games: 0.23/0.35 mid 29.0%, model 37.9% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT19BEJWAN-2-BEJ` Will Sara Bejlek win set 2 in the Sara Bejlek vs Xiyu Wang match: 0.32/0.71 mid 51.5%, model 44.5% (projection_v2.0 (prediction ledger)) -- gap -7.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT19BEJWAN-2-WAN` Will Xiyu Wang win set 2 in the Sara Bejlek vs Xiyu Wang match: 0.29/0.68 mid 48.5%, model 55.5% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT19BEJWAN-1-WAN` Will Xiyu Wang win set 1 in the Sara Bejlek vs Xiyu Wang match: 0.48/0.52 mid 50.0%, model 55.5% (projection_v2.0 (prediction ledger)) -- gap +5.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT19BEJWAN-1-BEJ` Will Sara Bejlek win set 1 in the Sara Bejlek vs Xiyu Wang match: 0.47/0.52 mid 49.5%, model 44.5% (projection_v2.0 (prediction ledger)) -- gap -5.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT19BEJWAN-17` Over 16.5 games: 0.81/0.94 mid 87.5%, model 92.4% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Cristina Bucsa / Nicole Melichar-Martinez vs Sara Errani / Jasmine Paolini -- WTA Ningbo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-20T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-19T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19BUCMELERRPAO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cristina Bucsa / Nicole Melichar-Martinez (`KXWTADOUBLES-26OCT19BUCMELERRPAO-BUCMEL`) | 0.32 / 0.54 (5) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sara Errani / Jasmine Paolini (`KXWTADOUBLES-26OCT19BUCMELERRPAO-ERRPAO`) | 0.46 / 0.66 (11) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ulrikke Eikeri / Quinn Gleason vs Su-Wei Hsieh / Jelena Ostapenko -- WTA Ningbo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-20T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-19T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19EIKGLEHSIOST:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ulrikke Eikeri / Quinn Gleason (`KXWTADOUBLES-26OCT19EIKGLEHSIOST-EIKGLE`) | 0.18 / 0.56 (11) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Su-Wei Hsieh / Jelena Ostapenko (`KXWTADOUBLES-26OCT19EIKGLEHSIOST-HSIOST`) | 0.37 / 0.72 (155) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Leylah Fernandez / Marta Kostyuk vs Anna Bondar / Alina Korneeva -- WTA Ningbo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-20T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-19T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19FERKOSBONKOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Bondar / Alina Korneeva (`KXWTADOUBLES-26OCT19FERKOSBONKOR-BONKOR`) | 0.36 / 0.40 (42) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leylah Fernandez / Marta Kostyuk (`KXWTADOUBLES-26OCT19FERKOSBONKOR-FERKOS`) | 0.23 / 0.63 (6) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hanyu Guo vs Ekaterina Alexandrova -- WTA Ningbo R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-19 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-20T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-10-19T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:206420:215250:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Alexandrova (`KXWTAMATCH-26OCT19GUOALE-ALE`) | 0.77 / 0.78 (6353) | 77.5% | 68.5% | 59.4% | 64.9% [58.9%-78.2%] | -- | -- | -- | -- | PASS | -9.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hanyu Guo (`KXWTAMATCH-26OCT19GUOALE-GUO`) | 0.21 / 0.23 (13986) | 22.0% | 31.5% | 40.6% | 35.1% [21.8%-41.1%] | -- | -- | -- | -- | WATCH | +9.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3015.0, B 4877.0; serve-point win A 55.1%, B 41.3%; Elo A 1759.8, B 1937.6; model uncertainty 0.0967
* Form inputs: days since last match A 4, B 7; matches on record A 329, B 745; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.048, surface_pool_high +0.060, surface_dev_loose +0.015, surface_dev_tight -0.015
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 6 carry a model probability
  * `KXWTAGTOTAL-26OCT19GUOALE-19` Over 18.5 games: 0.62/0.63 mid 62.5%, model 79.0% (projection_v2.0 (prediction ledger)) -- gap +16.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT19GUOALE-24` Over 23.5 games: 0.27/0.41 mid 34.0%, model 48.6% (projection_v2.0 (prediction ledger)) -- gap +14.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT19GUOALE-2-ALE` Will Ekaterina Alexandrova win set 2 in the Hanyu Guo vs Ekaterina Alexandrova match: 0.71/0.75 mid 73.0%, model 62.6% (projection_v2.0 (prediction ledger)) -- gap -10.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT19GUOALE-2-GUO` Will Hanyu Guo win set 2 in the Hanyu Guo vs Ekaterina Alexandrova match: 0.25/0.29 mid 27.0%, model 37.4% (projection_v2.0 (prediction ledger)) -- gap +10.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT19GUOALE-1-GUO` Will Hanyu Guo win set 1 in the Hanyu Guo vs Ekaterina Alexandrova match: 0.25/0.30 mid 27.5%, model 37.4% (projection_v2.0 (prediction ledger)) -- gap +9.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT19GUOALE-1-ALE` Will Ekaterina Alexandrova win set 1 in the Hanyu Guo vs Ekaterina Alexandrova match: 0.70/0.74 mid 72.0%, model 62.6% (projection_v2.0 (prediction ledger)) -- gap -9.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Desirae Krawczyk / Fanny Stollar vs Anna Danilina / Xinyu Jiang -- WTA Ningbo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-20T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-19T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19KRASTODANJIA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Danilina / Xinyu Jiang (`KXWTADOUBLES-26OCT19KRASTODANJIA-DANJIA`) | 0.57 / 0.66 (30) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Desirae Krawczyk / Fanny Stollar (`KXWTADOUBLES-26OCT19KRASTODANJIA-KRASTO`) | 0.34 / 0.42 (5) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jelena Ostapenko vs Belinda Bencic -- WTA Ningbo R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-19 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-20T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-10-19T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202505:211533:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Belinda Bencic (`KXWTAMATCH-26OCT19OSTBEN-BEN`) | 0.54 / 0.55 (1704) | 54.5% | 73.2% | 81.5% | 78.6% [72.4%-80.5%] | -- | -- | -- | -- | WATCH | +18.7 pp | HIGH_REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jelena Ostapenko (`KXWTAMATCH-26OCT19OSTBEN-OST`) | 0.45 / 0.46 (45443) | 45.5% | 26.8% | 18.5% | 21.4% [19.6%-27.6%] | -- | -- | -- | -- | PASS | -18.7 pp | HIGH_REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3919.0, B 3571.0; serve-point win A 54.3%, B 41.0%; Elo A 1932.8, B 2075.7; model uncertainty 0.0402
* Form inputs: days since last match A 2, B 5; matches on record A 681, B 674; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT19OSTBEN-BEN  (YES = Belinda Bencic)
Model: 73%
Kalshi: 55%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.004, surface_dev_loose -0.015, surface_dev_tight +0.020
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTASETWINNER-26OCT19OSTBEN-2-BEN` Will Belinda Bencic win set 2 in the Jelena Ostapenko vs Belinda Bencic match: 0.34/0.72 mid 53.0%, model 66.0% (projection_v2.0 (prediction ledger)) -- gap +13.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT19OSTBEN-1-BEN` Will Belinda Bencic win set 1 in the Jelena Ostapenko vs Belinda Bencic match: 0.52/0.57 mid 54.5%, model 66.0% (projection_v2.0 (prediction ledger)) -- gap +11.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT19OSTBEN-1-OST` Will Jelena Ostapenko win set 1 in the Jelena Ostapenko vs Belinda Bencic match: 0.43/0.48 mid 45.5%, model 34.0% (projection_v2.0 (prediction ledger)) -- gap -11.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT19OSTBEN-2-OST` Will Jelena Ostapenko win set 2 in the Jelena Ostapenko vs Belinda Bencic match: 0.28/0.58 mid 43.0%, model 34.0% (projection_v2.0 (prediction ledger)) -- gap -9.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26OCT19OSTBEN-28` Over 27.5 games: 0.17/0.29 mid 23.0%, model 30.4% (projection_v2.0 (prediction ledger)) -- gap +7.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT19OSTBEN-23` Over 22.5 games: 0.43/0.44 mid 43.5%, model 50.8% (projection_v2.0 (prediction ledger)) -- gap +7.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT19OSTBEN-18` Over 17.5 games: 0.73/0.85 mid 79.0%, model 84.4% (projection_v2.0 (prediction ledger)) -- gap +5.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Qianhui Tang / Yifan Xu vs Erin Routliffe / Aldila Sutjiadi -- WTA Ningbo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-20T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-19T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19TANYIFROUSUT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Erin Routliffe / Aldila Sutjiadi (`KXWTADOUBLES-26OCT19TANYIFROUSUT-ROUSUT`) | 0.64 / 0.68 (5) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Qianhui Tang / Yifan Xu (`KXWTADOUBLES-26OCT19TANYIFROUSUT-TANYIF`) | 0.31 / 0.36 (430) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Daria Kasatkina vs Aliaksandra Sasnovich -- WTA Ningbo R32

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-19 11:00Z
* Current expected start: 2026-10-19 08:15Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-19 07:30Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-165_MIN; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-19T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:205925:214082:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria Kasatkina (`KXWTAMATCH-26OCT19KASSAS-KAS`) | 0.29 / 0.30 (12701) | 29.5% | 54.0% | 47.9% | 50.0% [48.9%-51.6%] | 44.4% | 42.9% | 43.6% | MODEL_LONE_OUTLIER | SHADOW_BET | +24.5 pp | HIGH_REVIEW | FRESH | A / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Aliaksandra Sasnovich (`KXWTAMATCH-26OCT19KASSAS-SAS`) | 0.70 / 0.71 (40116) | 70.5% | 46.0% | 52.1% | 50.0% [48.4%-51.1%] | 55.6% | 56.6% | 56.1% | MODEL_LONE_OUTLIER | PASS | -24.5 pp | HIGH_REVIEW | FRESH | A / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 4023.0, B 4822.0; serve-point win A 52.5%, B 48.3%; Elo A 1878.0, B 1841.4; model uncertainty 0.0134
* Form inputs: days since last match A 6, B 1; matches on record A 670, B 790; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT19KASSAS-KAS  (YES = Daria Kasatkina)
Model: 54%
Kalshi: 30%
Gap: +25 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: SUPPORTS_MODEL_DIRECTION
Data quality: A (LIMITED)
Reasons: SURFACE_DATA_THIN, EXTERNAL_MARKET_CONFIRMATION
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high -0.000, surface_dev_loose -0.011, surface_dev_tight +0.016
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTASETWINNER-26OCT19KASSAS-1-KAS` Will Daria Kasatkina win set 1 in the Daria Kasatkina vs Aliaksandra Sasnovich match: 0.25/0.27 mid 26.0%, model 52.7% (projection_v2.0 (prediction ledger)) -- gap +26.7 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT19KASSAS-1-SAS` Will Aliaksandra Sasnovich win set 1 in the Daria Kasatkina vs Aliaksandra Sasnovich match: 0.73/0.74 mid 73.5%, model 47.3% (projection_v2.0 (prediction ledger)) -- gap -26.2 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26OCT19KASSAS-21` Over 20.5 games: 0.50/0.59 mid 54.5%, model 66.4% (projection_v2.0 (prediction ledger)) -- gap +11.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT19KASSAS-2-KAS` Will Daria Kasatkina win set 2 in the Daria Kasatkina vs Aliaksandra Sasnovich match: 0.41/0.43 mid 42.0%, model 52.7% (projection_v2.0 (prediction ledger)) -- gap +10.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT19KASSAS-2-SAS` Will Aliaksandra Sasnovich win set 2 in the Daria Kasatkina vs Aliaksandra Sasnovich match: 0.57/0.59 mid 58.0%, model 47.3% (projection_v2.0 (prediction ledger)) -- gap -10.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26OCT19KASSAS-26` Over 25.5 games: 0.30/0.38 mid 34.0%, model 43.2% (projection_v2.0 (prediction ledger)) -- gap +9.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT19KASSAS-16` Over 15.5 games: 0.97/0.98 mid 97.5%, model 96.5% (projection_v2.0 (prediction ledger)) -- gap -1.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; STATUS_AMBIGUOUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hanyu Guo / Kristina Mladenovic vs Shuko Aoyama / En-Shuo Liang -- WTA Ningbo R16

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-19 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-19 08:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-19 07:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-19T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19GUOMLAAOYLIA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shuko Aoyama / En-Shuo Liang (`KXWTADOUBLES-26OCT19GUOMLAAOYLIA-AOYLIA`) | 0.35 / 0.38 (607) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hanyu Guo / Kristina Mladenovic (`KXWTADOUBLES-26OCT19GUOMLAAOYLIA-GUOMLA`) | 0.61 / 0.64 (501) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; STATUS_AMBIGUOUS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Luciano Darderi / Tomas Martin Etcheverry vs Jason Kubler / John Peers -- ATP Almaty R16

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-19 08:30Z
* Source: COURT_PROGRESSION: preceding match on Court 1 in progress (set 3 of best-of-5); confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-19 07:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18DARETCKUBPEE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luciano Darderi / Tomas Martin Etcheverry (`KXATPDOUBLES-26OCT18DARETCKUBPEE-DARETC`) | 0.42 / 0.44 (377) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jason Kubler / John Peers (`KXATPDOUBLES-26OCT18DARETCKUBPEE-KUBPEE`) | 0.56 / 0.57 (53) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; STATUS_AMBIGUOUS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Pierre-Hugues Herbert vs Maxim Mrva -- ATP Lyon Q2

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-19 12:00Z
* Current expected start: 2026-10-19 09:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-19 08:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · Clay · scheduled 2026-10-19T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105732:211617:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pierre-Hugues Herbert (`KXATPMATCH-26OCT19HERMRV-HER`) | 0.60 / 0.61 (21938) | 60.5% | 38.0% | 50.0% | 51.5% [48.4%-56.7%] | 61.6% | -- | 61.6% | MARKETS_AGREE | PASS | -22.5 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Maxim Mrva (`KXATPMATCH-26OCT19HERMRV-MRV`) | 0.39 / 0.40 (12006) | 39.5% | 62.0% | 50.0% | 48.4% [43.3%-51.5%] | 38.4% | -- | 38.4% | MARKETS_AGREE | SHADOW_BET | +22.5 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2989.0, B 3391.0; serve-point win A 58.3%, B 39.4%; Elo A 1607.2, B 1580.7; model uncertainty 0.0412
* Form inputs: days since last match A 55, B 28; matches on record A 846, B 101; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT19HERMRV-MRV  (YES = Maxim Mrva)
Model: 62%
Kalshi: 40%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.031, surface_dev_loose -0.021, surface_dev_tight +0.015
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT19HERMRV-HER2` Will Pierre-Hugues Herbert win at least 1.5 more games than Maxim Mrva?: 0.55/0.57 mid 56.0%, model 31.5% (projection_v2.0 (prediction ledger)) -- gap -24.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT19HERMRV-MRV2` Will Maxim Mrva win at least 1.5 more games than Pierre-Hugues Herbert?: 0.31/0.36 mid 33.5%, model 55.3% (projection_v2.0 (prediction ledger)) -- gap +21.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT19HERMRV-HER20` Will Pierre-Hugues Herbert win the Pierre-Hugues Herbert vs Maxim Mrva match by a set score of 2-0?: 0.36/0.39 mid 37.5%, model 17.6% (projection_v2.0 (prediction ledger)) -- gap -19.9 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT19HERMRV-HER5` Will Pierre-Hugues Herbert win at least 4.5 more games than Maxim Mrva?: 0.31/0.33 mid 32.0%, model 13.4% (projection_v2.0 (prediction ledger)) -- gap -18.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT19HERMRV-2-MRV` Will Maxim Mrva win set 2 in the Pierre-Hugues Herbert vs Maxim Mrva match: 0.39/0.42 mid 40.5%, model 58.1% (projection_v2.0 (prediction ledger)) -- gap +17.6 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT19HERMRV-1-MRV` Will Maxim Mrva win set 1 in the Pierre-Hugues Herbert vs Maxim Mrva match: 0.40/0.43 mid 41.5%, model 58.1% (projection_v2.0 (prediction ledger)) -- gap +16.6 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT19HERMRV-2-HER` Will Pierre-Hugues Herbert win set 2 in the Pierre-Hugues Herbert vs Maxim Mrva match: 0.56/0.60 mid 58.0%, model 41.9% (projection_v2.0 (prediction ledger)) -- gap -16.1 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT19HERMRV-1-HER` Will Pierre-Hugues Herbert win set 1 in the Pierre-Hugues Herbert vs Maxim Mrva match: 0.56/0.59 mid 57.5%, model 41.9% (projection_v2.0 (prediction ledger)) -- gap -15.6 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT19HERMRV-MRV20` Will Maxim Mrva win the Pierre-Hugues Herbert vs Maxim Mrva match by a set score of 2-0?: 0.20/0.22 mid 21.0%, model 33.7% (projection_v2.0 (prediction ledger)) -- gap +12.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT19HERMRV-MRV21` Will Maxim Mrva win the Pierre-Hugues Herbert vs Maxim Mrva match by a set score of 2-1?: 0.16/0.19 mid 17.5%, model 28.3% (projection_v2.0 (prediction ledger)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT19HERMRV-25` Over 24.5 games: 0.41/0.44 mid 42.5%, model 49.5% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT19HERMRV-20` Over 19.5 games: 0.56/0.88 mid 72.0%, model 75.5% (projection_v2.0 (prediction ledger)) -- gap +3.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT19HERMRV-30` Over 29.5 games: 0.11/0.44 mid 27.5%, model 25.1% (projection_v2.0 (prediction ledger)) -- gap -2.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT19HERMRV-HER21` Will Pierre-Hugues Herbert win the Pierre-Hugues Herbert vs Maxim Mrva match by a set score of 2-1?: 0.21/0.24 mid 22.5%, model 20.4% (projection_v2.0 (prediction ledger)) -- gap -2.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: WIDE_SPREAD

## Marin Cilic vs Nikoloz Basilashvili -- ATP Almaty R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 14:40Z
* Current expected start: 2026-10-19 09:20Z
* Source: COURT_PROGRESSION: preceding match on Center Court in progress (set 1 of best-of-5); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-19 08:35Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1120_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T14:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105227:105932:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikoloz Basilashvili (`KXATPMATCH-26OCT18CILBAS-BAS`) | 0.58 / 0.59 (23784) | 58.5% | -- | 37.6% | 33.6% [29.1%-35.4%] | -- | -- | -- | -- | PASS | -24.9 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marin Cilic (`KXATPMATCH-26OCT18CILBAS-CIL`) | 0.41 / 0.42 (30458) | 41.5% | -- | 62.4% | 66.4% [64.6%-70.9%] | -- | -- | -- | -- | WATCH | +24.9 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3216.0, B 3285.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0313
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT18CILBAS-CIL  (YES = Marin Cilic)
Model: 66%
Kalshi: 42%
Gap: +25 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.018, surface_dev_loose -0.015, surface_dev_tight +0.014
* Derivatives listed: 6 (GAME_SPREAD, MATCH_WINNER, TOTAL_GAMES); 6 carry a model probability
  * `KXATPGSPREAD-26OCT18CILBAS-BAS2` Will Nikoloz Basilashvili win at least 1.5 more games than Marin Cilic?: 0.51/0.52 mid 51.5%, model 26.0% (projection_v2.0 (prediction ledger)) -- gap -25.5 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18CILBAS-CIL2` Will Marin Cilic win at least 1.5 more games than Nikoloz Basilashvili?: 0.34/0.38 mid 36.0%, model 59.1% (projection_v2.0 (prediction ledger)) -- gap +23.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18CILBAS-BAS5` Will Nikoloz Basilashvili win at least 4.5 more games than Marin Cilic?: 0.21/0.23 mid 22.0%, model 6.8% (projection_v2.0 (prediction ledger)) -- gap -15.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18CILBAS-25` Over 24.5 games: 0.46/0.48 mid 47.0%, model 53.4% (projection_v2.0 (prediction ledger)) -- gap +6.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18CILBAS-30` Over 29.5 games: 0.28/0.32 mid 30.0%, model 33.7% (projection_v2.0 (prediction ledger)) -- gap +3.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18CILBAS-20` Over 19.5 games: 0.80/0.84 mid 82.0%, model 83.4% (projection_v2.0 (prediction ledger)) -- gap +1.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE

## Alexander Donski / Filip Pieczonka vs Arthur Reymond / Luca Sanchez -- ATP Almaty R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-19 09:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-19 08:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18DONPIEREYSAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Donski / Filip Pieczonka (`KXATPDOUBLES-26OCT18DONPIEREYSAN-DONPIE`) | 0.48 / 0.51 (165) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arthur Reymond / Luca Sanchez (`KXATPDOUBLES-26OCT18DONPIEREYSAN-REYSAN`) | 0.48 / 0.51 (165) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Kamilla Rakhimova vs Marie Bouzkova -- WTA Ningbo R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-19 12:10Z
* Current expected start: 2026-10-19 09:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-19 08:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-19T12:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213631:215872:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marie Bouzkova (`KXWTAMATCH-26OCT19RAKBOU-BOU`) | 0.71 / 0.72 (32038) | 71.5% | 61.1% | 62.0% | 63.1% [62.0%-64.1%] | 70.6% | 71.5% | 71.0% | MODEL_LONE_OUTLIER | PASS | -10.4 pp | REVIEW | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Kamilla Rakhimova (`KXWTAMATCH-26OCT19RAKBOU-RAK`) | 0.28 / 0.29 (23791) | 28.5% | 39.0% | 38.0% | 36.9% [35.9%-38.0%] | 29.4% | 28.4% | 28.9% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.4 pp | REVIEW | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5718.0, B 4089.0; serve-point win A 53.7%, B 44.2%; Elo A 1844.0, B 1959.6; model uncertainty 0.0101
* Form inputs: days since last match A 2, B 5; matches on record A 476, B 644; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight -0.010
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT19RAKBOU-21` Over 20.5 games: 0.51/0.52 mid 51.5%, model 66.1% (projection_v2.0 (prediction ledger)) -- gap +14.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT19RAKBOU-26` Over 25.5 games: 0.28/0.31 mid 29.5%, model 43.0% (projection_v2.0 (prediction ledger)) -- gap +13.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT19RAKBOU-2-RAK` Will Kamilla Rakhimova win set 2 in the Kamilla Rakhimova vs Marie Bouzkova match: 0.30/0.33 mid 31.5%, model 42.6% (projection_v2.0 (prediction ledger)) -- gap +11.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT19RAKBOU-1-RAK` Will Kamilla Rakhimova win set 1 in the Kamilla Rakhimova vs Marie Bouzkova match: 0.32/0.34 mid 33.0%, model 42.6% (projection_v2.0 (prediction ledger)) -- gap +9.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT19RAKBOU-2-BOU` Will Marie Bouzkova win set 2 in the Kamilla Rakhimova vs Marie Bouzkova match: 0.65/0.69 mid 67.0%, model 57.4% (projection_v2.0 (prediction ledger)) -- gap -9.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT19RAKBOU-1-BOU` Will Marie Bouzkova win set 1 in the Kamilla Rakhimova vs Marie Bouzkova match: 0.65/0.67 mid 66.0%, model 57.4% (projection_v2.0 (prediction ledger)) -- gap -8.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26OCT19RAKBOU-16` Over 15.5 games: 0.90/0.97 mid 93.5%, model 96.6% (projection_v2.0 (prediction ledger)) -- gap +3.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
* Warnings: WIDE_SPREAD

## Mert Alkaya vs Andre Ilagan -- ATP Challenger Guangzhou Nansha R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-19T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207368:210318:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mert Alkaya (`KXATPCHALLENGERMATCH-26OCT19ALKILA-ALK`) | 0.39 / 0.40 (5489) | 39.5% | 49.7% | 49.5% | 46.4% [40.9%-47.9%] | -- | 35.0% | 35.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.2 pp | REVIEW | FRESH | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Andre Ilagan (`KXATPCHALLENGERMATCH-26OCT19ALKILA-ILA`) | 0.60 / 0.61 (22604) | 60.5% | 50.3% | 50.5% | 53.6% [52.0%-59.1%] | -- | 64.6% | 64.6% | MODEL_LONE_OUTLIER | PASS | -10.2 pp | REVIEW | FRESH | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1502.0, B 1597.0; serve-point win A 60.6%, B 39.3%; Elo A 1460.4, B 1508.3; model uncertainty 0.035
* Form inputs: days since last match A 29, B 14; matches on record A 107, B 123; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.010, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## James McCabe vs Elias Ymer -- ATP Challenger Guangzhou Nansha R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-19T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111200:210317:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| James McCabe (`KXATPCHALLENGERMATCH-26OCT19MCCYME-MCC`) | 0.71 / 0.72 (29991) | 71.5% | 45.1% | 40.8% | 43.6% [40.7%-46.6%] | -- | 39.0% | 39.0% | MODEL_LONE_OUTLIER | WATCH | -26.4 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Elias Ymer (`KXATPCHALLENGERMATCH-26OCT19MCCYME-YME`) | 0.28 / 0.29 (15552) | 28.5% | 54.9% | 59.2% | 56.4% [53.4%-59.3%] | -- | 60.6% | 60.6% | MODEL_LONE_OUTLIER | PASS | +26.4 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 3266.0, B 3750.0; serve-point win A 64.8%, B 34.2%; Elo A 1578.1, B 1587.2; model uncertainty 0.0292
* Form inputs: days since last match A 20, B 14; matches on record A 293, B 786; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT19MCCYME-YME  (YES = Elias Ymer)
Model: 55%
Kalshi: 28%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: SUPPORTS_MODEL_DIRECTION
Data quality: A (ADEQUATE)
Reasons: EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.029, surface_pool_high +0.029, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Petr Nouza / Michael Venus vs Constantin Frantzen / Robert Galloway -- ATP Brussels R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-19 10:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-19 09:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18NOUVENFRAGAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Constantin Frantzen / Robert Galloway (`KXATPDOUBLES-26OCT18NOUVENFRAGAL-FRAGAL`) | 0.29 / 0.56 (45) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Petr Nouza / Michael Venus (`KXATPDOUBLES-26OCT18NOUVENFRAGAL-NOUVEN`) | 0.43 / 0.62 (57) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Federico Cina vs Jaume Munar -- ATP Brussels R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-19 13:00Z
* Current expected start: 2026-10-19 10:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-19 09:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-19T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144719:210748:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Federico Cina (`KXATPMATCH-26OCT19CINMUN-CIN`) | 0.29 / 0.30 (13439) | 29.5% | 33.7% | 24.9% | 28.2% [26.6%-29.9%] | 29.4% | -- | 29.4% | MODEL_LONE_OUTLIER | PASS | +4.2 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Jaume Munar (`KXATPMATCH-26OCT19CINMUN-MUN`) | 0.70 / 0.71 (33642) | 70.5% | 66.3% | 75.1% | 71.8% [70.1%-73.5%] | 70.6% | -- | 70.6% | MODEL_LONE_OUTLIER | PASS | -4.2 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3338.0, B 4437.0; serve-point win A 61.8%, B 34.8%; Elo A 1670.7, B 1767.2; model uncertainty 0.0169
* Form inputs: days since last match A 12, B 11; matches on record A 152, B 730; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.017, surface_pool_high +0.017, surface_dev_loose -0.004, surface_dev_tight -0.001
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT19CINMUN-MUN5` Will Jaume Munar win at least 4.5 more games than Federico Cina?: 0.42/0.43 mid 42.5%, model 27.0% (projection_v2.0 (prediction ledger)) -- gap -15.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT19CINMUN-22` Over 21.5 games: 0.52/0.53 mid 52.5%, model 66.5% (projection_v2.0 (prediction ledger)) -- gap +14.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT19CINMUN-27` Over 26.5 games: 0.29/0.31 mid 30.0%, model 42.1% (projection_v2.0 (prediction ledger)) -- gap +12.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT19CINMUN-MUN20` Will Jaume Munar win the Federico Cina vs Jaume Munar match by a set score of 2-0?: 0.46/0.47 mid 46.5%, model 37.3% (projection_v2.0 (prediction ledger)) -- gap -9.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT19CINMUN-MUN8` Will Jaume Munar win at least 7.5 more games than Federico Cina?: 0.02/0.21 mid 11.5%, model 3.1% (projection_v2.0 (prediction ledger)) -- gap -8.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT19CINMUN-17` Over 16.5 games: 0.87/0.93 mid 90.0%, model 96.7% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT19CINMUN-MUN21` Will Jaume Munar win the Federico Cina vs Jaume Munar match by a set score of 2-1?: 0.21/0.24 mid 22.5%, model 29.0% (projection_v2.0 (prediction ledger)) -- gap +6.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT19CINMUN-2-CIN` Will Federico Cina win set 2 in the Federico Cina vs Jaume Munar match: 0.31/0.34 mid 32.5%, model 39.0% (projection_v2.0 (prediction ledger)) -- gap +6.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT19CINMUN-MUN2` Will Jaume Munar win at least 1.5 more games than Federico Cina?: 0.63/0.68 mid 65.5%, model 59.3% (projection_v2.0 (prediction ledger)) -- gap -6.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT19CINMUN-CIN21` Will Federico Cina win the Federico Cina vs Jaume Munar match by a set score of 2-1?: 0.12/0.13 mid 12.5%, model 18.5% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT19CINMUN-1-CIN` Will Federico Cina win set 1 in the Federico Cina vs Jaume Munar match: 0.33/0.34 mid 33.5%, model 39.0% (projection_v2.0 (prediction ledger)) -- gap +5.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT19CINMUN-2-MUN` Will Jaume Munar win set 2 in the Federico Cina vs Jaume Munar match: 0.65/0.67 mid 66.0%, model 61.1% (projection_v2.0 (prediction ledger)) -- gap -5.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT19CINMUN-1-MUN` Will Jaume Munar win set 1 in the Federico Cina vs Jaume Munar match: 0.64/0.67 mid 65.5%, model 61.1% (projection_v2.0 (prediction ledger)) -- gap -4.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT19CINMUN-CIN20` Will Federico Cina win the Federico Cina vs Jaume Munar match by a set score of 2-0?: 0.13/0.16 mid 14.5%, model 15.2% (projection_v2.0 (prediction ledger)) -- gap +0.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Vitaliy Sachko vs Borna Gojo -- ATP Lyon Q2

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-19 13:00Z
* Current expected start: 2026-10-19 10:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-19 09:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · Clay · scheduled 2026-10-19T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126964:127339:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Borna Gojo (`KXATPMATCH-26OCT19SACGOJ-GOJ`) | 0.55 / 0.56 (24513) | 55.5% | 45.4% | 47.0% | 46.5% [43.6%-49.5%] | 58.3% | -- | 58.3% | KALSHI_LONE_OUTLIER | PASS | -10.1 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Vitaliy Sachko (`KXATPMATCH-26OCT19SACGOJ-SAC`) | 0.44 / 0.45 (51) | 44.5% | 54.6% | 53.0% | 53.5% [50.5%-56.4%] | 41.7% | -- | 41.7% | KALSHI_LONE_OUTLIER | SHADOW_BET | +10.1 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3730.0, B 2738.0; serve-point win A 64.5%, B 36.4%; Elo A 1653.4, B 1619.2; model uncertainty 0.0297
* Form inputs: days since last match A 21, B 14; matches on record A 517, B 441; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.030, surface_dev_loose +0.010, surface_dev_tight -0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT19SACGOJ-GOJ3` Will Borna Gojo win at least 2.5 more games than Vitaliy Sachko?: 0.43/0.45 mid 44.0%, model 31.3% (projection_v2.0 (prediction ledger)) -- gap -12.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT19SACGOJ-SAC2` Will Vitaliy Sachko win at least 1.5 more games than Borna Gojo?: 0.32/0.37 mid 34.5%, model 47.0% (projection_v2.0 (prediction ledger)) -- gap +12.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT19SACGOJ-GOJ20` Will Borna Gojo win the Vitaliy Sachko vs Borna Gojo match by a set score of 2-0?: 0.33/0.35 mid 34.0%, model 22.0% (projection_v2.0 (prediction ledger)) -- gap -12.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT19SACGOJ-GOJ6` Will Borna Gojo win at least 5.5 more games than Vitaliy Sachko?: 0.01/0.34 mid 17.5%, model 7.0% (projection_v2.0 (prediction ledger)) -- gap -10.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT19SACGOJ-18` Over 17.5 games: 0.72/0.95 mid 83.5%, model 93.9% (projection_v2.0 (prediction ledger)) -- gap +10.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT19SACGOJ-1-GOJ` Will Borna Gojo win set 1 in the Vitaliy Sachko vs Borna Gojo match: 0.56/0.57 mid 56.5%, model 46.9% (projection_v2.0 (prediction ledger)) -- gap -9.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT19SACGOJ-1-SAC` Will Vitaliy Sachko win set 1 in the Vitaliy Sachko vs Borna Gojo match: 0.43/0.45 mid 44.0%, model 53.1% (projection_v2.0 (prediction ledger)) -- gap +9.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT19SACGOJ-2-SAC` Will Vitaliy Sachko win set 2 in the Vitaliy Sachko vs Borna Gojo match: 0.43/0.45 mid 44.0%, model 53.1% (projection_v2.0 (prediction ledger)) -- gap +9.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT19SACGOJ-23` Over 22.5 games: 0.52/0.53 mid 52.5%, model 61.5% (projection_v2.0 (prediction ledger)) -- gap +9.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT19SACGOJ-SAC21` Will Vitaliy Sachko win the Vitaliy Sachko vs Borna Gojo match by a set score of 2-1?: 0.18/0.19 mid 18.5%, model 26.4% (projection_v2.0 (prediction ledger)) -- gap +7.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT19SACGOJ-2-GOJ` Will Borna Gojo win set 2 in the Vitaliy Sachko vs Borna Gojo match: 0.52/0.57 mid 54.5%, model 46.9% (projection_v2.0 (prediction ledger)) -- gap -7.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT19SACGOJ-28` Over 27.5 games: 0.30/0.38 mid 34.0%, model 41.1% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT19SACGOJ-SAC20` Will Vitaliy Sachko win the Vitaliy Sachko vs Borna Gojo match by a set score of 2-0?: 0.22/0.24 mid 23.0%, model 28.2% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT19SACGOJ-GOJ21` Will Borna Gojo win the Vitaliy Sachko vs Borna Gojo match by a set score of 2-1?: 0.21/0.24 mid 22.5%, model 23.4% (projection_v2.0 (prediction ledger)) -- gap +0.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kyrian Jacquet vs Michael Mmoh -- ATP Lyon Q2

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-19 13:10Z
* Current expected start: 2026-10-19 10:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-19 09:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN

ATP (TOUR_500_250) · Clay · scheduled 2026-10-19T13:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111581:208021:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kyrian Jacquet (`KXATPMATCH-26OCT19JACMMO-JAC`) | 0.67 / 0.68 (5020) | 67.5% | 69.2% | 51.0% | 58.2% [55.6%-62.1%] | 66.4% | -- | 66.4% | MODEL_LONE_OUTLIER | PASS | +1.7 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Michael Mmoh (`KXATPMATCH-26OCT19JACMMO-MMO`) | 0.32 / 0.33 (27627) | 32.5% | 30.8% | 49.0% | 41.8% [37.9%-44.4%] | 33.6% | -- | 33.6% | MODEL_LONE_OUTLIER | SHADOW_BET | -1.7 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3771.0, B 2931.0; serve-point win A 62.5%, B 41.4%; Elo A 1691.6, B 1529.5; model uncertainty 0.0325
* Form inputs: days since last match A 13, B 21; matches on record A 388, B 552; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight +0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT19JACMMO-JAC21` Will Kyrian Jacquet win the Kyrian Jacquet vs Michael Mmoh match by a set score of 2-1?: 0.22/0.25 mid 23.5%, model 29.4% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT19JACMMO-JAC20` Will Kyrian Jacquet win the Kyrian Jacquet vs Michael Mmoh match by a set score of 2-0?: 0.43/0.44 mid 43.5%, model 39.8% (projection_v2.0 (prediction ledger)) -- gap -3.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT19JACMMO-MMO20` Will Michael Mmoh win the Kyrian Jacquet vs Michael Mmoh match by a set score of 2-0?: 0.15/0.18 mid 16.5%, model 13.6% (projection_v2.0 (prediction ledger)) -- gap -2.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT19JACMMO-MMO21` Will Michael Mmoh win the Kyrian Jacquet vs Michael Mmoh match by a set score of 2-1?: 0.14/0.17 mid 15.5%, model 17.2% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT19JACMMO-2-MMO` Will Michael Mmoh win set 2 in the Kyrian Jacquet vs Michael Mmoh match: 0.33/0.38 mid 35.5%, model 36.9% (projection_v2.0 (prediction ledger)) -- gap +1.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT19JACMMO-1-MMO` Will Michael Mmoh win set 1 in the Kyrian Jacquet vs Michael Mmoh match: 0.34/0.38 mid 36.0%, model 36.9% (projection_v2.0 (prediction ledger)) -- gap +0.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT19JACMMO-2-JAC` Will Kyrian Jacquet win set 2 in the Kyrian Jacquet vs Michael Mmoh match: 0.62/0.65 mid 63.5%, model 63.1% (projection_v2.0 (prediction ledger)) -- gap -0.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT19JACMMO-1-JAC` Will Kyrian Jacquet win set 1 in the Kyrian Jacquet vs Michael Mmoh match: 0.62/0.64 mid 63.0%, model 63.1% (projection_v2.0 (prediction ledger)) -- gap +0.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Izan Almazan Valiente vs Alex Marti Pujolras -- ATP Challenger Florence Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-19T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207704:212978:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Izan Almazan Valiente (`KXATPCHALLENGERMATCH-26OCT19ALMMAR-ALM`) | 0.47 / 0.48 (232) | 47.5% | 30.1% | 46.9% | 32.8% [26.0%-36.2%] | 55.4% | -- | 55.4% | MODEL_LONE_OUTLIER | PASS | -17.4 pp | HIGH_REVIEW | FRESH | F / POOR | ALL_DISAGREE | VERIFIED |
| Alex Marti Pujolras (`KXATPCHALLENGERMATCH-26OCT19ALMMAR-MAR`) | 0.51 / 0.52 (20059) | 51.5% | 69.9% | 53.1% | 67.2% [63.8%-74.0%] | 44.6% | -- | 44.6% | MODEL_LONE_OUTLIER | PASS | +18.4 pp | HIGH_REVIEW | FRESH | F / POOR | ALL_DISAGREE | VERIFIED |

* Serve evidence (points): A 663.0, B 1457.0; serve-point win A 55.9%, B 40.1%; Elo A 1327.7, B 1501.2; model uncertainty 0.0509
* Form inputs: days since last match A 28, B 693; matches on record A 18, B 339; data quality F

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT19ALMMAR-MAR  (YES = Alex Marti Pujolras)
Model: 70%
Kalshi: 52%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: ALL_DISAGREE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.005, surface_dev_loose +0.009, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Romain Arneodo / Ugo Blanchet vs Gonzalo Escobar / Niki Kaliyanda Poonacha -- ATP Lyon R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-20T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-19T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19ARNBLAESCKAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Romain Arneodo / Ugo Blanchet (`KXATPDOUBLES-26OCT19ARNBLAESCKAL-ARNBLA`) | 0.18 / 0.63 (2) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gonzalo Escobar / Niki Kaliyanda Poonacha (`KXATPDOUBLES-26OCT19ARNBLAESCKAL-ESCKAL`) | 0.39 / 0.75 (2) | 57.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Titouan Droguet / Kyrian Jacquet vs Theo Arribage / Albano Olivetti -- ATP Lyon R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-20T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-19T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19DROJACARROLI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theo Arribage / Albano Olivetti (`KXATPDOUBLES-26OCT19DROJACARROLI-ARROLI`) | 0.39 / 0.77 (2) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Titouan Droguet / Kyrian Jacquet (`KXATPDOUBLES-26OCT19DROJACARROLI-DROJAC`) | 0.19 / 0.54 (1) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Filip Misolic vs Daniel Siniakov -- ATP Challenger Florence Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-19T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209209:209338:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filip Misolic (`KXATPCHALLENGERMATCH-26OCT19MISSIN-MIS`) | 0.74 / 0.77 (1) | 75.5% | 90.6% | 74.9% | 87.2% [81.0%-92.5%] | 71.6% | -- | 71.6% | MODEL_LONE_OUTLIER | WATCH | +15.1 pp | HIGH_REVIEW | FRESH | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Daniel Siniakov (`KXATPCHALLENGERMATCH-26OCT19MISSIN-SIN`) | 0.22 / 0.25 (74) | 23.5% | 9.4% | 25.1% | 12.8% [7.5%-19.0%] | 28.4% | -- | 28.4% | MODEL_LONE_OUTLIER | PASS | -14.1 pp | REVIEW | FRESH | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2562.0, B 334.0; serve-point win A 65.0%, B 45.2%; Elo A 1600.2, B 1231.7; model uncertainty 0.0573
* Form inputs: days since last match A 42, B 42; matches on record A 293, B 81; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT19MISSIN-MIS  (YES = Filip Misolic)
Model: 91%
Kalshi: 76%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, MODEL_HIGH_UNCERTAINTY, MODEL_CALIBRATION_OUTLIER, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.044, surface_pool_high -0.062, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; THIN_DISPLAYED_SIZE

## Hugo Nys / Edouard Roger-Vasselin vs Finn Reynolds / James Watt -- ATP Lyon R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-20T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-19T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19NYSROGREYWAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Nys / Edouard Roger-Vasselin (`KXATPDOUBLES-26OCT19NYSROGREYWAT-NYSROG`) | 0.28 / 0.88 (3) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Finn Reynolds / James Watt (`KXATPDOUBLES-26OCT19NYSROGREYWAT-REYWAT`) | 0.11 / 0.58 (1) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jakub Paul / Matej Vocel vs Santiago Gonzalez / Hendrik Jebens -- ATP Lyon R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-20T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-19T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19PAUVOCGONJEB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Santiago Gonzalez / Hendrik Jebens (`KXATPDOUBLES-26OCT19PAUVOCGONJEB-GONJEB`) | 0.12 / 0.69 (3) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jakub Paul / Matej Vocel (`KXATPDOUBLES-26OCT19PAUVOCGONJEB-PAUVOC`) | 0.30 / 0.83 (3) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sergi Perez Contri vs Dimitris Sakellaridis -- ATP Challenger Florence Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-19T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133997:212029:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sergi Perez Contri (`KXATPCHALLENGERMATCH-26OCT19PERSAK-PER`) | 0.67 / 0.68 (20330) | 67.5% | 80.4% | 63.7% | 74.2% [68.0%-80.1%] | 68.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +12.9 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dimitris Sakellaridis (`KXATPCHALLENGERMATCH-26OCT19PERSAK-SAK`) | 0.33 / 0.34 (17772) | 33.5% | 19.6% | 36.3% | 25.8% [19.9%-32.0%] | 31.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.9 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 459.0, B 114.0; serve-point win A 62.5%, B 44.1%; Elo A 1388.8, B 1196.0; model uncertainty 0.0604
* Form inputs: days since last match A 196, B 14; matches on record A 280, B 39; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.059, surface_pool_high -0.062, surface_dev_loose +0.001, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE

## David Stevenson / Marcus Willis vs Andrew Paulson / Nino Serdarusic -- ATP Lyon R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-20T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-19T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19STEWILPAUSER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrew Paulson / Nino Serdarusic (`KXATPDOUBLES-26OCT19STEWILPAUSER-PAUSER`) | 0.18 / 0.62 (2) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| David Stevenson / Marcus Willis (`KXATPDOUBLES-26OCT19STEWILPAUSER-STEWIL`) | 0.38 / 0.82 (2) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jiangxue HAN vs Marika Jones -- W35 Qian Daohu R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-19T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220497:222913:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jiangxue HAN (`KXITFWMATCH-26OCT19HANJON-HAN`) | 0.82 / 0.83 (0) | 82.5% | 94.1% | 71.8% | 86.7% [85.8%-87.4%] | -- | -- | -- | -- | PASS | +11.6 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marika Jones (`KXITFWMATCH-26OCT19HANJON-JON`) | 0.17 / 0.18 (8) | 17.5% | 5.9% | 28.2% | 13.3% [12.6%-14.2%] | -- | -- | -- | -- | PASS | -11.6 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1410.0, B 76.0; serve-point win A 53.5%, B 58.1%; Elo A 1458.9, B 1127.1; model uncertainty 0.0079
* Form inputs: days since last match A 175, B 350; matches on record A 174, B 78; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.006, surface_dev_loose +0.003, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tallon Griekspoor / Botic Van de Zandschulp vs Juan Manuel Cerundolo / Benjamin Kittay -- ATP Brussels R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-19 11:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-19 10:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18GRIVANCERKIT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Manuel Cerundolo / Benjamin Kittay (`KXATPDOUBLES-26OCT18GRIVANCERKIT-CERKIT`) | 0.33 / 0.36 (23) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tallon Griekspoor / Botic Van de Zandschulp (`KXATPDOUBLES-26OCT18GRIVANCERKIT-GRIVAN`) | 0.63 / 0.67 (106) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Yannick Hanfmann vs Martin Damm Jr -- ATP Brussels R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-19 14:10Z
* Current expected start: 2026-10-19 11:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-19 10:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-19T14:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:102093:105870:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martin Damm Jr (`KXATPMATCH-26OCT19HANDAM-DAM`) | 0.48 / 0.49 (52514) | 48.5% | 16.1% | 23.8% | 26.4% [19.9%-30.7%] | 47.8% | -- | 47.8% | MODEL_LONE_OUTLIER | PASS | -32.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Yannick Hanfmann (`KXATPMATCH-26OCT19HANDAM-HAN`) | 0.51 / 0.52 (7037) | 51.5% | 83.9% | 76.2% | 73.6% [69.3%-80.1%] | 52.2% | -- | 52.2% | MODEL_LONE_OUTLIER | PASS | +32.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4562.0, B 3075.0; serve-point win A 74.0%, B 34.5%; Elo A 1728.0, B 1594.2; model uncertainty 0.0543
* Form inputs: days since last match A 10, B 728; matches on record A 656, B 252; data quality F

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT19HANDAM-HAN  (YES = Yannick Hanfmann)
Model: 84%
Kalshi: 52%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.040, surface_pool_high -0.043, surface_dev_loose +0.003, surface_dev_tight +0.001
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT19HANDAM-HAN2` Will Yannick Hanfmann win at least 1.5 more games than Martin Damm Jr?: 0.42/0.43 mid 42.5%, model 77.5% (projection_v2.0 (prediction ledger)) -- gap +35.0 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data POOR
  * `KXATPGSPREAD-26OCT19HANDAM-DAM2` Will Martin Damm Jr win at least 1.5 more games than Yannick Hanfmann?: 0.38/0.40 mid 39.0%, model 11.1% (projection_v2.0 (prediction ledger)) -- gap -27.9 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data POOR
  * `KXATPEXACTMATCH-26OCT19HANDAM-HAN20` Will Yannick Hanfmann win the Yannick Hanfmann vs Martin Damm Jr match by a set score of 2-0?: 0.28/0.32 mid 30.0%, model 55.6% (projection_v2.0 (prediction ledger)) -- gap +25.6 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data POOR
  * `KXATPSETWINNER-26OCT19HANDAM-1-HAN` Will Yannick Hanfmann win set 1 in the Yannick Hanfmann vs Martin Damm Jr match: 0.50/0.54 mid 52.0%, model 74.6% (projection_v2.0 (prediction ledger)) -- gap +22.6 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT19HANDAM-1-DAM` Will Martin Damm Jr win set 1 in the Yannick Hanfmann vs Martin Damm Jr match: 0.46/0.49 mid 47.5%, model 25.4% (projection_v2.0 (prediction ledger)) -- gap -22.1 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT19HANDAM-2-HAN` Will Yannick Hanfmann win set 2 in the Yannick Hanfmann vs Martin Damm Jr match: 0.51/0.54 mid 52.5%, model 74.6% (projection_v2.0 (prediction ledger)) -- gap +22.1 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT19HANDAM-2-DAM` Will Martin Damm Jr win set 2 in the Yannick Hanfmann vs Martin Damm Jr match: 0.46/0.48 mid 47.0%, model 25.4% (projection_v2.0 (prediction ledger)) -- gap -21.6 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPEXACTMATCH-26OCT19HANDAM-DAM20` Will Martin Damm Jr win the Yannick Hanfmann vs Martin Damm Jr match by a set score of 2-0?: 0.24/0.28 mid 26.0%, model 6.5% (projection_v2.0 (prediction ledger)) -- gap -19.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data POOR
  * `KXATPEXACTMATCH-26OCT19HANDAM-DAM21` Will Martin Damm Jr win the Yannick Hanfmann vs Martin Damm Jr match by a set score of 2-1?: 0.19/0.22 mid 20.5%, model 9.7% (projection_v2.0 (prediction ledger)) -- gap -10.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data POOR
  * `KXATPGTOTAL-26OCT19HANDAM-24` Over 23.5 games: 0.55/0.56 mid 55.5%, model 46.9% (projection_v2.0 (prediction ledger)) -- gap -8.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPGSPREAD-26OCT19HANDAM-HAN5` Will Yannick Hanfmann win at least 4.5 more games than Martin Damm Jr?: 0.07/0.36 mid 21.5%, model 29.5% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPEXACTMATCH-26OCT19HANDAM-HAN21` Will Yannick Hanfmann win the Yannick Hanfmann vs Martin Damm Jr match by a set score of 2-1?: 0.21/0.23 mid 22.0%, model 28.3% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPGTOTAL-26OCT19HANDAM-19` Over 18.5 games: 0.91/0.95 mid 93.0%, model 89.5% (projection_v2.0 (prediction ledger)) -- gap -3.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPGTOTAL-26OCT19HANDAM-29` Over 28.5 games: 0.32/0.36 mid 34.0%, model 32.4% (projection_v2.0 (prediction ledger)) -- gap -1.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Clement Tabur vs Nicolai Budkov Kjaer -- ATP Lyon Q2

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-19 11:00Z
* Current expected start: 2026-10-19 11:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-19 10:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+30_MIN

ATP (TOUR_500_250) · Clay · scheduled 2026-10-19T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:149282:202127:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolai Budkov Kjaer (`KXATPMATCH-26OCT19TABBUD-BUD`) | 0.54 / 0.56 (23519) | 55.0% | 57.3% | 50.5% | 53.6% [52.0%-55.1%] | 55.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Clement Tabur (`KXATPMATCH-26OCT19TABBUD-TAB`) | 0.45 / 0.46 (27195) | 45.5% | 42.7% | 49.5% | 46.4% [44.9%-48.0%] | 44.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3384.0, B 3085.0; serve-point win A 60.9%, B 37.6%; Elo A 1582.1, B 1649.3; model uncertainty 0.0152
* Form inputs: days since last match A 21, B 21; matches on record A 442, B 143; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.015, surface_dev_loose -0.010, surface_dev_tight +0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT19TABBUD-BUD21` Will Nicolai Budkov Kjaer win the Clement Tabur vs Nicolai Budkov Kjaer match by a set score of 2-1?: 0.21/0.23 mid 22.0%, model 27.2% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT19TABBUD-TAB20` Will Clement Tabur win the Clement Tabur vs Nicolai Budkov Kjaer match by a set score of 2-0?: 0.25/0.26 mid 25.5%, model 20.4% (projection_v2.0 (prediction ledger)) -- gap -5.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT19TABBUD-TAB21` Will Clement Tabur win the Clement Tabur vs Nicolai Budkov Kjaer match by a set score of 2-1?: 0.19/0.21 mid 20.0%, model 22.4% (projection_v2.0 (prediction ledger)) -- gap +2.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT19TABBUD-1-BUD` Will Nicolai Budkov Kjaer win set 1 in the Clement Tabur vs Nicolai Budkov Kjaer match: 0.52/0.54 mid 53.0%, model 54.9% (projection_v2.0 (prediction ledger)) -- gap +1.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT19TABBUD-BUD20` Will Nicolai Budkov Kjaer win the Clement Tabur vs Nicolai Budkov Kjaer match by a set score of 2-0?: 0.31/0.32 mid 31.5%, model 30.1% (projection_v2.0 (prediction ledger)) -- gap -1.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT19TABBUD-2-BUD` Will Nicolai Budkov Kjaer win set 2 in the Clement Tabur vs Nicolai Budkov Kjaer match: 0.52/0.56 mid 54.0%, model 54.9% (projection_v2.0 (prediction ledger)) -- gap +0.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT19TABBUD-1-TAB` Will Clement Tabur win set 1 in the Clement Tabur vs Nicolai Budkov Kjaer match: 0.44/0.47 mid 45.5%, model 45.1% (projection_v2.0 (prediction ledger)) -- gap -0.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT19TABBUD-2-TAB` Will Clement Tabur win set 2 in the Clement Tabur vs Nicolai Budkov Kjaer match: 0.43/0.48 mid 45.5%, model 45.1% (projection_v2.0 (prediction ledger)) -- gap -0.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alexandra Eala vs Diane Parry -- WTA Ningbo R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-19 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-19 11:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-19 10:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-19T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220348:223253:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandra Eala (`KXWTAMATCH-26OCT19EALPAR-EAL`) | 0.73 / 0.74 (8014) | 73.5% | 76.3% | 70.0% | 71.7% [66.8%-73.9%] | 72.6% | 73.3% | 73.3% | MODEL_LONE_OUTLIER | PASS | +2.9 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Diane Parry (`KXWTAMATCH-26OCT19EALPAR-PAR`) | 0.26 / 0.28 (68598) | 27.0% | 23.6% | 30.0% | 28.3% [26.1%-33.2%] | 27.4% | 26.7% | 26.7% | MODEL_LONE_OUTLIER | PASS | -3.4 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4541.0, B 3742.0; serve-point win A 61.2%, B 44.3%; Elo A 1956.2, B 1755.9; model uncertainty 0.0356
* Form inputs: days since last match A 25, B 7; matches on record A 365, B 431; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.022, surface_pool_high +0.022, surface_dev_loose +0.009, surface_dev_tight -0.009
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT19EALPAR-20` Over 19.5 games: 0.54/0.56 mid 55.0%, model 68.9% (projection_v2.0 (prediction ledger)) -- gap +13.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT19EALPAR-15` Over 14.5 games: 0.71/0.99 mid 85.0%, model 98.6% (projection_v2.0 (prediction ledger)) -- gap +13.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT19EALPAR-25` Over 24.5 games: 0.32/0.34 mid 33.0%, model 43.1% (projection_v2.0 (prediction ledger)) -- gap +10.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT19EALPAR-2-PAR` Will Diane Parry win set 2 in the Alexandra Eala vs Diane Parry match: 0.28/0.33 mid 30.5%, model 31.6% (projection_v2.0 (prediction ledger)) -- gap +1.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT19EALPAR-1-EAL` Will Alexandra Eala win set 1 in the Alexandra Eala vs Diane Parry match: 0.68/0.70 mid 69.0%, model 68.4% (projection_v2.0 (prediction ledger)) -- gap -0.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT19EALPAR-1-PAR` Will Diane Parry win set 1 in the Alexandra Eala vs Diane Parry match: 0.30/0.32 mid 31.0%, model 31.6% (projection_v2.0 (prediction ledger)) -- gap +0.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT19EALPAR-2-EAL` Will Alexandra Eala win set 2 in the Alexandra Eala vs Diane Parry match: 0.66/0.72 mid 69.0%, model 68.4% (projection_v2.0 (prediction ledger)) -- gap -0.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Azuma Visaya vs Ethan David Zapp -- M15 Singapore R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19VISZAP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Azuma Visaya (`KXITFMATCH-26OCT19VISZAP-VIS`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ethan David Zapp (`KXITFMATCH-26OCT19VISZAP-ZAP`) | -- / 0.01 (5510) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vasco Leote Prata vs Joao Domingues -- ATP Challenger Lisbon Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-19T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106249:211330:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joao Domingues (`KXATPCHALLENGERMATCH-26OCT19LEODOM-DOM`) | 0.78 / 0.79 (5283) | 78.5% | 73.0% | 45.9% | 68.8% [64.1%-73.2%] | 77.7% | -- | 77.7% | MARKETS_AGREE | PASS | -5.5 pp | NORMAL | FRESH | F / POOR | AGREES_WITH_KALSHI | AMBIGUOUS |
| Vasco Leote Prata (`KXATPCHALLENGERMATCH-26OCT19LEODOM-LEO`) | 0.21 / 0.22 (4386) | 21.5% | 27.0% | 54.1% | 31.2% [26.8%-35.9%] | 22.3% | -- | 22.3% | MODEL_LONE_OUTLIER | PASS | +5.5 pp | NORMAL | FRESH | F / POOR | AGREES_WITH_KALSHI | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 513.0; serve-point win A 57.7%, B 37.5%; Elo A 1364.7, B 1505.5; model uncertainty 0.0456
* Form inputs: days since last match A 819, B 14; matches on record A 8, B 676; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.044, surface_pool_high +0.047, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Andrej Martin vs Alexander Ritschard -- ATP Challenger Lisbon Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-19T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105413:106310:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrej Martin (`KXATPCHALLENGERMATCH-26OCT19MARRIT-MAR`) | 0.20 / 0.22 (898) | 21.0% | 22.2% | 15.5% | 22.0% [19.4%-25.2%] | 22.6% | -- | 22.6% | MODEL_LONE_OUTLIER | PASS | +1.2 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Alexander Ritschard (`KXATPCHALLENGERMATCH-26OCT19MARRIT-RIT`) | 0.78 / 0.79 (4) | 78.5% | 77.8% | 84.5% | 78.0% [74.8%-80.5%] | 77.4% | -- | 77.4% | MODEL_LONE_OUTLIER | PASS | -0.7 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 1496.0, B 1877.0; serve-point win A 57.8%, B 36.3%; Elo A 1593.4, B 1736.4; model uncertainty 0.029
* Form inputs: days since last match A 14, B 42; matches on record A 985, B 519; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.015, surface_dev_loose -0.019, surface_dev_tight +0.024
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; THIN_DISPLAYED_SIZE

## Pedro Rodenas vs Benjamin Hassan -- ATP Challenger Lisbon Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-19T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133975:210203:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benjamin Hassan (`KXATPCHALLENGERMATCH-26OCT19RODHAS-HAS`) | 0.63 / 0.64 (39) | 63.5% | 71.6% | 58.1% | 71.0% [67.9%-77.5%] | 62.5% | -- | 62.5% | MODEL_LONE_OUTLIER | PASS | +8.1 pp | NORMAL | FRESH | F / POOR | AGREES_WITH_KALSHI | AMBIGUOUS |
| Pedro Rodenas (`KXATPCHALLENGERMATCH-26OCT19RODHAS-ROD`) | 0.35 / 0.36 (5184) | 35.5% | 28.4% | 41.9% | 29.0% [22.5%-32.1%] | 37.5% | -- | 37.5% | MODEL_LONE_OUTLIER | PASS | -7.1 pp | NORMAL | FRESH | F / POOR | AGREES_WITH_KALSHI | AMBIGUOUS |

* Serve evidence (points): A 585.0, B 3395.0; serve-point win A 58.5%, B 37.0%; Elo A 1432.2, B 1630.9; model uncertainty 0.0479
* Form inputs: days since last match A 735, B 21; matches on record A 73, B 508; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.009, surface_dev_loose +0.001, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Matthew William Donald vs Javier Barranco Cosano -- ATP Challenger Florence Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 12:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-19T12:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200266:210054:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Javier Barranco Cosano (`KXATPCHALLENGERMATCH-26OCT19DONBAR-BAR`) | 0.38 / 0.39 (494) | 38.5% | 63.8% | 49.5% | 62.4% [54.8%-72.2%] | 41.6% | 38.8% | 38.8% | MODEL_LONE_OUTLIER | PASS | +25.4 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | EXTERNAL_STALE | VERIFIED |
| Matthew William Donald (`KXATPCHALLENGERMATCH-26OCT19DONBAR-DON`) | 0.59 / 0.60 (1) | 59.5% | 36.1% | 50.5% | 37.6% [27.8%-45.2%] | 58.4% | 61.6% | 61.6% | ALL_THREE_DISAGREE | PASS | -23.4 pp | HIGH_REVIEW | FRESH | B / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 667.0, B 1783.0; serve-point win A 55.6%, B 41.7%; Elo A 1341.1, B 1469.3; model uncertainty 0.0871
* Form inputs: days since last match A 21, B 14; matches on record A 128, B 530; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT19DONBAR-BAR  (YES = Javier Barranco Cosano)
Model: 64%
Kalshi: 38%
Gap: +25 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: EXTERNAL_STALE
Data quality: B (LIMITED)
Reasons: THIN_PLAYER_HISTORY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.063, surface_pool_high +0.061, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE

## Dmitry Popko vs Pierluigi Basile -- ATP Challenger Florence Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 12:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-19T12:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:122078:213003:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pierluigi Basile (`KXATPCHALLENGERMATCH-26OCT19POPBAS-BAS`) | 0.51 / 0.52 (81) | 51.5% | 35.8% | 39.4% | 36.9% [26.3%-45.4%] | -- | 52.1% | 52.1% | MODEL_LONE_OUTLIER | PASS | -15.7 pp | HIGH_REVIEW | FRESH | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Dmitry Popko (`KXATPCHALLENGERMATCH-26OCT19POPBAS-POP`) | 0.47 / 0.48 (399) | 47.5% | 64.2% | 60.6% | 63.1% [54.6%-73.7%] | -- | 48.1% | 48.1% | MODEL_LONE_OUTLIER | PASS | +16.7 pp | HIGH_REVIEW | FRESH | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2339.0, B 391.0; serve-point win A 62.3%, B 40.6%; Elo A 1566.0, B 1465.6; model uncertainty 0.0957
* Form inputs: days since last match A 105, B 168; matches on record A 799, B 21; data quality D

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT19POPBAS-POP  (YES = Dmitry Popko)
Model: 64%
Kalshi: 48%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.079, surface_pool_high -0.085, surface_dev_loose +0.000, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Yanaki Milev vs Maximus Jones -- ATP Challenger Florence Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-19T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210200:210382:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maximus Jones (`KXATPCHALLENGERMATCH-26OCT19MILJON-JON`) | 0.29 / 0.30 (648) | 29.5% | 49.3% | 52.6% | 47.9% [42.4%-50.5%] | 29.4% | 29.0% | 29.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +19.8 pp | HIGH_REVIEW | FRESH | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Yanaki Milev (`KXATPCHALLENGERMATCH-26OCT19MILJON-MIL`) | 0.70 / 0.71 (38) | 70.5% | 50.7% | 47.4% | 52.0% [49.5%-57.6%] | 70.6% | 70.7% | 70.6% | MODEL_LONE_OUTLIER | PASS | -19.8 pp | HIGH_REVIEW | FRESH | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1066.0, B 2348.0; serve-point win A 61.1%, B 39.1%; Elo A 1468.7, B 1426.9; model uncertainty 0.0407
* Form inputs: days since last match A 14, B 30; matches on record A 164, B 201; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT19MILJON-JON  (YES = Maximus Jones)
Model: 49%
Kalshi: 30%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: B (ADEQUATE)
Reasons: LOW_DISPLAYED_LIQUIDITY, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.015, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Sadio Doumbia / Bart Stevens vs Maximo Gonzalez / Andres Molteni -- ATP Brussels R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-19 13:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-19 12:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18DOUSTEGONMOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sadio Doumbia / Bart Stevens (`KXATPDOUBLES-26OCT18DOUSTEGONMOL-DOUSTE`) | 0.45 / 0.52 (44) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maximo Gonzalez / Andres Molteni (`KXATPDOUBLES-26OCT18DOUSTEGONMOL-GONMOL`) | 0.46 / 0.52 (86) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jaime Faria vs Felix Balshaw -- ATP Lyon R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-19 13:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-19 12:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:210262:213149:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felix Balshaw (`KXATPMATCH-26OCT18FARBAL-BAL`) | 0.40 / 0.41 (27) | 40.5% | 30.9% | 42.0% | 31.7% [24.1%-37.2%] | -- | -- | -- | -- | PASS | -9.6 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jaime Faria (`KXATPMATCH-26OCT18FARBAL-FAR`) | 0.60 / 0.61 (77477) | 60.5% | 69.1% | 58.0% | 68.3% [62.8%-75.9%] | -- | -- | -- | -- | WATCH | +8.6 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4745.0, B 1807.0; serve-point win A 65.4%, B 38.6%; Elo A 1800.9, B 1569.3; model uncertainty 0.0658
* Form inputs: days since last match A 11, B 13; matches on record A 312, B 44; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.022, surface_pool_high -0.023, surface_dev_loose -0.005, surface_dev_tight -0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT18FARBAL-BAL2` Will Felix Balshaw win at least 1.5 more games than Jaime Faria?: 0.32/0.37 mid 34.5%, model 24.6% (projection_v2.0 (prediction ledger)) -- gap -9.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18FARBAL-FAR3` Will Jaime Faria win at least 2.5 more games than Felix Balshaw?: 0.45/0.46 mid 45.5%, model 54.7% (projection_v2.0 (prediction ledger)) -- gap +9.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18FARBAL-BAL20` Will Felix Balshaw win the Jaime Faria vs Felix Balshaw match by a set score of 2-0?: 0.20/0.23 mid 21.5%, model 13.7% (projection_v2.0 (prediction ledger)) -- gap -7.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18FARBAL-1-FAR` Will Jaime Faria win set 1 in the Jaime Faria vs Felix Balshaw match: 0.55/0.57 mid 56.0%, model 63.0% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18FARBAL-28` Over 27.5 games: 0.29/0.34 mid 31.5%, model 37.4% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18FARBAL-FAR21` Will Jaime Faria win the Jaime Faria vs Felix Balshaw match by a set score of 2-1?: 0.22/0.25 mid 23.5%, model 29.4% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18FARBAL-1-BAL` Will Felix Balshaw win set 1 in the Jaime Faria vs Felix Balshaw match: 0.41/0.44 mid 42.5%, model 37.0% (projection_v2.0 (prediction ledger)) -- gap -5.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18FARBAL-2-FAR` Will Jaime Faria win set 2 in the Jaime Faria vs Felix Balshaw match: 0.56/0.59 mid 57.5%, model 63.0% (projection_v2.0 (prediction ledger)) -- gap +5.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT18FARBAL-FAR6` Will Jaime Faria win at least 5.5 more games than Felix Balshaw?: 0.14/0.30 mid 22.0%, model 17.3% (projection_v2.0 (prediction ledger)) -- gap -4.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18FARBAL-2-BAL` Will Felix Balshaw win set 2 in the Jaime Faria vs Felix Balshaw match: 0.40/0.43 mid 41.5%, model 37.0% (projection_v2.0 (prediction ledger)) -- gap -4.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18FARBAL-FAR20` Will Jaime Faria win the Jaime Faria vs Felix Balshaw match by a set score of 2-0?: 0.34/0.38 mid 36.0%, model 39.7% (projection_v2.0 (prediction ledger)) -- gap +3.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18FARBAL-23` Over 22.5 games: 0.55/0.56 mid 55.5%, model 57.2% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18FARBAL-BAL21` Will Felix Balshaw win the Jaime Faria vs Felix Balshaw match by a set score of 2-1?: 0.17/0.19 mid 18.0%, model 17.2% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18FARBAL-18` Over 17.5 games: 0.88/0.94 mid 91.0%, model 91.6% (projection_v2.0 (prediction ledger)) -- gap +0.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Julian Cash / Lloyd Glasspool vs Miguel Angel Reyes-Varela / Reese Stalder -- ATP Lyon R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-19 11:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-19 13:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-19 12:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-19T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19CASGLAREYSTA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julian Cash / Lloyd Glasspool (`KXATPDOUBLES-26OCT19CASGLAREYSTA-CASGLA`) | 0.80 / 0.82 (196) | 81.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Miguel Angel Reyes-Varela / Reese Stalder (`KXATPDOUBLES-26OCT19CASGLAREYSTA-REYSTA`) | 0.16 / 0.20 (10) | 18.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Coleman Wong vs Jake Delaney -- ATP Challenger Guangzhou Nansha R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-19T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:117359:209409:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jake Delaney (`KXATPCHALLENGERMATCH-26OCT19WONDEL-DEL`) | 0.09 / 0.10 (16386) | 9.5% | 9.7% | 11.6% | 10.7% [9.8%-11.8%] | -- | 8.7% | 8.7% | MODEL_LONE_OUTLIER | PASS | +0.2 pp | NORMAL | FRESH | B / LIMITED | ALL_AGREE | VERIFIED |
| Coleman Wong (`KXATPCHALLENGERMATCH-26OCT19WONDEL-WON`) | 0.91 / 0.92 (12023) | 91.5% | 90.3% | 88.4% | 89.3% [88.2%-90.2%] | -- | 91.8% | 91.8% | MODEL_LONE_OUTLIER | PASS | -1.2 pp | NORMAL | FRESH | B / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4541.0, B 901.0; serve-point win A 74.9%, B 36.2%; Elo A 1723.4, B 1347.1; model uncertainty 0.0097
* Form inputs: days since last match A 22, B 27; matches on record A 289, B 256; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.002, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Diogo Morais vs Carlo Alberto Caniato -- ATP Challenger Lisbon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 13:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-19T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211587:212241:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlo Alberto Caniato (`KXATPCHALLENGERMATCH-26OCT19MORCAN-CAN`) | 0.93 / 0.94 (841) | 93.5% | 86.3% | 83.9% | 75.6% [73.2%-77.9%] | -- | 94.0% | 94.0% | MODEL_LONE_OUTLIER | PASS | -7.2 pp | NORMAL | FRESH | F / POOR | AGREES_WITH_KALSHI | AMBIGUOUS |
| Diogo Morais (`KXATPCHALLENGERMATCH-26OCT19MORCAN-MOR`) | 0.06 / 0.07 (5798) | 6.5% | 13.7% | 16.1% | 24.4% [22.1%-26.8%] | -- | 6.1% | 6.1% | MODEL_LONE_OUTLIER | PASS | +7.2 pp | NORMAL | FRESH | F / POOR | AGREES_WITH_KALSHI | AMBIGUOUS |

* Serve evidence (points): A 58.0, B 1491.0; serve-point win A 60.1%, B 31.1%; Elo A 1283.3, B 1471.8; model uncertainty 0.0233
* Form inputs: days since last match A 791, B 14; matches on record A 7, B 88; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.024, surface_pool_high -0.015, surface_dev_loose +0.000, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Patrick Schoen vs Svyatoslav Gulin -- ATP Challenger Lisbon Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 13:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-19T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210425:211566:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Svyatoslav Gulin (`KXATPCHALLENGERMATCH-26OCT19SCHGUL-GUL`) | 0.54 / 0.55 (1061) | 54.5% | 62.2% | 57.8% | 67.1% [63.3%-69.4%] | 54.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +7.7 pp | NORMAL | FRESH | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Patrick Schoen (`KXATPCHALLENGERMATCH-26OCT19SCHGUL-SCH`) | 0.44 / 0.46 (9752) | 45.0% | 37.8% | 42.2% | 32.9% [30.6%-36.7%] | 45.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.2 pp | NORMAL | FRESH | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 156.0, B 1022.0; serve-point win A 57.8%, B 39.9%; Elo A 1399.8, B 1527.1; model uncertainty 0.0309
* Form inputs: days since last match A 14, B 42; matches on record A 40, B 186; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.038, surface_pool_high -0.023, surface_dev_loose -0.001, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE

## Carlos Taberner vs Oleksii Krutykh -- ATP Challenger Lisbon Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 13:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-19T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126535:208071:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oleksii Krutykh (`KXATPCHALLENGERMATCH-26OCT19TABKRU-KRU`) | 0.34 / 0.36 (1389) | 35.0% | 29.1% | 36.2% | 30.5% [28.3%-32.4%] | 35.4% | -- | 35.4% | MARKETS_AGREE | PASS | -5.9 pp | NORMAL | FRESH | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Carlos Taberner (`KXATPCHALLENGERMATCH-26OCT19TABKRU-TAB`) | 0.64 / 0.65 (461) | 64.5% | 70.9% | 63.8% | 69.5% [67.6%-71.7%] | 64.6% | -- | 64.6% | MARKETS_AGREE | WATCH | +6.4 pp | NORMAL | FRESH | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3887.0, B 1292.0; serve-point win A 60.8%, B 43.5%; Elo A 1700.1, B 1513.5; model uncertainty 0.0205
* Form inputs: days since last match A 21, B 14; matches on record A 721, B 404; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.022, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Miguel Damas vs Samuele Pieri -- ATP Challenger Florence R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 13:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-19T13:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207732:210129:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miguel Damas (`KXATPCHALLENGERMATCH-26OCT19DAMPIE-DAM`) | 0.52 / 0.53 (53) | 52.5% | 52.3% | 41.2% | 48.9% [44.2%-56.2%] | -- | 52.8% | 52.8% | MODEL_LONE_OUTLIER | PASS | -0.2 pp | NORMAL | FRESH | B / ADEQUATE | ALL_AGREE | VERIFIED |
| Samuele Pieri (`KXATPCHALLENGERMATCH-26OCT19DAMPIE-PIE`) | 0.47 / 0.48 (3810) | 47.5% | 47.7% | 58.8% | 51.0% [43.8%-55.8%] | -- | 47.9% | 47.9% | MODEL_LONE_OUTLIER | WATCH | +0.2 pp | NORMAL | FRESH | B / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 2818.0, B 1377.0; serve-point win A 58.2%, B 42.2%; Elo A 1435.3, B 1389.4; model uncertainty 0.0599
* Form inputs: days since last match A 14, B 14; matches on record A 293, B 119; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.031, surface_pool_high -0.031, surface_dev_loose -0.005, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Zdenek Kolar vs Federico Bondioli -- ATP Challenger Florence R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 13:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-19T13:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144645:210682:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Federico Bondioli (`KXATPCHALLENGERMATCH-26OCT19KOLBON-BON`) | 0.42 / 0.43 (17453) | 42.5% | 34.0% | 25.4% | 29.3% [27.1%-32.1%] | -- | 41.9% | 41.9% | MODEL_LONE_OUTLIER | PASS | -8.5 pp | NORMAL | FRESH | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Zdenek Kolar (`KXATPCHALLENGERMATCH-26OCT19KOLBON-KOL`) | 0.58 / 0.59 (602) | 58.5% | 66.0% | 74.6% | 70.7% [67.9%-72.9%] | -- | 58.2% | 58.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +7.5 pp | NORMAL | FRESH | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3944.0, B 797.0; serve-point win A 61.2%, B 42.0%; Elo A 1546.7, B 1416.1; model uncertainty 0.0249
* Form inputs: days since last match A 14, B 121; matches on record A 769, B 99; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.004, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Andrea Guerrieri vs Alex Michelsen -- ATP Brussels R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-19 16:30Z
* Current expected start: 2026-10-19 13:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-19 12:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-19T16:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200462:210506:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea Guerrieri (`KXATPMATCH-26OCT19GUEMIC-GUE`) | 0.19 / 0.20 (7000) | 19.5% | 13.2% | 12.3% | 11.1% [10.6%-12.2%] | 18.2% | -- | 18.2% | MODEL_LONE_OUTLIER | PASS | -6.3 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Alex Michelsen (`KXATPMATCH-26OCT19GUEMIC-MIC`) | 0.79 / 0.80 (248) | 79.5% | 86.8% | 87.7% | 88.9% [87.8%-89.4%] | 81.8% | -- | 81.8% | KALSHI_LONE_OUTLIER | SHADOW_BET | +7.3 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2272.0, B 5402.0; serve-point win A 57.3%, B 33.9%; Elo A 1570.7, B 1958.0; model uncertainty 0.0077
* Form inputs: days since last match A 2, B 9; matches on record A 346, B 303; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.001, surface_dev_tight +0.002
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT19GUEMIC-MIC21` Will Alex Michelsen win the Andrea Guerrieri vs Alex Michelsen match by a set score of 2-1?: 0.22/0.23 mid 22.5%, model 27.2% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT19GUEMIC-GUE20` Will Andrea Guerrieri win the Andrea Guerrieri vs Alex Michelsen match by a set score of 2-0?: 0.08/0.10 mid 9.0%, model 5.2% (projection_v2.0 (prediction ledger)) -- gap -3.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT19GUEMIC-2-MIC` Will Alex Michelsen win set 2 in the Andrea Guerrieri vs Alex Michelsen match: 0.73/0.77 mid 75.0%, model 77.2% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT19GUEMIC-1-GUE` Will Andrea Guerrieri win set 1 in the Andrea Guerrieri vs Alex Michelsen match: 0.24/0.25 mid 24.5%, model 22.8% (projection_v2.0 (prediction ledger)) -- gap -1.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT19GUEMIC-1-MIC` Will Alex Michelsen win set 1 in the Andrea Guerrieri vs Alex Michelsen match: 0.75/0.76 mid 75.5%, model 77.2% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT19GUEMIC-2-GUE` Will Andrea Guerrieri win set 2 in the Andrea Guerrieri vs Alex Michelsen match: 0.23/0.25 mid 24.0%, model 22.8% (projection_v2.0 (prediction ledger)) -- gap -1.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT19GUEMIC-MIC20` Will Alex Michelsen win the Andrea Guerrieri vs Alex Michelsen match by a set score of 2-0?: 0.58/0.59 mid 58.5%, model 59.6% (projection_v2.0 (prediction ledger)) -- gap +1.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT19GUEMIC-GUE21` Will Andrea Guerrieri win the Andrea Guerrieri vs Alex Michelsen match by a set score of 2-1?: 0.08/0.10 mid 9.0%, model 8.0% (projection_v2.0 (prediction ledger)) -- gap -1.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE

## Alexander Chang vs Tommaso Bardocci -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19CHABAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tommaso Bardocci (`KXITFMATCH-26OCT19CHABAR-BAR`) | -- / 0.01 (5470) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander Chang (`KXITFMATCH-26OCT19CHABAR-CHA`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Riccardo DI VITA vs Gabriele Maria Piano -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19DIVPIA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Riccardo DI VITA (`KXITFMATCH-26OCT19DIVPIA-DIV`) | 0.77 / 0.79 (3686) | 78.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gabriele Maria Piano (`KXITFMATCH-26OCT19DIVPIA-PIA`) | 0.21 / 0.22 (4) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leonardo Iemmi vs Carlo Cataldi -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19IEMCAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlo Cataldi (`KXITFMATCH-26OCT19IEMCAT-CAT`) | 0.04 / 0.08 (20) | 6.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leonardo Iemmi (`KXITFMATCH-26OCT19IEMCAT-IEM`) | 0.87 / 0.95 (89) | 91.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Simone Macchione vs Adriano Botta -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19MACBOT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adriano Botta (`KXITFMATCH-26OCT19MACBOT-BOT`) | 0.15 / 0.19 (39) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Simone Macchione (`KXITFMATCH-26OCT19MACBOT-MAC`) | 0.80 / 0.84 (2) | 82.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Noah Perfetti vs Giulio Stella -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19PERSTE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Noah Perfetti (`KXITFMATCH-26OCT19PERSTE-PER`) | 0.30 / 0.32 (139) | 31.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Giulio Stella (`KXITFMATCH-26OCT19PERSTE-STE`) | 0.69 / 0.71 (119) | 70.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Edouard Villoslada vs Romeo Spinolo -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19VILSPI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Romeo Spinolo (`KXITFMATCH-26OCT19VILSPI-SPI`) | 0.67 / 0.68 (615) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Edouard Villoslada (`KXITFMATCH-26OCT19VILSPI-VIL`) | 0.32 / 0.33 (18) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Michael Wright vs Boris Sarritzu -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19WRISAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Boris Sarritzu (`KXITFMATCH-26OCT19WRISAR-SAR`) | 0.52 / 0.53 (3918) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Michael Wright (`KXITFMATCH-26OCT19WRISAR-WRI`) | 0.47 / 0.48 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Franco Agamenone vs Max Houkes -- ATP Challenger Florence R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 13:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-19T13:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106162:208069:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Franco Agamenone (`KXATPCHALLENGERMATCH-26OCT19AGAHOU-AGA`) | 0.29 / 0.30 (26194) | 29.5% | 34.0% | 22.8% | 33.3% [28.6%-47.9%] | -- | 27.8% | 27.8% | MODEL_LONE_OUTLIER | WATCH | +4.5 pp | NORMAL | FRESH | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Max Houkes (`KXATPCHALLENGERMATCH-26OCT19AGAHOU-HOU`) | 0.72 / 0.73 (13698) | 72.5% | 66.0% | 77.2% | 66.7% [52.1%-71.4%] | -- | 72.8% | 72.8% | MODEL_LONE_OUTLIER | PASS | -6.5 pp | NORMAL | FRESH | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3366.0, B 1822.0; serve-point win A 56.7%, B 40.1%; Elo A 1479.9, B 1492.7; model uncertainty 0.0964
* Form inputs: days since last match A 35, B 119; matches on record A 645, B 275; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose -0.023, surface_dev_tight +0.029
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Thomas Gerbaud vs Hugo Pierre -- M25 Sarreguemines R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:145008:212840:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thomas Gerbaud (`KXITFMATCH-26OCT19GERPIE-GER`) | 0.56 / 0.57 (1) | 56.5% | 46.5% | 50.0% | 61.0% [61.0%-61.0%] | -- | -- | -- | -- | PASS | -10.0 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Hugo Pierre (`KXITFMATCH-26OCT19GERPIE-PIE`) | 0.42 / 0.43 (1522) | 42.5% | 53.5% | 50.0% | 39.0% [39.0%-39.0%] | -- | -- | -- | -- | PASS | +11.0 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 61.6%, B 37.7%; Elo A 1236.9, B 1159.2; model uncertainty 0.0
* Form inputs: days since last match A 784, B 679; matches on record A 9, B 43; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adrien Gobat vs Martin Riu -- M25 Sarreguemines R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19GOBRIU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrien Gobat (`KXITFMATCH-26OCT19GOBRIU-GOB`) | 0.94 / 0.95 (2388) | 94.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Martin Riu (`KXITFMATCH-26OCT19GOBRIU-RIU`) | 0.05 / 0.06 (512) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elijah Sanogo vs Antoine Walch -- M25 Sarreguemines R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126505:tml:S1EZ:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elijah Sanogo (`KXITFMATCH-26OCT19SANWAL-SAN`) | 0.77 / 0.79 (3753) | 78.0% | 67.8% | 34.1% | 72.2% [72.2%-72.2%] | -- | -- | -- | -- | PASS | -10.2 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Antoine Walch (`KXITFMATCH-26OCT19SANWAL-WAL`) | 0.21 / 0.22 (2) | 21.5% | 32.2% | 65.9% | 27.8% [27.8%-27.9%] | -- | -- | -- | -- | PASS | +10.7 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 182.0, B 0.0; serve-point win A 63.0%, B 40.6%; Elo A 1372.5, B 1201.8; model uncertainty 0.0004
* Form inputs: days since last match A 168, B 819; matches on record A 3, B 65; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Isabella Angelina Abendroth vs Vladlena Bokova -- W15 Karlovy Vary R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19ABEBOK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isabella Angelina Abendroth (`KXITFWMATCH-26OCT19ABEBOK-ABE`) | 0.67 / 0.69 (8) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vladlena Bokova (`KXITFWMATCH-26OCT19ABEBOK-BOK`) | 0.29 / 0.36 (6) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stefanie Auer vs Pavla Sviglerova -- W15 Karlovy Vary R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19AUESVI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefanie Auer (`KXITFWMATCH-26OCT19AUESVI-AUE`) | 0.06 / 0.07 (2642) | 6.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pavla Sviglerova (`KXITFWMATCH-26OCT19AUESVI-SVI`) | 0.93 / 0.94 (2440) | 93.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oliwia Drozdz vs Nadia Kulbiej -- W15 Karlovy Vary R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:270100:270332:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oliwia Drozdz (`KXITFWMATCH-26OCT19DROKUL-DRO`) | 0.29 / 0.30 (12) | 29.5% | 16.6% | 29.3% | 28.0% [27.6%-28.4%] | -- | -- | -- | -- | PASS | -12.9 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nadia Kulbiej (`KXITFWMATCH-26OCT19DROKUL-KUL`) | 0.70 / 0.71 (2) | 70.5% | 83.4% | 70.7% | 72.0% [71.6%-72.5%] | -- | -- | -- | -- | PASS | +12.9 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 58.0, B 680.0; serve-point win A 52.0%, B 40.7%; Elo A 1254.9, B 1417.9; model uncertainty 0.004
* Form inputs: days since last match A 350, B 490; matches on record A 1, B 10; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lucia Llinares Domingo vs Lucia Ros Parres -- W15 Villena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-19T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221197:260668:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucia Llinares Domingo (`KXITFWMATCH-26OCT19LLIROS-LLI`) | 0.69 / 0.70 (2048) | 69.5% | 41.3% | 15.4% | 44.7% [35.4%-53.7%] | -- | -- | -- | -- | PASS | -28.2 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lucia Ros Parres (`KXITFWMATCH-26OCT19LLIROS-ROS`) | 0.30 / 0.31 (1) | 30.5% | 58.7% | 84.6% | 55.3% [46.3%-64.6%] | -- | -- | -- | -- | PASS | +28.2 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 652.0, B 375.0; serve-point win A 51.6%, B 46.8%; Elo A 1314.4, B 1291.8; model uncertainty 0.0919
* Form inputs: days since last match A 399, B 322; matches on record A 195, B 43; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT19LLIROS-ROS  (YES = Lucia Ros Parres)
Model: 59%
Kalshi: 30%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.011, surface_dev_loose -0.016, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Montesinos Vilanova vs Maria Pares Bergnes de las Casas -- W15 Villena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-19T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:269696:270492:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Montesinos Vilanova (`KXITFWMATCH-26OCT19MONPAR-MON`) | 0.75 / 0.76 (1) | 75.5% | 26.7% | 47.3% | 37.4% [36.4%-37.5%] | -- | -- | -- | -- | PASS | -48.8 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Maria Pares Bergnes de las Casas (`KXITFWMATCH-26OCT19MONPAR-PAR`) | 0.21 / 0.24 (12) | 22.5% | 73.3% | 52.7% | 62.6% [62.5%-63.6%] | -- | -- | -- | -- | PASS | +50.8 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 92.0, B 161.0; serve-point win A 52.2%, B 43.1%; Elo A 1203.9, B 1298.1; model uncertainty 0.0053
* Form inputs: days since last match A 322, B 175; matches on record A 6, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT19MONPAR-PAR  (YES = Maria Pares Bergnes de las Casas)
Model: 73%
Kalshi: 22%
Gap: +51 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maria Paredes Perez vs Olga Bienzobas Fernandez Sancho -- W15 Villena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-19T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:233721:240163:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Olga Bienzobas Fernandez Sancho (`KXITFWMATCH-26OCT19PARBIE-BIE`) | 0.62 / 0.65 (3766) | 63.5% | 42.2% | 18.2% | 39.0% [36.5%-40.5%] | -- | -- | -- | -- | PASS | -21.3 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Maria Paredes Perez (`KXITFWMATCH-26OCT19PARBIE-PAR`) | 0.37 / 0.38 (2684) | 37.5% | 57.8% | 81.8% | 61.0% [59.5%-63.5%] | -- | -- | -- | -- | PASS | +20.3 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 89.0, B 244.0; serve-point win A 55.1%, B 46.4%; Elo A 1225.3, B 1155.9; model uncertainty 0.0202
* Form inputs: days since last match A 469, B 392; matches on record A 6, B 9; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT19PARBIE-PAR  (YES = Maria Paredes Perez)
Model: 58%
Kalshi: 38%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Freya Peet vs Carla Guerrero Calvo -- W15 Villena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19PEEGUE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carla Guerrero Calvo (`KXITFWMATCH-26OCT19PEEGUE-GUE`) | 0.35 / 0.38 (2) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Freya Peet (`KXITFWMATCH-26OCT19PEEGUE-PEE`) | 0.62 / 0.64 (280) | 63.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alejo Sanchez Quilez vs Kai Wehnelt -- ATP Challenger Lisbon Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 14:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-19T14:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132999:211639:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alejo Sanchez Quilez (`KXATPCHALLENGERMATCH-26OCT19SANWEH-SAN`) | 0.72 / 0.73 (462) | 72.5% | 66.5% | 59.6% | 61.1% [58.1%-64.5%] | 71.1% | 72.8% | 72.8% | MODEL_LONE_OUTLIER | PASS | -6.0 pp | NORMAL | FRESH | B / LIMITED | EXTERNAL_STALE | VERIFIED |
| Kai Wehnelt (`KXATPCHALLENGERMATCH-26OCT19SANWEH-WEH`) | 0.26 / 0.28 (4) | 27.0% | 33.5% | 40.4% | 38.9% [35.5%-41.9%] | 28.9% | 27.5% | 27.5% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.5 pp | NORMAL | FRESH | B / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 1220.0, B 662.0; serve-point win A 62.6%, B 40.7%; Elo A 1435.5, B 1353.8; model uncertainty 0.0318
* Form inputs: days since last match A 14, B 35; matches on record A 113, B 356; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.029, surface_pool_high -0.030, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE

## Matteo Arnaldi vs Lorenzo Musetti -- ATP Lyon R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-19 14:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-19 13:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207518:208286:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Arnaldi (`KXATPMATCH-26OCT18ARNMUS-ARN`) | 0.34 / 0.35 (36125) | 34.5% | 30.2% | 31.7% | 29.9% [29.0%-30.8%] | -- | -- | -- | -- | PASS | -4.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lorenzo Musetti (`KXATPMATCH-26OCT18ARNMUS-MUS`) | 0.65 / 0.66 (368) | 65.5% | 69.8% | 68.3% | 70.1% [69.2%-71.0%] | -- | -- | -- | -- | SHADOW_BET | +4.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4135.0, B 4676.0; serve-point win A 58.4%, B 37.5%; Elo A 1915.4, B 2101.7; model uncertainty 0.0091
* Form inputs: days since last match A 8, B 9; matches on record A 385, B 466; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high -0.000, surface_dev_loose +0.004, surface_dev_tight -0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18ARNMUS-22` Over 21.5 games: 0.53/0.54 mid 53.5%, model 61.7% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18ARNMUS-27` Over 26.5 games: 0.30/0.35 mid 32.5%, model 38.6% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18ARNMUS-MUS21` Will Lorenzo Musetti win the Matteo Arnaldi vs Lorenzo Musetti match by a set score of 2-1?: 0.23/0.25 mid 24.0%, model 29.4% (projection_v2.0 (prediction ledger)) -- gap +5.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18ARNMUS-ARN2` Will Matteo Arnaldi win at least 1.5 more games than Lorenzo Musetti?: 0.28/0.29 mid 28.5%, model 24.2% (projection_v2.0 (prediction ledger)) -- gap -4.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18ARNMUS-ARN20` Will Matteo Arnaldi win the Matteo Arnaldi vs Lorenzo Musetti match by a set score of 2-0?: 0.16/0.19 mid 17.5%, model 13.3% (projection_v2.0 (prediction ledger)) -- gap -4.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18ARNMUS-MUS7` Will Lorenzo Musetti win at least 6.5 more games than Matteo Arnaldi?: 0.02/0.16 mid 9.0%, model 12.2% (projection_v2.0 (prediction ledger)) -- gap +3.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ARNMUS-1-ARN` Will Matteo Arnaldi win set 1 in the Matteo Arnaldi vs Lorenzo Musetti match: 0.38/0.40 mid 39.0%, model 36.4% (projection_v2.0 (prediction ledger)) -- gap -2.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ARNMUS-1-MUS` Will Lorenzo Musetti win set 1 in the Matteo Arnaldi vs Lorenzo Musetti match: 0.60/0.62 mid 61.0%, model 63.5% (projection_v2.0 (prediction ledger)) -- gap +2.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18ARNMUS-MUS20` Will Lorenzo Musetti win the Matteo Arnaldi vs Lorenzo Musetti match by a set score of 2-0?: 0.41/0.43 mid 42.0%, model 40.4% (projection_v2.0 (prediction ledger)) -- gap -1.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18ARNMUS-MUS4` Will Lorenzo Musetti win at least 3.5 more games than Matteo Arnaldi?: 0.45/0.47 mid 46.0%, model 47.0% (projection_v2.0 (prediction ledger)) -- gap +1.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18ARNMUS-ARN21` Will Matteo Arnaldi win the Matteo Arnaldi vs Lorenzo Musetti match by a set score of 2-1?: 0.15/0.17 mid 16.0%, model 16.9% (projection_v2.0 (prediction ledger)) -- gap +0.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ARNMUS-2-ARN` Will Matteo Arnaldi win set 2 in the Matteo Arnaldi vs Lorenzo Musetti match: 0.35/0.39 mid 37.0%, model 36.4% (projection_v2.0 (prediction ledger)) -- gap -0.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ARNMUS-2-MUS` Will Lorenzo Musetti win set 2 in the Matteo Arnaldi vs Lorenzo Musetti match: 0.61/0.65 mid 63.0%, model 63.5% (projection_v2.0 (prediction ledger)) -- gap +0.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18ARNMUS-17` Over 16.5 games: 0.92/0.97 mid 94.5%, model 94.4% (projection_v2.0 (prediction ledger)) -- gap -0.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Trey Hilderbrand / Stefan Latinovic vs Ariel Behar / Joshua Paris -- ATP Lyon R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-19 11:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-19 14:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-19 13:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-19T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19HILLATBEHPAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ariel Behar / Joshua Paris (`KXATPDOUBLES-26OCT19HILLATBEHPAR-BEHPAR`) | 0.51 / 0.54 (21) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Trey Hilderbrand / Stefan Latinovic (`KXATPDOUBLES-26OCT19HILLATBEHPAR-HILLAT`) | 0.44 / 0.47 (11) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Mikhail Kukushkin vs Stefanos Sakellaridis -- ATP Almaty R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-19 17:30Z
* Current expected start: 2026-10-19 14:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-19 13:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-19T17:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105062:208852:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mikhail Kukushkin (`KXATPMATCH-26OCT19KUKSAK-KUK`) | 0.28 / 0.29 (30313) | 28.5% | 46.4% | 53.9% | 55.4% [54.9%-56.9%] | 29.9% | -- | 29.9% | MODEL_LONE_OUTLIER | WATCH | +17.9 pp | HIGH_REVIEW | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Stefanos Sakellaridis (`KXATPMATCH-26OCT19KUKSAK-SAK`) | 0.72 / 0.73 (131454) | 72.5% | 53.6% | 46.1% | 44.6% [43.1%-45.1%] | 70.1% | -- | 70.1% | KALSHI_LONE_OUTLIER | PASS | -18.9 pp | HIGH_REVIEW | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4018.0, B 3408.0; serve-point win A 64.4%, B 34.9%; Elo A 1679.5, B 1609.1; model uncertainty 0.0098
* Form inputs: days since last match A 121, B 2; matches on record A 1127, B 322; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT19KUKSAK-KUK  (YES = Mikhail Kukushkin)
Model: 46%
Kalshi: 28%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: A (LIMITED)
Reasons: STALE_PLAYER_DATA, EXTERNAL_MARKET_REJECTION
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.005, surface_dev_loose -0.000, surface_dev_tight +0.005
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT19KUKSAK-SAK20` Will Stefanos Sakellaridis win the Mikhail Kukushkin vs Stefanos Sakellaridis match by a set score of 2-0?: 0.50/0.51 mid 50.5%, model 27.4% (projection_v2.0 (prediction ledger)) -- gap -23.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPSETWINNER-26OCT19KUKSAK-1-KUK` Will Mikhail Kukushkin win set 1 in the Mikhail Kukushkin vs Stefanos Sakellaridis match: 0.30/0.34 mid 32.0%, model 47.6% (projection_v2.0 (prediction ledger)) -- gap +15.6 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT19KUKSAK-2-KUK` Will Mikhail Kukushkin win set 2 in the Mikhail Kukushkin vs Stefanos Sakellaridis match: 0.30/0.34 mid 32.0%, model 47.6% (projection_v2.0 (prediction ledger)) -- gap +15.6 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT19KUKSAK-1-SAK` Will Stefanos Sakellaridis win set 1 in the Mikhail Kukushkin vs Stefanos Sakellaridis match: 0.66/0.69 mid 67.5%, model 52.4% (projection_v2.0 (prediction ledger)) -- gap -15.1 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT19KUKSAK-2-SAK` Will Stefanos Sakellaridis win set 2 in the Mikhail Kukushkin vs Stefanos Sakellaridis match: 0.66/0.69 mid 67.5%, model 52.4% (projection_v2.0 (prediction ledger)) -- gap -15.1 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPEXACTMATCH-26OCT19KUKSAK-KUK21` Will Mikhail Kukushkin win the Mikhail Kukushkin vs Stefanos Sakellaridis match by a set score of 2-1?: 0.12/0.14 mid 13.0%, model 23.8% (projection_v2.0 (prediction ledger)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26OCT19KUKSAK-KUK20` Will Mikhail Kukushkin win the Mikhail Kukushkin vs Stefanos Sakellaridis match by a set score of 2-0?: 0.13/0.15 mid 14.0%, model 22.7% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26OCT19KUKSAK-SAK21` Will Stefanos Sakellaridis win the Mikhail Kukushkin vs Stefanos Sakellaridis match by a set score of 2-1?: 0.20/0.24 mid 22.0%, model 26.1% (projection_v2.0 (prediction ledger)) -- gap +4.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED

## Francesco Forti vs Jonas Forejtek -- ATP Challenger Florence R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-19T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207797:209506:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesco Forti (`KXATPCHALLENGERMATCH-26OCT19FORFOR2-FOR`) | 0.41 / 0.42 (6844) | 41.5% | 47.0% | 57.0% | 52.5% [48.5%-54.5%] | -- | 41.9% | 41.9% | MODEL_LONE_OUTLIER | SHADOW_BET | +5.5 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Jonas Forejtek (`KXATPCHALLENGERMATCH-26OCT19FORFOR2-FOR2`) | 0.58 / 0.59 (927) | 58.5% | 53.0% | 43.0% | 47.5% [45.5%-51.5%] | -- | 58.2% | 58.2% | MODEL_LONE_OUTLIER | PASS | -5.5 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1905.0, B 2857.0; serve-point win A 63.0%, B 36.4%; Elo A 1498.6, B 1524.8; model uncertainty 0.0301
* Form inputs: days since last match A 28, B 14; matches on record A 372, B 354; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.015, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Michele Ribecai vs Jacopo Vasami -- ATP Challenger Florence R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-19T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212020:213635:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michele Ribecai (`KXATPCHALLENGERMATCH-26OCT19RIBVAS-RIB`) | 0.57 / 0.58 (6940) | 57.5% | 78.0% | 53.6% | 65.1% [62.2%-67.9%] | -- | 58.8% | 58.8% | MODEL_LONE_OUTLIER | PASS | +20.5 pp | HIGH_REVIEW | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Jacopo Vasami (`KXATPCHALLENGERMATCH-26OCT19RIBVAS-VAS`) | 0.42 / 0.43 (76) | 42.5% | 22.0% | 46.4% | 34.9% [32.1%-37.8%] | -- | 41.2% | 41.2% | MODEL_LONE_OUTLIER | PASS | -20.5 pp | HIGH_REVIEW | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2063.0, B 0.0; serve-point win A 63.2%, B 42.8%; Elo A 1448.7, B 1340.5; model uncertainty 0.0287
* Form inputs: days since last match A 14, B 168; matches on record A 95, B 5; data quality F

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT19RIBVAS-RIB  (YES = Michele Ribecai)
Model: 78%
Kalshi: 57%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.028, surface_pool_high -0.029, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Raphael Collignon / David Goffin vs Marc Polmans / Jan Zielinski -- ATP Brussels R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-19 15:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-19 14:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18COLGOFPOLZIE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raphael Collignon / David Goffin (`KXATPDOUBLES-26OCT18COLGOFPOLZIE-COLGOF`) | 0.13 / 0.16 (25) | 14.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marc Polmans / Jan Zielinski (`KXATPDOUBLES-26OCT18COLGOFPOLZIE-POLZIE`) | 0.84 / 0.85 (200) | 84.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Arthur Bellegy vs Davide Ciaschetti -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19BELCIA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arthur Bellegy (`KXITFMATCH-26OCT19BELCIA-BEL`) | 0.47 / 0.48 (48) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Davide Ciaschetti (`KXITFMATCH-26OCT19BELCIA-CIA`) | 0.44 / 0.49 (32) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dali Blanch vs Henrique Rocha -- ATP Challenger Lisbon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-19T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209898:210012:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dali Blanch (`KXATPCHALLENGERMATCH-26OCT19BLAROC-BLA`) | 0.23 / 0.24 (642) | 23.5% | 27.6% | 35.8% | 30.6% [25.0%-33.8%] | -- | 23.6% | 23.6% | MODEL_LONE_OUTLIER | WATCH | +4.1 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Henrique Rocha (`KXATPCHALLENGERMATCH-26OCT19BLAROC-ROC`) | 0.75 / 0.77 (886) | 76.0% | 72.4% | 64.2% | 69.4% [66.2%-75.0%] | -- | 76.7% | 76.7% | MODEL_LONE_OUTLIER | PASS | -3.6 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 2080.0, B 3638.0; serve-point win A 56.9%, B 38.5%; Elo A 1478.6, B 1680.4; model uncertainty 0.0442
* Form inputs: days since last match A 14, B 21; matches on record A 217, B 286; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.027, surface_pool_high +0.028, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Kenny De Schepper vs Timeo Trufelli -- M25 Sarreguemines R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19DESTRU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kenny De Schepper (`KXITFMATCH-26OCT19DESTRU-DES`) | 0.61 / 0.66 (28) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Timeo Trufelli (`KXITFMATCH-26OCT19DESTRU-TRU`) | 0.31 / 0.36 (31) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Christian Djonov vs Remy Dugardin -- M25 Sarreguemines R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19DJODUG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Christian Djonov (`KXITFMATCH-26OCT19DJODUG-DJO`) | 0.33 / 0.38 (20) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Remy Dugardin (`KXITFMATCH-26OCT19DJODUG-DUG`) | 0.54 / 0.70 (38) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vincent Dullinger vs Florent Lagarrigue -- M25 Sarreguemines R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19DULLAG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vincent Dullinger (`KXITFMATCH-26OCT19DULLAG-DUL`) | 0.52 / 0.55 (37) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Florent Lagarrigue (`KXITFMATCH-26OCT19DULLAG-LAG`) | 0.41 / 0.47 (40) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jake Fellows vs Kyle McKay -- M25 Redbridge R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19FELMCK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jake Fellows (`KXITFMATCH-26OCT19FELMCK-FEL`) | 0.79 / 0.83 (63) | 81.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kyle McKay (`KXITFMATCH-26OCT19FELMCK-MCK`) | 0.18 / 0.21 (2) | 19.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Patrick Foley vs Max Benaim -- M25 Redbridge R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206299:206405:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Max Benaim (`KXITFMATCH-26OCT19FOLBEN-BEN`) | 0.63 / 0.67 (47) | 65.0% | 53.3% | 38.0% | 53.0% [53.0%-53.0%] | -- | -- | -- | -- | PASS | -11.7 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Patrick Foley (`KXITFMATCH-26OCT19FOLBEN-FOL`) | 0.35 / 0.37 (2) | 36.0% | 46.7% | 62.0% | 47.0% [47.0%-47.0%] | -- | -- | -- | -- | PASS | +10.7 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 68.0; serve-point win A 61.5%, B 37.8%; Elo A 1128.6, B 1150.1; model uncertainty 0.0
* Form inputs: days since last match A 784, B 679; matches on record A 24, B 22; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Younes Jenkins vs Bader Idrees -- M25 Redbridge R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19JENIDR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bader Idrees (`KXITFMATCH-26OCT19JENIDR-IDR`) | 0.37 / 0.40 (26) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Younes Jenkins (`KXITFMATCH-26OCT19JENIDR-JEN`) | 0.55 / 0.62 (76) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alex Kobelt vs Jake Evans -- M25 Redbridge R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19KOBEVA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jake Evans (`KXITFMATCH-26OCT19KOBEVA-EVA`) | 0.18 / 0.28 (69) | 23.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alex Kobelt (`KXITFMATCH-26OCT19KOBEVA-KOB`) | 0.37 / 0.85 (3) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thiago Monteiro vs Alejandro Moro Canas -- ATP Challenger Lisbon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-19T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106329:208279:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thiago Monteiro (`KXATPCHALLENGERMATCH-26OCT19MONMOR-MON`) | 0.51 / 0.52 (767) | 51.5% | 51.8% | 46.0% | 50.0% [48.0%-52.5%] | -- | 62.4% | -- | INSUFFICIENT_INPUTS | WATCH | +0.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alejandro Moro Canas (`KXATPCHALLENGERMATCH-26OCT19MONMOR-MOR`) | 0.48 / 0.49 (564) | 48.5% | 48.2% | 54.0% | 50.0% [47.5%-52.0%] | -- | 48.6% | 48.6% | MARKETS_AGREE | PASS | -0.3 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4338.0, B 4809.0; serve-point win A 64.1%, B 36.3%; Elo A 1716.1, B 1627.1; model uncertainty 0.0224
* Form inputs: days since last match A 14, B 14; matches on record A 920, B 324; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.020, surface_dev_loose -0.005, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Nishith Naveen vs LUCAS GONCALVES FRANCA -- M25 Luanda R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19NAVGON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LUCAS GONCALVES FRANCA (`KXITFMATCH-26OCT19NAVGON-GON`) | 0.81 / 0.84 (5) | 82.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nishith Naveen (`KXITFMATCH-26OCT19NAVGON-NAV`) | 0.16 / 0.19 (5) | 17.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pavel Skvortcov vs Christian Hamuli -- M25 Luanda R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19SKVHAM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Christian Hamuli (`KXITFMATCH-26OCT19SKVHAM-HAM`) | 0.08 / 0.13 (1) | 10.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pavel Skvortcov (`KXITFMATCH-26OCT19SKVHAM-SKV`) | 0.89 / 0.90 (8) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Melvin Vix vs Sparsh Rathi Rathi -- M25 Luanda R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19VIXRAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sparsh Rathi Rathi (`KXITFMATCH-26OCT19VIXRAT-RAT`) | 0.02 / 0.05 (508) | 3.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Melvin Vix (`KXITFMATCH-26OCT19VIXRAT-VIX`) | 0.97 / 0.98 (248) | 97.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lizette Cabrera vs Petra Sedlackova -- W100 Wrexham R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211878:220690:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lizette Cabrera (`KXITFWMATCH-26OCT19CABSED-CAB`) | 0.71 / 0.75 (63) | 73.0% | 91.7% | 65.5% | 85.3% [82.7%-88.2%] | -- | -- | -- | -- | PASS | +18.7 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Petra Sedlackova (`KXITFWMATCH-26OCT19CABSED-SED`) | 0.22 / 0.28 (10) | 25.0% | 8.3% | 34.5% | 14.7% [11.8%-17.3%] | -- | -- | -- | -- | PASS | -16.7 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3443.0, B 371.0; serve-point win A 60.4%, B 50.0%; Elo A 1687.9, B 1329.8; model uncertainty 0.0275
* Form inputs: days since last match A 28, B 350; matches on record A 524, B 28; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT19CABSED-CAB  (YES = Lizette Cabrera)
Model: 92%
Kalshi: 73%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Claudia Cairols Aparicio vs Anna Boron -- W15 Villena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19CAIBOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Boron (`KXITFWMATCH-26OCT19CAIBOR-BOR`) | 0.75 / 0.83 (12) | 79.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Claudia Cairols Aparicio (`KXITFWMATCH-26OCT19CAIBOR-CAI`) | 0.20 / 0.24 (48) | 22.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gina Marie Dittmann vs Lian Tran -- W50 Cherbourg-en-Cotentin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-19T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220560:222273:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gina Marie Dittmann (`KXITFWMATCH-26OCT19DITTRA-DIT`) | 0.42 / 0.43 (43) | 42.5% | 35.8% | 67.6% | 50.5% [40.0%-58.0%] | -- | -- | -- | -- | WATCH | -6.7 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lian Tran (`KXITFWMATCH-26OCT19DITTRA-TRA`) | 0.51 / 0.58 (49) | 54.5% | 64.2% | 32.4% | 49.5% [42.0%-60.1%] | -- | -- | -- | -- | PASS | +9.7 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1885.0, B 1204.0; serve-point win A 50.9%, B 46.4%; Elo A 1412.4, B 1505.4; model uncertainty 0.0902
* Form inputs: days since last match A 196, B 175; matches on record A 115, B 307; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.005, surface_dev_loose +0.011, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anna-Lena Friedsam vs Victoria Allen -- W100 Wrexham R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:204431:216253:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Victoria Allen (`KXITFWMATCH-26OCT19FRIALL-ALL`) | 0.13 / 0.22 (54) | 17.5% | 24.8% | 54.6% | 35.4% [23.2%-42.9%] | -- | -- | -- | -- | WATCH | +7.3 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna-Lena Friedsam (`KXITFWMATCH-26OCT19FRIALL-FRI`) | 0.77 / 0.81 (112) | 79.0% | 75.2% | 45.4% | 64.6% [57.1%-76.8%] | -- | -- | -- | -- | PASS | -3.8 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3834.0, B 1893.0; serve-point win A 62.7%, B 42.6%; Elo A 1767.1, B 1488.4; model uncertainty 0.0985
* Form inputs: days since last match A 7, B 142; matches on record A 669, B 83; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Farah Heddar vs Helene Pellicano -- W15 Villena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-19T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220532:267380:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Farah Heddar (`KXITFWMATCH-26OCT19HEDPEL-HED`) | 0.14 / 0.18 (3) | 16.0% | 10.4% | 14.3% | 21.9% [21.1%-23.5%] | -- | -- | -- | -- | PASS | -5.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Helene Pellicano (`KXITFWMATCH-26OCT19HEDPEL-PEL`) | 0.80 / 0.81 (142) | 80.5% | 89.5% | 85.7% | 78.1% [76.5%-78.8%] | -- | -- | -- | -- | PASS | +9.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 379.0, B 43.0; serve-point win A 49.2%, B 41.4%; Elo A 1100.7, B 1317.6; model uncertainty 0.0119
* Form inputs: days since last match A 189, B 574; matches on record A 14, B 117; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.016, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sarah Iliev vs Maia Ilinca Burcescu -- W50 Cherbourg-en-Cotentin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-19T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:225858:267176:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maia Ilinca Burcescu (`KXITFWMATCH-26OCT19ILIBUR-BUR`) | 0.49 / 0.53 (63) | 51.0% | 47.2% | 61.6% | 49.5% [44.1%-54.3%] | -- | -- | -- | -- | PASS | -3.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sarah Iliev (`KXITFWMATCH-26OCT19ILIBUR-ILI`) | 0.45 / 0.51 (0) | 48.0% | 52.8% | 38.4% | 50.5% [45.7%-55.9%] | -- | -- | -- | -- | PASS | +4.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1783.0, B 877.0; serve-point win A 51.8%, B 48.7%; Elo A 1486.6, B 1435.0; model uncertainty 0.0507
* Form inputs: days since last match A 189, B 83; matches on record A 157, B 30; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.011, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elly Meszarosova vs Jolie Angelique Abendroth -- W15 Karlovy Vary R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19MESABE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jolie Angelique Abendroth (`KXITFWMATCH-26OCT19MESABE-ABE`) | 0.42 / 0.49 (15) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Elly Meszarosova (`KXITFWMATCH-26OCT19MESABE-MES`) | 0.37 / 0.60 (10) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adriana Monlleo Ramos vs Anna Cabassers Morros -- W15 Villena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-19T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:266464:269799:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Cabassers Morros (`KXITFWMATCH-26OCT19MONCAB-CAB`) | 0.36 / 0.37 (39) | 36.5% | 64.7% | 65.1% | 58.5% [58.5%-58.5%] | -- | -- | -- | -- | PASS | +28.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Adriana Monlleo Ramos (`KXITFWMATCH-26OCT19MONCAB-MON`) | 0.57 / 0.63 (23) | 60.0% | 35.3% | 34.9% | 41.5% [41.5%-41.5%] | -- | -- | -- | -- | PASS | -24.7 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 264.0, B 27.0; serve-point win A 52.8%, B 44.4%; Elo A 1212.5, B 1272.7; model uncertainty 0.0001
* Form inputs: days since last match A 329, B 588; matches on record A 7, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT19MONCAB-CAB  (YES = Anna Cabassers Morros)
Model: 65%
Kalshi: 36%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adela Moravcova vs Gloria Reusch -- W15 Karlovy Vary R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19MORREU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adela Moravcova (`KXITFWMATCH-26OCT19MORREU-MOR`) | 0.13 / 0.18 (16) | 15.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gloria Reusch (`KXITFWMATCH-26OCT19MORREU-REU`) | 0.83 / 0.89 (12) | 86.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zi Ying Ruan vs Vega Aguilar Ferrandez -- W15 Villena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-19T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:267462:269990:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vega Aguilar Ferrandez (`KXITFWMATCH-26OCT19RUAAGU-AGU`) | 0.36 / 0.39 (52) | 37.5% | 30.1% | 73.6% | 38.4% [36.4%-39.9%] | -- | -- | -- | -- | PASS | -7.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zi Ying Ruan (`KXITFWMATCH-26OCT19RUAAGU-RUA`) | 0.54 / 0.65 (44) | 59.5% | 69.9% | 26.4% | 61.6% [60.1%-63.6%] | -- | -- | -- | -- | PASS | +10.4 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 832.0, B 66.0; serve-point win A 54.3%, B 49.6%; Elo A 1312.8, B 1217.2; model uncertainty 0.0178
* Form inputs: days since last match A 308, B 399; matches on record A 48, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vanesa Salaiova vs Maja Wrobel -- W15 Karlovy Vary R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:270208:270261:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vanesa Salaiova (`KXITFWMATCH-26OCT19SALWRO-SAL`) | 0.21 / 0.26 (3) | 23.5% | 49.5% | 44.1% | 50.0% [48.9%-50.0%] | -- | -- | -- | -- | PASS | +26.0 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maja Wrobel (`KXITFWMATCH-26OCT19SALWRO-WRO`) | 0.73 / 0.74 (96) | 73.5% | 50.5% | 55.9% | 50.0% [50.0%-51.1%] | -- | -- | -- | -- | PASS | -23.0 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 53.0, B 62.0; serve-point win A 53.9%, B 46.0%; Elo A 1262.6, B 1264.4; model uncertainty 0.0053
* Form inputs: days since last match A 224, B 427; matches on record A 1, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT19SALWRO-SAL  (YES = Vanesa Salaiova)
Model: 49%
Kalshi: 24%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Max Alcala Gurri vs Andres Andrade -- ATP Challenger Lisbon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-19T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200748:208024:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Max Alcala Gurri (`KXATPCHALLENGERMATCH-26OCT19ALCAND-ALC`) | 0.69 / 0.70 (11007) | 69.5% | 49.6% | 68.3% | 57.9% [47.9%-64.0%] | -- | 70.2% | 70.2% | MODEL_LONE_OUTLIER | PASS | -19.9 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Andres Andrade (`KXATPCHALLENGERMATCH-26OCT19ALCAND-AND`) | 0.28 / 0.29 (19073) | 28.5% | 50.4% | 31.7% | 42.1% [36.0%-52.1%] | -- | 30.0% | 30.0% | MODEL_LONE_OUTLIER | PASS | +21.9 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2251.0, B 3169.0; serve-point win A 56.2%, B 43.8%; Elo A 1587.7, B 1651.2; model uncertainty 0.0805
* Form inputs: days since last match A 14, B 21; matches on record A 278, B 244; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT19ALCAND-AND  (YES = Andres Andrade)
Model: 50%
Kalshi: 28%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.026, surface_pool_high +0.026, surface_dev_loose +0.010, surface_dev_tight -0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Lorenzo Sonego vs Moise Kouame -- ATP Lyon R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-19 16:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-19 15:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Clay · scheduled 2026-10-18T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:132283:213608:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Moise Kouame (`KXATPMATCH-26OCT18SONKOU-KOU`) | 0.39 / 0.40 (22491) | 39.5% | 29.6% | 43.0% | 28.2% [20.4%-35.4%] | -- | -- | -- | -- | PASS | -9.9 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lorenzo Sonego (`KXATPMATCH-26OCT18SONKOU-SON`) | 0.60 / 0.61 (16) | 60.5% | 70.4% | 57.0% | 71.8% [64.6%-79.6%] | -- | -- | -- | -- | SHADOW_BET | +9.9 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4551.0, B 1583.0; serve-point win A 65.9%, B 38.4%; Elo A 1802.2, B 1519.3; model uncertainty 0.0746
* Form inputs: days since last match A 13, B 19; matches on record A 689, B 33; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.026, surface_dev_loose -0.021, surface_dev_tight +0.012
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT18SONKOU-KOU2` Will Moise Kouame win at least 1.5 more games than Lorenzo Sonego?: 0.32/0.36 mid 34.0%, model 24.0% (projection_v2.0 (prediction ledger)) -- gap -10.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26OCT18SONKOU-KOU20` Will Moise Kouame win the Lorenzo Sonego vs Moise Kouame match by a set score of 2-0?: 0.19/0.23 mid 21.0%, model 13.0% (projection_v2.0 (prediction ledger)) -- gap -8.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPGSPREAD-26OCT18SONKOU-SON3` Will Lorenzo Sonego win at least 2.5 more games than Moise Kouame?: 0.48/0.49 mid 48.5%, model 55.1% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPGTOTAL-26OCT18SONKOU-29` Over 28.5 games: 0.24/0.29 mid 26.5%, model 33.1% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26OCT18SONKOU-SON21` Will Lorenzo Sonego win the Lorenzo Sonego vs Moise Kouame match by a set score of 2-1?: 0.22/0.24 mid 23.0%, model 29.5% (projection_v2.0 (prediction ledger)) -- gap +6.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPSETWINNER-26OCT18SONKOU-1-SON` Will Lorenzo Sonego win set 1 in the Lorenzo Sonego vs Moise Kouame match: 0.56/0.59 mid 57.5%, model 64.0% (projection_v2.0 (prediction ledger)) -- gap +6.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPGTOTAL-26OCT18SONKOU-24` Over 23.5 games: 0.44/0.46 mid 45.0%, model 51.0% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPSETWINNER-26OCT18SONKOU-1-KOU` Will Moise Kouame win set 1 in the Lorenzo Sonego vs Moise Kouame match: 0.40/0.44 mid 42.0%, model 36.0% (projection_v2.0 (prediction ledger)) -- gap -6.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT18SONKOU-2-KOU` Will Moise Kouame win set 2 in the Lorenzo Sonego vs Moise Kouame match: 0.39/0.44 mid 41.5%, model 36.0% (projection_v2.0 (prediction ledger)) -- gap -5.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT18SONKOU-2-SON` Will Lorenzo Sonego win set 2 in the Lorenzo Sonego vs Moise Kouame match: 0.56/0.61 mid 58.5%, model 64.0% (projection_v2.0 (prediction ledger)) -- gap +5.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPGSPREAD-26OCT18SONKOU-SON6` Will Lorenzo Sonego win at least 5.5 more games than Moise Kouame?: 0.12/0.32 mid 22.0%, model 17.2% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPGTOTAL-26OCT18SONKOU-19` Over 18.5 games: 0.79/0.84 mid 81.5%, model 85.7% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26OCT18SONKOU-SON20` Will Lorenzo Sonego win the Lorenzo Sonego vs Moise Kouame match by a set score of 2-0?: 0.35/0.39 mid 37.0%, model 40.9% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26OCT18SONKOU-KOU21` Will Moise Kouame win the Lorenzo Sonego vs Moise Kouame match by a set score of 2-1?: 0.17/0.19 mid 18.0%, model 16.6% (projection_v2.0 (prediction ledger)) -- gap -1.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Matisse Bobichon / Kilian Feldbausch vs Robert Cash / Alexander Erler -- ATP Lyon R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-19 11:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-19 16:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-19 15:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-19T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19BOBFELCASERL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matisse Bobichon / Kilian Feldbausch (`KXATPDOUBLES-26OCT19BOBFELCASERL-BOBFEL`) | 0.14 / 0.20 (12) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Robert Cash / Alexander Erler (`KXATPDOUBLES-26OCT19BOBFELCASERL-CASERL`) | 0.80 / 0.85 (127) | 82.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Adam Bajurko vs Johan Mapuard -- M25 Luanda R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19BAJMAP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adam Bajurko (`KXITFMATCH-26OCT19BAJMAP-BAJ`) | 0.94 / 0.97 (261) | 95.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Johan Mapuard (`KXITFMATCH-26OCT19BAJMAP-MAP`) | 0.04 / 0.07 (18) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yash Chaurasia vs Sizhe Yan -- M25 Luanda R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19CHAYAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yash Chaurasia (`KXITFMATCH-26OCT19CHAYAN-CHA`) | 0.54 / 0.59 (1) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sizhe Yan (`KXITFMATCH-26OCT19CHAYAN-YAN`) | 0.19 / 0.48 (1) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rahul Dhokia vs Liam Hignett -- M25 Redbridge R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208559:210723:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rahul Dhokia (`KXITFMATCH-26OCT19DHOHIG-DHO`) | 0.47 / 0.52 (1) | 49.5% | 36.9% | 50.0% | 39.0% [39.0%-39.0%] | -- | -- | -- | -- | PASS | -12.6 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Liam Hignett (`KXITFMATCH-26OCT19DHOHIG-HIG`) | 0.45 / 0.50 (40) | 47.5% | 63.1% | 50.0% | 61.0% [61.0%-61.0%] | -- | -- | -- | -- | PASS | +15.6 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 60.7%, B 36.7%; Elo A 1179.4, B 1253.3; model uncertainty 0.0
* Form inputs: days since last match A 721, B 1477; matches on record A 9, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT19DHOHIG-HIG  (YES = Liam Hignett)
Model: 63%
Kalshi: 48%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ivan Dorokhov vs Sizya Ernest Kivanda -- M25 Redbridge R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19DORKIV:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ivan Dorokhov (`KXITFMATCH-26OCT19DORKIV-DOR`) | 0.57 / 0.63 (3) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sizya Ernest Kivanda (`KXITFMATCH-26OCT19DORKIV-KIV`) | 0.37 / 0.39 (48) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carl Holder vs Jared Horwood -- M25 Redbridge R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19HOLHOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carl Holder (`KXITFMATCH-26OCT19HOLHOR-HOL`) | 0.45 / 0.51 (2) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jared Horwood (`KXITFMATCH-26OCT19HOLHOR-HOR`) | 0.45 / 0.50 (54) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sharath Murari vs Joao Rasgado -- M25 Luanda R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19MURRAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sharath Murari (`KXITFMATCH-26OCT19MURRAS-MUR`) | 0.34 / 0.37 (3) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Joao Rasgado (`KXITFMATCH-26OCT19MURRAS-RAS`) | 0.40 / 0.69 (1) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mateja Stanisavljevic vs Conor Brady -- M25 Redbridge R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19STABRA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Conor Brady (`KXITFMATCH-26OCT19STABRA-BRA`) | 0.64 / 0.67 (6131) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mateja Stanisavljevic (`KXITFMATCH-26OCT19STABRA-STA`) | 0.31 / 0.38 (30) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tessa Johanna Brockmann vs Eliz Maloney -- W100 Wrexham R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216340:260598:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tessa Johanna Brockmann (`KXITFWMATCH-26OCT19BROMAL-BRO`) | 0.69 / 0.75 (458) | 72.0% | 91.3% | 69.8% | 82.4% [79.5%-86.2%] | -- | -- | -- | -- | PASS | +19.3 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Eliz Maloney (`KXITFWMATCH-26OCT19BROMAL-MAL`) | 0.24 / 0.28 (14) | 26.0% | 8.7% | 30.2% | 17.6% [13.8%-20.5%] | -- | -- | -- | -- | PASS | -17.3 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3426.0, B 886.0; serve-point win A 59.9%, B 50.3%; Elo A 1727.2, B 1376.2; model uncertainty 0.0336
* Form inputs: days since last match A 6, B 196; matches on record A 169, B 211; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT19BROMAL-BRO  (YES = Tessa Johanna Brockmann)
Model: 91%
Kalshi: 72%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofya Lansere vs Mayuka Aikawa -- W100 Wrexham R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216139:219892:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mayuka Aikawa (`KXITFWMATCH-26OCT19LANAIK-AIK`) | 0.22 / 0.25 (41) | 23.5% | 17.7% | 19.2% | 26.5% [22.3%-34.9%] | -- | -- | -- | -- | PASS | -5.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sofya Lansere (`KXITFWMATCH-26OCT19LANAIK-LAN`) | 0.74 / 0.79 (500) | 76.5% | 82.3% | 80.8% | 73.5% [65.1%-77.7%] | -- | -- | -- | -- | PASS | +5.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3253.0, B 1667.0; serve-point win A 56.8%, B 50.1%; Elo A 1594.9, B 1500.9; model uncertainty 0.0629
* Form inputs: days since last match A 17, B 210; matches on record A 351, B 303; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Diana Martynov vs Marine Szostak -- W50 Cherbourg-en-Cotentin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-19T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221157:222347:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diana Martynov (`KXITFWMATCH-26OCT19MARSZO-MAR`) | 0.62 / 0.68 (45) | 65.0% | 51.4% | 36.4% | 43.6% [37.9%-54.8%] | -- | -- | -- | -- | PASS | -13.6 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marine Szostak (`KXITFWMATCH-26OCT19MARSZO-SZO`) | 0.33 / 0.37 (45) | 35.0% | 48.6% | 63.6% | 56.4% [45.2%-62.1%] | -- | -- | -- | -- | PASS | +13.6 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1861.0, B 1767.0; serve-point win A 53.1%, B 47.1%; Elo A 1465.8, B 1449.7; model uncertainty 0.0845
* Form inputs: days since last match A 43, B 175; matches on record A 329, B 238; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.026, surface_pool_high -0.031, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Clara Vlasselaer vs Liv Boulard -- W50 Cherbourg-en-Cotentin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-19T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221003:260185:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liv Boulard (`KXITFWMATCH-26OCT19VLABOU-BOU`) | 0.26 / 0.29 (37) | 27.5% | 18.9% | 31.1% | 22.6% [20.0%-25.4%] | -- | -- | -- | -- | PASS | -8.6 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Clara Vlasselaer (`KXITFWMATCH-26OCT19VLABOU-VLA`) | 0.70 / 0.74 (30) | 72.0% | 81.1% | 68.9% | 77.4% [74.6%-80.0%] | -- | -- | -- | -- | WATCH | +9.1 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1490.0, B 476.0; serve-point win A 62.9%, B 43.9%; Elo A 1481.5, B 1244.6; model uncertainty 0.0272
* Form inputs: days since last match A 175, B 105; matches on record A 332, B 50; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.028, surface_pool_high +0.026, surface_dev_loose +0.003, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tristan Boyer vs Elmer Moller -- ATP Challenger Lisbon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 16:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-19T16:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207729:209284:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tristan Boyer (`KXATPCHALLENGERMATCH-26OCT19BOYMOL-BOY`) | 0.48 / 0.50 (2034) | 49.0% | 49.5% | 47.9% | 44.7% [43.7%-46.8%] | -- | 48.4% | 48.4% | MARKETS_AGREE | PASS | +0.5 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Elmer Moller (`KXATPCHALLENGERMATCH-26OCT19BOYMOL-MOL`) | 0.50 / 0.51 (1001) | 50.5% | 50.5% | 52.1% | 55.3% [53.2%-56.3%] | -- | 51.8% | 51.8% | MARKETS_AGREE | WATCH | +0.0 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 2991.0, B 3743.0; serve-point win A 56.0%, B 43.9%; Elo A 1659.4, B 1728.4; model uncertainty 0.0158
* Form inputs: days since last match A 14, B 14; matches on record A 220, B 286; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.011, surface_dev_loose +0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Marco Cecchinato vs Vilius Gaubas -- ATP Challenger Lisbon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 16:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-19T16:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106065:209147:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marco Cecchinato (`KXATPCHALLENGERMATCH-26OCT19CECGAU-CEC`) | 0.37 / 0.38 (412) | 37.5% | 44.5% | 65.8% | 61.5% [56.1%-64.4%] | -- | 39.1% | 39.1% | MODEL_LONE_OUTLIER | WATCH | +7.0 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Vilius Gaubas (`KXATPCHALLENGERMATCH-26OCT19CECGAU-GAU`) | 0.62 / 0.63 (2672) | 62.5% | 55.5% | 34.2% | 38.5% [35.6%-43.9%] | -- | 60.8% | 60.8% | MODEL_LONE_OUTLIER | PASS | -7.0 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4793.0, B 4159.0; serve-point win A 61.5%, B 37.4%; Elo A 1685.8, B 1691.7; model uncertainty 0.0416
* Form inputs: days since last match A 14, B 14; matches on record A 953, B 293; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Luis Carlos Alvarez Valdes vs Eric Vanshelboim -- M25 Santa Margherita di Pula R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-19T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208322:211468:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luis Carlos Alvarez Valdes (`KXITFMATCH-26OCT19ALVVAN-ALV`) | 0.46 / 0.50 (62) | 48.0% | 35.4% | 49.5% | 29.2% [29.2%-29.6%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.6 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Eric Vanshelboim (`KXITFMATCH-26OCT19ALVVAN-VAN`) | 0.49 / 0.52 (45) | 50.5% | 64.6% | 50.5% | 70.8% [70.4%-70.8%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +14.1 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 1290.0; serve-point win A 57.8%, B 39.3%; Elo A 1307.7, B 1462.3; model uncertainty 0.0018
* Form inputs: days since last match A 728, B 693; matches on record A 27, B 333; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valerio Bracci vs Gabriele Bosio -- M25 Santa Margherita di Pula R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19BRABOS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriele Bosio (`KXITFMATCH-26OCT19BRABOS-BOS`) | 0.86 / 0.88 (307) | 87.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Valerio Bracci (`KXITFMATCH-26OCT19BRABOS-BRA`) | 0.13 / 0.14 (5) | 13.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tommaso Compagnucci vs Pietro Marino -- M25 Santa Margherita di Pula R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-19T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206867:209233:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tommaso Compagnucci (`KXITFMATCH-26OCT19COMMAR-COM`) | 0.76 / 0.78 (336) | 77.0% | 79.5% | 44.4% | 77.1% [75.6%-78.6%] | 72.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pietro Marino (`KXITFMATCH-26OCT19COMMAR-MAR`) | 0.23 / 0.24 (5) | 23.5% | 20.5% | 55.6% | 22.9% [21.4%-24.4%] | 28.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 515.0, B 56.0; serve-point win A 64.5%, B 42.0%; Elo A 1489.9, B 1271.3; model uncertainty 0.015
* Form inputs: days since last match A 672, B 77; matches on record A 85, B 103; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.008, surface_dev_loose -0.000, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adan Freire Da Silva vs Nicola Senn -- M25 Sarreguemines R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207676:213173:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adan Freire Da Silva (`KXITFMATCH-26OCT19FRESEN-FRE`) | 0.52 / 0.58 (20) | 55.0% | 63.2% | 50.0% | 41.9% [41.9%-41.9%] | -- | -- | -- | -- | PASS | +8.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Nicola Senn (`KXITFMATCH-26OCT19FRESEN-SEN`) | 0.40 / 0.45 (21) | 42.5% | 36.8% | 50.0% | 58.1% [58.1%-58.1%] | -- | -- | -- | -- | PASS | -5.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 63.3%, B 39.3%; Elo A 1211.9, B 1266.2; model uncertainty 0.0
* Form inputs: days since last match A 693, B 784; matches on record A 54, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tom Zeuch vs Yannick Baluska -- M25 Sarreguemines R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19ZEUBAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yannick Baluska (`KXITFMATCH-26OCT19ZEUBAL-BAL`) | 0.08 / 0.12 (4) | 10.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tom Zeuch (`KXITFMATCH-26OCT19ZEUBAL-ZEU`) | 0.88 / 0.90 (5) | 89.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yaiza Borderia vs Neus Torner Sensano -- W15 Villena R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19BORTOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yaiza Borderia (`KXITFWMATCH-26OCT19BORTOR-BOR`) | 0.05 / 0.06 (82) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Neus Torner Sensano (`KXITFWMATCH-26OCT19BORTOR-TOR`) | 0.94 / 0.96 (417) | 95.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Liana Cammilleri vs Nikola Koprivova -- W15 Karlovy Vary R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260589:264990:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liana Cammilleri (`KXITFWMATCH-26OCT19CAMKOP-CAM`) | 0.37 / 0.41 (13) | 39.0% | 58.4% | 58.0% | 50.0% [50.0%-50.0%] | -- | -- | -- | -- | PASS | +19.4 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nikola Koprivova (`KXITFWMATCH-26OCT19CAMKOP-KOP`) | 0.58 / 0.66 (5) | 62.0% | 41.6% | 42.0% | 50.0% [50.0%-50.0%] | -- | -- | -- | -- | PASS | -20.4 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 69.0; serve-point win A 53.7%, B 47.9%; Elo A 1131.5, B 1133.2; model uncertainty 0.0
* Form inputs: days since last match A 700, B 462; matches on record A 41, B 21; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT19CAMKOP-CAM  (YES = Liana Cammilleri)
Model: 58%
Kalshi: 39%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dore / Levicki vs Perez Naranjo / Perez Naranjo -- W15 Villena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-19T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19DORLEVPERPER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dore / Levicki (`KXITFWDOUBLES-26OCT19DORLEVPERPER-DORLEV`) | 0.05 / 0.95 (136) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Perez Naranjo / Perez Naranjo (`KXITFWDOUBLES-26OCT19DORLEVPERPER-PERPER`) | 0.05 / 0.95 (136) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Ariadna Garcia-Patron Canals vs Isabel Pascual Montalvo -- W15 Villena R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-19T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:240161:266543:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ariadna Garcia-Patron Canals (`KXITFWMATCH-26OCT19GARPAS-GAR`) | 0.20 / 0.21 (45) | 20.5% | 48.9% | 55.9% | 47.9% [46.8%-51.6%] | -- | -- | -- | -- | PASS | +28.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Isabel Pascual Montalvo (`KXITFWMATCH-26OCT19GARPAS-PAS`) | 0.78 / 0.81 (398) | 79.5% | 51.1% | 44.1% | 52.1% [48.4%-53.2%] | -- | -- | -- | -- | PASS | -28.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 864.0, B 207.0; serve-point win A 52.2%, B 47.6%; Elo A 1200.6, B 1221.7; model uncertainty 0.0241
* Form inputs: days since last match A 343, B 329; matches on record A 24, B 25; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT19GARPAS-GAR  (YES = Ariadna Garcia-Patron Canals)
Model: 49%
Kalshi: 20%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.011, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cindy Langlais vs Kateryna Lazarenko -- W15 Villena R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-19T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260766:265207:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cindy Langlais (`KXITFWMATCH-26OCT19LANLAZ-LAN`) | 0.34 / 0.37 (8494) | 35.5% | 43.6% | 36.9% | 34.4% [31.5%-39.0%] | -- | -- | -- | -- | PASS | +8.2 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kateryna Lazarenko (`KXITFWMATCH-26OCT19LANLAZ-LAZ`) | 0.64 / 0.65 (44) | 64.5% | 56.4% | 63.1% | 65.6% [61.1%-68.5%] | -- | -- | -- | -- | PASS | -8.2 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 854.0, B 1888.0; serve-point win A 53.6%, B 45.2%; Elo A 1299.2, B 1418.2; model uncertainty 0.0371
* Form inputs: days since last match A 175, B 175; matches on record A 38, B 140; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.035, surface_pool_high -0.029, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leticia Solakov vs Sophie Ehrenbergerova -- W15 Karlovy Vary R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19SOLEHR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sophie Ehrenbergerova (`KXITFWMATCH-26OCT19SOLEHR-EHR`) | 0.06 / 0.09 (24) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leticia Solakov (`KXITFWMATCH-26OCT19SOLEHR-SOL`) | 0.90 / 0.95 (6261) | 92.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Emily Victoria Eigelsbach vs Adriana Tkachenko -- W15 Karlovy Vary R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:263751:270401:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emily Victoria Eigelsbach (`KXITFWMATCH-26OCT19EIGTKA-EIG`) | 0.87 / 0.89 (76) | 88.0% | 50.0% | 51.6% | 53.2% [52.7%-53.2%] | -- | -- | -- | -- | PASS | -38.0 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Adriana Tkachenko (`KXITFWMATCH-26OCT19EIGTKA-TKA`) | 0.11 / 0.13 (9) | 12.0% | 50.0% | 48.4% | 46.8% [46.8%-47.3%] | -- | -- | -- | -- | PASS | +38.0 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 237.0, B 1179.0; serve-point win A 52.0%, B 48.0%; Elo A 1355.1, B 1334.4; model uncertainty 0.0027
* Form inputs: days since last match A 92, B 371; matches on record A 4, B 26; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT19EIGTKA-TKA  (YES = Adriana Tkachenko)
Model: 50%
Kalshi: 12%
Gap: +38 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amandine Hesse vs Julie Myatovic -- W50 Cherbourg-en-Cotentin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-19T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:203281:260204:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amandine Hesse (`KXITFWMATCH-26OCT19HESMYA-HES`) | 0.85 / 0.87 (0) | 86.0% | 91.3% | 74.0% | 88.0% [86.4%-90.7%] | -- | -- | -- | -- | PASS | +5.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Julie Myatovic (`KXITFWMATCH-26OCT19HESMYA-MYA`) | 0.10 / 0.12 (11) | 11.0% | 8.7% | 26.0% | 12.0% [9.3%-13.6%] | -- | -- | -- | -- | PASS | -2.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2021.0, B 350.0; serve-point win A 58.0%, B 52.2%; Elo A 1575.8, B 1189.9; model uncertainty 0.0216
* Form inputs: days since last match A 8, B 189; matches on record A 777, B 65; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.014, surface_dev_loose +0.003, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mina Hodzic vs Dalayna Hewitt -- W100 Wrexham R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216095:220550:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dalayna Hewitt (`KXITFWMATCH-26OCT19HODHEW-HEW`) | 0.29 / 0.35 (40) | 32.0% | 39.1% | 57.2% | 45.9% [40.1%-50.0%] | -- | -- | -- | -- | PASS | +7.1 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mina Hodzic (`KXITFWMATCH-26OCT19HODHEW-HOD`) | 0.63 / 0.68 (48) | 65.5% | 60.9% | 42.8% | 54.1% [50.0%-59.9%] | -- | -- | -- | -- | PASS | -4.6 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2700.0, B 918.0; serve-point win A 61.1%, B 41.1%; Elo A 1565.7, B 1482.7; model uncertainty 0.0495
* Form inputs: days since last match A 6, B 189; matches on record A 288, B 233; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Caroline Werner vs Ankita Raina -- W100 Wrexham R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206102:espn:espn:4384:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ankita Raina (`KXITFWMATCH-26OCT19WERRAI-RAI`) | 0.13 / 0.19 (107) | 16.0% | 31.6% | 48.9% | 42.6% [42.5%-42.6%] | -- | -- | -- | -- | PASS | +15.6 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Caroline Werner (`KXITFWMATCH-26OCT19WERRAI-WER`) | 0.83 / 0.84 (6137) | 83.5% | 68.4% | 51.1% | 57.4% [57.4%-57.5%] | -- | -- | -- | -- | PASS | -15.1 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 2055.0; serve-point win A 54.6%, B 49.0%; Elo A 1618.5, B 1565.5; model uncertainty 0.0
* Form inputs: days since last match A 7, B 8; matches on record A 24, B 780; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT19WERRAI-RAI  (YES = Ankita Raina)
Model: 32%
Kalshi: 16%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mateus Alves vs Jose Pereira -- ATP Challenger Cali Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-19T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105700:127123:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mateus Alves (`KXATPCHALLENGERMATCH-26OCT19ALVPER-ALV`) | 0.78 / 0.80 (40) | 79.0% | 70.9% | 46.5% | 59.4% [55.5%-61.8%] | 77.7% | 78.2% | -- | INSUFFICIENT_INPUTS | PASS | -8.1 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jose Pereira (`KXATPCHALLENGERMATCH-26OCT19ALVPER-PER`) | 0.20 / 0.21 (44) | 20.5% | 29.1% | 53.5% | 40.6% [38.2%-44.5%] | 22.3% | 21.7% | -- | INSUFFICIENT_INPUTS | WATCH | +8.6 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1772.0, B 703.0; serve-point win A 66.2%, B 38.2%; Elo A 1502.8, B 1397.4; model uncertainty 0.0319
* Form inputs: days since last match A 21, B 21; matches on record A 332, B 755; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Diego Dedura vs Frazier Rengifo -- ATP Challenger Cali Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-19T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19DEDREN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diego Dedura (`KXATPCHALLENGERMATCH-26OCT19DEDREN-DED`) | 0.93 / 0.94 (6616) | 93.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Frazier Rengifo (`KXATPCHALLENGERMATCH-26OCT19DEDREN-REN`) | 0.05 / 0.06 (2959) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Alan Magadan vs Daniel Salazar Martinez -- ATP Challenger Cali Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-19T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202369:209246:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alan Magadan (`KXATPCHALLENGERMATCH-26OCT19MAGSAL-MAG`) | 0.63 / 0.64 (261) | 63.5% | 71.4% | 38.2% | 69.9% [64.8%-74.0%] | 61.6% | 63.3% | 63.3% | MODEL_LONE_OUTLIER | PASS | +7.9 pp | NORMAL | FRESH | D / POOR | EXTERNAL_STALE | VERIFIED |
| Daniel Salazar Martinez (`KXATPCHALLENGERMATCH-26OCT19MAGSAL-SAL`) | 0.35 / 0.36 (8) | 35.5% | 28.6% | 61.8% | 30.1% [26.0%-35.2%] | 38.4% | 36.8% | 36.8% | MODEL_LONE_OUTLIER | PASS | -6.9 pp | NORMAL | FRESH | D / POOR | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 814.0, B 166.0; serve-point win A 61.3%, B 43.0%; Elo A 1422.8, B 1249.2; model uncertainty 0.0462
* Form inputs: days since last match A 30, B 210; matches on record A 40, B 41; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.014, surface_dev_loose +0.001, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE

## Milena Maria Ciocan vs Diana Marcinkevica -- W50 Cherbourg-en-Cotentin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-19T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:203509:270134:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Milena Maria Ciocan (`KXITFWMATCH-26OCT19CIOMAR-CIO`) | 0.62 / 0.63 (67) | 62.5% | 15.9% | 35.5% | 25.0% [21.2%-28.0%] | -- | -- | -- | -- | PASS | -46.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Diana Marcinkevica (`KXITFWMATCH-26OCT19CIOMAR-MAR`) | 0.31 / 0.36 (25) | 33.5% | 84.1% | 64.5% | 75.0% [72.0%-78.8%] | -- | -- | -- | -- | PASS | +50.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 217.0, B 1101.0; serve-point win A 52.0%, B 40.4%; Elo A 1236.2, B 1441.4; model uncertainty 0.0338
* Form inputs: days since last match A 231, B 210; matches on record A 6, B 942; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT19CIOMAR-MAR  (YES = Diana Marcinkevica)
Model: 84%
Kalshi: 34%
Gap: +51 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.028, surface_pool_high +0.030, surface_dev_loose +0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elena Malygina vs Alice Gillan -- W100 Wrexham R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216116:216268:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alice Gillan (`KXITFWMATCH-26OCT19MALGIL-GIL`) | 0.10 / 0.16 (25) | 13.0% | 18.5% | 33.4% | 29.6% [28.2%-31.5%] | -- | -- | -- | -- | PASS | +5.5 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elena Malygina (`KXITFWMATCH-26OCT19MALGIL-MAL`) | 0.79 / 0.88 (6260) | 83.5% | 81.5% | 66.6% | 70.4% [68.5%-71.8%] | -- | -- | -- | -- | PASS | -2.0 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2298.0, B 1933.0; serve-point win A 56.3%, B 50.3%; Elo A 1689.5, B 1499.9; model uncertainty 0.0161
* Form inputs: days since last match A 24, B 175; matches on record A 440, B 280; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Viktoria Morvayova vs Andre Lukosiute -- W100 Wrexham R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215077:221497:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andre Lukosiute (`KXITFWMATCH-26OCT19MORLUK-LUK`) | 0.33 / 0.41 (13) | 37.0% | 33.0% | 54.8% | 46.3% [39.5%-50.5%] | -- | -- | -- | -- | PASS | -4.0 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Viktoria Morvayova (`KXITFWMATCH-26OCT19MORLUK-MOR`) | 0.58 / 0.63 (35) | 60.5% | 67.0% | 45.2% | 53.7% [49.5%-60.5%] | -- | -- | -- | -- | PASS | +6.5 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3267.0, B 1759.0; serve-point win A 57.3%, B 46.0%; Elo A 1600.4, B 1501.8; model uncertainty 0.0552
* Form inputs: days since last match A 6, B 175; matches on record A 465, B 176; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cabassers Morros / Cabassers Morros vs Cairols Aparicio / Kova -- W15 Villena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-19T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19CABCABCAIKOV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cabassers Morros / Cabassers Morros (`KXITFWDOUBLES-26OCT19CABCABCAIKOV-CABCAB`) | 0.05 / 0.95 (136) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cairols Aparicio / Kova (`KXITFWDOUBLES-26OCT19CABCABCAIKOV-CAIKOV`) | 0.05 / 0.95 (136) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Giraldi Requena / Soto Neira vs De Oliveira Pinto / Montesinos Vilanova -- W15 Villena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-19T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19GIRSOTDEOMON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| De Oliveira Pinto / Montesinos Vilanova (`KXITFWDOUBLES-26OCT19GIRSOTDEOMON-DEOMON`) | 0.05 / 0.95 (136) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Giraldi Requena / Soto Neira (`KXITFWDOUBLES-26OCT19GIRSOTDEOMON-GIRSOT`) | 0.05 / 0.95 (136) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Tereza Hermanova vs Ella Haavisto -- W15 Karlovy Vary R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19HERHAA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ella Haavisto (`KXITFWMATCH-26OCT19HERHAA-HAA`) | 0.52 / 0.63 (198) | 57.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tereza Hermanova (`KXITFWMATCH-26OCT19HERHAA-HER`) | 0.37 / 0.49 (49) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## LEDOUX / Valbuena Moran vs Peet / Sarganella Verdu -- W15 Villena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-19T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19LEDVALPEESAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LEDOUX / Valbuena Moran (`KXITFWDOUBLES-26OCT19LEDVALPEESAR-LEDVAL`) | 0.05 / 0.95 (136) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Peet / Sarganella Verdu (`KXITFWDOUBLES-26OCT19LEDVALPEESAR-PEESAR`) | 0.05 / 0.95 (136) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Emma Slavikova vs Laetitia Pulchartova -- W15 Karlovy Vary R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:219965:239126:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Laetitia Pulchartova (`KXITFWMATCH-26OCT19SLAPUL-PUL`) | 0.29 / 0.30 (20) | 29.5% | 37.1% | 38.4% | 41.0% [39.4%-41.5%] | -- | -- | -- | -- | WATCH | +7.6 pp | NORMAL | FRESH | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Emma Slavikova (`KXITFWMATCH-26OCT19SLAPUL-SLA`) | 0.69 / 0.70 (301) | 69.5% | 62.9% | 61.6% | 59.0% [58.5%-60.6%] | -- | -- | -- | -- | PASS | -6.6 pp | NORMAL | FRESH | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1128.0, B 287.0; serve-point win A 53.1%, B 49.4%; Elo A 1315.8, B 1254.6; model uncertainty 0.0105
* Form inputs: days since last match A 175, B 196; matches on record A 137, B 169; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Angelina Wirges vs Lola Giza -- W15 Karlovy Vary R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220493:260503:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lola Giza (`KXITFWMATCH-26OCT19WIRGIZ-GIZ`) | 0.81 / 0.82 (7735) | 81.5% | 25.9% | 39.5% | 27.0% [24.4%-29.2%] | -- | -- | -- | -- | PASS | -55.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Angelina Wirges (`KXITFWMATCH-26OCT19WIRGIZ-WIR`) | 0.19 / 0.20 (51) | 19.5% | 74.1% | 60.5% | 73.0% [70.8%-75.6%] | -- | -- | -- | -- | PASS | +54.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1745.0, B 432.0; serve-point win A 56.5%, B 48.3%; Elo A 1453.3, B 1249.9; model uncertainty 0.0241
* Form inputs: days since last match A 182, B 441; matches on record A 257, B 14; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT19WIRGIZ-WIR  (YES = Angelina Wirges)
Model: 74%
Kalshi: 20%
Gap: +55 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valentin Basel vs SANTIAGO PESINO -- M15 Maceio R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19BASPES:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentin Basel (`KXITFMATCH-26OCT19BASPES-BAS`) | 0.69 / 0.75 (6137) | 72.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| SANTIAGO PESINO (`KXITFMATCH-26OCT19BASPES-PES`) | 0.25 / 0.29 (31) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eric Von Marton Martins vs Giovanni Branchetti -- M15 Maceio R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19MARBRA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giovanni Branchetti (`KXITFMATCH-26OCT19MARBRA-BRA`) | 0.89 / 0.92 (74) | 90.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eric Von Marton Martins (`KXITFMATCH-26OCT19MARBRA-MAR`) | 0.06 / 0.12 (4) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kenta Miyoshi (b. 2004) vs Sander Jong -- ATP Challenger Fort Worth Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-19T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210093:211501:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sander Jong (`KXATPCHALLENGERMATCH-26OCT19MIYJON-JON`) | 0.45 / 0.47 (692) | 46.0% | 41.9% | 34.3% | 55.0% [52.0%-57.0%] | 46.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.1 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Kenta Miyoshi (b. 2004) (`KXATPCHALLENGERMATCH-26OCT19MIYJON-MIY`) | 0.52 / 0.54 (59) | 53.0% | 58.1% | 65.7% | 45.0% [43.0%-48.0%] | 53.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.1 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 675.0, B 155.0; serve-point win A 63.6%, B 38.0%; Elo A 1444.8, B 1493.9; model uncertainty 0.0252
* Form inputs: days since last match A 27, B 134; matches on record A 54, B 105; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE

## Alex Rybakov vs Bor Artnak -- ATP Challenger Fort Worth Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-19T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126206:210107:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bor Artnak (`KXATPCHALLENGERMATCH-26OCT19RYBART-ART`) | 0.34 / 0.36 (303) | 35.0% | 33.3% | 28.8% | 30.6% [27.9%-32.0%] | 36.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.7 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alex Rybakov (`KXATPCHALLENGERMATCH-26OCT19RYBART-RYB`) | 0.63 / 0.65 (70) | 64.0% | 66.7% | 71.2% | 69.5% [68.0%-72.1%] | 63.8% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +2.7 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1869.0, B 815.0; serve-point win A 63.7%, B 39.7%; Elo A 1578.3, B 1436.8; model uncertainty 0.0203
* Form inputs: days since last match A 63, B 31; matches on record A 436, B 188; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Gavin Young vs Duncan Chan -- ATP Challenger Fort Worth Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-19T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211673:212405:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Duncan Chan (`KXATPCHALLENGERMATCH-26OCT19YOUCHA-CHA`) | 0.60 / 0.61 (21) | 60.5% | 34.6% | 46.5% | 40.0% [40.0%-40.0%] | 59.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -25.9 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Gavin Young (`KXATPCHALLENGERMATCH-26OCT19YOUCHA-YOU`) | 0.38 / 0.40 (313) | 39.0% | 65.4% | 53.5% | 60.0% [60.0%-60.0%] | 40.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +26.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 636.0; serve-point win A 63.5%, B 39.6%; Elo A 1501.3, B 1433.4; model uncertainty 0.0
* Form inputs: days since last match A 749, B 21; matches on record A 17, B 18; data quality F

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT19YOUCHA-YOU  (YES = Gavin Young)
Model: 65%
Kalshi: 39%
Gap: +26 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Irina Balus vs Michika Ozeki -- W75 Saguenay R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:210537:235161:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Irina Balus (`KXITFWMATCH-26OCT19BALOZE-BAL`) | 0.81 / 0.87 (6158) | 84.0% | 83.6% | 66.1% | 70.0% [68.6%-71.4%] | -- | -- | -- | -- | PASS | -0.4 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Michika Ozeki (`KXITFWMATCH-26OCT19BALOZE-OZE`) | 0.10 / 0.16 (5) | 13.0% | 16.4% | 33.9% | 30.0% [28.6%-31.4%] | -- | -- | -- | -- | PASS | +3.4 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 671.0, B 2363.0; serve-point win A 55.0%, B 52.3%; Elo A 1514.0, B 1354.1; model uncertainty 0.0141
* Form inputs: days since last match A 182, B 175; matches on record A 101, B 490; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sara Cakarevic vs Marie Mattel -- W50 Cherbourg-en-Cotentin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-19T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214319:215805:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Cakarevic (`KXITFWMATCH-26OCT19CAKMAT-CAK`) | 0.53 / 0.61 (60) | 57.0% | 74.2% | 42.7% | 63.9% [53.7%-77.1%] | -- | -- | -- | -- | PASS | +17.2 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marie Mattel (`KXITFWMATCH-26OCT19CAKMAT-MAT`) | 0.38 / 0.39 (40) | 38.5% | 25.8% | 57.3% | 36.1% [22.9%-46.3%] | -- | -- | -- | -- | PASS | -12.7 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1791.0, B 630.0; serve-point win A 60.1%, B 44.9%; Elo A 1460.0, B 1298.0; model uncertainty 0.1174
* Form inputs: days since last match A 7, B 196; matches on record A 475, B 32; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT19CAKMAT-CAK  (YES = Sara Cakarevic)
Model: 74%
Kalshi: 57%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.062, surface_pool_high -0.071, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gabriela Guapindaia Soares vs Martina Macarena Torrales Tebes -- W15 Campina Grande R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19GUATOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriela Guapindaia Soares (`KXITFWMATCH-26OCT19GUATOR-GUA`) | 0.91 / 0.94 (124) | 92.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Martina Macarena Torrales Tebes (`KXITFWMATCH-26OCT19GUATOR-TOR`) | 0.04 / 0.08 (4) | 6.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Clervie Ngounoue vs Michaela Bayerlova -- W75 Saguenay R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215693:238064:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michaela Bayerlova (`KXITFWMATCH-26OCT19NGOBAY-BAY`) | 0.12 / 0.14 (430) | 13.0% | 5.6% | 22.7% | 12.8% [9.1%-15.5%] | -- | -- | -- | -- | PASS | -7.4 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Clervie Ngounoue (`KXITFWMATCH-26OCT19NGOBAY-NGO`) | 0.84 / 0.86 (0) | 85.0% | 94.4% | 77.3% | 87.2% [84.5%-90.9%] | -- | -- | -- | -- | WATCH | +9.4 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2509.0, B 1530.0; serve-point win A 59.5%, B 52.4%; Elo A 1783.6, B 1315.6; model uncertainty 0.0319
* Form inputs: days since last match A 56, B 106; matches on record A 153, B 350; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carson Tanguilig vs Thara Gowda -- W75 Saguenay R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221624:270453:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thara Gowda (`KXITFWMATCH-26OCT19TANGOW-GOW`) | 0.28 / 0.32 (1) | 30.0% | 32.6% | 47.3% | 37.4% [36.4%-39.0%] | -- | -- | -- | -- | PASS | +2.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carson Tanguilig (`KXITFWMATCH-26OCT19TANGOW-TAN`) | 0.65 / 0.70 (10) | 67.5% | 67.3% | 52.7% | 62.6% [61.0%-63.6%] | -- | -- | -- | -- | PASS | -0.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1314.0, B 169.0; serve-point win A 56.4%, B 46.9%; Elo A 1468.5, B 1369.2; model uncertainty 0.0128
* Form inputs: days since last match A 182, B 231; matches on record A 33, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vitoria Zuccon vs sofia omati albieri -- W15 Campina Grande R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-19T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:266574:270364:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| sofia omati albieri (`KXITFWMATCH-26OCT19ZUCALB-ALB`) | 0.56 / 0.57 (58) | 56.5% | 32.4% | 65.2% | 42.5% [42.5%-42.6%] | -- | -- | -- | -- | PASS | -24.1 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Vitoria Zuccon (`KXITFWMATCH-26OCT19ZUCALB-ZUC`) | 0.38 / 0.44 (21) | 41.0% | 67.6% | 34.8% | 57.5% [57.4%-57.5%] | -- | -- | -- | -- | PASS | +26.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 48.0, B 0.0; serve-point win A 53.1%, B 50.3%; Elo A 1262.4, B 1211.5; model uncertainty 0.0002
* Form inputs: days since last match A 336, B 945; matches on record A 1, B 3; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT19ZUCALB-ZUC  (YES = Vitoria Zuccon)
Model: 68%
Kalshi: 41%
Gap: +27 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alex Hernandez vs Franco Ribero -- ATP Challenger Cali Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 19:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-19T19:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19HERRIB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Hernandez (`KXATPCHALLENGERMATCH-26OCT19HERRIB-HER`) | 0.62 / 0.65 (577) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Franco Ribero (`KXATPCHALLENGERMATCH-26OCT19HERRIB-RIB`) | 0.35 / 0.37 (302) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Felipe Meligeni Alves vs Juan Sebastian Gomez -- ATP Challenger Cali Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 19:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-19T19:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105944:200335:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Sebastian Gomez (`KXATPCHALLENGERMATCH-26OCT19MELGOM-GOM`) | 0.05 / 0.06 (1191) | 5.5% | 11.9% | 19.7% | 17.2% [16.2%-18.4%] | -- | 7.3% | 7.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.4 pp | NORMAL | FRESH | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Felipe Meligeni Alves (`KXATPCHALLENGERMATCH-26OCT19MELGOM-MEL`) | 0.93 / 0.94 (1355) | 93.5% | 88.1% | 80.3% | 82.8% [81.6%-83.8%] | -- | 90.0% | -- | INSUFFICIENT_INPUTS | PASS | -5.4 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2746.0, B 933.0; serve-point win A 64.3%, B 44.9%; Elo A 1683.7, B 1391.0; model uncertainty 0.0111
* Form inputs: days since last match A 14, B 105; matches on record A 510, B 466; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.003, surface_pool_high +0.003, surface_dev_loose +0.007, surface_dev_tight -0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Santiago Rodriguez Taverna vs Sergio Luis Hernandez Ramirez -- ATP Challenger Cali Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 19:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-19T19:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19RODHER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sergio Luis Hernandez Ramirez (`KXATPCHALLENGERMATCH-26OCT19RODHER-HER`) | 0.20 / 0.21 (1789) | 20.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Santiago Rodriguez Taverna (`KXATPCHALLENGERMATCH-26OCT19RODHER-ROD`) | 0.78 / 0.79 (125) | 78.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Filipe Bullamah vs Enzo Crevelaro -- M15 Maceio R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212787:tml:B19W:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filipe Bullamah (`KXITFMATCH-26OCT19BULCRE-BUL`) | 0.37 / 0.42 (2) | 39.5% | 67.7% | 37.0% | 68.6% [67.8%-68.6%] | -- | -- | -- | -- | PASS | +28.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Enzo Crevelaro (`KXITFMATCH-26OCT19BULCRE-CRE`) | 0.56 / 0.62 (6131) | 59.0% | 32.3% | 63.0% | 31.4% [31.4%-32.2%] | -- | -- | -- | -- | PASS | -26.7 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 47.0, B 0.0; serve-point win A 63.2%, B 40.4%; Elo A 1350.7, B 1215.0; model uncertainty 0.0042
* Form inputs: days since last match A 119, B 707; matches on record A 1, B 3; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT19BULCRE-BUL  (YES = Filipe Bullamah)
Model: 68%
Kalshi: 40%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Enzo Lima vs Andre Souza -- M15 Maceio R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19LIMSOU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Enzo Lima (`KXITFMATCH-26OCT19LIMSOU-LIM`) | 0.64 / 0.69 (6342) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Andre Souza (`KXITFMATCH-26OCT19LIMSOU-SOU`) | 0.29 / 0.36 (68) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andrea Cabio vs Annabelle Xu -- W75 Saguenay R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222376:267458:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea Cabio (`KXITFWMATCH-26OCT19CABXUX-CAB`) | 0.16 / 0.19 (5) | 17.5% | 28.9% | 23.5% | 36.9% [31.5%-39.5%] | -- | -- | -- | -- | PASS | +11.4 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Annabelle Xu (`KXITFWMATCH-26OCT19CABXUX-XUX`) | 0.76 / 0.82 (61) | 79.0% | 71.0% | 76.5% | 63.1% [60.5%-68.5%] | -- | -- | -- | -- | PASS | -8.0 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 318.0, B 722.0; serve-point win A 51.7%, B 44.2%; Elo A 1267.3, B 1339.2; model uncertainty 0.0397
* Form inputs: days since last match A 224, B 82; matches on record A 22, B 43; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Victoria Hu vs Ranah Akua Stoiber -- W75 Saguenay R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221023:239442:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Victoria Hu (`KXITFWMATCH-26OCT19HUXSTO-HUX`) | 0.54 / 0.60 (84) | 57.0% | 50.0% | 46.8% | 44.7% [43.1%-45.8%] | -- | -- | -- | -- | PASS | -7.0 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ranah Akua Stoiber (`KXITFWMATCH-26OCT19HUXSTO-STO`) | 0.37 / 0.42 (2) | 39.5% | 50.0% | 53.2% | 55.3% [54.2%-56.9%] | -- | -- | -- | -- | WATCH | +10.5 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2960.0, B 2562.0; serve-point win A 56.5%, B 43.5%; Elo A 1504.7, B 1566.8; model uncertainty 0.0132
* Form inputs: days since last match A 175, B 175; matches on record A 293, B 147; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Michael Antonius vs Albert Pedrico Kravtsov -- ATP Challenger Fort Worth Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 20:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-19T20:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212285:tml:A0O1:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michael Antonius (`KXATPCHALLENGERMATCH-26OCT19ANTPED-ANT`) | 0.62 / 0.63 (1669) | 62.5% | 53.7% | 50.0% | 55.6% [55.0%-56.1%] | 63.8% | -- | 63.8% | MODEL_LONE_OUTLIER | PASS | -8.8 pp | NORMAL | FRESH | F / POOR | AGREES_WITH_KALSHI | AMBIGUOUS |
| Albert Pedrico Kravtsov (`KXATPCHALLENGERMATCH-26OCT19ANTPED-PED`) | 0.36 / 0.37 (858) | 36.5% | 46.3% | 50.0% | 44.4% [43.9%-45.0%] | 36.2% | -- | 36.2% | MODEL_LONE_OUTLIER | PASS | +9.8 pp | NORMAL | FRESH | F / POOR | AGREES_WITH_KALSHI | AMBIGUOUS |

* Serve evidence (points): A 134.0, B 212.0; serve-point win A 62.6%, B 38.1%; Elo A 1440.5, B 1396.6; model uncertainty 0.0051
* Form inputs: days since last match A 54, B 735; matches on record A 3, B 50; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Kaylan Bigun vs Patrick Zahraj -- ATP Challenger Fort Worth Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 20:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-19T20:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200452:210744:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kaylan Bigun (`KXATPCHALLENGERMATCH-26OCT19BIGZAH-BIG`) | 0.57 / 0.58 (926) | 57.5% | 34.5% | 49.0% | 31.0% [23.5%-35.2%] | 59.9% | 59.1% | 59.5% | ALL_THREE_DISAGREE | PASS | -23.0 pp | HIGH_REVIEW | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Patrick Zahraj (`KXATPCHALLENGERMATCH-26OCT19BIGZAH-ZAH`) | 0.40 / 0.41 (6766) | 40.5% | 65.5% | 51.0% | 69.0% [64.8%-76.4%] | 40.1% | 41.9% | 41.0% | MODEL_LONE_OUTLIER | PASS | +25.0 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 734.0, B 1673.0; serve-point win A 57.2%, B 39.7%; Elo A 1282.3, B 1486.7; model uncertainty 0.0585
* Form inputs: days since last match A 714, B 56; matches on record A 41, B 167; data quality F

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT19BIGZAH-ZAH  (YES = Patrick Zahraj)
Model: 66%
Kalshi: 40%
Gap: +25 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Erik Arutiunian vs Aidan McHugh -- ATP Challenger Fort Worth Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-19T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202420:210250:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Erik Arutiunian (`KXATPCHALLENGERMATCH-26OCT19ARUMCH-ARU`) | 0.50 / 0.51 (486) | 50.5% | 27.9% | 54.0% | 26.6% [24.7%-29.6%] | -- | 52.2% | -- | INSUFFICIENT_INPUTS | PASS | -22.6 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aidan McHugh (`KXATPCHALLENGERMATCH-26OCT19ARUMCH-MCH`) | 0.48 / 0.49 (20) | 48.5% | 72.1% | 46.0% | 73.5% [70.4%-75.3%] | -- | 48.3% | -- | INSUFFICIENT_INPUTS | PASS | +23.6 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 208.0, B 2336.0; serve-point win A 61.0%, B 34.4%; Elo A 1294.6, B 1502.3; model uncertainty 0.0243
* Form inputs: days since last match A 35, B 707; matches on record A 133, B 414; data quality F

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT19ARUMCH-MCH  (YES = Aidan McHugh)
Model: 72%
Kalshi: 48%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Clemence Mercier vs Lilian Poling -- W75 Saguenay R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221585:260855:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Clemence Mercier (`KXITFWMATCH-26OCT19MERPOL-MER`) | 0.57 / 0.61 (66) | 59.0% | 73.3% | 78.4% | 63.6% [60.6%-67.0%] | -- | -- | -- | -- | PASS | +14.3 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lilian Poling (`KXITFWMATCH-26OCT19MERPOL-POL`) | 0.34 / 0.42 (65) | 38.0% | 26.7% | 21.6% | 36.4% [33.0%-39.5%] | -- | -- | -- | -- | PASS | -11.3 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 263.0, B 1063.0; serve-point win A 56.8%, B 47.9%; Elo A 1340.0, B 1269.9; model uncertainty 0.0321
* Form inputs: days since last match A 371, B 175; matches on record A 26, B 93; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jana Otzipka vs Salma Djoubri -- W50 Cherbourg-en-Cotentin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-19T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220305:260445:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Salma Djoubri (`KXITFWMATCH-26OCT19OTZDJO-DJO`) | 0.37 / 0.43 (44) | 40.0% | 55.3% | 45.7% | 54.3% [50.5%-57.4%] | -- | -- | -- | -- | PASS | +15.3 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jana Otzipka (`KXITFWMATCH-26OCT19OTZDJO-OTZ`) | 0.53 / 0.58 (2) | 55.5% | 44.7% | 54.3% | 45.7% [42.6%-49.5%] | -- | -- | -- | -- | PASS | -10.8 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 908.0, B 169.0; serve-point win A 51.7%, B 47.3%; Elo A 1434.0, B 1467.4; model uncertainty 0.0345
* Form inputs: days since last match A 175, B 336; matches on record A 98, B 168; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT19OTZDJO-DJO  (YES = Salma Djoubri)
Model: 55%
Kalshi: 40%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.027, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ayana Akli vs Kayla Cross -- W75 Saguenay R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:239436:264149:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ayana Akli (`KXITFWMATCH-26OCT19AKLCRO-AKL`) | 0.47 / 0.50 (47) | 48.5% | 42.7% | 57.4% | 51.6% [46.3%-54.2%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.8 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kayla Cross (`KXITFWMATCH-26OCT19AKLCRO-CRO`) | 0.50 / 0.51 (3) | 50.5% | 57.3% | 42.6% | 48.4% [45.8%-53.7%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.8 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2838.0, B 2619.0; serve-point win A 54.4%, B 44.2%; Elo A 1616.6, B 1669.5; model uncertainty 0.0398
* Form inputs: days since last match A 28, B 35; matches on record A 123, B 237; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Linea Bajraliu vs Kallista Liu -- W75 Saguenay R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259996:264180:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Linea Bajraliu (`KXITFWMATCH-26OCT19BAJLIU-BAJ`) | 0.59 / 0.68 (48) | 63.5% | 79.0% | 81.5% | 75.3% [69.4%-79.7%] | -- | -- | -- | -- | PASS | +15.5 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kallista Liu (`KXITFWMATCH-26OCT19BAJLIU-LIU`) | 0.29 / 0.37 (66) | 33.0% | 21.0% | 18.5% | 24.7% [20.3%-30.6%] | -- | -- | -- | -- | PASS | -12.0 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1577.0, B 1064.0; serve-point win A 56.1%, B 49.9%; Elo A 1440.7, B 1295.7; model uncertainty 0.0512
* Form inputs: days since last match A 104, B 196; matches on record A 46, B 41; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT19BAJLIU-BAJ  (YES = Linea Bajraliu)
Model: 79%
Kalshi: 64%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Emma Kamper vs Rose Marie Nijkamp -- W50 Austin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-19T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:241715:260225:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emma Kamper (`KXITFWMATCH-26OCT19KAMNIJ-KAM`) | 0.68 / 0.75 (57) | 71.5% | 40.7% | 69.5% | 44.6% [35.4%-53.2%] | -- | -- | -- | -- | PASS | -30.8 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rose Marie Nijkamp (`KXITFWMATCH-26OCT19KAMNIJ-NIJ`) | 0.21 / 0.29 (2) | 25.0% | 59.3% | 30.5% | 55.4% [46.8%-64.6%] | -- | -- | -- | -- | PASS | +34.3 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 510.0, B 1080.0; serve-point win A 49.2%, B 49.0%; Elo A 1348.1, B 1447.9; model uncertainty 0.0893
* Form inputs: days since last match A 350, B 182; matches on record A 33, B 54; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT19KAMNIJ-NIJ  (YES = Rose Marie Nijkamp)
Model: 59%
Kalshi: 25%
Gap: +34 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.011, surface_dev_loose +0.016, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Olivia Lincer vs Merna Refaat -- W50 Austin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-19T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221473:239386:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Olivia Lincer (`KXITFWMATCH-26OCT19LINREF-LIN`) | 0.53 / 0.58 (59) | 55.5% | 64.2% | 37.9% | 59.0% [53.2%-66.6%] | -- | -- | -- | -- | PASS | +8.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Merna Refaat (`KXITFWMATCH-26OCT19LINREF-REF`) | 0.36 / 0.43 (3) | 39.5% | 35.8% | 62.1% | 41.0% [33.4%-46.8%] | -- | -- | -- | -- | PASS | -3.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 785.0, B 556.0; serve-point win A 53.7%, B 49.0%; Elo A 1524.2, B 1402.3; model uncertainty 0.0668
* Form inputs: days since last match A 103, B 371; matches on record A 148, B 201; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.011, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ella McDonald vs Mathilde Ngijol Carre -- W50 Austin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-19T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259591:264248:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ella McDonald (`KXITFWMATCH-26OCT19MCDNGI-MCD`) | 0.88 / 0.93 (51) | 90.5% | 85.1% | 81.9% | 77.4% [75.7%-79.7%] | -- | -- | -- | -- | PASS | -5.4 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mathilde Ngijol Carre (`KXITFWMATCH-26OCT19MCDNGI-NGI`) | 0.04 / 0.10 (8) | 7.0% | 14.9% | 18.1% | 22.6% [20.3%-24.3%] | -- | -- | -- | -- | PASS | +7.9 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1341.0, B 227.0; serve-point win A 56.4%, B 51.4%; Elo A 1577.6, B 1369.4; model uncertainty 0.0203
* Form inputs: days since last match A 118, B 245; matches on record A 146, B 35; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.012, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lexington Reed vs Mayu Crossley -- W50 Austin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-19T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:239186:260714:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mayu Crossley (`KXITFWMATCH-26OCT19REECRO-CRO`) | 0.69 / 0.76 (56) | 72.5% | 82.3% | 77.6% | 73.0% [69.3%-76.5%] | -- | -- | -- | -- | PASS | +9.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lexington Reed (`KXITFWMATCH-26OCT19REECRO-REE`) | 0.22 / 0.29 (50) | 25.5% | 17.7% | 22.4% | 27.0% [23.5%-30.6%] | -- | -- | -- | -- | PASS | -7.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 144.0, B 1575.0; serve-point win A 51.4%, B 41.6%; Elo A 1375.5, B 1546.6; model uncertainty 0.0355
* Form inputs: days since last match A 322, B 343; matches on record A 98, B 81; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.034, surface_pool_high +0.036, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hernan Casanova vs Gonzalo Bueno -- ATP Challenger Cali R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-19T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19CASBUE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gonzalo Bueno (`KXATPCHALLENGERMATCH-26OCT19CASBUE-BUE`) | 0.60 / 0.62 (6709) | 61.0% | -- | -- | -- [-----] | -- | 62.0% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hernan Casanova (`KXATPCHALLENGERMATCH-26OCT19CASBUE-CAS`) | 0.38 / 0.39 (2195) | 38.5% | -- | -- | -- [-----] | -- | 36.2% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Luciano Emanuel Ambrogi vs Patrick Maloney -- ATP Challenger Fort Worth R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-19T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19AMBMAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luciano Emanuel Ambrogi (`KXATPCHALLENGERMATCH-26OCT19AMBMAL-AMB`) | 0.12 / 0.15 (333) | 13.5% | -- | -- | -- [-----] | -- | 15.2% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Patrick Maloney (`KXATPCHALLENGERMATCH-26OCT19AMBMAL-MAL`) | 0.84 / 0.88 (7278) | 86.0% | -- | -- | -- [-----] | -- | 84.8% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Daniel Milavsky vs Govind Nanda -- ATP Challenger Fort Worth R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-19T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19MILNAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Milavsky (`KXATPCHALLENGERMATCH-26OCT19MILNAN-MIL`) | 0.76 / 0.78 (377) | 77.0% | -- | -- | -- [-----] | -- | 74.3% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Govind Nanda (`KXATPCHALLENGERMATCH-26OCT19MILNAN-NAN`) | 0.22 / 0.24 (29) | 23.0% | -- | -- | -- [-----] | -- | 25.7% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Gabriel Schenekenberg vs Glauco Pinheiro da Cruz Junior -- M15 Maceio R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19SCHPIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Glauco Pinheiro da Cruz Junior (`KXITFMATCH-26OCT19SCHPIN-PIN`) | 0.15 / 0.28 (35) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gabriel Schenekenberg (`KXITFMATCH-26OCT19SCHPIN-SCH`) | 0.68 / 0.81 (30) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rocco Valente vs Lorenzo Sverzut Corsini -- M15 Maceio R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19VALSVE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Sverzut Corsini (`KXITFMATCH-26OCT19VALSVE-SVE`) | 0.18 / 0.24 (38) | 21.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rocco Valente (`KXITFMATCH-26OCT19VALSVE-VAL`) | 0.72 / 0.79 (6154) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Edward Winter vs Timo Legout -- ATP Challenger Fort Worth R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-19T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19WINLEG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Timo Legout (`KXATPCHALLENGERMATCH-26OCT19WINLEG-LEG`) | 0.74 / 0.76 (6236) | 75.0% | -- | -- | -- [-----] | -- | 76.0% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Edward Winter (`KXATPCHALLENGERMATCH-26OCT19WINLEG-WIN`) | 0.23 / 0.24 (100) | 23.5% | -- | -- | -- [-----] | -- | 25.4% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Brantmeier / Tanguilig vs Arseneault / Lacasse -- W75 Saguenay R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-19T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19BRATANARSLAC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arseneault / Lacasse (`KXITFWDOUBLES-26OCT19BRATANARSLAC-ARSLAC`) | 0.08 / 0.68 (78) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Brantmeier / Tanguilig (`KXITFWDOUBLES-26OCT19BRATANARSLAC-BRATAN`) | 0.08 / 0.49 (49) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Sofia Elena Cabezas Dominguez vs Amelie Van Impe -- W50 Austin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-19T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221982:228909:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Elena Cabezas Dominguez (`KXITFWMATCH-26OCT19CABVAN-CAB`) | 0.32 / 0.43 (99) | 37.5% | 54.0% | 52.7% | 52.7% [48.4%-56.4%] | -- | -- | -- | -- | PASS | +16.5 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amelie Van Impe (`KXITFWMATCH-26OCT19CABVAN-VAN`) | 0.53 / 0.65 (98) | 59.0% | 46.0% | 47.3% | 47.3% [43.6%-51.6%] | -- | -- | -- | -- | PASS | -13.0 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1826.0, B 1949.0; serve-point win A 55.1%, B 45.6%; Elo A 1484.8, B 1462.5; model uncertainty 0.0397
* Form inputs: days since last match A 182, B 196; matches on record A 71, B 185; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT19CABVAN-CAB  (YES = Sofia Elena Cabezas Dominguez)
Model: 54%
Kalshi: 38%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.026, surface_dev_loose +0.037, surface_dev_tight -0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thea Frodin vs Adriana Reami -- W50 Austin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-19T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222299:264140:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thea Frodin (`KXITFWMATCH-26OCT19FROREA-FRO`) | 0.69 / 0.75 (64) | 72.0% | 56.9% | 73.4% | 48.9% [43.6%-54.2%] | -- | -- | -- | -- | PASS | -15.1 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Adriana Reami (`KXITFWMATCH-26OCT19FROREA-REA`) | 0.21 / 0.27 (37) | 24.0% | 43.1% | 26.7% | 51.1% [45.8%-56.4%] | -- | -- | -- | -- | PASS | +19.1 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1232.0, B 549.0; serve-point win A 56.4%, B 44.9%; Elo A 1374.0, B 1445.5; model uncertainty 0.0529
* Form inputs: days since last match A 48, B 175; matches on record A 36, B 185; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT19FROREA-REA  (YES = Adriana Reami)
Model: 43%
Kalshi: 24%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.053, surface_pool_high -0.048, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuliya Hatouka vs Rebecca Munk Mortensen -- W50 Austin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-19T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216013:241714:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuliya Hatouka (`KXITFWMATCH-26OCT19HATMUN-HAT`) | 0.58 / 0.65 (44) | 61.5% | 73.2% | 74.0% | 72.7% [70.0%-74.5%] | -- | -- | -- | -- | PASS | +11.7 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rebecca Munk Mortensen (`KXITFWMATCH-26OCT19HATMUN-MUN`) | 0.29 / 0.40 (67) | 34.5% | 26.8% | 26.0% | 27.3% [25.5%-30.0%] | -- | -- | -- | -- | PASS | -7.7 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2126.0, B 1668.0; serve-point win A 54.6%, B 50.0%; Elo A 1626.6, B 1472.8; model uncertainty 0.0225
* Form inputs: days since last match A 196, B 175; matches on record A 378, B 166; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.009, surface_dev_loose +0.018, surface_dev_tight -0.018
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hosogi / Naito vs Abe / Yoshioka -- W75 Saguenay R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-19T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19HOSNAIABEYOS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Abe / Yoshioka (`KXITFWDOUBLES-26OCT19HOSNAIABEYOS-ABEYOS`) | 0.08 / 0.84 (156) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hosogi / Naito (`KXITFWDOUBLES-26OCT19HOSNAIABEYOS-HOSNAI`) | 0.05 / 0.29 (35) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Nadia Lagaev vs Carolina Kuhl -- W75 Saguenay R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:230882:263687:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carolina Kuhl (`KXITFWMATCH-26OCT19LAGKUH-KUH`) | 0.64 / 0.65 (71) | 64.5% | 64.0% | 49.5% | 61.1% [58.5%-64.6%] | -- | -- | -- | -- | PASS | -0.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nadia Lagaev (`KXITFWMATCH-26OCT19LAGKUH-LAG`) | 0.29 / 0.34 (3) | 31.5% | 35.9% | 50.5% | 38.9% [35.4%-41.5%] | -- | -- | -- | -- | PASS | +4.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 724.0, B 1139.0; serve-point win A 52.2%, B 45.1%; Elo A 1386.2, B 1506.5; model uncertainty 0.0305
* Form inputs: days since last match A 224, B 182; matches on record A 33, B 165; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Varvara Lepchenko vs Christasha McNeil -- W50 Austin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-19T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:201478:266937:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Varvara Lepchenko (`KXITFWMATCH-26OCT19LEPMCN-LEP`) | 0.80 / 0.85 (6178) | 82.5% | 77.4% | 47.4% | 63.9% [56.8%-77.9%] | -- | -- | -- | -- | PASS | -5.1 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Christasha McNeil (`KXITFWMATCH-26OCT19LEPMCN-MCN`) | 0.12 / 0.22 (46) | 17.0% | 22.6% | 52.6% | 36.1% [22.1%-43.2%] | -- | -- | -- | -- | PASS | +5.6 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4973.0, B 1523.0; serve-point win A 60.4%, B 45.3%; Elo A 1707.5, B 1490.4; model uncertainty 0.1056
* Form inputs: days since last match A 20, B 350; matches on record A 1226, B 49; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.020, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bayerlova / Gimbrere vs Grubor / Hrda -- W75 Saguenay R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-19T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19BAYGIMGRUHRD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bayerlova / Gimbrere (`KXITFWDOUBLES-26OCT19BAYGIMGRUHRD-BAYGIM`) | 0.08 / 0.95 (136) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Grubor / Hrda (`KXITFWDOUBLES-26OCT19BAYGIMGRUHRD-GRUHRD`) | 0.05 / 0.13 (28) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## bautista de la Pena vs Pedro Albuquerque Dietrich -- M15 Maceio R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19DELALB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pedro Albuquerque Dietrich (`KXITFMATCH-26OCT19DELALB-ALB`) | 0.64 / 0.73 (50) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| bautista de la Pena (`KXITFMATCH-26OCT19DELALB-DEL`) | 0.21 / 0.31 (7) | 26.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valentin Garay vs Kaua Lorenzo Santos Gava -- M15 Maceio R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-19T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211732:212864:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentin Garay (`KXITFMATCH-26OCT19GARSAN-GAR`) | 0.24 / 0.34 (32) | 29.0% | 68.5% | 61.6% | 60.1% [60.0%-60.2%] | -- | -- | -- | -- | PASS | +39.5 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Kaua Lorenzo Santos Gava (`KXITFMATCH-26OCT19GARSAN-SAN`) | 0.61 / 0.71 (41) | 66.0% | 31.5% | 38.4% | 39.9% [39.8%-40.0%] | -- | -- | -- | -- | PASS | -34.5 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 49.0; serve-point win A 63.0%, B 40.8%; Elo A 1279.9, B 1211.3; model uncertainty 0.0006
* Form inputs: days since last match A 777, B 756; matches on record A 7, B 5; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT19GARSAN-GAR  (YES = Valentin Garay)
Model: 69%
Kalshi: 29%
Gap: +40 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cabio / Thibault vs Dartron / Rouvroy -- W75 Saguenay R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-19T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19CABTHIDARROU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cabio / Thibault (`KXITFWDOUBLES-26OCT19CABTHIDARROU-CABTHI`) | 0.05 / 0.95 (136) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dartron / Rouvroy (`KXITFWDOUBLES-26OCT19CABTHIDARROU-DARROU`) | 0.05 / 0.95 (136) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Cross / Rogers vs Alexander / Mercier -- W75 Saguenay R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-19T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19CROROGALEMER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander / Mercier (`KXITFWDOUBLES-26OCT19CROROGALEMER-ALEMER`) | 0.05 / 0.06 (26) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cross / Rogers (`KXITFWDOUBLES-26OCT19CROROGALEMER-CROROG`) | 0.88 / 0.95 (217) | 91.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jenson Brooksby vs Mitchell Krueger -- ATP Challenger Fort Worth R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 23:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-19T23:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19BROKRU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jenson Brooksby (`KXATPCHALLENGERMATCH-26OCT19BROKRU-BRO`) | 0.71 / 0.90 (251) | 80.5% | -- | -- | -- [-----] | -- | 86.3% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mitchell Krueger (`KXATPCHALLENGERMATCH-26OCT19BROKRU-KRU`) | 0.07 / 0.14 (165) | 10.5% | -- | -- | -- [-----] | -- | 13.5% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; WIDE_SPREAD

## Max Hans Rehberg vs Mees Rottgering -- ATP Challenger Fort Worth R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-19 23:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-19T23:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19REHROT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Max Hans Rehberg (`KXATPCHALLENGERMATCH-26OCT19REHROT-REH`) | 0.40 / 0.44 (422) | 42.0% | -- | -- | -- [-----] | -- | 41.3% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mees Rottgering (`KXATPCHALLENGERMATCH-26OCT19REHROT-ROT`) | 0.56 / 0.59 (49) | 57.5% | -- | -- | -- [-----] | -- | 58.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Raquel Caballero Chica vs Madison Brengle -- W50 Austin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-20 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-20T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:201483:231636:2026-10-20`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Madison Brengle (`KXITFWMATCH-26OCT19CABBRE-BRE`) | 0.90 / 0.92 (59) | 91.0% | 98.5% | 76.6% | 95.1% [94.9%-96.1%] | -- | -- | -- | -- | PASS | +7.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Raquel Caballero Chica (`KXITFWMATCH-26OCT19CABBRE-CAB`) | 0.05 / 0.10 (10) | 7.5% | 1.5% | 23.4% | 4.9% [3.9%-5.1%] | -- | -- | -- | -- | PASS | -6.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 74.0, B 2464.0; serve-point win A 43.5%, B 40.3%; Elo A 1208.9, B 1752.5; model uncertainty 0.0061
* Form inputs: days since last match A 518, B 54; matches on record A 25, B 1012; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.006, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kylie Collins vs Anastasia Abbagnato -- W50 Austin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-20 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-20T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220891:221031:2026-10-20`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasia Abbagnato (`KXITFWMATCH-26OCT19COLABB-ABB`) | 0.19 / 0.20 (5) | 19.5% | 44.5% | 42.5% | 48.9% [46.8%-54.8%] | -- | -- | -- | -- | WATCH | +25.0 pp | HIGH_REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kylie Collins (`KXITFWMATCH-26OCT19COLABB-COL`) | 0.79 / 0.80 (44) | 79.5% | 55.5% | 57.5% | 51.1% [45.2%-53.2%] | -- | -- | -- | -- | PASS | -24.0 pp | HIGH_REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2145.0, B 1964.0; serve-point win A 51.7%, B 49.3%; Elo A 1438.8, B 1490.9; model uncertainty 0.0401
* Form inputs: days since last match A 28, B 90; matches on record A 126, B 220; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT19COLABB-ABB  (YES = Anastasia Abbagnato)
Model: 44%
Kalshi: 20%
Gap: +25 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Barbora Palicova vs Luciana Perry -- W50 Austin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-20 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-20T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223323:267920:2026-10-20`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barbora Palicova (`KXITFWMATCH-26OCT19PALPER-PAL`) | 0.69 / 0.81 (19) | 75.0% | 90.7% | 72.9% | 77.5% [73.8%-81.7%] | -- | -- | -- | -- | PASS | +15.7 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luciana Perry (`KXITFWMATCH-26OCT19PALPER-PER`) | 0.19 / 0.23 (65) | 21.0% | 9.3% | 27.1% | 22.5% [18.3%-26.2%] | -- | -- | -- | -- | PASS | -11.7 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2850.0, B 141.0; serve-point win A 60.7%, B 49.3%; Elo A 1576.8, B 1355.3; model uncertainty 0.0395
* Form inputs: days since last match A 7, B 504; matches on record A 350, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT19PALPER-PAL  (YES = Barbora Palicova)
Model: 91%
Kalshi: 75%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.034, surface_pool_high -0.037, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sonja Zhiyenbayeva vs Anastasia Tikhonova -- W50 Austin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-20 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-20T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221073:260306:2026-10-20`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasia Tikhonova (`KXITFWMATCH-26OCT19ZHITIK-TIK`) | 0.44 / 0.46 (362) | 45.0% | 62.2% | 43.2% | 57.4% [54.2%-61.5%] | -- | -- | -- | -- | PASS | +17.2 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sonja Zhiyenbayeva (`KXITFWMATCH-26OCT19ZHITIK-ZHI`) | 0.51 / 0.54 (20) | 52.5% | 37.8% | 56.8% | 42.6% [38.6%-45.8%] | -- | -- | -- | -- | PASS | -14.7 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 112.0, B 2660.0; serve-point win A 55.2%, B 42.4%; Elo A 1511.7, B 1574.6; model uncertainty 0.0362
* Form inputs: days since last match A 192, B 15; matches on record A 61, B 387; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT19ZHITIK-TIK  (YES = Anastasia Tikhonova)
Model: 62%
Kalshi: 45%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.031, surface_pool_high -0.041, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## El Jardi / Frodin vs Johnson / Elizabeth Reasco Gonzalez -- W50 Austin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-20 01:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-20T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19ELJFROJOHELI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| El Jardi / Frodin (`KXITFWDOUBLES-26OCT19ELJFROJOHELI-ELJFRO`) | 0.46 / 0.73 (27) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Johnson / Elizabeth Reasco Gonzalez (`KXITFWDOUBLES-26OCT19ELJFROJOHELI-JOHELI`) | 0.08 / 0.55 (10) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Lahey / Vagramov vs Rapolu / Rus -- W50 Austin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-20 01:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-20T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19LAHVAGRAPRUS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lahey / Vagramov (`KXITFWDOUBLES-26OCT19LAHVAGRAPRUS-LAHVAG`) | 0.08 / 0.54 (54) | 31.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rapolu / Rus (`KXITFWDOUBLES-26OCT19LAHVAGRAPRUS-RAPRUS`) | 0.08 / 0.67 (75) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Munk Mortensen / Nilsson vs Bulatova / Lincer -- W50 Austin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-20 01:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-20T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19MUNNILBULLIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bulatova / Lincer (`KXITFWDOUBLES-26OCT19MUNNILBULLIN-BULLIN`) | 0.32 / 0.41 (0) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Munk Mortensen / Nilsson (`KXITFWDOUBLES-26OCT19MUNNILBULLIN-MUNNIL`) | 0.05 / 0.68 (10) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Osborne / Urhobo vs Osuigwe / Smith -- W50 Austin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-20 01:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-20T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19OSBURHOSUSMI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Osborne / Urhobo (`KXITFWDOUBLES-26OCT19OSBURHOSUSMI-OSBURH`) | 0.08 / 0.46 (46) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Osuigwe / Smith (`KXITFWDOUBLES-26OCT19OSBURHOSUSMI-OSUSMI`) | 0.32 / 0.74 (96) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Ann Li vs Emerson Jones -- WTA Osaka R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-19 04:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-20 02:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-20 01:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-19T04:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215983:263644:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ann Li (`KXWTAMATCH-26OCT18ANNJON-ANN`) | 0.71 / 0.72 (9184) | 71.5% | 62.3% | 49.5% | 54.7% [51.0%-64.3%] | -- | -- | -- | -- | PASS | -9.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Emerson Jones (`KXWTAMATCH-26OCT18ANNJON-JON`) | 0.27 / 0.28 (6) | 27.5% | 37.7% | 50.5% | 45.3% [35.7%-49.0%] | -- | -- | -- | -- | WATCH | +10.2 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4567.0, B 3547.0; serve-point win A 59.7%, B 42.6%; Elo A 1913.2, B 1796.1; model uncertainty 0.0665
* Form inputs: days since last match A 2, B 0; matches on record A 471, B 150; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.021, surface_dev_loose -0.000, surface_dev_tight +0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT18ANNJON-21` Over 20.5 games: 0.50/0.51 mid 50.5%, model 63.8% (market_conditioned_v1 (model4_board_v1)) -- gap +13.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT18ANNJON-2-JON` Will Emerson Jones win set 2 in the Ann Li vs Emerson Jones match: 0.24/0.36 mid 30.0%, model 41.7% (projection_v2.0 (prediction ledger)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT18ANNJON-2-ANN` Will Ann Li win set 2 in the Ann Li vs Emerson Jones match: 0.60/0.76 mid 68.0%, model 58.3% (projection_v2.0 (prediction ledger)) -- gap -9.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT18ANNJON-26` Over 25.5 games: 0.26/0.38 mid 32.0%, model 40.8% (market_conditioned_v1 (model4_board_v1)) -- gap +8.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT18ANNJON-1-JON` Will Emerson Jones win set 1 in the Ann Li vs Emerson Jones match: 0.31/0.35 mid 33.0%, model 41.7% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT18ANNJON-1-ANN` Will Ann Li win set 1 in the Ann Li vs Emerson Jones match: 0.65/0.68 mid 66.5%, model 58.3% (projection_v2.0 (prediction ledger)) -- gap -8.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT18ANNJON-16` Over 15.5 games: 0.86/0.97 mid 91.5%, model 96.6% (market_conditioned_v1 (model4_board_v1)) -- gap +5.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Claire Liu vs Magda Linette -- WTA Osaka R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-19 04:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-20 02:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-20 01:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-19T04:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202663:214906:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Magda Linette (`KXWTAMATCH-26OCT18LIULIN-LIN`) | 0.38 / 0.39 (5183) | 38.5% | 53.9% | 47.4% | 52.1% [50.0%-55.8%] | -- | -- | -- | -- | SHADOW_BET | +15.4 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Claire Liu (`KXWTAMATCH-26OCT18LIULIN-LIU`) | 0.61 / 0.63 (9071) | 62.0% | 46.1% | 52.6% | 47.9% [44.2%-50.0%] | -- | -- | -- | -- | PASS | -15.9 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3837.0, B 4278.0; serve-point win A 57.3%, B 42.0%; Elo A 1772.6, B 1875.2; model uncertainty 0.0288
* Form inputs: days since last match A 0, B 8; matches on record A 456, B 909; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT18LIULIN-LIN  (YES = Magda Linette)
Model: 54%
Kalshi: 38%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.026, surface_dev_loose +0.005, surface_dev_tight -0.016
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTASETWINNER-26OCT18LIULIN-1-LIN` Will Magda Linette win set 1 in the Claire Liu vs Magda Linette match: 0.39/0.43 mid 41.0%, model 52.6% (projection_v2.0 (prediction ledger)) -- gap +11.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT18LIULIN-1-LIU` Will Claire Liu win set 1 in the Claire Liu vs Magda Linette match: 0.57/0.61 mid 59.0%, model 47.4% (projection_v2.0 (prediction ledger)) -- gap -11.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT18LIULIN-23` Over 22.5 games: 0.44/0.45 mid 44.5%, model 55.7% (market_conditioned_v1 (model4_board_v1)) -- gap +11.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT18LIULIN-2-LIU` Will Claire Liu win set 2 in the Claire Liu vs Magda Linette match: 0.45/0.72 mid 58.5%, model 47.4% (projection_v2.0 (prediction ledger)) -- gap -11.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT18LIULIN-28` Over 27.5 games: 0.19/0.31 mid 25.0%, model 34.5% (market_conditioned_v1 (model4_board_v1)) -- gap +9.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT18LIULIN-18` Over 17.5 games: 0.75/0.84 mid 79.5%, model 88.1% (market_conditioned_v1 (model4_board_v1)) -- gap +8.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT18LIULIN-2-LIN` Will Magda Linette win set 2 in the Claire Liu vs Magda Linette match: 0.30/0.58 mid 44.0%, model 52.6% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tereza Valentova vs Shuai Zhang -- WTA Osaka R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-19 05:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-20 02:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-20 01:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-19T05:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:201533:238184:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tereza Valentova (`KXWTAMATCH-26OCT18VALZHA-VAL`) | 0.69 / 0.70 (6433) | 69.5% | 67.1% | 58.9% | 58.9% [56.8%-61.5%] | -- | -- | -- | -- | PASS | -2.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Shuai Zhang (`KXWTAMATCH-26OCT18VALZHA-ZHA`) | 0.30 / 0.31 (876) | 30.5% | 32.9% | 41.1% | 41.1% [38.5%-43.2%] | -- | -- | -- | -- | SHADOW_BET | +2.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3231.0, B 3846.0; serve-point win A 57.9%, B 45.4%; Elo A 1904.1, B 1846.8; model uncertainty 0.0232
* Form inputs: days since last match A 51, B 6; matches on record A 166, B 1067; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.021, surface_dev_loose -0.005, surface_dev_tight +0.010
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT18VALZHA-15` Over 14.5 games: 0.54/0.99 mid 76.5%, model 98.8% (projection_v2.0 (prediction ledger)) -- gap +22.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT18VALZHA-20` Over 19.5 games: 0.56/0.58 mid 57.0%, model 71.7% (projection_v2.0 (prediction ledger)) -- gap +14.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT18VALZHA-25` Over 24.5 games: 0.29/0.41 mid 35.0%, model 46.5% (projection_v2.0 (prediction ledger)) -- gap +11.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT18VALZHA-1-ZHA` Will Shuai Zhang win set 1 in the Tereza Valentova vs Shuai Zhang match: 0.31/0.36 mid 33.5%, model 38.4% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT18VALZHA-2-VAL` Will Tereza Valentova win set 2 in the Tereza Valentova vs Shuai Zhang match: 0.60/0.73 mid 66.5%, model 61.6% (projection_v2.0 (prediction ledger)) -- gap -4.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT18VALZHA-1-VAL` Will Tereza Valentova win set 1 in the Tereza Valentova vs Shuai Zhang match: 0.64/0.66 mid 65.0%, model 61.6% (projection_v2.0 (prediction ledger)) -- gap -3.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT18VALZHA-2-ZHA` Will Shuai Zhang win set 2 in the Tereza Valentova vs Shuai Zhang match: 0.25/0.49 mid 37.0%, model 38.4% (projection_v2.0 (prediction ledger)) -- gap +1.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Paula Badosa vs Antonia Ruzic -- WTA Osaka R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-19 05:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-20 04:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-20 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-19T05:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211651:222045:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Paula Badosa (`KXWTAMATCH-26OCT18BADRUZ-BAD`) | 0.72 / 0.73 (3) | 72.5% | 65.4% | 63.4% | 64.8% [60.9%-71.0%] | -- | -- | -- | -- | PASS | -7.1 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Antonia Ruzic (`KXWTAMATCH-26OCT18BADRUZ-RUZ`) | 0.26 / 0.27 (150) | 26.5% | 34.6% | 36.6% | 35.1% [29.0%-39.1%] | -- | -- | -- | -- | WATCH | +8.1 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3479.0, B 4066.0; serve-point win A 59.1%, B 43.9%; Elo A 1962.1, B 1838.3; model uncertainty 0.0507
* Form inputs: days since last match A 16, B 4; matches on record A 612, B 359; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.029, surface_pool_high -0.040, surface_dev_loose -0.005, surface_dev_tight +0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT18BADRUZ-21` Over 20.5 games: 0.50/0.53 mid 51.5%, model 66.3% (projection_v2.0 (prediction ledger)) -- gap +14.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT18BADRUZ-26` Over 25.5 games: 0.26/0.35 mid 30.5%, model 43.2% (projection_v2.0 (prediction ledger)) -- gap +12.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT18BADRUZ-1-RUZ` Will Antonia Ruzic win set 1 in the Paula Badosa vs Antonia Ruzic match: 0.29/0.33 mid 31.0%, model 39.6% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT18BADRUZ-2-BAD` Will Paula Badosa win set 2 in the Paula Badosa vs Antonia Ruzic match: 0.67/0.71 mid 69.0%, model 60.4% (projection_v2.0 (prediction ledger)) -- gap -8.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT18BADRUZ-1-BAD` Will Paula Badosa win set 1 in the Paula Badosa vs Antonia Ruzic match: 0.67/0.69 mid 68.0%, model 60.4% (projection_v2.0 (prediction ledger)) -- gap -7.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT18BADRUZ-2-RUZ` Will Antonia Ruzic win set 2 in the Paula Badosa vs Antonia Ruzic match: 0.28/0.36 mid 32.0%, model 39.6% (projection_v2.0 (prediction ledger)) -- gap +7.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26OCT18BADRUZ-16` Over 15.5 games: 0.84/0.96 mid 90.0%, model 97.0% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Oleksandra Oliynykova vs Mary Stoiana -- WTA Osaka R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-19 04:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-20 04:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-20 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-19T04:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220716:223168:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oleksandra Oliynykova (`KXWTAMATCH-26OCT18OLISTO-OLI`) | 0.33 / 0.34 (26469) | 33.5% | 37.4% | 60.5% | 49.5% [44.2%-53.7%] | -- | -- | -- | -- | SHADOW_BET | +3.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mary Stoiana (`KXWTAMATCH-26OCT18OLISTO-STO`) | 0.67 / 0.68 (258) | 67.5% | 62.6% | 39.5% | 50.5% [46.3%-55.8%] | -- | -- | -- | -- | PASS | -4.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4041.0, B 2840.0; serve-point win A 54.7%, B 42.9%; Elo A 1658.9, B 1805.4; model uncertainty 0.0475
* Form inputs: days since last match A 10, B 0; matches on record A 438, B 142; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.037, surface_pool_high -0.032, surface_dev_loose -0.016, surface_dev_tight +0.021
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT18OLISTO-1-OLI` Will Oleksandra Oliynykova win set 1 in the Oleksandra Oliynykova vs Mary Stoiana match: 0.34/0.37 mid 35.5%, model 41.5% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT18OLISTO-1-STO` Will Mary Stoiana win set 1 in the Oleksandra Oliynykova vs Mary Stoiana match: 0.63/0.66 mid 64.5%, model 58.5% (projection_v2.0 (prediction ledger)) -- gap -6.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT18OLISTO-2-STO` Will Mary Stoiana win set 2 in the Oleksandra Oliynykova vs Mary Stoiana match: 0.52/0.75 mid 63.5%, model 58.5% (projection_v2.0 (prediction ledger)) -- gap -5.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT18OLISTO-2-OLI` Will Oleksandra Oliynykova win set 2 in the Oleksandra Oliynykova vs Mary Stoiana match: 0.25/0.50 mid 37.5%, model 41.5% (projection_v2.0 (prediction ledger)) -- gap +4.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Moyuka Uchijima vs Ena Shibahara -- WTA Osaka R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-19 05:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-20 04:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-20 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-19T05:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214262:220416:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ena Shibahara (`KXWTAMATCH-26OCT18UCHSHI-SHI`) | 0.41 / 0.42 (14942) | 41.5% | 35.4% | 35.9% | 37.3% [36.4%-38.7%] | -- | -- | -- | -- | PASS | -6.1 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Moyuka Uchijima (`KXWTAMATCH-26OCT18UCHSHI-UCH`) | 0.59 / 0.60 (6150) | 59.5% | 64.6% | 64.1% | 62.7% [61.3%-63.6%] | -- | -- | -- | -- | PASS | +5.1 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4591.0, B 3247.0; serve-point win A 61.4%, B 41.5%; Elo A 1743.0, B 1676.2; model uncertainty 0.0119
* Form inputs: days since last match A 9, B 203; matches on record A 473, B 249; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose +0.009, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT18UCHSHI-22` Over 21.5 games: 0.51/0.52 mid 51.5%, model 63.2% (projection_v2.0 (prediction ledger)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT18UCHSHI-27` Over 26.5 games: 0.24/0.36 mid 30.0%, model 40.0% (projection_v2.0 (prediction ledger)) -- gap +10.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT18UCHSHI-2-SHI` Will Ena Shibahara win set 2 in the Moyuka Uchijima vs Ena Shibahara match: 0.41/0.57 mid 49.0%, model 40.1% (projection_v2.0 (prediction ledger)) -- gap -8.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26OCT18UCHSHI-17` Over 16.5 games: 0.82/0.92 mid 87.0%, model 94.8% (projection_v2.0 (prediction ledger)) -- gap +7.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT18UCHSHI-2-UCH` Will Moyuka Uchijima win set 2 in the Moyuka Uchijima vs Ena Shibahara match: 0.49/0.58 mid 53.5%, model 59.9% (projection_v2.0 (prediction ledger)) -- gap +6.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT18UCHSHI-1-UCH` Will Moyuka Uchijima win set 1 in the Moyuka Uchijima vs Ena Shibahara match: 0.55/0.58 mid 56.5%, model 59.9% (projection_v2.0 (prediction ledger)) -- gap +3.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT18UCHSHI-1-SHI` Will Ena Shibahara win set 1 in the Moyuka Uchijima vs Ena Shibahara match: 0.40/0.45 mid 42.5%, model 40.1% (projection_v2.0 (prediction ledger)) -- gap -2.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Oliver Clark Anderson vs Nikolas Baker -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-20 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-20T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19ANDBAK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oliver Clark Anderson (`KXITFMATCH-26OCT19ANDBAK-AND`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nikolas Baker (`KXITFMATCH-26OCT19ANDBAK-BAK`) | 0.03 / 0.97 (311) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ethan Cook vs Derek Pham -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-20 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-20T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19COOPHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ethan Cook (`KXITFMATCH-26OCT19COOPHA-COO`) | 0.05 / 0.96 (22) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Derek Pham (`KXITFMATCH-26OCT19COOPHA-PHA`) | 0.03 / 0.97 (311) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Harrison Satara vs Heaton Pann -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-20 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-20T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19SATPAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Heaton Pann (`KXITFMATCH-26OCT19SATPAN-PAN`) | 0.05 / 0.95 (99) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Harrison Satara (`KXITFMATCH-26OCT19SATPAN-SAT`) | 0.04 / 0.96 (99) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eric Tripathi vs Matthew Shearer -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-20 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-20T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19TRISHE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthew Shearer (`KXITFMATCH-26OCT19TRISHE-SHE`) | 0.05 / 0.95 (99) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eric Tripathi (`KXITFMATCH-26OCT19TRISHE-TRI`) | 0.03 / 0.97 (311) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leyla Fiorella Britez Risso vs Angela Cui -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-20 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-20T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19BRICUI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leyla Fiorella Britez Risso (`KXITFWMATCH-26OCT19BRICUI-BRI`) | 0.23 / 0.97 (233) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Angela Cui (`KXITFWMATCH-26OCT19BRICUI-CUI`) | 0.03 / 0.06 (26) | 4.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cristina Bucsa vs Polina Kudermetova -- WTA Ningbo R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-20 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-20T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-10-20T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213710:221236:2026-10-20`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cristina Bucsa (`KXWTAMATCH-26OCT19BUCKUD-BUC`) | 0.50 / 0.52 (8375) | 51.0% | 50.0% | 56.3% | 55.3% [52.1%-56.3%] | 51.1% | -- | 51.1% | MARKETS_AGREE | WATCH | -1.0 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Polina Kudermetova (`KXWTAMATCH-26OCT19BUCKUD-KUD`) | 0.48 / 0.50 (376) | 49.0% | 50.0% | 43.7% | 44.7% [43.7%-47.9%] | 48.9% | -- | 48.9% | MARKETS_AGREE | PASS | +1.0 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4493.0, B 4285.0; serve-point win A 55.9%, B 44.1%; Elo A 1837.9, B 1810.4; model uncertainty 0.021
* Form inputs: days since last match A 6, B 1; matches on record A 588, B 389; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.011, surface_dev_loose -0.000, surface_dev_tight +0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT19BUCKUD-21` Over 20.5 games: 0.56/0.58 mid 57.0%, model 67.8% (projection_v2.0 (prediction ledger)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT19BUCKUD-26` Over 25.5 games: 0.28/0.40 mid 34.0%, model 44.5% (projection_v2.0 (prediction ledger)) -- gap +10.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT19BUCKUD-2-BUC` Will Cristina Bucsa win set 2 in the Cristina Bucsa vs Polina Kudermetova match: 0.45/0.74 mid 59.5%, model 50.0% (projection_v2.0 (prediction ledger)) -- gap -9.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT19BUCKUD-16` Over 15.5 games: 0.88/0.98 mid 93.0%, model 97.2% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT19BUCKUD-2-KUD` Will Polina Kudermetova win set 2 in the Cristina Bucsa vs Polina Kudermetova match: 0.41/0.57 mid 49.0%, model 50.0% (projection_v2.0 (prediction ledger)) -- gap +1.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT19BUCKUD-1-BUC` Will Cristina Bucsa win set 1 in the Cristina Bucsa vs Polina Kudermetova match: 0.48/0.53 mid 50.5%, model 50.0% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT19BUCKUD-1-KUD` Will Polina Kudermetova win set 1 in the Cristina Bucsa vs Polina Kudermetova match: 0.47/0.52 mid 49.5%, model 50.0% (projection_v2.0 (prediction ledger)) -- gap +0.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nanari Katsumi vs Larisa Arnautovic -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-20 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-20T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19KATARN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Larisa Arnautovic (`KXITFWMATCH-26OCT19KATARN-ARN`) | 0.04 / 0.38 (40) | 21.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nanari Katsumi (`KXITFWMATCH-26OCT19KATARN-KAT`) | 0.63 / 0.82 (2) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Katarzyna Kawa vs Daria Snigur -- WTA Ningbo R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-20 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-20T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-10-20T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:203514:220750:2026-10-20`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katarzyna Kawa (`KXWTAMATCH-26OCT19KAWSNI-KAW`) | 0.20 / 0.21 (234) | 20.5% | 12.9% | 3.6% | 5.6% [3.9%-16.2%] | 22.5% | -- | 22.5% | EXTERNAL_LONE_OUTLIER | PASS | -7.6 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Daria Snigur (`KXWTAMATCH-26OCT19KAWSNI-SNI`) | 0.78 / 0.80 (961) | 79.0% | 87.1% | 96.4% | 94.4% [83.8%-96.1%] | 77.5% | -- | 77.5% | EXTERNAL_LONE_OUTLIER | SHADOW_BET | +8.1 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4311.0, B 4190.0; serve-point win A 49.1%, B 42.4%; Elo A 1608.7, B 1890.2; model uncertainty 0.0612
* Form inputs: days since last match A 1, B 1; matches on record A 703, B 443; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.004, surface_dev_loose -0.015, surface_dev_tight +0.020
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT19KAWSNI-1-SNI` Will Daria Snigur win set 1 in the Katarzyna Kawa vs Daria Snigur match: 0.72/0.75 mid 73.5%, model 77.5% (projection_v2.0 (prediction ledger)) -- gap +4.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT19KAWSNI-2-KAW` Will Katarzyna Kawa win set 2 in the Katarzyna Kawa vs Daria Snigur match: 0.11/0.30 mid 20.5%, model 22.5% (projection_v2.0 (prediction ledger)) -- gap +2.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT19KAWSNI-2-SNI` Will Daria Snigur win set 2 in the Katarzyna Kawa vs Daria Snigur match: 0.73/0.85 mid 79.0%, model 77.5% (projection_v2.0 (prediction ledger)) -- gap -1.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT19KAWSNI-1-KAW` Will Katarzyna Kawa win set 1 in the Katarzyna Kawa vs Daria Snigur match: 0.16/0.28 mid 22.0%, model 22.5% (projection_v2.0 (prediction ledger)) -- gap +0.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Yuhan Liu vs Naomi McKenzie -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-20 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-20T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19LIUMCK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuhan Liu (`KXITFWMATCH-26OCT19LIUMCK-LIU`) | 0.23 / 0.85 (166) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Naomi McKenzie (`KXITFWMATCH-26OCT19LIUMCK-MCK`) | 0.16 / 0.33 (2) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sera Nishimoto vs Maiko Uchijima -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-20 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-20T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19NISUCH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sera Nishimoto (`KXITFWMATCH-26OCT19NISUCH-NIS`) | 0.23 / 0.69 (80) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maiko Uchijima (`KXITFWMATCH-26OCT19NISUCH-UCH`) | 0.32 / 0.54 (2) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jasmine Paolini vs Anhelina Kalinina -- WTA Ningbo R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-20 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-20T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-10-20T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211148:211843:2026-10-20`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anhelina Kalinina (`KXWTAMATCH-26OCT19PAOKAL-KAL`) | 0.33 / 0.35 (106) | 34.0% | 36.5% | 50.0% | 43.2% [34.5%-45.8%] | 35.4% | -- | 35.4% | MODEL_LONE_OUTLIER | WATCH | +2.5 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Jasmine Paolini (`KXWTAMATCH-26OCT19PAOKAL-PAO`) | 0.64 / 0.67 (1463) | 65.5% | 63.5% | 50.0% | 56.8% [54.2%-65.5%] | 64.6% | -- | 64.6% | MODEL_LONE_OUTLIER | PASS | -2.0 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4852.0, B 4204.0; serve-point win A 57.6%, B 45.0%; Elo A 2005.4, B 1825.0; model uncertainty 0.0562
* Form inputs: days since last match A 4, B 1; matches on record A 711, B 613; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight +0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTASETWINNER-26OCT19PAOKAL-2-PAO` Will Jasmine Paolini win set 2 in the Jasmine Paolini vs Anhelina Kalinina match: 0.60/0.94 mid 77.0%, model 59.1% (projection_v2.0 (prediction ledger)) -- gap -17.9 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT19PAOKAL-21` Over 20.5 games: 0.52/0.54 mid 53.0%, model 66.2% (projection_v2.0 (prediction ledger)) -- gap +13.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT19PAOKAL-26` Over 25.5 games: 0.25/0.37 mid 31.0%, model 43.1% (projection_v2.0 (prediction ledger)) -- gap +12.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT19PAOKAL-1-KAL` Will Anhelina Kalinina win set 1 in the Jasmine Paolini vs Anhelina Kalinina match: 0.27/0.41 mid 34.0%, model 40.9% (projection_v2.0 (prediction ledger)) -- gap +6.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT19PAOKAL-2-KAL` Will Anhelina Kalinina win set 2 in the Jasmine Paolini vs Anhelina Kalinina match: 0.22/0.48 mid 35.0%, model 40.9% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT19PAOKAL-16` Over 15.5 games: 0.86/0.97 mid 91.5%, model 96.8% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT19PAOKAL-1-PAO` Will Jasmine Paolini win set 1 in the Jasmine Paolini vs Anhelina Kalinina match: 0.60/0.63 mid 61.5%, model 59.1% (projection_v2.0 (prediction ledger)) -- gap -2.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Yulia Putintseva vs Diana Shnaider -- WTA Ningbo R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-20 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-20T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-10-20T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:201709:223670:2026-10-20`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yulia Putintseva (`KXWTAMATCH-26OCT19PUTSHN-PUT`) | 0.25 / 0.27 (2660) | 26.0% | 33.5% | 43.7% | 42.1% [36.5%-44.8%] | 27.4% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +7.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Diana Shnaider (`KXWTAMATCH-26OCT19PUTSHN-SHN`) | 0.73 / 0.74 (21) | 73.5% | 66.5% | 56.3% | 57.9% [55.2%-63.4%] | 72.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4366.0, B 4846.0; serve-point win A 55.2%, B 41.6%; Elo A 1895.4, B 1969.8; model uncertainty 0.041
* Form inputs: days since last match A 1, B 3; matches on record A 858, B 320; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.026, surface_dev_loose +0.005, surface_dev_tight +0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTASETWINNER-26OCT19PUTSHN-2-SHN` Will Diana Shnaider win set 2 in the Yulia Putintseva vs Diana Shnaider match: 0.68/0.91 mid 79.5%, model 61.2% (projection_v2.0 (prediction ledger)) -- gap -18.3 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT19PUTSHN-21` Over 20.5 games: 0.48/0.50 mid 49.0%, model 65.5% (projection_v2.0 (prediction ledger)) -- gap +16.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT19PUTSHN-26` Over 25.5 games: 0.24/0.36 mid 30.0%, model 42.5% (projection_v2.0 (prediction ledger)) -- gap +12.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT19PUTSHN-2-PUT` Will Yulia Putintseva win set 2 in the Yulia Putintseva vs Diana Shnaider match: 0.11/0.45 mid 28.0%, model 38.8% (projection_v2.0 (prediction ledger)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT19PUTSHN-1-PUT` Will Yulia Putintseva win set 1 in the Yulia Putintseva vs Diana Shnaider match: 0.28/0.32 mid 30.0%, model 38.8% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT19PUTSHN-1-SHN` Will Diana Shnaider win set 1 in the Yulia Putintseva vs Diana Shnaider match: 0.68/0.71 mid 69.5%, model 61.2% (projection_v2.0 (prediction ledger)) -- gap -8.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT19PUTSHN-16` Over 15.5 games: 0.86/0.97 mid 91.5%, model 96.7% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Maya Joint vs Zeynep Sonmez -- WTA Osaka R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-19 04:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-20 05:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-20 04:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-19T04:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220309:233741:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maya Joint (`KXWTAMATCH-26OCT18JOISON-JOI`) | 0.48 / 0.49 (1084) | 48.5% | 46.4% | 40.5% | 42.6% [41.0%-45.7%] | -- | -- | -- | -- | PASS | -2.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zeynep Sonmez (`KXWTAMATCH-26OCT18JOISON-SON`) | 0.50 / 0.52 (2267) | 51.0% | 53.6% | 59.5% | 57.4% [54.3%-59.0%] | -- | -- | -- | -- | WATCH | +2.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3855.0, B 4355.0; serve-point win A 53.5%, B 45.8%; Elo A 1829.6, B 1832.0; model uncertainty 0.0237
* Form inputs: days since last match A 0, B 5; matches on record A 238, B 427; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.011, surface_dev_loose -0.016, surface_dev_tight +0.021
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT18JOISON-22` Over 21.5 games: 0.50/0.51 mid 50.5%, model 62.0% (market_conditioned_v1 (model4_board_v1)) -- gap +11.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT18JOISON-27` Over 26.5 games: 0.23/0.35 mid 29.0%, model 38.5% (market_conditioned_v1 (model4_board_v1)) -- gap +9.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT18JOISON-17` Over 16.5 games: 0.81/0.92 mid 86.5%, model 92.8% (market_conditioned_v1 (model4_board_v1)) -- gap +6.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT18JOISON-1-SON` Will Zeynep Sonmez win set 1 in the Maya Joint vs Zeynep Sonmez match: 0.49/0.52 mid 50.5%, model 52.4% (projection_v2.0 (prediction ledger)) -- gap +1.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT18JOISON-1-JOI` Will Maya Joint win set 1 in the Maya Joint vs Zeynep Sonmez match: 0.46/0.51 mid 48.5%, model 47.6% (projection_v2.0 (prediction ledger)) -- gap -0.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT18JOISON-2-SON` Will Zeynep Sonmez win set 2 in the Maya Joint vs Zeynep Sonmez match: 0.49/0.54 mid 51.5%, model 52.4% (projection_v2.0 (prediction ledger)) -- gap +0.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT18JOISON-2-JOI` Will Maya Joint win set 2 in the Maya Joint vs Zeynep Sonmez match: 0.45/0.51 mid 48.0%, model 47.6% (projection_v2.0 (prediction ledger)) -- gap -0.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Katerina Siniakova vs Peyton Stearns -- WTA Osaka R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-19 05:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-20 05:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-20 04:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-19T05:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211701:220548:2026-10-19`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katerina Siniakova (`KXWTAMATCH-26OCT18SINSTE-SIN`) | 0.55 / 0.56 (150) | 55.5% | 55.5% | 60.9% | 59.9% [58.9%-60.9%] | -- | -- | -- | -- | WATCH | +0.0 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Peyton Stearns (`KXWTAMATCH-26OCT18SINSTE-STE`) | 0.43 / 0.45 (13558) | 44.0% | 44.5% | 39.1% | 40.1% [39.1%-41.1%] | -- | -- | -- | -- | PASS | +0.5 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4278.0, B 4027.0; serve-point win A 57.8%, B 43.2%; Elo A 1916.2, B 1855.7; model uncertainty 0.0101
* Form inputs: days since last match A 6, B 17; matches on record A 720, B 330; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight +0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT18SINSTE-21` Over 20.5 games: 0.55/0.57 mid 56.0%, model 68.2% (projection_v2.0 (prediction ledger)) -- gap +12.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT18SINSTE-26` Over 25.5 games: 0.28/0.40 mid 34.0%, model 45.0% (projection_v2.0 (prediction ledger)) -- gap +11.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT18SINSTE-16` Over 15.5 games: 0.88/0.98 mid 93.0%, model 97.5% (projection_v2.0 (prediction ledger)) -- gap +4.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT18SINSTE-2-STE` Will Peyton Stearns win set 2 in the Katerina Siniakova vs Peyton Stearns match: 0.43/0.52 mid 47.5%, model 46.3% (projection_v2.0 (prediction ledger)) -- gap -1.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT18SINSTE-1-STE` Will Peyton Stearns win set 1 in the Katerina Siniakova vs Peyton Stearns match: 0.43/0.48 mid 45.5%, model 46.3% (projection_v2.0 (prediction ledger)) -- gap +0.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT18SINSTE-1-SIN` Will Katerina Siniakova win set 1 in the Katerina Siniakova vs Peyton Stearns match: 0.52/0.56 mid 54.0%, model 53.7% (projection_v2.0 (prediction ledger)) -- gap -0.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT18SINSTE-2-SIN` Will Katerina Siniakova win set 2 in the Katerina Siniakova vs Peyton Stearns match: 0.50/0.57 mid 53.5%, model 53.7% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Kayla Day vs Kimberly Birrell -- WTA Osaka R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-20 05:30Z
* Current expected start: 2026-10-20 05:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-20 04:45Z

WTA (TOUR_500_250) · Hard · scheduled 2026-10-20T05:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214040:215037:2026-10-20`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kimberly Birrell (`KXWTAMATCH-26OCT19DAYBIR-BIR`) | 0.48 / 0.64 (3) | 56.0% | 60.1% | 35.7% | 44.8% [40.7%-56.3%] | -- | -- | -- | -- | PASS | +4.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kayla Day (`KXWTAMATCH-26OCT19DAYBIR-DAY`) | 0.26 / 0.46 (6) | 36.0% | 39.9% | 64.3% | 55.2% [43.7%-59.3%] | -- | -- | -- | -- | PASS | +3.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3639.0, B 5020.0; serve-point win A 57.0%, B 41.1%; Elo A 1745.4, B 1875.3; model uncertainty 0.078
* Form inputs: days since last match A 1, B 6; matches on record A 479, B 476; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.016, surface_dev_loose +0.015, surface_dev_tight -0.016
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
* Warnings: NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Cody Atkinson vs Nick Beamish -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-20 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-20T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19ATKBEA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cody Atkinson (`KXITFMATCH-26OCT19ATKBEA-ATK`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nick Beamish (`KXITFMATCH-26OCT19ATKBEA-BEA`) | 0.03 / 0.97 (261) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jeremy Beale vs Luca Connaughton -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-20 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-20T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19BEACON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jeremy Beale (`KXITFMATCH-26OCT19BEACON-BEA`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luca Connaughton (`KXITFMATCH-26OCT19BEACON-CON`) | 0.03 / 0.97 (261) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adrian Correa vs Zaharije-Zak Talic -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-20 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-20T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19CORTAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Correa (`KXITFMATCH-26OCT19CORTAL-COR`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Zaharije-Zak Talic (`KXITFMATCH-26OCT19CORTAL-TAL`) | 0.03 / 0.97 (261) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stefan Storch vs Archie Stewart -- M25 Tamworth R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-20 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-20T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT19STOSTE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Archie Stewart (`KXITFMATCH-26OCT19STOSTE-STE`) | 0.05 / 0.96 (22) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stefan Storch (`KXITFMATCH-26OCT19STOSTE-STO`) | 0.03 / 0.97 (261) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Natsuho Arakawa vs Lucia Gale -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-20 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-20T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19ARAGAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Natsuho Arakawa (`KXITFWMATCH-26OCT19ARAGAL-ARA`) | 0.04 / 0.97 (183) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucia Gale (`KXITFWMATCH-26OCT19ARAGAL-GAL`) | 0.03 / 0.95 (27) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eva Lopez vs Georgia Campbell -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-20 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-20T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19LOPCAM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Georgia Campbell (`KXITFWMATCH-26OCT19LOPCAM-CAM`) | 0.04 / 0.95 (28) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eva Lopez (`KXITFWMATCH-26OCT19LOPCAM-LOP`) | 0.03 / 0.97 (161) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jizelle Sibai vs Ameerah Khan -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-20 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-20T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19SIBKHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ameerah Khan (`KXITFWMATCH-26OCT19SIBKHA-KHA`) | 0.04 / 0.97 (183) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jizelle Sibai (`KXITFWMATCH-26OCT19SIBKHA-SIB`) | 0.03 / 0.97 (161) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## I Wen Wan vs Taylah Lawless -- W35 Sydney R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-20 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-20T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19WANLAW:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Taylah Lawless (`KXITFWMATCH-26OCT19WANLAW-LAW`) | 0.04 / 0.97 (183) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| I Wen Wan (`KXITFWMATCH-26OCT19WANLAW-WAN`) | 0.03 / 0.97 (161) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nicole Fossa Huergo / Peangtarn Plipuech vs Isabelle Haverlag / Lilli Tagger -- WTA Osaka R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-19 05:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-20 07:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-20 06:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-19T05:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18FOSPLIHAVTAG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicole Fossa Huergo / Peangtarn Plipuech (`KXWTADOUBLES-26OCT18FOSPLIHAVTAG-FOSPLI`) | 0.06 / 0.57 (1) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Isabelle Haverlag / Lilli Tagger (`KXWTADOUBLES-26OCT18FOSPLIHAVTAG-HAVTAG`) | 0.06 / 0.73 (1) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alexa Guarachi / Asia Muhammad vs Jesika Maleckova / Miriam Skoch -- WTA Osaka R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-19 05:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-20 07:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-20 06:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-19T05:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18GUAMUHMALSKO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexa Guarachi / Asia Muhammad (`KXWTADOUBLES-26OCT18GUAMUHMALSKO-GUAMUH`) | 0.19 / 0.41 (5) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jesika Maleckova / Miriam Skoch (`KXWTADOUBLES-26OCT18GUAMUHMALSKO-MALSKO`) | 0.30 / 0.63 (59) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Storm Hunter / Janice Tjen vs Ingrid Martins / Sara Sorribes Tormo -- WTA Osaka R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-19 05:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-20 07:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-20 06:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-19T05:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18HUNTJEMARSOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Storm Hunter / Janice Tjen (`KXWTADOUBLES-26OCT18HUNTJEMARSOR-HUNTJE`) | 0.05 / 0.90 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ingrid Martins / Sara Sorribes Tormo (`KXWTADOUBLES-26OCT18HUNTJEMARSOR-MARSOR`) | 0.05 / 0.71 (1) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Claire Liu / Kaitlin Quevedo vs Harriet Dart / Heather Watson -- WTA Osaka R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-20 05:30Z
* Current expected start: 2026-10-20 07:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-20 06:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-20T05:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT19LIUQUEDARWAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harriet Dart / Heather Watson (`KXWTADOUBLES-26OCT19LIUQUEDARWAT-DARWAT`) | 0.07 / 0.93 (1) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Claire Liu / Kaitlin Quevedo (`KXWTADOUBLES-26OCT19LIUQUEDARWAT-LIUQUE`) | 0.07 / 0.93 (1) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Eri Hozumi / Andreja Klepac vs Hao-Ching Chan / Miyu (1994) Kato -- WTA Osaka R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-19 05:30Z (day placeholder, not a start time)
* Current expected start: 2026-10-20 08:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-20 07:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-19T05:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18HOZKLECHAKAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hao-Ching Chan / Miyu (1994) Kato (`KXWTADOUBLES-26OCT18HOZKLECHAKAT-CHAKAT`) | 0.07 / 0.89 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eri Hozumi / Andreja Klepac (`KXWTADOUBLES-26OCT18HOZKLECHAKAT-HOZKLE`) | 0.05 / 0.71 (1) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## James Duckworth vs Luciano Darderi -- ATP Almaty R16

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-20 09:30Z
* Current expected start: 2026-10-20 09:30Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-20 08:45Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-21T04:00:00+00:00 as not a valid time

ATP (TOUR_500_250) · surface ? · scheduled 2026-10-20T09:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT20DUCDAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luciano Darderi (`KXATPMATCH-26OCT20DUCDAR-DAR`) | 0.06 / 0.94 (222) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| James Duckworth (`KXATPMATCH-26OCT20DUCDAR-DUC`) | 0.06 / 0.93 (5714) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Rei Sakamoto vs Karen Khachanov -- ATP Almaty R32

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-20 09:30Z
* Current expected start: 2026-10-20 09:30Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-20 08:45Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-20T04:00:00+00:00 as not a valid time

ATP (TOUR_500_250) · surface ? · scheduled 2026-10-20T09:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT20SAKKHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karen Khachanov (`KXATPMATCH-26OCT20SAKKHA-KHA`) | 0.67 / 0.70 (6114) | 68.5% | -- | -- | -- [-----] | 67.6% | -- | 67.6% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rei Sakamoto (`KXATPMATCH-26OCT20SAKKHA-SAK`) | 0.30 / 0.32 (100) | 31.0% | -- | -- | -- [-----] | 32.4% | -- | 32.4% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sho Shimabukuro vs Roman Safiullin -- ATP Almaty R32

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-20 09:30Z
* Current expected start: 2026-10-20 09:30Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-19 08:15Z
* Recommended handicap-by time: 2026-10-20 08:45Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-20T04:00:00+00:00 as not a valid time

ATP (TOUR_500_250) · surface ? · scheduled 2026-10-20T09:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT20SHISAF:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Roman Safiullin (`KXATPMATCH-26OCT20SHISAF-SAF`) | 0.82 / 0.85 (6561) | 83.5% | -- | -- | -- [-----] | 82.7% | -- | 82.7% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sho Shimabukuro (`KXATPMATCH-26OCT20SHISAF-SHI`) | 0.14 / 0.17 (100) | 15.5% | -- | -- | -- [-----] | 17.3% | -- | 17.3% | KALSHI_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; THIN_DISPLAYED_SIZE; WIDE_SPREAD

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
