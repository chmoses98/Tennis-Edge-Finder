# ASSISTED SLATE -- 2026-10-06T15:39Z (`SL-20261006T153914Z-3c6ec82c`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

278 open matches not seen started, 960 markets. Skipped: {"first_ball_already_observed": 1}. Sources: shadow board 2026-10-06T06:49:59.241553+00:00, Model 4 2026-10-06T06:51:52.405380+00:00, Gen-1 ledger 2026-10-06T06:49:55.670839+00:00, external 2026-10-06T15:18:49.748694+00:00, capture 20261006T152617Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-10-07 04:00Z**
* Recommended RUN TENNIS time: **2026-10-07 03:15Z**
* Final price/status check time: **2026-10-07 03:50Z**
* Number of matches in window: 7 (Arthur Gea vs Jaime Faria, Aleksandar Kovacevic vs Matteo Berrettini, Sho Shimabukuro vs Miomir Kecmanovic, Iva Jovic vs Iga Swiatek, Yannick Hanfmann vs Kamil Majchrzak, Zhizhen Zhang vs Tomas Machac ...)

* **18 main-tour match(es) have NO verified start status** (START_UNKNOWN): BET blocked until a live status check.

Slate built 2026-10-06T15:39Z. Refresh due by: 2026-10-07 03:15Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 15, "HIGH_REVIEW": 33, "NORMAL": 412, "REVIEW": 68, "UNPRICED": 432}; match winners: {"EXTREME": 15, "HIGH_REVIEW": 31, "NORMAL": 150, "REVIEW": 24, "UNPRICED": 336}; quote freshness at build: {"FRESH": 528}.

