# ASSISTED SLATE -- 2026-10-12T05:31Z (`SL-20261012T053148Z-2d2081a6`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

231 open matches not seen started, 687 markets. Skipped: {"first_ball_already_observed": 7, "scheduled_start_over_24h_past": 3}. Sources: shadow board 2026-10-12T01:44:46.740207+00:00, Model 4 2026-10-12T01:45:04.378010+00:00, Gen-1 ledger 2026-10-12T01:44:43.144849+00:00, external 2026-10-12T05:14:46.340014+00:00, capture 20261012T051226Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-10-12 05:56Z**
* Recommended RUN TENNIS time: **2026-10-12 05:11Z**  (**OVERDUE -- run now**)
* Final price/status check time: **2026-10-12 05:46Z**
* Number of matches in window: 3 (Jasmine Paolini vs Sara Bejlek, Mananchaya Sawangkaew vs Magdalena Frech, Maria Sakkari vs Donna Vekic)

* **17 main-tour match(es) have NO verified start status** (START_UNKNOWN, STATUS_AMBIGUOUS): BET blocked until a live status check.

Slate built 2026-10-12T05:31Z. Refresh due by: 2026-10-12 05:11Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 38, "HIGH_REVIEW": 73, "NORMAL": 282, "REVIEW": 56, "UNPRICED": 238}; match winners: {"EXTREME": 36, "HIGH_REVIEW": 62, "NORMAL": 132, "REVIEW": 30, "UNPRICED": 202}; quote freshness at build: {"FRESH": 449}.

## Alex de Minaur vs Karen Khachanov -- ATP Shanghai R16

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-12 05:00Z
* Current expected start: 2026-10-12 05:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 04:15Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-13T04:00:00+00:00 as not a valid time; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (MASTERS_1000) · Hard · scheduled 2026-10-12T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111575:200282:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex de Minaur (`KXATPMATCH-26OCT11DEKHA-DE`) | 0.56 / 0.57 (1856) | 56.5% | 60.9% | 59.9% | 61.8% [60.8%-62.7%] | -- | -- | -- | -- | SHADOW_BET | +4.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Karen Khachanov (`KXATPMATCH-26OCT11DEKHA-KHA`) | 0.42 / 0.44 (46538) | 43.0% | 39.1% | 40.1% | 38.2% [37.3%-39.2%] | -- | -- | -- | -- | PASS | -3.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5728.0, B 5265.0; serve-point win A 65.0%, B 37.2%; Elo A 2064.5, B 1944.8; model uncertainty 0.0095
* Form inputs: days since last match A 1, B 1; matches on record A 668, B 750; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight +0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT11DEKHA-KHA2` Will Karen Khachanov win at least 1.5 more games than Alex de Minaur?: 0.35/0.53 mid 44.0%, model 32.0% (projection_v2.0 (prediction ledger)) -- gap -12.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT11DEKHA-19` Over 18.5 games: 0.78/0.83 mid 80.5%, model 87.9% (projection_v2.0 (prediction ledger)) -- gap +7.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT11DEKHA-29` Over 28.5 games: 0.26/0.31 mid 28.5%, model 35.5% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT11DEKHA-24` Over 23.5 games: 0.45/0.49 mid 47.0%, model 53.8% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT11DEKHA-DE21` Will Alex de Minaur win the Alex de Minaur vs Karen Khachanov match by a set score of 2-1?: 0.20/0.24 mid 22.0%, model 28.0% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT11DEKHA-KHA20` Will Karen Khachanov win the Alex de Minaur vs Karen Khachanov match by a set score of 2-0?: 0.22/0.25 mid 23.5%, model 18.2% (projection_v2.0 (prediction ledger)) -- gap -5.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT11DEKHA-1-DE` Will Alex de Minaur win set 1 in the Alex de Minaur vs Karen Khachanov match: 0.50/0.56 mid 53.0%, model 57.3% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT11DEKHA-2-DE` Will Alex de Minaur win set 2 in the Alex de Minaur vs Karen Khachanov match: 0.51/0.56 mid 53.5%, model 57.3% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT11DEKHA-KHA21` Will Karen Khachanov win the Alex de Minaur vs Karen Khachanov match by a set score of 2-1?: 0.17/0.19 mid 18.0%, model 20.9% (projection_v2.0 (prediction ledger)) -- gap +2.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT11DEKHA-2-KHA` Will Karen Khachanov win set 2 in the Alex de Minaur vs Karen Khachanov match: 0.43/0.48 mid 45.5%, model 42.7% (projection_v2.0 (prediction ledger)) -- gap -2.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT11DEKHA-DE2` Will Alex de Minaur win at least 1.5 more games than Karen Khachanov?: 0.49/0.54 mid 51.5%, model 53.5% (projection_v2.0 (prediction ledger)) -- gap +2.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT11DEKHA-DE20` Will Alex de Minaur win the Alex de Minaur vs Karen Khachanov match by a set score of 2-0?: 0.33/0.36 mid 34.5%, model 32.9% (projection_v2.0 (prediction ledger)) -- gap -1.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT11DEKHA-DE5` Will Alex de Minaur win at least 4.5 more games than Karen Khachanov?: 0.21/0.26 mid 23.5%, model 22.7% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT11DEKHA-1-KHA` Will Karen Khachanov win set 1 in the Alex de Minaur vs Karen Khachanov match: 0.42/0.45 mid 43.5%, model 42.7% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Arthur Gea vs Jakub Mensik -- ATP Shanghai R16

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-12 05:00Z
* Current expected start: 2026-10-12 05:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 04:15Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-13T04:00:00+00:00 as not a valid time; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (MASTERS_1000) · Hard · scheduled 2026-10-12T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:210150:210338:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arthur Gea (`KXATPMATCH-26OCT11GEAMEN-GEA`) | 0.37 / 0.38 (50420) | 37.5% | 44.5% | 51.5% | 48.5% [40.9%-50.5%] | -- | -- | -- | -- | PASS | +7.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jakub Mensik (`KXATPMATCH-26OCT11GEAMEN-MEN`) | 0.62 / 0.63 (1874) | 62.5% | 55.5% | 48.5% | 51.5% [49.5%-59.1%] | -- | -- | -- | -- | PASS | -7.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4164.0, B 4875.0; serve-point win A 61.2%, B 37.7%; Elo A 1840.6, B 1909.0; model uncertainty 0.0482
* Form inputs: days since last match A 1, B 714; matches on record A 215, B 169; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.020, surface_dev_tight -0.020
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT11GEAMEN-MEN6` Will Jakub Mensik win at least 5.5 more games than Arthur Gea?: 0.13/0.37 mid 25.0%, model 12.5% (projection_v2.0 (prediction ledger)) -- gap -12.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data POOR
  * `KXATPEXACTMATCH-26OCT11GEAMEN-MEN20` Will Jakub Mensik win the Arthur Gea vs Jakub Mensik match by a set score of 2-0?: 0.37/0.41 mid 39.0%, model 28.8% (projection_v2.0 (prediction ledger)) -- gap -10.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data POOR
  * `KXATPGTOTAL-26OCT11GEAMEN-24` Over 23.5 games: 0.45/0.46 mid 45.5%, model 53.6% (projection_v2.0 (prediction ledger)) -- gap +8.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPGSPREAD-26OCT11GEAMEN-MEN3` Will Jakub Mensik win at least 2.5 more games than Arthur Gea?: 0.49/0.50 mid 49.5%, model 41.6% (projection_v2.0 (prediction ledger)) -- gap -7.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPGSPREAD-26OCT11GEAMEN-GEA2` Will Arthur Gea win at least 1.5 more games than Jakub Mensik?: 0.29/0.33 mid 31.0%, model 37.5% (projection_v2.0 (prediction ledger)) -- gap +6.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPSETWINNER-26OCT11GEAMEN-1-GEA` Will Arthur Gea win set 1 in the Arthur Gea vs Jakub Mensik match: 0.39/0.42 mid 40.5%, model 46.3% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPEXACTMATCH-26OCT11GEAMEN-GEA21` Will Arthur Gea win the Arthur Gea vs Jakub Mensik match by a set score of 2-1?: 0.16/0.19 mid 17.5%, model 23.0% (projection_v2.0 (prediction ledger)) -- gap +5.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPSETWINNER-26OCT11GEAMEN-1-MEN` Will Jakub Mensik win set 1 in the Arthur Gea vs Jakub Mensik match: 0.57/0.61 mid 59.0%, model 53.7% (projection_v2.0 (prediction ledger)) -- gap -5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT11GEAMEN-2-GEA` Will Arthur Gea win set 2 in the Arthur Gea vs Jakub Mensik match: 0.38/0.44 mid 41.0%, model 46.3% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT11GEAMEN-2-MEN` Will Jakub Mensik win set 2 in the Arthur Gea vs Jakub Mensik match: 0.56/0.62 mid 59.0%, model 53.7% (projection_v2.0 (prediction ledger)) -- gap -5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPGTOTAL-26OCT11GEAMEN-29` Over 28.5 games: 0.27/0.33 mid 30.0%, model 33.7% (projection_v2.0 (prediction ledger)) -- gap +3.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPEXACTMATCH-26OCT11GEAMEN-MEN21` Will Jakub Mensik win the Arthur Gea vs Jakub Mensik match by a set score of 2-1?: 0.21/0.25 mid 23.0%, model 26.7% (projection_v2.0 (prediction ledger)) -- gap +3.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPEXACTMATCH-26OCT11GEAMEN-GEA20` Will Arthur Gea win the Arthur Gea vs Jakub Mensik match by a set score of 2-0?: 0.17/0.21 mid 19.0%, model 21.5% (projection_v2.0 (prediction ledger)) -- gap +2.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPGTOTAL-26OCT11GEAMEN-19` Over 18.5 games: 0.81/0.89 mid 85.0%, model 86.0% (projection_v2.0 (prediction ledger)) -- gap +1.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Alexander Zverev vs Alexander Bublik -- ATP Shanghai R16

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-12 05:00Z
* Current expected start: 2026-10-12 05:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 04:15Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-13T04:00:00+00:00 as not a valid time; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (MASTERS_1000) · Hard · scheduled 2026-10-12T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:100644:122330:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Bublik (`KXATPMATCH-26OCT11ZVEBUB-BUB`) | 0.24 / 0.26 (53151) | 25.0% | 22.2% | 19.6% | 19.9% [19.6%-20.6%] | -- | -- | -- | -- | PASS | -2.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexander Zverev (`KXATPMATCH-26OCT11ZVEBUB-ZVE`) | 0.74 / 0.76 (163511) | 75.0% | 77.8% | 80.4% | 80.1% [79.4%-80.4%] | -- | -- | -- | -- | SHADOW_BET | +2.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 7426.0, B 5208.0; serve-point win A 72.6%, B 33.9%; Elo A 2160.7, B 1947.1; model uncertainty 0.005
* Form inputs: days since last match A 3, B 3; matches on record A 916, B 703; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.007, surface_dev_loose -0.001, surface_dev_tight +0.001
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT11ZVEBUB-28` Over 27.5 games: 0.28/0.34 mid 31.0%, model 38.8% (projection_v2.0 (prediction ledger)) -- gap +7.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT11ZVEBUB-ZVE7` Will Alexander Zverev win at least 6.5 more games than Alexander Bublik?: 0.06/0.20 mid 13.0%, model 5.3% (projection_v2.0 (prediction ledger)) -- gap -7.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT11ZVEBUB-ZVE21` Will Alexander Zverev win the Alexander Zverev vs Alexander Bublik match by a set score of 2-1?: 0.22/0.24 mid 23.0%, model 29.5% (projection_v2.0 (prediction ledger)) -- gap +6.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT11ZVEBUB-2-BUB` Will Alexander Bublik win set 2 in the Alexander Zverev vs Alexander Bublik match: 0.15/0.34 mid 24.5%, model 30.4% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT11ZVEBUB-23` Over 22.5 games: 0.56/0.57 mid 56.5%, model 61.0% (projection_v2.0 (prediction ledger)) -- gap +4.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT11ZVEBUB-BUB2` Will Alexander Bublik win at least 1.5 more games than Alexander Zverev?: 0.19/0.21 mid 20.0%, model 16.0% (projection_v2.0 (prediction ledger)) -- gap -4.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT11ZVEBUB-BUB20` Will Alexander Bublik win the Alexander Zverev vs Alexander Bublik match by a set score of 2-0?: 0.10/0.14 mid 12.0%, model 9.3% (projection_v2.0 (prediction ledger)) -- gap -2.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT11ZVEBUB-18` Over 17.5 games: 0.93/0.95 mid 94.0%, model 95.6% (projection_v2.0 (prediction ledger)) -- gap +1.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT11ZVEBUB-1-ZVE` Will Alexander Zverev win set 1 in the Alexander Zverev vs Alexander Bublik match: 0.66/0.70 mid 68.0%, model 69.5% (projection_v2.0 (prediction ledger)) -- gap +1.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT11ZVEBUB-ZVE20` Will Alexander Zverev win the Alexander Zverev vs Alexander Bublik match by a set score of 2-0?: 0.47/0.51 mid 49.0%, model 48.4% (projection_v2.0 (prediction ledger)) -- gap -0.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT11ZVEBUB-1-BUB` Will Alexander Bublik win set 1 in the Alexander Zverev vs Alexander Bublik match: 0.30/0.32 mid 31.0%, model 30.4% (projection_v2.0 (prediction ledger)) -- gap -0.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT11ZVEBUB-2-ZVE` Will Alexander Zverev win set 2 in the Alexander Zverev vs Alexander Bublik match: 0.67/0.71 mid 69.0%, model 69.5% (projection_v2.0 (prediction ledger)) -- gap +0.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT11ZVEBUB-ZVE4` Will Alexander Zverev win at least 3.5 more games than Alexander Bublik?: 0.42/0.43 mid 42.5%, model 42.9% (projection_v2.0 (prediction ledger)) -- gap +0.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT11ZVEBUB-BUB21` Will Alexander Bublik win the Alexander Zverev vs Alexander Bublik match by a set score of 2-1?: 0.11/0.14 mid 12.5%, model 12.9% (projection_v2.0 (prediction ledger)) -- gap +0.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nikola Bartunkova / Maja Chwalinska vs Elise Mertens / Diana Shnaider -- WTA Wuhan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-11 05:00Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-12T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-12T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT11BARCHWMERSHN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikola Bartunkova / Maja Chwalinska (`KXWTADOUBLES-26OCT11BARCHWMERSHN-BARCHW`) | 0.16 / 0.22 (116) | 19.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Elise Mertens / Diana Shnaider (`KXWTADOUBLES-26OCT11BARCHWMERSHN-MERSHN`) | 0.75 / 0.82 (142) | 78.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Kimberly Birrell vs Katie Volynets -- WTA Wuhan R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-13T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (MASTERS_1000) · Hard · scheduled 2026-10-12T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214040:220465:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kimberly Birrell (`KXWTAMATCH-26OCT11BIRVOL-BIR`) | 0.36 / 0.38 (9609) | 37.0% | 48.4% | 52.7% | 52.1% [47.9%-53.2%] | -- | -- | -- | -- | SHADOW_BET | +11.4 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katie Volynets (`KXWTAMATCH-26OCT11BIRVOL-VOL`) | 0.62 / 0.63 (1797) | 62.5% | 51.6% | 47.3% | 47.9% [46.8%-52.1%] | -- | -- | -- | -- | PASS | -10.9 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5020.0, B 5386.0; serve-point win A 53.8%, B 45.9%; Elo A 1882.8, B 1886.1; model uncertainty 0.0266
* Form inputs: days since last match A 8, B 0; matches on record A 475, B 450; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.011, surface_dev_loose -0.000, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTASETWINNER-26OCT11BIRVOL-2-BIR` Will Kimberly Birrell win set 2 in the Kimberly Birrell vs Katie Volynets match: 0.34/0.42 mid 38.0%, model 48.9% (projection_v2.0 (prediction ledger)) -- gap +10.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11BIRVOL-2-VOL` Will Katie Volynets win set 2 in the Kimberly Birrell vs Katie Volynets match: 0.58/0.66 mid 62.0%, model 51.0% (projection_v2.0 (prediction ledger)) -- gap -10.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT11BIRVOL-22` Over 21.5 games: 0.50/0.51 mid 50.5%, model 60.3% (market_conditioned_v1 (model4_board_v1)) -- gap +9.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT11BIRVOL-1-BIR` Will Kimberly Birrell win set 1 in the Kimberly Birrell vs Katie Volynets match: 0.38/0.42 mid 40.0%, model 48.9% (projection_v2.0 (prediction ledger)) -- gap +8.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11BIRVOL-1-VOL` Will Katie Volynets win set 1 in the Kimberly Birrell vs Katie Volynets match: 0.58/0.61 mid 59.5%, model 51.0% (projection_v2.0 (prediction ledger)) -- gap -8.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT11BIRVOL-27` Over 26.5 games: 0.27/0.31 mid 29.0%, model 37.2% (market_conditioned_v1 (model4_board_v1)) -- gap +8.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT11BIRVOL-17` Over 16.5 games: 0.83/0.89 mid 86.0%, model 92.1% (market_conditioned_v1 (model4_board_v1)) -- gap +6.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Katie Boulter vs Diana Shnaider -- WTA Wuhan R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-13T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (MASTERS_1000) · Hard · scheduled 2026-10-12T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211107:223670:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katie Boulter (`KXWTAMATCH-26OCT11BOUSHN-BOU`) | 0.21 / 0.22 (1282) | 21.5% | 37.9% | 46.9% | 45.3% [42.1%-46.3%] | -- | -- | -- | -- | WATCH | +16.4 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Diana Shnaider (`KXWTAMATCH-26OCT11BOUSHN-SHN`) | 0.77 / 0.78 (8152) | 77.5% | 62.1% | 53.1% | 54.7% [53.7%-57.9%] | -- | -- | -- | -- | PASS | -15.4 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3928.0, B 4846.0; serve-point win A 56.0%, B 41.6%; Elo A 1894.5, B 1952.9; model uncertainty 0.0209
* Form inputs: days since last match A 9, B 7; matches on record A 589, B 316; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT11BOUSHN-BOU  (YES = Katie Boulter)
Model: 38%
Kalshi: 22%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.011, surface_dev_loose +0.011, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT11BOUSHN-15` Over 14.5 games: 0.45/0.94 mid 69.5%, model 99.1% (projection_v2.0 (prediction ledger)) -- gap +29.6 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT11BOUSHN-20` Over 19.5 games: 0.52/0.54 mid 53.0%, model 73.7% (projection_v2.0 (prediction ledger)) -- gap +20.7 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT11BOUSHN-2-SHN` Will Diana Shnaider win set 2 in the Katie Boulter vs Diana Shnaider match: 0.69/0.86 mid 77.5%, model 58.1% (projection_v2.0 (prediction ledger)) -- gap -19.4 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT11BOUSHN-25` Over 24.5 games: 0.24/0.34 mid 29.0%, model 48.3% (projection_v2.0 (prediction ledger)) -- gap +19.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT11BOUSHN-2-BOU` Will Katie Boulter win set 2 in the Katie Boulter vs Diana Shnaider match: 0.16/0.30 mid 23.0%, model 41.9% (projection_v2.0 (prediction ledger)) -- gap +18.9 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11BOUSHN-1-BOU` Will Katie Boulter win set 1 in the Katie Boulter vs Diana Shnaider match: 0.26/0.29 mid 27.5%, model 41.9% (projection_v2.0 (prediction ledger)) -- gap +14.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11BOUSHN-1-SHN` Will Diana Shnaider win set 1 in the Katie Boulter vs Diana Shnaider match: 0.71/0.73 mid 72.0%, model 58.1% (projection_v2.0 (prediction ledger)) -- gap -13.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sara Errani / Jasmine Paolini vs Leylah Fernandez / Talia Gibson -- WTA Wuhan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-13T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-12T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT11ERRPAOFERGIB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Errani / Jasmine Paolini (`KXWTADOUBLES-26OCT11ERRPAOFERGIB-ERRPAO`) | 0.69 / 0.74 (55) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leylah Fernandez / Talia Gibson (`KXWTADOUBLES-26OCT11ERRPAOFERGIB-FERGIB`) | 0.25 / 0.29 (8) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Hanyu Guo vs Sorana Cirstea -- WTA Wuhan R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-13T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (MASTERS_1000) · Hard · scheduled 2026-10-12T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:201514:215250:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sorana Cirstea (`KXWTAMATCH-26OCT11GUOCIR-CIR`) | 0.86 / 0.88 (42125) | 87.0% | 79.9% | 78.5% | 80.7% [78.5%-84.5%] | -- | -- | -- | -- | PASS | -7.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hanyu Guo (`KXWTAMATCH-26OCT11GUOCIR-GUO`) | 0.12 / 0.13 (1416) | 12.5% | 20.1% | 21.5% | 19.3% [15.5%-21.5%] | -- | -- | -- | -- | SHADOW_BET | +7.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3015.0, B 4410.0; serve-point win A 54.2%, B 39.5%; Elo A 1734.6, B 2024.6; model uncertainty 0.0299
* Form inputs: days since last match A 5, B 35; matches on record A 326, B 1061; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.022, surface_dev_loose -0.004, surface_dev_tight +0.007
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 6 carry a model probability
  * `KXWTAGTOTAL-26OCT11GUOCIR-19` Over 18.5 games: 0.52/0.54 mid 53.0%, model 73.6% (projection_v2.0 (prediction ledger)) -- gap +20.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT11GUOCIR-24` Over 23.5 games: 0.19/0.34 mid 26.5%, model 42.5% (projection_v2.0 (prediction ledger)) -- gap +16.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT11GUOCIR-1-GUO` Will Hanyu Guo win set 1 in the Hanyu Guo vs Sorana Cirstea match: 0.17/0.21 mid 19.0%, model 28.8% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11GUOCIR-1-CIR` Will Sorana Cirstea win set 1 in the Hanyu Guo vs Sorana Cirstea match: 0.78/0.82 mid 80.0%, model 71.2% (projection_v2.0 (prediction ledger)) -- gap -8.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11GUOCIR-2-CIR` Will Sorana Cirstea win set 2 in the Hanyu Guo vs Sorana Cirstea match: 0.61/0.93 mid 77.0%, model 71.2% (projection_v2.0 (prediction ledger)) -- gap -5.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11GUOCIR-2-GUO` Will Hanyu Guo win set 2 in the Hanyu Guo vs Sorana Cirstea match: 0.09/0.39 mid 24.0%, model 28.8% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Xinyu Jiang / Xiyu Wang vs Cristina Bucsa / Nicole Melichar-Martinez -- WTA Wuhan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-11 05:00Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-12T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-12T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT11JIAWANBUCMEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cristina Bucsa / Nicole Melichar-Martinez (`KXWTADOUBLES-26OCT11JIAWANBUCMEL-BUCMEL`) | 0.40 / 0.80 (2) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xinyu Jiang / Xiyu Wang (`KXWTADOUBLES-26OCT11JIAWANBUCMEL-JIAWAN`) | 0.05 / 0.56 (50) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Anhelina Kalinina / Dayana Yastremska vs Alexandra Eala / Zeynep Sonmez -- WTA Wuhan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-13T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-12T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT11KALYASEALSON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandra Eala / Zeynep Sonmez (`KXWTADOUBLES-26OCT11KALYASEALSON-EALSON`) | 0.50 / 0.52 (267) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anhelina Kalinina / Dayana Yastremska (`KXWTADOUBLES-26OCT11KALYASEALSON-KALYAS`) | 0.21 / 0.52 (61) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Anna Kalinskaya vs Shuai Zhang -- WTA Wuhan R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-13T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (MASTERS_1000) · Hard · scheduled 2026-10-12T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:201533:214939:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Kalinskaya (`KXWTAMATCH-26OCT11KALZHA-KAL`) | 0.70 / 0.71 (1419) | 70.5% | 74.4% | 52.6% | 58.3% [55.2%-66.8%] | 69.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Shuai Zhang (`KXWTAMATCH-26OCT11KALZHA-ZHA`) | 0.29 / 0.30 (150) | 29.5% | 25.6% | 47.4% | 41.7% [33.2%-44.8%] | 30.9% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | -3.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4015.0, B 3846.0; serve-point win A 60.2%, B 44.8%; Elo A 2017.6, B 1852.0; model uncertainty 0.058
* Form inputs: days since last match A 8, B 42; matches on record A 554, B 1066; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.015, surface_dev_loose -0.010, surface_dev_tight +0.010
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT11KALZHA-22` Over 21.5 games: 0.44/0.45 mid 44.5%, model 59.7% (market_conditioned_v1 (model4_board_v1)) -- gap +15.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT11KALZHA-27` Over 26.5 games: 0.19/0.32 mid 25.5%, model 37.0% (market_conditioned_v1 (model4_board_v1)) -- gap +11.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT11KALZHA-17` Over 16.5 games: 0.79/0.90 mid 84.5%, model 92.7% (market_conditioned_v1 (model4_board_v1)) -- gap +8.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT11KALZHA-2-ZHA` Will Shuai Zhang win set 2 in the Anna Kalinskaya vs Shuai Zhang match: 0.23/0.55 mid 39.0%, model 33.1% (projection_v2.0 (prediction ledger)) -- gap -5.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11KALZHA-1-KAL` Will Anna Kalinskaya win set 1 in the Anna Kalinskaya vs Shuai Zhang match: 0.60/0.67 mid 63.5%, model 66.9% (projection_v2.0 (prediction ledger)) -- gap +3.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11KALZHA-2-KAL` Will Anna Kalinskaya win set 2 in the Anna Kalinskaya vs Shuai Zhang match: 0.45/0.83 mid 64.0%, model 66.9% (projection_v2.0 (prediction ledger)) -- gap +2.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11KALZHA-1-ZHA` Will Shuai Zhang win set 1 in the Anna Kalinskaya vs Shuai Zhang match: 0.31/0.36 mid 33.5%, model 33.1% (projection_v2.0 (prediction ledger)) -- gap -0.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Daria Kasatkina vs Jelena Ostapenko -- WTA Wuhan R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-13T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (MASTERS_1000) · Hard · scheduled 2026-10-12T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211533:214082:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria Kasatkina (`KXWTAMATCH-26OCT11KASOST-KAS`) | 0.44 / 0.45 (2719) | 44.5% | 47.3% | 54.3% | 52.1% [45.7%-54.3%] | -- | -- | -- | -- | WATCH | +2.8 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jelena Ostapenko (`KXWTAMATCH-26OCT11KASOST-OST`) | 0.55 / 0.56 (8400) | 55.5% | 52.7% | 45.7% | 47.9% [45.7%-54.3%] | -- | -- | -- | -- | PASS | -2.8 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4023.0, B 3919.0; serve-point win A 51.1%, B 48.4%; Elo A 1884.2, B 1906.4; model uncertainty 0.0428
* Form inputs: days since last match A 0, B 6; matches on record A 669, B 676; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.021, surface_dev_loose -0.000, surface_dev_tight -0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT11KASOST-22` Over 21.5 games: 0.50/0.52 mid 51.0%, model 61.3% (market_conditioned_v1 (model4_board_v1)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT11KASOST-27` Over 26.5 games: 0.26/0.32 mid 29.0%, model 37.8% (market_conditioned_v1 (model4_board_v1)) -- gap +8.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT11KASOST-17` Over 16.5 games: 0.84/0.90 mid 87.0%, model 92.2% (market_conditioned_v1 (model4_board_v1)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT11KASOST-2-KAS` Will Daria Kasatkina win set 2 in the Daria Kasatkina vs Jelena Ostapenko match: 0.38/0.49 mid 43.5%, model 48.2% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT11KASOST-2-OST` Will Jelena Ostapenko win set 2 in the Daria Kasatkina vs Jelena Ostapenko match: 0.51/0.62 mid 56.5%, model 51.8% (projection_v2.0 (prediction ledger)) -- gap -4.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT11KASOST-1-KAS` Will Daria Kasatkina win set 1 in the Daria Kasatkina vs Jelena Ostapenko match: 0.43/0.48 mid 45.5%, model 48.2% (projection_v2.0 (prediction ledger)) -- gap +2.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT11KASOST-1-OST` Will Jelena Ostapenko win set 1 in the Daria Kasatkina vs Jelena Ostapenko match: 0.52/0.55 mid 53.5%, model 51.8% (projection_v2.0 (prediction ledger)) -- gap -1.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Caty McNally / Janice Tjen vs Qianhui Tang / Yifan Xu -- WTA Wuhan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-12T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT11MCCTJETANYIF:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Caty McNally / Janice Tjen (`KXWTADOUBLES-26OCT11MCCTJETANYIF-MCCTJE`) | 0.46 / 0.60 (40) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Qianhui Tang / Yifan Xu (`KXWTADOUBLES-26OCT11MCCTJETANYIF-TANYIF`) | 0.22 / 0.44 (23) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Ellen Perez / Demi Schuurs vs Marie Bouzkova / Sara Sorribes Tormo -- WTA Wuhan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-13T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-12T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT11PERSCHBOUSOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marie Bouzkova / Sara Sorribes Tormo (`KXWTADOUBLES-26OCT11PERSCHBOUSOR-BOUSOR`) | 0.29 / 0.33 (150) | 31.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ellen Perez / Demi Schuurs (`KXWTADOUBLES-26OCT11PERSCHBOUSOR-PERSCH`) | 0.65 / 0.70 (274) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Yulia Putintseva vs Zeynep Sonmez -- WTA Wuhan R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-13T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (MASTERS_1000) · Hard · scheduled 2026-10-12T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:201709:220309:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yulia Putintseva (`KXWTAMATCH-26OCT11PUTSON-PUT`) | 0.54 / 0.55 (30827) | 54.5% | 51.0% | 51.1% | 53.2% [52.1%-54.3%] | -- | -- | -- | -- | PASS | -3.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zeynep Sonmez (`KXWTAMATCH-26OCT11PUTSON-SON`) | 0.46 / 0.47 (1854) | 46.5% | 49.0% | 48.9% | 46.8% [45.7%-47.9%] | -- | -- | -- | -- | PASS | +2.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4366.0, B 4355.0; serve-point win A 54.2%, B 46.0%; Elo A 1893.1, B 1838.8; model uncertainty 0.0106
* Form inputs: days since last match A 0, B 0; matches on record A 854, B 426; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.011, surface_dev_loose -0.011, surface_dev_tight +0.011
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT11PUTSON-22` Over 21.5 games: 0.51/0.53 mid 52.0%, model 62.0% (market_conditioned_v1 (model4_board_v1)) -- gap +10.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT11PUTSON-27` Over 26.5 games: 0.28/0.32 mid 30.0%, model 38.6% (market_conditioned_v1 (model4_board_v1)) -- gap +8.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT11PUTSON-17` Over 16.5 games: 0.84/0.91 mid 87.5%, model 92.9% (market_conditioned_v1 (model4_board_v1)) -- gap +5.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT11PUTSON-1-SON` Will Zeynep Sonmez win set 1 in the Yulia Putintseva vs Zeynep Sonmez match: 0.47/0.48 mid 47.5%, model 49.4% (projection_v2.0 (prediction ledger)) -- gap +1.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11PUTSON-1-PUT` Will Yulia Putintseva win set 1 in the Yulia Putintseva vs Zeynep Sonmez match: 0.51/0.53 mid 52.0%, model 50.6% (projection_v2.0 (prediction ledger)) -- gap -1.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11PUTSON-2-PUT` Will Yulia Putintseva win set 2 in the Yulia Putintseva vs Zeynep Sonmez match: 0.33/0.70 mid 51.5%, model 50.6% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11PUTSON-2-SON` Will Zeynep Sonmez win set 2 in the Yulia Putintseva vs Zeynep Sonmez match: 0.30/0.67 mid 48.5%, model 49.4% (projection_v2.0 (prediction ledger)) -- gap +0.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Maria Sakkari / Donna Vekic vs Shuko Aoyama / En-Shuo Liang -- WTA Wuhan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-11 05:00Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-12T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-12T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT11SAKVEKAOYLIA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shuko Aoyama / En-Shuo Liang (`KXWTADOUBLES-26OCT11SAKVEKAOYLIA-AOYLIA`) | 0.58 / 0.75 (252) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maria Sakkari / Donna Vekic (`KXWTADOUBLES-26OCT11SAKVEKAOYLIA-SAKVEK`) | 0.24 / 0.29 (18) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Mayar Sherif Ahmed Abdelaziz vs Maja Chwalinska -- WTA Wuhan R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-13T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (MASTERS_1000) · Hard · scheduled 2026-10-12T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:210886:216081:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maja Chwalinska (`KXWTAMATCH-26OCT11SHECHW-CHW`) | 0.78 / 0.80 (17581) | 79.0% | 72.4% | 87.6% | 83.8% [68.4%-87.6%] | -- | -- | -- | -- | PASS | -6.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Mayar Sherif Ahmed Abdelaziz (`KXWTAMATCH-26OCT11SHECHW-SHE`) | 0.21 / 0.22 (25671) | 21.5% | 27.6% | 12.4% | 16.2% [12.4%-31.6%] | -- | -- | -- | -- | PASS | +6.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 4792.0, B 3543.0; serve-point win A 52.6%, B 42.9%; Elo A 1643.4, B 1796.2; model uncertainty 0.096
* Form inputs: days since last match A 39, B 9; matches on record A 525, B 391; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.013, surface_dev_loose -0.039, surface_dev_tight +0.046
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT11SHECHW-2-CHW` Will Maja Chwalinska win set 2 in the Maiar Sherif Ahmed Abdelaziz vs Maja Chwalinska match: 0.71/0.79 mid 75.0%, model 65.4% (projection_v2.0 (prediction ledger)) -- gap -9.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11SHECHW-1-SHE` Will Maiar Sherif Ahmed Abdelaziz win set 1 in the Maiar Sherif Ahmed Abdelaziz vs Maja Chwalinska match: 0.24/0.29 mid 26.5%, model 34.6% (projection_v2.0 (prediction ledger)) -- gap +8.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11SHECHW-1-CHW` Will Maja Chwalinska win set 1 in the Maiar Sherif Ahmed Abdelaziz vs Maja Chwalinska match: 0.71/0.74 mid 72.5%, model 65.4% (projection_v2.0 (prediction ledger)) -- gap -7.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11SHECHW-2-SHE` Will Maiar Sherif Ahmed Abdelaziz win set 2 in the Maiar Sherif Ahmed Abdelaziz vs Maja Chwalinska match: 0.15/0.42 mid 28.5%, model 34.6% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Katerina Siniakova vs Liudmila Samsonova -- WTA Wuhan R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-13T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (MASTERS_1000) · Hard · scheduled 2026-10-12T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211701:214643:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liudmila Samsonova (`KXWTAMATCH-26OCT11SINSAM-SAM`) | 0.51 / 0.53 (2098) | 52.0% | 48.1% | 38.6% | 41.1% [39.6%-47.4%] | -- | -- | -- | -- | PASS | -3.9 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katerina Siniakova (`KXWTAMATCH-26OCT11SINSAM-SIN`) | 0.46 / 0.48 (250) | 47.0% | 51.9% | 61.4% | 58.9% [52.6%-60.4%] | -- | -- | -- | -- | SHADOW_BET | +4.9 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4278.0, B 3968.0; serve-point win A 57.3%, B 43.1%; Elo A 1922.9, B 1911.7; model uncertainty 0.0388
* Form inputs: days since last match A 8, B 7; matches on record A 719, B 537; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.015, surface_dev_tight -0.021
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT11SINSAM-23` Over 22.5 games: 0.44/0.45 mid 44.5%, model 56.7% (projection_v2.0 (prediction ledger)) -- gap +12.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT11SINSAM-28` Over 27.5 games: 0.23/0.31 mid 27.0%, model 35.1% (projection_v2.0 (prediction ledger)) -- gap +8.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT11SINSAM-18` Over 17.5 games: 0.78/0.88 mid 83.0%, model 88.6% (projection_v2.0 (prediction ledger)) -- gap +5.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT11SINSAM-2-SIN` Will Katerina Siniakova win set 2 in the Katerina Siniakova vs Liudmila Samsonova match: 0.45/0.49 mid 47.0%, model 51.3% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT11SINSAM-1-SIN` Will Katerina Siniakova win set 1 in the Katerina Siniakova vs Liudmila Samsonova match: 0.45/0.50 mid 47.5%, model 51.3% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT11SINSAM-1-SAM` Will Liudmila Samsonova win set 1 in the Katerina Siniakova vs Liudmila Samsonova match: 0.50/0.54 mid 52.0%, model 48.7% (projection_v2.0 (prediction ledger)) -- gap -3.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT11SINSAM-2-SAM` Will Liudmila Samsonova win set 2 in the Katerina Siniakova vs Liudmila Samsonova match: 0.50/0.54 mid 52.0%, model 48.7% (projection_v2.0 (prediction ledger)) -- gap -3.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Daria Snigur vs Elise Mertens -- WTA Wuhan R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-13T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (MASTERS_1000) · Hard · scheduled 2026-10-12T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:210722:220750:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elise Mertens (`KXWTAMATCH-26OCT11SNIMER-MER`) | 0.66 / 0.67 (44184) | 66.5% | 55.6% | 42.1% | 47.9% [44.2%-60.5%] | -- | -- | -- | -- | PASS | -10.9 pp | REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daria Snigur (`KXWTAMATCH-26OCT11SNIMER-SNI`) | 0.32 / 0.33 (1434) | 32.5% | 44.4% | 57.9% | 52.1% [39.5%-55.8%] | -- | -- | -- | -- | WATCH | +11.9 pp | REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4190.0, B 3838.0; serve-point win A 55.5%, B 43.4%; Elo A 1890.9, B 1990.0; model uncertainty 0.0813
* Form inputs: days since last match A 5, B 1; matches on record A 439, B 804; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.026, surface_pool_high +0.021, surface_dev_loose +0.011, surface_dev_tight -0.016
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT11SNIMER-15` Over 14.5 games: 0.48/0.92 mid 70.0%, model 99.0% (projection_v2.0 (prediction ledger)) -- gap +29.0 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT11SNIMER-20` Over 19.5 games: 0.55/0.61 mid 58.0%, model 74.1% (projection_v2.0 (prediction ledger)) -- gap +16.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT11SNIMER-25` Over 24.5 games: 0.33/0.38 mid 35.5%, model 48.9% (projection_v2.0 (prediction ledger)) -- gap +13.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT11SNIMER-1-SNI` Will Daria Snigur win set 1 in the Daria Snigur vs Elise Mertens match: 0.36/0.39 mid 37.5%, model 46.2% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT11SNIMER-1-MER` Will Elise Mertens win set 1 in the Daria Snigur vs Elise Mertens match: 0.59/0.63 mid 61.0%, model 53.8% (projection_v2.0 (prediction ledger)) -- gap -7.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT11SNIMER-2-SNI` Will Daria Snigur win set 2 in the Daria Snigur vs Elise Mertens match: 0.31/0.51 mid 41.0%, model 46.2% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT11SNIMER-2-MER` Will Elise Mertens win set 2 in the Daria Snigur vs Elise Mertens match: 0.44/0.71 mid 57.5%, model 53.8% (projection_v2.0 (prediction ledger)) -- gap -3.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Fanny Stollar / Fang-Hsien Wu vs Erin Routliffe / Aldila Sutjiadi -- WTA Wuhan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-13T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-12T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT11STOFANROUSUT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Erin Routliffe / Aldila Sutjiadi (`KXWTADOUBLES-26OCT11STOFANROUSUT-ROUSUT`) | 0.34 / 0.66 (52) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fanny Stollar / Fang-Hsien Wu (`KXWTADOUBLES-26OCT11STOFANROUSUT-STOFAN`) | 0.08 / 0.39 (42) | 23.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Lilli Tagger vs Nikola Bartunkova -- WTA Wuhan R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-13T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (MASTERS_1000) · Hard · scheduled 2026-10-12T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:223360:260172:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikola Bartunkova (`KXWTAMATCH-26OCT11TAGBAR-BAR`) | 0.70 / 0.71 (19739) | 70.5% | 63.8% | 49.0% | 55.2% [51.5%-61.4%] | -- | -- | -- | -- | PASS | -6.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lilli Tagger (`KXWTAMATCH-26OCT11TAGBAR-TAG`) | 0.29 / 0.30 (1286) | 29.5% | 36.2% | 51.0% | 44.8% [38.6%-48.4%] | -- | -- | -- | -- | SHADOW_BET | +6.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2552.0, B 3248.0; serve-point win A 58.0%, B 39.3%; Elo A 1797.2, B 1898.4; model uncertainty 0.049
* Form inputs: days since last match A 11, B 1; matches on record A 128, B 249; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight +0.010
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT11TAGBAR-15` Over 14.5 games: 0.54/0.95 mid 74.5%, model 99.3% (projection_v2.0 (prediction ledger)) -- gap +24.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT11TAGBAR-20` Over 19.5 games: 0.60/0.62 mid 61.0%, model 74.9% (projection_v2.0 (prediction ledger)) -- gap +13.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT11TAGBAR-25` Over 24.5 games: 0.33/0.38 mid 35.5%, model 48.9% (projection_v2.0 (prediction ledger)) -- gap +13.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT11TAGBAR-1-BAR` Will Nikola Bartunkova win set 1 in the Lilli Tagger vs Nikola Bartunkova match: 0.64/0.67 mid 65.5%, model 59.3% (projection_v2.0 (prediction ledger)) -- gap -6.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11TAGBAR-1-TAG` Will Lilli Tagger win set 1 in the Lilli Tagger vs Nikola Bartunkova match: 0.34/0.36 mid 35.0%, model 40.7% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11TAGBAR-2-TAG` Will Lilli Tagger win set 2 in the Lilli Tagger vs Nikola Bartunkova match: 0.26/0.46 mid 36.0%, model 40.7% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11TAGBAR-2-BAR` Will Nikola Bartunkova win set 2 in the Lilli Tagger vs Nikola Bartunkova match: 0.55/0.72 mid 63.5%, model 59.3% (projection_v2.0 (prediction ledger)) -- gap -4.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dayana Yastremska vs Cristina Bucsa -- WTA Wuhan R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-13T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (MASTERS_1000) · Hard · scheduled 2026-10-12T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213710:215035:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cristina Bucsa (`KXWTAMATCH-26OCT11YASBUC-BUC`) | 0.43 / 0.44 (1361) | 43.5% | 54.4% | 65.5% | 62.0% [52.1%-64.5%] | -- | -- | -- | -- | WATCH | +10.9 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dayana Yastremska (`KXWTAMATCH-26OCT11YASBUC-YAS`) | 0.54 / 0.56 (19833) | 55.0% | 45.6% | 34.5% | 38.0% [35.5%-47.9%] | -- | -- | -- | -- | PASS | -9.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4632.0, B 4493.0; serve-point win A 55.2%, B 44.0%; Elo A 1844.2, B 1845.0; model uncertainty 0.0619
* Form inputs: days since last match A 7, B 8; matches on record A 477, B 587; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.020
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT11YASBUC-21` Over 20.5 games: 0.55/0.57 mid 56.0%, model 67.5% (projection_v2.0 (prediction ledger)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT11YASBUC-26` Over 25.5 games: 0.31/0.36 mid 33.5%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap +10.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT11YASBUC-1-BUC` Will Cristina Bucsa win set 1 in the Dayana Yastremska vs Cristina Bucsa match: 0.43/0.47 mid 45.0%, model 53.0% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11YASBUC-2-BUC` Will Cristina Bucsa win set 2 in the Dayana Yastremska vs Cristina Bucsa match: 0.43/0.47 mid 45.0%, model 53.0% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11YASBUC-2-YAS` Will Dayana Yastremska win set 2 in the Dayana Yastremska vs Cristina Bucsa match: 0.52/0.57 mid 54.5%, model 47.0% (projection_v2.0 (prediction ledger)) -- gap -7.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11YASBUC-1-YAS` Will Dayana Yastremska win set 1 in the Dayana Yastremska vs Cristina Bucsa match: 0.52/0.56 mid 54.0%, model 47.0% (projection_v2.0 (prediction ledger)) -- gap -7.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT11YASBUC-16` Over 15.5 games: 0.90/0.95 mid 92.5%, model 97.1% (projection_v2.0 (prediction ledger)) -- gap +4.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Anna Bondar vs Mia Pohankova -- WTA Wuhan R64

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-12 07:10Z
* Current expected start: 2026-10-12 05:20Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 04:35Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-110_MIN; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-12T07:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT12BONPOH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Bondar (`KXWTAMATCH-26OCT12BONPOH-BON`) | 0.50 / 0.51 (23823) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mia Pohankova (`KXWTAMATCH-26OCT12BONPOH-POH`) | 0.49 / 0.50 (477) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Robert Galloway / Andre Goransson vs Adam Pavlasek / Patrik Rikl -- ATP Shanghai R16

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-11 07:00Z
* Current expected start: 2026-10-12 05:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 04:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-11T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT11GALGORPAVRIK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robert Galloway / Andre Goransson (`KXATPDOUBLES-26OCT11GALGORPAVRIK-GALGOR`) | 0.41 / 0.42 (6396) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Adam Pavlasek / Patrik Rikl (`KXATPDOUBLES-26OCT11GALGORPAVRIK-PAVRIK`) | 0.58 / 0.59 (987) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Jiri Lehecka vs Rafael Jodar -- ATP Shanghai R32

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-11 07:00Z
* Current expected start: 2026-10-12 05:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 04:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1350_MIN; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (MASTERS_1000) · Hard · scheduled 2026-10-11T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208103:212588:2026-10-11`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rafael Jodar (`KXATPMATCH-26OCT11LEHJOD-JOD`) | 0.39 / 0.40 (24933) | 39.5% | 54.5% | 58.4% | 56.5% [53.0%-58.9%] | -- | -- | -- | -- | SHADOW_BET | +15.0 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jiri Lehecka (`KXATPMATCH-26OCT11LEHJOD-LEH`) | 0.60 / 0.61 (17337) | 60.5% | 45.5% | 41.6% | 43.5% [41.1%-47.0%] | -- | -- | -- | -- | PASS | -15.0 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5105.0, B 4275.0; serve-point win A 63.4%, B 35.7%; Elo A 1981.7, B 1998.9; model uncertainty 0.0296
* Form inputs: days since last match A 1, B 1; matches on record A 457, B 135; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT11LEHJOD-JOD  (YES = Rafael Jodar)
Model: 55%
Kalshi: 40%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight +0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT11LEHJOD-LEH2` Will Jiri Lehecka win at least 1.5 more games than Rafael Jodar?: 0.53/0.54 mid 53.5%, model 37.4% (projection_v2.0 (prediction ledger)) -- gap -16.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT11LEHJOD-LEH20` Will Jiri Lehecka win the Jiri Lehecka vs Rafael Jodar match by a set score of 2-0?: 0.36/0.37 mid 36.5%, model 22.1% (projection_v2.0 (prediction ledger)) -- gap -14.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT11LEHJOD-JOD2` Will Rafael Jodar win at least 1.5 more games than Jiri Lehecka?: 0.35/0.37 mid 36.0%, model 47.8% (projection_v2.0 (prediction ledger)) -- gap +11.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT11LEHJOD-LEH5` Will Jiri Lehecka win at least 4.5 more games than Rafael Jodar?: 0.23/0.28 mid 25.5%, model 13.9% (projection_v2.0 (prediction ledger)) -- gap -11.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT11LEHJOD-1-JOD` Will Rafael Jodar win set 1 in the Jiri Lehecka vs Rafael Jodar match: 0.41/0.44 mid 42.5%, model 53.0% (projection_v2.0 (prediction ledger)) -- gap +10.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT11LEHJOD-2-JOD` Will Rafael Jodar win set 2 in the Jiri Lehecka vs Rafael Jodar match: 0.41/0.44 mid 42.5%, model 53.0% (projection_v2.0 (prediction ledger)) -- gap +10.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT11LEHJOD-2-LEH` Will Jiri Lehecka win set 2 in the Jiri Lehecka vs Rafael Jodar match: 0.56/0.58 mid 57.0%, model 47.0% (projection_v2.0 (prediction ledger)) -- gap -10.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT11LEHJOD-1-LEH` Will Jiri Lehecka win set 1 in the Jiri Lehecka vs Rafael Jodar match: 0.55/0.58 mid 56.5%, model 47.0% (projection_v2.0 (prediction ledger)) -- gap -9.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT11LEHJOD-20` Over 19.5 games: 0.67/0.76 mid 71.5%, model 80.8% (projection_v2.0 (prediction ledger)) -- gap +9.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT11LEHJOD-JOD21` Will Rafael Jodar win the Jiri Lehecka vs Rafael Jodar match by a set score of 2-1?: 0.17/0.18 mid 17.5%, model 26.4% (projection_v2.0 (prediction ledger)) -- gap +8.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT11LEHJOD-25` Over 24.5 games: 0.40/0.50 mid 45.0%, model 53.2% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT11LEHJOD-30` Over 29.5 games: 0.20/0.30 mid 25.0%, model 30.7% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT11LEHJOD-JOD20` Will Rafael Jodar win the Jiri Lehecka vs Rafael Jodar match by a set score of 2-0?: 0.22/0.23 mid 22.5%, model 28.1% (projection_v2.0 (prediction ledger)) -- gap +5.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT11LEHJOD-LEH21` Will Jiri Lehecka win the Jiri Lehecka vs Rafael Jodar match by a set score of 2-1?: 0.22/0.24 mid 23.0%, model 23.4% (projection_v2.0 (prediction ledger)) -- gap +0.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Stefanos Tsitsipas vs Taylor Fritz -- ATP Shanghai R32

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-12 07:00Z
* Current expected start: 2026-10-12 05:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 04:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-90_MIN; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (MASTERS_1000) · Hard · scheduled 2026-10-12T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126203:126774:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Taylor Fritz (`KXATPMATCH-26OCT12TSIFRI-FRI`) | 0.60 / 0.61 (71548) | 60.5% | 66.5% | 74.2% | 71.9% [67.9%-73.8%] | 59.4% | 59.7% | 59.6% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.0 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Stefanos Tsitsipas (`KXATPMATCH-26OCT12TSIFRI-TSI`) | 0.40 / 0.41 (49338) | 40.5% | 33.5% | 25.8% | 28.1% [26.2%-32.1%] | 40.6% | 40.3% | 40.5% | MODEL_LONE_OUTLIER | PASS | -7.0 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5052.0, B 5964.0; serve-point win A 66.9%, B 29.5%; Elo A 1948.6, B 2055.4; model uncertainty 0.0294
* Form inputs: days since last match A 2, B 2; matches on record A 799, B 738; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.016, surface_dev_loose -0.012, surface_dev_tight +0.009
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT12TSIFRI-30` Over 29.5 games: 0.25/0.33 mid 29.0%, model 37.0% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT12TSIFRI-25` Over 24.5 games: 0.47/0.49 mid 48.0%, model 55.7% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT12TSIFRI-TSI2` Will Stefanos Tsitsipas win at least 1.5 more games than Taylor Fritz?: 0.32/0.33 mid 32.5%, model 25.8% (projection_v2.0 (prediction ledger)) -- gap -6.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT12TSIFRI-TSI20` Will Stefanos Tsitsipas win the Stefanos Tsitsipas vs Taylor Fritz match by a set score of 2-0?: 0.21/0.22 mid 21.5%, model 15.0% (projection_v2.0 (prediction ledger)) -- gap -6.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT12TSIFRI-FRI21` Will Taylor Fritz win the Stefanos Tsitsipas vs Taylor Fritz match by a set score of 2-1?: 0.22/0.24 mid 23.0%, model 29.1% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT12TSIFRI-2-FRI` Will Taylor Fritz win set 2 in the Stefanos Tsitsipas vs Taylor Fritz match: 0.55/0.59 mid 57.0%, model 61.2% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT12TSIFRI-2-TSI` Will Stefanos Tsitsipas win set 2 in the Stefanos Tsitsipas vs Taylor Fritz match: 0.40/0.45 mid 42.5%, model 38.8% (projection_v2.0 (prediction ledger)) -- gap -3.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT12TSIFRI-1-FRI` Will Taylor Fritz win set 1 in the Stefanos Tsitsipas vs Taylor Fritz match: 0.57/0.59 mid 58.0%, model 61.2% (projection_v2.0 (prediction ledger)) -- gap +3.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT12TSIFRI-1-TSI` Will Stefanos Tsitsipas win set 1 in the Stefanos Tsitsipas vs Taylor Fritz match: 0.41/0.43 mid 42.0%, model 38.8% (projection_v2.0 (prediction ledger)) -- gap -3.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT12TSIFRI-FRI3` Will Taylor Fritz win at least 2.5 more games than Stefanos Tsitsipas?: 0.44/0.45 mid 44.5%, model 47.4% (projection_v2.0 (prediction ledger)) -- gap +2.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT12TSIFRI-FRI6` Will Taylor Fritz win at least 5.5 more games than Stefanos Tsitsipas?: 0.08/0.14 mid 11.0%, model 8.4% (projection_v2.0 (prediction ledger)) -- gap -2.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT12TSIFRI-20` Over 19.5 games: 0.80/0.88 mid 84.0%, model 86.6% (projection_v2.0 (prediction ledger)) -- gap +2.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT12TSIFRI-TSI21` Will Stefanos Tsitsipas win the Stefanos Tsitsipas vs Taylor Fritz match by a set score of 2-1?: 0.17/0.19 mid 18.0%, model 18.4% (projection_v2.0 (prediction ledger)) -- gap +0.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT12TSIFRI-FRI20` Will Taylor Fritz win the Stefanos Tsitsipas vs Taylor Fritz match by a set score of 2-0?: 0.37/0.38 mid 37.5%, model 37.5% (projection_v2.0 (prediction ledger)) -- gap -0.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STATUS_AMBIGUOUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hanyu Guo / Kristina Mladenovic vs Maia Lumsden / Alexandra Panova -- WTA Wuhan R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-12 05:56Z
* Source: COURT_PROGRESSION: preceding match on Court 4 in progress (set 1 of best-of-3); confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 05:11Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-12T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT11GUOMLALUMPAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hanyu Guo / Kristina Mladenovic (`KXWTADOUBLES-26OCT11GUOMLALUMPAN-GUOMLA`) | 0.69 / 0.73 (2986) | 71.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maia Lumsden / Alexandra Panova (`KXWTADOUBLES-26OCT11GUOMLALUMPAN-LUMPAN`) | 0.27 / 0.30 (1013) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Jasmine Paolini vs Sara Bejlek -- WTA Wuhan R64

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-12 05:56Z
* Source: COURT_PROGRESSION: preceding match on Court 1 in progress (set 1 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 05:11Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-12T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211148:239383:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Bejlek (`KXWTAMATCH-26OCT11PAOBEJ-BEJ`) | 0.53 / 0.54 (22310) | 53.5% | 44.6% | 55.9% | 48.9% [36.4%-53.7%] | 55.6% | 53.8% | 54.7% | MODEL_LONE_OUTLIER | PASS | -8.8 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Jasmine Paolini (`KXWTAMATCH-26OCT11PAOBEJ-PAO`) | 0.46 / 0.47 (35622) | 46.5% | 55.4% | 44.1% | 51.1% [46.3%-63.6%] | 44.4% | 46.1% | 45.2% | MODEL_LONE_OUTLIER | WATCH | +8.8 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4852.0, B 3433.0; serve-point win A 53.7%, B 47.3%; Elo A 2004.2, B 1886.4; model uncertainty 0.0866
* Form inputs: days since last match A 9, B 7; matches on record A 708, B 269; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.016, surface_dev_loose -0.016, surface_dev_tight +0.011
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT11PAOBEJ-23` Over 22.5 games: 0.43/0.44 mid 43.5%, model 55.2% (projection_v2.0 (prediction ledger)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT11PAOBEJ-28` Over 27.5 games: 0.21/0.26 mid 23.5%, model 33.1% (projection_v2.0 (prediction ledger)) -- gap +9.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT11PAOBEJ-18` Over 17.5 games: 0.74/0.82 mid 78.0%, model 86.7% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT11PAOBEJ-1-PAO` Will Jasmine Paolini win set 1 in the Jasmine Paolini vs Sara Bejlek match: 0.46/0.48 mid 47.0%, model 53.6% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11PAOBEJ-2-PAO` Will Jasmine Paolini win set 2 in the Jasmine Paolini vs Sara Bejlek match: 0.45/0.49 mid 47.0%, model 53.6% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11PAOBEJ-1-BEJ` Will Sara Bejlek win set 1 in the Jasmine Paolini vs Sara Bejlek match: 0.51/0.54 mid 52.5%, model 46.4% (projection_v2.0 (prediction ledger)) -- gap -6.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11PAOBEJ-2-BEJ` Will Sara Bejlek win set 2 in the Jasmine Paolini vs Sara Bejlek match: 0.51/0.54 mid 52.5%, model 46.4% (projection_v2.0 (prediction ledger)) -- gap -6.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; WIDE_SPREAD

## Mananchaya Sawangkaew vs Magdalena Frech -- WTA Wuhan R64

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-12 05:56Z
* Source: COURT_PROGRESSION: preceding match on Court 2 in progress (set 1 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 05:11Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-12T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211684:216566:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Magdalena Frech (`KXWTAMATCH-26OCT11SAWFRE-FRE`) | 0.57 / 0.58 (12724) | 57.5% | 43.5% | 36.1% | 38.6% [34.1%-51.6%] | 56.6% | 57.2% | 56.9% | MODEL_LONE_OUTLIER | PASS | -14.0 pp | REVIEW | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Mananchaya Sawangkaew (`KXWTAMATCH-26OCT11SAWFRE-SAW`) | 0.42 / 0.43 (25180) | 42.5% | 56.5% | 63.9% | 61.4% [48.4%-65.9%] | 43.4% | 42.8% | 43.1% | MODEL_LONE_OUTLIER | WATCH | +14.0 pp | REVIEW | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2947.0, B 4552.0; serve-point win A 57.7%, B 43.6%; Elo A 1868.7, B 1830.0; model uncertainty 0.0872
* Form inputs: days since last match A 0, B 0; matches on record A 343, B 700; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.041, surface_pool_high +0.040, surface_dev_loose +0.005, surface_dev_tight -0.010
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT11SAWFRE-21` Over 20.5 games: 0.57/0.58 mid 57.5%, model 68.0% (projection_v2.0 (prediction ledger)) -- gap +10.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT11SAWFRE-2-FRE` Will Magdalena Frech win set 2 in the Mananchaya Sawangkaew vs Magdalena Frech match: 0.54/0.57 mid 55.5%, model 45.6% (projection_v2.0 (prediction ledger)) -- gap -9.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT11SAWFRE-2-SAW` Will Mananchaya Sawangkaew win set 2 in the Mananchaya Sawangkaew vs Magdalena Frech match: 0.43/0.46 mid 44.5%, model 54.4% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26OCT11SAWFRE-26` Over 25.5 games: 0.32/0.38 mid 35.0%, model 44.7% (projection_v2.0 (prediction ledger)) -- gap +9.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT11SAWFRE-1-FRE` Will Magdalena Frech win set 1 in the Mananchaya Sawangkaew vs Magdalena Frech match: 0.54/0.56 mid 55.0%, model 45.6% (projection_v2.0 (prediction ledger)) -- gap -9.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT11SAWFRE-1-SAW` Will Mananchaya Sawangkaew win set 1 in the Mananchaya Sawangkaew vs Magdalena Frech match: 0.44/0.46 mid 45.0%, model 54.4% (projection_v2.0 (prediction ledger)) -- gap +9.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26OCT11SAWFRE-16` Over 15.5 games: 0.91/0.95 mid 93.0%, model 97.4% (projection_v2.0 (prediction ledger)) -- gap +4.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE

## Maria Sakkari vs Donna Vekic -- WTA Wuhan R64

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-12 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-12T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202499:206289:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Sakkari (`KXWTAMATCH-26OCT11SAKVEK-SAK`) | 0.60 / 0.61 (17544) | 60.5% | 54.7% | 56.2% | 56.8% [55.7%-59.4%] | 60.2% | 61.6% | 60.9% | MODEL_LONE_OUTLIER | PASS | -5.8 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Donna Vekic (`KXWTAMATCH-26OCT11SAKVEK-VEK`) | 0.39 / 0.40 (90800) | 39.5% | 45.3% | 43.8% | 43.2% [40.6%-44.3%] | 39.8% | 38.8% | 39.3% | MODEL_LONE_OUTLIER | WATCH | +5.8 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3640.0, B 4044.0; serve-point win A 58.9%, B 42.0%; Elo A 1931.5, B 1871.9; model uncertainty 0.0182
* Form inputs: days since last match A 6, B 6; matches on record A 857, B 751; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT11SAKVEK-22` Over 21.5 games: 0.49/0.51 mid 50.0%, model 64.0% (projection_v2.0 (prediction ledger)) -- gap +14.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT11SAKVEK-27` Over 26.5 games: 0.27/0.33 mid 30.0%, model 40.6% (projection_v2.0 (prediction ledger)) -- gap +10.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT11SAKVEK-17` Over 16.5 games: 0.85/0.90 mid 87.5%, model 94.7% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT11SAKVEK-1-SAK` Will Maria Sakkari win set 1 in the Maria Sakkari vs Donna Vekic match: 0.57/0.60 mid 58.5%, model 53.2% (projection_v2.0 (prediction ledger)) -- gap -5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11SAKVEK-1-VEK` Will Donna Vekic win set 1 in the Maria Sakkari vs Donna Vekic match: 0.41/0.42 mid 41.5%, model 46.8% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11SAKVEK-2-VEK` Will Donna Vekic win set 2 in the Maria Sakkari vs Donna Vekic match: 0.39/0.44 mid 41.5%, model 46.8% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT11SAKVEK-2-SAK` Will Maria Sakkari win set 2 in the Maria Sakkari vs Donna Vekic match: 0.56/0.60 mid 58.0%, model 53.2% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER

## Francisco Cabral / James Tracy vs Sander Arends / Luke Johnson -- ATP Shanghai R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-12T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12CABTRAAREJOH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sander Arends / Luke Johnson (`KXATPDOUBLES-26OCT12CABTRAAREJOH-AREJOH`) | 0.40 / 0.42 (1157) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Francisco Cabral / James Tracy (`KXATPDOUBLES-26OCT12CABTRAAREJOH-CABTRA`) | 0.58 / 0.59 (48) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Ilya Ivashka vs Kaichi Uchida -- ATP Challenger Jinan Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-12T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111187:125802:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ilya Ivashka (`KXATPCHALLENGERMATCH-26OCT12IVAUCH-IVA`) | 0.94 / 0.96 (247) | 95.0% | 81.4% | 90.5% | 87.1% [82.3%-89.6%] | 86.5% | 88.9% | 88.9% | MODEL_LONE_OUTLIER | PASS | -13.6 pp | REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Kaichi Uchida (`KXATPCHALLENGERMATCH-26OCT12IVAUCH-UCH`) | 0.04 / 0.05 (163) | 4.5% | 18.6% | 9.5% | 12.9% [10.4%-17.7%] | 13.5% | 10.9% | 10.9% | MODEL_LONE_OUTLIER | WATCH | +14.1 pp | REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 2118.0, B 2579.0; serve-point win A 69.0%, B 38.3%; Elo A 1718.5, B 1476.4; model uncertainty 0.0369
* Form inputs: days since last match A 35, B 20; matches on record A 599, B 762; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high -0.000, surface_dev_loose +0.009, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Hayato Matsuoka vs James McCabe -- ATP Challenger Jinan Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-12T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210317:211627:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hayato Matsuoka (`KXATPCHALLENGERMATCH-26OCT12MATMCC-MAT`) | 0.96 / 0.97 (27401) | 96.5% | 47.7% | 64.4% | 51.5% [46.1%-56.4%] | 57.2% | -- | 57.2% | MODEL_LONE_OUTLIER | PASS | -48.8 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| James McCabe (`KXATPCHALLENGERMATCH-26OCT12MATMCC-MCC`) | 0.03 / 0.04 (34992) | 3.5% | 52.3% | 35.6% | 48.5% [43.6%-53.9%] | 42.8% | -- | 42.8% | MODEL_LONE_OUTLIER | WATCH | +48.8 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 2224.0, B 3266.0; serve-point win A 65.1%, B 34.5%; Elo A 1447.7, B 1578.1; model uncertainty 0.0514
* Form inputs: days since last match A 19, B 13; matches on record A 108, B 293; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT12MATMCC-MCC  (YES = James McCabe)
Model: 52%
Kalshi: 4%
Gap: +49 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: SUPPORTS_MODEL_DIRECTION
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.034, surface_dev_loose +0.005, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Zhizhen Zhang / Yi Zhou vs Kevin Krawietz / Tim Putz -- ATP Shanghai R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-12T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12ZHAZHOKRAPUT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kevin Krawietz / Tim Putz (`KXATPDOUBLES-26OCT12ZHAZHOKRAPUT-KRAPUT`) | 0.77 / 0.79 (2510) | 78.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Zhizhen Zhang / Yi Zhou (`KXATPDOUBLES-26OCT12ZHAZHOKRAPUT-ZHAZHO`) | 0.21 / 0.24 (1123) | 22.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Caty McNally vs Yuliia Starodubtseva -- WTA Wuhan R64

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-12 07:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 06:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-12T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:216083:263857:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Caty McNally (`KXWTAMATCH-26OCT11MCCSTA-MCC`) | 0.61 / 0.62 (4285) | 61.5% | 54.8% | 50.0% | 52.6% [51.1%-55.8%] | -- | 61.8% | 61.8% | MARKETS_AGREE | PASS | -6.7 pp | NORMAL | FRESH | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Yuliia Starodubtseva (`KXWTAMATCH-26OCT11MCCSTA-STA`) | 0.38 / 0.39 (18386) | 38.5% | 45.2% | 50.0% | 47.3% [44.2%-48.9%] | -- | 38.6% | 38.6% | MARKETS_AGREE | SHADOW_BET | +6.7 pp | NORMAL | FRESH | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3757.0, B 4584.0; serve-point win A 56.2%, B 44.7%; Elo A 1869.3, B 1808.5; model uncertainty 0.0238
* Form inputs: days since last match A 173, B 10; matches on record A 313, B 261; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.005, surface_dev_loose -0.016, surface_dev_tight +0.016
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 4 carry a model probability
  * `KXWTASETWINNER-26OCT11MCCSTA-2-STA` Will Yuliia Starodubtseva win set 2 in the Catherine McNally vs Yuliia Starodubtseva match: 0.38/0.42 mid 40.0%, model 46.8% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT11MCCSTA-2-MCC` Will Catherine McNally win set 2 in the Catherine McNally vs Yuliia Starodubtseva match: 0.58/0.61 mid 59.5%, model 53.2% (projection_v2.0 (prediction ledger)) -- gap -6.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT11MCCSTA-1-MCC` Will Catherine McNally win set 1 in the Catherine McNally vs Yuliia Starodubtseva match: 0.58/0.60 mid 59.0%, model 53.2% (projection_v2.0 (prediction ledger)) -- gap -5.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT11MCCSTA-1-STA` Will Yuliia Starodubtseva win set 1 in the Catherine McNally vs Yuliia Starodubtseva match: 0.39/0.43 mid 41.0%, model 46.8% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tereza Mihalikova / Olivia Nicholls vs Hao-Ching Chan / Miyu (1994) Kato -- WTA Wuhan R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-12 07:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 06:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-12T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT11MIHNICCHAKAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hao-Ching Chan / Miyu (1994) Kato (`KXWTADOUBLES-26OCT11MIHNICCHAKAT-CHAKAT`) | 0.40 / 0.42 (20) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tereza Mihalikova / Olivia Nicholls (`KXWTADOUBLES-26OCT11MIHNICCHAKAT-MIHNIC`) | 0.57 / 0.60 (3773) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Lucie Nguyen Tan vs Ruth Roura Llaverias -- WTA 125K Mallorca Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 11:00Z
* Current expected start: 2026-10-12 08:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 07:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Grass · scheduled 2026-10-12T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221468:260763:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucie Nguyen Tan (`KXWTACHALLENGERMATCH-26OCT12NGUROU-NGU`) | 0.40 / 0.42 (16211) | 41.0% | -- | 73.8% | 69.3% [64.0%-73.0%] | 40.8% | -- | 40.8% | MODEL_LONE_OUTLIER | WATCH | +28.3 pp | EXTREME (DATA_WARNING) | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Ruth Roura Llaverias (`KXWTACHALLENGERMATCH-26OCT12NGUROU-ROU`) | 0.59 / 0.60 (556) | 59.5% | -- | 26.2% | 30.7% [27.1%-36.0%] | 59.2% | -- | 59.2% | MODEL_LONE_OUTLIER | PASS | -28.8 pp | EXTREME (DATA_WARNING) | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1887.0, B 1893.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0446
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTACHALLENGERMATCH-26OCT12NGUROU-NGU  (YES = Lucie Nguyen Tan)
Model: 69%
Kalshi: 41%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: A (LIMITED)
Reasons: SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Ida Wobker vs Cristina Diaz Adrover -- WTA 125K Mallorca Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 11:00Z
* Current expected start: 2026-10-12 08:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 07:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Grass · scheduled 2026-10-12T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:232881:270076:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cristina Diaz Adrover (`KXWTACHALLENGERMATCH-26OCT12WOBDIA-DIA`) | 0.15 / 0.16 (1627) | 15.5% | -- | 42.5% | 45.7% [43.1%-47.9%] | 18.8% | -- | 18.8% | KALSHI_LONE_OUTLIER | WATCH | +30.2 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Ida Wobker (`KXWTACHALLENGERMATCH-26OCT12WOBDIA-WOB`) | 0.83 / 0.85 (3344) | 84.0% | -- | 57.5% | 54.3% [52.1%-56.9%] | 81.2% | -- | 81.2% | KALSHI_LONE_OUTLIER | PASS | -29.7 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1220.0, B 3491.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.024
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXWTACHALLENGERMATCH-26OCT12WOBDIA-DIA  (YES = Cristina Diaz Adrover)
Model: 46%
Kalshi: 16%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, SURFACE_DATA_THIN, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Luka Pavlovic vs Kangyuan Shi -- ATP Challenger Jinan Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-12T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12PAVSHI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luka Pavlovic (`KXATPCHALLENGERMATCH-26OCT12PAVSHI-PAV`) | 0.98 / 0.99 (9965) | 98.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kangyuan Shi (`KXATPCHALLENGERMATCH-26OCT12PAVSHI-SHI`) | 0.01 / 0.02 (87137) | 1.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Anna-Lena Friedsam vs Tessa Johanna Brockmann -- WTA 125K Rovereto Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 11:30Z
* Current expected start: 2026-10-12 08:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 07:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Hard · scheduled 2026-10-12T11:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:204431:260598:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tessa Johanna Brockmann (`KXWTACHALLENGERMATCH-26OCT12FRIBRO-BRO`) | 0.29 / 0.30 (1847) | 29.5% | -- | 55.2% | 49.0% [43.8%-51.5%] | 31.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +19.5 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna-Lena Friedsam (`KXWTACHALLENGERMATCH-26OCT12FRIBRO-FRI`) | 0.69 / 0.71 (549) | 70.0% | -- | 44.8% | 51.0% [48.4%-56.2%] | 68.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.0 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3834.0, B 3426.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.039
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTACHALLENGERMATCH-26OCT12FRIBRO-BRO  (YES = Tessa Johanna Brockmann)
Model: 49%
Kalshi: 30%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.015, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Elsa Jacquemot vs Lea Boskovic -- WTA 125K Rovereto Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 11:30Z
* Current expected start: 2026-10-12 08:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 07:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Hard · scheduled 2026-10-12T11:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:214521:221039:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lea Boskovic (`KXWTACHALLENGERMATCH-26OCT12JACBOS-BOS`) | 0.24 / 0.25 (1636) | 24.5% | -- | 44.8% | 42.7% [38.0%-43.7%] | 25.7% | 24.7% | 24.7% | MODEL_LONE_OUTLIER | WATCH | +18.2 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Elsa Jacquemot (`KXWTACHALLENGERMATCH-26OCT12JACBOS-JAC`) | 0.75 / 0.76 (1874) | 75.5% | -- | 55.2% | 57.3% [56.3%-62.0%] | 74.3% | 76.1% | 76.1% | MODEL_LONE_OUTLIER | PASS | -18.2 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4592.0, B 2773.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0284
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTACHALLENGERMATCH-26OCT12JACBOS-BOS  (YES = Lea Boskovic)
Model: 43%
Kalshi: 24%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: EXTERNAL_STALE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.005, surface_dev_loose -0.011, surface_dev_tight +0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Liam Draxl vs Omar Jasika -- ATP Challenger Jinan Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 08:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-12T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:117357:208119:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liam Draxl (`KXATPCHALLENGERMATCH-26OCT12DRAJAS-DRA`) | 0.75 / 0.76 (355) | 75.5% | 76.4% | 84.1% | 80.8% [78.6%-82.9%] | 75.0% | 76.4% | 75.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +0.9 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Omar Jasika (`KXATPCHALLENGERMATCH-26OCT12DRAJAS-JAS`) | 0.24 / 0.25 (19985) | 24.5% | 23.6% | 15.9% | 19.2% [17.1%-21.4%] | 25.0% | 23.9% | 24.4% | MODEL_LONE_OUTLIER | PASS | -0.9 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3235.0, B 2343.0; serve-point win A 63.8%, B 41.8%; Elo A 1693.1, B 1509.5; model uncertainty 0.0211
* Form inputs: days since last match A 6, B 13; matches on record A 329, B 462; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.011, surface_dev_loose +0.007, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Marat Sharipov vs Jake Delaney -- ATP Challenger Jinan Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 08:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-12T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:117359:129911:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jake Delaney (`KXATPCHALLENGERMATCH-26OCT12SHADEL-DEL`) | 0.16 / 0.18 (9495) | 17.0% | 8.8% | 5.0% | 8.2% [6.7%-9.5%] | 19.7% | 17.0% | 17.0% | MODEL_LONE_OUTLIER | PASS | -8.2 pp | NORMAL | FRESH | B / LIMITED | EXTERNAL_STALE | VERIFIED |
| Marat Sharipov (`KXATPCHALLENGERMATCH-26OCT12SHADEL-SHA`) | 0.83 / 0.84 (14031) | 83.5% | 91.2% | 95.0% | 91.8% [90.5%-93.3%] | 80.3% | 83.4% | 83.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +7.7 pp | NORMAL | FRESH | B / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 2250.0, B 901.0; serve-point win A 74.8%, B 36.7%; Elo A 1716.3, B 1347.1; model uncertainty 0.0142
* Form inputs: days since last match A 13, B 20; matches on record A 253, B 256; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.006, surface_dev_loose +0.007, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Xirui Han vs Anthony Susanto -- M25 Qian Daohu R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-12T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200045:212472:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xirui Han (`KXITFMATCH-26OCT11HANSUS-HAN`) | 0.66 / 0.68 (2461) | 67.0% | 75.8% | 77.4% | 76.9% [76.9%-77.8%] | -- | -- | -- | -- | PASS | +8.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Anthony Susanto (`KXITFMATCH-26OCT11HANSUS-SUS`) | 0.33 / 0.34 (3155) | 33.5% | 24.2% | 22.6% | 23.1% [22.2%-23.1%] | -- | -- | -- | -- | PASS | -9.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 102.0; serve-point win A 64.5%, B 41.0%; Elo A 1259.6, B 1048.5; model uncertainty 0.0043
* Form inputs: days since last match A 756, B 665; matches on record A 5, B 49; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.008, surface_dev_loose +0.001, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kristjan Tamm vs Yue Xia -- M25 Qian Daohu R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT11TAMXIA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kristjan Tamm (`KXITFMATCH-26OCT11TAMXIA-TAM`) | 0.85 / 0.89 (35) | 87.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yue Xia (`KXITFMATCH-26OCT11TAMXIA-XIA`) | 0.12 / 0.14 (71) | 13.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zhao Zhao vs Lingxi Zhao -- M25 Qian Daohu R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-12T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206789:206888:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zhao Zhao (`KXITFMATCH-26OCT11ZHAZHA2-ZHA`) | 0.55 / 0.57 (111) | 56.0% | 36.0% | 43.4% | 40.0% [38.0%-40.9%] | -- | -- | -- | -- | PASS | -20.0 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lingxi Zhao (`KXITFMATCH-26OCT11ZHAZHA2-ZHA2`) | 0.41 / 0.43 (23) | 42.0% | 64.0% | 56.6% | 60.0% [59.1%-62.0%] | -- | -- | -- | -- | PASS | +22.0 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 118.0, B 0.0; serve-point win A 60.4%, B 36.8%; Elo A 1180.9, B 1254.0; model uncertainty 0.0149
* Form inputs: days since last match A 189, B 672; matches on record A 24, B 30; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT11ZHAZHA2-ZHA2  (YES = Lingxi Zhao)
Model: 64%
Kalshi: 42%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.019, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kaito Uesugi vs Yosuke Watanuki -- ATP Challenger Jinan Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 09:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-12T09:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133297:144682:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kaito Uesugi (`KXATPCHALLENGERMATCH-26OCT12UESWAT-UES`) | 0.09 / 0.10 (1277) | 9.5% | 14.8% | 39.5% | 17.1% [13.3%-20.5%] | 12.6% | 10.0% | 10.0% | MODEL_LONE_OUTLIER | PASS | +5.3 pp | NORMAL | FRESH | D / POOR | EXTERNAL_STALE | VERIFIED |
| Yosuke Watanuki (`KXATPCHALLENGERMATCH-26OCT12UESWAT-WAT`) | 0.90 / 0.91 (2714) | 90.5% | 85.2% | 60.5% | 82.9% [79.5%-86.7%] | 87.4% | 90.1% | 90.1% | MODEL_LONE_OUTLIER | PASS | -5.3 pp | NORMAL | FRESH | D / POOR | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 457.0, B 2346.0; serve-point win A 58.0%, B 33.7%; Elo A 1389.8, B 1726.0; model uncertainty 0.0357
* Form inputs: days since last match A 413, B 35; matches on record A 121, B 413; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.013, surface_dev_loose +0.006, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE

## Lidia Encheva vs Daria Yesypchuk -- WTA 125K Mallorca Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 12:10Z
* Current expected start: 2026-10-12 09:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 08:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Grass · scheduled 2026-10-12T12:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:260032:260565:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lidia Encheva (`KXWTACHALLENGERMATCH-26OCT12ENCYES-ENC`) | 0.66 / 0.68 (124) | 67.0% | -- | 54.8% | 58.0% [56.9%-60.6%] | 67.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.0 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daria Yesypchuk (`KXWTACHALLENGERMATCH-26OCT12ENCYES-YES`) | 0.32 / 0.33 (585) | 32.5% | -- | 45.2% | 42.0% [39.4%-43.1%] | 32.9% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +9.5 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2702.0, B 2518.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0182
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Aran Teixido Garcia vs Laura Samson -- WTA 125K Mallorca R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 12:30Z
* Current expected start: 2026-10-12 09:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 08:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-12T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT12TEISAM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Laura Samson (`KXWTACHALLENGERMATCH-26OCT12TEISAM-SAM`) | 0.87 / 0.88 (2578) | 87.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aran Teixido Garcia (`KXWTACHALLENGERMATCH-26OCT12TEISAM-TEI`) | 0.12 / 0.13 (9136) | 12.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Eva Vedder vs Francesca Curmi -- WTA 125K Mallorca R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 12:30Z
* Current expected start: 2026-10-12 09:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 08:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Grass · scheduled 2026-10-12T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220770:221014:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesca Curmi (`KXWTACHALLENGERMATCH-26OCT12VEDCUR-CUR`) | 0.59 / 0.60 (168) | 59.5% | -- | 64.4% | 59.4% [53.7%-62.9%] | 58.4% | 59.2% | 59.2% | MARKETS_AGREE | PASS | -0.1 pp | NORMAL | FRESH | A / LIMITED | EXTERNAL_STALE | VERIFIED |
| Eva Vedder (`KXWTACHALLENGERMATCH-26OCT12VEDCUR-VED`) | 0.39 / 0.41 (733) | 40.0% | -- | 35.6% | 40.6% [37.1%-46.3%] | 41.6% | 40.8% | 40.8% | MARKETS_AGREE | PASS | +0.6 pp | NORMAL | FRESH | A / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3271.0, B 2628.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0461
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Kabir Hans vs Adil Kalyanpur -- M25 Solapur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-12T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200681:212069:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kabir Hans (`KXITFMATCH-26OCT11HANKAL-HAN`) | 0.44 / 0.45 (3529) | 44.5% | 54.1% | 72.2% | 59.1% [55.1%-62.0%] | -- | -- | -- | -- | PASS | +9.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Adil Kalyanpur (`KXITFMATCH-26OCT11HANKAL-KAL`) | 0.53 / 0.54 (10) | 53.5% | 45.9% | 27.9% | 40.9% [38.0%-44.9%] | -- | -- | -- | -- | PASS | -7.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 84.0; serve-point win A 61.9%, B 38.9%; Elo A 1190.7, B 1128.5; model uncertainty 0.0349
* Form inputs: days since last match A 693, B 546; matches on record A 22, B 139; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.040, surface_pool_high +0.029, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Erika Andreeva vs Zongyu Li -- WTA 125K Rovereto Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 12:40Z
* Current expected start: 2026-10-12 10:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 09:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Hard · scheduled 2026-10-12T12:40:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:222965:252493:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Erika Andreeva (`KXWTACHALLENGERMATCH-26OCT12ANDZON-AND`) | 0.80 / 0.81 (969) | 80.5% | -- | 62.8% | 64.8% [60.8%-70.6%] | 79.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.7 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zongyu Li (`KXWTACHALLENGERMATCH-26OCT12ANDZON-ZON`) | 0.19 / 0.20 (977) | 19.5% | -- | 37.2% | 35.2% [29.4%-39.2%] | 20.8% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +15.7 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3408.0, B 1900.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0487
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTACHALLENGERMATCH-26OCT12ANDZON-ZON  (YES = Zongyu Li)
Model: 35%
Kalshi: 20%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.033, surface_pool_high -0.040, surface_dev_loose -0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Gina Feistel vs Tena Lukas -- WTA 125K Lisbon Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 13:00Z
* Current expected start: 2026-10-12 10:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 09:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Clay · scheduled 2026-10-12T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:211329:252531:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gina Feistel (`KXWTACHALLENGERMATCH-26OCT12FEILUK-FEI`) | 0.66 / 0.68 (1) | 67.0% | -- | 75.3% | 64.7% [58.0%-69.0%] | 66.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.3 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tena Lukas (`KXWTACHALLENGERMATCH-26OCT12FEILUK-LUK`) | 0.31 / 0.33 (395) | 32.0% | -- | 24.7% | 35.3% [31.0%-42.0%] | 33.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +3.3 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1907.0, B 2775.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0554
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose +0.020, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE

## Anouk Koevermans vs Caroline Werner -- WTA 125K Rovereto Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 12:40Z
* Current expected start: 2026-10-12 10:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 09:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Hard · scheduled 2026-10-12T12:40:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:222017:espn:espn:4384:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anouk Koevermans (`KXWTACHALLENGERMATCH-26OCT12KOEWER-KOE`) | 0.61 / 0.63 (936) | 62.0% | -- | 84.9% | 56.3% [47.9%-64.5%] | 61.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Caroline Werner (`KXWTACHALLENGERMATCH-26OCT12KOEWER-WER`) | 0.37 / 0.39 (7119) | 38.0% | -- | 15.1% | 43.7% [35.5%-52.1%] | 38.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2985.0, B 0.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0831
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.082, surface_pool_high -0.084, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE

## Mathilde Lollia vs Loes Ebeling Koning -- WTA 125K Lisbon Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 13:00Z
* Current expected start: 2026-10-12 10:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 09:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Clay · scheduled 2026-10-12T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221443:266901:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Loes Ebeling Koning (`KXWTACHALLENGERMATCH-26OCT12LOLEBE-EBE`) | 0.81 / 0.82 (10005) | 81.5% | -- | 71.9% | 62.9% [50.0%-67.8%] | 78.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -18.6 pp | HIGH_REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mathilde Lollia (`KXWTACHALLENGERMATCH-26OCT12LOLEBE-LOL`) | 0.18 / 0.19 (1161) | 18.5% | -- | 28.1% | 37.1% [32.2%-50.0%] | 22.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +18.6 pp | HIGH_REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2163.0, B 1642.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0888
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B

```
DISCREPANCY SANITY CHECK  KXWTACHALLENGERMATCH-26OCT12LOLEBE-LOL  (YES = Mathilde Lollia)
Model: 37%
Kalshi: 18%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.030, surface_pool_high -0.020, surface_dev_loose -0.025, surface_dev_tight +0.035
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Adrienn Nagy vs Iva Primorac Pavicic -- WTA 125K Lisbon Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 13:00Z
* Current expected start: 2026-10-12 10:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 09:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Clay · scheduled 2026-10-12T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:206248:215909:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrienn Nagy (`KXWTACHALLENGERMATCH-26OCT12NAGPRI-NAG`) | 0.53 / 0.54 (1412) | 53.5% | -- | 62.5% | 47.4% [40.0%-52.6%] | 53.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.1 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Iva Primorac Pavicic (`KXWTACHALLENGERMATCH-26OCT12NAGPRI-PRI`) | 0.47 / 0.48 (7272) | 47.5% | -- | 37.5% | 52.6% [47.4%-60.0%] | 46.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +5.1 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1856.0, B 1407.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0631
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.021, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Martin Landaluce vs Ilia Simakin -- ATP Challenger Jinan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-12T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209899:212021:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martin Landaluce (`KXATPCHALLENGERMATCH-26OCT12LANSIM-LAN`) | 0.58 / 0.59 (8296) | 58.5% | 52.4% | 38.2% | 41.1% [38.7%-53.0%] | 58.4% | 58.7% | 58.5% | MODEL_LONE_OUTLIER | PASS | -6.1 pp | NORMAL | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Ilia Simakin (`KXATPCHALLENGERMATCH-26OCT12LANSIM-SIM`) | 0.41 / 0.42 (12924) | 41.5% | 47.6% | 61.8% | 58.9% [47.0%-61.3%] | 41.6% | 41.9% | 41.8% | MODEL_LONE_OUTLIER | PASS | +6.1 pp | NORMAL | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3597.0, B 3713.0; serve-point win A 64.2%, B 36.2%; Elo A 1706.0, B 1720.5; model uncertainty 0.0714
* Form inputs: days since last match A 693, B 4; matches on record A 115, B 239; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.029, surface_pool_high -0.019, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Hitesh Chauhan vs Vraj Gohil -- M25 Solapur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 10:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12CHAGOH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hitesh Chauhan (`KXITFMATCH-26OCT12CHAGOH-CHA`) | 0.91 / 0.92 (303) | 91.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vraj Gohil (`KXITFMATCH-26OCT12CHAGOH-GOH`) | 0.07 / 0.08 (92) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Udit Kamboj vs Prasad Ingale -- M25 Solapur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 10:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12KAMING:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Prasad Ingale (`KXITFMATCH-26OCT12KAMING-ING`) | 0.05 / 0.07 (15000) | 6.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Udit Kamboj (`KXITFMATCH-26OCT12KAMING-KAM`) | 0.94 / 0.95 (148) | 94.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mayand Tewary vs Caheer Warik -- M25 Solapur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 10:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12TEWWAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mayand Tewary (`KXITFMATCH-26OCT12TEWWAR-TEW`) | 0.05 / 0.18 (24) | 11.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Caheer Warik (`KXITFMATCH-26OCT12TEWWAR-WAR`) | 0.20 / 0.88 (23) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Julia Grabher vs Deborah Chiesa -- WTA 125K Mallorca R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 13:40Z
* Current expected start: 2026-10-12 11:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 10:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Grass · scheduled 2026-10-12T13:40:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:211328:211814:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Deborah Chiesa (`KXWTACHALLENGERMATCH-26OCT12GRACHI-CHI`) | 0.24 / 0.25 (327) | 24.5% | -- | 58.9% | 47.9% [34.5%-53.7%] | 26.0% | 24.5% | 25.3% | MODEL_LONE_OUTLIER | WATCH | +23.4 pp | HIGH_REVIEW | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Julia Grabher (`KXWTACHALLENGERMATCH-26OCT12GRACHI-GRA`) | 0.75 / 0.76 (8390) | 75.5% | -- | 41.1% | 52.1% [46.3%-65.5%] | 74.0% | 74.9% | 74.5% | MODEL_LONE_OUTLIER | PASS | -23.4 pp | HIGH_REVIEW | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3872.0, B 2456.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0962
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTACHALLENGERMATCH-26OCT12GRACHI-CHI  (YES = Deborah Chiesa)
Model: 48%
Kalshi: 24%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: A (LIMITED)
Reasons: SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Jennifer Ruggeri vs Elizara Yaneva -- WTA 125K Mallorca R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 13:40Z
* Current expected start: 2026-10-12 11:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 10:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Grass · scheduled 2026-10-12T13:40:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221411:260664:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jennifer Ruggeri (`KXWTACHALLENGERMATCH-26OCT12RUGYAN-RUG`) | 0.40 / 0.41 (211) | 40.5% | -- | 32.5% | 32.5% [31.0%-33.9%] | 41.6% | 41.3% | 41.5% | MODEL_LONE_OUTLIER | PASS | -8.0 pp | NORMAL | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Elizara Yaneva (`KXWTACHALLENGERMATCH-26OCT12RUGYAN-YAN`) | 0.59 / 0.60 (14383) | 59.5% | -- | 67.5% | 67.5% [66.1%-69.0%] | 58.4% | 58.8% | 58.6% | MODEL_LONE_OUTLIER | SHADOW_BET | +8.0 pp | NORMAL | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3454.0, B 2860.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0145
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Sebastian Gima vs Pedro Vives Marcos -- ATP Challenger Catania Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-12T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206325:209142:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sebastian Gima (`KXATPCHALLENGERMATCH-26OCT12GIMVIV-GIM`) | 0.27 / 0.28 (1646) | 27.5% | 30.5% | 38.0% | 35.6% [34.6%-36.6%] | 32.3% | -- | 32.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +3.0 pp | NORMAL | FRESH | B / LIMITED | ALL_AGREE | VERIFIED |
| Pedro Vives Marcos (`KXATPCHALLENGERMATCH-26OCT12GIMVIV-VIV`) | 0.72 / 0.73 (263) | 72.5% | 69.5% | 62.0% | 64.4% [63.4%-65.4%] | 67.7% | -- | 67.7% | MODEL_LONE_OUTLIER | PASS | -3.0 pp | NORMAL | FRESH | B / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 833.0, B 561.0; serve-point win A 59.7%, B 36.3%; Elo A 1408.1, B 1522.4; model uncertainty 0.0097
* Form inputs: days since last match A 21, B 42; matches on record A 297, B 171; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER

## Dimitar Kuzmanov vs Matyas Cerny -- ATP Challenger Olbia Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-12T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106220:210063:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matyas Cerny (`KXATPCHALLENGERMATCH-26OCT12KUZCER-CER`) | 0.17 / 0.18 (1583) | 17.5% | 24.6% | 45.9% | 23.1% [16.4%-30.6%] | 20.8% | -- | 20.8% | ALL_THREE_DISAGREE | WATCH | +7.1 pp | NORMAL | FRESH | C / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Dimitar Kuzmanov (`KXATPCHALLENGERMATCH-26OCT12KUZCER-KUZ`) | 0.81 / 0.82 (81) | 81.5% | 75.4% | 54.1% | 76.9% [69.4%-83.6%] | 79.2% | -- | 79.2% | MODEL_LONE_OUTLIER | PASS | -6.1 pp | NORMAL | FRESH | C / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3650.0, B 342.0; serve-point win A 62.5%, B 42.8%; Elo A 1564.0, B 1314.1; model uncertainty 0.0711
* Form inputs: days since last match A 14, B 77; matches on record A 885, B 55; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.041, surface_pool_high -0.054, surface_dev_loose -0.003, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER

## Christian Langmo vs Viktor Durasovic -- ATP Challenger Olbia Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-12T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126340:132052:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Viktor Durasovic (`KXATPCHALLENGERMATCH-26OCT12LANDUR-DUR`) | 0.44 / 0.45 (1717) | 44.5% | 55.5% | 56.8% | 55.4% [53.4%-58.4%] | 44.6% | 44.7% | 44.6% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.9 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Christian Langmo (`KXATPCHALLENGERMATCH-26OCT12LANDUR-LAN`) | 0.54 / 0.56 (6430) | 55.0% | 44.5% | 43.2% | 44.6% [41.6%-46.6%] | 55.4% | 56.0% | 55.7% | ALL_THREE_DISAGREE | PASS | -10.4 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2013.0, B 2619.0; serve-point win A 64.9%, B 34.0%; Elo A 1419.0, B 1450.8; model uncertainty 0.0246
* Form inputs: days since last match A 35, B 14; matches on record A 374, B 685; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.029, surface_pool_high +0.019, surface_dev_loose -0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER

## Ivan Marrero Curbelo vs Niels Visker -- ATP Challenger Olbia Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-12T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202326:208253:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ivan Marrero Curbelo (`KXATPCHALLENGERMATCH-26OCT12MARVIS-MAR`) | 0.37 / 0.38 (393) | 37.5% | 46.5% | 72.3% | 47.5% [39.2%-57.3%] | 38.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +9.0 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Niels Visker (`KXATPCHALLENGERMATCH-26OCT12MARVIS-VIS`) | 0.61 / 0.63 (7131) | 62.0% | 53.5% | 27.7% | 52.5% [42.7%-60.8%] | 61.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.5 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1114.0, B 1205.0; serve-point win A 64.8%, B 34.4%; Elo A 1269.6, B 1418.8; model uncertainty 0.0902
* Form inputs: days since last match A 35, B 14; matches on record A 155, B 182; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.000, surface_dev_loose +0.020, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

## Pedro Rodenas vs Svyatoslav Gulin -- ATP Challenger Catania Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-12T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210203:210425:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Svyatoslav Gulin (`KXATPCHALLENGERMATCH-26OCT12RODGUL-GUL`) | 0.59 / 0.60 (2795) | 59.5% | 58.4% | 55.7% | 54.2% [54.1%-55.2%] | 59.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pedro Rodenas (`KXATPCHALLENGERMATCH-26OCT12RODGUL-ROD`) | 0.39 / 0.40 (1728) | 39.5% | 41.6% | 44.3% | 45.8% [44.8%-45.9%] | 40.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 585.0, B 1022.0; serve-point win A 57.6%, B 40.7%; Elo A 1465.0, B 1491.8; model uncertainty 0.0058
* Form inputs: days since last match A 728, B 35; matches on record A 73, B 186; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

## Stefanos Sakellaridis vs Keegan Smith -- ATP Challenger Jinan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-12T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202333:208852:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefanos Sakellaridis (`KXATPCHALLENGERMATCH-26OCT12SAKSMI-SAK`) | 0.59 / 0.60 (8762) | 59.5% | 68.1% | 51.0% | 57.2% [52.9%-74.5%] | 58.4% | 60.5% | 60.5% | MODEL_LONE_OUTLIER | PASS | +8.6 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Keegan Smith (`KXATPCHALLENGERMATCH-26OCT12SAKSMI-SMI`) | 0.40 / 0.41 (334) | 40.5% | 31.9% | 49.0% | 42.8% [25.5%-47.1%] | 41.6% | 39.7% | 39.7% | MODEL_LONE_OUTLIER | PASS | -8.6 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3408.0, B 2747.0; serve-point win A 68.8%, B 35.1%; Elo A 1606.8, B 1478.1; model uncertainty 0.1079
* Form inputs: days since last match A 7, B 49; matches on record A 321, B 240; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.033, surface_pool_high -0.034, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

## Matthew Shearer vs Siu Chi Nicholas Cheng -- M25 Qian Daohu R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12SHECHE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Siu Chi Nicholas Cheng (`KXITFMATCH-26OCT12SHECHE-CHE`) | 0.30 / 0.39 (69) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matthew Shearer (`KXITFMATCH-26OCT12SHECHE-SHE`) | 0.57 / 0.63 (5) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Wishaya Trongcharoenchaikul vs Jordan Chiu -- M25 Qian Daohu R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-12T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106397:207780:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jordan Chiu (`KXITFMATCH-26OCT12TROCHI-CHI`) | 0.33 / 0.38 (8) | 35.5% | 13.6% | 75.2% | 17.9% [16.1%-19.4%] | -- | -- | -- | -- | PASS | -21.9 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Wishaya Trongcharoenchaikul (`KXITFMATCH-26OCT12TROCHI-TRO`) | 0.59 / 0.60 (62) | 59.5% | 86.4% | 24.8% | 82.0% [80.6%-83.9%] | -- | -- | -- | -- | PASS | +26.9 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 520.0, B 0.0; serve-point win A 69.0%, B 39.9%; Elo A 1274.4, B 1011.4; model uncertainty 0.0166
* Form inputs: days since last match A 272, B 671; matches on record A 466, B 22; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT12TROCHI-TRO  (YES = Wishaya Trongcharoenchaikul)
Model: 86%
Kalshi: 60%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.013, surface_dev_loose -0.001, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jakub Vrba vs Daniel Siniakov -- ATP Challenger Catania Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-12T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12VRBSIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Siniakov (`KXATPCHALLENGERMATCH-26OCT12VRBSIN-SIN`) | 0.65 / 0.66 (3323) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jakub Vrba (`KXATPCHALLENGERMATCH-26OCT12VRBSIN-VRB`) | 0.33 / 0.34 (997) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Aneta Kucmova vs Maria Garcia Cid -- WTA 125K Mallorca Q3

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-12 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-12T04:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

WTA125 (WTA_125) · Grass · scheduled 2026-10-12T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:225850:espn:espn:17027:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Garcia Cid (`KXWTACHALLENGERMATCH-26OCT12KUCGAR-GAR`) | 0.72 / 0.73 (7940) | 72.5% | -- | 83.1% | 55.3% [55.3%-55.3%] | 70.6% | 72.0% | 71.3% | MODEL_LONE_OUTLIER | PASS | -17.2 pp | HIGH_REVIEW | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Aneta Kucmova (`KXWTACHALLENGERMATCH-26OCT12KUCGAR-KUC`) | 0.27 / 0.28 (1452) | 27.5% | -- | 16.9% | 44.7% [44.7%-44.7%] | 29.4% | 28.4% | 28.9% | MODEL_LONE_OUTLIER | PASS | +17.2 pp | HIGH_REVIEW | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 0.0, B 1857.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXWTACHALLENGERMATCH-26OCT12KUCGAR-KUC  (YES = Aneta Kucmova)
Model: 45%
Kalshi: 28%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE

## Fajing Sun vs Jie Cui -- ATP Challenger Jinan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 11:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-12T11:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111806:200666:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jie Cui (`KXATPCHALLENGERMATCH-26OCT12SUNCUI-CUI`) | 0.55 / 0.56 (5186) | 55.5% | 46.4% | 34.7% | 38.4% [36.6%-40.3%] | 53.1% | 54.2% | 53.6% | MODEL_LONE_OUTLIER | PASS | -9.1 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Fajing Sun (`KXATPCHALLENGERMATCH-26OCT12SUNCUI-SUN`) | 0.45 / 0.46 (9199) | 45.5% | 53.6% | 65.3% | 61.6% [59.7%-63.4%] | 46.9% | 45.7% | 46.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +8.1 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3209.0, B 2196.0; serve-point win A 65.8%, B 34.9%; Elo A 1554.2, B 1514.3; model uncertainty 0.0187
* Form inputs: days since last match A 13, B 7; matches on record A 492, B 277; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.004, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Tommy Paul vs Valentin Vacherot -- ATP Shanghai R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 07:00Z
* Current expected start: 2026-10-12 11:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 10:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+270_MIN

ATP (MASTERS_1000) · Hard · scheduled 2026-10-12T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126205:200473:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tommy Paul (`KXATPMATCH-26OCT12PAUVAC-PAU`) | 0.58 / 0.60 (101200) | 59.0% | 65.8% | 70.3% | 71.6% [70.3%-72.8%] | 58.3% | 59.0% | 58.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.8 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Valentin Vacherot (`KXATPMATCH-26OCT12PAUVAC-VAC`) | 0.41 / 0.42 (194039) | 41.5% | 34.2% | 29.7% | 28.4% [27.2%-29.7%] | 41.7% | 40.8% | 41.3% | MODEL_LONE_OUTLIER | PASS | -7.3 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5900.0, B 3666.0; serve-point win A 68.4%, B 35.0%; Elo A 2031.4, B 1841.3; model uncertainty 0.0129
* Form inputs: days since last match A 2, B 2; matches on record A 717, B 387; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.008, surface_dev_loose -0.001, surface_dev_tight +0.001
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT12PAUVAC-VAC2` Will Valentin Vacherot win at least 1.5 more games than Tommy Paul?: 0.37/0.39 mid 38.0%, model 26.9% (projection_v2.0 (prediction ledger)) -- gap -11.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT12PAUVAC-29` Over 28.5 games: 0.27/0.30 mid 28.5%, model 38.0% (projection_v2.0 (prediction ledger)) -- gap +9.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT12PAUVAC-24` Over 23.5 games: 0.45/0.46 mid 45.5%, model 54.5% (projection_v2.0 (prediction ledger)) -- gap +9.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT12PAUVAC-19` Over 18.5 games: 0.81/0.85 mid 83.0%, model 90.7% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT12PAUVAC-VAC20` Will Valentin Vacherot win the Tommy Paul vs Valentin Vacherot match by a set score of 2-0?: 0.21/0.24 mid 22.5%, model 15.4% (projection_v2.0 (prediction ledger)) -- gap -7.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT12PAUVAC-PAU21` Will Tommy Paul win the Tommy Paul vs Valentin Vacherot match by a set score of 2-1?: 0.21/0.23 mid 22.0%, model 29.0% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT12PAUVAC-PAU2` Will Tommy Paul win at least 1.5 more games than Valentin Vacherot?: 0.52/0.53 mid 52.5%, model 58.0% (projection_v2.0 (prediction ledger)) -- gap +5.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT12PAUVAC-2-PAU` Will Tommy Paul win set 2 in the Tommy Paul vs Valentin Vacherot match: 0.54/0.59 mid 56.5%, model 60.7% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT12PAUVAC-1-PAU` Will Tommy Paul win set 1 in the Tommy Paul vs Valentin Vacherot match: 0.56/0.58 mid 57.0%, model 60.7% (projection_v2.0 (prediction ledger)) -- gap +3.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT12PAUVAC-1-VAC` Will Valentin Vacherot win set 1 in the Tommy Paul vs Valentin Vacherot match: 0.42/0.43 mid 42.5%, model 39.3% (projection_v2.0 (prediction ledger)) -- gap -3.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT12PAUVAC-2-VAC` Will Valentin Vacherot win set 2 in the Tommy Paul vs Valentin Vacherot match: 0.41/0.44 mid 42.5%, model 39.3% (projection_v2.0 (prediction ledger)) -- gap -3.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT12PAUVAC-PAU20` Will Tommy Paul win the Tommy Paul vs Valentin Vacherot match by a set score of 2-0?: 0.35/0.37 mid 36.0%, model 36.9% (projection_v2.0 (prediction ledger)) -- gap +0.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT12PAUVAC-VAC21` Will Valentin Vacherot win the Tommy Paul vs Valentin Vacherot match by a set score of 2-1?: 0.18/0.20 mid 19.0%, model 18.7% (projection_v2.0 (prediction ledger)) -- gap -0.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT12PAUVAC-PAU5` Will Tommy Paul win at least 4.5 more games than Valentin Vacherot?: 0.21/0.22 mid 21.5%, model 21.6% (projection_v2.0 (prediction ledger)) -- gap +0.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE

## Xiyu Wang vs Xinyu Wang -- WTA Wuhan R64

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-12 11:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 10:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-12T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT11WANWAN2:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xiyu Wang (`KXWTAMATCH-26OCT11WANWAN2-WAN`) | 0.51 / 0.52 (20355) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xinyu Wang (`KXWTAMATCH-26OCT11WANWAN2-WAN2`) | 0.48 / 0.49 (92326) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ugo Blanchet vs Daniel de Jonge -- ATP Challenger Roanne Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-12T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200259:207893:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ugo Blanchet (`KXATPCHALLENGERMATCH-26OCT12BLADE-BLA`) | 0.79 / 0.80 (1601) | 79.5% | 92.6% | 70.8% | 86.9% [84.2%-89.3%] | 78.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +13.1 pp | REVIEW | FRESH | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daniel de Jonge (`KXATPCHALLENGERMATCH-26OCT12BLADE-DE`) | 0.20 / 0.21 (8549) | 20.5% | 7.4% | 29.2% | 13.1% [10.7%-15.8%] | 22.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.1 pp | REVIEW | FRESH | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3260.0, B 162.0; serve-point win A 70.0%, B 41.7%; Elo A 1589.9, B 1240.9; model uncertainty 0.0255
* Form inputs: days since last match A 14, B 98; matches on record A 356, B 93; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.022, surface_dev_loose -0.001, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE

## Lucas Poullain vs Tom Paris -- ATP Challenger Roanne Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-12T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:131911:209512:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tom Paris (`KXATPCHALLENGERMATCH-26OCT12POUPAR-PAR`) | 0.26 / 0.28 (5336) | 27.0% | 40.2% | 33.8% | 38.0% [32.0%-45.9%] | 28.9% | 28.9% | -- | INSUFFICIENT_INPUTS | PASS | +13.2 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lucas Poullain (`KXATPCHALLENGERMATCH-26OCT12POUPAR-POU`) | 0.72 / 0.73 (8502) | 72.5% | 59.8% | 66.2% | 62.0% [54.1%-68.0%] | 71.1% | 72.3% | -- | INSUFFICIENT_INPUTS | PASS | -12.7 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1936.0, B 303.0; serve-point win A 63.0%, B 38.9%; Elo A 1561.2, B 1481.8; model uncertainty 0.0695
* Form inputs: days since last match A 14, B 686; matches on record A 307, B 74; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.059, surface_pool_high +0.057, surface_dev_loose -0.001, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Emiliana Arango vs Gabriela Knutson -- WTA 125K Rovereto R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 15:00Z
* Current expected start: 2026-10-12 12:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 11:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-12T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT12ARAKNU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emiliana Arango (`KXWTACHALLENGERMATCH-26OCT12ARAKNU-ARA`) | 0.42 / 0.43 (14373) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gabriela Knutson (`KXWTACHALLENGERMATCH-26OCT12ARAKNU-KNU`) | 0.58 / 0.59 (764) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Clara Burel vs Lina Gjorcheska -- WTA 125K Lisbon R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 15:00Z
* Current expected start: 2026-10-12 12:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 11:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Clay · scheduled 2026-10-12T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:211227:216262:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Clara Burel (`KXWTACHALLENGERMATCH-26OCT12BURGJO-BUR`) | 0.87 / 0.88 (123) | 87.5% | -- | 36.4% | 47.9% [41.5%-62.1%] | -- | -- | -- | -- | PASS | -39.6 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lina Gjorcheska (`KXWTACHALLENGERMATCH-26OCT12BURGJO-GJO`) | 0.12 / 0.13 (914) | 12.5% | -- | 63.6% | 52.1% [37.9%-58.5%] | -- | -- | -- | -- | WATCH | +39.6 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1472.0, B 2459.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.103
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTACHALLENGERMATCH-26OCT12BURGJO-GJO  (YES = Lina Gjorcheska)
Model: 52%
Kalshi: 12%
Gap: +40 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.043, surface_pool_high -0.043, surface_dev_loose -0.011, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Madhwin Kamath vs Aniketh Venkataraman -- M25 Solapur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12KAMVEN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Madhwin Kamath (`KXITFMATCH-26OCT12KAMVEN-KAM`) | 0.41 / 0.82 (3) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aniketh Venkataraman (`KXITFMATCH-26OCT12KAMVEN-VEN`) | 0.04 / 0.29 (35) | 16.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## ARADHYA KSHITIJ vs Suraj R Prabodh -- M25 Solapur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-12T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:122617:tml:K0QY:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ARADHYA KSHITIJ (`KXITFMATCH-26OCT12KSHPRA-KSH`) | 0.70 / 0.93 (58) | 81.5% | -- | 65.7% | 79.0% [78.9%-79.9%] | -- | -- | -- | -- | PASS | -2.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Suraj R Prabodh (`KXITFMATCH-26OCT12KSHPRA-PRA`) | 0.06 / 0.29 (152) | 17.5% | -- | 34.3% | 21.0% [20.1%-21.1%] | -- | -- | -- | -- | PASS | +3.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 57.0, B 164.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0052
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mathys Erhard vs Leo Raquillet -- ATP Challenger Olbia Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 12:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-12T12:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207231:210447:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mathys Erhard (`KXATPCHALLENGERMATCH-26OCT12ERHRAQ-ERH`) | 0.77 / 0.78 (2946) | 77.5% | 87.4% | 85.7% | 86.6% [83.6%-89.1%] | 74.3% | -- | 74.3% | ALL_THREE_DISAGREE | WATCH | +9.9 pp | NORMAL | FRESH | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Leo Raquillet (`KXATPCHALLENGERMATCH-26OCT12ERHRAQ-RAQ`) | 0.22 / 0.24 (462) | 23.0% | 12.6% | 14.3% | 13.5% [10.9%-16.4%] | 25.7% | -- | 25.7% | ALL_THREE_DISAGREE | PASS | -10.4 pp | REVIEW | FRESH | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3008.0, B 397.0; serve-point win A 65.0%, B 43.9%; Elo A 1593.7, B 1268.5; model uncertainty 0.0277
* Form inputs: days since last match A 35, B 28; matches on record A 349, B 54; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.026, surface_pool_high -0.030, surface_dev_loose +0.003, surface_dev_tight -0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER

## Georgii Kravchenko vs Daniel Masur -- ATP Challenger Olbia Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 12:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-12T12:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:109054:206662:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Georgii Kravchenko (`KXATPCHALLENGERMATCH-26OCT12KRAMAS-KRA`) | 0.38 / 0.39 (2493) | 38.5% | 38.8% | 60.5% | 40.0% [34.7%-46.0%] | 39.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.3 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daniel Masur (`KXATPCHALLENGERMATCH-26OCT12KRAMAS-MAS`) | 0.61 / 0.62 (61) | 61.5% | 61.2% | 39.5% | 60.0% [54.0%-65.3%] | 60.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.3 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 665.0, B 2334.0; serve-point win A 61.0%, B 36.7%; Elo A 1474.3, B 1611.2; model uncertainty 0.0564
* Form inputs: days since last match A 22, B 21; matches on record A 308, B 710; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.020, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

## Pavel Lagutin vs Oleksandr Ovcharenko -- ATP Challenger Catania Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 12:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-12T12:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209191:tml:L0N0:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pavel Lagutin (`KXATPCHALLENGERMATCH-26OCT12LAGOVC-LAG`) | 0.67 / 0.68 (101) | 67.5% | 23.4% | 53.6% | 29.0% [26.9%-33.5%] | 63.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -44.1 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oleksandr Ovcharenko (`KXATPCHALLENGERMATCH-26OCT12LAGOVC-OVC`) | 0.31 / 0.32 (970) | 31.5% | 76.6% | 46.4% | 71.0% [66.5%-73.1%] | 36.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +45.1 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 368.0, B 511.0; serve-point win A 57.9%, B 36.4%; Elo A 1368.6, B 1565.9; model uncertainty 0.0329
* Form inputs: days since last match A 21, B 42; matches on record A 5, B 251; data quality D

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT12LAGOVC-OVC  (YES = Oleksandr Ovcharenko)
Model: 77%
Kalshi: 32%
Gap: +45 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

## Laurent Lokoli vs George Loffhagen -- ATP Challenger Olbia Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 12:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-12T12:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106362:207785:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| George Loffhagen (`KXATPCHALLENGERMATCH-26OCT12LOKLOF-LOF`) | 0.65 / 0.67 (2129) | 66.0% | 56.9% | 75.6% | 54.5% [47.0%-63.3%] | -- | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.1 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Laurent Lokoli (`KXATPCHALLENGERMATCH-26OCT12LOKLOF-LOK`) | 0.33 / 0.34 (3448) | 33.5% | 43.1% | 24.4% | 45.5% [36.7%-53.0%] | -- | -- | -- | INSUFFICIENT_INPUTS | WATCH | +9.6 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1677.0, B 1238.0; serve-point win A 62.2%, B 36.4%; Elo A 1601.0, B 1499.8; model uncertainty 0.0817
* Form inputs: days since last match A 14, B 49; matches on record A 620, B 203; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.015, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Alex Marti Pujolras vs Kai Wehnelt -- ATP Challenger Catania Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 12:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-12T12:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132999:207704:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Marti Pujolras (`KXATPCHALLENGERMATCH-26OCT12MARWEH-MAR`) | 0.53 / 0.54 (3585) | 53.5% | 73.6% | 65.2% | 72.9% [70.7%-75.4%] | 54.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +20.1 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kai Wehnelt (`KXATPCHALLENGERMATCH-26OCT12MARWEH-WEH`) | 0.45 / 0.46 (1854) | 45.5% | 26.4% | 34.8% | 27.1% [24.6%-29.3%] | 45.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.1 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1457.0, B 662.0; serve-point win A 61.7%, B 43.1%; Elo A 1539.5, B 1342.6; model uncertainty 0.0232
* Form inputs: days since last match A 686, B 28; matches on record A 339, B 356; data quality F

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT12MARWEH-MAR  (YES = Alex Marti Pujolras)
Model: 74%
Kalshi: 54%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

## Yanaki Milev vs Federico Iannaccone -- ATP Challenger Catania Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 12:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-12T12:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200713:210200:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Federico Iannaccone (`KXATPCHALLENGERMATCH-26OCT12MILIAN-IAN`) | 0.50 / 0.52 (6838) | 51.0% | 57.9% | 51.0% | 52.6% [51.6%-52.6%] | 52.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.9 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yanaki Milev (`KXATPCHALLENGERMATCH-26OCT12MILIAN-MIL`) | 0.48 / 0.49 (2028) | 48.5% | 42.1% | 48.9% | 47.4% [47.4%-48.4%] | 48.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.4 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 968.0, B 725.0; serve-point win A 57.4%, B 41.1%; Elo A 1498.3, B 1517.2; model uncertainty 0.0053
* Form inputs: days since last match A 42, B 21; matches on record A 161, B 290; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

## Andrea Lazaro Garcia vs Yasmine Kabbaj -- WTA 125K Mallorca R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 15:30Z
* Current expected start: 2026-10-12 12:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 11:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Grass · scheduled 2026-10-12T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:210622:236956:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yasmine Kabbaj (`KXWTACHALLENGERMATCH-26OCT12LAZKAB-KAB`) | 0.29 / 0.30 (600) | 29.5% | -- | 27.8% | 26.9% [26.0%-29.1%] | 31.2% | 30.1% | 30.1% | MODEL_LONE_OUTLIER | PASS | -2.6 pp | NORMAL | FRESH | A / LIMITED | EXTERNAL_STALE | VERIFIED |
| Andrea Lazaro Garcia (`KXWTACHALLENGERMATCH-26OCT12LAZKAB-LAZ`) | 0.70 / 0.71 (417) | 70.5% | -- | 72.2% | 73.1% [70.9%-74.0%] | 68.8% | 70.5% | 70.5% | MODEL_LONE_OUTLIER | WATCH | +2.6 pp | NORMAL | FRESH | A / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3043.0, B 2651.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0157
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.004, surface_dev_loose -0.013, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Alexia-Shara Iancu vs Andreya Glushkova -- W50 Stara Zagora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260262:267887:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andreya Glushkova (`KXITFWMATCH-26OCT12IANGLU-GLU`) | 0.11 / 0.12 (6110) | 11.5% | -- | 67.5% | 35.4% [35.4%-35.4%] | -- | -- | -- | -- | PASS | +23.9 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexia-Shara Iancu (`KXITFWMATCH-26OCT12IANGLU-IAN`) | 0.88 / 0.92 (5656) | 90.0% | -- | 32.5% | 64.6% [64.6%-64.6%] | -- | -- | -- | -- | PASS | -25.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 74.0, B 0.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0001
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT12IANGLU-GLU  (YES = Andreya Glushkova)
Model: 35%
Kalshi: 12%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexa Karatancheva vs Raya Markova -- W50 Stara Zagora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12KARMAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexa Karatancheva (`KXITFWMATCH-26OCT12KARMAR-KAR`) | 0.71 / 0.78 (118) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Raya Markova (`KXITFWMATCH-26OCT12KARMAR-MAR`) | 0.21 / 0.26 (28) | 23.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rafaela Simeonova vs Elena Papadopoulou -- W50 Stara Zagora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12SIMPAP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Papadopoulou (`KXITFWMATCH-26OCT12SIMPAP-PAP`) | 0.55 / 0.60 (66) | 57.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rafaela Simeonova (`KXITFWMATCH-26OCT12SIMPAP-SIM`) | 0.41 / 0.43 (43) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sonja Zhenikhova vs Daria Maria Marioara -- W50 Stara Zagora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12ZHEMAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria Maria Marioara (`KXITFWMATCH-26OCT12ZHEMAR-MAR`) | 0.10 / 0.11 (6159) | 10.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sonja Zhenikhova (`KXITFWMATCH-26OCT12ZHEMAR-ZHE`) | 0.90 / 0.93 (6) | 91.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Henry Bernet vs Thijs Boogaard -- ATP Challenger Roanne Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 12:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-12T12:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:148679:212275:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Henry Bernet (`KXATPCHALLENGERMATCH-26OCT12BERBOO-BER`) | 0.82 / 0.83 (9947) | 82.5% | 77.2% | 56.9% | 65.9% [64.5%-67.7%] | 80.3% | -- | 80.3% | KALSHI_LONE_OUTLIER | PASS | -5.3 pp | NORMAL | FRESH | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Thijs Boogaard (`KXATPCHALLENGERMATCH-26OCT12BERBOO-BOO`) | 0.17 / 0.18 (544) | 17.5% | 22.8% | 43.1% | 34.1% [32.3%-35.5%] | 19.7% | -- | 19.7% | KALSHI_LONE_OUTLIER | PASS | +5.3 pp | NORMAL | FRESH | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1310.0, B 514.0; serve-point win A 67.7%, B 38.3%; Elo A 1531.0, B 1390.9; model uncertainty 0.0159
* Form inputs: days since last match A 14, B 91; matches on record A 33, B 10; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.009, surface_dev_loose +0.008, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Loann Massard vs Jakub Paul -- ATP Challenger Roanne Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 12:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-12T12:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207605:210604:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Loann Massard (`KXATPCHALLENGERMATCH-26OCT12MASPAU-MAS`) | 0.39 / 0.40 (607) | 39.5% | 33.0% | 42.4% | 31.9% [27.4%-36.1%] | 40.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jakub Paul (`KXATPCHALLENGERMATCH-26OCT12MASPAU-PAU`) | 0.60 / 0.61 (7311) | 60.5% | 67.0% | 57.6% | 68.1% [63.9%-72.6%] | 59.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 441.0, B 1703.0; serve-point win A 60.2%, B 36.3%; Elo A 1386.9, B 1542.0; model uncertainty 0.0433
* Form inputs: days since last match A 238, B 197; matches on record A 81, B 358; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.022, surface_pool_high +0.028, surface_dev_loose -0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE

## Alexandra Eala vs Han Shi -- WTA Wuhan R64

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-12 13:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 12:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-12T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:222559:223253:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandra Eala (`KXWTAMATCH-26OCT11EALSHI-EAL`) | 0.79 / 0.80 (101381) | 79.5% | 86.7% | 59.0% | 70.3% [65.1%-83.1%] | 77.5% | 79.1% | 79.1% | MODEL_LONE_OUTLIER | PASS | +7.2 pp | NORMAL | FRESH | B / LIMITED | EXTERNAL_STALE | VERIFIED |
| Han Shi (`KXWTAMATCH-26OCT11EALSHI-SHI`) | 0.19 / 0.21 (18783) | 20.0% | 13.3% | 41.0% | 29.7% [16.9%-34.9%] | 22.5% | 20.7% | 20.7% | MODEL_LONE_OUTLIER | WATCH | -6.7 pp | NORMAL | FRESH | B / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4541.0, B 3226.0; serve-point win A 58.3%, B 50.0%; Elo A 1956.2, B 1600.6; model uncertainty 0.0902
* Form inputs: days since last match A 17, B 167; matches on record A 365, B 228; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.023, surface_pool_high -0.019, surface_dev_loose -0.005, surface_dev_tight +0.014
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT11EALSHI-15` Over 14.5 games: 0.64/0.95 mid 79.5%, model 96.3% (projection_v2.0 (prediction ledger)) -- gap +16.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT11EALSHI-20` Over 19.5 games: 0.50/0.52 mid 51.0%, model 57.0% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT11EALSHI-25` Over 24.5 games: 0.22/0.33 mid 27.5%, model 33.2% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT11EALSHI-1-SHI` Will Han Shi win set 1 in the Alexandra Eala vs Han Shi match: 0.26/0.27 mid 26.5%, model 22.9% (projection_v2.0 (prediction ledger)) -- gap -3.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT11EALSHI-1-EAL` Will Alexandra Eala win set 1 in the Alexandra Eala vs Han Shi match: 0.74/0.75 mid 74.5%, model 77.1% (projection_v2.0 (prediction ledger)) -- gap +2.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT11EALSHI-2-EAL` Will Alexandra Eala win set 2 in the Alexandra Eala vs Han Shi match: 0.73/0.76 mid 74.5%, model 77.1% (projection_v2.0 (prediction ledger)) -- gap +2.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT11EALSHI-2-SHI` Will Han Shi win set 2 in the Alexandra Eala vs Han Shi match: 0.22/0.26 mid 24.0%, model 22.9% (projection_v2.0 (prediction ledger)) -- gap -1.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Duje Ajdukovic vs Andrej Martin -- ATP Challenger Maia Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-12T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105413:207213:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Duje Ajdukovic (`KXATPCHALLENGERMATCH-26OCT12AJDMAR-AJD`) | 0.65 / 0.66 (406) | 65.5% | 65.0% | 62.4% | 58.5% [57.0%-59.5%] | 65.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.5 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Andrej Martin (`KXATPCHALLENGERMATCH-26OCT12AJDMAR-MAR`) | 0.33 / 0.35 (12057) | 34.0% | 34.9% | 37.6% | 41.5% [40.5%-43.0%] | 34.8% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +0.9 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3949.0, B 1394.0; serve-point win A 64.1%, B 39.0%; Elo A 1629.7, B 1596.4; model uncertainty 0.0123
* Form inputs: days since last match A 35, B 14; matches on record A 451, B 983; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.015, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Florian Broska vs Sergi Perez Contri -- ATP Challenger Maia Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-12T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133997:202239:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Florian Broska (`KXATPCHALLENGERMATCH-26OCT12BROPER-BRO`) | 0.65 / 0.67 (756) | 66.0% | 56.5% | 64.3% | 54.0% [51.0%-57.0%] | 65.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.5 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sergi Perez Contri (`KXATPCHALLENGERMATCH-26OCT12BROPER-PER`) | 0.33 / 0.35 (7848) | 34.0% | 43.5% | 35.7% | 46.0% [43.0%-49.0%] | 34.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +9.5 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1189.0, B 459.0; serve-point win A 63.2%, B 38.1%; Elo A 1464.8, B 1455.8; model uncertainty 0.0301
* Form inputs: days since last match A 56, B 189; matches on record A 140, B 280; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.030, surface_pool_high -0.030, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE

## Benjamin Hassan vs Ryan Nijboer -- ATP Challenger Maia Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-12T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133975:207764:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benjamin Hassan (`KXATPCHALLENGERMATCH-26OCT12HASNIJ-HAS`) | 0.48 / 0.49 (852) | 48.5% | 62.5% | 57.6% | 65.8% [61.5%-72.1%] | 50.0% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +14.0 pp | REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ryan Nijboer (`KXATPCHALLENGERMATCH-26OCT12HASNIJ-NIJ`) | 0.50 / 0.52 (2444) | 51.0% | 37.5% | 42.4% | 34.2% [27.9%-38.5%] | 50.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.5 pp | REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3395.0, B 1089.0; serve-point win A 63.2%, B 39.3%; Elo A 1630.9, B 1468.5; model uncertainty 0.0526
* Form inputs: days since last match A 14, B 21; matches on record A 508, B 378; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.032, surface_pool_high -0.024, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Aurora Corvi vs Thea Marcu -- W15 Chisinau R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12CORMAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aurora Corvi (`KXITFWMATCH-26OCT12CORMAR-COR`) | 0.77 / 0.79 (52) | 78.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Thea Marcu (`KXITFWMATCH-26OCT12CORMAR-MAR`) | 0.22 / 0.23 (5114) | 22.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Simona Cucu vs Sophie Williams -- W15 Chisinau R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-12T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221633:267776:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Simona Cucu (`KXITFWMATCH-26OCT12CUCWIL-CUC`) | 0.71 / 0.75 (87) | 73.0% | -- | 61.6% | 43.6% [42.6%-44.7%] | -- | -- | -- | -- | PASS | -29.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sophie Williams (`KXITFWMATCH-26OCT12CUCWIL-WIL`) | 0.23 / 0.26 (27) | 24.5% | -- | 38.4% | 56.4% [55.3%-57.4%] | -- | -- | -- | -- | PASS | +31.9 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 52.0, B 117.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0105
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT12CUCWIL-WIL  (YES = Sophie Williams)
Model: 56%
Kalshi: 24%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anna Lena Ebster vs Yeva Galiievska -- W15 Chisinau R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-12T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:244079:262885:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Lena Ebster (`KXITFWMATCH-26OCT12EBSGAL-EBS`) | 0.52 / 0.55 (88) | 53.5% | -- | 21.1% | 36.4% [32.0%-42.1%] | -- | -- | -- | -- | PASS | -17.1 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yeva Galiievska (`KXITFWMATCH-26OCT12EBSGAL-GAL`) | 0.44 / 0.47 (44) | 45.5% | -- | 78.8% | 63.6% [57.9%-68.0%] | -- | -- | -- | -- | PASS | +18.1 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 978.0, B 455.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0503
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT12EBSGAL-GAL  (YES = Yeva Galiievska)
Model: 64%
Kalshi: 46%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.000, surface_dev_loose -0.015, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eva Iurina vs Alina Nesmianovych -- W15 Chisinau R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12IURNES:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eva Iurina (`KXITFWMATCH-26OCT12IURNES-IUR`) | 0.07 / 0.10 (14) | 8.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alina Nesmianovych (`KXITFWMATCH-26OCT12IURNES-NES`) | 0.91 / 0.92 (6150) | 91.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Susan Bandecchi vs Gaia Maduzzi -- WTA 125K Rovereto R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 16:30Z
* Current expected start: 2026-10-12 13:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 12:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-12T16:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT12BANMAD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Susan Bandecchi (`KXWTACHALLENGERMATCH-26OCT12BANMAD-BAN`) | 0.87 / 0.89 (13430) | 88.0% | -- | -- | -- [-----] | 85.5% | 87.0% | 87.0% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gaia Maduzzi (`KXWTACHALLENGERMATCH-26OCT12BANMAD-MAD`) | 0.12 / 0.13 (1923) | 12.5% | -- | -- | -- [-----] | 14.5% | 11.9% | 11.9% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Polina Iatcenko vs Harmony Tan -- WTA 125K Rovereto R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 16:10Z
* Current expected start: 2026-10-12 13:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 12:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Hard · scheduled 2026-10-12T16:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:211552:223325:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Iatcenko (`KXWTACHALLENGERMATCH-26OCT12IATTAN-IAT`) | 0.62 / 0.63 (1558) | 62.5% | -- | 40.1% | 45.8% [43.7%-49.5%] | 60.9% | 63.7% | 60.9% | MODEL_LONE_OUTLIER | PASS | -16.7 pp | HIGH_REVIEW | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Harmony Tan (`KXWTACHALLENGERMATCH-26OCT12IATTAN-TAN`) | 0.37 / 0.38 (230) | 37.5% | -- | 59.9% | 54.2% [50.5%-56.3%] | 39.1% | 36.7% | 37.9% | MODEL_LONE_OUTLIER | PASS | +16.7 pp | HIGH_REVIEW | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2951.0, B 3731.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0288
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTACHALLENGERMATCH-26OCT12IATTAN-TAN  (YES = Harmony Tan)
Model: 54%
Kalshi: 38%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: A (LIMITED)
Reasons: SURFACE_DATA_THIN, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.026, surface_dev_loose -0.016, surface_dev_tight +0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Barbora Palicova vs Jazmin Ortenzi -- WTA 125K Lisbon R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 16:10Z
* Current expected start: 2026-10-12 13:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 12:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Clay · scheduled 2026-10-12T16:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220446:223323:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jazmin Ortenzi (`KXWTACHALLENGERMATCH-26OCT12PALORT-ORT`) | 0.38 / 0.39 (1260) | 38.5% | -- | 81.1% | 74.4% [61.1%-79.2%] | -- | -- | -- | -- | PASS | +35.9 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Barbora Palicova (`KXWTACHALLENGERMATCH-26OCT12PALORT-PAL`) | 0.61 / 0.62 (563) | 61.5% | -- | 18.9% | 25.6% [20.8%-39.0%] | -- | -- | -- | -- | PASS | -35.9 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2850.0, B 3121.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0909
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTACHALLENGERMATCH-26OCT12PALORT-ORT  (YES = Jazmin Ortenzi)
Model: 74%
Kalshi: 38%
Gap: +36 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.017, surface_dev_loose -0.009, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Luis Carlos Alvarez Valdes vs Alexander Chang -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211468:212959:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luis Carlos Alvarez Valdes (`KXITFMATCH-26OCT12ALVCHA-ALV`) | 0.59 / 0.61 (73) | 60.0% | 70.3% | 50.0% | 61.0% [61.0%-61.0%] | -- | -- | -- | -- | PASS | +10.3 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Alexander Chang (`KXITFMATCH-26OCT12ALVCHA-CHA`) | 0.36 / 0.41 (86) | 38.5% | 29.7% | 50.0% | 39.0% [39.0%-39.0%] | -- | -- | -- | -- | PASS | -8.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 64.1%, B 40.1%; Elo A 1307.7, B 1231.4; model uncertainty 0.0
* Form inputs: days since last match A 721, B 826; matches on record A 27, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tobia Costanzo Baragiola Mordini vs Edouard Villoslada -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209973:213701:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tobia Costanzo Baragiola Mordini (`KXITFMATCH-26OCT12BARVIL-BAR`) | 0.77 / 0.78 (78) | 77.5% | 68.6% | 50.0% | 72.9% [70.3%-74.6%] | -- | -- | -- | -- | PASS | -8.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Edouard Villoslada (`KXITFMATCH-26OCT12BARVIL-VIL`) | 0.23 / 0.24 (77) | 23.5% | 31.4% | 50.0% | 27.1% [25.4%-29.7%] | -- | -- | -- | -- | PASS | +7.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 63.9%, B 39.9%; Elo A 1271.9, B 1100.4; model uncertainty 0.0212
* Form inputs: days since last match A 672, B 756; matches on record A 1, B 44; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.026, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lorenzo Berto vs Arthur Bellegy -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213004:213120:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arthur Bellegy (`KXITFMATCH-26OCT12BERBEL-BEL`) | 0.25 / 0.27 (4) | 26.0% | 22.6% | 70.1% | 31.6% [30.8%-32.5%] | -- | -- | -- | -- | PASS | -3.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lorenzo Berto (`KXITFMATCH-26OCT12BERBEL-BER`) | 0.69 / 0.75 (92) | 72.0% | 77.5% | 29.9% | 68.4% [67.5%-69.2%] | -- | -- | -- | -- | PASS | +5.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 73.0, B 0.0; serve-point win A 66.1%, B 39.9%; Elo A 1334.0, B 1199.8; model uncertainty 0.0085
* Form inputs: days since last match A 21, B 700; matches on record A 2, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.009, surface_dev_loose +0.008, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marco Furlanetto vs Alessandro Bellifemine -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209117:210110:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alessandro Bellifemine (`KXITFMATCH-26OCT12FURBEL-BEL`) | 0.45 / 0.52 (5116) | 48.5% | 64.9% | 51.0% | 61.8% [61.8%-63.7%] | -- | -- | -- | -- | PASS | +16.4 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Marco Furlanetto (`KXITFMATCH-26OCT12FURBEL-FUR`) | 0.47 / 0.52 (42) | 49.5% | 35.1% | 49.0% | 38.2% [36.3%-38.2%] | -- | -- | -- | -- | PASS | -14.4 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 227.0; serve-point win A 62.5%, B 34.4%; Elo A 1128.3, B 1217.8; model uncertainty 0.0094
* Form inputs: days since last match A 784, B 700; matches on record A 27, B 47; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT12FURBEL-BEL  (YES = Alessandro Bellifemine)
Model: 65%
Kalshi: 48%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.019, surface_dev_loose -0.009, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dimitar Kisimov vs Simone Massucco -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12KISMAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dimitar Kisimov (`KXITFMATCH-26OCT12KISMAS-KIS`) | 0.78 / 0.86 (86) | 82.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Simone Massucco (`KXITFMATCH-26OCT12KISMAS-MAS`) | 0.14 / 0.16 (7) | 15.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matteo Sciahbasi vs Nicolas Ifi -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212552:tml:S1AZ:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Ifi (`KXITFMATCH-26OCT12SCIIFI-IFI`) | 0.36 / 0.41 (1) | 38.5% | -- | 61.1% | 40.9% [40.9%-41.9%] | -- | -- | -- | -- | PASS | +2.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matteo Sciahbasi (`KXITFMATCH-26OCT12SCIIFI-SCI`) | 0.57 / 0.63 (5108) | 60.0% | -- | 38.9% | 59.1% [58.1%-59.1%] | -- | -- | -- | -- | PASS | -0.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 78.0, B 0.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.005
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adam Walton vs Marin Cilic -- ATP Challenger Jinan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 13:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105227:200443:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marin Cilic (`KXATPCHALLENGERMATCH-26OCT12WALCIL-CIL`) | 0.46 / 0.48 (7638) | 47.0% | 53.8% | 52.4% | 56.8% [51.9%-67.5%] | 46.9% | 46.8% | 46.8% | MODEL_LONE_OUTLIER | WATCH | +6.8 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Adam Walton (`KXATPCHALLENGERMATCH-26OCT12WALCIL-WAL`) | 0.52 / 0.53 (2051) | 52.5% | 46.2% | 47.6% | 43.2% [32.5%-48.0%] | 53.1% | 53.5% | 53.5% | MODEL_LONE_OUTLIER | PASS | -6.3 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5302.0, B 3216.0; serve-point win A 65.8%, B 33.4%; Elo A 1740.0, B 1870.5; model uncertainty 0.0778
* Form inputs: days since last match A 7, B 5; matches on record A 347, B 1098; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.057, surface_pool_high +0.048, surface_dev_loose -0.004, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Valeria Garnevska vs Daniella Dimitrova -- W50 Stara Zagora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220692:270109:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniella Dimitrova (`KXITFWMATCH-26OCT12GARDIM-DIM`) | 0.17 / 0.18 (61) | 17.5% | -- | 72.2% | 55.3% [55.3%-55.3%] | -- | -- | -- | -- | PASS | +37.8 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Valeria Garnevska (`KXITFWMATCH-26OCT12GARDIM-GAR`) | 0.83 / 0.85 (99) | 84.0% | -- | 27.8% | 44.7% [44.7%-44.7%] | -- | -- | -- | -- | PASS | -39.3 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 149.0, B 0.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0001
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT12GARDIM-DIM  (YES = Daniella Dimitrova)
Model: 55%
Kalshi: 18%
Gap: +38 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gala Ivanovic vs Yoana Moneva -- W50 Stara Zagora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:246492:270115:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gala Ivanovic (`KXITFWMATCH-26OCT12IVAMON-IVA`) | 0.92 / 0.94 (284) | 93.0% | -- | 81.5% | 92.5% [91.7%-93.2%] | -- | -- | -- | -- | PASS | -0.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yoana Moneva (`KXITFWMATCH-26OCT12IVAMON-MON`) | 0.08 / 0.10 (28) | 9.0% | -- | 18.5% | 7.5% [6.8%-8.3%] | -- | -- | -- | -- | PASS | -1.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 844.0, B 180.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0075
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Madhurima Sawant vs Teodora Naidenova -- W50 Stara Zagora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12SAWNAI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Teodora Naidenova (`KXITFWMATCH-26OCT12SAWNAI-NAI`) | 0.08 / 0.11 (0) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Madhurima Sawant (`KXITFWMATCH-26OCT12SAWNAI-SAW`) | 0.89 / 0.92 (123) | 90.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Darya Velikova vs Ilina Ilieva -- W50 Stara Zagora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12VELILI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ilina Ilieva (`KXITFWMATCH-26OCT12VELILI-ILI`) | 0.23 / 0.29 (23) | 26.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Darya Velikova (`KXITFWMATCH-26OCT12VELILI-VEL`) | 0.68 / 0.75 (6145) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Norbert Gombos vs Robin Catry -- ATP Challenger Roanne Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 13:50Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-12T13:50:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105613:210714:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robin Catry (`KXATPCHALLENGERMATCH-26OCT12GOMCAT-CAT`) | 0.20 / 0.21 (2266) | 20.5% | 22.7% | 31.6% | 18.6% [15.0%-22.0%] | 21.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.2 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Norbert Gombos (`KXATPCHALLENGERMATCH-26OCT12GOMCAT-GOM`) | 0.79 / 0.80 (6739) | 79.5% | 77.3% | 68.4% | 81.4% [78.0%-85.0%] | 78.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.2 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3555.0, B 431.0; serve-point win A 65.8%, B 40.2%; Elo A 1609.5, B 1320.6; model uncertainty 0.0351
* Form inputs: days since last match A 22, B 98; matches on record A 992, B 54; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.028, surface_dev_loose +0.003, surface_dev_tight -0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE

## James Beaven vs Xavi Matas Ortega -- M15 Offenbach R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208519:212536:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| James Beaven (`KXITFMATCH-26OCT12BEAMAT-BEA`) | 0.56 / 0.57 (18) | 56.5% | 43.6% | 50.0% | 47.0% [47.0%-47.0%] | -- | -- | -- | -- | PASS | -12.9 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xavi Matas Ortega (`KXITFMATCH-26OCT12BEAMAT-MAT`) | 0.37 / 0.40 (87) | 38.5% | 56.4% | 50.0% | 53.0% [53.0%-53.0%] | -- | -- | -- | -- | PASS | +17.9 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 61.4%, B 37.4%; Elo A 1161.8, B 1183.8; model uncertainty 0.0
* Form inputs: days since last match A 672, B 672; matches on record A 7, B 52; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT12BEAMAT-MAT  (YES = Xavi Matas Ortega)
Model: 56%
Kalshi: 38%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sven Corbinais vs Claus Piening -- M15 Offenbach R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12CORPIE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sven Corbinais (`KXITFMATCH-26OCT12CORPIE-COR`) | 0.69 / 0.72 (37) | 70.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Claus Piening (`KXITFMATCH-26OCT12CORPIE-PIE`) | 0.26 / 0.31 (14) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sean Cuenin vs Izan Almazan Valiente -- ATP Challenger Catania R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-12T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209952:212978:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Izan Almazan Valiente (`KXATPCHALLENGERMATCH-26OCT12CUEALM-ALM`) | 0.35 / 0.37 (5743) | 36.0% | 37.0% | 40.8% | 39.3% [38.8%-40.4%] | -- | 36.6% | 36.6% | MODEL_LONE_OUTLIER | PASS | +1.0 pp | NORMAL | FRESH | C / LIMITED | ALL_AGREE | VERIFIED |
| Sean Cuenin (`KXATPCHALLENGERMATCH-26OCT12CUEALM-CUE`) | 0.63 / 0.64 (6557) | 63.5% | 63.0% | 59.2% | 60.7% [59.6%-61.2%] | -- | 63.9% | 63.9% | MODEL_LONE_OUTLIER | PASS | -0.5 pp | NORMAL | FRESH | C / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 624.0, B 663.0; serve-point win A 61.7%, B 40.9%; Elo A 1419.3, B 1343.2; model uncertainty 0.0078
* Form inputs: days since last match A 21, B 21; matches on record A 117, B 18; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Buvaysar Gadamauri vs Sandro Kopp -- ATP Challenger Catania R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-12T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207491:207527:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Buvaysar Gadamauri (`KXATPCHALLENGERMATCH-26OCT12GADKOP-GAD`) | 0.47 / 0.48 (8336) | 47.5% | 62.7% | 57.6% | 57.6% [56.6%-58.1%] | -- | 46.3% | 46.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +15.2 pp | HIGH_REVIEW | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Sandro Kopp (`KXATPCHALLENGERMATCH-26OCT12GADKOP-KOP`) | 0.52 / 0.53 (931) | 52.5% | 37.3% | 42.4% | 42.4% [41.9%-43.4%] | -- | 54.0% | 54.0% | MODEL_LONE_OUTLIER | PASS | -15.2 pp | HIGH_REVIEW | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2280.0, B 2544.0; serve-point win A 63.0%, B 39.5%; Elo A 1588.6, B 1541.8; model uncertainty 0.0076
* Form inputs: days since last match A 84, B 21; matches on record A 232, B 330; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT12GADKOP-GAD  (YES = Buvaysar Gadamauri)
Model: 63%
Kalshi: 48%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: A (LIMITED)
Reasons: STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Alex Kobelt vs Jiang Yi Qing -- M15 Szabolcsveresmart R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12KOBYIQ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Kobelt (`KXITFMATCH-26OCT12KOBYIQ-KOB`) | 0.67 / 0.95 (10077) | 81.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jiang Yi Qing (`KXITFMATCH-26OCT12KOBYIQ-YIQ`) | 0.07 / 0.12 (114) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aryan Lakshmanan vs Vilmos Krisztian Kovacs -- M15 Szabolcsveresmart R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12LAKKOV:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vilmos Krisztian Kovacs (`KXITFMATCH-26OCT12LAKKOV-KOV`) | 0.18 / 0.29 (5100) | 23.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aryan Lakshmanan (`KXITFMATCH-26OCT12LAKKOV-LAK`) | 0.56 / 0.81 (87) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gabriele Piraino vs Felix Gill -- ATP Challenger Catania R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-12T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208269:210042:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felix Gill (`KXATPCHALLENGERMATCH-26OCT12PIRGIL-GIL`) | 0.61 / 0.62 (7366) | 61.5% | 75.6% | 70.3% | 76.6% [75.0%-81.8%] | -- | 61.4% | 61.4% | MODEL_LONE_OUTLIER | PASS | +14.2 pp | REVIEW | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Gabriele Piraino (`KXATPCHALLENGERMATCH-26OCT12PIRGIL-PIR`) | 0.37 / 0.38 (2277) | 37.5% | 24.3% | 29.6% | 23.4% [18.2%-25.0%] | -- | 38.7% | 38.7% | MODEL_LONE_OUTLIER | PASS | -13.2 pp | REVIEW | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1418.0, B 2694.0; serve-point win A 59.2%, B 35.4%; Elo A 1383.9, B 1649.8; model uncertainty 0.0339
* Form inputs: days since last match A 700, B 21; matches on record A 175, B 281; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Pierre Antoine Tailleu vs Tim Hammes -- M15 Offenbach R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12TAIHAM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tim Hammes (`KXITFMATCH-26OCT12TAIHAM-HAM`) | 0.28 / 0.31 (64) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pierre Antoine Tailleu (`KXITFMATCH-26OCT12TAIHAM-TAI`) | 0.66 / 0.67 (75) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dean Thurner vs Filip Martinovic -- M15 Szabolcsveresmart R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12THUMAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filip Martinovic (`KXITFMATCH-26OCT12THUMAR-MAR`) | 0.44 / 0.47 (3) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dean Thurner (`KXITFMATCH-26OCT12THUMAR-THU`) | 0.51 / 0.58 (6877) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mac Visser vs Andre Megrabian -- M15 Offenbach R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12VISMEG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andre Megrabian (`KXITFMATCH-26OCT12VISMEG-MEG`) | 0.14 / 0.19 (20) | 16.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mac Visser (`KXITFMATCH-26OCT12VISMEG-VIS`) | 0.80 / 0.83 (7937) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Milan Zavaczki vs Nikolaos Papavasiliu -- M15 Szabolcsveresmart R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12ZAVPAP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikolaos Papavasiliu (`KXITFMATCH-26OCT12ZAVPAP-PAP`) | 0.48 / 0.54 (11) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Milan Zavaczki (`KXITFMATCH-26OCT12ZAVPAP-ZAV`) | 0.43 / 0.54 (6716) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alessia Marinescu vs Justine Bretnacher -- W15 Chisinau R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-12T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:265611:267401:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Justine Bretnacher (`KXITFWMATCH-26OCT12MARBRE-BRE`) | 0.44 / 0.51 (37) | 47.5% | -- | 44.7% | 57.5% [55.9%-58.5%] | -- | -- | -- | -- | PASS | +9.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alessia Marinescu (`KXITFWMATCH-26OCT12MARBRE-MAR`) | 0.48 / 0.52 (5107) | 50.0% | -- | 55.3% | 42.5% [41.5%-44.1%] | -- | -- | -- | -- | PASS | -7.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 174.0, B 222.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0131
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.011, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Milana Maslenkova vs Ingrid Ioana Sanduleasa -- W15 Chisinau R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12MASSAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Milana Maslenkova (`KXITFWMATCH-26OCT12MASSAN-MAS`) | 0.18 / 0.24 (176) | 21.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ingrid Ioana Sanduleasa (`KXITFWMATCH-26OCT12MASSAN-SAN`) | 0.74 / 0.79 (6135) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Krystyna Pochtovyk vs Ines Faltinger -- W15 Chisinau R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-12T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:237476:239449:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ines Faltinger (`KXITFWMATCH-26OCT12POCFAL-FAL`) | 0.18 / 0.21 (58) | 19.5% | -- | 56.9% | 41.5% [40.5%-42.5%] | -- | -- | -- | -- | PASS | +22.0 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Krystyna Pochtovyk (`KXITFWMATCH-26OCT12POCFAL-POC`) | 0.75 / 0.81 (105) | 78.0% | -- | 43.1% | 58.5% [57.5%-59.5%] | -- | -- | -- | -- | PASS | -19.5 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 999.0, B 111.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0104
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT12POCFAL-FAL  (YES = Ines Faltinger)
Model: 41%
Kalshi: 20%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luisa Schruff vs Ekaterina Agureeva -- W15 Chisinau R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-12T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:266852:269769:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Agureeva (`KXITFWMATCH-26OCT12SCHAGU-AGU`) | 0.69 / 0.75 (6122) | 72.0% | -- | 61.6% | 72.2% [71.3%-73.1%] | -- | -- | -- | -- | PASS | +0.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luisa Schruff (`KXITFWMATCH-26OCT12SCHAGU-SCH`) | 0.25 / 0.29 (28) | 27.0% | -- | 38.4% | 27.8% [26.9%-28.7%] | -- | -- | -- | -- | PASS | +0.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 449.0, B 144.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0088
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Milos Karol vs Oleksii Krutykh -- ATP Challenger Maia Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 14:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-12T14:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208071:209984:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Milos Karol (`KXATPCHALLENGERMATCH-26OCT12KARKRU-KAR`) | 0.35 / 0.36 (256) | 35.5% | 52.2% | 53.5% | 47.0% [41.9%-49.0%] | 36.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +16.7 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oleksii Krutykh (`KXATPCHALLENGERMATCH-26OCT12KARKRU-KRU`) | 0.63 / 0.65 (1969) | 64.0% | 47.8% | 46.5% | 53.0% [51.0%-58.1%] | 63.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -16.2 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1164.0, B 1235.0; serve-point win A 64.6%, B 35.9%; Elo A 1450.8, B 1507.2; model uncertainty 0.0355
* Form inputs: days since last match A 693, B 23; matches on record A 165, B 402; data quality F

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT12KARKRU-KAR  (YES = Milos Karol)
Model: 52%
Kalshi: 36%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.015, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Alejo Sanchez Quilez vs Ivan Gakhov -- ATP Challenger Maia Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 14:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-12T14:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:123809:211639:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ivan Gakhov (`KXATPCHALLENGERMATCH-26OCT12SANGAK-GAK`) | 0.42 / 0.43 (449) | 42.5% | 62.0% | 54.7% | 63.3% [60.3%-65.7%] | -- | -- | -- | -- | WATCH | +19.5 pp | HIGH_REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alejo Sanchez Quilez (`KXATPCHALLENGERMATCH-26OCT12SANGAK-SAN`) | 0.58 / 0.59 (2437) | 58.5% | 38.0% | 45.3% | 36.7% [34.3%-39.7%] | -- | -- | -- | -- | PASS | -20.5 pp | HIGH_REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1177.0, B 2642.0; serve-point win A 57.6%, B 40.1%; Elo A 1441.5, B 1584.1; model uncertainty 0.0271
* Form inputs: days since last match A 14, B 28; matches on record A 112, B 794; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT12SANGAK-GAK  (YES = Ivan Gakhov)
Model: 62%
Kalshi: 42%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.030, surface_pool_high -0.019, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Patrick Schoen vs Michael Vrbensky -- ATP Challenger Maia Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 14:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-12T14:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202398:211566:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Patrick Schoen (`KXATPCHALLENGERMATCH-26OCT12SCHVRB-SCH`) | 0.81 / 0.83 (1891) | 82.0% | 25.8% | 37.5% | 22.3% [22.3%-23.1%] | 78.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -56.2 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Michael Vrbensky (`KXATPCHALLENGERMATCH-26OCT12SCHVRB-VRB`) | 0.17 / 0.18 (94) | 17.5% | 74.2% | 62.5% | 77.7% [76.9%-77.7%] | 21.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +56.7 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 65.0, B 1127.0; serve-point win A 59.4%, B 35.5%; Elo A 1384.4, B 1604.8; model uncertainty 0.0038
* Form inputs: days since last match A 42, B 77; matches on record A 38, B 450; data quality D

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT12SCHVRB-VRB  (YES = Michael Vrbensky)
Model: 74%
Kalshi: 18%
Gap: +57 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE

## Raluca Georgiana Serban vs Sara Cakarevic -- WTA 125K Lisbon Q3

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-12 14:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

WTA125 (WTA_125) · surface ? · scheduled 2026-10-12T14:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT12SERCAK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Cakarevic (`KXWTACHALLENGERMATCH-26OCT12SERCAK-CAK`) | 0.42 / 0.45 (2149) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Raluca Georgiana Serban (`KXWTACHALLENGERMATCH-26OCT12SERCAK-SER`) | 0.56 / 0.57 (91) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Patrick Brady vs Etienne Donnet -- ATP Challenger Roanne Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-12T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208044:211394:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Patrick Brady (`KXATPCHALLENGERMATCH-26OCT12BRADON-BRA`) | 0.69 / 0.72 (1596) | 70.5% | 50.6% | 57.9% | 53.0% [51.0%-53.9%] | 69.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.9 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Etienne Donnet (`KXATPCHALLENGERMATCH-26OCT12BRADON-DON`) | 0.28 / 0.29 (2905) | 28.5% | 49.4% | 42.1% | 47.0% [46.1%-49.0%] | 30.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +20.9 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 822.0, B 237.0; serve-point win A 64.4%, B 35.8%; Elo A 1420.1, B 1407.9; model uncertainty 0.0146
* Form inputs: days since last match A 49, B 392; matches on record A 94, B 55; data quality D

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT12BRADON-DON  (YES = Etienne Donnet)
Model: 49%
Kalshi: 28%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE

## Linda Klimovicova vs Lucie Havlickova -- WTA 125K Rovereto R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 17:20Z
* Current expected start: 2026-10-12 15:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 14:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-12T17:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT12KLIHAV:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucie Havlickova (`KXWTACHALLENGERMATCH-26OCT12KLIHAV-HAV`) | 0.51 / 0.52 (1713) | 51.5% | -- | -- | -- [-----] | 51.0% | 52.2% | 52.2% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Linda Klimovicova (`KXWTACHALLENGERMATCH-26OCT12KLIHAV-KLI`) | 0.48 / 0.49 (360) | 48.5% | -- | -- | -- [-----] | 49.0% | 48.1% | 48.1% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Leyre Romero Gormaz vs Alice Rame -- WTA 125K Lisbon R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 17:20Z
* Current expected start: 2026-10-12 15:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 14:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-12T17:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT12ROMRAM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alice Rame (`KXWTACHALLENGERMATCH-26OCT12ROMRAM-RAM`) | 0.28 / 0.29 (7194) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leyre Romero Gormaz (`KXWTACHALLENGERMATCH-26OCT12ROMRAM-ROM`) | 0.71 / 0.72 (1344) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Jesse De Jager vs Lewie Lane -- M15 Offenbach R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207431:210454:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jesse De Jager (`KXITFMATCH-26OCT12DEJLAN-DEJ`) | 0.53 / 0.58 (35) | 55.5% | 40.4% | 56.0% | 39.0% [39.0%-39.1%] | -- | -- | -- | -- | PASS | -15.1 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lewie Lane (`KXITFMATCH-26OCT12DEJLAN-LAN`) | 0.40 / 0.44 (36) | 42.0% | 59.6% | 44.0% | 61.0% [60.9%-61.0%] | -- | -- | -- | -- | PASS | +17.6 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 123.0; serve-point win A 61.7%, B 36.4%; Elo A 1198.0, B 1275.2; model uncertainty 0.0005
* Form inputs: days since last match A 728, B 728; matches on record A 28, B 76; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT12DEJLAN-LAN  (YES = Lewie Lane)
Model: 60%
Kalshi: 42%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexey Dubinin vs Joao Rasgado -- M25 Luanda R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12DUBRAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexey Dubinin (`KXITFMATCH-26OCT12DUBRAS-DUB`) | 0.65 / 0.94 (18) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Joao Rasgado (`KXITFMATCH-26OCT12DUBRAS-RAS`) | 0.06 / 0.35 (100) | 20.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andrea Guerrieri vs Abdullah Shelbayh -- ATP Challenger Olbia R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12GUESHE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea Guerrieri (`KXATPCHALLENGERMATCH-26OCT12GUESHE-GUE`) | 0.52 / 0.53 (2) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Abdullah Shelbayh (`KXATPCHALLENGERMATCH-26OCT12GUESHE-SHE`) | 0.46 / 0.47 (65) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Theo Herrmann vs Amar Tahirovic -- M15 Offenbach R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12HERTAH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theo Herrmann (`KXITFMATCH-26OCT12HERTAH-HER`) | 0.50 / 0.55 (0) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Amar Tahirovic (`KXITFMATCH-26OCT12HERTAH-TAH`) | 0.42 / 0.48 (60) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sebastian Grundtvig Jorgensen vs Noel Larwig -- M15 Offenbach R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207864:212963:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sebastian Grundtvig Jorgensen (`KXITFMATCH-26OCT12JORLAR-JOR`) | 0.46 / 0.52 (2) | 49.0% | 73.3% | 61.1% | 70.4% [70.3%-70.4%] | -- | -- | -- | -- | PASS | +24.3 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Noel Larwig (`KXITFMATCH-26OCT12JORLAR-LAR`) | 0.47 / 0.53 (6112) | 50.0% | 26.7% | 38.9% | 29.6% [29.6%-29.7%] | -- | -- | -- | -- | PASS | -23.3 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 110.0; serve-point win A 64.0%, B 40.8%; Elo A 1249.3, B 1103.4; model uncertainty 0.0004
* Form inputs: days since last match A 665, B 707; matches on record A 6, B 24; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT12JORLAR-JOR  (YES = Sebastian Grundtvig Jorgensen)
Model: 73%
Kalshi: 49%
Gap: +24 pp
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

## Maks Kasnikowski vs Cezar Cretu (b. 2001) -- ATP Challenger Olbia R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206470:209874:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cezar Cretu (b. 2001) (`KXATPCHALLENGERMATCH-26OCT12KASCRE-CRE`) | 0.29 / 0.30 (836) | 29.5% | 46.5% | 36.8% | 42.3% [40.8%-44.8%] | 31.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +17.0 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Maks Kasnikowski (`KXATPCHALLENGERMATCH-26OCT12KASCRE-KAS`) | 0.70 / 0.71 (7372) | 70.5% | 53.5% | 63.2% | 57.7% [55.2%-59.2%] | 68.8% | 70.2% | 70.2% | MODEL_LONE_OUTLIER | PASS | -17.0 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | B / ADEQUATE | EXTERNAL_STALE | AMBIGUOUS |

* Serve evidence (points): A 3304.0, B 1942.0; serve-point win A 60.0%, B 40.7%; Elo A 1597.8, B 1596.6; model uncertainty 0.0203
* Form inputs: days since last match A 23, B 14; matches on record A 272, B 337; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT12KASCRE-CRE  (YES = Cezar Cretu (b. 2001))
Model: 47%
Kalshi: 30%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: PLAYER_IDENTITY_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.020, surface_dev_loose +0.000, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Guelord Kayombo vs Nishith Naveen -- M25 Luanda R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12KAYNAV:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guelord Kayombo (`KXITFMATCH-26OCT12KAYNAV-KAY`) | 0.79 / 0.84 (6101) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nishith Naveen (`KXITFMATCH-26OCT12KAYNAV-NAV`) | 0.13 / 0.20 (6127) | 16.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Linus Lagerbohm vs Giammarco Gandolfi -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210631:210649:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giammarco Gandolfi (`KXITFMATCH-26OCT12LAGGAN-GAN`) | 0.18 / 0.23 (101) | 20.5% | -- | 46.5% | 26.3% [26.3%-27.9%] | -- | -- | -- | -- | PASS | +5.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Linus Lagerbohm (`KXITFMATCH-26OCT12LAGGAN-LAG`) | 0.74 / 0.80 (57) | 77.0% | -- | 53.5% | 73.7% [72.1%-73.7%] | -- | -- | -- | -- | PASS | -3.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 42.0, B 55.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0084
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.008, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Julien Penzlin vs Moritz Hoffmann -- M15 Offenbach R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206709:210114:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Moritz Hoffmann (`KXITFMATCH-26OCT12PENHOF-HOF`) | 0.22 / 0.30 (78) | 26.0% | -- | 50.0% | 48.0% [48.0%-48.0%] | -- | -- | -- | -- | PASS | +22.0 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Julien Penzlin (`KXITFMATCH-26OCT12PENHOF-PEN`) | 0.62 / 0.75 (57) | 68.5% | -- | 50.0% | 52.0% [52.0%-52.0%] | -- | -- | -- | -- | PASS | -16.5 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT12PENHOF-HOF  (YES = Moritz Hoffmann)
Model: 48%
Kalshi: 26%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rares Teodor Pieleanu vs Gabriele Pennaforti -- M25 Santa Margherita di Pula R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210398:212888:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriele Pennaforti (`KXITFMATCH-26OCT12PIEPEN-PEN`) | 0.45 / 0.51 (51) | 48.0% | -- | 53.1% | 81.5% [80.2%-82.6%] | -- | -- | -- | -- | PASS | +33.5 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rares Teodor Pieleanu (`KXITFMATCH-26OCT12PIEPEN-PIE`) | 0.46 / 0.52 (5120) | 49.0% | -- | 46.9% | 18.5% [17.4%-19.8%] | -- | -- | -- | -- | PASS | -30.5 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 61.0, B 652.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0121
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT12PIEPEN-PEN  (YES = Gabriele Pennaforti)
Model: 82%
Kalshi: 48%
Gap: +34 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.007, surface_dev_loose -0.001, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eliz Maloney vs Eloise Newberry -- W35 Birmingham R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12MALNEW:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eliz Maloney (`KXITFWMATCH-26OCT12MALNEW-MAL`) | 0.93 / 0.95 (1705) | 94.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eloise Newberry (`KXITFWMATCH-26OCT12MALNEW-NEW`) | 0.03 / 0.05 (7) | 4.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lois Newberry vs Kate Gardiner -- W35 Birmingham R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Grass · scheduled 2026-10-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222440:259964:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kate Gardiner (`KXITFWMATCH-26OCT12NEWGAR-GAR`) | 0.37 / 0.40 (130) | 38.5% | -- | 60.5% | 51.1% [50.0%-51.6%] | -- | -- | -- | -- | PASS | +12.6 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lois Newberry (`KXITFWMATCH-26OCT12NEWGAR-NEW`) | 0.54 / 0.63 (26) | 58.5% | -- | 39.5% | 48.9% [48.4%-50.0%] | -- | -- | -- | -- | PASS | -9.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 666.0, B 135.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.008
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anna Ozerova vs Lily Hutchings -- W35 Birmingham R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Grass · scheduled 2026-10-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216030:270177:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lily Hutchings (`KXITFWMATCH-26OCT12OZEHUT-HUT`) | 0.62 / 0.69 (5122) | 65.5% | -- | 35.4% | 44.7% [42.5%-45.7%] | -- | -- | -- | -- | PASS | -20.8 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna Ozerova (`KXITFWMATCH-26OCT12OZEHUT-OZE`) | 0.29 / 0.34 (29) | 31.5% | -- | 64.6% | 55.3% [54.3%-57.5%] | -- | -- | -- | -- | PASS | +23.8 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 140.0, B 129.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.016
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT12OZEHUT-OZE  (YES = Anna Ozerova)
Model: 55%
Kalshi: 32%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marie Weckerle vs Sophie Johnstone -- W35 Birmingham R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12WECJOH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sophie Johnstone (`KXITFWMATCH-26OCT12WECJOH-JOH`) | 0.07 / 0.12 (25) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marie Weckerle (`KXITFWMATCH-26OCT12WECJOH-WEC`) | 0.87 / 0.91 (118) | 89.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Francesco Forti vs Zdenek Kolar -- ATP Challenger Catania R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 15:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-12T15:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144645:209506:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesco Forti (`KXATPCHALLENGERMATCH-26OCT12FORKOL-FOR`) | 0.51 / 0.52 (1328) | 51.5% | 45.3% | 43.3% | 45.4% [44.3%-45.9%] | -- | 52.4% | 52.4% | MODEL_LONE_OUTLIER | PASS | -6.2 pp | NORMAL | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Zdenek Kolar (`KXATPCHALLENGERMATCH-26OCT12FORKOL-KOL`) | 0.48 / 0.49 (2429) | 48.5% | 54.7% | 56.7% | 54.6% [54.1%-55.7%] | -- | 47.4% | 47.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.2 pp | NORMAL | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1905.0, B 4035.0; serve-point win A 59.3%, B 39.8%; Elo A 1568.8, B 1588.8; model uncertainty 0.0078
* Form inputs: days since last match A 21, B 28; matches on record A 372, B 767; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Lisa Pigato vs Julia Avdeeva -- WTA 125K Rovereto R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-12 19:00Z
* Current expected start: 2026-10-12 16:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-12 15:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-12T19:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT12PIGAVD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julia Avdeeva (`KXWTACHALLENGERMATCH-26OCT12PIGAVD-AVD`) | 0.29 / 0.31 (1032) | 30.0% | -- | -- | -- [-----] | 31.2% | 30.6% | 30.6% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lisa Pigato (`KXWTACHALLENGERMATCH-26OCT12PIGAVD-PIG`) | 0.70 / 0.71 (1092) | 70.5% | -- | -- | -- [-----] | 68.8% | 70.0% | 70.0% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Adam Bajurko vs Afonso Oliveira -- M25 Luanda R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12BAJOLI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adam Bajurko (`KXITFMATCH-26OCT12BAJOLI-BAJ`) | 0.13 / 0.94 (16) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Afonso Oliveira (`KXITFMATCH-26OCT12BAJOLI-OLI`) | 0.08 / 0.66 (36) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Filip Drab vs Florin Cristian Lucaciu -- M15 Szabolcsveresmart R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12DRALUC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filip Drab (`KXITFMATCH-26OCT12DRALUC-DRA`) | 0.05 / 0.81 (0) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Florin Cristian Lucaciu (`KXITFMATCH-26OCT12DRALUC-LUC`) | 0.18 / 0.88 (100) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Trisztan Gubi vs Nicholas Volnik -- M15 Szabolcsveresmart R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12GUBVOL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Trisztan Gubi (`KXITFMATCH-26OCT12GUBVOL-GUB`) | 0.05 / 0.93 (11) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nicholas Volnik (`KXITFMATCH-26OCT12GUBVOL-VOL`) | 0.06 / 0.88 (100) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Radovan Michalik vs Filip Czyrek -- M15 Szabolcsveresmart R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12MICCZY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filip Czyrek (`KXITFMATCH-26OCT12MICCZY-CZY`) | 0.09 / 0.15 (57) | 12.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Radovan Michalik (`KXITFMATCH-26OCT12MICCZY-MIC`) | 0.71 / 0.92 (1518) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sumit Nagal vs Henrique Rocha -- ATP Challenger Maia R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111576:210012:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sumit Nagal (`KXATPCHALLENGERMATCH-26OCT12NAGROC-NAG`) | 0.24 / 0.25 (1) | 24.5% | 45.2% | 41.2% | 43.8% [41.7%-45.8%] | 26.5% | 25.0% | 25.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +20.7 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Henrique Rocha (`KXATPCHALLENGERMATCH-26OCT12NAGROC-ROC`) | 0.74 / 0.75 (419) | 74.5% | 54.8% | 58.8% | 56.2% [54.2%-58.3%] | 73.5% | 75.3% | 75.3% | MODEL_LONE_OUTLIER | PASS | -19.7 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3668.0, B 3638.0; serve-point win A 57.5%, B 41.6%; Elo A 1687.4, B 1680.4; model uncertainty 0.0207
* Form inputs: days since last match A 24, B 14; matches on record A 620, B 286; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT12NAGROC-NAG  (YES = Sumit Nagal)
Model: 45%
Kalshi: 24%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: EXTERNAL_STALE
Data quality: A (ADEQUATE)
Reasons: LOW_DISPLAYED_LIQUIDITY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.021, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE

## Andriy Poritskyy vs Oliver Pivnik -- M15 Szabolcsveresmart R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12PORPIV:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oliver Pivnik (`KXITFMATCH-26OCT12PORPIV-PIV`) | 0.23 / 0.31 (4) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Andriy Poritskyy (`KXITFMATCH-26OCT12PORPIV-POR`) | 0.58 / 0.80 (56) | 69.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pavel Skvortcov vs Sharath Murari -- M25 Luanda R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12SKVMUR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sharath Murari (`KXITFMATCH-26OCT12SKVMUR-MUR`) | 0.04 / 0.51 (100) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pavel Skvortcov (`KXITFMATCH-26OCT12SKVMUR-SKV`) | 0.45 / 0.95 (50) | 70.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amelie Brooks vs Chloe Cleaver -- W35 Birmingham R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12BROCLE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amelie Brooks (`KXITFWMATCH-26OCT12BROCLE-BRO`) | 0.79 / 0.87 (68) | 83.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Chloe Cleaver (`KXITFWMATCH-26OCT12BROCLE-CLE`) | 0.11 / 0.18 (74) | 14.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Edie Griffiths vs Michelle Dzjachangirova -- W35 Birmingham R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12GRIDZJ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michelle Dzjachangirova (`KXITFWMATCH-26OCT12GRIDZJ-DZJ`) | 0.04 / 0.12 (72) | 8.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Edie Griffiths (`KXITFWMATCH-26OCT12GRIDZJ-GRI`) | 0.82 / 0.93 (118) | 87.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Madelief Hageman vs Andrea Burguete Beltran -- W35 Birmingham R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Grass · scheduled 2026-10-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221568:239409:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea Burguete Beltran (`KXITFWMATCH-26OCT12HAGBUR-BUR`) | 0.20 / 0.24 (35) | 22.0% | -- | 42.1% | 42.6% [42.1%-42.6%] | -- | -- | -- | -- | PASS | +20.6 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Madelief Hageman (`KXITFWMATCH-26OCT12HAGBUR-HAG`) | 0.70 / 0.80 (104) | 75.0% | -- | 57.9% | 57.4% [57.4%-57.9%] | -- | -- | -- | -- | PASS | -17.6 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2662.0, B 45.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0026
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT12HAGBUR-BUR  (YES = Andrea Burguete Beltran)
Model: 43%
Kalshi: 22%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mia Wainwright vs Sophie Bekker -- W35 Birmingham R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Grass · scheduled 2026-10-12T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:261968:264392:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sophie Bekker (`KXITFWMATCH-26OCT12WAIBEK-BEK`) | 0.62 / 0.66 (46) | 64.0% | -- | 72.7% | 46.8% [46.8%-47.9%] | -- | -- | -- | -- | PASS | -17.2 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mia Wainwright (`KXITFWMATCH-26OCT12WAIBEK-WAI`) | 0.31 / 0.36 (39) | 33.5% | -- | 27.3% | 53.2% [52.1%-53.2%] | -- | -- | -- | -- | PASS | +19.7 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 547.0, B 19.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0053
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT12WAIBEK-WAI  (YES = Mia Wainwright)
Model: 53%
Kalshi: 34%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lorenzo Carboni vs Mackenzie McDonald -- ATP Challenger Olbia R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 16:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-12T16:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111456:212077:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Carboni (`KXATPCHALLENGERMATCH-26OCT12CARMCD-CAR`) | 0.20 / 0.21 (2097) | 20.5% | 23.6% | 18.1% | 22.8% [13.8%-35.0%] | 23.4% | 22.1% | 22.7% | ALL_THREE_DISAGREE | PASS | +3.1 pp | NORMAL | FRESH | C / LIMITED | ALL_AGREE | VERIFIED |
| Mackenzie McDonald (`KXATPCHALLENGERMATCH-26OCT12CARMCD-MCD`) | 0.79 / 0.80 (2935) | 79.5% | 76.4% | 82.0% | 77.2% [65.0%-86.2%] | 76.6% | 78.5% | 77.5% | MODEL_LONE_OUTLIER | PASS | -3.1 pp | NORMAL | FRESH | C / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 448.0, B 3014.0; serve-point win A 57.6%, B 36.8%; Elo A 1371.5, B 1566.3; model uncertainty 0.106
* Form inputs: days since last match A 161, B 14; matches on record A 79, B 617; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.082, surface_pool_high +0.122, surface_dev_loose +0.003, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Daniel Frasconi / Lorenzo Rocco vs Andrea Colombo / Simone Massellani -- ATP Challenger Olbia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 16:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-12T16:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12FRAROCCOLMAS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea Colombo / Simone Massellani (`KXATPCHALLENGERDOUBLES-26OCT12FRAROCCOLMAS-COLMAS`) | 0.09 / 0.95 (529) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daniel Frasconi / Lorenzo Rocco (`KXATPCHALLENGERDOUBLES-26OCT12FRAROCCOLMAS-FRAROC`) | 0.05 / 0.94 (4) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mika Brunold vs Mathys Domenc -- ATP Challenger Roanne R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-12T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12BRUDOM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mika Brunold (`KXATPCHALLENGERMATCH-26OCT12BRUDOM-BRU`) | 0.85 / 0.86 (78) | 85.5% | 89.3% | -- | -- [-----] | 82.9% | 85.5% | 85.5% | MODEL_LONE_OUTLIER | -- | +3.8 pp | NORMAL | FRESH | F / POOR | EXTERNAL_STALE | AMBIGUOUS |
| Mathys Domenc (`KXATPCHALLENGERMATCH-26OCT12BRUDOM-DOM`) | 0.14 / 0.15 (11959) | 14.5% | 10.7% | -- | -- [-----] | 17.1% | 15.9% | -- | INSUFFICIENT_INPUTS | -- | -3.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 66.3%, B 43.4%; Elo A 1510.5, B 1262.9; model uncertainty None
* Form inputs: days since last match A 672, B 812; matches on record A 128, B 2; data quality F
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Ivan Ivanov vs Gabriele Crivellaro -- M25 Santa Margherita di Pula R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12IVACRI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriele Crivellaro (`KXITFMATCH-26OCT12IVACRI-CRI`) | 0.24 / 0.27 (5129) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ivan Ivanov (`KXITFMATCH-26OCT12IVACRI-IVA`) | 0.74 / 0.75 (32) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Guillaume Dalmasso vs Aleksandr Braynin -- M15 Offenbach R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202089:211409:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aleksandr Braynin (`KXITFMATCH-26OCT12DALBRA-BRA`) | 0.51 / 0.53 (60) | 52.0% | 64.3% | 56.5% | 62.4% [61.5%-63.4%] | -- | -- | -- | -- | PASS | +12.3 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Guillaume Dalmasso (`KXITFMATCH-26OCT12DALBRA-DAL`) | 0.46 / 0.48 (115) | 47.0% | 35.6% | 43.5% | 37.6% [36.6%-38.6%] | -- | -- | -- | -- | PASS | -11.3 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 352.0, B 470.0; serve-point win A 61.1%, B 36.0%; Elo A 1296.7, B 1396.3; model uncertainty 0.0096
* Form inputs: days since last match A 98, B 322; matches on record A 47, B 160; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vincent Dullinger vs Filip Krolo -- M15 Offenbach R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212593:213629:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vincent Dullinger (`KXITFMATCH-26OCT12DULKRO-DUL`) | 0.51 / 0.52 (1) | 51.5% | 48.0% | 50.0% | 53.0% [53.0%-53.0%] | -- | -- | -- | -- | PASS | -3.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Filip Krolo (`KXITFMATCH-26OCT12DULKRO-KRO`) | 0.44 / 0.45 (210) | 44.5% | 52.0% | 50.0% | 47.0% [47.0%-47.0%] | -- | -- | -- | -- | PASS | +7.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 61.8%, B 37.8%; Elo A 1253.8, B 1233.3; model uncertainty 0.0
* Form inputs: days since last match A 707, B 707; matches on record A 1, B 18; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maes / Steveker vs Egbring / Hopfe -- M15 Offenbach R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-12T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12MAESTEEGBHOP:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Egbring / Hopfe (`KXITFDOUBLES-26OCT12MAESTEEGBHOP-EGBHOP`) | 0.06 / 0.92 (100) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maes / Steveker (`KXITFDOUBLES-26OCT12MAESTEEGBHOP-MAESTE`) | 0.05 / 0.95 (224) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Sascha Gueymard Wayenburg vs Liam Broady -- ATP Challenger Roanne R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-12T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12GUEBRO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liam Broady (`KXATPCHALLENGERMATCH-26OCT12GUEBRO-BRO`) | 0.28 / 0.29 (250) | 28.5% | -- | -- | -- [-----] | 30.3% | 29.1% | 29.1% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sascha Gueymard Wayenburg (`KXATPCHALLENGERMATCH-26OCT12GUEBRO-GUE`) | 0.70 / 0.72 (7392) | 71.0% | -- | -- | -- [-----] | 69.7% | 71.7% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Agwi / Vega vs De Jager / Antoine Tailleu -- M15 Offenbach R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-12T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12AGWVEGDEJANT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Agwi / Vega (`KXITFDOUBLES-26OCT12AGWVEGDEJANT-AGWVEG`) | 0.05 / 0.95 (124) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| De Jager / Antoine Tailleu (`KXITFDOUBLES-26OCT12AGWVEGDEJANT-DEJANT`) | 0.05 / 0.95 (124) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Raul Brancaccio / Pedro Martinez vs Joao Domingues / Tiago Torres -- ATP Challenger Maia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-12T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12BRAMARDOMTOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raul Brancaccio / Pedro Martinez (`KXATPCHALLENGERDOUBLES-26OCT12BRAMARDOMTOR-BRAMAR`) | 0.08 / 0.65 (20) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Joao Domingues / Tiago Torres (`KXATPCHALLENGERDOUBLES-26OCT12BRAMARDOMTOR-DOMTOR`) | 0.08 / 0.44 (36) | 26.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Yash Chaurasia vs Afonso Vaz Pinto -- M25 Luanda R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12CHAVAZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yash Chaurasia (`KXITFMATCH-26OCT12CHAVAZ-CHA`) | 0.77 / 0.95 (50) | 86.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Afonso Vaz Pinto (`KXITFMATCH-26OCT12CHAVAZ-VAZ`) | 0.04 / 0.23 (180) | 13.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Phil Dungs vs Flynn Thomas -- M15 Offenbach R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12DUNTHO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Phil Dungs (`KXITFMATCH-26OCT12DUNTHO-DUN`) | 0.10 / 0.13 (2) | 11.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Flynn Thomas (`KXITFMATCH-26OCT12DUNTHO-THO`) | 0.87 / 0.90 (181) | 88.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hammes / Lemke vs Eichenseher / Penzlin -- M15 Offenbach R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-12T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12HAMLEMEICPEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eichenseher / Penzlin (`KXITFDOUBLES-26OCT12HAMLEMEICPEN-EICPEN`) | 0.06 / 0.95 (124) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hammes / Lemke (`KXITFDOUBLES-26OCT12HAMLEMEICPEN-HAMLEM`) | 0.05 / 0.95 (224) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Pol Martin Tiffon vs Francisco Rocha -- ATP Challenger Maia R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-12T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12MARROC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pol Martin Tiffon (`KXATPCHALLENGERMATCH-26OCT12MARROC-MAR`) | 0.82 / 0.83 (1618) | 82.5% | -- | -- | -- [-----] | 80.3% | 82.1% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Francisco Rocha (`KXATPCHALLENGERMATCH-26OCT12MARROC-ROC`) | 0.17 / 0.18 (3930) | 17.5% | -- | -- | -- [-----] | 19.7% | 17.7% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Fred Barry Nimubona vs Melvin Vix -- M25 Luanda R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12NIMVIX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fred Barry Nimubona (`KXITFMATCH-26OCT12NIMVIX-NIM`) | 0.04 / 0.32 (18) | 18.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Melvin Vix (`KXITFMATCH-26OCT12NIMVIX-VIX`) | 0.64 / 0.95 (50) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexander Page vs Johan Mapuard -- M25 Luanda R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12PAGMAP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Johan Mapuard (`KXITFMATCH-26OCT12PAGMAP-MAP`) | 0.05 / 0.95 (50) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander Page (`KXITFMATCH-26OCT12PAGMAP-PAG`) | 0.05 / 0.95 (50) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jakub Kusy vs Mika Petkovic -- M15 Offenbach R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12KUSPET:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jakub Kusy (`KXITFMATCH-26OCT12KUSPET-KUS`) | 0.16 / 0.20 (23) | 18.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mika Petkovic (`KXITFMATCH-26OCT12KUSPET-PET`) | 0.82 / 0.84 (873) | 83.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bruna Liotto de Carvalho vs sofia omati albieri -- W15 Maceio R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:266574:267493:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| sofia omati albieri (`KXITFWMATCH-26OCT12LIOALB-ALB`) | 0.66 / 0.81 (5132) | 73.5% | -- | 72.2% | 65.6% [65.6%-65.7%] | -- | -- | -- | -- | PASS | -7.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Bruna Liotto de Carvalho (`KXITFWMATCH-26OCT12LIOALB-LIO`) | 0.14 / 0.28 (9) | 21.0% | -- | 27.8% | 34.4% [34.3%-34.4%] | -- | -- | -- | -- | PASS | +13.3 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 258.0, B 0.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0003
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Manuela Maia Citolino vs Lara Moreira Kanadani -- W15 Maceio R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12MAIMOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Manuela Maia Citolino (`KXITFWMATCH-26OCT12MAIMOR-MAI`) | 0.30 / 0.70 (83) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lara Moreira Kanadani (`KXITFWMATCH-26OCT12MAIMOR-MOR`) | 0.29 / 0.69 (81) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hugo Gaston vs Daniel Jade -- ATP Challenger Roanne R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-12T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12GASJAD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Gaston (`KXATPCHALLENGERMATCH-26OCT12GASJAD-GAS`) | 0.81 / 0.82 (542) | 81.5% | -- | -- | -- [-----] | 79.2% | 80.1% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daniel Jade (`KXATPCHALLENGERMATCH-26OCT12GASJAD-JAD`) | 0.18 / 0.19 (292) | 18.5% | -- | -- | -- [-----] | 20.8% | 18.0% | 18.0% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Caripi / Krolo vs Hoffmann / Mueller -- M15 Offenbach R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-12T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12CARKROHOFMUE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Caripi / Krolo (`KXITFDOUBLES-26OCT12CARKROHOFMUE-CARKRO`) | 0.05 / 0.95 (124) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hoffmann / Mueller (`KXITFDOUBLES-26OCT12CARKROHOFMUE-HOFMUE`) | 0.05 / 0.95 (124) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Francoise Abanda vs Tori Kinard -- W50 Quebec City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-12T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:203370:211796:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francoise Abanda (`KXITFWMATCH-26OCT12ABAKIN-ABA`) | 0.67 / 0.84 (5157) | 75.5% | -- | 64.7% | 79.4% [76.2%-83.9%] | -- | -- | -- | -- | PASS | +3.9 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tori Kinard (`KXITFWMATCH-26OCT12ABAKIN-KIN`) | 0.11 / 0.27 (37) | 19.0% | -- | 35.3% | 20.6% [16.1%-23.8%] | -- | -- | -- | -- | PASS | +1.6 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 902.0, B 725.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0387
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sabrina Dias vs Gabriela Guapindaia Soares -- W15 Maceio R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12DIAGUA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sabrina Dias (`KXITFWMATCH-26OCT12DIAGUA-DIA`) | 0.79 / 0.92 (59) | 85.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gabriela Guapindaia Soares (`KXITFWMATCH-26OCT12DIAGUA-GUA`) | 0.05 / 0.16 (80) | 10.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Raphaelle Lacasse vs Andrea Cabio -- W50 Quebec City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-12T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221165:267458:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea Cabio (`KXITFWMATCH-26OCT12LACCAB-CAB`) | 0.05 / 0.16 (80) | 10.5% | -- | 23.7% | 31.0% [27.2%-32.6%] | -- | -- | -- | -- | PASS | +20.5 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Raphaelle Lacasse (`KXITFWMATCH-26OCT12LACCAB-LAC`) | 0.79 / 0.93 (58) | 86.0% | -- | 76.3% | 69.0% [67.3%-72.8%] | -- | -- | -- | -- | PASS | -17.0 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1172.0, B 318.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0274
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT12LACCAB-CAB  (YES = Andrea Cabio)
Model: 31%
Kalshi: 10%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.009, surface_dev_loose +0.008, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Isabella Marton vs Emy Gauvin -- W50 Quebec City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12MARGAU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emy Gauvin (`KXITFWMATCH-26OCT12MARGAU-GAU`) | 0.05 / 0.30 (36) | 17.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Isabella Marton (`KXITFWMATCH-26OCT12MARGAU-MAR`) | 0.69 / 0.92 (59) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Isadora Sigrist vs Lais Mika Shibata -- W15 Maceio R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12SIGSHI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lais Mika Shibata (`KXITFWMATCH-26OCT12SIGSHI-SHI`) | 0.41 / 0.45 (70) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Isadora Sigrist (`KXITFWMATCH-26OCT12SIGSHI-SIG`) | 0.55 / 0.56 (56) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alberto Odiseo Alvarado Berrospi vs Thomas Enrique Menzel Piccioli -- M15 Quito R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12ALVMEN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alberto Odiseo Alvarado Berrospi (`KXITFMATCH-26OCT12ALVMEN-ALV`) | 0.27 / 0.53 (104) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Thomas Enrique Menzel Piccioli (`KXITFMATCH-26OCT12ALVMEN-MEN`) | 0.43 / 0.45 (45) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juan Sebastian Dominguez Collado vs Enmanuel Munoz -- M15 Quito R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12DOMMUN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Sebastian Dominguez Collado (`KXITFMATCH-26OCT12DOMMUN-DOM`) | 0.15 / 0.78 (0) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Enmanuel Munoz (`KXITFMATCH-26OCT12DOMMUN-MUN`) | 0.14 / 0.38 (40) | 26.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ivan Dreycopp vs Jose Luis Claro -- M15 Quito R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12DRECLA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jose Luis Claro (`KXITFMATCH-26OCT12DRECLA-CLA`) | 0.05 / 0.11 (72) | 8.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ivan Dreycopp (`KXITFMATCH-26OCT12DRECLA-DRE`) | 0.69 / 0.94 (112) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elias Julian Werner vs Miles Clark -- M15 Quito R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-12T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212473:213218:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miles Clark (`KXITFMATCH-26OCT12WERCLA-CLA`) | 0.68 / 0.92 (313) | 80.0% | -- | 50.0% | 43.9% [43.9%-43.9%] | -- | -- | -- | -- | PASS | -36.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Elias Julian Werner (`KXITFMATCH-26OCT12WERCLA-WER`) | 0.04 / 0.26 (26) | 15.0% | -- | 50.0% | 56.1% [56.1%-56.1%] | -- | -- | -- | -- | PASS | +41.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT12WERCLA-WER  (YES = Elias Julian Werner)
Model: 56%
Kalshi: 15%
Gap: +41 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Michaela Bayerlova vs Mia Kupres -- W50 Quebec City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-12T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215693:222377:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michaela Bayerlova (`KXITFWMATCH-26OCT12BAYKUP-BAY`) | 0.26 / 0.43 (5) | 34.5% | -- | 35.9% | 38.4% [33.4%-42.6%] | -- | -- | -- | -- | PASS | +3.9 pp | NORMAL | FRESH | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mia Kupres (`KXITFWMATCH-26OCT12BAYKUP-KUP`) | 0.50 / 0.68 (79) | 59.0% | -- | 64.1% | 61.6% [57.4%-66.6%] | -- | -- | -- | -- | PASS | +2.6 pp | NORMAL | FRESH | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1530.0, B 144.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0459
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.050, surface_pool_high +0.041, surface_dev_loose -0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Johnson vs McKenna Schaefbauer -- W100 Edmond OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-12T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:239103:260338:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Johnson (`KXITFWMATCH-26OCT12JOHSCH-JOH`) | 0.70 / 0.94 (438) | 82.0% | -- | 96.4% | 79.6% [75.7%-82.9%] | -- | -- | -- | -- | PASS | -2.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| McKenna Schaefbauer (`KXITFWMATCH-26OCT12JOHSCH-SCH`) | 0.03 / 0.17 (23) | 10.0% | -- | 3.6% | 20.4% [17.1%-24.3%] | -- | -- | -- | -- | PASS | +10.4 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1199.0, B 204.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0362
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.036, surface_dev_loose -0.000, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anastasia Kulikova vs Allura Zamarripa -- W100 Edmond OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-12T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214741:221440:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasia Kulikova (`KXITFWMATCH-26OCT12KULZAM-KUL`) | 0.55 / 0.94 (438) | 74.5% | -- | 40.6% | 59.4% [53.7%-64.5%] | -- | -- | -- | -- | PASS | -15.1 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Allura Zamarripa (`KXITFWMATCH-26OCT12KULZAM-ZAM`) | 0.03 / 0.37 (40) | 20.0% | -- | 59.4% | 40.6% [35.5%-46.3%] | -- | -- | -- | -- | PASS | +20.6 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1819.0, B 454.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0541
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT12KULZAM-ZAM  (YES = Allura Zamarripa)
Model: 41%
Kalshi: 20%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ashley Lahey vs Anne Christine Lutkemeyer -- W100 Edmond OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12LAHLUT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ashley Lahey (`KXITFWMATCH-26OCT12LAHLUT-LAH`) | 0.35 / 0.58 (44) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anne Christine Lutkemeyer (`KXITFWMATCH-26OCT12LAHLUT-LUT`) | 0.33 / 0.65 (83) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kallista Liu vs Ava Catanzarite -- W50 Quebec City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-12T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260303:264180:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ava Catanzarite (`KXITFWMATCH-26OCT12LIUCAT-CAT`) | 0.48 / 0.52 (104) | 50.0% | -- | 53.2% | 48.9% [47.9%-50.5%] | -- | -- | -- | -- | PASS | -1.1 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kallista Liu (`KXITFWMATCH-26OCT12LIUCAT-LIU`) | 0.45 / 0.49 (2) | 47.0% | -- | 46.8% | 51.1% [49.5%-52.1%] | -- | -- | -- | -- | PASS | +4.1 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1064.0, B 106.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0134
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lilian Poling vs Luisa Hrda -- W50 Quebec City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-12T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221585:222358:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luisa Hrda (`KXITFWMATCH-26OCT12POLHRD-HRD`) | 0.04 / 0.21 (24) | 12.5% | -- | 84.5% | 52.1% [51.1%-54.3%] | -- | -- | -- | -- | PASS | +39.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lilian Poling (`KXITFWMATCH-26OCT12POLHRD-POL`) | 0.69 / 0.94 (5416) | 81.5% | -- | 15.5% | 47.9% [45.7%-48.9%] | -- | -- | -- | -- | PASS | -33.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1063.0, B 0.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.016
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT12POLHRD-HRD  (YES = Luisa Hrda)
Model: 52%
Kalshi: 12%
Gap: +40 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.021, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anna Rogers vs Kennedy Drenser-Hagmann -- W100 Edmond OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12ROGDRE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kennedy Drenser-Hagmann (`KXITFWMATCH-26OCT12ROGDRE-DRE`) | 0.07 / 0.35 (39) | 21.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anna Rogers (`KXITFWMATCH-26OCT12ROGDRE-ROG`) | 0.57 / 0.92 (5313) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chukwumelije Clarke vs Briana Szabo -- W100 Edmond OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-12T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223120:269864:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chukwumelije Clarke (`KXITFWMATCH-26OCT12CLASZA-CLA`) | 0.51 / 0.68 (48) | 59.5% | -- | 71.7% | 63.6% [59.5%-66.1%] | -- | -- | -- | -- | PASS | +4.1 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Briana Szabo (`KXITFWMATCH-26OCT12CLASZA-SZA`) | 0.26 / 0.40 (42) | 33.0% | -- | 28.3% | 36.4% [33.9%-40.5%] | -- | -- | -- | -- | PASS | +3.4 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 633.0, B 1762.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0328
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.025, surface_dev_tight -0.025
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## ISABELA DE MATTOS SILVA vs Barbara Gatica -- W15 Maceio R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211903:270013:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ISABELA DE MATTOS SILVA (`KXITFWMATCH-26OCT12DEMGAT-DEM`) | 0.03 / 0.95 (50) | 49.0% | -- | 26.9% | 6.4% [6.1%-6.9%] | -- | -- | -- | -- | PASS | -42.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Barbara Gatica (`KXITFWMATCH-26OCT12DEMGAT-GAT`) | 0.03 / 0.95 (50) | 49.0% | -- | 73.1% | 93.6% [93.1%-93.9%] | -- | -- | -- | -- | PASS | +44.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 55.0, B 633.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0039
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT12DEMGAT-GAT  (YES = Barbara Gatica)
Model: 94%
Kalshi: 49%
Gap: +45 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Reina Goto vs Martina Okalova -- W100 Edmond OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-12T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214862:260737:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Reina Goto (`KXITFWMATCH-26OCT12GOTOKA-GOT`) | 0.59 / 0.94 (438) | 76.5% | -- | 77.7% | 64.1% [50.0%-71.3%] | -- | -- | -- | -- | PASS | -12.4 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Martina Okalova (`KXITFWMATCH-26OCT12GOTOKA-OKA`) | 0.03 / 0.32 (32) | 17.5% | -- | 22.3% | 35.9% [28.7%-50.0%] | -- | -- | -- | -- | PASS | +18.4 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1864.0, B 1467.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1066
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT12GOTOKA-OKA  (YES = Martina Okalova)
Model: 36%
Kalshi: 18%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.010, surface_dev_loose +0.015, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thara Gowda vs Sophia Xie -- W50 Quebec City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12GOWXIE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thara Gowda (`KXITFWMATCH-26OCT12GOWXIE-GOW`) | 0.45 / 0.95 (50) | 70.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sophia Xie (`KXITFWMATCH-26OCT12GOWXIE-XIE`) | 0.03 / 0.58 (30) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rose Marie Nijkamp vs Alina Shcherbinina -- W100 Edmond OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-12T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221278:260225:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rose Marie Nijkamp (`KXITFWMATCH-26OCT12NIJSHC-NIJ`) | 0.03 / 0.34 (29) | 18.5% | -- | 58.0% | 63.2% [60.6%-67.6%] | -- | -- | -- | -- | PASS | +44.7 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alina Shcherbinina (`KXITFWMATCH-26OCT12NIJSHC-SHC`) | 0.58 / 0.94 (416) | 76.0% | -- | 42.0% | 36.8% [32.4%-39.4%] | -- | -- | -- | -- | PASS | -39.2 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1080.0, B 127.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0349
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT12NIJSHC-NIJ  (YES = Rose Marie Nijkamp)
Model: 63%
Kalshi: 18%
Gap: +45 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.035, surface_pool_high -0.026, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bruna Roberta Bouth Pinheiro vs Sophia Santos -- W15 Maceio R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12ROBSAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bruna Roberta Bouth Pinheiro (`KXITFWMATCH-26OCT12ROBSAN-ROB`) | 0.03 / 0.95 (50) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sophia Santos (`KXITFWMATCH-26OCT12ROBSAN-SAN`) | 0.03 / 0.95 (50) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jamilah Snells vs Maya Iacoban -- W50 Quebec City R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12SNEIAC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maya Iacoban (`KXITFWMATCH-26OCT12SNEIAC-IAC`) | 0.09 / 0.10 (8) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jamilah Snells (`KXITFWMATCH-26OCT12SNEIAC-SNE`) | 0.88 / 0.91 (311) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexandra Vagramov vs Alana Smith -- W100 Edmond OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-12T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215545:220673:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alana Smith (`KXITFWMATCH-26OCT12VAGSMI-SMI`) | 0.62 / 0.94 (5438) | 78.0% | -- | 26.3% | 45.9% [37.9%-59.9%] | -- | -- | -- | -- | PASS | -32.1 pp | EXTREME (DATA_WARNING) | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexandra Vagramov (`KXITFWMATCH-26OCT12VAGSMI-VAG`) | 0.04 / 0.29 (41) | 16.5% | -- | 73.7% | 54.1% [40.1%-62.2%] | -- | -- | -- | -- | PASS | +37.6 pp | EXTREME (DATA_WARNING) | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1940.0, B 1759.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1101
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT12VAGSMI-VAG  (YES = Alexandra Vagramov)
Model: 54%
Kalshi: 16%
Gap: +38 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: WIDE_SPREAD, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose +0.005, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Victor Bini vs Gonzalo Zeitune -- M15 Quito R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-12T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211698:212192:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Victor Bini (`KXITFMATCH-26OCT12BINZEI-BIN`) | 0.58 / 0.74 (48) | 66.0% | 62.1% | 72.1% | 58.1% [57.1%-58.1%] | -- | -- | -- | -- | PASS | -3.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Gonzalo Zeitune (`KXITFMATCH-26OCT12BINZEI-ZEI`) | 0.22 / 0.34 (5138) | 28.0% | 37.9% | 27.9% | 41.9% [41.9%-42.9%] | -- | -- | -- | -- | PASS | +9.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 83.0; serve-point win A 63.1%, B 39.3%; Elo A 1225.6, B 1169.0; model uncertainty 0.005
* Form inputs: days since last match A 1155, B 707; matches on record A 3, B 9; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nicolas Hollender vs Franco Marini -- M15 Quito R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-12T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210598:211699:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Hollender (`KXITFMATCH-26OCT12HOLMAR-HOL`) | 0.48 / 0.72 (90) | 60.0% | 45.4% | 38.4% | 39.9% [38.9%-40.0%] | -- | -- | -- | -- | PASS | -14.6 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Franco Marini (`KXITFMATCH-26OCT12HOLMAR-MAR`) | 0.25 / 0.44 (7) | 34.5% | 54.6% | 61.6% | 60.1% [60.0%-61.1%] | -- | -- | -- | -- | PASS | +20.1 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 70.0, B 0.0; serve-point win A 60.9%, B 38.2%; Elo A 1078.1, B 1152.2; model uncertainty 0.0051
* Form inputs: days since last match A 686, B 1057; matches on record A 11, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT12HOLMAR-MAR  (YES = Franco Marini)
Model: 55%
Kalshi: 34%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Manuel Mouilleron Salvo vs Juan Carlos Fuentes Vasquez -- M15 Quito R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-12T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211389:212720:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Carlos Fuentes Vasquez (`KXITFMATCH-26OCT12MOUFUE-FUE`) | 0.28 / 0.45 (45) | 36.5% | -- | 40.8% | 86.2% [84.9%-87.8%] | -- | -- | -- | -- | PASS | +49.7 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Manuel Mouilleron Salvo (`KXITFMATCH-26OCT12MOUFUE-MOU`) | 0.48 / 0.63 (68) | 55.5% | -- | 59.2% | 13.8% [12.2%-15.1%] | -- | -- | -- | -- | PASS | -41.7 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 107.0, B 72.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0145
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT12MOUFUE-FUE  (YES = Juan Carlos Fuentes Vasquez)
Model: 86%
Kalshi: 36%
Gap: +50 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.006, surface_pool_high +0.000, surface_dev_loose -0.001, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andres Urrea vs Facundo Perlov -- M15 Quito R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT12URRPER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Facundo Perlov (`KXITFMATCH-26OCT12URRPER-PER`) | 0.15 / 0.36 (40) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Andres Urrea (`KXITFMATCH-26OCT12URRPER-URR`) | 0.55 / 0.85 (5190) | 70.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Antonella Azambuja Werner vs Vitoria Zuccon -- W15 Maceio R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12AZAZUC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Antonella Azambuja Werner (`KXITFWMATCH-26OCT12AZAZUC-AZA`) | 0.03 / 0.55 (56) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vitoria Zuccon (`KXITFWMATCH-26OCT12AZAZUC-ZUC`) | 0.39 / 0.94 (416) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Elena Cabezas Dominguez vs Sara Shumate -- W100 Edmond OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-12T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221982:270081:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Elena Cabezas Dominguez (`KXITFWMATCH-26OCT12CABSHU-CAB`) | 0.37 / 0.94 (438) | 65.5% | -- | 79.9% | 80.6% [78.8%-83.7%] | -- | -- | -- | -- | PASS | +15.1 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sara Shumate (`KXITFWMATCH-26OCT12CABSHU-SHU`) | 0.03 / 0.66 (106) | 34.5% | -- | 20.1% | 19.4% [16.3%-21.2%] | -- | -- | -- | -- | PASS | -15.1 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1826.0, B 278.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0244
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT12CABSHU-CAB  (YES = Sofia Elena Cabezas Dominguez)
Model: 81%
Kalshi: 66%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.007, surface_dev_loose +0.003, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zoie Epps vs Evialina Laskevich -- W100 Edmond OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12EPPLAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zoie Epps (`KXITFWMATCH-26OCT12EPPLAS-EPP`) | 0.03 / 0.28 (35) | 15.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Evialina Laskevich (`KXITFWMATCH-26OCT12EPPLAS-LAS`) | 0.65 / 0.94 (416) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ana Clara Furlan Britzki vs Maria Jose Rico Sanchez -- W15 Maceio R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-12T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12FURRIC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ana Clara Furlan Britzki (`KXITFWMATCH-26OCT12FURRIC-FUR`) | 0.47 / 0.58 (51) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maria Jose Rico Sanchez (`KXITFWMATCH-26OCT12FURRIC-RIC`) | 0.36 / 0.47 (47) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rasheeda McAdoo vs Edda Mamedova -- W100 Edmond OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-12T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213771:239422:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Edda Mamedova (`KXITFWMATCH-26OCT12MCAMAM-MAM`) | 0.03 / 0.53 (54) | 28.0% | -- | 85.7% | 67.8% [51.1%-77.8%] | -- | -- | -- | -- | PASS | +39.8 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rasheeda McAdoo (`KXITFWMATCH-26OCT12MCAMAM-MCA`) | 0.39 / 0.94 (416) | 66.5% | -- | 14.3% | 32.2% [22.2%-48.9%] | -- | -- | -- | -- | PASS | -34.3 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1119.0, B 879.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1335
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT12MCAMAM-MAM  (YES = Edda Mamedova)
Model: 68%
Kalshi: 28%
Gap: +40 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.029, surface_pool_high -0.028, surface_dev_loose -0.018, surface_dev_tight +0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chloe Noel vs Valeriya Strakhova -- W100 Edmond OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-12 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-12T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211063:223402:2026-10-12`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chloe Noel (`KXITFWMATCH-26OCT12NOESTR-NOE`) | 0.36 / 0.94 (438) | 65.0% | -- | 85.0% | 69.8% [47.3%-79.6%] | -- | -- | -- | -- | PASS | +4.8 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valeriya Strakhova (`KXITFWMATCH-26OCT12NOESTR-STR`) | 0.03 / 0.56 (43) | 29.5% | -- | 14.9% | 30.1% [20.4%-52.7%] | -- | -- | -- | -- | PASS | +0.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1408.0, B 2323.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1611
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.028, surface_pool_high +0.027, surface_dev_loose +0.013, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Julia Adams vs Diae El Jardi -- W100 Edmond OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12ADAELJ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julia Adams (`KXITFWMATCH-26OCT12ADAELJ-ADA`) | 0.56 / 0.94 (438) | 75.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Diae El Jardi (`KXITFWMATCH-26OCT12ADAELJ-ELJ`) | 0.03 / 0.36 (46) | 19.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Shria Atturu vs Thea Frodin -- W100 Edmond OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12ATTFRO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shria Atturu (`KXITFWMATCH-26OCT12ATTFRO-ATT`) | 0.03 / 0.08 (20) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Thea Frodin (`KXITFWMATCH-26OCT12ATTFRO-FRO`) | 0.88 / 0.95 (80) | 91.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carmen Andreea Herea vs Zoe Hammond -- W100 Edmond OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12HERHAM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zoe Hammond (`KXITFWMATCH-26OCT12HERHAM-HAM`) | 0.03 / 0.21 (24) | 12.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Carmen Andreea Herea (`KXITFWMATCH-26OCT12HERHAM-HER`) | 0.70 / 0.94 (416) | 82.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Olivia Lincer vs Dana Guzman -- W100 Edmond OK R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-13T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT12LINGUZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dana Guzman (`KXITFWMATCH-26OCT12LINGUZ-GUZ`) | 0.52 / 0.94 (438) | 73.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Olivia Lincer (`KXITFWMATCH-26OCT12LINGUZ-LIN`) | 0.03 / 0.40 (42) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ann Li vs Camila Osorio -- WTA Wuhan R64

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-13 06:00Z
* Current expected start: 2026-10-13 06:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-13 05:15Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-13T04:00:00+00:00 as not a valid time

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-13T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT12ANNOSO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ann Li (`KXWTAMATCH-26OCT12ANNOSO-ANN`) | 0.50 / 0.54 (152) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Camila Osorio (`KXWTAMATCH-26OCT12ANNOSO-OSO`) | 0.46 / 0.49 (5150) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Sonay Kartal vs Belinda Bencic -- WTA Wuhan R32

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-13 06:00Z
* Current expected start: 2026-10-13 06:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-13 05:15Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-10-14T04:00:00+00:00 as not a valid time

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-13T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT12KARBEN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Belinda Bencic (`KXWTAMATCH-26OCT12KARBEN-BEN`) | 0.12 / 0.93 (222) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sonay Kartal (`KXWTAMATCH-26OCT12KARBEN-KAR`) | 0.09 / 0.92 (14) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Hubert Hurkacz vs Alejandro Davidovich Fokina -- ATP Shanghai R16

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-13 07:00Z
* Current expected start: 2026-10-13 07:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: 2026-10-13 06:15Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-13T04:00:00+00:00 as not a valid time

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-13T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT13HURDAV:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alejandro Davidovich Fokina (`KXATPMATCH-26OCT13HURDAV-DAV`) | 0.47 / 0.49 (37924) | 48.0% | -- | -- | -- [-----] | 47.8% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hubert Hurkacz (`KXATPMATCH-26OCT13HURDAV-HUR`) | 0.51 / 0.53 (38680) | 52.0% | -- | -- | -- [-----] | 52.2% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Theo Arribage / Albano Olivetti vs Ivan Liutarevich / Daniil Medvedev -- ATP Shanghai R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-13T04:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-13T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13ARROLILIUMED:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theo Arribage / Albano Olivetti (`KXATPDOUBLES-26OCT13ARROLILIUMED-ARROLI`) | 0.63 / 0.67 (1) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ivan Liutarevich / Daniil Medvedev (`KXATPDOUBLES-26OCT13ARROLILIUMED-LIUMED`) | 0.31 / 0.36 (76) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Austin Krajicek / Nikola Mektic vs Lucas Miedler / Neil Oberleitner -- ATP Shanghai R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-13T04:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-13T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13KRAMEKMIEOBE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Austin Krajicek / Nikola Mektic (`KXATPDOUBLES-26OCT13KRAMEKMIEOBE-KRAMEK`) | 0.54 / 0.63 (8) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucas Miedler / Neil Oberleitner (`KXATPDOUBLES-26OCT13KRAMEKMIEOBE-MIEOBE`) | 0.29 / 0.40 (53) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Marc Polmans / Jan Zielinski vs Julian Cash / Lloyd Glasspool -- ATP Shanghai R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-13 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-12 05:16Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-13T04:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-13T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT13POLZIECASGLA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julian Cash / Lloyd Glasspool (`KXATPDOUBLES-26OCT13POLZIECASGLA-CASGLA`) | 0.67 / 0.71 (52) | 69.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marc Polmans / Jan Zielinski (`KXATPDOUBLES-26OCT13POLZIECASGLA-POLZIE`) | 0.28 / 0.31 (12) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