## Nuno Borges vs Facundo Diaz Acosta -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-08T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:132686:207680:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nuno Borges (`KXATPMATCH-26OCT06BORDIA-BOR`) | 0.74 / 0.76 (5740) | 75.0% | 67.0% | 57.4% | 62.2% [59.8%-65.5%] | -- | -- | -- | -- | PASS | -8.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Facundo Diaz Acosta (`KXATPMATCH-26OCT06BORDIA-DIA`) | 0.24 / 0.26 (15432) | 25.0% | 33.0% | 42.6% | 37.8% [34.5%-40.2%] | -- | -- | -- | -- | SHADOW_BET | +8.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6214.0, B 5689.0; serve-point win A 65.8%, B 37.7%; Elo A 1863.7, B 1644.6; model uncertainty 0.0284
* Form inputs: days since last match A 6, B 22; matches on record A 548, B 464; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.018, surface_dev_tight -0.024
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT06BORDIA-23` Over 22.5 games: 0.43/0.44 mid 43.5%, model 58.7% (projection_v2.0 (prediction ledger)) -- gap +15.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06BORDIA-BOR4` Will Nuno Borges win at least 3.5 more games than Facundo Diaz Acosta?: 0.55/0.56 mid 55.5%, model 40.6% (projection_v2.0 (prediction ledger)) -- gap -14.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06BORDIA-BOR20` Will Nuno Borges win the Nuno Borges vs Facundo Diaz Acosta match by a set score of 2-0?: 0.51/0.54 mid 52.5%, model 37.9% (projection_v2.0 (prediction ledger)) -- gap -14.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06BORDIA-28` Over 27.5 games: 0.21/0.33 mid 27.0%, model 38.7% (projection_v2.0 (prediction ledger)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06BORDIA-BOR7` Will Nuno Borges win at least 6.5 more games than Facundo Diaz Acosta?: 0.16/0.20 mid 18.0%, model 7.7% (projection_v2.0 (prediction ledger)) -- gap -10.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06BORDIA-18` Over 17.5 games: 0.68/0.98 mid 83.0%, model 92.6% (projection_v2.0 (prediction ledger)) -- gap +9.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT06BORDIA-2-DIA` Will Facundo Diaz Acosta win set 2 in the Nuno Borges vs Facundo Diaz Acosta match: 0.28/0.31 mid 29.5%, model 38.5% (projection_v2.0 (prediction ledger)) -- gap +9.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06BORDIA-2-BOR` Will Nuno Borges win set 2 in the Nuno Borges vs Facundo Diaz Acosta match: 0.69/0.71 mid 70.0%, model 61.5% (projection_v2.0 (prediction ledger)) -- gap -8.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06BORDIA-1-DIA` Will Facundo Diaz Acosta win set 1 in the Nuno Borges vs Facundo Diaz Acosta match: 0.30/0.31 mid 30.5%, model 38.5% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06BORDIA-1-BOR` Will Nuno Borges win set 1 in the Nuno Borges vs Facundo Diaz Acosta match: 0.68/0.69 mid 68.5%, model 61.5% (projection_v2.0 (prediction ledger)) -- gap -7.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06BORDIA-DIA21` Will Facundo Diaz Acosta win the Nuno Borges vs Facundo Diaz Acosta match by a set score of 2-1?: 0.10/0.13 mid 11.5%, model 18.2% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06BORDIA-BOR21` Will Nuno Borges win the Nuno Borges vs Facundo Diaz Acosta match by a set score of 2-1?: 0.21/0.24 mid 22.5%, model 29.1% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06BORDIA-DIA2` Will Facundo Diaz Acosta win at least 1.5 more games than Nuno Borges?: 0.19/0.23 mid 21.0%, model 26.4% (projection_v2.0 (prediction ledger)) -- gap +5.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06BORDIA-DIA20` Will Facundo Diaz Acosta win the Nuno Borges vs Facundo Diaz Acosta match by a set score of 2-0?: 0.12/0.14 mid 13.0%, model 14.8% (projection_v2.0 (prediction ledger)) -- gap +1.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Marcos Giron vs Sebastian Baez -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-08T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:106218:202104:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sebastian Baez (`KXATPMATCH-26OCT06GIRBAE-BAE`) | 0.53 / 0.55 (3430) | 54.0% | 48.1% | 40.4% | 40.0% [38.0%-44.4%] | -- | -- | -- | -- | PASS | -5.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marcos Giron (`KXATPMATCH-26OCT06GIRBAE-GIR`) | 0.45 / 0.46 (724) | 45.5% | 51.9% | 59.6% | 60.1% [55.6%-62.0%] | -- | -- | -- | -- | PASS | +6.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5186.0, B 5194.0; serve-point win A 62.1%, B 38.3%; Elo A 1802.0, B 1722.8; model uncertainty 0.0322
* Form inputs: days since last match A 8, B 5; matches on record A 720, B 502; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.025, surface_pool_high +0.019, surface_dev_loose +0.010, surface_dev_tight -0.015
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT06GIRBAE-19` Over 18.5 games: 0.67/0.83 mid 75.0%, model 86.3% (projection_v2.0 (prediction ledger)) -- gap +11.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06GIRBAE-24` Over 23.5 games: 0.44/0.45 mid 44.5%, model 53.9% (projection_v2.0 (prediction ledger)) -- gap +9.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06GIRBAE-BAE20` Will Sebastian Baez win the Marcos Giron vs Sebastian Baez match by a set score of 2-0?: 0.31/0.35 mid 33.0%, model 23.8% (projection_v2.0 (prediction ledger)) -- gap -9.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06GIRBAE-BAE5` Will Sebastian Baez win at least 4.5 more games than Marcos Giron?: 0.24/0.28 mid 26.0%, model 17.1% (projection_v2.0 (prediction ledger)) -- gap -8.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06GIRBAE-BAE2` Will Sebastian Baez win at least 1.5 more games than Marcos Giron?: 0.48/0.51 mid 49.5%, model 40.9% (projection_v2.0 (prediction ledger)) -- gap -8.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06GIRBAE-29` Over 28.5 games: 0.21/0.33 mid 27.0%, model 34.1% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06GIRBAE-GIR21` Will Marcos Giron win the Marcos Giron vs Sebastian Baez match by a set score of 2-1?: 0.18/0.21 mid 19.5%, model 25.6% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT06GIRBAE-1-BAE` Will Sebastian Baez win set 1 in the Marcos Giron vs Sebastian Baez match: 0.52/0.55 mid 53.5%, model 48.8% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06GIRBAE-1-GIR` Will Marcos Giron win set 1 in the Marcos Giron vs Sebastian Baez match: 0.45/0.48 mid 46.5%, model 51.2% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06GIRBAE-2-BAE` Will Sebastian Baez win set 2 in the Marcos Giron vs Sebastian Baez match: 0.52/0.55 mid 53.5%, model 48.8% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06GIRBAE-2-GIR` Will Marcos Giron win set 2 in the Marcos Giron vs Sebastian Baez match: 0.45/0.48 mid 46.5%, model 51.2% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT06GIRBAE-GIR2` Will Marcos Giron win at least 1.5 more games than Sebastian Baez?: 0.38/0.43 mid 40.5%, model 44.7% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06GIRBAE-BAE21` Will Sebastian Baez win the Marcos Giron vs Sebastian Baez match by a set score of 2-1?: 0.19/0.22 mid 20.5%, model 24.4% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06GIRBAE-GIR20` Will Marcos Giron win the Marcos Giron vs Sebastian Baez match by a set score of 2-0?: 0.25/0.28 mid 26.5%, model 26.3% (projection_v2.0 (prediction ledger)) -- gap -0.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hubert Hurkacz vs James Duckworth -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-08T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105902:128034:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| James Duckworth (`KXATPMATCH-26OCT06HURDUC-DUC`) | 0.28 / 0.30 (8222) | 29.0% | 17.0% | 33.4% | 30.5% [28.4%-31.6%] | -- | -- | -- | -- | PASS | -12.0 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hubert Hurkacz (`KXATPMATCH-26OCT06HURDUC-HUR`) | 0.70 / 0.71 (36) | 70.5% | 83.0% | 66.6% | 69.5% [68.4%-71.6%] | -- | -- | -- | -- | PASS | +12.5 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4906.0, B 6399.0; serve-point win A 72.3%, B 35.7%; Elo A 1976.7, B 1754.3; model uncertainty 0.016
* Form inputs: days since last match A 2, B 12; matches on record A 684, B 935; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT06HURDUC-DUC2` Will James Duckworth win at least 1.5 more games than Hubert Hurkacz?: 0.22/0.25 mid 23.5%, model 12.0% (projection_v2.0 (prediction ledger)) -- gap -11.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06HURDUC-HUR20` Will Hubert Hurkacz win the Hubert Hurkacz vs James Duckworth match by a set score of 2-0?: 0.46/0.47 mid 46.5%, model 54.5% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06HURDUC-DUC20` Will James Duckworth win the Hubert Hurkacz vs James Duckworth match by a set score of 2-0?: 0.13/0.16 mid 14.5%, model 6.9% (projection_v2.0 (prediction ledger)) -- gap -7.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT06HURDUC-1-HUR` Will Hubert Hurkacz win set 1 in the Hubert Hurkacz vs James Duckworth match: 0.66/0.67 mid 66.5%, model 73.8% (projection_v2.0 (prediction ledger)) -- gap +7.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06HURDUC-2-DUC` Will James Duckworth win set 2 in the Hubert Hurkacz vs James Duckworth match: 0.32/0.35 mid 33.5%, model 26.2% (projection_v2.0 (prediction ledger)) -- gap -7.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06HURDUC-2-HUR` Will Hubert Hurkacz win set 2 in the Hubert Hurkacz vs James Duckworth match: 0.65/0.68 mid 66.5%, model 73.8% (projection_v2.0 (prediction ledger)) -- gap +7.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT06HURDUC-HUR4` Will Hubert Hurkacz win at least 3.5 more games than James Duckworth?: 0.44/0.45 mid 44.5%, model 51.6% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT06HURDUC-1-DUC` Will James Duckworth win set 1 in the Hubert Hurkacz vs James Duckworth match: 0.31/0.35 mid 33.0%, model 26.2% (projection_v2.0 (prediction ledger)) -- gap -6.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT06HURDUC-18` Over 17.5 games: 0.76/0.99 mid 87.5%, model 93.1% (projection_v2.0 (prediction ledger)) -- gap +5.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06HURDUC-HUR21` Will Hubert Hurkacz win the Hubert Hurkacz vs James Duckworth match by a set score of 2-1?: 0.22/0.25 mid 23.5%, model 28.5% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06HURDUC-DUC21` Will James Duckworth win the Hubert Hurkacz vs James Duckworth match by a set score of 2-1?: 0.13/0.15 mid 14.0%, model 10.1% (projection_v2.0 (prediction ledger)) -- gap -3.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06HURDUC-HUR7` Will Hubert Hurkacz win at least 6.5 more games than James Duckworth?: 0.10/0.12 mid 11.0%, model 8.2% (projection_v2.0 (prediction ledger)) -- gap -2.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06HURDUC-23` Over 22.5 games: 0.54/0.55 mid 54.5%, model 54.7% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06HURDUC-28` Over 27.5 games: 0.32/0.37 mid 34.5%, model 34.4% (projection_v2.0 (prediction ledger)) -- gap -0.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Vit Kopriva vs Zizou Bergs -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-08T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200240:200267:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zizou Bergs (`KXATPMATCH-26OCT06KOPBER-BER`) | 0.70 / 0.72 (22059) | 71.0% | 62.6% | 71.3% | 70.9% [68.6%-72.2%] | -- | -- | -- | -- | PASS | -8.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Vit Kopriva (`KXATPMATCH-26OCT06KOPBER-KOP`) | 0.28 / 0.30 (330) | 29.0% | 37.4% | 28.7% | 29.1% [27.8%-31.4%] | -- | -- | -- | -- | PASS | +8.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5796.0, B 5776.0; serve-point win A 60.0%, B 37.5%; Elo A 1685.7, B 1822.4; model uncertainty 0.0178
* Form inputs: days since last match A 8, B 5; matches on record A 722, B 564; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.004, surface_dev_loose -0.013, surface_dev_tight +0.013
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT06KOPBER-BER4` Will Zizou Bergs win at least 3.5 more games than Vit Kopriva?: 0.51/0.54 mid 52.5%, model 39.1% (projection_v2.0 (prediction ledger)) -- gap -13.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06KOPBER-BER20` Will Zizou Bergs win the Vit Kopriva vs Zizou Bergs match by a set score of 2-0?: 0.46/0.49 mid 47.5%, model 34.2% (projection_v2.0 (prediction ledger)) -- gap -13.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06KOPBER-23` Over 22.5 games: 0.45/0.47 mid 46.0%, model 57.6% (projection_v2.0 (prediction ledger)) -- gap +11.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06KOPBER-BER7` Will Zizou Bergs win at least 6.5 more games than Vit Kopriva?: 0.16/0.21 mid 18.5%, model 8.8% (projection_v2.0 (prediction ledger)) -- gap -9.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06KOPBER-28` Over 27.5 games: 0.22/0.33 mid 27.5%, model 37.2% (projection_v2.0 (prediction ledger)) -- gap +9.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT06KOPBER-1-KOP` Will Vit Kopriva win set 1 in the Vit Kopriva vs Zizou Bergs match: 0.32/0.35 mid 33.5%, model 41.5% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06KOPBER-2-BER` Will Zizou Bergs win set 2 in the Vit Kopriva vs Zizou Bergs match: 0.65/0.68 mid 66.5%, model 58.5% (projection_v2.0 (prediction ledger)) -- gap -8.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06KOPBER-2-KOP` Will Vit Kopriva win set 2 in the Vit Kopriva vs Zizou Bergs match: 0.32/0.35 mid 33.5%, model 41.5% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06KOPBER-1-BER` Will Zizou Bergs win set 1 in the Vit Kopriva vs Zizou Bergs match: 0.65/0.67 mid 66.0%, model 58.5% (projection_v2.0 (prediction ledger)) -- gap -7.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06KOPBER-KOP21` Will Vit Kopriva win the Vit Kopriva vs Zizou Bergs match by a set score of 2-1?: 0.12/0.15 mid 13.5%, model 20.2% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06KOPBER-BER21` Will Zizou Bergs win the Vit Kopriva vs Zizou Bergs match by a set score of 2-1?: 0.21/0.24 mid 22.5%, model 28.4% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06KOPBER-KOP2` Will Vit Kopriva win at least 1.5 more games than Zizou Bergs?: 0.23/0.27 mid 25.0%, model 30.8% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06KOPBER-KOP20` Will Vit Kopriva win the Vit Kopriva vs Zizou Bergs match by a set score of 2-0?: 0.14/0.16 mid 15.0%, model 17.2% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06KOPBER-18` Over 17.5 games: 0.81/0.98 mid 89.5%, model 90.8% (projection_v2.0 (prediction ledger)) -- gap +1.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Martin Landaluce vs Jan-Lennard Struff -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-08T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105526:212021:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martin Landaluce (`KXATPMATCH-26OCT06LANSTR-LAN`) | 0.50 / 0.51 (2) | 50.5% | 58.7% | 57.9% | 56.4% [47.5%-59.4%] | -- | -- | -- | -- | WATCH | +8.2 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jan-Lennard Struff (`KXATPMATCH-26OCT06LANSTR-STR`) | 0.48 / 0.50 (33073) | 49.0% | 41.3% | 42.1% | 43.6% [40.6%-52.5%] | -- | -- | -- | -- | PASS | -7.7 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5793.0, B 5483.0; serve-point win A 65.1%, B 36.7%; Elo A 1809.8, B 1795.9; model uncertainty 0.0592
* Form inputs: days since last match A 134, B 3; matches on record A 219, B 1066; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.029, surface_dev_loose +0.019, surface_dev_tight -0.020
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT06LANSTR-STR2` Will Jan-Lennard Struff win at least 1.5 more games than Martin Landaluce?: 0.41/0.45 mid 43.0%, model 34.0% (projection_v2.0 (prediction ledger)) -- gap -9.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26OCT06LANSTR-STR20` Will Jan-Lennard Struff win the Martin Landaluce vs Jan-Lennard Struff match by a set score of 2-0?: 0.27/0.30 mid 28.5%, model 19.5% (projection_v2.0 (prediction ledger)) -- gap -9.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26OCT06LANSTR-LAN21` Will Martin Landaluce win the Martin Landaluce vs Jan-Lennard Struff match by a set score of 2-1?: 0.19/0.22 mid 20.5%, model 27.5% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPGTOTAL-26OCT06LANSTR-25` Over 24.5 games: 0.46/0.49 mid 47.5%, model 53.3% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPGSPREAD-26OCT06LANSTR-LAN2` Will Martin Landaluce win at least 1.5 more games than Jan-Lennard Struff?: 0.44/0.47 mid 45.5%, model 51.1% (projection_v2.0 (prediction ledger)) -- gap +5.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPSETWINNER-26OCT06LANSTR-1-LAN` Will Martin Landaluce win set 1 in the Martin Landaluce vs Jan-Lennard Struff match: 0.49/0.52 mid 50.5%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT06LANSTR-1-STR` Will Jan-Lennard Struff win set 1 in the Martin Landaluce vs Jan-Lennard Struff match: 0.48/0.50 mid 49.0%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT06LANSTR-2-LAN` Will Martin Landaluce win set 2 in the Martin Landaluce vs Jan-Lennard Struff match: 0.50/0.52 mid 51.0%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT06LANSTR-2-STR` Will Jan-Lennard Struff win set 2 in the Martin Landaluce vs Jan-Lennard Struff match: 0.48/0.50 mid 49.0%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPGTOTAL-26OCT06LANSTR-30` Over 29.5 games: 0.23/0.45 mid 34.0%, model 31.4% (projection_v2.0 (prediction ledger)) -- gap -2.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26OCT06LANSTR-STR21` Will Jan-Lennard Struff win the Martin Landaluce vs Jan-Lennard Struff match by a set score of 2-1?: 0.18/0.21 mid 19.5%, model 21.8% (projection_v2.0 (prediction ledger)) -- gap +2.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPGTOTAL-26OCT06LANSTR-20` Over 19.5 games: 0.72/0.94 mid 83.0%, model 81.4% (projection_v2.0 (prediction ledger)) -- gap -1.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26OCT06LANSTR-LAN20` Will Martin Landaluce win the Martin Landaluce vs Jan-Lennard Struff match by a set score of 2-0?: 0.29/0.31 mid 30.0%, model 31.2% (projection_v2.0 (prediction ledger)) -- gap +1.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPGSPREAD-26OCT06LANSTR-LAN5` Will Martin Landaluce win at least 4.5 more games than Jan-Lennard Struff?: 0.20/0.23 mid 21.5%, model 20.8% (projection_v2.0 (prediction ledger)) -- gap -0.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Fabian Marozsan vs Zachary Svajda -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-08T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:206681:208260:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fabian Marozsan (`KXATPMATCH-26OCT06MARSVA-MAR`) | 0.53 / 0.54 (13250) | 53.5% | 52.8% | 49.5% | 49.0% [47.0%-52.5%] | -- | -- | -- | -- | PASS | -0.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zachary Svajda (`KXATPMATCH-26OCT06MARSVA-SVA`) | 0.46 / 0.48 (10692) | 47.0% | 47.2% | 50.5% | 51.0% [47.5%-53.0%] | -- | -- | -- | -- | PASS | +0.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4957.0, B 5117.0; serve-point win A 65.0%, B 35.6%; Elo A 1795.5, B 1817.0; model uncertainty 0.0272
* Form inputs: days since last match A 9, B 8; matches on record A 451, B 358; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose -0.005, surface_dev_tight -0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT06MARSVA-29` Over 28.5 games: 0.23/0.27 mid 25.0%, model 37.5% (projection_v2.0 (prediction ledger)) -- gap +12.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06MARSVA-24` Over 23.5 games: 0.45/0.46 mid 45.5%, model 55.5% (projection_v2.0 (prediction ledger)) -- gap +9.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06MARSVA-19` Over 18.5 games: 0.79/0.87 mid 83.0%, model 89.7% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06MARSVA-MAR5` Will Fabian Marozsan win at least 4.5 more games than Zachary Svajda?: 0.21/0.24 mid 22.5%, model 16.8% (projection_v2.0 (prediction ledger)) -- gap -5.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06MARSVA-MAR21` Will Fabian Marozsan win the Fabian Marozsan vs Zachary Svajda match by a set score of 2-1?: 0.19/0.22 mid 20.5%, model 25.9% (projection_v2.0 (prediction ledger)) -- gap +5.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06MARSVA-SVA21` Will Zachary Svajda win the Fabian Marozsan vs Zachary Svajda match by a set score of 2-1?: 0.18/0.21 mid 19.5%, model 24.0% (projection_v2.0 (prediction ledger)) -- gap +4.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06MARSVA-MAR20` Will Fabian Marozsan win the Fabian Marozsan vs Zachary Svajda match by a set score of 2-0?: 0.30/0.32 mid 31.0%, model 26.9% (projection_v2.0 (prediction ledger)) -- gap -4.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06MARSVA-SVA20` Will Zachary Svajda win the Fabian Marozsan vs Zachary Svajda match by a set score of 2-0?: 0.26/0.28 mid 27.0%, model 23.2% (projection_v2.0 (prediction ledger)) -- gap -3.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06MARSVA-SVA2` Will Zachary Svajda win at least 1.5 more games than Fabian Marozsan?: 0.40/0.44 mid 42.0%, model 39.6% (projection_v2.0 (prediction ledger)) -- gap -2.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06MARSVA-MAR2` Will Fabian Marozsan win at least 1.5 more games than Zachary Svajda?: 0.45/0.47 mid 46.0%, model 45.1% (projection_v2.0 (prediction ledger)) -- gap -0.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT06MARSVA-1-MAR` Will Fabian Marozsan win set 1 in the Fabian Marozsan vs Zachary Svajda match: 0.51/0.52 mid 51.5%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap +0.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06MARSVA-2-MAR` Will Fabian Marozsan win set 2 in the Fabian Marozsan vs Zachary Svajda match: 0.50/0.53 mid 51.5%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap +0.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06MARSVA-1-SVA` Will Zachary Svajda win set 1 in the Fabian Marozsan vs Zachary Svajda match: 0.47/0.49 mid 48.0%, model 48.1% (projection_v2.0 (prediction ledger)) -- gap +0.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06MARSVA-2-SVA` Will Zachary Svajda win set 2 in the Fabian Marozsan vs Zachary Svajda match: 0.47/0.49 mid 48.0%, model 48.1% (projection_v2.0 (prediction ledger)) -- gap +0.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jaume Munar vs Jenson Brooksby -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-08T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144719:202385:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jenson Brooksby (`KXATPMATCH-26OCT06MUNBRO-BRO`) | 0.37 / 0.38 (3201) | 37.5% | 44.9% | 34.7% | 40.5% [37.1%-44.5%] | -- | -- | -- | -- | PASS | +7.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jaume Munar (`KXATPMATCH-26OCT06MUNBRO-MUN`) | 0.61 / 0.63 (23677) | 62.0% | 55.1% | 65.3% | 59.5% [55.5%-62.9%] | -- | -- | -- | -- | PASS | -6.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4675.0, B 3401.0; serve-point win A 62.8%, B 38.2%; Elo A 1798.4, B 1830.9; model uncertainty 0.0369
* Form inputs: days since last match A 1, B 9; matches on record A 744, B 287; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.034, surface_pool_high -0.040, surface_dev_loose -0.000, surface_dev_tight -0.009
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT06MUNBRO-23` Over 22.5 games: 0.46/0.47 mid 46.5%, model 59.8% (projection_v2.0 (prediction ledger)) -- gap +13.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06MUNBRO-28` Over 27.5 games: 0.25/0.30 mid 27.5%, model 39.2% (projection_v2.0 (prediction ledger)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06MUNBRO-MUN3` Will Jaume Munar win at least 2.5 more games than Jenson Brooksby?: 0.51/0.54 mid 52.5%, model 41.0% (projection_v2.0 (prediction ledger)) -- gap -11.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06MUNBRO-MUN20` Will Jaume Munar win the Jaume Munar vs Jenson Brooksby match by a set score of 2-0?: 0.39/0.41 mid 40.0%, model 28.5% (projection_v2.0 (prediction ledger)) -- gap -11.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06MUNBRO-MUN6` Will Jaume Munar win at least 5.5 more games than Jenson Brooksby?: 0.21/0.25 mid 23.0%, model 11.9% (projection_v2.0 (prediction ledger)) -- gap -11.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06MUNBRO-BRO21` Will Jenson Brooksby win the Jaume Munar vs Jenson Brooksby match by a set score of 2-1?: 0.15/0.18 mid 16.5%, model 23.2% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT06MUNBRO-1-BRO` Will Jenson Brooksby win set 1 in the Jaume Munar vs Jenson Brooksby match: 0.39/0.42 mid 40.5%, model 46.6% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06MUNBRO-1-MUN` Will Jaume Munar win set 1 in the Jaume Munar vs Jenson Brooksby match: 0.58/0.61 mid 59.5%, model 53.4% (projection_v2.0 (prediction ledger)) -- gap -6.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06MUNBRO-2-BRO` Will Jenson Brooksby win set 2 in the Jaume Munar vs Jenson Brooksby match: 0.39/0.42 mid 40.5%, model 46.6% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06MUNBRO-2-MUN` Will Jaume Munar win set 2 in the Jaume Munar vs Jenson Brooksby match: 0.58/0.61 mid 59.5%, model 53.4% (projection_v2.0 (prediction ledger)) -- gap -6.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT06MUNBRO-BRO2` Will Jenson Brooksby win at least 1.5 more games than Jaume Munar?: 0.31/0.34 mid 32.5%, model 37.8% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06MUNBRO-MUN21` Will Jaume Munar win the Jaume Munar vs Jenson Brooksby match by a set score of 2-1?: 0.21/0.24 mid 22.5%, model 26.6% (projection_v2.0 (prediction ledger)) -- gap +4.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06MUNBRO-18` Over 17.5 games: 0.85/0.93 mid 89.0%, model 92.3% (projection_v2.0 (prediction ledger)) -- gap +3.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06MUNBRO-BRO20` Will Jenson Brooksby win the Jaume Munar vs Jenson Brooksby match by a set score of 2-0?: 0.19/0.22 mid 20.5%, model 21.7% (projection_v2.0 (prediction ledger)) -- gap +1.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mariano Navone vs Pablo Carreno Busta -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-08T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105807:208363:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pablo Carreno Busta (`KXATPMATCH-26OCT06NAVCAR-CAR`) | 0.49 / 0.50 (36994) | 49.5% | 47.9% | 48.4% | 52.6% [51.0%-55.7%] | -- | -- | -- | -- | WATCH | -1.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mariano Navone (`KXATPMATCH-26OCT06NAVCAR-NAV`) | 0.51 / 0.52 (105) | 51.5% | 52.1% | 51.5% | 47.4% [44.3%-49.0%] | -- | -- | -- | -- | PASS | +0.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5962.0, B 4960.0; serve-point win A 59.6%, B 40.8%; Elo A 1725.9, B 1834.8; model uncertainty 0.0232
* Form inputs: days since last match A 5, B 4; matches on record A 430, B 989; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT06NAVCAR-24` Over 23.5 games: 0.43/0.45 mid 44.0%, model 52.8% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06NAVCAR-29` Over 28.5 games: 0.21/0.26 mid 23.5%, model 31.5% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06NAVCAR-19` Over 18.5 games: 0.75/0.81 mid 78.0%, model 83.8% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06NAVCAR-NAV21` Will Mariano Navone win the Mariano Navone vs Pablo Carreno Busta match by a set score of 2-1?: 0.19/0.22 mid 20.5%, model 25.7% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06NAVCAR-CAR20` Will Pablo Carreno Busta win the Mariano Navone vs Pablo Carreno Busta match by a set score of 2-0?: 0.27/0.30 mid 28.5%, model 23.6% (projection_v2.0 (prediction ledger)) -- gap -4.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06NAVCAR-CAR21` Will Pablo Carreno Busta win the Mariano Navone vs Pablo Carreno Busta match by a set score of 2-1?: 0.18/0.21 mid 19.5%, model 24.3% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06NAVCAR-NAV20` Will Mariano Navone win the Mariano Navone vs Pablo Carreno Busta match by a set score of 2-0?: 0.29/0.32 mid 30.5%, model 26.5% (projection_v2.0 (prediction ledger)) -- gap -4.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06NAVCAR-CAR5` Will Pablo Carreno Busta win at least 4.5 more games than Mariano Navone?: 0.18/0.25 mid 21.5%, model 18.8% (projection_v2.0 (prediction ledger)) -- gap -2.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06NAVCAR-NAV2` Will Mariano Navone win at least 1.5 more games than Pablo Carreno Busta?: 0.46/0.49 mid 47.5%, model 45.3% (projection_v2.0 (prediction ledger)) -- gap -2.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06NAVCAR-CAR2` Will Pablo Carreno Busta win at least 1.5 more games than Mariano Navone?: 0.41/0.45 mid 43.0%, model 41.0% (projection_v2.0 (prediction ledger)) -- gap -2.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT06NAVCAR-1-CAR` Will Pablo Carreno Busta win set 1 in the Mariano Navone vs Pablo Carreno Busta match: 0.48/0.51 mid 49.5%, model 48.6% (projection_v2.0 (prediction ledger)) -- gap -0.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06NAVCAR-2-CAR` Will Pablo Carreno Busta win set 2 in the Mariano Navone vs Pablo Carreno Busta match: 0.48/0.51 mid 49.5%, model 48.6% (projection_v2.0 (prediction ledger)) -- gap -0.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06NAVCAR-2-NAV` Will Mariano Navone win set 2 in the Mariano Navone vs Pablo Carreno Busta match: 0.49/0.52 mid 50.5%, model 51.4% (projection_v2.0 (prediction ledger)) -- gap +0.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06NAVCAR-1-NAV` Will Mariano Navone win set 1 in the Mariano Navone vs Pablo Carreno Busta match: 0.50/0.52 mid 51.0%, model 51.4% (projection_v2.0 (prediction ledger)) -- gap +0.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Cameron Norrie vs Denis Shapovalov -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 08:41Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-07T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111815:133430:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cameron Norrie (`KXATPMATCH-26OCT06NORSHA-NOR`) | 0.46 / 0.48 (13345) | 47.0% | 41.3% | 43.5% | 44.0% [43.5%-46.0%] | -- | -- | -- | -- | PASS | -5.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Denis Shapovalov (`KXATPMATCH-26OCT06NORSHA-SHA`) | 0.52 / 0.54 (5518) | 53.0% | 58.7% | 56.5% | 56.0% [54.0%-56.5%] | -- | -- | -- | -- | SHADOW_BET | +5.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5827.0, B 4524.0; serve-point win A 62.0%, B 36.3%; Elo A 1904.7, B 1930.7; model uncertainty 0.0124
* Form inputs: days since last match A 5, B 3; matches on record A 675, B 579; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight +0.015
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT06NORSHA-29` Over 28.5 games: 0.31/0.66 mid 48.5%, model 34.6% (projection_v2.0 (prediction ledger)) -- gap -13.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06NORSHA-SHA20` Will Denis Shapovalov win the Cameron Norrie vs Denis Shapovalov match by a set score of 2-0?: 0.02/0.34 mid 18.0%, model 31.1% (projection_v2.0 (prediction ledger)) -- gap +13.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06NORSHA-19` Over 18.5 games: 0.54/0.97 mid 75.5%, model 87.0% (projection_v2.0 (prediction ledger)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06NORSHA-NOR21` Will Cameron Norrie win the Cameron Norrie vs Denis Shapovalov match by a set score of 2-1?: 0.04/0.21 mid 12.5%, model 21.8% (projection_v2.0 (prediction ledger)) -- gap +9.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06NORSHA-NOR20` Will Cameron Norrie win the Cameron Norrie vs Denis Shapovalov match by a set score of 2-0?: 0.25/0.28 mid 26.5%, model 19.5% (projection_v2.0 (prediction ledger)) -- gap -7.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06NORSHA-NOR2` Will Cameron Norrie win at least 1.5 more games than Denis Shapovalov?: 0.38/0.43 mid 40.5%, model 34.3% (projection_v2.0 (prediction ledger)) -- gap -6.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06NORSHA-24` Over 23.5 games: 0.45/0.74 mid 59.5%, model 53.7% (projection_v2.0 (prediction ledger)) -- gap -5.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06NORSHA-SHA2` Will Denis Shapovalov win at least 1.5 more games than Cameron Norrie?: 0.46/0.48 mid 47.0%, model 51.4% (projection_v2.0 (prediction ledger)) -- gap +4.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT06NORSHA-1-SHA` Will Denis Shapovalov win set 1 in the Cameron Norrie vs Denis Shapovalov match: 0.50/0.53 mid 51.5%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT06NORSHA-SHA5` Will Denis Shapovalov win at least 4.5 more games than Cameron Norrie?: 0.03/0.48 mid 25.5%, model 22.5% (projection_v2.0 (prediction ledger)) -- gap -3.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT06NORSHA-1-NOR` Will Cameron Norrie win set 1 in the Cameron Norrie vs Denis Shapovalov match: 0.45/0.49 mid 47.0%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap -2.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06NORSHA-2-SHA` Will Denis Shapovalov win set 2 in the Cameron Norrie vs Denis Shapovalov match: 0.42/0.64 mid 53.0%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap +2.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06NORSHA-SHA21` Will Denis Shapovalov win the Cameron Norrie vs Denis Shapovalov match by a set score of 2-1?: 0.16/0.41 mid 28.5%, model 27.5% (projection_v2.0 (prediction ledger)) -- gap -1.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT06NORSHA-2-NOR` Will Cameron Norrie win set 2 in the Cameron Norrie vs Denis Shapovalov match: 0.31/0.56 mid 43.5%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap +0.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Thiago Agustin Tirante vs Hamad Medjedovic -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-08T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:202058:209098:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hamad Medjedovic (`KXATPMATCH-26OCT06TIRMED-MED`) | 0.42 / 0.43 (4463) | 42.5% | 47.0% | 36.3% | 40.0% [38.2%-43.2%] | -- | -- | -- | -- | PASS | +4.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Thiago Agustin Tirante (`KXATPMATCH-26OCT06TIRMED-TIR`) | 0.58 / 0.59 (24748) | 58.5% | 53.0% | 63.7% | 60.0% [56.8%-61.8%] | -- | -- | -- | -- | PASS | -5.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5826.0, B 4333.0; serve-point win A 67.3%, B 33.4%; Elo A 1751.9, B 1761.0; model uncertainty 0.0253
* Form inputs: days since last match A 6, B 17; matches on record A 486, B 309; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.000, surface_dev_loose +0.018, surface_dev_tight -0.023
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT06TIRMED-24` Over 23.5 games: 0.45/0.46 mid 45.5%, model 57.1% (projection_v2.0 (prediction ledger)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06TIRMED-29` Over 28.5 games: 0.30/0.31 mid 30.5%, model 40.4% (projection_v2.0 (prediction ledger)) -- gap +9.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06TIRMED-TIR5` Will Thiago Agustin Tirante win at least 4.5 more games than Hamad Medjedovic?: 0.22/0.25 mid 23.5%, model 14.1% (projection_v2.0 (prediction ledger)) -- gap -9.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06TIRMED-TIR20` Will Thiago Agustin Tirante win the Thiago Agustin Tirante vs Hamad Medjedovic match by a set score of 2-0?: 0.34/0.37 mid 35.5%, model 27.0% (projection_v2.0 (prediction ledger)) -- gap -8.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06TIRMED-19` Over 18.5 games: 0.84/0.85 mid 84.5%, model 92.4% (projection_v2.0 (prediction ledger)) -- gap +7.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06TIRMED-TIR2` Will Thiago Agustin Tirante win at least 1.5 more games than Hamad Medjedovic?: 0.49/0.52 mid 50.5%, model 44.6% (projection_v2.0 (prediction ledger)) -- gap -5.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06TIRMED-MED21` Will Hamad Medjedovic win the Thiago Agustin Tirante vs Hamad Medjedovic match by a set score of 2-1?: 0.17/0.20 mid 18.5%, model 24.0% (projection_v2.0 (prediction ledger)) -- gap +5.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT06TIRMED-2-MED` Will Hamad Medjedovic win set 2 in the Thiago Agustin Tirante vs Hamad Medjedovic match: 0.43/0.45 mid 44.0%, model 48.0% (projection_v2.0 (prediction ledger)) -- gap +4.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06TIRMED-2-TIR` Will Thiago Agustin Tirante win set 2 in the Thiago Agustin Tirante vs Hamad Medjedovic match: 0.55/0.57 mid 56.0%, model 52.0% (projection_v2.0 (prediction ledger)) -- gap -4.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06TIRMED-1-TIR` Will Thiago Agustin Tirante win set 1 in the Thiago Agustin Tirante vs Hamad Medjedovic match: 0.54/0.57 mid 55.5%, model 52.0% (projection_v2.0 (prediction ledger)) -- gap -3.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06TIRMED-TIR21` Will Thiago Agustin Tirante win the Thiago Agustin Tirante vs Hamad Medjedovic match by a set score of 2-1?: 0.21/0.24 mid 22.5%, model 25.9% (projection_v2.0 (prediction ledger)) -- gap +3.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT06TIRMED-1-MED` Will Hamad Medjedovic win set 1 in the Thiago Agustin Tirante vs Hamad Medjedovic match: 0.44/0.46 mid 45.0%, model 48.0% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT06TIRMED-MED2` Will Hamad Medjedovic win at least 1.5 more games than Thiago Agustin Tirante?: 0.35/0.39 mid 37.0%, model 38.9% (projection_v2.0 (prediction ledger)) -- gap +1.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06TIRMED-MED20` Will Hamad Medjedovic win the Thiago Agustin Tirante vs Hamad Medjedovic match by a set score of 2-0?: 0.22/0.25 mid 23.5%, model 23.1% (projection_v2.0 (prediction ledger)) -- gap -0.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Adolfo Daniel Vallejo vs Valentin Royer -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-08T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208316:209226:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentin Royer (`KXATPMATCH-26OCT06VALROY-ROY`) | 0.44 / 0.46 (15939) | 45.0% | 50.6% | 56.1% | 56.1% [53.6%-58.6%] | -- | -- | -- | -- | PASS | +5.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Adolfo Daniel Vallejo (`KXATPMATCH-26OCT06VALROY-VAL`) | 0.54 / 0.55 (415) | 54.5% | 49.4% | 43.9% | 43.9% [41.4%-46.4%] | -- | -- | -- | -- | PASS | -5.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5604.0, B 6396.0; serve-point win A 61.6%, B 38.3%; Elo A 1705.7, B 1742.0; model uncertainty 0.025
* Form inputs: days since last match A 2, B 8; matches on record A 226, B 453; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.025, surface_dev_tight +0.025
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT06VALROY-VAL20` Will Adolfo Daniel Vallejo win the Adolfo Daniel Vallejo vs Valentin Royer match by a set score of 2-0?: 0.32/0.35 mid 33.5%, model 24.6% (projection_v2.0 (prediction ledger)) -- gap -8.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06VALROY-25` Over 24.5 games: 0.42/0.45 mid 43.5%, model 52.2% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06VALROY-VAL5` Will Adolfo Daniel Vallejo win at least 4.5 more games than Valentin Royer?: 0.25/0.28 mid 26.5%, model 18.0% (projection_v2.0 (prediction ledger)) -- gap -8.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06VALROY-VAL2` Will Adolfo Daniel Vallejo win at least 1.5 more games than Valentin Royer?: 0.48/0.52 mid 50.0%, model 42.2% (projection_v2.0 (prediction ledger)) -- gap -7.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06VALROY-20` Over 19.5 games: 0.67/0.76 mid 71.5%, model 78.9% (projection_v2.0 (prediction ledger)) -- gap +7.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06VALROY-ROY21` Will Valentin Royer win the Adolfo Daniel Vallejo vs Valentin Royer match by a set score of 2-1?: 0.17/0.20 mid 18.5%, model 25.2% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT06VALROY-1-ROY` Will Valentin Royer win set 1 in the Adolfo Daniel Vallejo vs Valentin Royer match: 0.44/0.46 mid 45.0%, model 50.4% (projection_v2.0 (prediction ledger)) -- gap +5.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06VALROY-1-VAL` Will Adolfo Daniel Vallejo win set 1 in the Adolfo Daniel Vallejo vs Valentin Royer match: 0.53/0.56 mid 54.5%, model 49.6% (projection_v2.0 (prediction ledger)) -- gap -4.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT06VALROY-ROY2` Will Valentin Royer win at least 1.5 more games than Adolfo Daniel Vallejo?: 0.37/0.42 mid 39.5%, model 43.4% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT06VALROY-2-ROY` Will Valentin Royer win set 2 in the Adolfo Daniel Vallejo vs Valentin Royer match: 0.46/0.47 mid 46.5%, model 50.4% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06VALROY-2-VAL` Will Adolfo Daniel Vallejo win set 2 in the Adolfo Daniel Vallejo vs Valentin Royer match: 0.52/0.55 mid 53.5%, model 49.6% (projection_v2.0 (prediction ledger)) -- gap -3.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06VALROY-VAL21` Will Adolfo Daniel Vallejo win the Adolfo Daniel Vallejo vs Valentin Royer match by a set score of 2-1?: 0.20/0.23 mid 21.5%, model 24.8% (projection_v2.0 (prediction ledger)) -- gap +3.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06VALROY-30` Over 29.5 games: 0.19/0.32 mid 25.5%, model 28.5% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06VALROY-ROY20` Will Valentin Royer win the Adolfo Daniel Vallejo vs Valentin Royer match by a set score of 2-0?: 0.24/0.27 mid 25.5%, model 25.4% (projection_v2.0 (prediction ledger)) -- gap -0.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Botic Van de Zandschulp vs Daniel Merida -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-08T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:122298:210017:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Merida (`KXATPMATCH-26OCT06VANMER-MER`) | 0.49 / 0.51 (15218) | 50.0% | 40.8% | 36.8% | 36.8% [34.4%-37.8%] | -- | -- | -- | -- | PASS | -9.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Botic Van de Zandschulp (`KXATPMATCH-26OCT06VANMER-VAN`) | 0.49 / 0.51 (11060) | 50.0% | 59.2% | 63.2% | 63.2% [62.2%-65.6%] | -- | -- | -- | -- | PASS | +9.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 5744.0, B 5739.0; serve-point win A 60.9%, B 40.9%; Elo A 1880.9, B 1779.0; model uncertainty 0.017
* Form inputs: days since last match A 5, B 32; matches on record A 644, B 359; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.015, surface_dev_loose -0.000, surface_dev_tight +0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT06VANMER-MER5` Will Daniel Merida win at least 4.5 more games than Botic Van de Zandschulp?: 0.19/0.34 mid 26.5%, model 14.5% (projection_v2.0 (prediction ledger)) -- gap -12.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT06VANMER-MER2` Will Daniel Merida win at least 1.5 more games than Botic Van de Zandschulp?: 0.43/0.46 mid 44.5%, model 34.1% (projection_v2.0 (prediction ledger)) -- gap -10.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06VANMER-MER20` Will Daniel Merida win the Botic Van de Zandschulp vs Daniel Merida match by a set score of 2-0?: 0.27/0.31 mid 29.0%, model 19.2% (projection_v2.0 (prediction ledger)) -- gap -9.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT06VANMER-VAN2` Will Botic Van de Zandschulp win at least 1.5 more games than Daniel Merida?: 0.42/0.46 mid 44.0%, model 52.4% (projection_v2.0 (prediction ledger)) -- gap +8.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT06VANMER-19` Over 18.5 games: 0.67/0.84 mid 75.5%, model 83.8% (projection_v2.0 (prediction ledger)) -- gap +8.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06VANMER-VAN21` Will Botic Van de Zandschulp win the Botic Van de Zandschulp vs Daniel Merida match by a set score of 2-1?: 0.18/0.22 mid 20.0%, model 27.7% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06VANMER-1-MER` Will Daniel Merida win set 1 in the Botic Van de Zandschulp vs Daniel Merida match: 0.49/0.53 mid 51.0%, model 43.8% (projection_v2.0 (prediction ledger)) -- gap -7.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06VANMER-1-VAN` Will Botic Van de Zandschulp win set 1 in the Botic Van de Zandschulp vs Daniel Merida match: 0.48/0.51 mid 49.5%, model 56.2% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT06VANMER-24` Over 23.5 games: 0.44/0.48 mid 46.0%, model 52.3% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT06VANMER-29` Over 28.5 games: 0.22/0.33 mid 27.5%, model 31.5% (projection_v2.0 (prediction ledger)) -- gap +4.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06VANMER-VAN20` Will Botic Van de Zandschulp win the Botic Van de Zandschulp vs Daniel Merida match by a set score of 2-0?: 0.27/0.31 mid 29.0%, model 31.6% (projection_v2.0 (prediction ledger)) -- gap +2.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06VANMER-MER21` Will Daniel Merida win the Botic Van de Zandschulp vs Daniel Merida match by a set score of 2-1?: 0.18/0.22 mid 20.0%, model 21.6% (projection_v2.0 (prediction ledger)) -- gap +1.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06VANMER-2-MER` Will Daniel Merida win set 2 in the Botic Van de Zandschulp vs Daniel Merida match: 0.35/0.55 mid 45.0%, model 43.8% (projection_v2.0 (prediction ledger)) -- gap -1.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06VANMER-2-VAN` Will Botic Van de Zandschulp win set 2 in the Botic Van de Zandschulp vs Daniel Merida match: 0.45/0.69 mid 57.0%, model 56.2% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Luca Van Assche vs Yunchaokete Bu -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-08T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207352:209414:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luca Van Assche (`KXATPMATCH-26OCT06VANYUN-VAN`) | 0.40 / 0.41 (3100) | 40.5% | 50.5% | 59.5% | 57.0% [55.5%-59.0%] | -- | -- | -- | -- | WATCH | +10.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Yunchaokete Bu (`KXATPMATCH-26OCT06VANYUN-YUN`) | 0.60 / 0.61 (20336) | 60.5% | 49.5% | 40.5% | 43.0% [41.0%-44.5%] | -- | -- | -- | -- | PASS | -11.0 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 6331.0, B 4671.0; serve-point win A 62.9%, B 37.1%; Elo A 1808.9, B 1807.7; model uncertainty 0.0173
* Form inputs: days since last match A 6, B 4; matches on record A 389, B 338; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.015, surface_dev_loose +0.005, surface_dev_tight -0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT06VANYUN-YUN3` Will Yunchaokete Bu win at least 2.5 more games than Luca Van Assche?: 0.48/0.50 mid 49.0%, model 35.5% (projection_v2.0 (prediction ledger)) -- gap -13.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06VANYUN-YUN20` Will Yunchaokete Bu win the Luca Van Assche vs Yunchaokete Bu match by a set score of 2-0?: 0.36/0.39 mid 37.5%, model 24.7% (projection_v2.0 (prediction ledger)) -- gap -12.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT06VANYUN-YUN6` Will Yunchaokete Bu win at least 5.5 more games than Luca Van Assche?: 0.18/0.23 mid 20.5%, model 9.2% (projection_v2.0 (prediction ledger)) -- gap -11.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT06VANYUN-23` Over 22.5 games: 0.49/0.51 mid 50.0%, model 60.6% (projection_v2.0 (prediction ledger)) -- gap +10.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT06VANYUN-28` Over 27.5 games: 0.27/0.33 mid 30.0%, model 40.1% (projection_v2.0 (prediction ledger)) -- gap +10.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT06VANYUN-VAN2` Will Luca Van Assche win at least 1.5 more games than Yunchaokete Bu?: 0.32/0.37 mid 34.5%, model 43.1% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06VANYUN-1-YUN` Will Yunchaokete Bu win set 1 in the Luca Van Assche vs Yunchaokete Bu match: 0.57/0.59 mid 58.0%, model 49.7% (projection_v2.0 (prediction ledger)) -- gap -8.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06VANYUN-1-VAN` Will Luca Van Assche win set 1 in the Luca Van Assche vs Yunchaokete Bu match: 0.41/0.44 mid 42.5%, model 50.3% (projection_v2.0 (prediction ledger)) -- gap +7.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06VANYUN-2-VAN` Will Luca Van Assche win set 2 in the Luca Van Assche vs Yunchaokete Bu match: 0.41/0.44 mid 42.5%, model 50.3% (projection_v2.0 (prediction ledger)) -- gap +7.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06VANYUN-2-YUN` Will Yunchaokete Bu win set 2 in the Luca Van Assche vs Yunchaokete Bu match: 0.56/0.59 mid 57.5%, model 49.7% (projection_v2.0 (prediction ledger)) -- gap -7.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06VANYUN-VAN21` Will Luca Van Assche win the Luca Van Assche vs Yunchaokete Bu match by a set score of 2-1?: 0.16/0.19 mid 17.5%, model 25.2% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT06VANYUN-18` Over 17.5 games: 0.86/0.90 mid 88.0%, model 93.0% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06VANYUN-VAN20` Will Luca Van Assche win the Luca Van Assche vs Yunchaokete Bu match by a set score of 2-0?: 0.21/0.24 mid 22.5%, model 25.3% (projection_v2.0 (prediction ledger)) -- gap +2.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06VANYUN-YUN21` Will Yunchaokete Bu win the Luca Van Assche vs Yunchaokete Bu match by a set score of 2-1?: 0.21/0.24 mid 22.5%, model 24.8% (projection_v2.0 (prediction ledger)) -- gap +2.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Felix Balshaw vs Joel Schwaerzler -- ATP Challenger Villena R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-06T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212082:213149:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felix Balshaw (`KXATPCHALLENGERMATCH-26OCT06BALSCH-BAL`) | 0.53 / 0.54 (0) | 53.5% | 55.5% | 64.3% | 60.6% [58.3%-62.9%] | -- | -- | -- | -- | SHADOW_BET | +2.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Joel Schwaerzler (`KXATPCHALLENGERMATCH-26OCT06BALSCH-SCH`) | 0.42 / 0.45 (121) | 43.5% | 44.5% | 35.7% | 39.4% [37.1%-41.7%] | -- | -- | -- | -- | PASS | +1.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4242.0, B 4654.0; serve-point win A 66.3%, B 34.9%; Elo A 1611.5, B 1607.8; model uncertainty 0.0233
* Form inputs: days since last match A 8, B 8; matches on record A 120, B 175; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.000, surface_dev_loose +0.004, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Matej Dodig vs Andrea Pellegrino -- ATP Challenger Braga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126504:212063:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matej Dodig (`KXATPCHALLENGERMATCH-26OCT06DODPEL-DOD`) | 0.60 / 0.61 (362) | 60.5% | 49.5% | 54.5% | 51.0% [49.0%-52.5%] | -- | 61.4% | 61.4% | MODEL_LONE_OUTLIER | PASS | -11.1 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Andrea Pellegrino (`KXATPCHALLENGERMATCH-26OCT06DODPEL-PEL`) | 0.38 / 0.40 (499) | 39.0% | 50.5% | 45.5% | 49.0% [47.5%-51.0%] | -- | 38.8% | 38.8% | MODEL_LONE_OUTLIER | SHADOW_BET | +11.6 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4783.0, B 4868.0; serve-point win A 63.8%, B 36.1%; Elo A 1702.9, B 1768.8; model uncertainty 0.0175
* Form inputs: days since last match A 17, B 29; matches on record A 248, B 641; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.000, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER

## Daniil Glinka vs Gauthier Onclin -- ATP Challenger Villena R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-06T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206750:206904:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniil Glinka (`KXATPCHALLENGERMATCH-26OCT06GLIONC-GLI`) | 0.64 / 0.65 (22220) | 64.5% | 45.3% | 40.4% | 41.9% [39.9%-42.9%] | -- | -- | -- | -- | PASS | -19.2 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gauthier Onclin (`KXATPCHALLENGERMATCH-26OCT06GLIONC-ONC`) | 0.35 / 0.36 (28122) | 35.5% | 54.7% | 59.6% | 58.1% [57.1%-60.1%] | -- | -- | -- | -- | SHADOW_BET | +19.2 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5087.0, B 4854.0; serve-point win A 60.6%, B 38.5%; Elo A 1639.8, B 1672.9; model uncertainty 0.0149
* Form inputs: days since last match A 8, B 8; matches on record A 382, B 463; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT06GLIONC-ONC  (YES = Gauthier Onclin)
Model: 55%
Kalshi: 36%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.010, surface_dev_loose -0.020, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Sumit Nagal vs Luka Mikrut -- ATP Challenger Braga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111576:210053:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luka Mikrut (`KXATPCHALLENGERMATCH-26OCT06NAGMIK-MIK`) | 0.74 / 0.78 (102) | 76.0% | 72.7% | 76.0% | 72.7% [67.8%-76.0%] | -- | -- | -- | -- | PASS | -3.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sumit Nagal (`KXATPCHALLENGERMATCH-26OCT06NAGMIK-NAG`) | 0.22 / 0.25 (2608) | 23.5% | 27.4% | 24.0% | 27.3% [24.0%-32.2%] | -- | -- | -- | -- | PASS | +3.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4981.0, B 3483.0; serve-point win A 58.4%, B 36.9%; Elo A 1666.7, B 1772.3; model uncertainty 0.0411
* Form inputs: days since last match A 18, B 15; matches on record A 656, B 236; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.013, surface_dev_loose -0.021, surface_dev_tight +0.017
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Johan Nikles vs Miguel Damas -- ATP Challenger Braga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126627:207732:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miguel Damas (`KXATPCHALLENGERMATCH-26OCT06NIKDAM-DAM`) | 0.54 / 0.56 (408) | 55.0% | 51.6% | 43.1% | 46.3% [44.2%-49.5%] | -- | 56.2% | 56.2% | MODEL_LONE_OUTLIER | PASS | -3.4 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Johan Nikles (`KXATPCHALLENGERMATCH-26OCT06NIKDAM-NIK`) | 0.43 / 0.45 (170) | 44.0% | 48.4% | 56.9% | 53.7% [50.5%-55.8%] | -- | 43.9% | 43.9% | MODEL_LONE_OUTLIER | SHADOW_BET | +4.4 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3626.0, B 5525.0; serve-point win A 54.4%, B 45.3%; Elo A 1549.4, B 1574.0; model uncertainty 0.0266
* Form inputs: days since last match A 22, B 29; matches on record A 483, B 385; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER

## Philip Henning vs Maks Kasnikowski -- ATP Challenger Villena R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 13:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-06T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202475:209874:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Philip Henning (`KXATPCHALLENGERMATCH-26OCT06HENKAS-HEN`) | 0.43 / 0.45 (6461) | 44.0% | 45.1% | 59.5% | 55.6% [51.0%-59.0%] | -- | 43.6% | 43.6% | MODEL_LONE_OUTLIER | SHADOW_BET | +1.1 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Maks Kasnikowski (`KXATPCHALLENGERMATCH-26OCT06HENKAS-KAS`) | 0.55 / 0.57 (1155) | 56.0% | 54.9% | 40.5% | 44.4% [41.0%-49.0%] | -- | 56.0% | 56.0% | MODEL_LONE_OUTLIER | PASS | -1.1 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3773.0, B 5200.0; serve-point win A 61.8%, B 37.2%; Elo A 1603.0, B 1621.2; model uncertainty 0.0401
* Form inputs: days since last match A 8, B 17; matches on record A 212, B 326; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.020, surface_dev_loose +0.015, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER

## Carles Hernandez vs Pyotr Nesterov -- ATP Challenger Villena R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 13:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-06T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208264:209318:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carles Hernandez (`KXATPCHALLENGERMATCH-26OCT06HERNES-HER`) | 0.25 / 0.26 (2839) | 25.5% | 20.0% | 19.2% | 18.2% [16.9%-19.6%] | -- | 18.7% | 18.7% | MARKETS_AGREE | PASS | -5.5 pp | NORMAL | FRESH | B / LIMITED | AGREES_WITH_MODEL | AMBIGUOUS |
| Pyotr Nesterov (`KXATPCHALLENGERMATCH-26OCT06HERNES-NES`) | 0.74 / 0.75 (22876) | 74.5% | 80.0% | 80.8% | 81.8% [80.4%-83.2%] | -- | 81.3% | 81.3% | MARKETS_AGREE | PASS | +5.5 pp | NORMAL | FRESH | B / LIMITED | AGREES_WITH_MODEL | AMBIGUOUS |

* Serve evidence (points): A 2103.0, B 4166.0; serve-point win A 57.8%, B 35.6%; Elo A 1253.2, B 1529.9; model uncertainty 0.0136
* Form inputs: days since last match A 141, B 8; matches on record A 85, B 272; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.014, surface_dev_loose -0.006, surface_dev_tight +0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER

## Oleksii Krutykh vs Javier Barranco Cosano -- ATP Challenger Braga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 13:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200266:208071:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Javier Barranco Cosano (`KXATPCHALLENGERMATCH-26OCT06KRUBAR-BAR`) | 0.41 / 0.42 (123) | 41.5% | 59.1% | 48.4% | 54.7% [52.1%-57.3%] | 42.8% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +17.6 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oleksii Krutykh (`KXATPCHALLENGERMATCH-26OCT06KRUBAR-KRU`) | 0.58 / 0.59 (3167) | 58.5% | 40.9% | 51.6% | 45.3% [42.7%-47.9%] | 57.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -17.6 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3648.0, B 3059.0; serve-point win A 57.4%, B 40.9%; Elo A 1490.7, B 1605.1; model uncertainty 0.0259
* Form inputs: days since last match A 17, B 50; matches on record A 472, B 570; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT06KRUBAR-BAR  (YES = Javier Barranco Cosano)
Model: 59%
Kalshi: 42%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

## Francesco Maestrelli vs Oliver Tarvet -- ATP Challenger Villena R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 13:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-06T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208353:210472:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesco Maestrelli (`KXATPCHALLENGERMATCH-26OCT06MAETAR-MAE`) | 0.23 / 0.26 (7913) | 24.5% | 27.7% | 22.7% | 27.4% [22.3%-35.8%] | -- | 23.9% | 23.9% | MODEL_LONE_OUTLIER | PASS | +3.1 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Oliver Tarvet (`KXATPCHALLENGERMATCH-26OCT06MAETAR-TAR`) | 0.75 / 0.77 (8567) | 76.0% | 72.4% | 77.3% | 72.6% [64.2%-77.7%] | -- | 75.8% | 75.8% | MODEL_LONE_OUTLIER | PASS | -3.6 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5164.0, B 1824.0; serve-point win A 61.4%, B 33.9%; Elo A 1603.9, B 1721.7; model uncertainty 0.0675
* Form inputs: days since last match A 15, B 43; matches on record A 363, B 86; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.020, surface_dev_loose -0.012, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER

## Patrick Schoen vs Andrej Nedic -- ATP Challenger Braga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 13:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210119:211566:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrej Nedic (`KXATPCHALLENGERMATCH-26OCT06SCHNED-NED`) | 0.51 / 0.53 (453) | 52.0% | 62.2% | 49.0% | 58.8% [54.7%-61.8%] | 52.0% | -- | 52.0% | MARKETS_AGREE | WATCH | +10.2 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Patrick Schoen (`KXATPCHALLENGERMATCH-26OCT06SCHNED-SCH`) | 0.46 / 0.47 (363) | 46.5% | 37.8% | 51.0% | 41.2% [38.2%-45.3%] | 48.0% | -- | 48.0% | MARKETS_AGREE | PASS | -8.7 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1754.0, B 4271.0; serve-point win A 57.4%, B 40.2%; Elo A 1486.2, B 1625.3; model uncertainty 0.0356
* Form inputs: days since last match A 36, B 17; matches on record A 85, B 233; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.020, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER

## Kalin Ivanovski vs Alejandro Moro Canas -- ATP Challenger Palermo R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 13:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T13:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208279:209928:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kalin Ivanovski (`KXATPCHALLENGERMATCH-26OCT06IVAMOR-IVA`) | 0.07 / 0.08 (9168) | 7.5% | 38.5% | 42.4% | 38.0% [28.3%-41.0%] | -- | -- | -- | -- | PASS | +30.9 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alejandro Moro Canas (`KXATPCHALLENGERMATCH-26OCT06IVAMOR-MOR`) | 0.92 / 0.93 (7023) | 92.5% | 61.6% | 57.6% | 62.0% [59.0%-71.7%] | -- | -- | -- | -- | PASS | -30.9 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2540.0, B 5786.0; serve-point win A 61.0%, B 36.7%; Elo A 1491.4, B 1628.6; model uncertainty 0.0635
* Form inputs: days since last match A 435, B 22; matches on record A 177, B 357; data quality D

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT06IVAMOR-IVA  (YES = Kalin Ivanovski)
Model: 38%
Kalshi: 8%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.015, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE

## Zdenek Kolar vs Dimitris Sakellaridis -- ATP Challenger Palermo R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 13:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T13:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144645:212029:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zdenek Kolar (`KXATPCHALLENGERMATCH-26OCT06KOLSAK-KOL`) | 0.98 / 0.99 (4662) | 98.5% | 85.6% | 82.5% | 84.1% [83.1%-85.1%] | -- | -- | -- | -- | PASS | -12.9 pp | REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dimitris Sakellaridis (`KXATPCHALLENGERMATCH-26OCT06KOLSAK-SAK`) | 0.01 / 0.02 (5117) | 1.5% | 14.4% | 17.5% | 15.9% [14.9%-16.9%] | -- | -- | -- | -- | PASS | +12.9 pp | REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5539.0, B 4537.0; serve-point win A 61.3%, B 46.8%; Elo A 1627.2, B 1281.1; model uncertainty 0.0098
* Form inputs: days since last match A 22, B 71; matches on record A 832, B 154; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.006, surface_pool_high +0.003, surface_dev_loose +0.003, surface_dev_tight -0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE

## Dali Blanch vs Max Alcala Gurri -- ATP Challenger Braga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 14:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T14:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208024:209898:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Max Alcala Gurri (`KXATPCHALLENGERMATCH-26OCT06BLAALC-ALC`) | 0.68 / 0.69 (3985) | 68.5% | 67.0% | 74.2% | 72.0% [69.7%-72.9%] | 67.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dali Blanch (`KXATPCHALLENGERMATCH-26OCT06BLAALC-BLA`) | 0.31 / 0.32 (494) | 31.5% | 33.0% | 25.8% | 28.0% [27.1%-30.3%] | 32.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4556.0, B 5372.0; serve-point win A 54.3%, B 42.4%; Elo A 1581.8, B 1687.8; model uncertainty 0.0161
* Form inputs: days since last match A 15, B 15; matches on record A 301, B 383; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; EXTERNAL_PRICE_STALE

## Mackenzie McDonald vs Ryan Nijboer -- ATP Challenger Braga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 14:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T14:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111456:207764:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mackenzie McDonald (`KXATPCHALLENGERMATCH-26OCT06MCDNIJ-MCD`) | 0.46 / 0.47 (8882) | 46.5% | 57.7% | 44.3% | 48.4% [40.8%-61.7%] | 44.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +11.2 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ryan Nijboer (`KXATPCHALLENGERMATCH-26OCT06MCDNIJ-NIJ`) | 0.53 / 0.54 (30699) | 53.5% | 42.3% | 55.7% | 51.5% [38.3%-59.2%] | 55.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.2 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4329.0, B 3899.0; serve-point win A 60.7%, B 40.8%; Elo A 1551.0, B 1494.4; model uncertainty 0.1045
* Form inputs: days since last match A 8, B 15; matches on record A 659, B 474; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.052, surface_pool_high -0.061, surface_dev_loose -0.077, surface_dev_tight +0.057
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; EXTERNAL_PRICE_STALE

## Mateo Luis Alvarez Sarmiento vs Daniel Verbeek -- M15 Pontevedra R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-06T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211392:211490:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mateo Luis Alvarez Sarmiento (`KXITFMATCH-26OCT06ALVVER-ALV`) | 0.28 / 0.29 (4724) | 28.5% | 42.2% | 58.8% | 49.5% [48.4%-50.5%] | -- | -- | -- | -- | PASS | +13.7 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daniel Verbeek (`KXITFMATCH-26OCT06ALVVER-VER`) | 0.71 / 0.72 (1946) | 71.5% | 57.8% | 41.2% | 50.5% [49.5%-51.5%] | -- | -- | -- | -- | PASS | -13.7 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 273.0, B 853.0; serve-point win A 58.5%, B 40.0%; Elo A 1116.4, B 1131.1; model uncertainty 0.0104
* Form inputs: days since last match A 162, B 141; matches on record A 20, B 29; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ivan Gakhov vs Yanaki Milev -- ATP Challenger Palermo R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:123809:210200:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ivan Gakhov (`KXATPCHALLENGERMATCH-26OCT06GAKMIL-GAK`) | 0.56 / 0.58 (57) | 57.0% | 72.6% | 66.2% | 69.5% [68.1%-70.8%] | -- | 55.7% | 55.7% | MODEL_LONE_OUTLIER | PASS | +15.6 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Yanaki Milev (`KXATPCHALLENGERMATCH-26OCT06GAKMIL-MIL`) | 0.42 / 0.44 (74) | 43.0% | 27.4% | 33.8% | 30.5% [29.2%-31.9%] | -- | 44.3% | 44.3% | MODEL_LONE_OUTLIER | PASS | -15.6 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4293.0, B 3245.0; serve-point win A 60.8%, B 43.8%; Elo A 1598.8, B 1397.5; model uncertainty 0.0138
* Form inputs: days since last match A 22, B 36; matches on record A 856, B 228; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT06GAKMIL-GAK  (YES = Ivan Gakhov)
Model: 73%
Kalshi: 57%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.004, surface_dev_loose +0.000, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED

## Christian Langmo vs Lorenzo Giustino -- ATP Challenger Palermo R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105841:132052:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Giustino (`KXATPCHALLENGERMATCH-26OCT06LANGIU-GIU`) | 0.74 / 0.76 (95) | 75.0% | 65.2% | 59.9% | 64.1% [62.3%-67.3%] | 74.0% | 74.7% | 74.3% | MODEL_LONE_OUTLIER | PASS | -9.8 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Christian Langmo (`KXATPCHALLENGERMATCH-26OCT06LANGIU-LAN`) | 0.24 / 0.26 (8875) | 25.0% | 34.8% | 40.1% | 35.9% [32.6%-37.8%] | 26.0% | 25.2% | 25.6% | MODEL_LONE_OUTLIER | SHADOW_BET | +9.8 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4655.0, B 5516.0; serve-point win A 62.4%, B 34.5%; Elo A 1427.1, B 1624.5; model uncertainty 0.0255
* Form inputs: days since last match A 29, B 8; matches on record A 450, B 1089; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED

## Andres Pereiro Lopez vs Valentin Gonzalez-Galino -- M15 Pontevedra R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06PERGON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentin Gonzalez-Galino (`KXITFMATCH-26OCT06PERGON-GON`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Andres Pereiro Lopez (`KXITFMATCH-26OCT06PERGON-PER`) | -- / 0.01 (9351) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luca Potenza vs Enrico Dalla Valle -- ATP Challenger Palermo R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133872:206553:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Enrico Dalla Valle (`KXATPCHALLENGERMATCH-26OCT06POTDAL-DAL`) | 0.80 / 0.82 (11300) | 81.0% | 77.2% | 74.7% | 75.9% [74.3%-77.4%] | -- | 80.7% | 80.7% | MODEL_LONE_OUTLIER | PASS | -3.8 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Luca Potenza (`KXATPCHALLENGERMATCH-26OCT06POTDAL-POT`) | 0.18 / 0.20 (3135) | 19.0% | 22.8% | 25.3% | 24.1% [22.6%-25.7%] | -- | 19.8% | 19.8% | MODEL_LONE_OUTLIER | WATCH | +3.8 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3694.0, B 5117.0; serve-point win A 60.4%, B 33.7%; Elo A 1381.5, B 1616.9; model uncertainty 0.0156
* Form inputs: days since last match A 8, B 8; matches on record A 351, B 488; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.015, surface_dev_loose -0.008, surface_dev_tight +0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED

## Leolia Jeanjean vs Mariam Bolkvadze -- WTA 125K Samsun R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-07T04:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

WTA125 (WTA_125) · Hard · scheduled 2026-10-06T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:206417:213734:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mariam Bolkvadze (`KXWTACHALLENGERMATCH-26OCT06JEABOL-BOL`) | 0.29 / 0.30 (1263) | 29.5% | 44.1% | 56.3% | 50.5% [40.0%-55.3%] | 31.2% | 29.7% | 30.5% | MODEL_LONE_OUTLIER | WATCH | +14.6 pp | REVIEW | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Leolia Jeanjean (`KXWTACHALLENGERMATCH-26OCT06JEABOL-JEA`) | 0.71 / 0.72 (12694) | 71.5% | 55.9% | 43.7% | 49.5% [44.7%-60.0%] | 68.8% | 71.2% | 70.0% | MODEL_LONE_OUTLIER | PASS | -15.6 pp | HIGH_REVIEW | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4130.0, B 1814.0; serve-point win A 56.1%, B 45.0%; Elo A 1777.0, B 1731.0; model uncertainty 0.0763
* Form inputs: days since last match A 2, B 1; matches on record A 436, B 551; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.032, surface_pool_high -0.032, surface_dev_loose -0.016, surface_dev_tight +0.016
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED

## Tiago Pereira vs Pol Martin Tiffon -- ATP Challenger Braga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 14:55Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T14:55:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207546:211500:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pol Martin Tiffon (`KXATPCHALLENGERMATCH-26OCT06PERMAR-MAR`) | 0.61 / 0.63 (3260) | 62.0% | 68.0% | 60.7% | 66.1% [63.7%-68.9%] | 60.9% | -- | 60.9% | MODEL_LONE_OUTLIER | WATCH | +6.0 pp | NORMAL | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Tiago Pereira (`KXATPCHALLENGERMATCH-26OCT06PERMAR-PER`) | 0.37 / 0.39 (865) | 38.0% | 32.0% | 39.3% | 33.9% [31.1%-36.3%] | 39.1% | -- | 39.1% | MODEL_LONE_OUTLIER | PASS | -6.0 pp | NORMAL | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5117.0, B 3622.0; serve-point win A 58.0%, B 38.4%; Elo A 1437.2, B 1656.8; model uncertainty 0.0261
* Form inputs: days since last match A 77, B 8; matches on record A 280, B 484; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.024, surface_pool_high -0.019, surface_dev_loose -0.009, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED

## Elena Pridankina vs Anna Blinkova -- WTA 125K Samsun R32

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-06 12:20Z
* Current expected start: 2026-10-06 15:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-06 14:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA125 (WTA_125) · Hard · scheduled 2026-10-06T12:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:215020:239389:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Blinkova (`KXWTACHALLENGERMATCH-26OCT06PRIBLI-BLI`) | 0.68 / 0.69 (2235) | 68.5% | 58.4% | 31.9% | 40.5% [36.9%-52.7%] | -- | -- | -- | INSUFFICIENT_INPUTS | PASS | -10.1 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elena Pridankina (`KXWTACHALLENGERMATCH-26OCT06PRIBLI-PRI`) | 0.31 / 0.32 (3780) | 31.5% | 41.6% | 68.1% | 59.5% [47.3%-63.1%] | -- | 29.9% | -- | INSUFFICIENT_INPUTS | WATCH | +10.1 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3685.0, B 4417.0; serve-point win A 51.6%, B 46.8%; Elo A 1726.4, B 1822.4; model uncertainty 0.0791
* Form inputs: days since last match A 4, B 5; matches on record A 286, B 628; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose +0.015, surface_dev_tight -0.026
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE

## Hynek Barton vs Toby Samuel -- ATP Challenger Villena R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-06T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210389:210558:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hynek Barton (`KXATPCHALLENGERMATCH-26OCT06BARSAM-BAR`) | 0.19 / 0.20 (3658) | 19.5% | 21.9% | 13.8% | 15.8% [14.4%-18.1%] | 22.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Toby Samuel (`KXATPCHALLENGERMATCH-26OCT06BARSAM-SAM`) | 0.80 / 0.81 (2133) | 80.5% | 78.1% | 86.2% | 84.2% [82.0%-85.6%] | 77.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5731.0, B 3862.0; serve-point win A 59.2%, B 34.7%; Elo A 1611.3, B 1827.0; model uncertainty 0.0184
* Form inputs: days since last match A 22, B 8; matches on record A 271, B 185; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.006, surface_dev_loose -0.011, surface_dev_tight +0.022
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

## Florian Broska vs Lukas Neumayer -- ATP Challenger Braga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202239:209903:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Florian Broska (`KXATPCHALLENGERMATCH-26OCT06BRONEU-BRO`) | 0.27 / 0.28 (197) | 27.5% | 25.7% | 45.0% | 36.1% [32.0%-40.0%] | 29.4% | -- | 29.4% | MODEL_LONE_OUTLIER | SHADOW_BET | -1.8 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Lukas Neumayer (`KXATPCHALLENGERMATCH-26OCT06BRONEU-NEU`) | 0.72 / 0.73 (5708) | 72.5% | 74.3% | 55.0% | 63.8% [60.0%-68.0%] | 70.6% | -- | 70.6% | MODEL_LONE_OUTLIER | PASS | +1.8 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3459.0, B 5238.0; serve-point win A 59.9%, B 34.9%; Elo A 1485.5, B 1727.2; model uncertainty 0.0402
* Form inputs: days since last match A 15, B 15; matches on record A 218, B 402; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.009, surface_dev_loose +0.000, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER

## Tiago Cacao / Francisco Rocha vs Finn Bass / Scott Duncan -- ATP Challenger Braga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-06T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06CACROCBASDUN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Finn Bass / Scott Duncan (`KXATPCHALLENGERDOUBLES-26OCT06CACROCBASDUN-BASDUN`) | 0.52 / 0.67 (10) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tiago Cacao / Francisco Rocha (`KXATPCHALLENGERDOUBLES-26OCT06CACROCBASDUN-CACROC`) | 0.33 / 0.48 (132) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Ian Lucca Cervantes Tomas vs Mario Arce Fernandez -- M15 Pontevedra R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-06T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212486:213535:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mario Arce Fernandez (`KXITFMATCH-26OCT06CERARC-ARC`) | 0.51 / 0.55 (443) | 53.0% | 47.1% | 60.4% | 54.2% [53.1%-55.2%] | -- | -- | -- | -- | PASS | -5.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ian Lucca Cervantes Tomas (`KXITFMATCH-26OCT06CERARC-CER`) | 0.44 / 0.47 (2) | 45.5% | 52.9% | 39.6% | 45.8% [44.8%-46.9%] | -- | -- | -- | -- | PASS | +7.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 529.0, B 239.0; serve-point win A 58.1%, B 42.5%; Elo A 1163.1, B 1186.1; model uncertainty 0.0107
* Form inputs: days since last match A 379, B 176; matches on record A 24, B 7; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## August Holmgren vs Pedro Martinez -- ATP Challenger Villena R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-06T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:124079:200416:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| August Holmgren (`KXATPCHALLENGERMATCH-26OCT06HOLMAR-HOL`) | 0.51 / 0.52 (6294) | 51.5% | 59.0% | 59.3% | 56.9% [53.0%-58.4%] | 51.0% | 50.5% | 50.8% | MARKETS_AGREE | WATCH | +7.5 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Pedro Martinez (`KXATPCHALLENGERMATCH-26OCT06HOLMAR-MAR`) | 0.48 / 0.49 (3877) | 48.5% | 41.0% | 40.7% | 43.1% [41.6%-47.0%] | 49.0% | 49.1% | 49.0% | MARKETS_AGREE | PASS | -7.5 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4680.0, B 5163.0; serve-point win A 65.3%, B 36.5%; Elo A 1620.9, B 1636.6; model uncertainty 0.0269
* Form inputs: days since last match A 8, B 15; matches on record A 319, B 804; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.005, surface_dev_loose +0.005, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER

## Vasco Leote Prata vs Ziga Sesko -- M15 Pontevedra R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-06T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211330:212949:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vasco Leote Prata (`KXITFMATCH-26OCT06LEOSES-LEO`) | 0.25 / 0.41 (43) | 33.0% | 32.3% | 32.8% | 43.8% [40.1%-47.4%] | -- | -- | -- | -- | PASS | -0.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ziga Sesko (`KXITFMATCH-26OCT06LEOSES-SES`) | 0.52 / 0.71 (89) | 61.5% | 67.7% | 67.2% | 56.2% [52.6%-59.9%] | -- | -- | -- | -- | PASS | +6.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 516.0, B 1006.0; serve-point win A 56.2%, B 40.3%; Elo A 1350.1, B 1365.8; model uncertainty 0.0364
* Form inputs: days since last match A 435, B 35; matches on record A 17, B 34; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dominic Stricker vs Laslo Djere -- ATP Challenger Villena R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-06T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111513:208502:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Laslo Djere (`KXATPCHALLENGERMATCH-26OCT06STRDJE-DJE`) | 0.40 / 0.41 (5416) | 40.5% | 49.4% | 42.7% | 43.1% [41.3%-46.6%] | -- | 40.7% | 40.7% | MODEL_LONE_OUTLIER | PASS | +8.9 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Dominic Stricker (`KXATPCHALLENGERMATCH-26OCT06STRDJE-STR`) | 0.59 / 0.60 (1674) | 59.5% | 50.6% | 57.3% | 56.9% [53.4%-58.7%] | -- | 59.2% | 59.2% | MODEL_LONE_OUTLIER | PASS | -8.9 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3466.0, B 4279.0; serve-point win A 65.3%, B 34.8%; Elo A 1706.2, B 1668.0; model uncertainty 0.0265
* Form inputs: days since last match A 8, B 8; matches on record A 291, B 768; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.019, surface_dev_tight -0.019
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER

## Gian Luca Tanner vs David Eichenseher -- M15 Pontevedra R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-06T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209198:212631:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| David Eichenseher (`KXITFMATCH-26OCT06TANEIC-EIC`) | 0.27 / 0.49 (6) | 38.0% | 29.8% | 17.8% | 24.6% [19.9%-31.9%] | -- | -- | -- | -- | PASS | -8.2 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gian Luca Tanner (`KXITFMATCH-26OCT06TANEIC-TAN`) | 0.50 / 0.57 (1) | 53.5% | 70.2% | 82.2% | 75.4% [68.2%-80.2%] | -- | -- | -- | -- | PASS | +16.7 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1550.0, B 1660.0; serve-point win A 58.5%, B 45.5%; Elo A 1378.0, B 1256.5; model uncertainty 0.06
* Form inputs: days since last match A 169, B 127; matches on record A 54, B 39; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT06TANEIC-TAN  (YES = Gian Luca Tanner)
Model: 70%
Kalshi: 54%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.008, surface_dev_loose +0.000, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elvin Egribel vs Caroline Werner -- WTA 125K Samsun R32

**START STATUS: START_IMMINENT**
* Nominal schedule: 2026-10-06 15:40Z
* Current expected start: 2026-10-06 15:40Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-06 14:55Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-06T15:40:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT06EGRWER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elvin Egribel (`KXWTACHALLENGERMATCH-26OCT06EGRWER-EGR`) | 0.05 / 0.06 (6654) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Caroline Werner (`KXWTACHALLENGERMATCH-26OCT06EGRWER-WER`) | 0.94 / 0.95 (89) | 94.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Marvin Moeller vs Tiago Torres -- ATP Challenger Braga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 16:05Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T16:05:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202359:208426:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marvin Moeller (`KXATPCHALLENGERMATCH-26OCT06MOETOR-MOE`) | 0.63 / 0.65 (3824) | 64.0% | 66.7% | 74.1% | 70.6% [68.2%-72.0%] | 60.9% | -- | 60.9% | MODEL_LONE_OUTLIER | PASS | +2.7 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_OUTLIER | VERIFIED |
| Tiago Torres (`KXATPCHALLENGERMATCH-26OCT06MOETOR-TOR`) | 0.35 / 0.37 (8766) | 36.0% | 33.3% | 25.9% | 29.4% [28.0%-31.8%] | 39.1% | -- | 39.1% | MODEL_LONE_OUTLIER | PASS | -2.7 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_OUTLIER | VERIFIED |

* Serve evidence (points): A 5499.0, B 3105.0; serve-point win A 58.4%, B 44.9%; Elo A 1636.5, B 1558.8; model uncertainty 0.0187
* Form inputs: days since last match A 15, B 8; matches on record A 407, B 91; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.009, surface_dev_loose -0.009, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Bellifemine / Maria Noce vs Agostini / Carboni -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06BELMARAGOCAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Agostini / Carboni (`KXITFDOUBLES-26OCT06BELMARAGOCAR-AGOCAR`) | 0.24 / 0.25 (1033) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bellifemine / Maria Noce (`KXITFDOUBLES-26OCT06BELMARAGOCAR-BELMAR`) | 0.74 / 0.76 (1) | 75.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Rocco Piatti vs OLUWASEUN PETER OGUNSAKIN -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-06T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211497:213595:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| OLUWASEUN PETER OGUNSAKIN (`KXITFMATCH-26OCT06PIAOGU-OGU`) | 0.01 / 0.03 (15436) | 2.0% | 22.8% | 21.9% | 36.8% [31.1%-43.8%] | -- | -- | -- | -- | PASS | +20.8 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rocco Piatti (`KXITFMATCH-26OCT06PIAOGU-PIA`) | 0.97 / 0.98 (948) | 97.5% | 77.2% | 78.1% | 63.2% [56.2%-68.9%] | -- | -- | -- | -- | PASS | -20.3 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2078.0, B 176.0; serve-point win A 62.7%, B 43.1%; Elo A 1267.0, B 1193.2; model uncertainty 0.0637
* Form inputs: days since last match A 148, B 218; matches on record A 64, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT06PIAOGU-OGU  (YES = OLUWASEUN PETER OGUNSAKIN)
Model: 23%
Kalshi: 2%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.045, surface_pool_high +0.024, surface_dev_loose +0.010, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Edas Butvilas vs Max Hans Rehberg -- ATP Challenger Villena R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 16:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-06T16:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208819:210220:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Edas Butvilas (`KXATPCHALLENGERMATCH-26OCT06BUTREH-BUT`) | 0.62 / 0.63 (52) | 62.5% | 55.6% | 51.5% | 53.5% [52.0%-56.4%] | 62.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Max Hans Rehberg (`KXATPCHALLENGERMATCH-26OCT06BUTREH-REH`) | 0.37 / 0.38 (5781) | 37.5% | 44.4% | 48.5% | 46.5% [43.6%-48.0%] | 37.5% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +6.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5096.0, B 3983.0; serve-point win A 65.3%, B 35.9%; Elo A 1670.1, B 1609.9; model uncertainty 0.0223
* Form inputs: days since last match A 8, B 29; matches on record A 267, B 254; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.010, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Stefan Latinovic / Mili Poljicak vs Enrique Carrascosa Diaz / Maxi Carrascosa Diaz -- ATP Challenger Villena R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 16:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-06T16:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06LATPOLCARCAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Enrique Carrascosa Diaz / Maxi Carrascosa Diaz (`KXATPCHALLENGERDOUBLES-26OCT06LATPOLCARCAR-CARCAR`) | 0.08 / 0.09 (17) | 8.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stefan Latinovic / Mili Poljicak (`KXATPCHALLENGERDOUBLES-26OCT06LATPOLCARCAR-LATPOL`) | 0.85 / 0.91 (22) | 88.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Oswaldo Alejandro Reyes Tirado vs Julio Cesar Porras -- M15 Pontevedra R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-06T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210132:213783:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julio Cesar Porras (`KXITFMATCH-26OCT06REYPOR-POR`) | 0.87 / 0.90 (6) | 88.5% | 86.8% | 89.0% | 84.2% [82.0%-87.5%] | -- | -- | -- | -- | PASS | -1.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oswaldo Alejandro Reyes Tirado (`KXITFMATCH-26OCT06REYPOR-REY`) | 0.08 / 0.13 (9) | 10.5% | 13.2% | 11.0% | 15.8% [12.5%-18.0%] | -- | -- | -- | -- | PASS | +2.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 411.0, B 1554.0; serve-point win A 52.2%, B 39.3%; Elo A 1216.0, B 1485.8; model uncertainty 0.0274
* Form inputs: days since last match A 162, B 316; matches on record A 9, B 115; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.003, surface_pool_high +0.006, surface_dev_loose -0.007, surface_dev_tight +0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Martin Rodriguez Figueiredo vs Daniil Sarksian -- M15 Pontevedra R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-06T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212022:214195:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martin Rodriguez Figueiredo (`KXITFMATCH-26OCT06RODSAR-ROD`) | 0.06 / 0.14 (14) | 10.0% | 34.5% | 35.2% | 47.9% [44.8%-50.5%] | -- | -- | -- | -- | PASS | +24.6 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daniil Sarksian (`KXITFMATCH-26OCT06RODSAR-SAR`) | 0.91 / 0.94 (38) | 92.5% | 65.5% | 64.8% | 52.1% [49.5%-55.2%] | -- | -- | -- | -- | PASS | -27.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 45.0, B 2770.0; serve-point win A 56.1%, B 40.8%; Elo A 1265.5, B 1277.4; model uncertainty 0.0288
* Form inputs: days since last match A 365, B 127; matches on record A 1, B 72; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT06RODSAR-ROD  (YES = Martin Rodriguez Figueiredo)
Model: 35%
Kalshi: 10%
Gap: +25 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.031, surface_pool_high +0.026, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alex Barrena vs Matheus Pucinelli de Almeida -- ATP Challenger Antofagasta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 17:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T17:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207799:209875:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Barrena (`KXATPCHALLENGERMATCH-26OCT06BARPDA-BAR`) | 0.34 / 0.35 (4728) | 34.5% | 44.4% | 29.4% | 34.1% [31.7%-37.6%] | 42.8% | -- | 42.8% | MODEL_LONE_OUTLIER | PASS | +9.9 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Matheus Pucinelli de Almeida (`KXATPCHALLENGERMATCH-26OCT06BARPDA-PDA`) | 0.65 / 0.66 (21540) | 65.5% | 55.6% | 70.6% | 65.9% [62.4%-68.3%] | 57.2% | -- | 57.2% | MODEL_LONE_OUTLIER | SHADOW_BET | -9.9 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 4939.0, B 4881.0; serve-point win A 56.1%, B 42.9%; Elo A 1643.5, B 1635.3; model uncertainty 0.0294
* Form inputs: days since last match A 15, B 8; matches on record A 336, B 410; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Franco Roncadelli vs Marcelo Tomas Barrios Vera -- ATP Challenger Antofagasta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 17:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-06T17:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06RONBAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcelo Tomas Barrios Vera (`KXATPCHALLENGERMATCH-26OCT06RONBAR-BAR`) | 0.84 / 0.85 (13942) | 84.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Franco Roncadelli (`KXATPCHALLENGERMATCH-26OCT06RONBAR-RON`) | 0.15 / 0.16 (24078) | 15.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Juan Bautista Torres vs Pedro Boscardin Dias -- ATP Challenger Antofagasta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 17:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T17:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208046:208913:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pedro Boscardin Dias (`KXATPCHALLENGERMATCH-26OCT06TORBOS-BOS`) | 0.47 / 0.48 (11396) | 47.5% | 36.7% | 22.9% | 27.5% [24.5%-35.1%] | 49.0% | 47.7% | 48.3% | MODEL_LONE_OUTLIER | PASS | -10.8 pp | REVIEW | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Juan Bautista Torres (`KXATPCHALLENGERMATCH-26OCT06TORBOS-TOR`) | 0.52 / 0.53 (600) | 52.5% | 63.3% | 77.1% | 72.5% [64.9%-75.5%] | 51.0% | 52.4% | 51.7% | MODEL_LONE_OUTLIER | PASS | +10.8 pp | REVIEW | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5511.0, B 4818.0; serve-point win A 56.8%, B 45.7%; Elo A 1622.4, B 1587.3; model uncertainty 0.0529
* Form inputs: days since last match A 148, B 8; matches on record A 369, B 345; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high +0.000, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Marco Cecchinato vs Olle Wallin -- ATP Challenger Braga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 17:15Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T17:15:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106065:209167:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marco Cecchinato (`KXATPCHALLENGERMATCH-26OCT06CECWAL-CEC`) | 0.70 / 0.71 (1455) | 70.5% | 75.7% | 74.0% | 76.4% [73.6%-78.0%] | 68.8% | -- | 68.8% | MODEL_LONE_OUTLIER | PASS | +5.2 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Olle Wallin (`KXATPCHALLENGERMATCH-26OCT06CECWAL-WAL`) | 0.29 / 0.30 (292) | 29.5% | 24.3% | 26.0% | 23.6% [22.1%-26.4%] | 31.2% | -- | 31.2% | MODEL_LONE_OUTLIER | PASS | -5.2 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5924.0, B 3594.0; serve-point win A 65.5%, B 40.0%; Elo A 1699.6, B 1449.6; model uncertainty 0.0216
* Form inputs: days since last match A 22, B 8; matches on record A 991, B 161; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.024, surface_pool_high +0.015, surface_dev_loose +0.004, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Avataneo / Roots vs Alekseeva / Salvadori -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06AVAROOALESAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alekseeva / Salvadori (`KXITFWDOUBLES-26OCT06AVAROOALESAL-ALESAL`) | 0.23 / 0.25 (94) | 24.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Avataneo / Roots (`KXITFWDOUBLES-26OCT06AVAROOALESAL-AVAROO`) | 0.72 / 0.76 (329) | 74.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Esther Lopez Alcaraz vs Caijsa Wilda Hennemann -- W35 Seville R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-06T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215701:216385:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Caijsa Wilda Hennemann (`KXITFWMATCH-26OCT06LOPHEN-HEN`) | 0.73 / 0.74 (2025) | 73.5% | 95.0% | 92.6% | 89.6% [88.4%-90.8%] | -- | -- | -- | -- | PASS | +21.4 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Esther Lopez Alcaraz (`KXITFWMATCH-26OCT06LOPHEN-LOP`) | 0.26 / 0.27 (31383) | 26.5% | 5.1% | 7.4% | 10.4% [9.2%-11.6%] | -- | -- | -- | -- | PASS | -21.4 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 243.0, B 2350.0; serve-point win A 45.6%, B 42.2%; Elo A 1351.0, B 1713.9; model uncertainty 0.012
* Form inputs: days since last match A 351, B 162; matches on record A 101, B 313; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT06LOPHEN-HEN  (YES = Caijsa Wilda Hennemann)
Model: 95%
Kalshi: 74%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.013, surface_dev_loose -0.002, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dimitrov / Khorozov vs Chetverikov / Ilie Bogdan Petre -- M15 Burgas R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06DIMKHOCHEILI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chetverikov / Ilie Bogdan Petre (`KXITFDOUBLES-26OCT06DIMKHOCHEILI-CHEILI`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dimitrov / Khorozov (`KXITFDOUBLES-26OCT06DIMKHOCHEILI-DIMKHO`) | -- / 0.01 (59163) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE

## Lock / John Lock vs Nefve / Schachter -- M25 Kigali R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06LOCJOHNEFSCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lock / John Lock (`KXITFDOUBLES-26OCT06LOCJOHNEFSCH-LOCJOH`) | 0.24 / 0.63 (2) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nefve / Schachter (`KXITFDOUBLES-26OCT06LOCJOHNEFSCH-NEFSCH`) | 0.06 / 0.65 (2) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Shandarov / Shandarov vs Lazarov / Manukyan -- M15 Burgas R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06SHASHALAZMAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lazarov / Manukyan (`KXITFDOUBLES-26OCT06SHASHALAZMAN-LAZMAN`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Shandarov / Shandarov (`KXITFDOUBLES-26OCT06SHASHALAZMAN-SHASHA`) | -- / 0.01 (463) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE

## Pierre Antoine Tailleu vs Mae Malige -- M15+H Rodez R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210032:211898:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mae Malige (`KXITFMATCH-26OCT06TAIMAL-MAL`) | 0.77 / 0.78 (2803) | 77.5% | 83.3% | 67.4% | 79.0% [76.2%-81.5%] | -- | -- | -- | -- | WATCH | +5.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pierre Antoine Tailleu (`KXITFMATCH-26OCT06TAIMAL-TAI`) | 0.22 / 0.23 (10818) | 22.5% | 16.7% | 32.6% | 21.0% [18.5%-23.8%] | -- | -- | -- | -- | PASS | -5.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 742.0, B 3016.0; serve-point win A 52.8%, B 39.9%; Elo A 1146.8, B 1428.7; model uncertainty 0.0263
* Form inputs: days since last match A 190, B 29; matches on record A 41, B 148; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alvisi / Parentini Vallega Montebruno vs Gandolfi / Raggi -- W35 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06ALVPARGANRAG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alvisi / Parentini Vallega Montebruno (`KXITFWDOUBLES-26OCT06ALVPARGANRAG-ALVPAR`) | 0.44 / 0.46 (418) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gandolfi / Raggi (`KXITFWDOUBLES-26OCT06ALVPARGANRAG-GANRAG`) | 0.52 / 0.56 (788) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Brancaccio / Papamichail vs Longueville / Ogescu -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06BRAPAPLONOGE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brancaccio / Papamichail (`KXITFWDOUBLES-26OCT06BRAPAPLONOGE-BRAPAP`) | 0.65 / 0.66 (451) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Longueville / Ogescu (`KXITFWDOUBLES-26OCT06BRAPAPLONOGE-LONOGE`) | 0.34 / 0.38 (35) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Lazar / Shapatava vs Chastang Cooper / Toma -- W35 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06LAZSHACHATOM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chastang Cooper / Toma (`KXITFWDOUBLES-26OCT06LAZSHACHATOM-CHATOM`) | 0.10 / 0.12 (1) | 11.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lazar / Shapatava (`KXITFWDOUBLES-26OCT06LAZSHACHATOM-LAZSHA`) | 0.88 / 0.90 (787) | 89.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Rebecca Munk Mortensen vs Tian Jialin -- W35 Lagos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:241714:266448:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tian Jialin (`KXITFWMATCH-26OCT06MUNJIA-JIA`) | 0.33 / 0.34 (6260) | 33.5% | 49.1% | 56.4% | 48.4% [42.6%-51.6%] | -- | -- | -- | -- | PASS | +15.6 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rebecca Munk Mortensen (`KXITFWMATCH-26OCT06MUNJIA-MUN`) | 0.66 / 0.67 (1292) | 66.5% | 50.9% | 43.6% | 51.6% [48.4%-57.4%] | -- | -- | -- | -- | PASS | -15.6 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1668.0, B 1919.0; serve-point win A 54.2%, B 46.0%; Elo A 1478.6, B 1402.4; model uncertainty 0.0451
* Form inputs: days since last match A 162, B 8; matches on record A 166, B 106; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT06MUNJIA-JIA  (YES = Tian Jialin)
Model: 49%
Kalshi: 34%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bobichon / Car vs Burdet / Luca Tanner -- M15 Pontevedra R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06BOBCARBURLUC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bobichon / Car (`KXITFDOUBLES-26OCT06BOBCARBURLUC-BOBCAR`) | 0.20 / 0.69 (1) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Burdet / Luca Tanner (`KXITFDOUBLES-26OCT06BOBCARBURLUC-BURLUC`) | 0.02 / 0.79 (1) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Eichenseher / Thurner vs Galea / Munoz Fuster -- M15 Pontevedra R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06EICTHUGALMUN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eichenseher / Thurner (`KXITFDOUBLES-26OCT06EICTHUGALMUN-EICTHU`) | 0.08 / 0.85 (3) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Galea / Munoz Fuster (`KXITFDOUBLES-26OCT06EICTHUGALMUN-GALMUN`) | 0.04 / 0.69 (1) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alejandro Garcia Carbajal vs Tomas Curras Abasolo -- M15 Pontevedra R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-06T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200330:202307:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomas Curras Abasolo (`KXITFMATCH-26OCT06GARCUR-CUR`) | 0.21 / 0.58 (1) | 39.5% | 59.7% | 64.8% | 61.4% [60.3%-62.8%] | -- | -- | -- | -- | PASS | +20.2 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Alejandro Garcia Carbajal (`KXITFMATCH-26OCT06GARCUR-GAR`) | 0.37 / 0.56 (1) | 46.5% | 40.3% | 35.2% | 38.6% [37.2%-39.7%] | -- | -- | -- | -- | PASS | -6.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 204.0, B 2566.0; serve-point win A 57.3%, B 40.8%; Elo A 1274.7, B 1354.0; model uncertainty 0.0125
* Form inputs: days since last match A 232, B 127; matches on record A 63, B 136; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT06GARCUR-CUR  (YES = Tomas Curras Abasolo)
Model: 60%
Kalshi: 40%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.010, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gniewkowska / Tahiri vs Lemaitre / Tran -- W35 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06GNITAHLEMTRA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gniewkowska / Tahiri (`KXITFWDOUBLES-26OCT06GNITAHLEMTRA-GNITAH`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lemaitre / Tran (`KXITFWDOUBLES-26OCT06GNITAHLEMTRA-LEMTRA`) | -- / 0.01 (60100) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE

## Kuzmova / Pawlikowska vs Nakashima / Zhu -- W35 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06KUZPAWNAKZHU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kuzmova / Pawlikowska (`KXITFWDOUBLES-26OCT06KUZPAWNAKZHU-KUZPAW`) | 0.62 / 0.71 (281) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nakashima / Zhu (`KXITFWDOUBLES-26OCT06KUZPAWNAKZHU-NAKZHU`) | 0.23 / 0.38 (1) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Damir Dzumhur vs Georgii Kravchenko -- ATP Challenger Villena R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-06T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106000:206662:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Damir Dzumhur (`KXATPCHALLENGERMATCH-26OCT06DZUKRA-DZU`) | 0.66 / 0.67 (4230) | 66.5% | 64.1% | 38.3% | 51.5% [44.8%-62.2%] | 65.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Georgii Kravchenko (`KXATPCHALLENGERMATCH-26OCT06DZUKRA-KRA`) | 0.33 / 0.34 (1588) | 33.5% | 35.9% | 61.7% | 48.4% [37.8%-55.2%] | 34.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5398.0, B 3595.0; serve-point win A 61.2%, B 41.5%; Elo A 1691.4, B 1452.9; model uncertainty 0.0867
* Form inputs: days since last match A 8, B 16; matches on record A 1076, B 397; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.015, surface_dev_loose -0.021, surface_dev_tight +0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

## Felipe Meligeni Alves vs Juan Pablo Varillas -- ATP Challenger Antofagasta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:122669:200335:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felipe Meligeni Alves (`KXATPCHALLENGERMATCH-26OCT06MELVAR-MEL`) | 0.46 / 0.47 (10279) | 46.5% | 44.1% | 38.0% | 41.0% [39.5%-42.5%] | -- | 45.9% | 45.9% | MODEL_LONE_OUTLIER | PASS | -2.4 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Juan Pablo Varillas (`KXATPCHALLENGERMATCH-26OCT06MELVAR-VAR`) | 0.53 / 0.54 (3521) | 53.5% | 55.9% | 62.0% | 59.0% [57.5%-60.5%] | -- | 53.9% | 53.9% | MODEL_LONE_OUTLIER | WATCH | +2.4 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3001.0, B 5280.0; serve-point win A 61.8%, B 37.0%; Elo A 1670.3, B 1694.3; model uncertainty 0.0148
* Form inputs: days since last match A 8, B 15; matches on record A 524, B 792; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER

## Bernardo Munk Mesa vs Joao Lucas Reis Da Silva -- ATP Challenger Antofagasta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206307:212827:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bernardo Munk Mesa (`KXATPCHALLENGERMATCH-26OCT06MUNREI-MUN`) | 0.16 / 0.17 (7645) | 16.5% | 12.6% | 18.7% | 14.9% [14.3%-16.1%] | 17.9% | 15.6% | 16.8% | MARKETS_AGREE | PASS | -3.9 pp | NORMAL | FRESH | D / POOR | ALL_AGREE | VERIFIED |
| Joao Lucas Reis Da Silva (`KXATPCHALLENGERMATCH-26OCT06MUNREI-REI`) | 0.84 / 0.85 (11208) | 84.5% | 87.4% | 81.3% | 85.1% [83.9%-85.7%] | 82.1% | 84.1% | 83.1% | MARKETS_AGREE | PASS | +2.9 pp | NORMAL | FRESH | D / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 814.0, B 4857.0; serve-point win A 57.5%, B 33.5%; Elo A 1302.0, B 1630.6; model uncertainty 0.0089
* Form inputs: days since last match A 274, B 8; matches on record A 18, B 476; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.003, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER

## Juan Carlos Prado Angelo vs Joao Eduardo Schiessl -- ATP Challenger Antofagasta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210178:210214:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Carlos Prado Angelo (`KXATPCHALLENGERMATCH-26OCT06PRASCH-PRA`) | 0.81 / 0.82 (11714) | 81.5% | 72.7% | 59.8% | 66.2% [63.7%-68.5%] | 79.2% | 80.5% | -- | INSUFFICIENT_INPUTS | PASS | -8.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Joao Eduardo Schiessl (`KXATPCHALLENGERMATCH-26OCT06PRASCH-SCH`) | 0.18 / 0.19 (1350) | 18.5% | 27.3% | 40.2% | 33.8% [31.5%-36.2%] | 20.8% | 19.8% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +8.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4633.0, B 2313.0; serve-point win A 61.2%, B 43.4%; Elo A 1653.8, B 1464.6; model uncertainty 0.0238
* Form inputs: days since last match A 8, B 8; matches on record A 250, B 181; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.005, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

## Oriol Roca Batalla vs Francesco Passaro -- ATP Challenger Palermo R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106177:208859:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesco Passaro (`KXATPCHALLENGERMATCH-26OCT06ROCPAS-PAS`) | 0.61 / 0.62 (1112) | 61.5% | 61.7% | 41.1% | 47.0% [44.6%-52.0%] | -- | 59.4% | -- | INSUFFICIENT_INPUTS | PASS | +0.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oriol Roca Batalla (`KXATPCHALLENGERMATCH-26OCT06ROCPAS-ROC`) | 0.38 / 0.39 (1048) | 38.5% | 38.3% | 58.9% | 53.0% [48.0%-55.4%] | -- | 40.7% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | -0.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5560.0, B 4611.0; serve-point win A 63.0%, B 34.6%; Elo A 1624.9, B 1743.2; model uncertainty 0.0372
* Form inputs: days since last match A 15, B 15; matches on record A 1048, B 376; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER

## Brown / Nozdrachova vs Agra Amorim / Ivantsiv -- W35 Lagos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06BRONOZAGRIVA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Agra Amorim / Ivantsiv (`KXITFWDOUBLES-26OCT06BRONOZAGRIVA-AGRIVA`) | 0.63 / 0.74 (1) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Brown / Nozdrachova (`KXITFWDOUBLES-26OCT06BRONOZAGRIVA-BRONOZ`) | 0.26 / 0.37 (52) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Zoe Doldan vs Maria Florencia Urrutia -- W15 Cipolletti R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220447:269847:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zoe Doldan (`KXITFWMATCH-26OCT06DOLURR-DOL`) | 0.04 / 0.06 (14) | 5.0% | 5.5% | 30.0% | 18.8% [18.8%-18.8%] | -- | -- | -- | -- | PASS | +0.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Florencia Urrutia (`KXITFWMATCH-26OCT06DOLURR-URR`) | 0.92 / 0.96 (107) | 94.0% | 94.5% | 70.0% | 81.2% [81.2%-81.2%] | -- | -- | -- | -- | PASS | +0.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 2454.0; serve-point win A 46.2%, B 41.8%; Elo A 1244.4, B 1501.0; model uncertainty 0.0001
* Form inputs: days since last match A 715, B 162; matches on record A 1, B 106; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Isakova / Xu vs Ordonez Anduiza / Patier -- W35 Lagos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06ISAXUXORDPAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isakova / Xu (`KXITFWDOUBLES-26OCT06ISAXUXORDPAT-ISAXUX`) | 0.02 / 0.90 (50) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ordonez Anduiza / Patier (`KXITFWDOUBLES-26OCT06ISAXUXORDPAT-ORDPAT`) | -- / 0.90 (50) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Ana Sofia Sanchez vs Milagros Cristobal -- W15 Cipolletti R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:204419:264197:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Milagros Cristobal (`KXITFWMATCH-26OCT06SANCRI-CRI`) | 0.01 / 0.02 (25275) | 1.5% | 0.7% | 14.1% | 6.0% [5.7%-6.3%] | -- | -- | -- | -- | PASS | -0.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ana Sofia Sanchez (`KXITFWMATCH-26OCT06SANCRI-SAN`) | 0.98 / 0.99 (5476) | 98.5% | 99.3% | 85.9% | 94.0% [93.7%-94.3%] | -- | -- | -- | -- | PASS | +0.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3191.0, B 71.0; serve-point win A 58.7%, B 59.9%; Elo A 1620.5, B 1133.4; model uncertainty 0.0031
* Form inputs: days since last match A 24, B 197; matches on record A 854, B 8; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carola Celina Sosa vs Sofia Meabe -- W15 Cipolletti R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260707:266446:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Meabe (`KXITFWMATCH-26OCT06SOSMEA-MEA`) | 0.91 / 0.95 (120) | 93.0% | 87.1% | 64.1% | 80.1% [78.5%-81.8%] | -- | -- | -- | -- | PASS | -5.9 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carola Celina Sosa (`KXITFWMATCH-26OCT06SOSMEA-SOS`) | 0.05 / 0.08 (18) | 6.5% | 12.9% | 35.9% | 19.9% [18.2%-21.4%] | -- | -- | -- | -- | PASS | +6.4 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 230.0, B 235.0; serve-point win A 48.4%, B 43.1%; Elo A 1073.9, B 1335.6; model uncertainty 0.0164
* Form inputs: days since last match A 260, B 260; matches on record A 35, B 18; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Agustin Pernas / Schlossmann vs Ali Abibsi / Smiej -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06AGUSCHALISMI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Agustin Pernas / Schlossmann (`KXITFDOUBLES-26OCT06AGUSCHALISMI-AGUSCH`) | 0.16 / 0.78 (1) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ali Abibsi / Smiej (`KXITFDOUBLES-26OCT06AGUSCHALISMI-ALISMI`) | 0.03 / 0.69 (1) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## De Carvalho / Echeverria vs Begg-Smith / Frydrych -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06DECECHBEGFRY:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Begg-Smith / Frydrych (`KXITFDOUBLES-26OCT06DECECHBEGFRY-BEGFRY`) | 0.02 / 0.87 (75) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| De Carvalho / Echeverria (`KXITFDOUBLES-26OCT06DECECHBEGFRY-DECECH`) | 0.14 / 0.86 (99) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## De Felipe Garcia / Nirundorn vs Freire Da Silva / Picard -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06DEFNIRFREPIC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| De Felipe Garcia / Nirundorn (`KXITFDOUBLES-26OCT06DEFNIRFREPIC-DEFNIR`) | -- / 0.02 (412) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Freire Da Silva / Picard (`KXITFDOUBLES-26OCT06DEFNIRFREPIC-FREPIC`) | 0.94 / 0.99 (620) | 96.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE

## Sarah Iliev vs Hanna Bougouffa -- W35 Villeneuve d'Ascq R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-06T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:225858:230121:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hanna Bougouffa (`KXITFWMATCH-26OCT06ILIBOU-BOU`) | 0.10 / 0.11 (6174) | 10.5% | 13.0% | 37.9% | 25.5% [22.7%-27.3%] | 20.6% | -- | 20.6% | KALSHI_LONE_OUTLIER | PASS | +2.5 pp | NORMAL | FRESH | D / POOR | EXTERNAL_OUTLIER | VERIFIED |
| Sarah Iliev (`KXITFWMATCH-26OCT06ILIBOU-ILI`) | 0.89 / 0.90 (7920) | 89.5% | 87.0% | 62.1% | 74.5% [72.7%-77.3%] | 79.4% | -- | 79.4% | MODEL_LONE_OUTLIER | PASS | -2.5 pp | NORMAL | FRESH | D / POOR | EXTERNAL_OUTLIER | VERIFIED |

* Serve evidence (points): A 1783.0, B 245.0; serve-point win A 55.9%, B 52.5%; Elo A 1486.6, B 1280.0; model uncertainty 0.0231
* Form inputs: days since last match A 176, B 435; matches on record A 157, B 134; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.009, surface_dev_loose +0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Francoise Abanda vs Jane Dunyon -- W50 Lexington SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-06T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211796:266672:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francoise Abanda (`KXITFWMATCH-26OCT06ABADUN-ABA`) | 0.91 / 0.92 (4950) | 91.5% | 95.4% | 78.2% | 89.1% [88.1%-90.9%] | -- | -- | -- | -- | PASS | +3.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jane Dunyon (`KXITFWMATCH-26OCT06ABADUN-DUN`) | 0.08 / 0.09 (12353) | 8.5% | 4.6% | 21.8% | 10.9% [9.1%-11.9%] | -- | -- | -- | -- | PASS | -3.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 902.0, B 200.0; serve-point win A 57.8%, B 54.8%; Elo A 1618.9, B 1231.1; model uncertainty 0.0141
* Form inputs: days since last match A 204, B 456; matches on record A 323, B 21; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.008, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leyla Fiorella Britez Risso vs Maria Sofia Madrid Rocca -- W15 Cipolletti R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222513:237458:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leyla Fiorella Britez Risso (`KXITFWMATCH-26OCT06BRIMAD-BRI`) | 0.91 / 0.94 (96) | 92.5% | 89.0% | 28.2% | 76.5% [76.5%-76.5%] | -- | -- | -- | -- | PASS | -3.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Maria Sofia Madrid Rocca (`KXITFWMATCH-26OCT06BRIMAD-MAD`) | 0.08 / 0.09 (68) | 8.5% | 11.0% | 71.8% | 23.5% [23.5%-23.5%] | -- | -- | -- | -- | PASS | +2.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 257.0, B 0.0; serve-point win A 57.7%, B 51.5%; Elo A 1409.9, B 1206.8; model uncertainty 0.0003
* Form inputs: days since last match A 848, B 1205; matches on record A 44, B 25; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Helena Buchwald vs Megan Heuser -- W50 Lexington SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-06T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259887:260962:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Helena Buchwald (`KXITFWMATCH-26OCT06BUCHEU-BUC`) | 0.94 / 0.96 (1243) | 95.0% | 72.2% | 57.8% | 69.1% [66.7%-73.4%] | -- | -- | -- | -- | PASS | -22.8 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Megan Heuser (`KXITFWMATCH-26OCT06BUCHEU-HEU`) | 0.04 / 0.06 (9436) | 5.0% | 27.8% | 42.2% | 30.9% [26.6%-33.3%] | -- | -- | -- | -- | PASS | +22.8 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 320.0, B 459.0; serve-point win A 59.8%, B 44.7%; Elo A 1362.3, B 1202.2; model uncertainty 0.0337
* Form inputs: days since last match A 435, B 309; matches on record A 101, B 12; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT06BUCHEU-HEU  (YES = Megan Heuser)
Model: 28%
Kalshi: 5%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.019, surface_dev_loose -0.001, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ema Burgic vs Victoria Osuigwe -- W50 Lexington SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-06T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:202619:259820:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ema Burgic (`KXITFWMATCH-26OCT06BUROSU-BUR`) | 0.97 / 0.98 (5533) | 97.5% | 53.6% | 68.6% | 63.7% [58.5%-66.6%] | -- | -- | -- | -- | PASS | -43.9 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Victoria Osuigwe (`KXITFWMATCH-26OCT06BUROSU-OSU`) | 0.02 / 0.04 (4084) | 3.0% | 46.4% | 31.4% | 36.3% [33.4%-41.5%] | -- | -- | -- | -- | PASS | +43.4 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1373.0, B 749.0; serve-point win A 50.3%, B 50.3%; Elo A 1468.1, B 1395.6; model uncertainty 0.0407
* Form inputs: days since last match A 225, B 372; matches on record A 225, B 93; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT06BUROSU-OSU  (YES = Victoria Osuigwe)
Model: 46%
Kalshi: 3%
Gap: +43 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kovacs / Teker vs Boroczky / Lena Jaszfai -- W15 Székesfehérvár R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06KOVTEKBORLEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Boroczky / Lena Jaszfai (`KXITFWDOUBLES-26OCT06KOVTEKBORLEN-BORLEN`) | -- / 0.01 (573) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kovacs / Teker (`KXITFWDOUBLES-26OCT06KOVTEKBORLEN-KOVTEK`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE

## Florencia Belen Moron vs Justina Maria Gonzalez Daniele -- W15 Cipolletti R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260357:260708:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Justina Maria Gonzalez Daniele (`KXITFWMATCH-26OCT06MORGON-GON`) | 0.95 / 0.96 (5935) | 95.5% | 95.5% | 83.3% | 85.2% [84.6%-86.4%] | -- | -- | -- | -- | PASS | +0.0 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Florencia Belen Moron (`KXITFWMATCH-26OCT06MORGON-MOR`) | 0.04 / 0.05 (84) | 4.5% | 4.5% | 16.7% | 14.8% [13.6%-15.4%] | -- | -- | -- | -- | PASS | -0.0 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 144.0, B 2911.0; serve-point win A 45.2%, B 42.1%; Elo A 1107.5, B 1409.6; model uncertainty 0.0093
* Form inputs: days since last match A 260, B 162; matches on record A 77, B 154; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luciana Moyano vs Sofia Nahiara Nappi -- W15 Cipolletti R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06MOYNAP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luciana Moyano (`KXITFWMATCH-26OCT06MOYNAP-MOY`) | 0.96 / 0.98 (1758) | 97.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sofia Nahiara Nappi (`KXITFWMATCH-26OCT06MOYNAP-NAP`) | 0.02 / 0.05 (151) | 3.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexis Nguyen vs Eva Maria Ionescu -- W50 Lexington SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-06T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260490:260787:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eva Maria Ionescu (`KXITFWMATCH-26OCT06NGUION-ION`) | 0.02 / 0.03 (43983) | 2.5% | 59.8% | 52.7% | 57.4% [55.3%-60.6%] | -- | -- | -- | -- | PASS | +57.3 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexis Nguyen (`KXITFWMATCH-26OCT06NGUION-NGU`) | 0.97 / 0.98 (389) | 97.5% | 40.2% | 47.3% | 42.6% [39.5%-44.7%] | -- | -- | -- | -- | PASS | -57.3 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1010.0, B 1868.0; serve-point win A 52.5%, B 45.6%; Elo A 1406.5, B 1477.2; model uncertainty 0.0262
* Form inputs: days since last match A 162, B 86; matches on record A 69, B 92; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT06NGUION-ION  (YES = Eva Maria Ionescu)
Model: 60%
Kalshi: 2%
Gap: +57 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.016, surface_dev_loose +0.021, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gustavo Heide vs Maximo Zeitune -- ATP Challenger Antofagasta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 20:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T20:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208361:212784:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gustavo Heide (`KXATPCHALLENGERMATCH-26OCT06HEIZEI-HEI`) | 0.87 / 0.88 (2162) | 87.5% | 88.5% | 89.5% | 90.1% [89.1%-90.5%] | 85.5% | 87.8% | 86.6% | MARKETS_AGREE | SHADOW_BET | +1.0 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Maximo Zeitune (`KXATPCHALLENGERMATCH-26OCT06HEIZEI-ZEI`) | 0.12 / 0.13 (3591) | 12.5% | 11.5% | 10.5% | 9.9% [9.4%-10.9%] | 14.5% | 12.8% | 13.6% | MARKETS_AGREE | PASS | -1.0 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4582.0, B 2440.0; serve-point win A 68.2%, B 41.4%; Elo A 1779.8, B 1379.1; model uncertainty 0.0074
* Form inputs: days since last match A 8, B 29; matches on record A 312, B 72; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.004, surface_dev_tight -0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Guido Ivan Justo vs Francisco Comesana -- ATP Challenger Antofagasta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 20:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T20:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207681:207815:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisco Comesana (`KXATPCHALLENGERMATCH-26OCT06JUSCOM-COM`) | 0.68 / 0.69 (8390) | 68.5% | 59.2% | 43.3% | 50.5% [46.9%-55.6%] | 66.4% | 69.2% | 67.8% | MODEL_LONE_OUTLIER | PASS | -9.3 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Guido Ivan Justo (`KXATPCHALLENGERMATCH-26OCT06JUSCOM-JUS`) | 0.31 / 0.32 (1508) | 31.5% | 40.8% | 56.7% | 49.5% [44.4%-53.1%] | 33.6% | 32.0% | 32.8% | MODEL_LONE_OUTLIER | SHADOW_BET | +9.3 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5127.0, B 5153.0; serve-point win A 59.1%, B 39.1%; Elo A 1647.0, B 1818.6; model uncertainty 0.0437
* Form inputs: days since last match A 8, B 15; matches on record A 354, B 458; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.005, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Jose Pereira vs Lautaro Midon -- ATP Challenger Antofagasta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 20:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-06T20:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105700:210510:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lautaro Midon (`KXATPCHALLENGERMATCH-26OCT06PERMID-MID`) | 0.87 / 0.88 (2635) | 87.5% | 86.4% | 72.1% | 77.1% [75.5%-79.0%] | 84.4% | 87.4% | 87.4% | MODEL_LONE_OUTLIER | PASS | -1.1 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Jose Pereira (`KXATPCHALLENGERMATCH-26OCT06PERMID-PER`) | 0.12 / 0.13 (7869) | 12.5% | 13.6% | 27.9% | 22.9% [21.0%-24.5%] | 15.6% | 13.1% | 13.1% | MODEL_LONE_OUTLIER | SHADOW_BET | +1.1 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 2181.0, B 4637.0; serve-point win A 54.8%, B 36.7%; Elo A 1380.4, B 1663.5; model uncertainty 0.0177
* Form inputs: days since last match A 8, B 8; matches on record A 808, B 269; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.012, surface_pool_high -0.012, surface_dev_loose +0.000, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Barreira Bonzom / Casas Blasi vs Cardinaud / Jonio -- M15+H Rodez R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06BARCASCARJON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barreira Bonzom / Casas Blasi (`KXITFDOUBLES-26OCT06BARCASCARJON-BARCAS`) | 0.80 / 0.87 (10) | 83.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cardinaud / Jonio (`KXITFDOUBLES-26OCT06BARCASCARJON-CARJON`) | 0.13 / 0.14 (599) | 13.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Batsabaken / Ramiaramanana vs Hueller-Varga / LAUMON -- M15+H Rodez R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06BATRAMHUELAU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Batsabaken / Ramiaramanana (`KXITFDOUBLES-26OCT06BATRAMHUELAU-BATRAM`) | 0.08 / 0.12 (301) | 10.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hueller-Varga / LAUMON (`KXITFDOUBLES-26OCT06BATRAMHUELAU-HUELAU`) | 0.89 / 0.90 (803) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Matteo Covato vs Dakotah Bobo -- M15 Quito R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 20:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-06T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:149145:212860:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dakotah Bobo (`KXITFMATCH-26OCT06COVBOB-BOB`) | 0.53 / 0.54 (4119) | 53.5% | 61.8% | 61.5% | 57.1% [54.5%-59.1%] | 72.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matteo Covato (`KXITFMATCH-26OCT06COVBOB-COV`) | 0.46 / 0.47 (4640) | 46.5% | 38.2% | 38.5% | 42.9% [40.9%-45.5%] | 28.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2350.0, B 547.0; serve-point win A 60.9%, B 36.7%; Elo A 1155.8, B 1193.4; model uncertainty 0.0225
* Form inputs: days since last match A 127, B 134; matches on record A 76, B 15; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.025, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dando / Poupinel vs Eldin / Lapalu -- M15+H Rodez R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06DANPOUELDLAP:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dando / Poupinel (`KXITFDOUBLES-26OCT06DANPOUELDLAP-DANPOU`) | 0.02 / 0.93 (3) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eldin / Lapalu (`KXITFDOUBLES-26OCT06DANPOUELDLAP-ELDLAP`) | 0.02 / 0.92 (1) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Juan Sebastian Dominguez Collado vs Mwendwa Mbithi -- M15 Quito R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 20:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06DOMMBI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Sebastian Dominguez Collado (`KXITFMATCH-26OCT06DOMMBI-DOM`) | 0.08 / 0.09 (3059) | 8.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mwendwa Mbithi (`KXITFMATCH-26OCT06DOMMBI-MBI`) | 0.91 / 0.92 (214) | 91.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ivan Dreycopp vs Juan Sebastian Gomez -- M15 Quito R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 20:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-06T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105944:210403:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ivan Dreycopp (`KXITFMATCH-26OCT06DREGOM-DRE`) | 0.47 / 0.48 (58) | 47.5% | 26.1% | 28.9% | 26.3% [24.5%-27.3%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -21.4 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Juan Sebastian Gomez (`KXITFMATCH-26OCT06DREGOM-GOM`) | 0.50 / 0.51 (183) | 50.5% | 73.9% | 71.0% | 73.7% [72.7%-75.5%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +23.4 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 293.0, B 2089.0; serve-point win A 54.2%, B 41.0%; Elo A 1189.4, B 1368.1; model uncertainty 0.0136
* Form inputs: days since last match A 225, B 92; matches on record A 10, B 492; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT06DREGOM-GOM  (YES = Juan Sebastian Gomez)
Model: 74%
Kalshi: 50%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.009, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juan Sebastian Osorio vs Tadeo Meneo -- M15 Quito R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 20:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-06T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126581:212745:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tadeo Meneo (`KXITFMATCH-26OCT06OSOMEN-MEN`) | 0.06 / 0.09 (219) | 7.5% | 21.6% | 9.7% | 19.5% [14.0%-27.9%] | 10.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +14.1 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Juan Sebastian Osorio (`KXITFMATCH-26OCT06OSOMEN-OSO`) | 0.91 / 0.94 (151) | 92.5% | 78.4% | 90.3% | 80.5% [72.1%-86.1%] | 89.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -14.1 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2333.0, B 1218.0; serve-point win A 65.7%, B 40.5%; Elo A 1287.4, B 1147.3; model uncertainty 0.0699
* Form inputs: days since last match A 92, B 148; matches on record A 140, B 39; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.011, surface_dev_loose +0.013, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bella Bergqvist Larsson vs Briley Rhoden -- W50 Lexington SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06BERRHO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bella Bergqvist Larsson (`KXITFWMATCH-26OCT06BERRHO-BER`) | 0.61 / 0.78 (97) | 69.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Briley Rhoden (`KXITFWMATCH-26OCT06BERRHO-RHO`) | 0.10 / 0.25 (6) | 17.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Misa Malkin vs Astra Sharma -- W50 Lexington SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-06T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206292:222509:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Misa Malkin (`KXITFWMATCH-26OCT06MALSHA-MAL`) | 0.07 / 0.11 (1) | 9.0% | 10.0% | 35.0% | 22.8% [16.9%-27.0%] | -- | -- | -- | -- | WATCH | +1.0 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Astra Sharma (`KXITFWMATCH-26OCT06MALSHA-SHA`) | 0.91 / 0.92 (202) | 91.5% | 90.0% | 65.0% | 77.2% [73.0%-83.1%] | -- | -- | -- | -- | PASS | -1.5 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 892.0, B 2800.0; serve-point win A 49.9%, B 40.4%; Elo A 1364.5, B 1638.0; model uncertainty 0.0505
* Form inputs: days since last match A 211, B 20; matches on record A 39, B 423; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.025, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Isabella Marton vs McKenna Schaefbauer -- W50 Lexington SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-06T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:239103:260400:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isabella Marton (`KXITFWMATCH-26OCT06MARSCH-MAR`) | 0.29 / 0.41 (43) | 35.0% | 39.6% | 56.9% | 40.5% [37.9%-44.1%] | -- | -- | -- | -- | PASS | +4.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| McKenna Schaefbauer (`KXITFWMATCH-26OCT06MARSCH-SCH`) | 0.52 / 0.64 (42) | 58.0% | 60.4% | 43.1% | 59.5% [55.9%-62.1%] | -- | -- | -- | -- | PASS | +2.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1055.0, B 204.0; serve-point win A 52.3%, B 45.8%; Elo A 1223.0, B 1303.1; model uncertainty 0.0312
* Form inputs: days since last match A 66, B 421; matches on record A 32, B 53; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.037, surface_pool_high -0.026, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mia Slama vs Jensen Diianni -- W50 Lexington SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-06T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260693:270383:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jensen Diianni (`KXITFWMATCH-26OCT06SLADII-DII`) | 0.09 / 0.11 (10) | 10.0% | 26.3% | 24.7% | 37.9% [33.8%-39.4%] | -- | -- | -- | -- | PASS | +16.3 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mia Slama (`KXITFWMATCH-26OCT06SLADII-SLA`) | 0.87 / 0.89 (30) | 88.0% | 73.7% | 75.3% | 62.1% [60.6%-66.2%] | -- | -- | -- | -- | PASS | -14.3 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 435.0, B 180.0; serve-point win A 53.7%, B 51.0%; Elo A 1374.9, B 1299.6; model uncertainty 0.0279
* Form inputs: days since last match A 421, B 232; matches on record A 34, B 3; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT06SLADII-DII  (YES = Jensen Diianni)
Model: 26%
Kalshi: 10%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cesar Castro / Guadagno vs Luis Claro / Leon Mantilla -- M15 Quito R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06CESGUALUILEO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cesar Castro / Guadagno (`KXITFDOUBLES-26OCT06CESGUALUILEO-CESGUA`) | 0.02 / 0.95 (52) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luis Claro / Leon Mantilla (`KXITFDOUBLES-26OCT06CESGUALUILEO-LUILEO`) | 0.03 / 0.90 (100) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Felipe De Dios vs Darwin Andres Macias Elizalde -- M15 Quito R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06DEDMAC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felipe De Dios (`KXITFMATCH-26OCT06DEDMAC-DED`) | 0.88 / 0.92 (6) | 90.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Darwin Andres Macias Elizalde (`KXITFMATCH-26OCT06DEDMAC-MAC`) | 0.07 / 0.11 (6) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alex Hernandez vs Mario Andre Galarraga -- M15 Quito R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06HERGAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mario Andre Galarraga (`KXITFMATCH-26OCT06HERGAL-GAL`) | 0.05 / 0.07 (14) | 6.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alex Hernandez (`KXITFMATCH-26OCT06HERGAL-HER`) | 0.92 / 0.95 (27) | 93.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## BASEL / DELFINA VEGA GUDINO vs Luisana Mondati / Tejada -- W15 Cipolletti R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06BASDELLUITEJ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BASEL / DELFINA VEGA GUDINO (`KXITFWDOUBLES-26OCT06BASDELLUITEJ-BASDEL`) | 0.10 / 0.61 (1) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luisana Mondati / Tejada (`KXITFWDOUBLES-26OCT06BASDELLUITEJ-LUITEJ`) | -- / 0.80 (1) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Daniela Duarte / Lassaga vs Victoria Gobbi Monllau / Zornada -- W15 Cipolletti R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06DANLASVICZOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniela Duarte / Lassaga (`KXITFWDOUBLES-26OCT06DANLASVICZOR-DANLAS`) | 0.10 / 0.23 (55) | 16.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Victoria Gobbi Monllau / Zornada (`KXITFWDOUBLES-26OCT06DANLASVICZOR-VICZOR`) | 0.11 / 0.85 (5) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jay Clarke vs Gabriele Piraino -- ATP Challenger Palermo R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 21:45Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-06T21:45:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06CLAPIR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jay Clarke (`KXATPCHALLENGERMATCH-26OCT06CLAPIR-CLA`) | 0.63 / 0.64 (2004) | 63.5% | -- | -- | -- [-----] | 62.5% | 64.6% | 63.5% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gabriele Piraino (`KXATPCHALLENGERMATCH-26OCT06CLAPIR-PIR`) | 0.36 / 0.37 (14684) | 36.5% | -- | -- | -- [-----] | 37.5% | 36.8% | 37.2% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Daniel Jade vs Kenny De Schepper -- M15+H Rodez R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:104932:212711:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kenny De Schepper (`KXITFMATCH-26OCT06JADDES-DES`) | 0.43 / 0.46 (48) | 44.5% | 50.6% | 64.3% | 68.5% [67.2%-69.9%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.1 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daniel Jade (`KXITFMATCH-26OCT06JADDES-JAD`) | 0.54 / 0.57 (4697) | 55.5% | 49.4% | 35.6% | 31.5% [30.1%-32.8%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.1 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1136.0, B 3218.0; serve-point win A 62.2%, B 37.7%; Elo A 1353.1, B 1515.7; model uncertainty 0.0136
* Form inputs: days since last match A 15, B 134; matches on record A 31, B 980; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Clara Vlasselaer vs Daphnee Mpetshi Perricard -- W35 Villeneuve d'Ascq R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-06T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221003:263995:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daphnee Mpetshi Perricard (`KXITFWMATCH-26OCT06VLAMPE-MPE`) | 0.40 / 0.42 (47) | 41.0% | 31.1% | 29.3% | 29.3% [25.6%-33.7%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Clara Vlasselaer (`KXITFWMATCH-26OCT06VLAMPE-VLA`) | 0.60 / 0.61 (4884) | 60.5% | 68.9% | 70.7% | 70.7% [66.3%-74.5%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.4 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1490.0, B 1272.0; serve-point win A 61.6%, B 42.2%; Elo A 1481.5, B 1322.9; model uncertainty 0.0407
* Form inputs: days since last match A 162, B 140; matches on record A 332, B 45; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.026, surface_dev_loose +0.003, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Linea Bajraliu vs Lea Ma -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-06T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221220:259996:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Linea Bajraliu (`KXITFWMATCH-26OCT06BAJMAX-BAJ`) | 0.26 / 0.27 (2702) | 26.5% | 29.2% | 55.1% | 41.3% [29.1%-47.9%] | 26.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +2.7 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lea Ma (`KXITFWMATCH-26OCT06BAJMAX-MAX`) | 0.73 / 0.74 (99) | 73.5% | 70.8% | 44.9% | 58.7% [52.1%-70.9%] | 73.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.7 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1577.0, B 2727.0; serve-point win A 57.7%, B 38.1%; Elo A 1450.1, B 1612.4; model uncertainty 0.0942
* Form inputs: days since last match A 91, B 24; matches on record A 46, B 166; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.015, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kylie Collins vs Hina Inoue -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-06T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220891:222080:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kylie Collins (`KXITFWMATCH-26OCT06COLINO-COL`) | 0.58 / 0.59 (62) | 58.5% | 29.9% | 39.9% | 32.9% [30.0%-35.4%] | 59.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -28.6 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hina Inoue (`KXITFWMATCH-26OCT06COLINO-INO`) | 0.39 / 0.41 (101) | 40.0% | 70.1% | 60.1% | 67.1% [64.6%-70.0%] | 40.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +30.1 pp | EXTREME (DATA_WARNING) | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2145.0, B 2804.0; serve-point win A 50.2%, B 45.9%; Elo A 1438.6, B 1638.6; model uncertainty 0.0266
* Form inputs: days since last match A 15, B 169; matches on record A 126, B 325; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT06COLINO-INO  (YES = Hina Inoue)
Model: 70%
Kalshi: 40%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.014, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nahiara Nappi / Rondinoni vs Cristobal / Pajello -- W15 Cipolletti R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06NAHRONCRIPAJ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cristobal / Pajello (`KXITFWDOUBLES-26OCT06NAHRONCRIPAJ-CRIPAJ`) | 0.19 / 0.82 (67) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nahiara Nappi / Rondinoni (`KXITFWDOUBLES-26OCT06NAHRONCRIPAJ-NAHRON`) | 0.06 / 0.89 (400) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Malaika Rapolu vs Dalayna Hewitt -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-06T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220550:222837:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dalayna Hewitt (`KXITFWMATCH-26OCT06RAPHEW-HEW`) | 0.14 / 0.15 (4346) | 14.5% | 23.6% | 35.8% | 33.4% [31.7%-34.9%] | 17.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +9.1 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Malaika Rapolu (`KXITFWMATCH-26OCT06RAPHEW-RAP`) | 0.85 / 0.86 (506) | 85.5% | 76.4% | 64.2% | 66.6% [65.1%-68.3%] | 82.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.1 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1761.0, B 918.0; serve-point win A 61.9%, B 43.6%; Elo A 1619.4, B 1482.6; model uncertainty 0.016
* Form inputs: days since last match A 19, B 176; matches on record A 134, B 233; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.005, surface_dev_loose -0.001, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arantxa Rus vs Ena Koike -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-06T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:201551:260514:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ena Koike (`KXITFWMATCH-26OCT06RUSKOI-KOI`) | 0.38 / 0.40 (7) | 39.0% | 46.6% | 49.0% | 40.7% [31.8%-44.8%] | 39.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Arantxa Rus (`KXITFWMATCH-26OCT06RUSKOI-RUS`) | 0.61 / 0.62 (6437) | 61.5% | 53.4% | 51.0% | 59.3% [55.2%-68.2%] | 60.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4567.0, B 1979.0; serve-point win A 58.8%, B 41.8%; Elo A 1695.6, B 1551.5; model uncertainty 0.0653
* Form inputs: days since last match A 15, B 24; matches on record A 1205, B 119; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose -0.011, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Sanchez / Florencia Urrutia vs Maria Maruca / Soto Neira -- W15 Cipolletti R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06SOFFLOMARSOT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Maruca / Soto Neira (`KXITFWDOUBLES-26OCT06SOFFLOMARSOT-MARSOT`) | 0.07 / 0.08 (27) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sofia Sanchez / Florencia Urrutia (`KXITFWDOUBLES-26OCT06SOFFLOMARSOT-SOFFLO`) | 0.88 / 0.93 (56) | 90.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Victor Bini vs Patricio Alvarado -- M15 Quito R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-06T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105419:212192:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Patricio Alvarado (`KXITFMATCH-26OCT06BINALV-ALV`) | 0.57 / 0.69 (12) | 63.0% | 42.5% | 38.3% | 43.3% [42.3%-44.9%] | -- | -- | -- | -- | PASS | -20.4 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Victor Bini (`KXITFMATCH-26OCT06BINALV-BIN`) | 0.26 / 0.42 (1) | 34.0% | 57.5% | 61.7% | 56.7% [55.1%-57.7%] | -- | -- | -- | -- | PASS | +23.4 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 499.0, B 867.0; serve-point win A 60.6%, B 40.8%; Elo A 1121.0, B 1087.4; model uncertainty 0.0129
* Form inputs: days since last match A 141, B 190; matches on record A 12, B 82; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT06BINALV-BIN  (YES = Victor Bini)
Model: 57%
Kalshi: 34%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.015, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Miles Clark vs Bernardo Casares -- M15 Quito R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-06T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106369:212473:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bernardo Casares (`KXITFMATCH-26OCT06CLACAS-CAS`) | 0.07 / 0.08 (3954) | 7.5% | 48.0% | 77.8% | 52.1% [51.0%-52.1%] | -- | -- | -- | -- | PASS | +40.5 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Miles Clark (`KXITFMATCH-26OCT06CLACAS-CLA`) | 0.89 / 0.94 (573) | 91.5% | 52.0% | 22.2% | 47.9% [47.9%-49.0%] | -- | -- | -- | -- | PASS | -39.5 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 336.0, B 0.0; serve-point win A 60.0%, B 40.4%; Elo A 1162.3, B 1173.9; model uncertainty 0.0052
* Form inputs: days since last match A 134, B 5090; matches on record A 14, B 12; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT06CLACAS-CAS  (YES = Bernardo Casares)
Model: 48%
Kalshi: 8%
Gap: +41 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dreycopp / Zeitune vs Sebastian Gomez / Urrea -- M15 Quito R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06DREZEISEBURR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dreycopp / Zeitune (`KXITFDOUBLES-26OCT06DREZEISEBURR-DREZEI`) | 0.15 / 0.74 (400) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sebastian Gomez / Urrea (`KXITFDOUBLES-26OCT06DREZEISEBURR-SEBURR`) | 0.08 / 0.72 (400) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jordi Leston / Perlov vs Covato / Voelzke -- M15 Quito R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06JORPERCOVVOE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Covato / Voelzke (`KXITFDOUBLES-26OCT06JORPERCOVVOE-COVVOE`) | 0.07 / 0.86 (100) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jordi Leston / Perlov (`KXITFDOUBLES-26OCT06JORPERCOVVOE-JORPER`) | 0.06 / 0.92 (1) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Baier / Corvalan Mitilli vs Doldan / Celina Sosa -- W15 Cipolletti R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06BAICORDOLCEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Baier / Corvalan Mitilli (`KXITFWDOUBLES-26OCT06BAICORDOLCEL-BAICOR`) | 0.07 / 0.86 (4) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Doldan / Celina Sosa (`KXITFWDOUBLES-26OCT06BAICORDOLCEL-DOLCEL`) | 0.08 / 0.88 (33) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Emma Kamper vs Shihomi Li Xuan Leong -- W35 Las Vegas NV R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-06T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:241715:263622:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emma Kamper (`KXITFWMATCH-26OCT06KAMLEO-KAM`) | 0.57 / 0.62 (56) | 59.5% | 52.3% | 59.5% | 51.1% [47.9%-54.8%] | -- | -- | -- | -- | PASS | -7.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Shihomi Li Xuan Leong (`KXITFWMATCH-26OCT06KAMLEO-LEO`) | 0.36 / 0.43 (3109) | 39.5% | 47.7% | 40.5% | 48.9% [45.2%-52.1%] | -- | -- | -- | -- | PASS | +8.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 510.0, B 969.0; serve-point win A 52.8%, B 47.6%; Elo A 1348.1, B 1363.2; model uncertainty 0.0347
* Form inputs: days since last match A 337, B 323; matches on record A 33, B 52; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Janae Preston vs Jenna DeFalco -- W35 Las Vegas NV R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-06T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221914:270320:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jenna DeFalco (`KXITFWMATCH-26OCT06PREDEF-DEF`) | 0.15 / 0.16 (867) | 15.5% | 35.7% | 21.8% | 42.0% [32.4%-52.1%] | -- | -- | -- | -- | PASS | +20.2 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Janae Preston (`KXITFWMATCH-26OCT06PREDEF-PRE`) | 0.81 / 0.83 (29) | 82.0% | 64.3% | 78.2% | 58.0% [47.9%-67.6%] | -- | -- | -- | -- | PASS | -17.7 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 739.0, B 1687.0; serve-point win A 52.3%, B 50.4%; Elo A 1423.8, B 1442.5; model uncertainty 0.0988
* Form inputs: days since last match A 42, B 162; matches on record A 14, B 247; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT06PREDEF-DEF  (YES = Jenna DeFalco)
Model: 36%
Kalshi: 16%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.016, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Duru Soke vs Anna Pushkareva -- W35 Las Vegas NV R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-06T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:224488:270315:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Pushkareva (`KXITFWMATCH-26OCT06SOKPUS-PUS`) | 0.65 / 0.67 (7) | 66.0% | 47.2% | 58.0% | 56.4% [56.4%-58.5%] | -- | -- | -- | -- | PASS | -18.8 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Duru Soke (`KXITFWMATCH-26OCT06SOKPUS-SOK`) | 0.33 / 0.35 (38) | 34.0% | 52.8% | 42.0% | 43.6% [41.5%-43.6%] | -- | -- | -- | -- | PASS | +18.8 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 316.0, B 666.0; serve-point win A 54.2%, B 46.3%; Elo A 1387.9, B 1433.8; model uncertainty 0.0105
* Form inputs: days since last match A 288, B 211; matches on record A 71, B 12; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT06SOKPUS-SOK  (YES = Duru Soke)
Model: 53%
Kalshi: 34%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.011, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amelie Van Impe vs Lexington Reed -- W35 Las Vegas NV R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-06T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:228909:239186:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lexington Reed (`KXITFWMATCH-26OCT06VANREE-REE`) | 0.26 / 0.28 (61) | 27.0% | 33.8% | 39.0% | 37.5% [33.5%-42.6%] | -- | -- | -- | -- | PASS | +6.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amelie Van Impe (`KXITFWMATCH-26OCT06VANREE-VAN`) | 0.73 / 0.74 (84) | 73.5% | 66.2% | 61.0% | 62.5% [57.4%-66.5%] | -- | -- | -- | -- | PASS | -7.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1949.0, B 144.0; serve-point win A 56.5%, B 46.6%; Elo A 1462.5, B 1375.5; model uncertainty 0.0458
* Form inputs: days since last match A 183, B 309; matches on record A 185, B 98; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.040, surface_pool_high -0.051, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Joaquin Aguilar Cardozo vs Nicolas Villalon Valdes -- ATP Challenger Antofagasta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-07T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06AGUVIL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joaquin Aguilar Cardozo (`KXATPCHALLENGERMATCH-26OCT06AGUVIL-AGU`) | 0.92 / 0.93 (5839) | 92.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nicolas Villalon Valdes (`KXATPCHALLENGERMATCH-26OCT06AGUVIL-VIL`) | 0.06 / 0.07 (513) | 6.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Bhatia / Belen Moron vs Ailin Larraya Guidi / Meabe -- W15 Cipolletti R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06BHABELAILMEA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ailin Larraya Guidi / Meabe (`KXITFWDOUBLES-26OCT06BHABELAILMEA-AILMEA`) | 0.64 / 0.87 (0) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bhatia / Belen Moron (`KXITFWDOUBLES-26OCT06BHABELAILMEA-BHABEL`) | 0.11 / 0.37 (0) | 24.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Fiorella Britez Risso / Kawano Cho vs Bulbarella / Rain -- W15 Cipolletti R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06FIOKAWBULRAI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bulbarella / Rain (`KXITFWDOUBLES-26OCT06FIOKAWBULRAI-BULRAI`) | 0.15 / 0.27 (0) | 21.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fiorella Britez Risso / Kawano Cho (`KXITFWDOUBLES-26OCT06FIOKAWBULRAI-FIOKAW`) | 0.71 / 0.83 (0) | 77.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ciara Harding vs Emma Ottavia Ghirardato -- W35 Las Vegas NV R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264270:270321:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emma Ottavia Ghirardato (`KXITFWMATCH-26OCT06HARGHI-GHI`) | 0.81 / 0.85 (29) | 83.0% | 67.3% | 44.7% | 52.1% [51.1%-52.1%] | -- | -- | -- | -- | PASS | -15.7 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ciara Harding (`KXITFWMATCH-26OCT06HARGHI-HAR`) | 0.15 / 0.19 (3153) | 17.0% | 32.7% | 55.3% | 47.9% [47.9%-48.9%] | -- | -- | -- | -- | PASS | +15.7 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 75.0, B 465.0; serve-point win A 54.9%, B 41.7%; Elo A 1262.2, B 1274.5; model uncertainty 0.0054
* Form inputs: days since last match A 344, B 344; matches on record A 1, B 36; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT06HARGHI-HAR  (YES = Ciara Harding)
Model: 33%
Kalshi: 17%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jurado / Sofia Madrid Rocca vs Mai / Markus -- W15 Cipolletti R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06JURSOFMAIMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jurado / Sofia Madrid Rocca (`KXITFWDOUBLES-26OCT06JURSOFMAIMAR-JURSOF`) | 0.06 / 0.90 (50) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mai / Markus (`KXITFWDOUBLES-26OCT06JURSOFMAIMAR-MAIMAR`) | 0.07 / 0.89 (100) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Chloe Noel vs Yekaterina Dmitrichenko -- W35 Las Vegas NV R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216243:223402:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yekaterina Dmitrichenko (`KXITFWMATCH-26OCT06NOEDMI-DMI`) | 0.66 / 0.67 (140) | 66.5% | 23.6% | 16.5% | 28.6% [23.2%-35.4%] | -- | -- | -- | -- | PASS | -42.9 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Chloe Noel (`KXITFWMATCH-26OCT06NOEDMI-NOE`) | 0.32 / 0.34 (69) | 33.0% | 76.4% | 83.5% | 71.4% [64.6%-76.8%] | -- | -- | -- | -- | PASS | +43.4 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1408.0, B 301.0; serve-point win A 60.1%, B 45.3%; Elo A 1430.5, B 1295.6; model uncertainty 0.0611
* Form inputs: days since last match A 435, B 421; matches on record A 178, B 134; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT06NOEDMI-NOE  (YES = Chloe Noel)
Model: 76%
Kalshi: 33%
Gap: +43 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.032, surface_pool_high +0.030, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anita Sahdiieva vs Francesca Mattioli -- W35 Las Vegas NV R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221370:260150:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesca Mattioli (`KXITFWMATCH-26OCT06SAHMAT-MAT`) | 0.48 / 0.52 (3923) | 50.0% | 54.7% | 37.4% | 56.4% [52.7%-61.6%] | -- | -- | -- | -- | PASS | +4.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anita Sahdiieva (`KXITFWMATCH-26OCT06SAHMAT-SAH`) | 0.49 / 0.52 (3991) | 50.5% | 45.3% | 62.6% | 43.6% [38.4%-47.3%] | -- | -- | -- | -- | PASS | -5.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1325.0, B 492.0; serve-point win A 53.0%, B 46.1%; Elo A 1390.1, B 1476.0; model uncertainty 0.0445
* Form inputs: days since last match A 162, B 428; matches on record A 111, B 28; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high +0.000, surface_dev_loose +0.011, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maria Sholokhova vs Krisha Mahendran -- W35 Las Vegas NV R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:233718:266645:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Krisha Mahendran (`KXITFWMATCH-26OCT06SHOMAH-MAH`) | 0.28 / 0.32 (17) | 30.0% | 43.0% | 10.5% | 32.0% [24.7%-43.6%] | -- | -- | -- | -- | PASS | +13.0 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Sholokhova (`KXITFWMATCH-26OCT06SHOMAH-SHO`) | 0.68 / 0.72 (72) | 70.0% | 57.0% | 89.5% | 68.0% [56.4%-75.3%] | -- | -- | -- | -- | PASS | -13.0 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1181.0, B 456.0; serve-point win A 53.9%, B 47.5%; Elo A 1517.5, B 1450.9; model uncertainty 0.0944
* Form inputs: days since last match A 435, B 365; matches on record A 85, B 13; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.024, surface_dev_loose +0.009, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Baker / Clarke vs Evans / Frey -- W50 Lexington SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 00:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06BAKCLAEVAFRE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Baker / Clarke (`KXITFWDOUBLES-26OCT06BAKCLAEVAFRE-BAKCLA`) | 0.06 / 0.89 (400) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Evans / Frey (`KXITFWDOUBLES-26OCT06BAKCLAEVAFRE-EVAFRE`) | 0.46 / 0.75 (5) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Capurro Taborda / Perez Alarcon vs Slama / Tanasie -- W50 Lexington SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 00:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06CAPPERSLATAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Capurro Taborda / Perez Alarcon (`KXITFWDOUBLES-26OCT06CAPPERSLATAN-CAPPER`) | 0.10 / 0.62 (3) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Slama / Tanasie (`KXITFWDOUBLES-26OCT06CAPPERSLATAN-SLATAN`) | 0.06 / 0.49 (50) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hui / Kononova vs El Jardi / Yamalapalli -- W50 Lexington SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 00:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06HUIKONELJYAM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| El Jardi / Yamalapalli (`KXITFWDOUBLES-26OCT06HUIKONELJYAM-ELJYAM`) | 0.21 / 0.48 (1) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hui / Kononova (`KXITFWDOUBLES-26OCT06HUIKONELJYAM-HUIKON`) | 0.06 / 0.63 (67) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Osuigwe / Osuigwe vs Heuser / Sharabura -- W50 Lexington SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 00:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06OSUOSUHEUSHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Heuser / Sharabura (`KXITFWDOUBLES-26OCT06OSUOSUHEUSHA-HEUSHA`) | 0.06 / 0.37 (39) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Osuigwe / Osuigwe (`KXITFWDOUBLES-26OCT06OSUOSUHEUSHA-OSUOSU`) | 0.07 / 0.73 (38) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Ariel Hidalgo Aguirre / Nicolas Sicco Hanna vs Mbithi / Sebastian Osorio -- M15 Quito R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06ARINICMBISEB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ariel Hidalgo Aguirre / Nicolas Sicco Hanna (`KXITFDOUBLES-26OCT06ARINICMBISEB-ARINIC`) | 0.07 / 0.79 (1) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mbithi / Sebastian Osorio (`KXITFDOUBLES-26OCT06ARINICMBISEB-MBISEB`) | 0.07 / 0.94 (102) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Esteban Rico Arias / Salazar vs De Dios / Grippo -- M15 Quito R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06ESTSALDEDGRI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| De Dios / Grippo (`KXITFDOUBLES-26OCT06ESTSALDEDGRI-DEDGRI`) | 0.08 / 0.45 (45) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Esteban Rico Arias / Salazar (`KXITFDOUBLES-26OCT06ESTSALDEDGRI-ESTSAL`) | 0.06 / 0.67 (75) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Rebecca Sramkova vs Claire Liu -- WTA 125K Suzhou R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 05:00Z
* Current expected start: 2026-10-07 02:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-07 01:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Hard · scheduled 2026-10-06T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:211685:214906:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Claire Liu (`KXWTACHALLENGERMATCH-26OCT05SRALIU-LIU`) | 0.66 / 0.67 (894) | 66.5% | 53.9% | 52.6% | 52.1% [51.6%-52.6%] | -- | -- | -- | -- | PASS | -12.6 pp | REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rebecca Sramkova (`KXWTACHALLENGERMATCH-26OCT05SRALIU-SRA`) | 0.33 / 0.35 (1116) | 34.0% | 46.1% | 47.3% | 47.9% [47.3%-48.4%] | -- | -- | -- | -- | SHADOW_BET | +12.1 pp | REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4339.0, B 3837.0; serve-point win A 54.8%, B 44.5%; Elo A 1764.6, B 1776.9; model uncertainty 0.0053
* Form inputs: days since last match A 1, B 1; matches on record A 634, B 450; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE

## Darya Astakhova vs Renata Zarazua -- WTA 125K Suzhou R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-07 05:00Z
* Current expected start: 2026-10-07 02:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-07 01:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-07T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT06ASTZAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Darya Astakhova (`KXWTACHALLENGERMATCH-26OCT06ASTZAR-AST`) | 0.33 / 0.34 (1) | 33.5% | -- | -- | -- [-----] | -- | 35.8% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Renata Zarazua (`KXWTACHALLENGERMATCH-26OCT06ASTZAR-ZAR`) | 0.65 / 0.66 (1448) | 65.5% | -- | -- | -- [-----] | -- | 64.3% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; THIN_DISPLAYED_SIZE

## Yara Bartashevich vs Edda Mamedova -- W35 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 02:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T02:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06BARMAM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yara Bartashevich (`KXITFWMATCH-26OCT06BARMAM-BAR`) | 0.37 / 0.40 (180) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Edda Mamedova (`KXITFWMATCH-26OCT06BARMAM-MAM`) | 0.58 / 0.59 (60) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jo-Yee Chan vs Victoria Bosio -- W35 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 02:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T02:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206345:270125:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Victoria Bosio (`KXITFWMATCH-26OCT06CHABOS-BOS`) | 0.47 / 0.49 (1039) | 48.0% | 76.1% | 91.5% | 75.3% [68.5%-79.7%] | -- | -- | -- | -- | PASS | +28.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jo-Yee Chan (`KXITFWMATCH-26OCT06CHABOS-CHA`) | 0.50 / 0.52 (3231) | 51.0% | 23.9% | 8.5% | 24.7% [20.3%-31.5%] | -- | -- | -- | -- | PASS | -27.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 531.0, B 3098.0; serve-point win A 50.5%, B 44.2%; Elo A 1410.0, B 1532.9; model uncertainty 0.0558
* Form inputs: days since last match A 428, B 23; matches on record A 8, B 564; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT06CHABOS-BOS  (YES = Victoria Bosio)
Model: 76%
Kalshi: 48%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.022, surface_dev_loose -0.013, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jordyn Hazelitt vs Annika Penickova -- W35 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 02:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T02:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:266379:270434:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jordyn Hazelitt (`KXITFWMATCH-26OCT06HAZPEN-HAZ`) | 0.22 / 0.23 (3479) | 22.5% | 14.7% | 26.1% | 25.6% [23.9%-27.8%] | -- | -- | -- | -- | PASS | -7.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Annika Penickova (`KXITFWMATCH-26OCT06HAZPEN-PEN`) | 0.77 / 0.78 (1496) | 77.5% | 85.3% | 73.9% | 74.4% [72.2%-76.1%] | -- | -- | -- | -- | PASS | +7.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 347.0, B 702.0; serve-point win A 49.9%, B 42.2%; Elo A 1294.5, B 1478.6; model uncertainty 0.0196
* Form inputs: days since last match A 42, B 42; matches on record A 6, B 38; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.009, surface_dev_loose -0.013, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ekaterina Maklakova vs Victoria Rodriguez -- W35 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 02:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T02:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211874:221952:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Maklakova (`KXITFWMATCH-26OCT06MAKROD-MAK`) | 0.53 / 0.58 (59) | 55.5% | 48.3% | 62.1% | 55.4% [52.1%-58.0%] | -- | -- | -- | -- | PASS | -7.2 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Victoria Rodriguez (`KXITFWMATCH-26OCT06MAKROD-ROD`) | 0.42 / 0.44 (44) | 43.0% | 51.7% | 37.9% | 44.6% [42.0%-47.9%] | -- | -- | -- | -- | PASS | +8.7 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1496.0, B 2050.0; serve-point win A 51.2%, B 48.5%; Elo A 1536.4, B 1548.3; model uncertainty 0.0292
* Form inputs: days since last match A 162, B 24; matches on record A 213, B 574; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.016, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amelie Justine Hejtmanek vs Hanna Chang -- W35 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 03:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T03:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213949:260323:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hanna Chang (`KXITFWMATCH-26OCT06HEJCHA-CHA`) | 0.87 / 0.90 (3376) | 88.5% | 90.9% | 81.0% | 81.3% [79.5%-82.7%] | -- | -- | -- | -- | PASS | +2.4 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amelie Justine Hejtmanek (`KXITFWMATCH-26OCT06HEJCHA-HEJ`) | 0.10 / 0.12 (1234) | 11.0% | 9.1% | 19.0% | 18.7% [17.3%-20.5%] | -- | -- | -- | -- | PASS | -1.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1296.0, B 3084.0; serve-point win A 50.3%, B 39.6%; Elo A 1348.8, B 1608.7; model uncertainty 0.0159
* Form inputs: days since last match A 169, B 169; matches on record A 54, B 519; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.004, surface_dev_loose -0.007, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kristina Penickova vs Alina Shcherbinina -- W35 Las Vegas NV R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 03:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-07T03:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221278:266381:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kristina Penickova (`KXITFWMATCH-26OCT06PENSHC-PEN`) | 0.57 / 0.58 (1936) | 57.5% | 78.6% | 59.5% | 69.4% [68.5%-71.3%] | -- | -- | -- | -- | PASS | +21.1 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alina Shcherbinina (`KXITFWMATCH-26OCT06PENSHC-SHC`) | 0.41 / 0.42 (984) | 41.5% | 21.4% | 40.5% | 30.6% [28.7%-31.6%] | -- | -- | -- | -- | PASS | -20.1 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1178.0, B 127.0; serve-point win A 57.4%, B 48.6%; Elo A 1498.0, B 1349.9; model uncertainty 0.0141
* Form inputs: days since last match A 41, B 232; matches on record A 39, B 55; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT06PENSHC-PEN  (YES = Kristina Penickova)
Model: 79%
Kalshi: 57%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arthur Gea vs Jaime Faria -- ATP Shanghai R128

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-07 04:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-07 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:210262:210338:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jaime Faria (`KXATPMATCH-26OCT06GEAFAR-FAR`) | 0.37 / 0.38 (118) | 37.5% | 37.0% | 26.3% | 30.2% [27.1%-37.1%] | -- | -- | -- | -- | PASS | -0.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Arthur Gea (`KXATPMATCH-26OCT06GEAFAR-GEA`) | 0.62 / 0.63 (17274) | 62.5% | 63.0% | 73.7% | 69.8% [62.9%-72.9%] | -- | -- | -- | -- | PASS | +0.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5572.0, B 6042.0; serve-point win A 63.6%, B 39.0%; Elo A 1848.2, B 1819.9; model uncertainty 0.0497
* Form inputs: days since last match A 4, B 4; matches on record A 265, B 343; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.017, surface_dev_loose +0.021, surface_dev_tight -0.026
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT06GEAFAR-28` Over 27.5 games: 0.28/0.31 mid 29.5%, model 38.1% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06GEAFAR-18` Over 17.5 games: 0.84/0.86 mid 85.0%, model 91.6% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06GEAFAR-GEA6` Will Arthur Gea win at least 5.5 more games than Jaime Faria?: 0.19/0.24 mid 21.5%, model 15.4% (projection_v2.0 (prediction ledger)) -- gap -6.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06GEAFAR-GEA21` Will Arthur Gea win the Arthur Gea vs Jaime Faria match by a set score of 2-1?: 0.21/0.24 mid 22.5%, model 28.5% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06GEAFAR-23` Over 22.5 games: 0.52/0.53 mid 52.5%, model 58.3% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06GEAFAR-GEA20` Will Arthur Gea win the Arthur Gea vs Jaime Faria match by a set score of 2-0?: 0.39/0.41 mid 40.0%, model 34.5% (projection_v2.0 (prediction ledger)) -- gap -5.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06GEAFAR-FAR20` Will Jaime Faria win the Arthur Gea vs Jaime Faria match by a set score of 2-0?: 0.19/0.22 mid 20.5%, model 17.0% (projection_v2.0 (prediction ledger)) -- gap -3.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06GEAFAR-FAR21` Will Jaime Faria win the Arthur Gea vs Jaime Faria match by a set score of 2-1?: 0.15/0.18 mid 16.5%, model 20.0% (projection_v2.0 (prediction ledger)) -- gap +3.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06GEAFAR-FAR2` Will Jaime Faria win at least 1.5 more games than Arthur Gea?: 0.30/0.35 mid 32.5%, model 30.2% (projection_v2.0 (prediction ledger)) -- gap -2.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT06GEAFAR-2-FAR` Will Jaime Faria win set 2 in the Arthur Gea vs Jaime Faria match: 0.39/0.42 mid 40.5%, model 41.2% (projection_v2.0 (prediction ledger)) -- gap +0.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06GEAFAR-2-GEA` Will Arthur Gea win set 2 in the Arthur Gea vs Jaime Faria match: 0.58/0.61 mid 59.5%, model 58.8% (projection_v2.0 (prediction ledger)) -- gap -0.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT06GEAFAR-GEA3` Will Arthur Gea win at least 2.5 more games than Jaime Faria?: 0.48/0.51 mid 49.5%, model 48.8% (projection_v2.0 (prediction ledger)) -- gap -0.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT06GEAFAR-1-FAR` Will Jaime Faria win set 1 in the Arthur Gea vs Jaime Faria match: 0.40/0.42 mid 41.0%, model 41.2% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06GEAFAR-1-GEA` Will Arthur Gea win set 1 in the Arthur Gea vs Jaime Faria match: 0.58/0.60 mid 59.0%, model 58.8% (projection_v2.0 (prediction ledger)) -- gap -0.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Aleksandar Kovacevic vs Matteo Berrettini -- ATP Shanghai R128

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-07 04:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-07 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126610:206499:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Berrettini (`KXATPMATCH-26OCT06KOVBER-BER`) | 0.66 / 0.67 (24185) | 66.5% | 63.7% | 66.9% | 67.7% [63.1%-74.3%] | -- | -- | -- | -- | PASS | -2.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aleksandar Kovacevic (`KXATPMATCH-26OCT06KOVBER-KOV`) | 0.34 / 0.35 (4695) | 34.5% | 36.3% | 33.1% | 32.3% [25.7%-36.9%] | -- | -- | -- | -- | PASS | +1.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5809.0, B 4137.0; serve-point win A 69.5%, B 27.5%; Elo A 1768.7, B 1920.8; model uncertainty 0.0559
* Form inputs: days since last match A 7, B 3; matches on record A 421, B 559; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.044, surface_pool_high +0.047, surface_dev_loose +0.000, surface_dev_tight -0.009
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT06KOVBER-24` Over 23.5 games: 0.49/0.50 mid 49.5%, model 60.3% (projection_v2.0 (prediction ledger)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06KOVBER-BER6` Will Matteo Berrettini win at least 5.5 more games than Aleksandar Kovacevic?: 0.12/0.15 mid 13.5%, model 5.0% (projection_v2.0 (prediction ledger)) -- gap -8.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06KOVBER-29` Over 28.5 games: 0.35/0.37 mid 36.0%, model 43.7% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06KOVBER-19` Over 18.5 games: 0.88/0.91 mid 89.5%, model 96.0% (projection_v2.0 (prediction ledger)) -- gap +6.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06KOVBER-BER20` Will Matteo Berrettini win the Aleksandar Kovacevic vs Matteo Berrettini match by a set score of 2-0?: 0.40/0.43 mid 41.5%, model 35.1% (projection_v2.0 (prediction ledger)) -- gap -6.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06KOVBER-BER3` Will Matteo Berrettini win at least 2.5 more games than Aleksandar Kovacevic?: 0.46/0.47 mid 46.5%, model 41.5% (projection_v2.0 (prediction ledger)) -- gap -5.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06KOVBER-BER21` Will Matteo Berrettini win the Aleksandar Kovacevic vs Matteo Berrettini match by a set score of 2-1?: 0.23/0.26 mid 24.5%, model 28.6% (projection_v2.0 (prediction ledger)) -- gap +4.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT06KOVBER-2-BER` Will Matteo Berrettini win set 2 in the Aleksandar Kovacevic vs Matteo Berrettini match: 0.61/0.64 mid 62.5%, model 59.2% (projection_v2.0 (prediction ledger)) -- gap -3.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06KOVBER-KOV21` Will Aleksandar Kovacevic win the Aleksandar Kovacevic vs Matteo Berrettini match by a set score of 2-1?: 0.15/0.18 mid 16.5%, model 19.7% (projection_v2.0 (prediction ledger)) -- gap +3.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT06KOVBER-1-BER` Will Matteo Berrettini win set 1 in the Aleksandar Kovacevic vs Matteo Berrettini match: 0.60/0.63 mid 61.5%, model 59.2% (projection_v2.0 (prediction ledger)) -- gap -2.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06KOVBER-1-KOV` Will Aleksandar Kovacevic win set 1 in the Aleksandar Kovacevic vs Matteo Berrettini match: 0.38/0.39 mid 38.5%, model 40.8% (projection_v2.0 (prediction ledger)) -- gap +2.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06KOVBER-2-KOV` Will Aleksandar Kovacevic win set 2 in the Aleksandar Kovacevic vs Matteo Berrettini match: 0.37/0.40 mid 38.5%, model 40.8% (projection_v2.0 (prediction ledger)) -- gap +2.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06KOVBER-KOV20` Will Aleksandar Kovacevic win the Aleksandar Kovacevic vs Matteo Berrettini match by a set score of 2-0?: 0.16/0.19 mid 17.5%, model 16.6% (projection_v2.0 (prediction ledger)) -- gap -0.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06KOVBER-KOV2` Will Aleksandar Kovacevic win at least 1.5 more games than Matteo Berrettini?: 0.26/0.29 mid 27.5%, model 27.6% (projection_v2.0 (prediction ledger)) -- gap +0.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Sho Shimabukuro vs Miomir Kecmanovic -- ATP Shanghai R128

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-07 04:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-07 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200175:200647:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miomir Kecmanovic (`KXATPMATCH-26OCT06SHIKEC-KEC`) | 0.67 / 0.68 (3343) | 67.5% | 62.5% | 60.3% | 60.3% [59.4%-61.8%] | -- | -- | -- | -- | PASS | -5.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sho Shimabukuro (`KXATPMATCH-26OCT06SHIKEC-SHI`) | 0.32 / 0.33 (42086) | 32.5% | 37.5% | 39.7% | 39.7% [38.2%-40.6%] | -- | -- | -- | -- | SHADOW_BET | +5.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5302.0, B 5606.0; serve-point win A 62.8%, B 34.7%; Elo A 1701.1, B 1785.5; model uncertainty 0.0121
* Form inputs: days since last match A 5, B 8; matches on record A 462, B 613; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT06SHIKEC-KEC6` Will Miomir Kecmanovic win at least 5.5 more games than Sho Shimabukuro?: 0.23/0.27 mid 25.0%, model 13.0% (projection_v2.0 (prediction ledger)) -- gap -12.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06SHIKEC-28` Over 27.5 games: 0.27/0.30 mid 28.5%, model 39.9% (projection_v2.0 (prediction ledger)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06SHIKEC-23` Over 22.5 games: 0.48/0.50 mid 49.0%, model 60.1% (projection_v2.0 (prediction ledger)) -- gap +11.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06SHIKEC-KEC20` Will Miomir Kecmanovic win the Sho Shimabukuro vs Miomir Kecmanovic match by a set score of 2-0?: 0.43/0.46 mid 44.5%, model 34.1% (projection_v2.0 (prediction ledger)) -- gap -10.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06SHIKEC-KEC3` Will Miomir Kecmanovic win at least 2.5 more games than Sho Shimabukuro?: 0.56/0.57 mid 56.5%, model 47.3% (projection_v2.0 (prediction ledger)) -- gap -9.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06SHIKEC-18` Over 17.5 games: 0.85/0.88 mid 86.5%, model 93.2% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06SHIKEC-KEC21` Will Miomir Kecmanovic win the Sho Shimabukuro vs Miomir Kecmanovic match by a set score of 2-1?: 0.21/0.24 mid 22.5%, model 28.4% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06SHIKEC-SHI21` Will Sho Shimabukuro win the Sho Shimabukuro vs Miomir Kecmanovic match by a set score of 2-1?: 0.13/0.16 mid 14.5%, model 20.2% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT06SHIKEC-1-KEC` Will Miomir Kecmanovic win set 1 in the Sho Shimabukuro vs Miomir Kecmanovic match: 0.63/0.65 mid 64.0%, model 58.4% (projection_v2.0 (prediction ledger)) -- gap -5.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06SHIKEC-2-KEC` Will Miomir Kecmanovic win set 2 in the Sho Shimabukuro vs Miomir Kecmanovic match: 0.62/0.65 mid 63.5%, model 58.4% (projection_v2.0 (prediction ledger)) -- gap -5.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06SHIKEC-2-SHI` Will Sho Shimabukuro win set 2 in the Sho Shimabukuro vs Miomir Kecmanovic match: 0.35/0.38 mid 36.5%, model 41.6% (projection_v2.0 (prediction ledger)) -- gap +5.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06SHIKEC-1-SHI` Will Sho Shimabukuro win set 1 in the Sho Shimabukuro vs Miomir Kecmanovic match: 0.36/0.38 mid 37.0%, model 41.6% (projection_v2.0 (prediction ledger)) -- gap +4.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT06SHIKEC-SHI2` Will Sho Shimabukuro win at least 1.5 more games than Miomir Kecmanovic?: 0.26/0.29 mid 27.5%, model 30.5% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06SHIKEC-SHI20` Will Sho Shimabukuro win the Sho Shimabukuro vs Miomir Kecmanovic match by a set score of 2-0?: 0.15/0.19 mid 17.0%, model 17.3% (projection_v2.0 (prediction ledger)) -- gap +0.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Elizabeth Reasco Gonzalez / Sahdiieva vs Eraydin / Walker -- W35 Las Vegas NV R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06ELISAHERAWAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elizabeth Reasco Gonzalez / Sahdiieva (`KXITFWDOUBLES-26OCT06ELISAHERAWAL-ELISAH`) | 0.06 / 0.90 (50) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eraydin / Walker (`KXITFWDOUBLES-26OCT06ELISAHERAWAL-ERAWAL`) | 0.06 / 0.90 (50) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Mattioli / Scott vs Cherubini / Pace -- W35 Las Vegas NV R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06MATSCOCHEPAC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cherubini / Pace (`KXITFWDOUBLES-26OCT06MATSCOCHEPAC-CHEPAC`) | 0.06 / 0.90 (50) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mattioli / Scott (`KXITFWDOUBLES-26OCT06MATSCOCHEPAC-MATSCO`) | 0.06 / 0.90 (50) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Iva Jovic vs Iga Swiatek -- WTA Beijing R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 06:00Z
* Current expected start: 2026-10-07 05:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-07 04:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1380_MIN

WTA (MASTERS_1000) · Hard · scheduled 2026-10-06T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:216347:260300:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iva Jovic (`KXWTAMATCH-26OCT05JOVSWI-JOV`) | 0.33 / 0.35 (15925) | 34.0% | 34.9% | 20.8% | 22.7% [21.2%-24.7%] | -- | -- | -- | -- | PASS | +0.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Iga Swiatek (`KXWTAMATCH-26OCT05JOVSWI-SWI`) | 0.66 / 0.67 (52100) | 66.5% | 65.0% | 79.2% | 77.3% [75.3%-78.8%] | -- | -- | -- | -- | SHADOW_BET | -1.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3602.0, B 4863.0; serve-point win A 56.2%, B 40.8%; Elo A 2011.1, B 2176.9; model uncertainty 0.0178
* Form inputs: days since last match A 1, B 1; matches on record A 167, B 541; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.020, surface_dev_loose +0.012, surface_dev_tight -0.012
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT05JOVSWI-22` Over 21.5 games: 0.44/0.45 mid 44.5%, model 61.4% (projection_v2.0 (prediction ledger)) -- gap +16.9 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT05JOVSWI-27` Over 26.5 games: 0.23/0.27 mid 25.0%, model 38.4% (projection_v2.0 (prediction ledger)) -- gap +13.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT05JOVSWI-17` Over 16.5 games: 0.83/0.86 mid 84.5%, model 93.4% (projection_v2.0 (prediction ledger)) -- gap +8.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT05JOVSWI-2-SWI` Will Iga Swiatek win set 2 in the Iva Jovic vs Iga Swiatek match: 0.63/0.65 mid 64.0%, model 60.2% (projection_v2.0 (prediction ledger)) -- gap -3.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT05JOVSWI-1-SWI` Will Iga Swiatek win set 1 in the Iva Jovic vs Iga Swiatek match: 0.62/0.63 mid 62.5%, model 60.2% (projection_v2.0 (prediction ledger)) -- gap -2.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT05JOVSWI-2-JOV` Will Iva Jovic win set 2 in the Iva Jovic vs Iga Swiatek match: 0.37/0.39 mid 38.0%, model 39.8% (projection_v2.0 (prediction ledger)) -- gap +1.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT05JOVSWI-1-JOV` Will Iva Jovic win set 1 in the Iva Jovic vs Iga Swiatek match: 0.38/0.39 mid 38.5%, model 39.8% (projection_v2.0 (prediction ledger)) -- gap +1.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE

## Sara Errani / Jasmine Paolini vs Katie Boulter / Yuliia Starodubtseva -- WTA Beijing R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-07 14:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-07 05:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-07 04:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-07T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07ERRPAOBOUSTA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katie Boulter / Yuliia Starodubtseva (`KXWTADOUBLES-26OCT07ERRPAOBOUSTA-BOUSTA`) | 0.30 / 0.34 (24) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sara Errani / Jasmine Paolini (`KXWTADOUBLES-26OCT07ERRPAOBOUSTA-ERRPAO`) | 0.63 / 0.70 (437) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Erin Routliffe / Aldila Sutjiadi vs Anna Danilina / Desirae Krawczyk -- WTA Beijing R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-07 14:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-07 05:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-07 04:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-07T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07ROUSUTDANKRA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Danilina / Desirae Krawczyk (`KXWTADOUBLES-26OCT07ROUSUTDANKRA-DANKRA`) | 0.41 / 0.46 (46) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Erin Routliffe / Aldila Sutjiadi (`KXWTADOUBLES-26OCT07ROUSUTDANKRA-ROUSUT`) | 0.51 / 0.58 (328) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Yuhan Liu vs Tori Russell -- W35 Wagga Wagga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06LIURUS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuhan Liu (`KXITFWMATCH-26OCT06LIURUS-LIU`) | 0.55 / 0.70 (3271) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tori Russell (`KXITFWMATCH-26OCT06LIURUS-RUS`) | 0.30 / 0.34 (29) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alana Subasic vs Haruna Arakawa -- W35 Wagga Wagga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06SUBARA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Haruna Arakawa (`KXITFWMATCH-26OCT06SUBARA-ARA`) | 0.34 / 0.37 (4) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alana Subasic (`KXITFWMATCH-26OCT06SUBARA-SUB`) | 0.61 / 0.65 (32) | 63.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Belle Thompson vs Yuno Kitahara -- W35 Wagga Wagga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06THOKIT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuno Kitahara (`KXITFWMATCH-26OCT06THOKIT-KIT`) | 0.60 / 0.63 (2539) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Belle Thompson (`KXITFWMATCH-26OCT06THOKIT-THO`) | 0.35 / 0.38 (3866) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ya Yi Yang vs Ena Shibahara -- W35 Wagga Wagga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06YANSHI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ena Shibahara (`KXITFWMATCH-26OCT06YANSHI-SHI`) | 0.70 / 0.78 (27) | 74.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ya Yi Yang (`KXITFWMATCH-26OCT06YANSHI-YAN`) | 0.20 / 0.26 (34) | 23.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yannick Hanfmann vs Kamil Majchrzak -- ATP Shanghai R128

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-07 05:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-07 04:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105870:111794:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yannick Hanfmann (`KXATPMATCH-26OCT06HANMAJ-HAN`) | 0.37 / 0.38 (12807) | 37.5% | 39.5% | 58.8% | 55.4% [53.4%-56.8%] | -- | -- | -- | -- | SHADOW_BET | +2.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kamil Majchrzak (`KXATPMATCH-26OCT06HANMAJ-MAJ`) | 0.62 / 0.63 (3366) | 62.5% | 60.5% | 41.2% | 44.6% [43.2%-46.6%] | -- | -- | -- | -- | PASS | -2.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5796.0, B 5075.0; serve-point win A 64.3%, B 33.5%; Elo A 1781.4, B 1830.3; model uncertainty 0.017
* Form inputs: days since last match A 8, B 7; matches on record A 700, B 700; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose +0.005, surface_dev_tight -0.015
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT06HANMAJ-20` Over 19.5 games: 0.69/0.72 mid 70.5%, model 82.8% (projection_v2.0 (prediction ledger)) -- gap +12.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06HANMAJ-30` Over 29.5 games: 0.20/0.22 mid 21.0%, model 33.0% (projection_v2.0 (prediction ledger)) -- gap +12.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06HANMAJ-MAJ5` Will Kamil Majchrzak win at least 4.5 more games than Yannick Hanfmann?: 0.30/0.33 mid 31.5%, model 20.3% (projection_v2.0 (prediction ledger)) -- gap -11.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06HANMAJ-25` Over 24.5 games: 0.44/0.46 mid 45.0%, model 53.9% (projection_v2.0 (prediction ledger)) -- gap +8.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06HANMAJ-MAJ20` Will Kamil Majchrzak win the Yannick Hanfmann vs Kamil Majchrzak match by a set score of 2-0?: 0.38/0.41 mid 39.5%, model 32.6% (projection_v2.0 (prediction ledger)) -- gap -7.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06HANMAJ-MAJ21` Will Kamil Majchrzak win the Yannick Hanfmann vs Kamil Majchrzak match by a set score of 2-1?: 0.21/0.24 mid 22.5%, model 28.0% (projection_v2.0 (prediction ledger)) -- gap +5.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06HANMAJ-HAN21` Will Yannick Hanfmann win the Yannick Hanfmann vs Kamil Majchrzak match by a set score of 2-1?: 0.15/0.18 mid 16.5%, model 21.1% (projection_v2.0 (prediction ledger)) -- gap +4.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06HANMAJ-MAJ2` Will Kamil Majchrzak win at least 1.5 more games than Yannick Hanfmann?: 0.56/0.57 mid 56.5%, model 52.7% (projection_v2.0 (prediction ledger)) -- gap -3.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT06HANMAJ-1-HAN` Will Yannick Hanfmann win set 1 in the Yannick Hanfmann vs Kamil Majchrzak match: 0.39/0.42 mid 40.5%, model 43.0% (projection_v2.0 (prediction ledger)) -- gap +2.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06HANMAJ-1-MAJ` Will Kamil Majchrzak win set 1 in the Yannick Hanfmann vs Kamil Majchrzak match: 0.58/0.61 mid 59.5%, model 57.0% (projection_v2.0 (prediction ledger)) -- gap -2.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06HANMAJ-2-HAN` Will Yannick Hanfmann win set 2 in the Yannick Hanfmann vs Kamil Majchrzak match: 0.39/0.42 mid 40.5%, model 43.0% (projection_v2.0 (prediction ledger)) -- gap +2.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06HANMAJ-2-MAJ` Will Kamil Majchrzak win set 2 in the Yannick Hanfmann vs Kamil Majchrzak match: 0.58/0.61 mid 59.5%, model 57.0% (projection_v2.0 (prediction ledger)) -- gap -2.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06HANMAJ-HAN20` Will Yannick Hanfmann win the Yannick Hanfmann vs Kamil Majchrzak match by a set score of 2-0?: 0.19/0.22 mid 20.5%, model 18.4% (projection_v2.0 (prediction ledger)) -- gap -2.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06HANMAJ-HAN2` Will Yannick Hanfmann win at least 1.5 more games than Kamil Majchrzak?: 0.30/0.33 mid 31.5%, model 32.1% (projection_v2.0 (prediction ledger)) -- gap +0.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Zhizhen Zhang vs Tomas Machac -- ATP Shanghai R128

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-07 05:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-07 04:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111190:207830:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomas Machac (`KXATPMATCH-26OCT06ZHAMAC-MAC`) | 0.70 / 0.71 (19039) | 70.5% | 71.6% | 63.4% | 69.2% [66.6%-71.8%] | -- | -- | -- | -- | PASS | +1.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zhizhen Zhang (`KXATPMATCH-26OCT06ZHAMAC-ZHA`) | 0.29 / 0.30 (312) | 29.5% | 28.4% | 36.6% | 30.8% [28.2%-33.4%] | -- | -- | -- | -- | PASS | -1.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3629.0, B 3946.0; serve-point win A 63.4%, B 32.0%; Elo A 1684.4, B 1933.0; model uncertainty 0.0258
* Form inputs: days since last match A 6, B 5; matches on record A 535, B 449; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.009, surface_dev_loose +0.001, surface_dev_tight +0.008
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT06ZHAMAC-29` Over 28.5 games: 0.23/0.26 mid 24.5%, model 34.8% (projection_v2.0 (prediction ledger)) -- gap +10.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06ZHAMAC-19` Over 18.5 games: 0.78/0.82 mid 80.0%, model 87.9% (projection_v2.0 (prediction ledger)) -- gap +7.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06ZHAMAC-24` Over 23.5 games: 0.43/0.44 mid 43.5%, model 51.4% (projection_v2.0 (prediction ledger)) -- gap +7.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06ZHAMAC-MAC7` Will Tomas Machac win at least 6.5 more games than Zhizhen Zhang?: 0.12/0.16 mid 14.0%, model 7.4% (projection_v2.0 (prediction ledger)) -- gap -6.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06ZHAMAC-MAC21` Will Tomas Machac win the Zhizhen Zhang vs Tomas Machac match by a set score of 2-1?: 0.21/0.25 mid 23.0%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06ZHAMAC-ZHA2` Will Zhizhen Zhang win at least 1.5 more games than Tomas Machac?: 0.24/0.27 mid 25.5%, model 22.0% (projection_v2.0 (prediction ledger)) -- gap -3.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06ZHAMAC-MAC20` Will Tomas Machac win the Zhizhen Zhang vs Tomas Machac match by a set score of 2-0?: 0.45/0.46 mid 45.5%, model 42.0% (projection_v2.0 (prediction ledger)) -- gap -3.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06ZHAMAC-ZHA20` Will Zhizhen Zhang win the Zhizhen Zhang vs Tomas Machac match by a set score of 2-0?: 0.14/0.17 mid 15.5%, model 12.4% (projection_v2.0 (prediction ledger)) -- gap -3.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06ZHAMAC-MAC4` Will Tomas Machac win at least 3.5 more games than Zhizhen Zhang?: 0.45/0.46 mid 45.5%, model 43.0% (projection_v2.0 (prediction ledger)) -- gap -2.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06ZHAMAC-ZHA21` Will Zhizhen Zhang win the Zhizhen Zhang vs Tomas Machac match by a set score of 2-1?: 0.13/0.15 mid 14.0%, model 16.0% (projection_v2.0 (prediction ledger)) -- gap +2.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT06ZHAMAC-2-MAC` Will Tomas Machac win set 2 in the Zhizhen Zhang vs Tomas Machac match: 0.65/0.67 mid 66.0%, model 64.8% (projection_v2.0 (prediction ledger)) -- gap -1.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06ZHAMAC-2-ZHA` Will Zhizhen Zhang win set 2 in the Zhizhen Zhang vs Tomas Machac match: 0.33/0.35 mid 34.0%, model 35.2% (projection_v2.0 (prediction ledger)) -- gap +1.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06ZHAMAC-1-MAC` Will Tomas Machac win set 1 in the Zhizhen Zhang vs Tomas Machac match: 0.64/0.65 mid 64.5%, model 64.8% (projection_v2.0 (prediction ledger)) -- gap +0.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06ZHAMAC-1-ZHA` Will Zhizhen Zhang win set 1 in the Zhizhen Zhang vs Tomas Machac match: 0.35/0.36 mid 35.5%, model 35.2% (projection_v2.0 (prediction ledger)) -- gap -0.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Adrian Mannarino vs Nikoloz Basilashvili -- ATP Shanghai R128

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-07 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-07 05:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-07 04:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-07T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT07MANBAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikoloz Basilashvili (`KXATPMATCH-26OCT07MANBAS-BAS`) | 0.55 / 0.58 (100) | 56.5% | -- | -- | -- [-----] | -- | 56.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Adrian Mannarino (`KXATPMATCH-26OCT07MANBAS-MAN`) | 0.41 / 0.44 (127) | 42.5% | -- | -- | -- [-----] | -- | 43.4% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE

## Alex Molcan vs Federico Cina -- ATP Shanghai R128

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-07 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-07 06:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-07 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-07T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT07MOLCIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Federico Cina (`KXATPMATCH-26OCT07MOLCIN-CIN`) | 0.43 / 0.47 (222) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alex Molcan (`KXATPMATCH-26OCT07MOLCIN-MOL`) | 0.53 / 0.57 (783) | 55.0% | -- | -- | -- [-----] | -- | 59.1% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Yaroslav Demin vs Akira Santillan -- ATP Challenger Wuning 3 R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-07T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06DEMSAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yaroslav Demin (`KXATPCHALLENGERMATCH-26OCT06DEMSAN-DEM`) | 0.43 / 0.44 (1081) | 43.5% | -- | -- | -- [-----] | -- | 40.8% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Akira Santillan (`KXATPCHALLENGERMATCH-26OCT06DEMSAN-SAN`) | 0.56 / 0.57 (976) | 56.5% | -- | -- | -- [-----] | -- | 57.3% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Omar Jasika vs Marat Sharipov -- ATP Challenger Wuning 3 R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-07T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06JASSHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Omar Jasika (`KXATPCHALLENGERMATCH-26OCT06JASSHA-JAS`) | 0.18 / 0.19 (1099) | 18.5% | -- | -- | -- [-----] | -- | 32.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marat Sharipov (`KXATPCHALLENGERMATCH-26OCT06JASSHA-SHA`) | 0.81 / 0.82 (283) | 81.5% | -- | -- | -- [-----] | -- | 80.3% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Hiroki Moriya vs Keisuke Saitoh -- ATP Challenger Wuning 3 R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-07T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06MORSAI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hiroki Moriya (`KXATPCHALLENGERMATCH-26OCT06MORSAI-MOR`) | 0.51 / 0.52 (976) | 51.5% | -- | -- | -- [-----] | -- | 51.3% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Keisuke Saitoh (`KXATPCHALLENGERMATCH-26OCT06MORSAI-SAI`) | 0.48 / 0.50 (1240) | 49.0% | -- | -- | -- [-----] | -- | 47.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Laquisa Khan vs Ashleigh Simes -- W35 Wagga Wagga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06KHASIM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Laquisa Khan (`KXITFWMATCH-26OCT06KHASIM-KHA`) | 0.33 / 0.36 (843) | 34.5% | -- | -- | -- [-----] | 35.6% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ashleigh Simes (`KXITFWMATCH-26OCT06KHASIM-SIM`) | 0.64 / 0.67 (4533) | 65.5% | -- | -- | -- [-----] | 64.4% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kanon Sawashiro vs Tahlia Kokkinis -- W35 Wagga Wagga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06SAWKOK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tahlia Kokkinis (`KXITFWMATCH-26OCT06SAWKOK-KOK`) | 0.70 / 0.73 (2) | 71.5% | -- | -- | -- [-----] | 70.2% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kanon Sawashiro (`KXITFWMATCH-26OCT06SAWKOK-SAW`) | 0.26 / 0.29 (2) | 27.5% | -- | -- | -- [-----] | 29.8% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elyse Tse vs Monique Barry -- W35 Wagga Wagga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06TSEBAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Monique Barry (`KXITFWMATCH-26OCT06TSEBAR-BAR`) | 0.28 / 0.36 (40) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Elyse Tse (`KXITFWMATCH-26OCT06TSEBAR-TSE`) | 0.51 / 0.72 (3624) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## I Wen Wan vs Jizelle Sibai -- W35 Wagga Wagga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06WANSIB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jizelle Sibai (`KXITFWMATCH-26OCT06WANSIB-SIB`) | 0.45 / 0.46 (47) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| I Wen Wan (`KXITFWMATCH-26OCT06WANSIB-WAN`) | 0.49 / 0.53 (4088) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Coco Gauff vs Elise Mertens -- WTA Beijing R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-07 06:00Z
* Current expected start: 2026-10-07 06:15Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-07 05:30Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+15_MIN

WTA (MASTERS_1000) · Hard · scheduled 2026-10-07T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:210722:221103:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Coco Gauff (`KXWTAMATCH-26OCT06GAUMER-GAU`) | 0.78 / 0.79 (29988) | 78.5% | 75.4% | 58.4% | 64.5% [61.5%-71.6%] | 76.2% | -- | 76.2% | KALSHI_LONE_OUTLIER | PASS | -3.1 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Elise Mertens (`KXWTAMATCH-26OCT06GAUMER-MER`) | 0.22 / 0.23 (44036) | 22.5% | 24.6% | 41.6% | 35.5% [28.4%-38.5%] | 23.8% | -- | 23.8% | KALSHI_LONE_OUTLIER | SHADOW_BET | +2.1 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5157.0, B 3838.0; serve-point win A 58.1%, B 47.1%; Elo A 2204.5, B 1983.0; model uncertainty 0.0506
* Form inputs: days since last match A 3, B 1; matches on record A 444, B 801; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.010, surface_dev_loose -0.015, surface_dev_tight +0.010
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT06GAUMER-21` Over 20.5 games: 0.47/0.48 mid 47.5%, model 60.6% (projection_v2.0 (prediction ledger)) -- gap +13.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT06GAUMER-26` Over 25.5 games: 0.25/0.27 mid 26.0%, model 38.1% (projection_v2.0 (prediction ledger)) -- gap +12.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT06GAUMER-16` Over 15.5 games: 0.87/0.91 mid 89.0%, model 95.2% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT06GAUMER-2-GAU` Will Coco Gauff win set 2 in the Coco Gauff vs Elise Mertens match: 0.72/0.75 mid 73.5%, model 67.7% (projection_v2.0 (prediction ledger)) -- gap -5.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT06GAUMER-2-MER` Will Elise Mertens win set 2 in the Coco Gauff vs Elise Mertens match: 0.25/0.28 mid 26.5%, model 32.3% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT06GAUMER-1-MER` Will Elise Mertens win set 1 in the Coco Gauff vs Elise Mertens match: 0.27/0.28 mid 27.5%, model 32.3% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT06GAUMER-1-GAU` Will Coco Gauff win set 1 in the Coco Gauff vs Elise Mertens match: 0.71/0.72 mid 71.5%, model 67.7% (projection_v2.0 (prediction ledger)) -- gap -3.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE

## Su-Wei Hsieh / Jelena Ostapenko vs Irina Khromacheva / Liudmila Samsonova -- WTA Beijing R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-07 14:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-07 06:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-07 05:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-07T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07HSIOSTKHRSAM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Su-Wei Hsieh / Jelena Ostapenko (`KXWTADOUBLES-26OCT07HSIOSTKHRSAM-HSIOST`) | 0.63 / 0.69 (25) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Irina Khromacheva / Liudmila Samsonova (`KXWTADOUBLES-26OCT07HSIOSTKHRSAM-KHRSAM`) | 0.31 / 0.33 (23) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Katerina Siniakova / Shuai Zhang vs Nikola Bartunkova / Maja Chwalinska -- WTA Beijing R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-07 14:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-07 06:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-07 05:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-07T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07SINZHABARCHW:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikola Bartunkova / Maja Chwalinska (`KXWTADOUBLES-26OCT07SINZHABARCHW-BARCHW`) | 0.18 / 0.20 (9) | 19.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Katerina Siniakova / Shuai Zhang (`KXWTADOUBLES-26OCT07SINZHABARCHW-SINZHA`) | 0.77 / 0.82 (261) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Mattia Bellucci vs Yi Zhou -- ATP Shanghai R128

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-07 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-07 07:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-07 06:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-07T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT07BELZHO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mattia Bellucci (`KXATPMATCH-26OCT07BELZHO-BEL`) | 0.73 / 0.75 (3202) | 74.0% | -- | -- | -- [-----] | -- | 72.3% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yi Zhou (`KXATPMATCH-26OCT07BELZHO-ZHO`) | 0.25 / 0.27 (21) | 26.0% | -- | -- | -- [-----] | -- | 27.5% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE

## Marco Trungelliti vs Rei Sakamoto -- ATP Shanghai R128

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-07 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-07 07:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-07 06:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-07T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT07TRUSAK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rei Sakamoto (`KXATPMATCH-26OCT07TRUSAK-SAK`) | 0.65 / 0.68 (100) | 66.5% | -- | -- | -- [-----] | -- | 66.2% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marco Trungelliti (`KXATPMATCH-26OCT07TRUSAK-TRU`) | 0.31 / 0.34 (36) | 32.5% | -- | -- | -- [-----] | -- | 33.8% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER

## Juan Manuel Cerundolo vs Nicolas Mejia -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-07 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-08T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-07T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT07CERMEJ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Manuel Cerundolo (`KXATPMATCH-26OCT07CERMEJ-CER`) | 0.65 / 0.68 (141) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nicolas Mejia (`KXATPMATCH-26OCT07CERMEJ-MEJ`) | 0.31 / 0.34 (100) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Kimmer Coppejans vs Stefanos Tsitsipas -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-07 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-08T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-07T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT07COPTSI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kimmer Coppejans (`KXATPMATCH-26OCT07COPTSI-COP`) | 0.10 / 0.12 (1500) | 11.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stefanos Tsitsipas (`KXATPMATCH-26OCT07COPTSI-TSI`) | 0.87 / 0.88 (300) | 87.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Pavel Kotov vs Tallon Griekspoor -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-07 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-08T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-07T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT07KOTGRI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tallon Griekspoor (`KXATPMATCH-26OCT07KOTGRI-GRI`) | 0.67 / 0.69 (126) | 68.0% | -- | -- | -- [-----] | -- | 67.4% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pavel Kotov (`KXATPMATCH-26OCT07KOTGRI-KOT`) | 0.30 / 0.34 (527) | 32.0% | -- | -- | -- [-----] | -- | 32.7% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE

## Bernard Tomic vs Matteo Arnaldi -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-07 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-08T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-07T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT07TOMARN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Arnaldi (`KXATPMATCH-26OCT07TOMARN-ARN`) | 0.62 / 0.65 (43) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bernard Tomic (`KXATPMATCH-26OCT07TOMARN-TOM`) | 0.34 / 0.38 (316) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Camilo Ugo Carabelli vs Ilia Simakin -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-07 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-08T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-07T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT07UGOSIM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ilia Simakin (`KXATPMATCH-26OCT07UGOSIM-SIM`) | 0.69 / 0.72 (100) | 70.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Camilo Ugo Carabelli (`KXATPMATCH-26OCT07UGOSIM-UGO`) | 0.27 / 0.31 (324) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Rinky Hijikata vs Roman Safiullin -- ATP Shanghai R128

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-07 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-07 07:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-07 06:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-07T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT07HIJSAF:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rinky Hijikata (`KXATPMATCH-26OCT07HIJSAF-HIJ`) | 0.26 / 0.28 (100) | 27.0% | -- | -- | -- [-----] | -- | 27.8% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Roman Safiullin (`KXATPMATCH-26OCT07HIJSAF-SAF`) | 0.71 / 0.74 (1530) | 72.5% | -- | -- | -- [-----] | -- | 72.3% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER

## Francesca Franchi vs Guyun Yuchi -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06FRAYUC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesca Franchi (`KXITFWMATCH-26OCT06FRAYUC-FRA`) | 0.05 / 0.95 (50) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Guyun Yuchi (`KXITFWMATCH-26OCT06FRAYUC-YUC`) | 0.03 / 0.95 (50) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nagi Hanatani vs Mutsumi Uemura -- W35 Wagga Wagga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06HANUEM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nagi Hanatani (`KXITFWMATCH-26OCT06HANUEM-HAN`) | 0.15 / 0.25 (67) | 20.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mutsumi Uemura (`KXITFWMATCH-26OCT06HANUEM-UEM`) | 0.69 / 0.85 (3399) | 77.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Haruka Kaji vs Rira Kosaka -- W35 Wagga Wagga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06KAJKOS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Haruka Kaji (`KXITFWMATCH-26OCT06KAJKOS-KAJ`) | 0.92 / 0.94 (169) | 93.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rira Kosaka (`KXITFWMATCH-26OCT06KAJKOS-KOS`) | 0.06 / 0.08 (1189) | 7.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xiaowei Li vs Daria Egorova -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06LIXEGO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria Egorova (`KXITFWMATCH-26OCT06LIXEGO-EGO`) | 0.54 / 0.95 (50) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xiaowei Li (`KXITFWMATCH-26OCT06LIXEGO-LIX`) | 0.03 / 0.06 (26) | 4.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nana Onozawa vs Hikaru Sato -- W35 Wagga Wagga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06ONOSAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nana Onozawa (`KXITFWMATCH-26OCT06ONOSAT-ONO`) | 0.08 / 0.09 (5) | 8.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hikaru Sato (`KXITFWMATCH-26OCT06ONOSAT-SAT`) | 0.88 / 0.92 (3837) | 90.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ke Ren vs Junhan Zhang -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06RENZHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ke Ren (`KXITFWMATCH-26OCT06RENZHA-REN`) | 0.13 / 0.16 (3150) | 14.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Junhan Zhang (`KXITFWMATCH-26OCT06RENZHA-ZHA`) | 0.83 / 0.87 (116) | 85.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amy Stevens vs Jasmine Adams -- W35 Wagga Wagga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06STEADA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jasmine Adams (`KXITFWMATCH-26OCT06STEADA-ADA`) | 0.33 / 0.36 (39) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Amy Stevens (`KXITFWMATCH-26OCT06STEADA-STE`) | 0.57 / 0.67 (3344) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xiao Tang vs Albina Kakenova -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06TANKAK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Albina Kakenova (`KXITFWMATCH-26OCT06TANKAK-KAK`) | 0.31 / 0.34 (3123) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xiao Tang (`KXITFWMATCH-26OCT06TANKAK-TAN`) | 0.65 / 0.71 (185) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nino Ehrenschneider vs Qian Sun -- M25 Luan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06EHRSUN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nino Ehrenschneider (`KXITFMATCH-26OCT06EHRSUN-EHR`) | 0.70 / 0.75 (2) | 72.5% | -- | -- | -- [-----] | 72.0% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Qian Sun (`KXITFMATCH-26OCT06EHRSUN-SUN`) | 0.25 / 0.28 (3686) | 26.5% | -- | -- | -- [-----] | 28.0% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yanki Erel vs Boxiong Zhang -- M25 Luan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06EREZHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yanki Erel (`KXITFMATCH-26OCT06EREZHA-ERE`) | 0.94 / 0.97 (3143) | 95.5% | -- | -- | -- [-----] | 93.7% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Boxiong Zhang (`KXITFMATCH-26OCT06EREZHA-ZHA`) | 0.03 / 0.05 (527) | 4.0% | -- | -- | -- [-----] | 6.3% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Egor Pleshivtsev vs Yua Taka -- M25 Luan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06PLETAK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Egor Pleshivtsev (`KXITFMATCH-26OCT06PLETAK-PLE`) | 0.49 / 0.64 (52) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yua Taka (`KXITFMATCH-26OCT06PLETAK-TAK`) | 0.27 / 0.41 (43) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Taiyo Yamanaka vs Wishaya Trongcharoenchaikul -- M25 Luan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06YAMTRO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wishaya Trongcharoenchaikul (`KXITFMATCH-26OCT06YAMTRO-TRO`) | 0.23 / 0.27 (3) | 25.0% | -- | -- | -- [-----] | 27.6% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Taiyo Yamanaka (`KXITFMATCH-26OCT06YAMTRO-YAM`) | 0.72 / 0.75 (1) | 73.5% | -- | -- | -- [-----] | 72.4% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Holger Rune vs Daniel Altmaier -- ATP Shanghai R128

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-07 08:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-07 07:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:127157:208029:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Altmaier (`KXATPMATCH-26OCT06RUNALT-ALT`) | 0.30 / 0.31 (24) | 30.5% | 22.5% | 18.5% | 18.5% [16.6%-22.0%] | -- | -- | -- | -- | PASS | -8.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Holger Rune (`KXATPMATCH-26OCT06RUNALT-RUN`) | 0.69 / 0.70 (1333) | 69.5% | 77.5% | 81.5% | 81.5% [78.0%-83.4%] | -- | -- | -- | -- | SHADOW_BET | +8.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3078.0, B 5949.0; serve-point win A 67.1%, B 39.0%; Elo A 1980.3, B 1721.2; model uncertainty 0.0269
* Form inputs: days since last match A 5, B 8; matches on record A 444, B 723; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.013, surface_dev_loose +0.016, surface_dev_tight -0.017
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT06RUNALT-ALT2` Will Daniel Altmaier win at least 1.5 more games than Holger Rune?: 0.25/0.28 mid 26.5%, model 17.1% (projection_v2.0 (prediction ledger)) -- gap -9.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06RUNALT-28` Over 27.5 games: 0.23/0.27 mid 25.0%, model 34.2% (projection_v2.0 (prediction ledger)) -- gap +9.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06RUNALT-23` Over 22.5 games: 0.44/0.45 mid 44.5%, model 53.2% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06RUNALT-RUN21` Will Holger Rune win the Holger Rune vs Daniel Altmaier match by a set score of 2-1?: 0.21/0.24 mid 22.5%, model 29.5% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06RUNALT-ALT20` Will Daniel Altmaier win the Holger Rune vs Daniel Altmaier match by a set score of 2-0?: 0.15/0.17 mid 16.0%, model 9.4% (projection_v2.0 (prediction ledger)) -- gap -6.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06RUNALT-18` Over 17.5 games: 0.84/0.85 mid 84.5%, model 89.9% (projection_v2.0 (prediction ledger)) -- gap +5.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06RUNALT-RUN7` Will Holger Rune win at least 6.5 more games than Daniel Altmaier?: 0.14/0.18 mid 16.0%, model 11.7% (projection_v2.0 (prediction ledger)) -- gap -4.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT06RUNALT-1-RUN` Will Holger Rune win set 1 in the Holger Rune vs Daniel Altmaier match: 0.64/0.66 mid 65.0%, model 69.3% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06RUNALT-1-ALT` Will Daniel Altmaier win set 1 in the Holger Rune vs Daniel Altmaier match: 0.33/0.36 mid 34.5%, model 30.7% (projection_v2.0 (prediction ledger)) -- gap -3.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06RUNALT-2-ALT` Will Daniel Altmaier win set 2 in the Holger Rune vs Daniel Altmaier match: 0.33/0.36 mid 34.5%, model 30.7% (projection_v2.0 (prediction ledger)) -- gap -3.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06RUNALT-2-RUN` Will Holger Rune win set 2 in the Holger Rune vs Daniel Altmaier match: 0.64/0.67 mid 65.5%, model 69.3% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT06RUNALT-RUN4` Will Holger Rune win at least 3.5 more games than Daniel Altmaier?: 0.48/0.49 mid 48.5%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap +3.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06RUNALT-RUN20` Will Holger Rune win the Holger Rune vs Daniel Altmaier match by a set score of 2-0?: 0.45/0.46 mid 45.5%, model 48.0% (projection_v2.0 (prediction ledger)) -- gap +2.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06RUNALT-ALT21` Will Daniel Altmaier win the Holger Rune vs Daniel Altmaier match by a set score of 2-1?: 0.13/0.16 mid 14.5%, model 13.1% (projection_v2.0 (prediction ledger)) -- gap -1.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Quentin Halys vs Coleman Wong -- ATP Shanghai R128

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-07 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-07 08:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-07 07:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-07T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT07HALWON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Quentin Halys (`KXATPMATCH-26OCT07HALWON-HAL`) | 0.51 / 0.55 (138) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Coleman Wong (`KXATPMATCH-26OCT07HALWON-WON`) | 0.44 / 0.48 (136) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ava Beck vs Himari Sato -- W35 Wagga Wagga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06BECSAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ava Beck (`KXITFWMATCH-26OCT06BECSAT-BEC`) | 0.59 / 0.61 (85) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Himari Sato (`KXITFWMATCH-26OCT06BECSAT-SAT`) | 0.38 / 0.40 (10) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ha Eum Lee vs Yanan Hou -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06LEEHOU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yanan Hou (`KXITFWMATCH-26OCT06LEEHOU-HOU`) | 0.17 / 0.27 (69) | 22.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ha Eum Lee (`KXITFWMATCH-26OCT06LEEHOU-LEE`) | 0.65 / 0.83 (3409) | 74.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chihiro Muramatsu vs Naho Sato -- W35 Wagga Wagga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06MURSAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chihiro Muramatsu (`KXITFWMATCH-26OCT06MURSAT-MUR`) | 0.09 / 0.12 (468) | 10.5% | -- | -- | -- [-----] | 12.4% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Naho Sato (`KXITFWMATCH-26OCT06MURSAT-SAT`) | 0.87 / 0.91 (231) | 89.0% | -- | -- | -- [-----] | 87.6% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mio Mushika vs Remika Ohashi -- W35 Wagga Wagga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06MUSOHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mio Mushika (`KXITFWMATCH-26OCT06MUSOHA-MUS`) | 0.59 / 0.80 (22) | 69.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Remika Ohashi (`KXITFWMATCH-26OCT06MUSOHA-OHA`) | 0.19 / 0.28 (35) | 23.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Varvara Panshina vs Liuyan An -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06PANANX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liuyan An (`KXITFWMATCH-26OCT06PANANX-ANX`) | 0.03 / 0.07 (356) | 5.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Varvara Panshina (`KXITFWMATCH-26OCT06PANANX-PAN`) | 0.89 / 0.95 (50) | 92.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gurmanat Kaur Sandhu vs Olga Danilova -- W35 Wagga Wagga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06SANDAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Olga Danilova (`KXITFWMATCH-26OCT06SANDAN-DAN`) | 0.66 / 0.78 (3208) | 72.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gurmanat Kaur Sandhu (`KXITFWMATCH-26OCT06SANDAN-SAN`) | 0.15 / 0.25 (26) | 20.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marianna Shikhanova vs Honori Koyama -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06SHIKOY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Honori Koyama (`KXITFWMATCH-26OCT06SHIKOY-KOY`) | 0.40 / 0.46 (46) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marianna Shikhanova (`KXITFWMATCH-26OCT06SHIKOY-SHI`) | 0.54 / 0.58 (150) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anna Yang vs Darja Suvirdjonkova -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06YANSUV:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Darja Suvirdjonkova (`KXITFWMATCH-26OCT06YANSUV-SUV`) | 0.18 / 0.58 (61) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anna Yang (`KXITFWMATCH-26OCT06YANSUV-YAN`) | 0.23 / 0.62 (67) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elise Mertens / Diana Shnaider vs Tereza Mihalikova / Olivia Nicholls -- WTA Beijing R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-07 14:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-07 09:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-07 08:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-07T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07MERSHNMIHNIC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elise Mertens / Diana Shnaider (`KXWTADOUBLES-26OCT07MERSHNMIHNIC-MERSHN`) | 0.69 / 0.74 (274) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tereza Mihalikova / Olivia Nicholls (`KXWTADOUBLES-26OCT07MERSHNMIHNIC-MIHNIC`) | 0.26 / 0.29 (19) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Isaac Becroft vs Mert Alkaya -- M25 Luan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06BECALK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mert Alkaya (`KXITFMATCH-26OCT06BECALK-ALK`) | 0.53 / 0.57 (2) | 55.0% | -- | -- | -- [-----] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Isaac Becroft (`KXITFMATCH-26OCT06BECALK-BEC`) | 0.41 / 0.45 (2) | 43.0% | -- | -- | -- [-----] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yan Cheng CHEN vs Kuan-Shou Chen -- M25 Luan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06CHECHE2:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yan Cheng CHEN (`KXITFMATCH-26OCT06CHECHE2-CHE`) | 0.11 / 0.13 (1150) | 12.0% | -- | -- | -- [-----] | 14.4% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kuan-Shou Chen (`KXITFMATCH-26OCT06CHECHE2-CHE2`) | 0.86 / 0.89 (3715) | 87.5% | -- | -- | -- [-----] | 85.6% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kuan-Yi Lee vs Dong Ju Kim -- M25 Luan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06LEEKIM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dong Ju Kim (`KXITFMATCH-26OCT06LEEKIM-KIM`) | 0.43 / 0.45 (2585) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kuan-Yi Lee (`KXITFMATCH-26OCT06LEEKIM-LEE`) | 0.52 / 0.57 (4010) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xin Zhou vs Jordan Chiu -- M25 Luan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06ZHOCHI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jordan Chiu (`KXITFMATCH-26OCT06ZHOCHI-CHI`) | 0.49 / 0.64 (52) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xin Zhou (`KXITFMATCH-26OCT06ZHOCHI-ZHO`) | 0.27 / 0.38 (40) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gaeul Jang vs Kunwei Wang -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 09:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06JANWAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gaeul Jang (`KXITFWMATCH-26OCT06JANWAN-JAN`) | 0.74 / 0.95 (50) | 84.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kunwei Wang (`KXITFWMATCH-26OCT06JANWAN-WAN`) | 0.03 / 0.25 (34) | 14.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Satima Toregen vs Yuhan Wang -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 09:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06TORWAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Satima Toregen (`KXITFWMATCH-26OCT06TORWAN-TOR`) | 0.03 / 0.07 (26) | 5.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yuhan Wang (`KXITFWMATCH-26OCT06TORWAN-WAN`) | 0.28 / 0.95 (50) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Guyu Xu vs Jiaqi Wang -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 09:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06XUXWAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jiaqi Wang (`KXITFWMATCH-26OCT06XUXWAN-WAN`) | 0.34 / 0.95 (50) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Guyu Xu (`KXITFWMATCH-26OCT06XUXWAN-XUX`) | 0.03 / 0.07 (26) | 5.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alina Yuneva vs Yingqun Sun -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 09:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06YUNSUN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yingqun Sun (`KXITFWMATCH-26OCT06YUNSUN-SUN`) | 0.91 / 0.95 (50) | 93.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alina Yuneva (`KXITFWMATCH-26OCT06YUNSUN-YUN`) | 0.04 / 0.06 (16) | 5.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yibing Wu vs Michael Zheng -- ATP Shanghai R128

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-07 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-07 10:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-07 09:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-07T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT07YIBZHE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yibing Wu (`KXATPMATCH-26OCT07YIBZHE-YIB`) | 0.47 / 0.50 (485) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Michael Zheng (`KXATPMATCH-26OCT07YIBZHE-ZHE`) | 0.50 / 0.53 (573) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Alina Charaeva vs Qinwen Zheng -- WTA Beijing R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 06:00Z
* Current expected start: 2026-10-07 11:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-07 10:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1740_MIN

WTA (MASTERS_1000) · Hard · scheduled 2026-10-06T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:221012:221406:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alina Charaeva (`KXWTAMATCH-26OCT05CHAZHE-CHA`) | 0.23 / 0.24 (11187) | 23.5% | 24.7% | 17.3% | 16.7% [15.5%-19.8%] | -- | -- | -- | -- | PASS | +1.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Qinwen Zheng (`KXWTAMATCH-26OCT05CHAZHE-ZHE`) | 0.76 / 0.77 (20810) | 76.5% | 75.3% | 82.7% | 83.4% [80.2%-84.5%] | -- | -- | -- | -- | SHADOW_BET | -1.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3668.0, B 3151.0; serve-point win A 57.4%, B 37.3%; Elo A 1769.5, B 2067.0; model uncertainty 0.0218
* Form inputs: days since last match A 1, B 1; matches on record A 328, B 376; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.006, surface_pool_high -0.006, surface_dev_loose -0.002, surface_dev_tight +0.002
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT05CHAZHE-22` Over 21.5 games: 0.44/0.45 mid 44.5%, model 58.4% (projection_v2.0 (prediction ledger)) -- gap +13.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT05CHAZHE-27` Over 26.5 games: 0.23/0.27 mid 25.0%, model 35.9% (projection_v2.0 (prediction ledger)) -- gap +10.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT05CHAZHE-17` Over 16.5 games: 0.82/0.87 mid 84.5%, model 93.0% (projection_v2.0 (prediction ledger)) -- gap +8.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT05CHAZHE-2-ZHE` Will Qinwen Zheng win set 2 in the Alina Charaeva vs Qinwen Zheng match: 0.71/0.73 mid 72.0%, model 67.6% (projection_v2.0 (prediction ledger)) -- gap -4.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT05CHAZHE-2-CHA` Will Alina Charaeva win set 2 in the Alina Charaeva vs Qinwen Zheng match: 0.27/0.30 mid 28.5%, model 32.4% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT05CHAZHE-1-CHA` Will Alina Charaeva win set 1 in the Alina Charaeva vs Qinwen Zheng match: 0.29/0.30 mid 29.5%, model 32.4% (projection_v2.0 (prediction ledger)) -- gap +2.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT05CHAZHE-1-ZHE` Will Qinwen Zheng win set 1 in the Alina Charaeva vs Qinwen Zheng match: 0.70/0.71 mid 70.5%, model 67.6% (projection_v2.0 (prediction ledger)) -- gap -2.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Xirui Han vs James Van Herzeele -- M25 Luan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07HANVAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xirui Han (`KXITFMATCH-26OCT07HANVAN-HAN`) | 0.24 / 0.36 (40) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| James Van Herzeele (`KXITFMATCH-26OCT07HANVAN-VAN`) | 0.56 / 0.68 (17) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tsung-Hao Huang vs Ko Suzuki -- M25 Luan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07HUASUZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tsung-Hao Huang (`KXITFMATCH-26OCT07HUASUZ-HUA`) | 0.64 / 0.79 (52) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ko Suzuki (`KXITFMATCH-26OCT07HUASUZ-SUZ`) | 0.16 / 0.26 (26) | 21.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sasikumar Mukund vs Boris Butulija -- M25 Luan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07MUKBUT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Boris Butulija (`KXITFMATCH-26OCT07MUKBUT-BUT`) | 0.14 / 0.25 (34) | 19.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sasikumar Mukund (`KXITFMATCH-26OCT07MUKBUT-MUK`) | 0.66 / 0.79 (123) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lingxi Zhao vs Anton Shepp -- M25 Luan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07ZHASHE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anton Shepp (`KXITFMATCH-26OCT07ZHASHE-SHE`) | 0.67 / 0.79 (52) | 73.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lingxi Zhao (`KXITFMATCH-26OCT07ZHASHE-ZHA`) | 0.10 / 0.26 (26) | 18.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## suzuna oigawa vs Jeong Moon -- W15 Islamabad R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07OIGMOO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jeong Moon (`KXITFWMATCH-26OCT07OIGMOO-MOO`) | 0.68 / 0.73 (4151) | 70.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| suzuna oigawa (`KXITFWMATCH-26OCT07OIGMOO-OIG`) | 0.26 / 0.31 (28) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mahin Qureshi vs Wozuko Mdlulwa -- W15 Islamabad R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07QURMDL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wozuko Mdlulwa (`KXITFWMATCH-26OCT07QURMDL-MDL`) | 0.69 / 0.95 (74) | 82.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mahin Qureshi (`KXITFWMATCH-26OCT07QURMDL-QUR`) | 0.04 / 0.09 (70) | 6.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Romisa Romisa Malik vs Abhilasha Bista -- W15 Islamabad R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07ROMBIS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Abhilasha Bista (`KXITFWMATCH-26OCT07ROMBIS-BIS`) | 0.04 / 0.95 (80) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Romisa Romisa Malik (`KXITFWMATCH-26OCT07ROMBIS-ROM`) | 0.03 / 0.95 (80) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofiia Suslova vs Liliya Piskun -- W15 Islamabad R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07SUSPIS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liliya Piskun (`KXITFWMATCH-26OCT07SUSPIS-PIS`) | 0.13 / 0.21 (1) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sofiia Suslova (`KXITFWMATCH-26OCT07SUSPIS-SUS`) | 0.75 / 0.82 (50) | 78.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arthur Fery vs Marin Cilic -- ATP Shanghai R128

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-07 11:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-07 10:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105227:209259:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marin Cilic (`KXATPMATCH-26OCT06FERCIL-CIL`) | 0.38 / 0.39 (4321) | 38.5% | 40.8% | 40.8% | 45.1% [42.7%-51.0%] | -- | -- | -- | -- | WATCH | +2.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Arthur Fery (`KXATPMATCH-26OCT06FERCIL-FER`) | 0.61 / 0.62 (4768) | 61.5% | 59.2% | 59.2% | 54.9% [49.0%-57.3%] | -- | -- | -- | -- | PASS | -2.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4586.0, B 3596.0; serve-point win A 66.6%, B 35.3%; Elo A 1835.4, B 1871.5; model uncertainty 0.0413
* Form inputs: days since last match A 5, B 53; matches on record A 262, B 1112; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.019, surface_dev_loose -0.000, surface_dev_tight +0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT06FERCIL-29` Over 28.5 games: 0.23/0.26 mid 24.5%, model 38.0% (projection_v2.0 (prediction ledger)) -- gap +13.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06FERCIL-24` Over 23.5 games: 0.43/0.44 mid 43.5%, model 55.3% (projection_v2.0 (prediction ledger)) -- gap +11.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT06FERCIL-19` Over 18.5 games: 0.79/0.82 mid 80.5%, model 90.3% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06FERCIL-FER5` Will Arthur Fery win at least 4.5 more games than Marin Cilic?: 0.26/0.28 mid 27.0%, model 19.2% (projection_v2.0 (prediction ledger)) -- gap -7.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06FERCIL-FER20` Will Arthur Fery win the Arthur Fery vs Marin Cilic match by a set score of 2-0?: 0.37/0.40 mid 38.5%, model 31.5% (projection_v2.0 (prediction ledger)) -- gap -7.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06FERCIL-FER21` Will Arthur Fery win the Arthur Fery vs Marin Cilic match by a set score of 2-1?: 0.21/0.24 mid 22.5%, model 27.7% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06FERCIL-CIL21` Will Marin Cilic win the Arthur Fery vs Marin Cilic match by a set score of 2-1?: 0.16/0.19 mid 17.5%, model 21.6% (projection_v2.0 (prediction ledger)) -- gap +4.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06FERCIL-FER2` Will Arthur Fery win at least 1.5 more games than Marin Cilic?: 0.54/0.55 mid 54.5%, model 51.3% (projection_v2.0 (prediction ledger)) -- gap -3.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT06FERCIL-2-CIL` Will Marin Cilic win set 2 in the Arthur Fery vs Marin Cilic match: 0.40/0.43 mid 41.5%, model 43.9% (projection_v2.0 (prediction ledger)) -- gap +2.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06FERCIL-2-FER` Will Arthur Fery win set 2 in the Arthur Fery vs Marin Cilic match: 0.57/0.60 mid 58.5%, model 56.1% (projection_v2.0 (prediction ledger)) -- gap -2.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT06FERCIL-1-CIL` Will Marin Cilic win set 1 in the Arthur Fery vs Marin Cilic match: 0.41/0.43 mid 42.0%, model 43.9% (projection_v2.0 (prediction ledger)) -- gap +1.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT06FERCIL-CIL20` Will Marin Cilic win the Arthur Fery vs Marin Cilic match by a set score of 2-0?: 0.20/0.22 mid 21.0%, model 19.2% (projection_v2.0 (prediction ledger)) -- gap -1.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT06FERCIL-CIL2` Will Marin Cilic win at least 1.5 more games than Arthur Fery?: 0.33/0.36 mid 34.5%, model 33.3% (projection_v2.0 (prediction ledger)) -- gap -1.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT06FERCIL-1-FER` Will Arthur Fery win set 1 in the Arthur Fery vs Marin Cilic match: 0.56/0.57 mid 56.5%, model 56.1% (projection_v2.0 (prediction ledger)) -- gap -0.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Jack Bruce-Smith vs Casey Hoole -- M25 Darwin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07BRUHOO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jack Bruce-Smith (`KXITFMATCH-26OCT07BRUHOO-BRU`) | 0.05 / 0.35 (39) | 20.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Casey Hoole (`KXITFMATCH-26OCT07BRUHOO-HOO`) | 0.61 / 0.88 (0) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jake Delaney vs Harrison Satara -- M25 Darwin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07DELSAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jake Delaney (`KXITFMATCH-26OCT07DELSAT-DEL`) | 0.82 / 0.87 (439) | 84.5% | -- | -- | -- [-----] | 83.0% | -- | 83.0% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Harrison Satara (`KXITFMATCH-26OCT07DELSAT-SAT`) | 0.13 / 0.16 (226) | 14.5% | -- | -- | -- [-----] | 17.0% | -- | 17.0% | KALSHI_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Darcy Nicholls vs Tai Leonard Sach -- M25 Darwin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07NICSAC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Darcy Nicholls (`KXITFMATCH-26OCT07NICSAC-NIC`) | 0.03 / 0.47 (47) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tai Leonard Sach (`KXITFMATCH-26OCT07NICSAC-SAC`) | 0.52 / 0.89 (0) | 70.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Wihan Van Der Merwe vs Adrian Arcon -- M25 Darwin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07VANARC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Arcon (`KXITFMATCH-26OCT07VANARC-ARC`) | 0.03 / 0.67 (0) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Wihan Van Der Merwe (`KXITFMATCH-26OCT07VANARC-VAN`) | 0.28 / 0.89 (0) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Han / Yang vs Hou / Wang -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07HANYANHOUWAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Han / Yang (`KXITFWDOUBLES-26OCT07HANYANHOUWAN-HANYAN`) | 0.06 / 0.90 (50) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hou / Wang (`KXITFWDOUBLES-26OCT07HANYANHOUWAN-HOUWAN`) | 0.09 / 0.90 (50) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Ren / Tang vs Chen / Li -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07RENTANCHELIX:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chen / Li (`KXITFWDOUBLES-26OCT07RENTANCHELIX-CHELIX`) | 0.06 / 0.59 (60) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ren / Tang (`KXITFWDOUBLES-26OCT07RENTANCHELIX-RENTAN`) | 0.06 / 0.65 (73) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Dong / LIU vs KUAN LAI / ZENG -- M25 Luan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07DONLIUKUAZEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dong / LIU (`KXITFDOUBLES-26OCT07DONLIUKUAZEN-DONLIU`) | 0.06 / 0.94 (23) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| KUAN LAI / ZENG (`KXITFDOUBLES-26OCT07DONLIUKUAZEN-KUAZEN`) | 0.08 / 0.94 (23) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Pleshivtsev / Tomida vs Barsukov / Ehrenschneider -- M25 Luan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07PLETOMBAREHR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barsukov / Ehrenschneider (`KXITFDOUBLES-26OCT07PLETOMBAREHR-BAREHR`) | 0.09 / 0.83 (147) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pleshivtsev / Tomida (`KXITFDOUBLES-26OCT07PLETOMBAREHR-PLETOM`) | 0.06 / 0.38 (40) | 22.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Maxim Shin vs Petr Bar Biryukov -- M25 Luan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07SHIBAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Petr Bar Biryukov (`KXITFMATCH-26OCT07SHIBAR-BAR`) | 0.73 / 0.89 (0) | 81.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maxim Shin (`KXITFMATCH-26OCT07SHIBAR-SHI`) | 0.03 / 0.21 (32) | 12.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tang / Zhao vs Jin / Sun -- M25 Luan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-07T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07TANZHAJINSUN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jin / Sun (`KXITFDOUBLES-26OCT07TANZHAJINSUN-JINSUN`) | 0.06 / 0.75 (100) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tang / Zhao (`KXITFDOUBLES-26OCT07TANZHAJINSUN-TANZHA`) | 0.06 / 0.48 (48) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Elena Jamshidi vs Meheq Khokhar -- W15 Islamabad R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07JAMKHO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Jamshidi (`KXITFWMATCH-26OCT07JAMKHO-JAM`) | 0.04 / 0.95 (80) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Meheq Khokhar (`KXITFWMATCH-26OCT07JAMKHO-KHO`) | 0.03 / 0.95 (50) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anna Simkina vs Sevil Yuldasheva -- W15 Islamabad R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07SIMYUL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Simkina (`KXITFWMATCH-26OCT07SIMYUL-SIM`) | 0.04 / 0.95 (50) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sevil Yuldasheva (`KXITFWMATCH-26OCT07SIMYUL-YUL`) | 0.03 / 0.95 (50) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## HAJRA SOHAIL vs Anastasiya Kuparev -- W15 Islamabad R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07SOHKUP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasiya Kuparev (`KXITFWMATCH-26OCT07SOHKUP-KUP`) | 0.04 / 0.95 (50) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| HAJRA SOHAIL (`KXITFWMATCH-26OCT07SOHKUP-SOH`) | 0.03 / 0.95 (50) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ann Li vs Elina Svitolina -- WTA Beijing R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-07 06:00Z
* Current expected start: 2026-10-07 12:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-06 15:25Z
* Recommended handicap-by time: 2026-10-07 11:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+390_MIN

WTA (MASTERS_1000) · Hard · scheduled 2026-10-07T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202494:215983:2026-10-07`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ann Li (`KXWTAMATCH-26OCT06ANNSVI-ANN`) | 0.24 / 0.25 (1248) | 24.5% | 27.6% | 26.2% | 25.4% [22.4%-26.6%] | 25.5% | -- | 25.5% | MODEL_LONE_OUTLIER | PASS | +3.0 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Elina Svitolina (`KXWTAMATCH-26OCT06ANNSVI-SVI`) | 0.75 / 0.76 (33549) | 75.5% | 72.5% | 73.8% | 74.7% [73.4%-77.6%] | 74.5% | -- | 74.5% | MODEL_LONE_OUTLIER | PASS | -3.0 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4567.0, B 4144.0; serve-point win A 56.8%, B 38.6%; Elo A 1892.1, B 2113.3; model uncertainty 0.021
* Form inputs: days since last match A 1, B 1; matches on record A 466, B 853; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.008, surface_dev_loose -0.004, surface_dev_tight -0.001
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT06ANNSVI-21` Over 20.5 games: 0.51/0.52 mid 51.5%, model 64.5% (projection_v2.0 (prediction ledger)) -- gap +13.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT06ANNSVI-26` Over 25.5 games: 0.27/0.32 mid 29.5%, model 41.4% (projection_v2.0 (prediction ledger)) -- gap +11.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT06ANNSVI-2-SVI` Will Elina Svitolina win set 2 in the Ann Li vs Elina Svitolina match: 0.71/0.72 mid 71.5%, model 65.5% (projection_v2.0 (prediction ledger)) -- gap -6.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT06ANNSVI-1-ANN` Will Ann Li win set 1 in the Ann Li vs Elina Svitolina match: 0.29/0.30 mid 29.5%, model 34.5% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT06ANNSVI-2-ANN` Will Ann Li win set 2 in the Ann Li vs Elina Svitolina match: 0.28/0.31 mid 29.5%, model 34.5% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT06ANNSVI-1-SVI` Will Elina Svitolina win set 1 in the Ann Li vs Elina Svitolina match: 0.69/0.71 mid 70.0%, model 65.5% (projection_v2.0 (prediction ledger)) -- gap -4.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT06ANNSVI-16` Over 15.5 games: 0.91/0.95 mid 93.0%, model 96.9% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE

## Nikolas Baker vs Stefan Vujic -- M25 Darwin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07BAKVUJ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikolas Baker (`KXITFMATCH-26OCT07BAKVUJ-BAK`) | 0.19 / 0.44 (45) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stefan Vujic (`KXITFMATCH-26OCT07BAKVUJ-VUJ`) | 0.50 / 0.73 (0) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Joshua Charlton vs Arjun Mehrotra -- M25 Darwin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07CHAMEH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joshua Charlton (`KXITFMATCH-26OCT07CHAMEH-CHA`) | 0.41 / 0.86 (5) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arjun Mehrotra (`KXITFMATCH-26OCT07CHAMEH-MEH`) | 0.11 / 0.51 (0) | 31.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Herman Hoeyeraal vs Chen Dong -- M25 Darwin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07HOEDON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chen Dong (`KXITFMATCH-26OCT07HOEDON-DON`) | 0.34 / 0.40 (42) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Herman Hoeyeraal (`KXITFMATCH-26OCT07HOEDON-HOE`) | 0.59 / 0.64 (34) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zaharije-Zak Talic vs Jesse Delaney -- M25 Darwin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07TALDEL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jesse Delaney (`KXITFMATCH-26OCT07TALDEL-DEL`) | 0.33 / 0.89 (0) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Zaharije-Zak Talic (`KXITFMATCH-26OCT07TALDEL-TAL`) | 0.03 / 0.83 (100) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lamis Alhussein Abdel Aziz vs Vanesa Salaiova -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07ALHSAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lamis Alhussein Abdel Aziz (`KXITFWMATCH-26OCT07ALHSAL-ALH`) | 0.04 / 0.95 (50) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vanesa Salaiova (`KXITFWMATCH-26OCT07ALHSAL-SAL`) | 0.03 / 0.95 (50) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jinte Eve De boer vs Anna Kashyrina -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07DEBKAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jinte Eve De boer (`KXITFWMATCH-26OCT07DEBKAS-DEB`) | 0.04 / 0.95 (50) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anna Kashyrina (`KXITFWMATCH-26OCT07DEBKAS-KAS`) | 0.03 / 0.95 (50) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alisa Vasileva vs Sarafina Olivia Hansen -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07VASHAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sarafina Olivia Hansen (`KXITFWMATCH-26OCT07VASHAN-HAN`) | 0.04 / 0.95 (50) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alisa Vasileva (`KXITFWMATCH-26OCT07VASHAN-VAS`) | 0.03 / 0.95 (50) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mia Wainwright vs Sveva Pieroni -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07WAIPIE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sveva Pieroni (`KXITFWMATCH-26OCT07WAIPIE-PIE`) | 0.04 / 0.95 (50) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mia Wainwright (`KXITFWMATCH-26OCT07WAIPIE-WAI`) | 0.03 / 0.95 (80) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cezar Stefan Bentzel vs Nicolas Garcia Longo -- M15 Burgas R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07BENGAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cezar Stefan Bentzel (`KXITFMATCH-26OCT07BENGAR-BEN`) | 0.20 / 0.69 (0) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nicolas Garcia Longo (`KXITFMATCH-26OCT07BENGAR-GAR`) | 0.03 / 0.71 (50) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Melios Efstathiou vs Finn Murgett -- M15 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07EFSMUR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Melios Efstathiou (`KXITFMATCH-26OCT07EFSMUR-EFS`) | 0.05 / 0.68 (3) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Finn Murgett (`KXITFMATCH-26OCT07EFSMUR-MUR`) | 0.09 / 0.90 (5) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amr Elsayed vs Zian Vanderstappen -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07ELSVAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amr Elsayed (`KXITFMATCH-26OCT07ELSVAN-ELS`) | 0.38 / 0.89 (0) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Zian Vanderstappen (`KXITFMATCH-26OCT07ELSVAN-VAN`) | 0.03 / 0.50 (50) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Odysseas Geladaris vs James McGloughlin -- M15 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07GELMCG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Odysseas Geladaris (`KXITFMATCH-26OCT07GELMCG-GEL`) | 0.05 / 0.89 (0) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| James McGloughlin (`KXITFMATCH-26OCT07GELMCG-MCG`) | 0.03 / 0.90 (5) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Karim Ibrahim vs Ferdinand Livet Novkirichka -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07IBRLIV:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karim Ibrahim (`KXITFMATCH-26OCT07IBRLIV-IBR`) | 0.26 / 0.66 (0) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ferdinand Livet Novkirichka (`KXITFMATCH-26OCT07IBRLIV-LIV`) | 0.30 / 0.70 (10) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jan Kupcic vs Noah Lopez -- M15 Burgas R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07KUPLOP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jan Kupcic (`KXITFMATCH-26OCT07KUPLOP-KUP`) | 0.31 / 0.56 (1) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Noah Lopez (`KXITFMATCH-26OCT07KUPLOP-LOP`) | 0.20 / 0.55 (0) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniel Michalski vs Lorenzo Bocchi -- M25 Santa Margherita di Pula R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07MICBOC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Bocchi (`KXITFMATCH-26OCT07MICBOC-BOC`) | 0.11 / 0.28 (35) | 19.5% | -- | -- | -- [-----] | 13.3% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daniel Michalski (`KXITFMATCH-26OCT07MICBOC-MIC`) | 0.85 / 0.90 (5) | 87.5% | -- | -- | -- [-----] | 86.7% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Iannis Miletich vs Yoan Naydenov -- M15 Burgas R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07MILNAY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iannis Miletich (`KXITFMATCH-26OCT07MILNAY-MIL`) | 0.42 / 0.89 (0) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yoan Naydenov (`KXITFMATCH-26OCT07MILNAY-NAY`) | 0.03 / 0.48 (0) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Giovanni Oradini vs Marco Furlanetto -- M25 Santa Margherita di Pula R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07ORAFUR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marco Furlanetto (`KXITFMATCH-26OCT07ORAFUR-FUR`) | 0.05 / 0.89 (8) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Giovanni Oradini (`KXITFMATCH-26OCT07ORAFUR-ORA`) | 0.06 / 0.90 (5) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jadon Price vs Dimitar Kisimov -- M25 Santa Margherita di Pula R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07PRIKIS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dimitar Kisimov (`KXITFMATCH-26OCT07PRIKIS-KIS`) | 0.05 / 0.89 (0) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jadon Price (`KXITFMATCH-26OCT07PRIKIS-PRI`) | 0.03 / 0.90 (5) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Finn Reilly vs Niklas Waldner -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07REIWAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Finn Reilly (`KXITFMATCH-26OCT07REIWAL-REI`) | 0.05 / 0.82 (50) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Niklas Waldner (`KXITFMATCH-26OCT07REIWAL-WAL`) | 0.23 / 0.90 (5) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mathieu Scaglia vs Henri Haupt -- M15 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07SCAHAU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Henri Haupt (`KXITFMATCH-26OCT07SCAHAU-HAU`) | 0.05 / 0.39 (50) | 22.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mathieu Scaglia (`KXITFMATCH-26OCT07SCAHAU-SCA`) | 0.50 / 0.90 (5) | 70.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Robert Strombachs vs Jan Werblinski -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07STRWER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robert Strombachs (`KXITFMATCH-26OCT07STRWER-STR`) | 0.05 / 0.90 (5) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jan Werblinski (`KXITFMATCH-26OCT07STRWER-WER`) | 0.06 / 0.90 (5) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amit Vales vs Jiri Cizek -- M15 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07VALCIZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jiri Cizek (`KXITFMATCH-26OCT07VALCIZ-CIZ`) | 0.15 / 0.47 (50) | 31.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Amit Vales (`KXITFMATCH-26OCT07VALCIZ-VAL`) | 0.39 / 0.78 (4) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Martin VAN DER MEERSCHEN vs Gabriele Crivellaro -- M25 Santa Margherita di Pula R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07VANCRI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriele Crivellaro (`KXITFMATCH-26OCT07VANCRI-CRI`) | 0.32 / 0.42 (43) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Martin VAN DER MEERSCHEN (`KXITFMATCH-26OCT07VANCRI-VAN`) | 0.61 / 0.67 (57) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexander Weis vs Fausto Tabacco -- M25 Santa Margherita di Pula R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT07WEITAB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fausto Tabacco (`KXITFMATCH-26OCT07WEITAB-TAB`) | 0.43 / 0.49 (0) | 46.0% | -- | -- | -- [-----] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander Weis (`KXITFMATCH-26OCT07WEITAB-WEI`) | 0.50 / 0.54 (150) | 52.0% | -- | -- | -- [-----] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ilinca Dalina Amariei vs Nikol Ivanova -- W50 Burgas R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07AMAIVA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ilinca Dalina Amariei (`KXITFWMATCH-26OCT07AMAIVA-AMA`) | 0.22 / 0.95 (50) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nikol Ivanova (`KXITFWMATCH-26OCT07AMAIVA-IVA`) | 0.03 / 0.46 (96) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jessica Bertoldo vs Elina Nepliy -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07BERNEP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jessica Bertoldo (`KXITFWMATCH-26OCT07BERNEP-BER`) | 0.04 / 0.57 (2) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Elina Nepliy (`KXITFWMATCH-26OCT07BERNEP-NEP`) | 0.23 / 0.95 (50) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kateryna Diatlova vs Milana Maslenkova -- W15 Chisinau R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07DIAMAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kateryna Diatlova (`KXITFWMATCH-26OCT07DIAMAS-DIA`) | 0.23 / 0.95 (50) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Milana Maslenkova (`KXITFWMATCH-26OCT07DIAMAS-MAS`) | 0.03 / 0.52 (150) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Delia Gaillard vs Felitsata Dorofeeva-Rybas -- W15 Chisinau R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07GAIDOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felitsata Dorofeeva-Rybas (`KXITFWMATCH-26OCT07GAIDOR-DOR`) | 0.06 / 0.95 (50) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Delia Gaillard (`KXITFWMATCH-26OCT07GAIDOR-GAI`) | 0.03 / 0.94 (50) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Romina Hincu vs Sophia Ksandinov -- W15 Chisinau R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07HINKSA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Romina Hincu (`KXITFWMATCH-26OCT07HINKSA-HIN`) | 0.04 / 0.94 (50) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sophia Ksandinov (`KXITFWMATCH-26OCT07HINKSA-KSA`) | 0.04 / 0.95 (50) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Laura Mair vs Jazmin Ortenzi -- W50 Burgas R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07MAIORT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Laura Mair (`KXITFWMATCH-26OCT07MAIORT-MAI`) | 0.04 / 0.25 (34) | 14.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jazmin Ortenzi (`KXITFWMATCH-26OCT07MAIORT-ORT`) | 0.77 / 0.86 (97) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Martha MATOULA vs Tilwith Di Girolami -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07MATDIG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tilwith Di Girolami (`KXITFWMATCH-26OCT07MATDIG-DIG`) | 0.05 / 0.82 (26) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Martha MATOULA (`KXITFWMATCH-26OCT07MATDIG-MAT`) | 0.04 / 0.94 (25) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maria Mikhailova vs Melissa Boyden -- W15 Chisinau R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07MIKBOY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Melissa Boyden (`KXITFWMATCH-26OCT07MIKBOY-BOY`) | 0.51 / 0.60 (59) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maria Mikhailova (`KXITFWMATCH-26OCT07MIKBOY-MIK`) | 0.38 / 0.45 (45) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Rocchetti vs Lisa Zaar -- W35 Santa Margherita di Pula R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07ROCZAA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Rocchetti (`KXITFWMATCH-26OCT07ROCZAA-ROC`) | 0.13 / 0.31 (37) | 22.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lisa Zaar (`KXITFWMATCH-26OCT07ROCZAA-ZAA`) | 0.80 / 0.87 (97) | 83.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jennifer Ruggeri vs Ani Amiraghyan -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07RUGAMI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ani Amiraghyan (`KXITFWMATCH-26OCT07RUGAMI-AMI`) | 0.05 / 0.68 (37) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jennifer Ruggeri (`KXITFWMATCH-26OCT07RUGAMI-RUG`) | 0.17 / 0.94 (25) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anastasiia Sobolieva vs Galena Krastenova -- W50 Burgas R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07SOBKRA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Galena Krastenova (`KXITFWMATCH-26OCT07SOBKRA-KRA`) | 0.04 / 0.95 (50) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anastasiia Sobolieva (`KXITFWMATCH-26OCT07SOBKRA-SOB`) | 0.03 / 0.95 (50) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eva Marie Voracek vs Cristiana Nicoleta Todoni -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07VORTOD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cristiana Nicoleta Todoni (`KXITFWMATCH-26OCT07VORTOD-TOD`) | 0.14 / 0.94 (13) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eva Marie Voracek (`KXITFWMATCH-26OCT07VORTOD-VOR`) | 0.04 / 0.65 (1) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Camilla Zanolini vs Giorgia Pedone -- W35 Santa Margherita di Pula R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-07 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-07T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT07ZANPED:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giorgia Pedone (`KXITFWMATCH-26OCT07ZANPED-PED`) | 0.73 / 0.79 (34) | 76.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Camilla Zanolini (`KXITFWMATCH-26OCT07ZANPED-ZAN`) | 0.14 / 0.29 (36) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
