# ASSISTED SLATE -- 2026-10-04T04:54Z (`SL-20261004T045435Z-18c223be`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

190 open matches not seen started, 559 markets. Skipped: {"first_ball_already_observed": 8}. Sources: shadow board 2026-10-04T00:59:44.456754+00:00, Model 4 2026-10-03T12:16:39.954681+00:00, Gen-1 ledger 2026-10-03T21:45:53.831770+00:00, external 2026-10-04T04:25:13.788180+00:00, capture 20261004T042031Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-10-04 05:00Z**
* Recommended RUN TENNIS time: **2026-10-04 04:15Z**  (**OVERDUE -- run now**)
* Final price/status check time: **2026-10-04 04:50Z**
* Number of matches in window: 5 (Hubert Hurkacz vs Karen Khachanov, Valentin Vacherot vs Arthur Fils, Daria Snigur vs Taylah Preston, Alex de Minaur vs Andrey Rublev, Linda Noskova vs Viktorija Golubic)

* **10 main-tour match(es) have NO verified start status** (START_UNKNOWN, STATUS_AMBIGUOUS): BET blocked until a live status check.

Slate built 2026-10-04T04:54Z. Refresh due by: 2026-10-04 04:15Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 35, "HIGH_REVIEW": 26, "NORMAL": 94, "REVIEW": 27, "UNPRICED": 377}; match winners: {"EXTREME": 35, "HIGH_REVIEW": 25, "NORMAL": 93, "REVIEW": 25, "UNPRICED": 202}; quote freshness at build: {"STALE": 182}.

## Yujia Huang vs Darya Khomutsianskaya -- WTA 125K Suzhou Q1

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-03 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

WTA125 (WTA_125) · surface ? · scheduled 2026-10-03T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT02HUAKHO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yujia Huang (`KXWTACHALLENGERMATCH-26OCT02HUAKHO-HUA`) | 0.60 / 0.61 (14751) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Darya Khomutsianskaya (`KXWTACHALLENGERMATCH-26OCT02HUAKHO-KHO`) | 0.39 / 0.40 (7683) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE

## Millen Hurrion vs Kerem Yilmaz -- M15 Baku SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-03T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209140:212030:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Millen Hurrion (`KXITFMATCH-26OCT03HURYIL-HUR`) | 0.80 / 0.85 (3) | 82.5% | 77.2% | 76.4% | 78.4% [76.8%-79.5%] | -- | -- | -- | -- | PASS | -4.1 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kerem Yilmaz (`KXITFMATCH-26OCT03HURYIL-YIL`) | 0.16 / 0.21 (3) | 18.5% | 22.8% | 23.6% | 21.6% [20.5%-23.2%] | -- | -- | -- | -- | PASS | +3.1 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3153.0, B 1537.0; serve-point win A 67.0%, B 39.0%; Elo A 1476.4, B 1224.3; model uncertainty 0.0138
* Form inputs: days since last match A 61, B 61; matches on record A 183, B 45; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marcus Walters vs Digvijay Pratap Singh -- M15 Baku SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-03T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126971:200014:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Digvijay Pratap Singh (`KXITFMATCH-26OCT03WALSIN-SIN`) | 0.61 / 0.69 (5) | 65.0% | 59.5% | 54.9% | 59.3% [57.3%-61.3%] | -- | -- | -- | -- | PASS | -5.7 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marcus Walters (`KXITFMATCH-26OCT03WALSIN-WAL`) | 0.29 / 0.30 (1) | 29.5% | 40.5% | 45.1% | 40.7% [38.7%-42.7%] | -- | -- | -- | -- | WATCH | +11.2 pp | REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2102.0, B 2204.0; serve-point win A 63.0%, B 35.0%; Elo A 1257.0, B 1360.6; model uncertainty 0.0197
* Form inputs: days since last match A 89, B 19; matches on record A 106, B 181; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Polina Kudermetova vs Mirra Andreeva -- WTA Beijing R32

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-04 04:46Z
* Source: COURT_PROGRESSION: preceding match on Lotus finished; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 04:01Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT03KUDAND:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mirra Andreeva (`KXWTAMATCH-26OCT03KUDAND-AND`) | 0.91 / 0.92 (62712) | 91.5% | -- | -- | -- [-----] | 89.1% | 90.5% | 90.5% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Polina Kudermetova (`KXWTAMATCH-26OCT03KUDAND-KUD`) | 0.09 / 0.10 (38049) | 9.5% | -- | -- | -- [-----] | 10.9% | 9.6% | 9.6% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; STATUS_AMBIGUOUS; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Yidi Yang vs Rina Saigo -- WTA 125K Suzhou Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-03 06:00Z
* Current expected start: 2026-10-04 04:50Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 04:05Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA125 (WTA_125) · surface ? · scheduled 2026-10-03T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT02YANSAI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rina Saigo (`KXWTACHALLENGERMATCH-26OCT02YANSAI-SAI`) | 0.49 / 0.50 (1744) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yidi Yang (`KXWTACHALLENGERMATCH-26OCT02YANSAI-YAN`) | 0.50 / 0.51 (19) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE; STALE_QUOTE

## Ekaterina Alexandrova vs Diana Shnaider -- WTA Beijing R32

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-04 04:50Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 04:05Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT03ALESHN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Alexandrova (`KXWTAMATCH-26OCT03ALESHN-ALE`) | 0.33 / 0.34 (11907) | 33.5% | -- | -- | -- [-----] | 34.2% | 34.1% | 34.2% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Diana Shnaider (`KXWTAMATCH-26OCT03ALESHN-SHN`) | 0.66 / 0.67 (19119) | 66.5% | -- | -- | -- [-----] | 65.8% | 65.8% | 65.8% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; STATUS_AMBIGUOUS; STALE_QUOTE; WIDE_SPREAD

## Katarina Zavatska vs Kristiana Sidorova -- WTA 125K Suzhou Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-03 08:00Z
* Current expected start: 2026-10-04 04:50Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 04:05Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA125 (WTA_125) · surface ? · scheduled 2026-10-03T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT03ZAVSID:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kristiana Sidorova (`KXWTACHALLENGERMATCH-26OCT03ZAVSID-SID`) | 0.64 / 0.65 (5) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Katarina Zavatska (`KXWTACHALLENGERMATCH-26OCT03ZAVSID-ZAV`) | 0.35 / 0.36 (1316) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Jessica Bouzas Maneiro vs Alexandra Shubladze -- WTA 125K Jingshan F

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-04 07:30Z
* Current expected start: 2026-10-04 04:50Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 04:05Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA125 (WTA_125) · surface ? · scheduled 2026-10-04T07:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT04BOUSHU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jessica Bouzas Maneiro (`KXWTACHALLENGERMATCH-26OCT04BOUSHU-BOU`) | 0.62 / 0.63 (3380) | 62.5% | -- | -- | -- [-----] | 60.9% | 61.6% | 61.6% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexandra Shubladze (`KXWTACHALLENGERMATCH-26OCT04BOUSHU-SHU`) | 0.37 / 0.38 (4744) | 37.5% | -- | -- | -- [-----] | 39.1% | 38.0% | 38.0% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; STATUS_AMBIGUOUS; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Zeynep Sonmez / Donna Vekic vs Ellen Perez / Demi Schuurs -- WTA Beijing R32

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-04 07:10Z
* Current expected start: 2026-10-04 04:50Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 04:05Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T07:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT04SONVEKPERSCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ellen Perez / Demi Schuurs (`KXWTADOUBLES-26OCT04SONVEKPERSCH-PERSCH`) | 0.05 / 0.85 (50) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Zeynep Sonmez / Donna Vekic (`KXWTADOUBLES-26OCT04SONVEKPERSCH-SONVEK`) | 0.05 / 0.85 (50) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; STATUS_AMBIGUOUS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Hubert Hurkacz vs Karen Khachanov -- ATP Beijing QF

**START STATUS: START_IMMINENT**
* Nominal schedule: 2026-10-04 06:00Z
* Current expected start: 2026-10-04 05:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 04:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-60_MIN

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT03HURKHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hubert Hurkacz (`KXATPMATCH-26OCT03HURKHA-HUR`) | 0.39 / 0.40 (250274) | 39.5% | -- | -- | -- [-----] | 41.7% | 40.2% | 40.9% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Karen Khachanov (`KXATPMATCH-26OCT03HURKHA-KHA`) | 0.60 / 0.61 (23719) | 60.5% | -- | -- | -- [-----] | 58.3% | 60.3% | 59.3% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Han Shi vs Chengyiyi Yuan -- WTA 125K Suzhou Q1

**START STATUS: START_IMMINENT**
* Nominal schedule: 2026-10-03 06:00Z
* Current expected start: 2026-10-04 05:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 04:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-03T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT02SHIYUA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Han Shi (`KXWTACHALLENGERMATCH-26OCT02SHIYUA-SHI`) | 0.87 / 0.88 (2991) | 87.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Chengyiyi Yuan (`KXWTACHALLENGERMATCH-26OCT02SHIYUA-YUA`) | 0.12 / 0.14 (8585) | 13.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE

## Naoya Honda vs Kristjan Tamm -- ATP Challenger Wuning 3 Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-04T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144932:211897:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naoya Honda (`KXATPCHALLENGERMATCH-26OCT03HONTAM-HON`) | -- / 0.01 (185523) | -- | -- | 81.5% | 74.2% [66.5%-77.9%] | -- | 71.8% | -- | INSUFFICIENT_INPUTS | WATCH | -- | UNPRICED | STALE | C / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |
| Kristjan Tamm (`KXATPCHALLENGERMATCH-26OCT03HONTAM-TAM`) | 0.99 / -- (0) | -- | -- | 18.5% | 25.8% [22.1%-33.5%] | -- | 28.0% | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | STALE | C / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 2045.0, B 1552.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0572
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.008, surface_dev_loose +0.011, surface_dev_tight -0.019
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE

## Rinky Hijikata / Kaito Uesugi vs Theo Arribage / Albano Olivetti -- ATP Tokyo SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 05:00Z
* Current expected start: 2026-10-04 05:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 04:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-04T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03HIJUESARROLI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theo Arribage / Albano Olivetti (`KXATPDOUBLES-26OCT03HIJUESARROLI-ARROLI`) | 0.63 / 0.64 (719) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rinky Hijikata / Kaito Uesugi (`KXATPDOUBLES-26OCT03HIJUESARROLI-HIJUES`) | 0.36 / 0.37 (946) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Valentin Vacherot vs Arthur Fils -- ATP Tokyo QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 05:00Z
* Current expected start: 2026-10-04 05:46Z
* Source: COURT_PROGRESSION: preceding match on Colosseum in progress (set 1 of best-of-5); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 05:01Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+46_MIN

ATP (TOUR_500_250) · surface ? · scheduled 2026-10-04T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT03VACFIL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arthur Fils (`KXATPMATCH-26OCT03VACFIL-FIL`) | 0.79 / 0.80 (40464) | 79.5% | -- | -- | -- [-----] | 76.2% | 79.1% | 79.1% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Valentin Vacherot (`KXATPMATCH-26OCT03VACFIL-VAC`) | 0.20 / 0.21 (49856) | 20.5% | -- | -- | -- [-----] | 23.8% | 21.1% | 21.1% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Marie Bouzkova / Ann Li vs Storm Hunter / Kristina Mladenovic -- WTA Beijing R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-04 06:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03BOUANNHUNMLA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marie Bouzkova / Ann Li (`KXWTADOUBLES-26OCT03BOUANNHUNMLA-BOUANN`) | 0.35 / 0.38 (1144) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Storm Hunter / Kristina Mladenovic (`KXWTADOUBLES-26OCT03BOUANNHUNMLA-HUNMLA`) | 0.62 / 0.64 (460) | 63.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Rinko Matsuda vs Sijia Wei -- WTA 125K Suzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 11:50Z
* Current expected start: 2026-10-04 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 05:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-03T11:50:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT03MATWEI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rinko Matsuda (`KXWTACHALLENGERMATCH-26OCT03MATWEI-MAT`) | 0.25 / 0.26 (13231) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sijia Wei (`KXWTACHALLENGERMATCH-26OCT03MATWEI-WEI`) | 0.74 / 0.75 (484) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE

## Priska Madelyn Nugroho vs Kyoka Okamura -- WTA 125K Suzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 08:00Z
* Current expected start: 2026-10-04 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 05:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-03T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT03NUGOKA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Priska Madelyn Nugroho (`KXWTACHALLENGERMATCH-26OCT03NUGOKA-NUG`) | 0.43 / 0.44 (482) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kyoka Okamura (`KXWTACHALLENGERMATCH-26OCT03NUGOKA-OKA`) | 0.55 / 0.56 (43) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE

## Daria Snigur vs Taylah Preston -- WTA Beijing R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-04 06:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT03SNIPRE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Taylah Preston (`KXWTAMATCH-26OCT03SNIPRE-PRE`) | 0.37 / 0.38 (24815) | 37.5% | -- | -- | -- [-----] | 38.4% | 37.1% | 37.7% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daria Snigur (`KXWTAMATCH-26OCT03SNIPRE-SNI`) | 0.62 / 0.63 (8700) | 62.5% | -- | -- | -- [-----] | 61.6% | 62.7% | 62.2% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE; WIDE_SPREAD

## Mattia Bellucci vs Lloyd Harris -- ATP Challenger Jingshan F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144750:208233:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mattia Bellucci (`KXATPCHALLENGERMATCH-26OCT03BELHAR-BEL`) | 0.53 / 0.54 (25253) | 53.5% | -- | 44.7% | 45.6% [43.7%-48.5%] | -- | 47.2% | 47.2% | MARKETS_AGREE | PASS | -7.9 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Lloyd Harris (`KXATPCHALLENGERMATCH-26OCT03BELHAR-HAR`) | 0.46 / 0.47 (35289) | 46.5% | -- | 55.3% | 54.4% [51.5%-56.3%] | -- | 52.9% | 52.9% | MARKETS_AGREE | PASS | +7.9 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 7020.0, B 4129.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0241
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Ekaterina Alexandrova / Fanny Stollar vs Cristina Bucsa / Nicole Melichar-Martinez -- WTA Beijing R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03ALESTOBUCMEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Alexandrova / Fanny Stollar (`KXWTADOUBLES-26OCT03ALESTOBUCMEL-ALESTO`) | 0.34 / 0.39 (242) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cristina Bucsa / Nicole Melichar-Martinez (`KXWTADOUBLES-26OCT03ALESTOBUCMEL-BUCMEL`) | 0.60 / 0.65 (326) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Shuko Aoyama / En-Shuo Liang vs Anna Danilina / Desirae Krawczyk -- WTA Beijing R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03AOYLIADANKRA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shuko Aoyama / En-Shuo Liang (`KXWTADOUBLES-26OCT03AOYLIADANKRA-AOYLIA`) | 0.40 / 0.46 (47) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anna Danilina / Desirae Krawczyk (`KXWTADOUBLES-26OCT03AOYLIADANKRA-DANKRA`) | 0.53 / 0.58 (1) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Hao-Ching Chan / Miyu (1994) Kato vs Tereza Mihalikova / Olivia Nicholls -- WTA Beijing R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03CHAKATMIHNIC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hao-Ching Chan / Miyu (1994) Kato (`KXWTADOUBLES-26OCT03CHAKATMIHNIC-CHAKAT`) | 0.41 / 0.48 (48) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tereza Mihalikova / Olivia Nicholls (`KXWTADOUBLES-26OCT03CHAKATMIHNIC-MIHNIC`) | 0.50 / 0.56 (1) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sara Errani / Jasmine Paolini vs Anastasia Detiuc / Fang-Hsien Wu -- WTA Beijing R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03ERRPAODETFAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasia Detiuc / Fang-Hsien Wu (`KXWTADOUBLES-26OCT03ERRPAODETFAN-DETFAN`) | 0.21 / 0.25 (17) | 23.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sara Errani / Jasmine Paolini (`KXWTADOUBLES-26OCT03ERRPAODETFAN-ERRPAO`) | 0.76 / 0.79 (767) | 77.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Su-Wei Hsieh / Jelena Ostapenko vs Xinyu Jiang / Xiyu Wang -- WTA Beijing R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03HSIOSTJIAWAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Su-Wei Hsieh / Jelena Ostapenko (`KXWTADOUBLES-26OCT03HSIOSTJIAWAN-HSIOST`) | 0.69 / 0.74 (674) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xinyu Jiang / Xiyu Wang (`KXWTADOUBLES-26OCT03HSIOSTJIAWAN-JIAWAN`) | 0.27 / 0.34 (30) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Irina Khromacheva / Liudmila Samsonova vs Jesika Maleckova / Miriam Skoch -- WTA Beijing R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03KHRSAMMALSKO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Irina Khromacheva / Liudmila Samsonova (`KXWTADOUBLES-26OCT03KHRSAMMALSKO-KHRSAM`) | 0.57 / 0.62 (45) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jesika Maleckova / Miriam Skoch (`KXWTADOUBLES-26OCT03KHRSAMMALSKO-MALSKO`) | 0.37 / 0.43 (44) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Caty McNally / Janice Tjen vs Nikola Bartunkova / Maja Chwalinska -- WTA Beijing R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03MCCTJEBARCHW:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikola Bartunkova / Maja Chwalinska (`KXWTADOUBLES-26OCT03MCCTJEBARCHW-BARCHW`) | 0.27 / 0.29 (157) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Caty McNally / Janice Tjen (`KXWTADOUBLES-26OCT03MCCTJEBARCHW-MCCTJE`) | 0.72 / 0.73 (9232) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Linda Noskova / Clara Tauson vs Ulrikke Eikeri / Quinn Gleason -- WTA Beijing R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03NOSTAUEIKGLE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ulrikke Eikeri / Quinn Gleason (`KXWTADOUBLES-26OCT03NOSTAUEIKGLE-EIKGLE`) | 0.42 / 0.47 (26) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Linda Noskova / Clara Tauson (`KXWTADOUBLES-26OCT03NOSTAUEIKGLE-NOSTAU`) | 0.53 / 0.57 (245) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Jelena Ostapenko vs Elise Mertens -- WTA Beijing R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT03OSTMER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elise Mertens (`KXWTAMATCH-26OCT03OSTMER-MER`) | 0.61 / 0.62 (3330) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jelena Ostapenko (`KXWTAMATCH-26OCT03OSTMER-OST`) | 0.38 / 0.39 (1506) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Erin Routliffe / Aldila Sutjiadi vs Ingrid Neel / Giuliana Olmos -- WTA Beijing R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03ROUSUTNEEOLM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ingrid Neel / Giuliana Olmos (`KXWTADOUBLES-26OCT03ROUSUTNEEOLM-NEEOLM`) | 0.37 / 0.40 (150) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Erin Routliffe / Aldila Sutjiadi (`KXWTADOUBLES-26OCT03ROUSUTNEEOLM-ROUSUT`) | 0.59 / 0.63 (754) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Maria Sakkari vs Elina Svitolina -- WTA Beijing R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT03SAKSVI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Sakkari (`KXWTAMATCH-26OCT03SAKSVI-SAK`) | 0.27 / 0.28 (6518) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Elina Svitolina (`KXWTAMATCH-26OCT03SAKSVI-SVI`) | 0.74 / 0.75 (3) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Katerina Siniakova / Shuai Zhang vs Shuo Feng / Yue Yuan -- WTA Beijing R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03SINZHAFENYUA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shuo Feng / Yue Yuan (`KXWTADOUBLES-26OCT03SINZHAFENYUA-FENYUA`) | 0.12 / 0.15 (2) | 13.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Katerina Siniakova / Shuai Zhang (`KXWTADOUBLES-26OCT03SINZHAFENYUA-SINZHA`) | 0.84 / 0.88 (501) | 86.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Donna Vekic vs Iga Swiatek -- WTA Beijing R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT03VEKSWI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iga Swiatek (`KXWTAMATCH-26OCT03VEKSWI-SWI`) | 0.90 / 0.91 (4839) | 90.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Donna Vekic (`KXWTAMATCH-26OCT03VEKSWI-VEK`) | 0.09 / 0.10 (9290) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Alex de Minaur vs Andrey Rublev -- ATP Beijing QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 06:00Z
* Current expected start: 2026-10-04 06:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 05:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+30_MIN

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT03DERUB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex de Minaur (`KXATPMATCH-26OCT03DERUB-DE`) | 0.53 / 0.54 (41929) | 53.5% | -- | -- | -- [-----] | 53.2% | 53.2% | 53.2% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Andrey Rublev (`KXATPMATCH-26OCT03DERUB-RUB`) | 0.47 / 0.48 (32076) | 47.5% | -- | -- | -- [-----] | 46.8% | 47.0% | 47.0% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Linda Noskova vs Viktorija Golubic -- WTA Beijing R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-04 06:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 05:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT03NOSGOL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Viktorija Golubic (`KXWTAMATCH-26OCT03NOSGOL-GOL`) | 0.12 / 0.13 (96979) | 12.5% | -- | -- | -- [-----] | 15.2% | 12.4% | 12.4% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Linda Noskova (`KXWTAMATCH-26OCT03NOSGOL-NOS`) | 0.87 / 0.88 (28170) | 87.5% | -- | -- | -- [-----] | 84.8% | 87.4% | 87.4% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD

## Siddhant Banthia vs Yusuke Takahashi -- ATP Challenger Wuning 3 Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-04T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126208:207996:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Siddhant Banthia (`KXATPCHALLENGERMATCH-26OCT04BANTAK-BAN`) | 0.11 / 0.14 (2) | 12.5% | -- | 17.4% | 18.5% [15.8%-20.7%] | -- | 15.4% | -- | INSUFFICIENT_INPUTS | WATCH | +6.0 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yusuke Takahashi (`KXATPCHALLENGERMATCH-26OCT04BANTAK-TAK`) | 0.86 / 0.88 (38) | 87.0% | -- | 82.6% | 81.5% [79.3%-84.2%] | -- | 84.7% | -- | INSUFFICIENT_INPUTS | PASS | -5.5 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 790.0, B 4325.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0246
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.007, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Max Purcell vs Julien de Cuyper -- ATP Challenger Wuning 3 Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-04T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126845:207761:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julien de Cuyper (`KXATPCHALLENGERMATCH-26OCT04PURDE-DE`) | 0.05 / 0.07 (5051) | 6.0% | -- | 6.9% | 2.9% [2.2%-3.5%] | -- | 6.0% | -- | INSUFFICIENT_INPUTS | PASS | -3.1 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Max Purcell (`KXATPCHALLENGERMATCH-26OCT04PURDE-PUR`) | 0.93 / 0.95 (3060) | 94.0% | -- | 93.1% | 97.1% [96.5%-97.8%] | -- | 93.7% | -- | INSUFFICIENT_INPUTS | WATCH | +3.1 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1721.0, B 542.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0068
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.005, surface_dev_loose +0.002, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; STALE_QUOTE

## Jumpei Yamasaki vs Martin Borisiouk -- ATP Challenger Wuning 3 Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-04T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126135:200456:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martin Borisiouk (`KXATPCHALLENGERMATCH-26OCT04YAMBOR-BOR`) | 0.73 / 0.74 (1072) | 73.5% | -- | 52.5% | 54.0% [52.0%-57.0%] | -- | 72.5% | 72.5% | MODEL_LONE_OUTLIER | PASS | -19.5 pp | HIGH_REVIEW | STALE | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Jumpei Yamasaki (`KXATPCHALLENGERMATCH-26OCT04YAMBOR-YAM`) | 0.26 / 0.27 (24039) | 26.5% | -- | 47.5% | 46.0% [43.0%-48.0%] | -- | 27.7% | 27.7% | MODEL_LONE_OUTLIER | WATCH | +19.5 pp | HIGH_REVIEW | STALE | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1700.0, B 869.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0249
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT04YAMBOR-YAM  (YES = Jumpei Yamasaki)
Model: 46%
Kalshi: 26%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: B (LIMITED)
Reasons: STALE_KALSHI_QUOTE, THIN_PLAYER_HISTORY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.020, surface_dev_loose -0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Mirra Andreeva / Anna Kalinskaya vs Maya Joint / Andreja Klepac -- WTA Beijing R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-04 07:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 06:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03ANDKALJOIKLE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mirra Andreeva / Anna Kalinskaya (`KXWTADOUBLES-26OCT03ANDKALJOIKLE-ANDKAL`) | 0.66 / 0.67 (1152) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maya Joint / Andreja Klepac (`KXWTADOUBLES-26OCT03ANDKALJOIKLE-JOIKLE`) | 0.33 / 0.35 (186) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Elise Mertens / Diana Shnaider vs Maia Lumsden / Alexandra Panova -- WTA Beijing R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-04 07:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 06:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03MERSHNLUMPAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maia Lumsden / Alexandra Panova (`KXWTADOUBLES-26OCT03MERSHNLUMPAN-LUMPAN`) | 0.24 / 0.26 (962) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Elise Mertens / Diana Shnaider (`KXWTADOUBLES-26OCT03MERSHNLUMPAN-MERSHN`) | 0.74 / 0.76 (5949) | 75.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Sander Arends / David Pel vs Alexander Bublik / Juncheng Shang -- ATP Beijing SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 06:00Z
* Current expected start: 2026-10-04 08:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 07:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03AREPELBUBSHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sander Arends / David Pel (`KXATPDOUBLES-26OCT03AREPELBUBSHA-AREPEL`) | 0.65 / 0.67 (958) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander Bublik / Juncheng Shang (`KXATPDOUBLES-26OCT03AREPELBUBSHA-BUBSHA`) | 0.33 / 0.34 (451) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Nino Ehrenschneider vs Isaac Becroft -- M15 Luan F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208653:209510:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isaac Becroft (`KXITFMATCH-26OCT03EHRBEC-BEC`) | 0.01 / 0.02 (1189) | 1.5% | -- | 38.9% | 40.3% [38.9%-41.3%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +38.8 pp | EXTREME (DATA_WARNING) | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nino Ehrenschneider (`KXITFMATCH-26OCT03EHRBEC-EHR`) | 0.97 / 0.98 (11499) | 97.5% | -- | 61.2% | 59.7% [58.7%-61.2%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -37.8 pp | EXTREME (DATA_WARNING) | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3879.0, B 1967.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0124
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT03EHRBEC-BEC  (YES = Isaac Becroft)
Model: 40%
Kalshi: 2%
Gap: +39 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.010, surface_dev_loose +0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jiri Lehecka vs Adolfo Daniel Vallejo -- ATP Tokyo QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 11:10Z
* Current expected start: 2026-10-04 08:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 07:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-04T11:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208103:209226:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jiri Lehecka (`KXATPMATCH-26OCT04LEHVAL-LEH`) | 0.71 / 0.72 (3032) | 71.5% | -- | 72.7% | 75.1% [73.6%-76.3%] | 71.8% | 71.2% | 71.5% | MODEL_LONE_OUTLIER | PASS | +3.6 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Adolfo Daniel Vallejo (`KXATPMATCH-26OCT04LEHVAL-VAL`) | 0.28 / 0.29 (33744) | 28.5% | -- | 27.3% | 24.9% [23.7%-26.5%] | 28.2% | 29.0% | 28.6% | MODEL_LONE_OUTLIER | PASS | -3.6 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5765.0, B 5913.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0139
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.008, surface_dev_loose +0.012, surface_dev_tight -0.016
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 4 carry a model probability
  * `KXATPEXACTMATCH-26OCT04LEHVAL-LEH20` Will Jiri Lehecka win the Jiri Lehecka vs Adolfo Daniel Vallejo match by a set score of 2-0?: 0.49/0.50 mid 49.5%, model 25.0% (market_conditioned_v1 (model4_board_v1)) -- gap -24.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT04LEHVAL-VAL21` Will Adolfo Daniel Vallejo win the Jiri Lehecka vs Adolfo Daniel Vallejo match by a set score of 2-1?: 0.12/0.13 mid 12.5%, model 25.0% (market_conditioned_v1 (model4_board_v1)) -- gap +12.5 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT04LEHVAL-VAL20` Will Adolfo Daniel Vallejo win the Jiri Lehecka vs Adolfo Daniel Vallejo match by a set score of 2-0?: 0.14/0.16 mid 15.0%, model 25.0% (market_conditioned_v1 (model4_board_v1)) -- gap +10.0 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT04LEHVAL-LEH21` Will Jiri Lehecka win the Jiri Lehecka vs Adolfo Daniel Vallejo match by a set score of 2-1?: 0.22/0.23 mid 22.5%, model 25.0% (market_conditioned_v1 (model4_board_v1)) -- gap +2.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: MODEL_ROW_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Daniil Medvedev vs Francisco Cerundolo -- ATP Beijing QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 11:30Z
* Current expected start: 2026-10-04 08:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 07:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-04T11:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT04MEDCER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisco Cerundolo (`KXATPMATCH-26OCT04MEDCER-CER`) | 0.29 / 0.30 (25391) | 29.5% | -- | -- | -- [-----] | 30.9% | 30.1% | 30.1% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daniil Medvedev (`KXATPMATCH-26OCT04MEDCER-MED`) | 0.71 / 0.72 (44263) | 71.5% | -- | -- | -- [-----] | 69.1% | 70.2% | 70.2% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD

## Ha Eum Lee vs Xi Luo -- W15 Maanshan F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 08:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264069:270449:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ha Eum Lee (`KXITFWMATCH-26OCT03LEELUO-LEE`) | 0.85 / 0.89 (643) | 87.0% | -- | 27.8% | 40.0% [34.4%-46.8%] | 57.0% | -- | 57.0% | MODEL_LONE_OUTLIER | PASS | -47.0 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Xi Luo (`KXITFWMATCH-26OCT03LEELUO-LUO`) | 0.11 / 0.14 (347) | 12.5% | -- | 72.2% | 60.0% [53.2%-65.6%] | 43.0% | -- | 43.0% | KALSHI_LONE_OUTLIER | PASS | +47.5 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 1048.0, B 827.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0619
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT03LEELUO-LUO  (YES = Xi Luo)
Model: 60%
Kalshi: 12%
Gap: +48 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: SUPPORTS_MODEL_DIRECTION
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.015, surface_dev_loose -0.030, surface_dev_tight +0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Noma Noha Akugue vs Ilay Yoruk -- WTA 125K Samsun Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 12:00Z
* Current expected start: 2026-10-04 09:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 08:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · Hard · scheduled 2026-10-04T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:215879:223333:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Noma Noha Akugue (`KXWTACHALLENGERMATCH-26OCT04NOHYOR-NOH`) | 0.92 / 0.93 (1872) | 92.5% | -- | 96.2% | 90.8% [83.9%-93.8%] | -- | 91.6% | -- | INSUFFICIENT_INPUTS | PASS | -1.6 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ilay Yoruk (`KXWTACHALLENGERMATCH-26OCT04NOHYOR-YOR`) | 0.06 / 0.07 (5523) | 6.5% | -- | 3.8% | 9.2% [6.2%-16.1%] | -- | 6.7% | -- | INSUFFICIENT_INPUTS | PASS | +2.6 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4975.0, B 1694.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0496
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.004, surface_dev_loose +0.012, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Egor Agafonov vs Maxim Zhukov -- ATP Challenger Wuning 3 Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-04T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208876:210393:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Egor Agafonov (`KXATPCHALLENGERMATCH-26OCT04AGAZHU-AGA`) | 0.42 / 0.43 (0) | 42.5% | -- | 39.2% | 41.2% [40.2%-42.8%] | -- | 44.8% | -- | INSUFFICIENT_INPUTS | PASS | -1.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maxim Zhukov (`KXATPCHALLENGERMATCH-26OCT04AGAZHU-ZHU`) | 0.58 / 0.59 (2326) | 58.5% | -- | 60.8% | 58.8% [57.2%-59.8%] | -- | 55.2% | -- | INSUFFICIENT_INPUTS | PASS | +0.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3266.0, B 2801.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0129
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Blake Bayldon vs Taisei Ichikawa -- ATP Challenger Wuning 3 Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-04T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207383:210471:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blake Bayldon (`KXATPCHALLENGERMATCH-26OCT04BAYICH-BAY`) | 0.13 / 0.14 (5411) | 13.5% | -- | 22.0% | 17.8% [16.4%-19.0%] | -- | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Taisei Ichikawa (`KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH`) | 0.86 / 0.87 (2479) | 86.5% | -- | 78.0% | 82.2% [81.0%-83.6%] | -- | 87.6% | -- | INSUFFICIENT_INPUTS | PASS | -4.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 357.0, B 3136.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0134
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.006, surface_dev_tight +0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE

## Keisuke Saitoh vs Zicong Wang -- ATP Challenger Wuning 3 Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-04T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04SAIWAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Keisuke Saitoh (`KXATPCHALLENGERMATCH-26OCT04SAIWAN-SAI`) | 0.96 / 0.97 (5591) | 96.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Zicong Wang (`KXATPCHALLENGERMATCH-26OCT04SAIWAN-WAN`) | 0.04 / 0.05 (4634) | 4.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Marcelo Melo / Alexander Zverev vs Julian Cash / Lloyd Glasspool -- ATP Beijing QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 06:00Z
* Current expected start: 2026-10-04 09:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 08:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-03T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT02MELZVECASGLA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julian Cash / Lloyd Glasspool (`KXATPDOUBLES-26OCT02MELZVECASGLA-CASGLA`) | 0.70 / 0.71 (479) | 70.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marcelo Melo / Alexander Zverev (`KXATPDOUBLES-26OCT02MELZVECASGLA-MELZVE`) | 0.29 / 0.30 (272) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Anastasia Tikhonova vs Mariia Tkacheva -- WTA 125K Samsun Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 13:30Z
* Current expected start: 2026-10-04 10:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 09:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-04T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT04TIKTKA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasia Tikhonova (`KXWTACHALLENGERMATCH-26OCT04TIKTKA-TIK`) | 0.60 / 0.61 (1894) | 60.5% | -- | -- | -- [-----] | 59.2% | 62.0% | 62.0% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mariia Tkacheva (`KXWTACHALLENGERMATCH-26OCT04TIKTKA-TKA`) | 0.39 / 0.41 (965) | 40.0% | -- | -- | -- [-----] | 40.8% | 39.6% | 39.6% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Alexander Zverev vs Novak Djokovic -- ATP Beijing QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 14:00Z
* Current expected start: 2026-10-04 11:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 10:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-04T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT04ZVEDJO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Novak Djokovic (`KXATPMATCH-26OCT04ZVEDJO-DJO`) | 0.29 / 0.30 (20347) | 29.5% | -- | -- | -- [-----] | 30.9% | 30.8% | 30.8% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander Zverev (`KXATPMATCH-26OCT04ZVEDJO-ZVE`) | 0.70 / 0.71 (51917) | 70.5% | -- | -- | -- [-----] | 69.1% | 69.5% | 69.3% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; STALE_QUOTE

## Sara Bejlek vs Naomi Osaka -- WTA Beijing R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-04 11:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 10:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT03BEJOSA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Bejlek (`KXWTAMATCH-26OCT03BEJOSA-BEJ`) | 0.26 / 0.27 (17761) | 26.5% | -- | -- | -- [-----] | 27.4% | 25.8% | 25.8% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Naomi Osaka (`KXWTAMATCH-26OCT03BEJOSA-OSA`) | 0.74 / 0.75 (56346) | 74.5% | -- | -- | -- [-----] | 72.6% | 73.8% | 73.8% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Fiona Crawley vs Alana Smith -- WTA 125K Samsun Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 14:00Z
* Current expected start: 2026-10-04 11:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 10:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-04T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT04CRASMI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fiona Crawley (`KXWTACHALLENGERMATCH-26OCT04CRASMI-CRA`) | 0.80 / 0.83 (4883) | 81.5% | -- | -- | -- [-----] | 79.2% | 81.0% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alana Smith (`KXWTACHALLENGERMATCH-26OCT04CRASMI-SMI`) | 0.17 / 0.20 (1400) | 18.5% | -- | -- | -- [-----] | 20.8% | 19.3% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Doga Turkmen vs Weronika Falkowska -- WTA 125K Samsun Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 14:00Z
* Current expected start: 2026-10-04 11:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 10:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-04T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT04TURFAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Weronika Falkowska (`KXWTACHALLENGERMATCH-26OCT04TURFAL-FAL`) | 0.96 / 0.97 (7810) | 96.5% | -- | -- | -- [-----] | 94.0% | 93.8% | 94.0% | KALSHI_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Doga Turkmen (`KXWTACHALLENGERMATCH-26OCT04TURFAL-TUR`) | 0.03 / 0.04 (6369) | 3.5% | -- | -- | -- [-----] | 6.0% | 3.4% | 4.7% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Gerard Campana Lee vs Pietro Marino -- ATP Challenger Palermo Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-04T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209233:210498:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gerard Campana Lee (`KXATPCHALLENGERMATCH-26OCT04CAMMAR-CAM`) | 0.84 / 0.85 (1787) | 84.5% | -- | 81.8% | 79.7% [76.1%-82.5%] | 81.2% | 83.7% | -- | INSUFFICIENT_INPUTS | PASS | -4.8 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pietro Marino (`KXATPCHALLENGERMATCH-26OCT04CAMMAR-MAR`) | 0.14 / 0.15 (2764) | 14.5% | -- | 18.2% | 20.3% [17.5%-23.9%] | 18.8% | 16.2% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +5.8 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4837.0, B 1738.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0322
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.007, surface_dev_loose +0.015, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Sebastiano Cocola vs Pedro Vives Marcos -- ATP Challenger Palermo Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-04T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206325:213717:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sebastiano Cocola (`KXATPCHALLENGERMATCH-26OCT04COCVIV-COC`) | 0.14 / 0.15 (2115) | 14.5% | -- | 4.9% | 8.2% [5.7%-10.8%] | 17.1% | 14.2% | -- | INSUFFICIENT_INPUTS | PASS | -6.3 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pedro Vives Marcos (`KXATPCHALLENGERMATCH-26OCT04COCVIV-VIV`) | 0.85 / 0.86 (3634) | 85.5% | -- | 95.1% | 91.8% [89.2%-94.3%] | 82.9% | 85.8% | -- | INSUFFICIENT_INPUTS | WATCH | +6.3 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1004.0, B 1642.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0254
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.008, surface_dev_loose -0.006, surface_dev_tight +0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Oscar Jose Gutierrez vs Yanaki Milev -- ATP Challenger Palermo Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-04T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:121264:210200:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oscar Jose Gutierrez (`KXATPCHALLENGERMATCH-26OCT04GUTMIL-GUT`) | 0.30 / 0.31 (2191) | 30.5% | -- | 39.7% | 39.7% [39.2%-40.7%] | 32.3% | 29.7% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +9.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yanaki Milev (`KXATPCHALLENGERMATCH-26OCT04GUTMIL-MIL`) | 0.68 / 0.70 (1500) | 69.0% | -- | 60.3% | 60.3% [59.3%-60.8%] | 67.7% | 70.1% | -- | INSUFFICIENT_INPUTS | PASS | -8.7 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2600.0, B 3208.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0077
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Yuta Kikuchi vs Kosuke Ogura -- ATP Challenger Wuning 3 Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-04T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202124:209043:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuta Kikuchi (`KXATPCHALLENGERMATCH-26OCT04KIKOGU-KIK`) | 0.41 / 0.42 (1733) | 41.5% | -- | 46.4% | 54.1% [51.0%-59.2%] | -- | 41.6% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +12.6 pp | REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kosuke Ogura (`KXATPCHALLENGERMATCH-26OCT04KIKOGU-OGU`) | 0.57 / 0.59 (3021) | 58.0% | -- | 53.6% | 45.9% [40.8%-49.0%] | -- | 58.2% | -- | INSUFFICIENT_INPUTS | PASS | -12.1 pp | REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2220.0, B 3515.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0408
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Ryuki Matsuda vs Sergey Betov -- ATP Challenger Wuning 3 Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-04T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105029:207987:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sergey Betov (`KXATPCHALLENGERMATCH-26OCT04MATBET-BET`) | 0.09 / 0.10 (4062) | 9.5% | -- | 21.6% | 47.9% [34.9%-60.6%] | -- | 9.7% | -- | INSUFFICIENT_INPUTS | WATCH | +38.5 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ryuki Matsuda (`KXATPCHALLENGERMATCH-26OCT04MATBET-MAT`) | 0.90 / 0.91 (2759) | 90.5% | -- | 78.4% | 52.0% [39.4%-65.0%] | -- | 90.4% | -- | INSUFFICIENT_INPUTS | PASS | -38.5 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3092.0, B 580.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1284
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT04MATBET-BET  (YES = Sergey Betov)
Model: 48%
Kalshi: 10%
Gap: +38 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.031, surface_pool_high +0.031, surface_dev_loose +0.015, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Ryan Seggerman vs Naoki Tajima -- ATP Challenger Wuning 3 Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-04T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202342:207248:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ryan Seggerman (`KXATPCHALLENGERMATCH-26OCT04SEGTAJ-SEG`) | 0.93 / 0.94 (14205) | 93.5% | -- | 76.8% | 82.5% [80.1%-85.5%] | -- | 90.8% | -- | INSUFFICIENT_INPUTS | PASS | -11.0 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Naoki Tajima (`KXATPCHALLENGERMATCH-26OCT04SEGTAJ-TAJ`) | 0.06 / 0.07 (969) | 6.5% | -- | 23.2% | 17.5% [14.5%-19.9%] | -- | 9.2% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +11.0 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2309.0, B 774.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0269
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.023, surface_dev_loose +0.006, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Casey Hoole vs Hayden Jones -- M25 Darwin F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210436:211315:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Casey Hoole (`KXITFMATCH-26OCT04HOOJON-HOO`) | 0.42 / 0.43 (1932) | 42.5% | -- | 63.0% | 63.5% [63.0%-64.1%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +21.0 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hayden Jones (`KXITFMATCH-26OCT04HOOJON-JON`) | 0.57 / 0.58 (2529) | 57.5% | -- | 37.0% | 36.5% [35.9%-37.0%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -21.0 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 187.0, B 1969.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0056
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT04HOOJON-HOO  (YES = Casey Hoole)
Model: 64%
Kalshi: 42%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Diego Dedura-Palomero vs Vadym Ursu -- ATP Challenger Villena Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-04T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:134068:212309:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diego Dedura-Palomero (`KXATPCHALLENGERMATCH-26OCT04DEDURS-DED`) | 0.75 / 0.76 (6382) | 75.5% | -- | 45.3% | 47.4% [45.3%-53.7%] | -- | 76.1% | -- | INSUFFICIENT_INPUTS | PASS | -28.1 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Vadym Ursu (`KXATPCHALLENGERMATCH-26OCT04DEDURS-URS`) | 0.23 / 0.24 (100) | 23.5% | -- | 54.7% | 52.6% [46.3%-54.7%] | -- | 24.1% | -- | INSUFFICIENT_INPUTS | WATCH | +29.1 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4501.0, B 4623.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0419
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT04DEDURS-URS  (YES = Vadym Ursu)
Model: 53%
Kalshi: 24%
Gap: +29 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.026, surface_pool_high -0.021, surface_dev_loose -0.021, surface_dev_tight +0.032
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Mathys Erhard vs Oliver Tarvet -- ATP Challenger Villena Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-04T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207231:210472:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mathys Erhard (`KXATPCHALLENGERMATCH-26OCT04ERHTAR-ERH`) | 0.22 / 0.23 (2943) | 22.5% | -- | 23.3% | 21.4% [18.6%-25.2%] | 25.7% | 22.9% | -- | INSUFFICIENT_INPUTS | PASS | -1.1 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oliver Tarvet (`KXATPCHALLENGERMATCH-26OCT04ERHTAR-TAR`) | 0.76 / 0.78 (1796) | 77.0% | -- | 76.7% | 78.6% [74.8%-81.4%] | 74.3% | 78.2% | -- | INSUFFICIENT_INPUTS | PASS | +1.6 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4744.0, B 1701.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0332
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.021, surface_dev_loose -0.006, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Tiago Esculcas vs Filip Misolic -- ATP Challenger Braga Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-04T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04ESCMIS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tiago Esculcas (`KXATPCHALLENGERMATCH-26OCT04ESCMIS-ESC`) | 0.05 / 0.06 (433) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Filip Misolic (`KXATPCHALLENGERMATCH-26OCT04ESCMIS-MIS`) | 0.91 / 0.95 (410) | 93.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE

## Sergi Fita Juan vs Georgii Kravchenko -- ATP Challenger Villena Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-04T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206662:211390:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sergi Fita Juan (`KXATPCHALLENGERMATCH-26OCT04FITKRA-FIT`) | 0.15 / 0.16 (9698) | 15.5% | -- | 14.4% | 18.2% [16.2%-19.6%] | 17.1% | 17.7% | 17.7% | KALSHI_LONE_OUTLIER | SHADOW_BET | +2.7 pp | NORMAL | STALE | B / LIMITED | EXTERNAL_STALE | VERIFIED |
| Georgii Kravchenko (`KXATPCHALLENGERMATCH-26OCT04FITKRA-KRA`) | 0.84 / 0.86 (9928) | 85.0% | -- | 85.6% | 81.8% [80.4%-83.8%] | 82.9% | 85.6% | -- | INSUFFICIENT_INPUTS | PASS | -3.2 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1712.0, B 3617.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0169
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.014, surface_dev_loose -0.013, surface_dev_tight +0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Juan Cruz Martin Manzano vs Samuele Pieri -- ATP Challenger Bari F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-04T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210129:212305:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Cruz Martin Manzano (`KXATPCHALLENGERMATCH-26OCT04MARPIE-MAR`) | 0.62 / 0.63 (5989) | 62.5% | -- | 33.2% | 37.1% [35.1%-39.1%] | 60.9% | 62.7% | -- | INSUFFICIENT_INPUTS | PASS | -25.4 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Samuele Pieri (`KXATPCHALLENGERMATCH-26OCT04MARPIE-PIE`) | 0.36 / 0.37 (1574) | 36.5% | -- | 66.8% | 62.9% [60.9%-64.9%] | 39.1% | 37.9% | -- | INSUFFICIENT_INPUTS | WATCH | +26.4 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3350.0, B 4011.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0202
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT04MARPIE-PIE  (YES = Samuele Pieri)
Model: 63%
Kalshi: 36%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose -0.005, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Johan Nikles vs Martim Bernardo -- ATP Challenger Braga Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-04T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04NIKBER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martim Bernardo (`KXATPCHALLENGERMATCH-26OCT04NIKBER-BER`) | 0.05 / 0.06 (821) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Johan Nikles (`KXATPCHALLENGERMATCH-26OCT04NIKBER-NIK`) | 0.94 / 0.95 (773) | 94.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE

## Guilherme Valdoleiros vs Vladyslav Orlov -- ATP Challenger Braga Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-04T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200550:207887:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vladyslav Orlov (`KXATPCHALLENGERMATCH-26OCT04VALORL-ORL`) | 0.94 / 0.95 (6321) | 94.5% | -- | 99.4% | 94.3% [89.3%-97.5%] | 90.5% | 90.8% | 90.5% | KALSHI_LONE_OUTLIER | WATCH | -0.2 pp | NORMAL | STALE | C / LIMITED | ALL_AGREE | VERIFIED |
| Guilherme Valdoleiros (`KXATPCHALLENGERMATCH-26OCT04VALORL-VAL`) | 0.05 / 0.06 (2331) | 5.5% | -- | 0.6% | 5.7% [2.5%-10.7%] | 9.5% | 6.9% | 9.5% | KALSHI_LONE_OUTLIER | PASS | +0.2 pp | NORMAL | STALE | C / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 735.0, B 3790.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.041
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.009, surface_dev_loose -0.009, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Maria Golovina vs Elena Micic -- WTA 125K Samsun Q1

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-04 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

WTA125 (WTA_125) · Hard · scheduled 2026-10-04T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:239397:261015:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Golovina (`KXWTACHALLENGERMATCH-26OCT04GOLMIC-GOL`) | 0.52 / 0.53 (2456) | 52.5% | -- | 72.5% | 62.5% [52.1%-67.9%] | 52.0% | 51.2% | -- | INSUFFICIENT_INPUTS | WATCH | +10.0 pp | REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elena Micic (`KXWTACHALLENGERMATCH-26OCT04GOLMIC-MIC`) | 0.46 / 0.47 (1954) | 46.5% | -- | 27.5% | 37.5% [32.1%-47.9%] | 48.0% | 48.6% | -- | INSUFFICIENT_INPUTS | PASS | -9.0 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2344.0, B 3357.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0789
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.015, surface_dev_tight -0.005
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Federico Arnaboldi vs Andrea de Marchi -- ATP Challenger Palermo Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 12:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-04T12:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206467:212972:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Federico Arnaboldi (`KXATPCHALLENGERMATCH-26OCT04ARNDE-ARN`) | 0.59 / 0.60 (1781) | 59.5% | -- | 72.0% | 80.9% [78.3%-83.7%] | 59.9% | 72.3% | 59.9% | MODEL_LONE_OUTLIER | WATCH | +21.4 pp | HIGH_REVIEW | STALE | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Andrea de Marchi (`KXATPCHALLENGERMATCH-26OCT04ARNDE-DE`) | 0.39 / 0.40 (100) | 39.5% | -- | 28.0% | 19.1% [16.3%-21.7%] | 40.1% | 34.0% | 40.1% | MODEL_LONE_OUTLIER | PASS | -20.4 pp | HIGH_REVIEW | STALE | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4215.0, B 1590.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0268
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT04ARNDE-ARN  (YES = Federico Arnaboldi)
Model: 81%
Kalshi: 60%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: B (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.004, surface_dev_loose +0.007, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Alex Marti Pujolras vs Filippo Moroni -- ATP Challenger Palermo Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 12:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-04T12:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207704:208092:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Marti Pujolras (`KXATPCHALLENGERMATCH-26OCT04MARMOR-MAR`) | 0.63 / 0.65 (583) | 64.0% | -- | 46.8% | 50.0% [47.9%-52.6%] | -- | 65.0% | -- | INSUFFICIENT_INPUTS | PASS | -14.0 pp | REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Filippo Moroni (`KXATPCHALLENGERMATCH-26OCT04MARMOR-MOR`) | 0.34 / 0.37 (807) | 35.5% | -- | 53.2% | 50.0% [47.3%-52.1%] | -- | 40.1% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +14.5 pp | REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3281.0, B 2040.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0239
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.011, surface_dev_loose +0.016, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Daniel Siniakov vs Daniele Rapagnetta -- ATP Challenger Palermo Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 12:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-04T12:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04SINRAP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniele Rapagnetta (`KXATPCHALLENGERMATCH-26OCT04SINRAP-RAP`) | 0.47 / 0.48 (375) | 47.5% | -- | -- | -- [-----] | 49.0% | 47.5% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daniel Siniakov (`KXATPCHALLENGERMATCH-26OCT04SINRAP-SIN`) | 0.50 / 0.52 (645) | 51.0% | -- | -- | -- [-----] | 51.0% | 52.3% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Karolina Muchova vs Liudmila Samsonova -- WTA Beijing R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-04 12:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 11:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT03MUCSAM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karolina Muchova (`KXWTAMATCH-26OCT03MUCSAM-MUC`) | 0.78 / 0.79 (45796) | 78.5% | -- | -- | -- [-----] | 75.5% | 77.0% | 77.0% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Liudmila Samsonova (`KXWTAMATCH-26OCT03MUCSAM-SAM`) | 0.21 / 0.22 (34593) | 21.5% | -- | -- | -- [-----] | 24.5% | 21.8% | 21.8% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alya Naz Altinel vs Mariam Bolkvadze -- WTA 125K Samsun Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 15:30Z
* Current expected start: 2026-10-04 12:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 11:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-04T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT04ALTBOL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alya Naz Altinel (`KXWTACHALLENGERMATCH-26OCT04ALTBOL-ALT`) | 0.07 / 0.87 (5) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mariam Bolkvadze (`KXWTACHALLENGERMATCH-26OCT04ALTBOL-BOL`) | 0.15 / 0.92 (5) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dalila Jakupovic vs Lucija Ciric-Bagaric -- WTA 125K Samsun Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 15:30Z
* Current expected start: 2026-10-04 12:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 11:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-04T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT04JAKCIR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucija Ciric-Bagaric (`KXWTACHALLENGERMATCH-26OCT04JAKCIR-CIR`) | 0.58 / 0.60 (2048) | 59.0% | -- | -- | -- [-----] | 58.4% | 62.0% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dalila Jakupovic (`KXWTACHALLENGERMATCH-26OCT04JAKCIR-JAK`) | 0.39 / 0.42 (3699) | 40.5% | -- | -- | -- [-----] | 41.6% | 38.9% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Caroline Werner vs Zhibek Kulambayeva -- WTA 125K Samsun Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 15:30Z
* Current expected start: 2026-10-04 12:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 11:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-04T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT04WERKUL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zhibek Kulambayeva (`KXWTACHALLENGERMATCH-26OCT04WERKUL-KUL`) | 0.31 / 0.33 (5867) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Caroline Werner (`KXWTACHALLENGERMATCH-26OCT04WERKUL-WER`) | 0.67 / 0.68 (2077) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Ilinca Dalina Amariei vs Alexia-Shara Iancu -- W50 Burgas R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221168:260262:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ilinca Dalina Amariei (`KXITFWMATCH-26OCT04AMAIAN-AMA`) | 0.93 / 0.95 (12) | 94.0% | -- | 81.8% | 87.5% [87.2%-88.0%] | -- | -- | -- | -- | PASS | -6.5 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexia-Shara Iancu (`KXITFWMATCH-26OCT04AMAIAN-IAN`) | 0.05 / 0.08 (11) | 6.5% | -- | 18.2% | 12.5% [12.0%-12.8%] | -- | -- | -- | -- | PASS | +6.0 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2360.0, B 74.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0041
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Raya Markova vs Maia Ilinca Burcescu -- W50 Burgas R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT04MARBUR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maia Ilinca Burcescu (`KXITFWMATCH-26OCT04MARBUR-BUR`) | 0.90 / 0.93 (48) | 91.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Raya Markova (`KXITFWMATCH-26OCT04MARBUR-MAR`) | 0.07 / 0.10 (3771) | 8.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yoana Moneva vs Beatris Spasova -- W50 Burgas R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221315:246492:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yoana Moneva (`KXITFWMATCH-26OCT04MONSPA-MON`) | 0.08 / 0.10 (14) | 9.0% | -- | 64.6% | 20.3% [17.5%-23.5%] | -- | -- | -- | -- | PASS | +11.3 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Beatris Spasova (`KXITFWMATCH-26OCT04MONSPA-SPA`) | 0.90 / 0.92 (117) | 91.0% | -- | 35.4% | 79.7% [76.5%-82.5%] | -- | -- | -- | -- | PASS | -11.3 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 180.0, B 520.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.03
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Paul Jubb vs Fares Zakaria -- M15 Sharm ElSheikh F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04JUBZAK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Paul Jubb (`KXITFMATCH-26OCT04JUBZAK-JUB`) | 0.82 / 0.83 (1169) | 82.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fares Zakaria (`KXITFMATCH-26OCT04JUBZAK-ZAK`) | 0.16 / 0.18 (4138) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Henrique Rocha vs Inaki Montes-de la Torre -- ATP Challenger Porto 2 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-04T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208540:210012:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Inaki Montes-de la Torre (`KXATPCHALLENGERMATCH-26OCT04ROCMON-MON`) | 0.32 / 0.33 (7724) | 32.5% | -- | 57.2% | 53.1% [47.9%-56.2%] | 33.6% | 31.1% | -- | INSUFFICIENT_INPUTS | WATCH | +20.6 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Henrique Rocha (`KXATPCHALLENGERMATCH-26OCT04ROCMON-ROC`) | 0.67 / 0.68 (5040) | 67.5% | -- | 42.8% | 46.9% [43.8%-52.1%] | 66.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.6 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5037.0, B 4378.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0413
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT04ROCMON-MON  (YES = Inaki Montes-de la Torre)
Model: 53%
Kalshi: 32%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Luisa Fusil vs Juliette Mazzoni -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220934:269936:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luisa Fusil (`KXITFWMATCH-26OCT04FUSMAZ-FUS`) | 0.67 / 0.68 (3211) | 67.5% | -- | 86.4% | 87.8% [87.1%-87.9%] | -- | -- | -- | -- | PASS | +20.3 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Juliette Mazzoni (`KXITFWMATCH-26OCT04FUSMAZ-MAZ`) | 0.32 / 0.36 (3239) | 34.0% | -- | 13.6% | 12.2% [12.1%-12.9%] | -- | -- | -- | -- | PASS | -21.8 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 206.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0041
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT04FUSMAZ-FUS  (YES = Luisa Fusil)
Model: 88%
Kalshi: 68%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.005, surface_dev_loose -0.001, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuliya Hatouka vs Antonina Sushkova -- W15 Sharm ElSheikh F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216013:266849:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuliya Hatouka (`KXITFWMATCH-26OCT04HATSUS-HAT`) | 0.55 / 0.58 (857) | 56.5% | -- | 77.8% | 85.2% [83.7%-87.6%] | -- | -- | -- | -- | PASS | +28.8 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Antonina Sushkova (`KXITFWMATCH-26OCT04HATSUS-SUS`) | 0.42 / 0.44 (3898) | 43.0% | -- | 22.2% | 14.8% [12.4%-16.4%] | -- | -- | -- | -- | PASS | -28.2 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2126.0, B 527.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0195
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT04HATSUS-HAT  (YES = Yuliya Hatouka)
Model: 85%
Kalshi: 56%
Gap: +29 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.006, surface_dev_loose -0.000, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anastasia Huijsegoms vs Natalia Fehr -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223064:264387:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Natalia Fehr (`KXITFWMATCH-26OCT04HUIFEH-FEH`) | 0.21 / 0.22 (3844) | 21.5% | -- | 17.7% | 22.6% [22.6%-23.4%] | -- | -- | -- | -- | PASS | +1.1 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Anastasia Huijsegoms (`KXITFWMATCH-26OCT04HUIFEH-HUI`) | 0.76 / 0.81 (1) | 78.5% | -- | 82.3% | 77.4% [76.6%-77.4%] | -- | -- | -- | -- | PASS | -1.1 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 203.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0042
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.008, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mio Kijima vs Cristina PESCUCCI -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223094:266471:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mio Kijima (`KXITFWMATCH-26OCT04KIJPES-KIJ`) | 0.07 / 0.08 (11) | 7.5% | -- | 64.6% | 40.5% [39.5%-42.6%] | -- | -- | -- | -- | PASS | +33.0 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Cristina PESCUCCI (`KXITFWMATCH-26OCT04KIJPES-PES`) | 0.92 / 0.93 (543) | 92.5% | -- | 35.4% | 59.5% [57.4%-60.5%] | -- | -- | -- | -- | PASS | -33.0 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 112.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0156
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT04KIJPES-KIJ  (YES = Mio Kijima)
Model: 40%
Kalshi: 8%
Gap: +33 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Styliani Roussopoulou vs Noa Krznaric Uygungul -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:257893:267381:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Noa Krznaric Uygungul (`KXITFWMATCH-26OCT04ROUKRZ-KRZ`) | 0.66 / 0.67 (3220) | 66.5% | -- | 67.1% | 69.5% [69.4%-70.4%] | -- | -- | -- | -- | PASS | +3.0 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Styliani Roussopoulou (`KXITFWMATCH-26OCT04ROUKRZ-ROU`) | 0.33 / 0.35 (1) | 34.0% | -- | 32.9% | 30.5% [29.6%-30.6%] | -- | -- | -- | -- | PASS | -3.5 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 185.0, B 0.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0048
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sonja Zhenikhova vs Giulia Safina Popa -- W15 Varna F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-04T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264961:267428:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giulia Safina Popa (`KXITFWMATCH-26OCT04ZHEPOP-POP`) | 0.71 / 0.72 (6988) | 71.5% | -- | 75.8% | 72.3% [67.6%-74.5%] | 68.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sonja Zhenikhova (`KXITFWMATCH-26OCT04ZHEPOP-ZHE`) | 0.29 / 0.30 (1485) | 29.5% | -- | 24.2% | 27.7% [25.5%-32.4%] | 31.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1212.0, B 1013.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0346
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high +0.000, surface_dev_loose -0.018, surface_dev_tight +0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tiago Cacao vs Milos Karol -- ATP Challenger Braga Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 13:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-04T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132310:209984:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tiago Cacao (`KXATPCHALLENGERMATCH-26OCT04CACKAR-CAC`) | 0.40 / 0.41 (5480) | 40.5% | -- | 39.1% | 35.8% [32.0%-39.1%] | 40.8% | 37.7% | -- | INSUFFICIENT_INPUTS | PASS | -4.8 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Milos Karol (`KXATPCHALLENGERMATCH-26OCT04CACKAR-KAR`) | 0.59 / 0.60 (3323) | 59.5% | -- | 60.9% | 64.2% [60.9%-68.0%] | 59.2% | 59.5% | -- | INSUFFICIENT_INPUTS | PASS | +4.8 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1518.0, B 4285.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0352
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.033, surface_dev_loose +0.004, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Hugo Grenier vs Bruno Pujol Navarro -- ATP Challenger Villena Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 13:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-04T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04GREPUJ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Grenier (`KXATPCHALLENGERMATCH-26OCT04GREPUJ-GRE`) | 0.91 / 0.92 (2272) | 91.5% | -- | -- | -- [-----] | 88.2% | 89.1% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bruno Pujol Navarro (`KXATPCHALLENGERMATCH-26OCT04GREPUJ-PUJ`) | 0.08 / 0.09 (1568) | 8.5% | -- | -- | -- [-----] | 11.8% | 9.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Patrick Schoen vs Alberto Barroso Campos -- ATP Challenger Braga Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 13:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-04T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132744:211566:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alberto Barroso Campos (`KXATPCHALLENGERMATCH-26OCT04SCHBAR-BAR`) | 0.26 / 0.28 (4687) | 27.0% | -- | 20.6% | 23.6% [19.5%-30.4%] | 26.9% | 25.8% | 26.9% | MARKETS_AGREE | PASS | -3.4 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Patrick Schoen (`KXATPCHALLENGERMATCH-26OCT04SCHBAR-SCH`) | 0.73 / 0.74 (6505) | 73.5% | -- | 79.4% | 76.4% [69.6%-80.5%] | 73.1% | 79.2% | 73.1% | MODEL_LONE_OUTLIER | PASS | +2.9 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 1754.0, B 3451.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0547
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.024, surface_pool_high +0.012, surface_dev_loose +0.000, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Dominic Stricker vs Enrique Carrascosa Diaz -- ATP Challenger Villena Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 13:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-04T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208502:213766:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Enrique Carrascosa Diaz (`KXATPCHALLENGERMATCH-26OCT04STRCAR-CAR`) | 0.03 / 0.04 (1677) | 3.5% | -- | 6.3% | 7.0% [5.8%-8.4%] | -- | 50.9% | 50.9% | KALSHI_LONE_OUTLIER | PASS | +3.5 pp | NORMAL | STALE | D / POOR | EXTERNAL_OUTLIER | VERIFIED |
| Dominic Stricker (`KXATPCHALLENGERMATCH-26OCT04STRCAR-STR`) | 0.96 / 0.97 (5622) | 96.5% | -- | 93.7% | 93.0% [91.6%-94.2%] | -- | 95.8% | -- | INSUFFICIENT_INPUTS | PASS | -3.5 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3840.0, B 922.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0135
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.015, surface_dev_loose +0.006, surface_dev_tight -0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Olle Wallin vs Pedro Rodenas -- ATP Challenger Braga Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 13:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-04T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209167:210203:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pedro Rodenas (`KXATPCHALLENGERMATCH-26OCT04WALROD-ROD`) | 0.38 / 0.39 (1208) | 38.5% | -- | 63.6% | 59.2% [51.5%-62.7%] | 40.1% | 40.5% | 40.3% | MODEL_LONE_OUTLIER | WATCH | +20.7 pp | HIGH_REVIEW | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Olle Wallin (`KXATPCHALLENGERMATCH-26OCT04WALROD-WAL`) | 0.61 / 0.62 (8007) | 61.5% | -- | 36.4% | 40.8% [37.3%-48.5%] | 59.9% | 67.4% | 59.9% | MODEL_LONE_OUTLIER | PASS | -20.7 pp | HIGH_REVIEW | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3463.0, B 1623.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0557
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT04WALROD-ROD  (YES = Pedro Rodenas)
Model: 59%
Kalshi: 38%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.015, surface_dev_loose -0.015, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Robert Guna vs Dimitris Sakellaridis -- ATP Challenger Palermo Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 13:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-04T13:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211491:212029:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robert Guna (`KXATPCHALLENGERMATCH-26OCT04GUNSAK-GUN`) | 0.47 / 0.48 (4427) | 47.5% | -- | 52.1% | 52.1% [52.1%-53.6%] | 45.9% | 48.6% | 45.9% | MODEL_LONE_OUTLIER | WATCH | +4.6 pp | NORMAL | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Dimitris Sakellaridis (`KXATPCHALLENGERMATCH-26OCT04GUNSAK-SAK`) | 0.52 / 0.54 (692) | 53.0% | -- | 47.9% | 47.9% [46.4%-47.9%] | 54.1% | 51.2% | 54.1% | MODEL_LONE_OUTLIER | PASS | -5.1 pp | NORMAL | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1268.0, B 4537.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0078
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.015, surface_dev_loose +0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; STALE_QUOTE

## Kalin Ivanovski vs Giuseppe La Vela -- ATP Challenger Palermo Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 13:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-04T13:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208153:209928:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kalin Ivanovski (`KXATPCHALLENGERMATCH-26OCT04IVALA-IVA`) | 0.56 / 0.58 (695) | 57.0% | -- | 67.9% | 64.2% [56.0%-66.0%] | 56.3% | 56.5% | -- | INSUFFICIENT_INPUTS | PASS | +7.2 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Giuseppe La Vela (`KXATPCHALLENGERMATCH-26OCT04IVALA-LA`) | 0.42 / 0.43 (2192) | 42.5% | -- | 32.1% | 35.8% [34.0%-44.0%] | 43.7% | 43.5% | -- | INSUFFICIENT_INPUTS | PASS | -6.7 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2742.0, B 2999.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0502
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.019, surface_dev_loose +0.014, surface_dev_tight -0.024
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Ignacio Parisca Romera vs Gabriel Ghetu -- ATP Challenger Palermo Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 13:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-04T13:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212244:212306:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriel Ghetu (`KXATPCHALLENGERMATCH-26OCT04PARGHE-GHE`) | 0.55 / 0.57 (1951) | 56.0% | -- | 44.7% | 51.1% [48.4%-58.8%] | 55.4% | 57.1% | -- | INSUFFICIENT_INPUTS | PASS | -4.9 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Ignacio Parisca Romera (`KXATPCHALLENGERMATCH-26OCT04PARGHE-PAR`) | 0.42 / 0.43 (1624) | 42.5% | -- | 55.3% | 48.9% [41.2%-51.6%] | 44.6% | 43.0% | -- | INSUFFICIENT_INPUTS | PASS | +6.4 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 2357.0, B 1953.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0522
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.011, surface_dev_loose +0.011, surface_dev_tight -0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Ana Lungu vs Darya Velikova -- W50 Burgas R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 13:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT04LUNVEL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ana Lungu (`KXITFWMATCH-26OCT04LUNVEL-LUN`) | 0.06 / 0.09 (3121) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Darya Velikova (`KXITFWMATCH-26OCT04LUNVEL-VEL`) | 0.91 / 0.94 (1262) | 92.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lucie Petruzelova vs Monika Gospodinova -- W50 Burgas R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 13:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT04PETGOS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Monika Gospodinova (`KXITFWMATCH-26OCT04PETGOS-GOS`) | 0.06 / 0.07 (91) | 6.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucie Petruzelova (`KXITFWMATCH-26OCT04PETGOS-PET`) | 0.91 / 0.95 (310) | 93.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sarah Van Emst vs Milana Konovalova -- W50 Burgas R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 13:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260647:266664:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Milana Konovalova (`KXITFWMATCH-26OCT04VANKON-KON`) | 0.07 / 0.08 (4) | 7.5% | -- | 25.3% | 16.9% [16.2%-16.9%] | -- | -- | -- | -- | PASS | +9.4 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sarah Van Emst (`KXITFWMATCH-26OCT04VANKON-VAN`) | 0.91 / 0.93 (603) | 92.0% | -- | 74.7% | 83.1% [83.1%-83.8%] | -- | -- | -- | -- | PASS | -8.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2135.0, B 31.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0035
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chetanna Amadike vs Gedeo Murinzi -- M25 Kigali R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04AMAMUR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chetanna Amadike (`KXITFMATCH-26OCT04AMAMUR-AMA`) | 0.91 / 0.94 (56) | 92.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gedeo Murinzi (`KXITFMATCH-26OCT04AMAMUR-MUR`) | 0.06 / 0.10 (116) | 8.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Fred Barry Nimubona vs George Gregoriou -- M25 Kigali R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04NIMGRE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| George Gregoriou (`KXITFMATCH-26OCT04NIMGRE-GRE`) | 0.51 / 0.93 (215) | 72.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fred Barry Nimubona (`KXITFMATCH-26OCT04NIMGRE-NIM`) | 0.05 / 0.73 (67) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Edison Edison Nshimiyimana vs AARYA JADHAV -- M25 Kigali R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04NSHJAD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AARYA JADHAV (`KXITFMATCH-26OCT04NSHJAD-JAD`) | 0.07 / 0.90 (5) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Edison Edison Nshimiyimana (`KXITFMATCH-26OCT04NSHJAD-NSH`) | 0.06 / 0.89 (0) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lenny Petit vs Manzi rwamucyo David -- M25 Kigali R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-04T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212897:214200:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Manzi rwamucyo David (`KXITFMATCH-26OCT04PETDAV-DAV`) | 0.05 / 0.52 (1) | 28.5% | -- | 40.8% | 59.2% [57.2%-60.2%] | -- | -- | -- | -- | PASS | +30.7 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lenny Petit (`KXITFMATCH-26OCT04PETDAV-PET`) | 0.51 / 0.94 (0) | 72.5% | -- | 59.2% | 40.8% [39.8%-42.8%] | -- | -- | -- | -- | PASS | -31.7 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 112.0, B 92.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.015
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT04PETDAV-DAV  (YES = Manzi rwamucyo David)
Model: 59%
Kalshi: 28%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Niels Visker vs Marko ToPo -- ATP Challenger Villena Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-04T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208253:209916:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marko ToPo (`KXATPCHALLENGERMATCH-26OCT04VISTOP-TOP`) | 0.56 / 0.57 (4339) | 56.5% | -- | 50.9% | 53.2% [52.3%-55.7%] | 57.2% | 56.2% | -- | INSUFFICIENT_INPUTS | PASS | -3.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Niels Visker (`KXATPCHALLENGERMATCH-26OCT04VISTOP-VIS`) | 0.41 / 0.44 (1542) | 42.5% | -- | 49.1% | 46.8% [44.3%-47.7%] | 42.8% | 43.3% | -- | INSUFFICIENT_INPUTS | WATCH | +4.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3470.0, B 3971.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0168
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Liv Boulard vs Maxine Sophie Kammerer -- W35 Villeneuve d'Ascq R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:236991:260185:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liv Boulard (`KXITFWMATCH-26OCT04BOUKAM-BOU`) | 0.20 / 0.95 (308) | 57.5% | -- | 33.5% | 60.5% [59.5%-61.6%] | -- | -- | -- | -- | PASS | +3.0 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Maxine Sophie Kammerer (`KXITFWMATCH-26OCT04BOUKAM-KAM`) | 0.05 / 0.08 (22) | 6.5% | -- | 66.5% | 39.5% [38.4%-40.5%] | -- | -- | -- | -- | PASS | +33.0 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 476.0, B 0.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0104
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT04BOUKAM-KAM  (YES = Maxine Sophie Kammerer)
Model: 39%
Kalshi: 6%
Gap: +33 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, PLAYER_IDENTITY_RISK, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anna Burchak vs Malkia Ngounoue -- W35 Villeneuve d'Ascq R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT04BURNGO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Burchak (`KXITFWMATCH-26OCT04BURNGO-BUR`) | 0.14 / 0.15 (139) | 14.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Malkia Ngounoue (`KXITFWMATCH-26OCT04BURNGO-NGO`) | 0.83 / 0.86 (45) | 84.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stella Jurina vs Sapir Cohen -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223062:252593:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sapir Cohen (`KXITFWMATCH-26OCT04JURCOH-COH`) | 0.09 / 0.14 (884) | 11.5% | -- | 22.7% | 39.5% [38.4%-39.5%] | -- | -- | -- | -- | PASS | +28.0 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Stella Jurina (`KXITFWMATCH-26OCT04JURCOH-JUR`) | 0.85 / 0.89 (3171) | 87.0% | -- | 77.3% | 60.5% [60.5%-61.6%] | -- | -- | -- | -- | PASS | -26.5 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 133.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0051
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT04JURCOH-COH  (YES = Sapir Cohen)
Model: 39%
Kalshi: 12%
Gap: +28 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Janika Kusy vs Maria Rentoumi -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259886:270259:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Janika Kusy (`KXITFWMATCH-26OCT04KUSREN-KUS`) | 0.32 / 0.37 (3172) | 34.5% | -- | 52.1% | 26.0% [24.3%-27.3%] | -- | -- | -- | -- | PASS | -8.5 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Rentoumi (`KXITFWMATCH-26OCT04KUSREN-REN`) | 0.63 / 0.68 (3856) | 65.5% | -- | 47.9% | 74.0% [72.7%-75.7%] | -- | -- | -- | -- | PASS | +8.5 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 70.0, B 149.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0149
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sarah Leroy vs Hanna Bougouffa -- W35 Villeneuve d'Ascq R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT04LERBOU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hanna Bougouffa (`KXITFWMATCH-26OCT04LERBOU-BOU`) | 0.90 / 0.94 (232) | 92.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sarah Leroy (`KXITFWMATCH-26OCT04LERBOU-LER`) | 0.06 / 0.10 (3812) | 8.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Polina Maneshina vs Keira Blackbeard -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT04MANBLA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Keira Blackbeard (`KXITFWMATCH-26OCT04MANBLA-BLA`) | 0.28 / 0.95 (164) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Polina Maneshina (`KXITFWMATCH-26OCT04MANBLA-MAN`) | 0.05 / 0.72 (606) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zejda Veljacic vs Karyna Fiadosik -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216070:269703:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karyna Fiadosik (`KXITFWMATCH-26OCT04VELFIA-FIA`) | 0.24 / 0.25 (161) | 24.5% | -- | 27.0% | 31.5% [31.5%-31.6%] | -- | -- | -- | -- | PASS | +7.0 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Zejda Veljacic (`KXITFWMATCH-26OCT04VELFIA-VEL`) | 0.70 / 0.75 (3907) | 72.5% | -- | 73.0% | 68.5% [68.5%-68.5%] | -- | -- | -- | -- | PASS | -4.0 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 44.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0001
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Charles Chen vs Pyotr Nesterov -- ATP Challenger Villena Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 14:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-04T14:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04CHENES:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charles Chen (`KXATPCHALLENGERMATCH-26OCT04CHENES-CHE`) | 0.06 / 0.07 (1684) | 6.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pyotr Nesterov (`KXATPCHALLENGERMATCH-26OCT04CHENES-NES`) | 0.92 / 0.94 (25171) | 93.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Philip Henning vs Thijs Boogaard -- ATP Challenger Villena Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 14:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-04T14:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202475:212275:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thijs Boogaard (`KXATPCHALLENGERMATCH-26OCT04HENBOO-BOO`) | 0.32 / 0.33 (5190) | 32.5% | -- | 27.3% | 25.6% [24.8%-26.9%] | 33.6% | 35.3% | 35.3% | EXTERNAL_LONE_OUTLIER | PASS | -6.9 pp | NORMAL | STALE | B / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Philip Henning (`KXATPCHALLENGERMATCH-26OCT04HENBOO-HEN`) | 0.66 / 0.67 (1514) | 66.5% | -- | 72.7% | 74.4% [73.1%-75.2%] | 66.4% | 65.8% | 65.8% | MODEL_LONE_OUTLIER | SHADOW_BET | +7.9 pp | NORMAL | STALE | B / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4250.0, B 1603.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0104
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.008, surface_dev_loose +0.001, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Fabrizio Andaloro vs Matyas Cerny -- ATP Challenger Palermo Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-04T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208257:210063:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fabrizio Andaloro (`KXATPCHALLENGERMATCH-26OCT04ANDCER-AND`) | 0.44 / 0.45 (2487) | 44.5% | -- | 27.7% | 34.2% [28.5%-47.9%] | 45.9% | 48.2% | 48.2% | KALSHI_LONE_OUTLIER | PASS | -10.3 pp | REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Matyas Cerny (`KXATPCHALLENGERMATCH-26OCT04ANDCER-CER`) | 0.54 / 0.55 (32) | 54.5% | -- | 72.3% | 65.8% [52.1%-71.5%] | 54.1% | 55.8% | -- | INSUFFICIENT_INPUTS | WATCH | +11.3 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2640.0, B 2034.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0968
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.049, surface_pool_high -0.047, surface_dev_loose -0.033, surface_dev_tight +0.030
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Christian Langmo vs Dominik Recek -- ATP Challenger Palermo Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-04T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:127087:132052:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Christian Langmo (`KXATPCHALLENGERMATCH-26OCT04LANREC-LAN`) | 0.46 / 0.48 (713) | 47.0% | -- | 55.0% | 57.9% [55.0%-62.3%] | 48.0% | 48.1% | 48.1% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.9 pp | REVIEW | STALE | B / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Dominik Recek (`KXATPCHALLENGERMATCH-26OCT04LANREC-REC`) | 0.52 / 0.54 (4238) | 53.0% | -- | 45.0% | 42.1% [37.8%-45.0%] | 52.0% | 60.0% | -- | INSUFFICIENT_INPUTS | PASS | -10.9 pp | REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4895.0, B 1329.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0365
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.020, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Oleksandr Ovcharenko vs Lorenzo Angelini -- ATP Challenger Palermo Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-04T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:149117:209191:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Angelini (`KXATPCHALLENGERMATCH-26OCT04OVCANG-ANG`) | 0.34 / 0.35 (2064) | 34.5% | -- | 28.2% | 27.4% [26.0%-29.7%] | 36.2% | 33.8% | -- | INSUFFICIENT_INPUTS | PASS | -7.1 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oleksandr Ovcharenko (`KXATPCHALLENGERMATCH-26OCT04OVCANG-OVC`) | 0.65 / 0.66 (697) | 65.5% | -- | 71.8% | 72.6% [70.3%-74.0%] | 63.8% | 66.2% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +7.1 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2396.0, B 2551.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0185
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose +0.009, surface_dev_tight -0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Leolia Jeanjean vs Lois Boisson -- WTA 125K Adana F

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 18:00Z
* Current expected start: 2026-10-04 15:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: 2026-10-04 14:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-04T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT04JEABOI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lois Boisson (`KXWTACHALLENGERMATCH-26OCT04JEABOI-BOI`) | 0.67 / 0.68 (174) | 67.5% | -- | -- | -- [-----] | 67.1% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leolia Jeanjean (`KXWTACHALLENGERMATCH-26OCT04JEABOI-JEA`) | 0.31 / 0.33 (2034) | 32.0% | -- | -- | -- [-----] | 32.9% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Lawrence Bataljin vs Harel Tarshish -- M25 Kigali R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04BATTAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lawrence Bataljin (`KXITFMATCH-26OCT04BATTAR-BAT`) | 0.91 / 0.95 (528) | 93.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Harel Tarshish (`KXITFMATCH-26OCT04BATTAR-TAR`) | 0.06 / 0.07 (26) | 6.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rafael Izquierdo Luque vs Benjamin Hassan -- ATP Challenger Braga Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-04T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133975:202258:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benjamin Hassan (`KXATPCHALLENGERMATCH-26OCT04IZQHAS-HAS`) | 0.80 / 0.82 (4365) | 81.0% | -- | 59.7% | 72.2% [67.8%-79.7%] | 78.7% | 80.7% | -- | INSUFFICIENT_INPUTS | PASS | -8.8 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rafael Izquierdo Luque (`KXATPCHALLENGERMATCH-26OCT04IZQHAS-IZQ`) | 0.18 / 0.20 (608) | 19.0% | -- | 40.4% | 27.8% [20.3%-32.2%] | 21.3% | 19.2% | -- | INSUFFICIENT_INPUTS | PASS | +8.8 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2063.0, B 5302.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0593
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.000, surface_dev_loose -0.009, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Ollie Knight vs Yash Chaurasia -- M25 Kigali R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04KNICHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yash Chaurasia (`KXITFMATCH-26OCT04KNICHA-CHA`) | 0.36 / 0.79 (0) | 57.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ollie Knight (`KXITFMATCH-26OCT04KNICHA-KNI`) | 0.05 / 0.33 (37) | 19.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hugo Maia vs Javier Barranco Cosano -- ATP Challenger Braga Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-04T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200266:206669:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Javier Barranco Cosano (`KXATPCHALLENGERMATCH-26OCT04MAIBAR-BAR`) | 0.94 / 0.95 (262) | 94.5% | -- | 94.5% | 92.3% [90.3%-94.3%] | 92.7% | 92.9% | -- | INSUFFICIENT_INPUTS | PASS | -2.1 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hugo Maia (`KXATPCHALLENGERMATCH-26OCT04MAIBAR-MAI`) | 0.05 / 0.06 (6729) | 5.5% | -- | 5.5% | 7.6% [5.7%-9.7%] | 7.3% | 6.0% | -- | INSUFFICIENT_INPUTS | WATCH | +2.1 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 991.0, B 3597.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0199
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.006, surface_dev_loose -0.011, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Nikita Mashtakov vs Noah Lopez -- M15 Sibenik F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04MASLOP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Noah Lopez (`KXITFMATCH-26OCT04MASLOP-LOP`) | 0.22 / 0.24 (13) | 23.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nikita Mashtakov (`KXITFMATCH-26OCT04MASLOP-MAS`) | 0.76 / 0.78 (24) | 77.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ryan Nijboer vs Nico Hipfl -- ATP Challenger Braga Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-04T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207764:211503:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nico Hipfl (`KXATPCHALLENGERMATCH-26OCT04NIJHIP-HIP`) | 0.23 / 0.24 (1315) | 23.5% | -- | 57.1% | 40.0% [34.2%-44.9%] | 25.7% | 22.7% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +16.5 pp | HIGH_REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ryan Nijboer (`KXATPCHALLENGERMATCH-26OCT04NIJHIP-NIJ`) | 0.75 / 0.77 (7837) | 76.0% | -- | 42.9% | 60.0% [55.1%-65.8%] | 74.3% | 77.3% | -- | INSUFFICIENT_INPUTS | PASS | -16.0 pp | HIGH_REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4005.0, B 1320.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0537
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT04NIJHIP-HIP  (YES = Nico Hipfl)
Model: 40%
Kalshi: 24%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.029, surface_dev_loose +0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Darrshan Suresh vs Rahul Lokesh -- M25 Kigali R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-04T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207559:214552:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rahul Lokesh (`KXITFMATCH-26OCT04SURLOK-LOK`) | 0.05 / 0.08 (106) | 6.5% | -- | 74.8% | 75.6% [75.6%-75.6%] | -- | -- | -- | -- | PASS | +69.1 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Darrshan Suresh (`KXITFMATCH-26OCT04SURLOK-SUR`) | 0.93 / 0.94 (68) | 93.5% | -- | 25.2% | 24.4% [24.3%-24.4%] | -- | -- | -- | -- | PASS | -69.1 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 639.0, B 34.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0004
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT04SURLOK-LOK  (YES = Rahul Lokesh)
Model: 76%
Kalshi: 6%
Gap: +69 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kris van Wyk vs Tuncay Duran -- M15 Monastir F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144748:210513:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tuncay Duran (`KXITFMATCH-26OCT04VANDUR-DUR`) | 0.87 / 0.89 (3437) | 88.0% | -- | 92.9% | 85.5% [75.7%-90.1%] | 85.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.5 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kris van Wyk (`KXITFMATCH-26OCT04VANDUR-VAN`) | 0.11 / 0.12 (1545) | 11.5% | -- | 7.1% | 14.5% [9.9%-24.3%] | 14.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +3.0 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2787.0, B 2317.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.072
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.003, surface_dev_loose -0.014, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bianca Elena Barbulescu vs Daniella Dimitrova -- W50 Burgas R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220692:266564:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bianca Elena Barbulescu (`KXITFWMATCH-26OCT04BARDIM-BAR`) | 0.79 / 0.82 (3146) | 80.5% | -- | 60.6% | 74.0% [74.0%-74.0%] | -- | -- | -- | -- | PASS | -6.5 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Daniella Dimitrova (`KXITFWMATCH-26OCT04BARDIM-DIM`) | 0.16 / 0.21 (116) | 18.5% | -- | 39.4% | 26.0% [26.0%-26.0%] | -- | -- | -- | -- | PASS | +7.5 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 2116.0, B 0.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0001
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ekaterina Dotsenko vs Sophia Biolay -- W15 Monastir F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT04DOTBIO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sophia Biolay (`KXITFWMATCH-26OCT04DOTBIO-BIO`) | 0.36 / 0.38 (3176) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ekaterina Dotsenko (`KXITFWMATCH-26OCT04DOTBIO-DOT`) | 0.62 / 0.65 (1049) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andzhelina Kostova vs Lisa Peer -- W50 Burgas R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:266558:269682:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andzhelina Kostova (`KXITFWMATCH-26OCT04KOSPEE-KOS`) | 0.31 / 0.38 (40) | 34.5% | -- | 40.0% | 44.7% [43.1%-44.7%] | -- | -- | -- | -- | PASS | +10.2 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lisa Peer (`KXITFWMATCH-26OCT04KOSPEE-PEE`) | 0.60 / 0.63 (67) | 61.5% | -- | 60.1% | 55.3% [55.3%-56.9%] | -- | -- | -- | -- | PASS | -6.2 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 121.0, B 154.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.008
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chrystal Lopez vs Kaat Coppez -- W35 Villeneuve d'Ascq R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:263838:266467:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kaat Coppez (`KXITFWMATCH-26OCT04LOPCOP-COP`) | 0.59 / 0.63 (844) | 61.0% | -- | 83.3% | 73.2% [69.0%-77.4%] | -- | -- | -- | -- | WATCH | +12.2 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Chrystal Lopez (`KXITFWMATCH-26OCT04LOPCOP-LOP`) | 0.31 / 0.35 (38) | 33.0% | -- | 16.7% | 26.8% [22.6%-31.0%] | -- | -- | -- | -- | PASS | -6.2 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 708.0, B 759.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0419
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.030, surface_pool_high +0.023, surface_dev_loose -0.017, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lilian Poling vs Milena Maria Ciocan -- W35 Villeneuve d'Ascq R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221585:270134:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Milena Maria Ciocan (`KXITFWMATCH-26OCT04POLCIO-CIO`) | 0.52 / 0.56 (3158) | 54.0% | -- | 65.1% | 47.3% [45.7%-49.5%] | -- | -- | -- | -- | PASS | -6.7 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lilian Poling (`KXITFWMATCH-26OCT04POLCIO-POL`) | 0.44 / 0.45 (130) | 44.5% | -- | 34.9% | 52.7% [50.5%-54.3%] | -- | -- | -- | -- | PASS | +8.2 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1063.0, B 217.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0187
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anja Stankovic vs Galena Krastenova -- W50 Burgas R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:244087:265603:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Galena Krastenova (`KXITFWMATCH-26OCT04STAKRA-KRA`) | 0.06 / 0.08 (27) | 7.0% | -- | 34.9% | 22.8% [21.9%-23.2%] | -- | -- | -- | -- | PASS | +15.8 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anja Stankovic (`KXITFWMATCH-26OCT04STAKRA-STA`) | 0.72 / 0.93 (3192) | 82.5% | -- | 65.1% | 77.2% [76.8%-78.1%] | -- | -- | -- | -- | PASS | -5.3 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2297.0, B 135.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0063
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT04STAKRA-KRA  (YES = Galena Krastenova)
Model: 23%
Kalshi: 7%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lian Tran vs Evita Ramirez -- W35 Villeneuve d'Ascq R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220560:221522:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Evita Ramirez (`KXITFWMATCH-26OCT04TRARAM-RAM`) | 0.07 / 0.11 (3193) | 9.0% | -- | 62.1% | 20.3% [14.8%-24.3%] | -- | -- | -- | -- | PASS | +11.3 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lian Tran (`KXITFWMATCH-26OCT04TRARAM-TRA`) | 0.89 / 0.93 (0) | 91.0% | -- | 37.9% | 79.7% [75.7%-85.2%] | -- | -- | -- | -- | PASS | -11.3 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1204.0, B 116.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0471
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.029, surface_pool_high -0.023, surface_dev_loose +0.000, surface_dev_tight +0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Max Hans Rehberg vs Daniel Cukierman -- ATP Challenger Villena Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 15:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-04T15:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:131951:208819:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Cukierman (`KXATPCHALLENGERMATCH-26OCT04REHCUK-CUK`) | 0.10 / 0.11 (362) | 10.5% | -- | 13.1% | 22.1% [18.6%-28.1%] | -- | 12.1% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +11.6 pp | REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Max Hans Rehberg (`KXATPCHALLENGERMATCH-26OCT04REHCUK-REH`) | 0.88 / 0.90 (176) | 89.0% | -- | 86.9% | 77.9% [71.9%-81.4%] | -- | 87.3% | -- | INSUFFICIENT_INPUTS | PASS | -11.1 pp | REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4369.0, B 1609.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0477
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.035, surface_pool_high -0.039, surface_dev_loose +0.014, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Hynek Barton vs Stefan Latinovic -- ATP Challenger Villena Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-04T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04BARLAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hynek Barton (`KXATPCHALLENGERMATCH-26OCT04BARLAT-BAR`) | 0.90 / 0.92 (5531) | 91.0% | -- | -- | -- [-----] | -- | 88.8% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stefan Latinovic (`KXATPCHALLENGERMATCH-26OCT04BARLAT-LAT`) | 0.08 / 0.10 (1652) | 9.0% | -- | -- | -- [-----] | -- | 9.8% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Sebastian Gima vs Gabi Adrian Boitan -- M25 Slobozia F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04GIMBOI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabi Adrian Boitan (`KXITFMATCH-26OCT04GIMBOI-BOI`) | 0.71 / 0.72 (92) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sebastian Gima (`KXITFMATCH-26OCT04GIMBOI-GIM`) | 0.25 / 0.26 (939) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alejandro Moro Canas vs Alexander Ritschard -- M25 Zaragoza F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-04T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106310:208279:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alejandro Moro Canas (`KXITFMATCH-26OCT04MORRIT-MOR`) | 0.50 / 0.51 (86) | 50.5% | -- | 45.8% | 41.2% [39.1%-43.2%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexander Ritschard (`KXITFMATCH-26OCT04MORRIT-RIT`) | 0.49 / 0.50 (3646) | 49.5% | -- | 54.2% | 58.8% [56.8%-60.9%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +9.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6297.0, B 3172.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0204
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.015, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Joshua Sheehy vs Ivan Marrero Curbelo -- ATP Challenger Villena Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-04T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04SHEMAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ivan Marrero Curbelo (`KXATPCHALLENGERMATCH-26OCT04SHEMAR-MAR`) | 0.66 / 0.68 (2727) | 67.0% | -- | -- | -- [-----] | 66.4% | 68.7% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Joshua Sheehy (`KXATPCHALLENGERMATCH-26OCT04SHEMAR-SHE`) | 0.31 / 0.34 (4442) | 32.5% | -- | -- | -- [-----] | 33.6% | 31.8% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Noemi La Cagnina vs Sherin Scheerle -- W50 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222935:267839:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Noemi La Cagnina (`KXITFWMATCH-26OCT04LACSCH-LAC`) | 0.54 / 0.95 (164) | 74.5% | -- | 19.2% | 52.1% [51.1%-52.1%] | -- | -- | -- | -- | PASS | -22.4 pp | HIGH_REVIEW (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Sherin Scheerle (`KXITFWMATCH-26OCT04LACSCH-SCH`) | 0.05 / 0.46 (100) | 25.5% | -- | 80.8% | 47.9% [47.9%-48.9%] | -- | -- | -- | -- | PASS | +22.4 pp | HIGH_REVIEW (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 289.0, B 0.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0053
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT04LACSCH-SCH  (YES = Sherin Scheerle)
Model: 48%
Kalshi: 26%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lisa Pigato vs Eva Vedder -- W75 Quinta do Lago F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220770:221354:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lisa Pigato (`KXITFWMATCH-26OCT04PIGVED-PIG`) | 0.61 / 0.64 (1817) | 62.5% | -- | 79.1% | 73.8% [66.5%-76.3%] | 60.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +11.3 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Eva Vedder (`KXITFWMATCH-26OCT04PIGVED-VED`) | 0.35 / 0.37 (975) | 36.0% | -- | 20.9% | 26.2% [23.7%-33.5%] | 39.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.8 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4114.0, B 3271.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0491
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.009, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Joaquin Aguilar Cardozo vs Santiago De la Fuente -- ATP Challenger Antofagasta Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-04T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04AGUDLF:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joaquin Aguilar Cardozo (`KXATPCHALLENGERMATCH-26OCT04AGUDLF-AGU`) | 0.91 / 0.92 (2625) | 91.5% | -- | -- | -- [-----] | 88.2% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Santiago De la Fuente (`KXATPCHALLENGERMATCH-26OCT04AGUDLF-DLF`) | 0.08 / 0.09 (2349) | 8.5% | -- | -- | -- [-----] | 11.8% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Sascha Gueymard Wayenburg vs Clement Chidekh -- ATP Challenger Mouilleron-Le-Captif F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-04T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04GUECHI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Clement Chidekh (`KXATPCHALLENGERMATCH-26OCT04GUECHI-CHI`) | 0.55 / 0.56 (5984) | 55.5% | -- | -- | -- [-----] | 55.4% | 55.4% | 55.4% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sascha Gueymard Wayenburg (`KXATPCHALLENGERMATCH-26OCT04GUECHI-GUE`) | 0.43 / 0.44 (1785) | 43.5% | -- | -- | -- [-----] | 44.6% | 45.6% | 45.6% | EXTERNAL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Calvin Habiyambere vs Mehluli Don Ayanda Sibanda -- M25 Kigali R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04HABSIB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Calvin Habiyambere (`KXITFMATCH-26OCT04HABSIB-HAB`) | 0.05 / 0.10 (33) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mehluli Don Ayanda Sibanda (`KXITFMATCH-26OCT04HABSIB-SIB`) | 0.91 / 0.95 (815) | 93.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Franco Ribero vs Lorenzo Joaquin Rodriguez -- ATP Challenger Antofagasta Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-04T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04RIBROD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Franco Ribero (`KXATPCHALLENGERMATCH-26OCT04RIBROD-RIB`) | 0.16 / 0.18 (420) | 17.0% | -- | -- | -- [-----] | 20.8% | 18.2% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lorenzo Joaquin Rodriguez (`KXATPCHALLENGERMATCH-26OCT04RIBROD-ROD`) | 0.81 / 0.84 (1212) | 82.5% | -- | -- | -- [-----] | 79.2% | 81.7% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Joao Eduardo Schiessl vs Benjamin Torrealba -- ATP Challenger Antofagasta Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-04T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04SCHTOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joao Eduardo Schiessl (`KXATPCHALLENGERMATCH-26OCT04SCHTOR-SCH`) | 0.73 / 0.75 (1348) | 74.0% | -- | -- | -- [-----] | 73.5% | 74.7% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Benjamin Torrealba (`KXATPCHALLENGERMATCH-26OCT04SCHTOR-TOR`) | 0.25 / 0.26 (250) | 25.5% | -- | -- | -- [-----] | 26.5% | 24.7% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE

## AUM HIREN THAKKAR vs Mayank Sharma -- M25 Kigali R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04THASHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mayank Sharma (`KXITFMATCH-26OCT04THASHA-SHA`) | 0.06 / 0.90 (5) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| AUM HIREN THAKKAR (`KXITFMATCH-26OCT04THASHA-THA`) | 0.09 / 0.90 (5) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aniketh Venkataraman vs Joao Azzari Cabas -- M25 Kigali R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04VENAZZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joao Azzari Cabas (`KXITFMATCH-26OCT04VENAZZ-AZZ`) | 0.06 / 0.56 (24) | 31.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aniketh Venkataraman (`KXITFMATCH-26OCT04VENAZZ-VEN`) | 0.20 / 0.93 (5) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Charo Esquiva Banuls vs Valentina Ivanov -- W35 Baza F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221173:264962:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charo Esquiva Banuls (`KXITFWMATCH-26OCT04ESQIVA-ESQ`) | 0.67 / 0.70 (893) | 68.5% | -- | 19.5% | 34.3% [27.7%-45.2%] | 67.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -34.2 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valentina Ivanov (`KXITFWMATCH-26OCT04ESQIVA-IVA`) | 0.29 / 0.31 (3778) | 30.0% | -- | 80.5% | 65.7% [54.8%-72.3%] | 32.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +35.7 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1005.0, B 1892.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0874
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT04ESQIVA-IVA  (YES = Valentina Ivanov)
Model: 66%
Kalshi: 30%
Gap: +36 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.024, surface_dev_tight +0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oleksii Krutykh vs Francisco Rocha -- ATP Challenger Braga Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 16:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-04T16:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04KRUROC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oleksii Krutykh (`KXATPCHALLENGERMATCH-26OCT04KRUROC-KRU`) | 0.82 / 0.84 (3744) | 83.0% | -- | -- | -- [-----] | 80.3% | 82.4% | 81.3% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Francisco Rocha (`KXATPCHALLENGERMATCH-26OCT04KRUROC-ROC`) | 0.16 / 0.17 (1269) | 16.5% | -- | -- | -- [-----] | 19.7% | 19.6% | 19.6% | KALSHI_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Sergi Perez Contri vs Nicolas Barrientos -- ATP Challenger Braga Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 16:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-04T16:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04PERBAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Barrientos (`KXATPCHALLENGERMATCH-26OCT04PERBAR-BAR`) | 0.32 / 0.33 (304) | 32.5% | -- | -- | -- [-----] | 34.3% | 32.3% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sergi Perez Contri (`KXATPCHALLENGERMATCH-26OCT04PERBAR-PER`) | 0.66 / 0.68 (2723) | 67.0% | -- | -- | -- [-----] | 65.7% | 67.7% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Filip Pieczonka vs Adrian Oetzbach -- ATP Challenger Braga Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 16:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-04T16:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04PIEOET:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Oetzbach (`KXATPCHALLENGERMATCH-26OCT04PIEOET-OET`) | 0.32 / 0.33 (350) | 32.5% | -- | -- | -- [-----] | 34.3% | 29.2% | 34.3% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Filip Pieczonka (`KXATPCHALLENGERMATCH-26OCT04PIEOET-PIE`) | 0.67 / 0.68 (5990) | 67.5% | -- | -- | -- [-----] | 65.7% | 68.1% | 65.7% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Patrick Brady vs Mili Poljicak -- ATP Challenger Villena Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 16:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-04T16:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04BRAPOL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Patrick Brady (`KXATPCHALLENGERMATCH-26OCT04BRAPOL-BRA`) | 0.45 / 0.46 (5278) | 45.5% | -- | -- | -- [-----] | 44.6% | 46.5% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mili Poljicak (`KXATPCHALLENGERMATCH-26OCT04BRAPOL-POL`) | 0.54 / 0.55 (3884) | 54.5% | -- | -- | -- [-----] | 55.4% | 52.7% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Benjamin Lock vs Calvin Hemery -- M25 Kigali F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-04T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111761:123921:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Calvin Hemery (`KXITFMATCH-26OCT04LOCHEM-HEM`) | 0.77 / 0.78 (4705) | 77.5% | -- | 69.6% | 72.2% [71.3%-77.6%] | 76.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.3 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Benjamin Lock (`KXITFMATCH-26OCT04LOCHEM-LOC`) | 0.21 / 0.22 (231) | 21.5% | -- | 30.4% | 27.8% [22.4%-28.7%] | 23.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.3 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4430.0, B 5909.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0313
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.004, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## HAJAR CRINEBOUCH vs eunchae Kim -- W35 Villeneuve d'Ascq R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260093:263728:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| HAJAR CRINEBOUCH (`KXITFWMATCH-26OCT04CRIKIM-CRI`) | 0.11 / 0.16 (94) | 13.5% | -- | 37.3% | 35.3% [34.3%-36.4%] | -- | -- | -- | -- | PASS | +21.8 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| eunchae Kim (`KXITFWMATCH-26OCT04CRIKIM-KIM`) | 0.82 / 0.87 (15) | 84.5% | -- | 62.7% | 64.7% [63.6%-65.7%] | -- | -- | -- | -- | PASS | -19.8 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 479.0, B 197.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0101
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT04CRIKIM-CRI  (YES = HAJAR CRINEBOUCH)
Model: 35%
Kalshi: 14%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.005, surface_dev_loose -0.000, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ilina Ilieva vs Melis Rasim -- W50 Burgas R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT04ILIRAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ilina Ilieva (`KXITFWMATCH-26OCT04ILIRAS-ILI`) | 0.10 / 0.27 (1) | 18.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Melis Rasim (`KXITFWMATCH-26OCT04ILIRAS-RAS`) | 0.67 / 0.90 (3925) | 78.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Diana-Ioana Simionescu vs Ralitsa Alexandrova -- W50 Burgas R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223319:264978:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ralitsa Alexandrova (`KXITFWMATCH-26OCT04SIMALE-ALE`) | 0.05 / 0.09 (4004) | 7.0% | -- | 50.5% | 34.4% [34.4%-34.4%] | -- | -- | -- | -- | PASS | +27.4 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Diana-Ioana Simionescu (`KXITFWMATCH-26OCT04SIMALE-SIM`) | 0.91 / 0.94 (994) | 92.5% | -- | 49.5% | 65.6% [65.6%-65.6%] | -- | -- | -- | -- | PASS | -26.9 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1418.0, B 0.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT04SIMALE-ALE  (YES = Ralitsa Alexandrova)
Model: 34%
Kalshi: 7%
Gap: +27 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Melanie Stoichkova vs Nicole Gadient -- W50 Burgas R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT04STOGAD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicole Gadient (`KXITFWMATCH-26OCT04STOGAD-GAD`) | 0.90 / 0.95 (4395) | 92.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Melanie Stoichkova (`KXITFWMATCH-26OCT04STOGAD-STO`) | 0.05 / 0.10 (3) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marie Villet vs Valentina Khrebtova -- W35 Villeneuve d'Ascq R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:219979:266803:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentina Khrebtova (`KXITFWMATCH-26OCT04VILKHR-KHR`) | 0.14 / 0.19 (61) | 16.5% | -- | 58.0% | 40.5% [38.4%-42.5%] | -- | -- | -- | -- | PASS | +24.0 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marie Villet (`KXITFWMATCH-26OCT04VILKHR-VIL`) | 0.81 / 0.86 (60) | 83.5% | -- | 42.0% | 59.5% [57.5%-61.6%] | -- | -- | -- | -- | PASS | -24.0 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2089.0, B 222.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0207
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT04VILKHR-KHR  (YES = Valentina Khrebtova)
Model: 40%
Kalshi: 16%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Niklas Grunewald vs Trishan Dhawan -- M25 Kigali R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04GRUDHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Trishan Dhawan (`KXITFMATCH-26OCT04GRUDHA-DHA`) | 0.05 / 0.90 (5) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Niklas Grunewald (`KXITFMATCH-26OCT04GRUDHA-GRU`) | 0.07 / 0.94 (0) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vansh Janghu vs Anup Bangargi -- M25 Kigali R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04JANBAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anup Bangargi (`KXITFMATCH-26OCT04JANBAN-BAN`) | 0.21 / 0.90 (5) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vansh Janghu (`KXITFMATCH-26OCT04JANBAN-JAN`) | 0.06 / 0.81 (50) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ethan Terblanche vs Nicholas Van Aken -- M25 Kigali R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04TERVAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ethan Terblanche (`KXITFMATCH-26OCT04TERVAN-TER`) | 0.06 / 0.90 (5) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nicholas Van Aken (`KXITFMATCH-26OCT04TERVAN-VAN`) | 0.06 / 0.90 (5) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nicolas Bruna vs Alan Magadan -- ATP Challenger Antofagasta Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 17:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-04T17:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04BRUMAG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Bruna (`KXATPCHALLENGERMATCH-26OCT04BRUMAG-BRU`) | 0.13 / 0.15 (319) | 14.0% | -- | -- | -- [-----] | 17.1% | -- | 17.1% | KALSHI_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alan Magadan (`KXATPCHALLENGERMATCH-26OCT04BRUMAG-MAG`) | 0.84 / 0.87 (1966) | 85.5% | -- | -- | -- [-----] | 82.9% | -- | 82.9% | KALSHI_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Hernan Casanova vs Wilson Leite -- ATP Challenger Antofagasta Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 17:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-04T17:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04CASLEI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hernan Casanova (`KXATPCHALLENGERMATCH-26OCT04CASLEI-CAS`) | 0.86 / 0.88 (4) | 87.0% | -- | -- | -- [-----] | 83.6% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Wilson Leite (`KXATPCHALLENGERMATCH-26OCT04CASLEI-LEI`) | 0.12 / 0.14 (1973) | 13.0% | -- | -- | -- [-----] | 16.4% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Bernardo Munk Mesa vs Bruno Fernandez -- ATP Challenger Antofagasta Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 17:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-04T17:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04MUNFER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bruno Fernandez (`KXATPCHALLENGERMATCH-26OCT04MUNFER-FER`) | 0.56 / 0.58 (1385) | 57.0% | -- | -- | -- [-----] | 57.2% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bernardo Munk Mesa (`KXATPCHALLENGERMATCH-26OCT04MUNFER-MUN`) | 0.42 / 0.43 (250) | 42.5% | -- | -- | -- [-----] | 42.8% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Kim Chiarello vs Anna Brunet-Brady -- W35 Villeneuve d'Ascq R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:269710:270452:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Brunet-Brady (`KXITFWMATCH-26OCT04CHIBRU-BRU`) | 0.11 / 0.13 (7) | 12.0% | -- | 46.3% | 36.5% [35.4%-37.0%] | -- | -- | -- | -- | PASS | +24.5 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kim Chiarello (`KXITFWMATCH-26OCT04CHIBRU-CHI`) | 0.70 / 0.89 (3367) | 79.5% | -- | 53.7% | 63.5% [63.0%-64.6%] | -- | -- | -- | -- | PASS | -16.0 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 458.0, B 135.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0078
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT04CHIBRU-BRU  (YES = Anna Brunet-Brady)
Model: 36%
Kalshi: 12%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lola Collin vs Heerae Im -- W35 Villeneuve d'Ascq R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259708:260091:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lola Collin (`KXITFWMATCH-26OCT04COLIMX-COL`) | 0.21 / 0.27 (35) | 24.0% | -- | 28.6% | 26.9% [26.0%-27.8%] | -- | -- | -- | -- | PASS | +2.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Heerae Im (`KXITFWMATCH-26OCT04COLIMX-IMX`) | 0.73 / 0.79 (22) | 76.0% | -- | 71.4% | 73.2% [72.2%-74.0%] | -- | -- | -- | -- | PASS | -2.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 74.0, B 568.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.009
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anna Ozerova vs Alexa Karatancheva -- W50 Burgas R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216030:246489:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexa Karatancheva (`KXITFWMATCH-26OCT04OZEKAR-KAR`) | 0.67 / 0.71 (59) | 69.0% | -- | 30.0% | 29.1% [28.6%-29.6%] | -- | -- | -- | -- | PASS | -39.9 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna Ozerova (`KXITFWMATCH-26OCT04OZEKAR-OZE`) | 0.29 / 0.33 (1) | 31.0% | -- | 70.0% | 70.9% [70.4%-71.4%] | -- | -- | -- | -- | PASS | +39.9 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 140.0, B 500.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0049
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT04OZEKAR-OZE  (YES = Anna Ozerova)
Model: 71%
Kalshi: 31%
Gap: +40 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oana Georgeta Simion vs Kalina Simeonova -- W50 Burgas R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211646:267821:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oana Georgeta Simion (`KXITFWMATCH-26OCT04SIMSIM2-SIM`) | 0.79 / 0.93 (0) | 86.0% | -- | 52.1% | 81.1% [81.1%-81.1%] | -- | -- | -- | -- | PASS | -4.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Kalina Simeonova (`KXITFWMATCH-26OCT04SIMSIM2-SIM2`) | 0.07 / 0.21 (0) | 14.0% | -- | 47.9% | 18.9% [18.9%-18.9%] | -- | -- | -- | -- | PASS | +4.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1762.0, B 0.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mariella Thamm vs Savine ERLER -- W35 Villeneuve d'Ascq R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222757:265701:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Savine ERLER (`KXITFWMATCH-26OCT04THAERL-ERL`) | 0.13 / 0.18 (24) | 15.5% | -- | 37.4% | 23.1% [16.8%-26.4%] | -- | -- | -- | -- | PASS | +7.5 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mariella Thamm (`KXITFWMATCH-26OCT04THAERL-THA`) | 0.82 / 0.87 (68) | 84.5% | -- | 62.6% | 77.0% [73.6%-83.2%] | -- | -- | -- | -- | PASS | -7.5 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1262.0, B 499.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0481
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.024, surface_pool_high -0.021, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dylan Dietrich vs Abdullah Shelbayh -- ATP Challenger Columbus F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-04T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04DIESHE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dylan Dietrich (`KXATPCHALLENGERMATCH-26OCT04DIESHE-DIE`) | 0.67 / 0.68 (10) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Abdullah Shelbayh (`KXATPCHALLENGERMATCH-26OCT04DIESHE-SHE`) | 0.32 / 0.33 (5389) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Gustavo Heide vs Guido Ivan Justo -- ATP Challenger Curitiba F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-04T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04HEIJUS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gustavo Heide (`KXATPCHALLENGERMATCH-26OCT04HEIJUS-HEI`) | 0.75 / 0.76 (73) | 75.5% | -- | -- | -- [-----] | 74.0% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Guido Ivan Justo (`KXATPCHALLENGERMATCH-26OCT04HEIJUS-JUS`) | 0.23 / 0.25 (2937) | 24.0% | -- | -- | -- [-----] | 26.0% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Mateus Alves vs Bautista de la Pena -- ATP Challenger Antofagasta Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 18:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-04T18:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04ALVDE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mateus Alves (`KXATPCHALLENGERMATCH-26OCT04ALVDE-ALV`) | 0.89 / 0.94 (21) | 91.5% | -- | -- | -- [-----] | -- | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bautista de la Pena (`KXATPCHALLENGERMATCH-26OCT04ALVDE-DE`) | 0.06 / 0.08 (41) | 7.0% | -- | -- | -- [-----] | -- | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Nicolas Kicker vs Milledge Cossu -- ATP Challenger Antofagasta Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 18:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-04T18:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04KICCOS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Milledge Cossu (`KXATPCHALLENGERMATCH-26OCT04KICCOS-COS`) | 0.04 / 0.05 (57) | 4.5% | -- | -- | -- [-----] | -- | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nicolas Kicker (`KXATPCHALLENGERMATCH-26OCT04KICCOS-KIC`) | 0.95 / 0.96 (700) | 95.5% | -- | -- | -- [-----] | -- | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Jose Pereira vs Arklon Huertas Del Pino Cordova -- ATP Challenger Antofagasta Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 18:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-04T18:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04PERHUE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arklon Huertas Del Pino Cordova (`KXATPCHALLENGERMATCH-26OCT04PERHUE-HUE`) | 0.32 / 0.40 (51) | 36.0% | -- | -- | -- [-----] | 35.4% | -- | 35.4% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jose Pereira (`KXATPCHALLENGERMATCH-26OCT04PERHUE-PER`) | 0.59 / 0.67 (200) | 63.0% | -- | -- | -- [-----] | 64.6% | -- | 64.6% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE; WIDE_SPREAD

## Florence Fedeli vs Margaux Komano -- W35 Villeneuve d'Ascq R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221524:266587:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Florence Fedeli (`KXITFWMATCH-26OCT04FEDKOM-FED`) | 0.05 / 0.06 (9) | 5.5% | -- | 41.5% | 19.6% [18.2%-20.4%] | -- | -- | -- | -- | PASS | +14.1 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Margaux Komano (`KXITFWMATCH-26OCT04FEDKOM-KOM`) | 0.94 / 0.95 (373) | 94.5% | -- | 58.5% | 80.4% [79.6%-81.8%] | -- | -- | -- | -- | PASS | -14.1 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 30.0, B 941.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0111
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.007, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andreya Glushkova vs Sonja Zhenikhova -- W50 Burgas R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264961:267887:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andreya Glushkova (`KXITFWMATCH-26OCT04GLUZHE-GLU`) | 0.05 / 0.95 (164) | 50.0% | -- | 54.3% | 18.9% [18.9%-18.9%] | -- | -- | -- | -- | PASS | -31.1 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sonja Zhenikhova (`KXITFWMATCH-26OCT04GLUZHE-ZHE`) | 0.05 / 0.95 (142) | 50.0% | -- | 45.7% | 81.1% [81.1%-81.2%] | -- | -- | -- | -- | PASS | +31.1 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 1212.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0002
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT04GLUZHE-ZHE  (YES = Sonja Zhenikhova)
Model: 81%
Kalshi: 50%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Giulia Safina Popa vs Julia Hofmann -- W50 Burgas R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:267428:270409:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julia Hofmann (`KXITFWMATCH-26OCT04POPHOF-HOF`) | 0.05 / 0.95 (164) | 50.0% | -- | 31.5% | 19.6% [19.6%-20.3%] | -- | -- | -- | -- | PASS | -30.4 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Giulia Safina Popa (`KXITFWMATCH-26OCT04POPHOF-POP`) | 0.05 / 0.95 (142) | 50.0% | -- | 68.5% | 80.4% [79.7%-80.4%] | -- | -- | -- | -- | PASS | +30.4 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1013.0, B 81.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0037
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT04POPHOF-POP  (YES = Giulia Safina Popa)
Model: 80%
Kalshi: 50%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elise Renard vs Amelie Brooks -- W35 Villeneuve d'Ascq R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259608:260377:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amelie Brooks (`KXITFWMATCH-26OCT04RENBRO-BRO`) | 0.43 / 0.47 (47) | 45.0% | -- | 69.5% | 36.9% [34.4%-40.4%] | -- | -- | -- | -- | PASS | -8.1 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elise Renard (`KXITFWMATCH-26OCT04RENBRO-REN`) | 0.53 / 0.57 (3100) | 55.0% | -- | 30.5% | 63.1% [59.6%-65.6%] | -- | -- | -- | -- | PASS | +8.1 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 389.0, B 164.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0303
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.005, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Isis Louise Van den Broek vs Britt Du Pree -- W35 Reims F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264227:264228:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Britt Du Pree (`KXITFWMATCH-26OCT04VANDUP-DUP`) | 0.73 / 0.75 (0) | 74.0% | -- | 69.0% | 61.1% [54.8%-64.2%] | 72.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.9 pp | REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Isis Louise Van den Broek (`KXITFWMATCH-26OCT04VANDUP-VAN`) | 0.25 / 0.28 (125) | 26.5% | -- | 30.9% | 38.9% [35.8%-45.2%] | 28.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +12.4 pp | REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1856.0, B 2691.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0468
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Klara Veldman vs Emma Fulvia Wiesenfeld -- W35 Villeneuve d'Ascq R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223418:266477:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Klara Veldman (`KXITFWMATCH-26OCT04VELWIE-VEL`) | 0.89 / 0.94 (67) | 91.5% | -- | 52.7% | 63.6% [61.5%-64.6%] | -- | -- | -- | -- | PASS | -27.9 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Emma Fulvia Wiesenfeld (`KXITFWMATCH-26OCT04VELWIE-WIE`) | 0.06 / 0.11 (22) | 8.5% | -- | 47.3% | 36.4% [35.4%-38.5%] | -- | -- | -- | -- | PASS | +27.9 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1299.0, B 46.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0151
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT04VELWIE-WIE  (YES = Emma Fulvia Wiesenfeld)
Model: 36%
Kalshi: 8%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ana Sofia Sanchez vs Leyla Fiorella Britez Risso -- W15 Trelew F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:204419:222513:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leyla Fiorella Britez Risso (`KXITFWMATCH-26OCT04SANBRI-BRI`) | 0.48 / 0.51 (1) | 49.5% | -- | 9.0% | 24.2% [21.4%-27.7%] | 50.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -25.3 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Ana Sofia Sanchez (`KXITFWMATCH-26OCT04SANBRI-SAN`) | 0.49 / 0.51 (1) | 50.0% | -- | 91.0% | 75.8% [72.3%-78.6%] | 50.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +25.8 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 3191.0, B 257.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0315
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT04SANBRI-SAN  (YES = Ana Sofia Sanchez)
Model: 76%
Kalshi: 50%
Gap: +26 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.021, surface_dev_loose +0.008, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marine Szostak vs Leila Fabbri -- W35 Villeneuve d'Ascq R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT04SZOFAB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leila Fabbri (`KXITFWMATCH-26OCT04SZOFAB-FAB`) | 0.05 / 0.09 (80) | 7.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marine Szostak (`KXITFWMATCH-26OCT04SZOFAB-SZO`) | 0.91 / 0.95 (363) | 93.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Theo Papamalamis vs Dominick Mosejczuk -- M15 Fayetteville AR F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210494:213771:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dominick Mosejczuk (`KXITFMATCH-26OCT04PAPMOS-MOS`) | 0.43 / 0.45 (18) | 44.0% | -- | 26.4% | 27.7% [27.3%-28.6%] | 43.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -16.3 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Theo Papamalamis (`KXITFMATCH-26OCT04PAPMOS-PAP`) | 0.55 / 0.58 (24) | 56.5% | -- | 73.6% | 72.3% [71.4%-72.7%] | 56.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +15.8 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1643.0, B 379.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0067
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT04PAPMOS-PAP  (YES = Theo Papamalamis)
Model: 72%
Kalshi: 56%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.009, surface_dev_loose +0.004, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rose Marie Nijkamp vs Astra Sharma -- W15 Nashville TN F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206292:260225:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rose Marie Nijkamp (`KXITFWMATCH-26OCT04NIJSHA-NIJ`) | 0.20 / 0.22 (12) | 21.0% | -- | 45.2% | 30.6% [25.2%-35.4%] | 23.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +9.6 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Astra Sharma (`KXITFWMATCH-26OCT04NIJSHA-SHA`) | 0.77 / 0.80 (353) | 78.5% | -- | 54.8% | 69.4% [64.6%-74.8%] | 76.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.1 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1080.0, B 2800.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.051
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Max Dahlin vs Oliver Bonding -- M15 Ann Arbor MI F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-04T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211609:212839:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oliver Bonding (`KXITFMATCH-26OCT04DAHBON-BON`) | 0.50 / 0.52 (375) | 51.0% | -- | 43.5% | 50.0% [47.0%-53.0%] | 51.9% | -- | 51.9% | MODEL_LONE_OUTLIER | PASS | -1.0 pp | NORMAL | STALE | C / LIMITED | ALL_AGREE | VERIFIED |
| Max Dahlin (`KXITFMATCH-26OCT04DAHBON-DAH`) | 0.47 / 0.49 (71) | 48.0% | -- | 56.5% | 50.0% [47.0%-53.0%] | 48.1% | -- | 48.1% | MODEL_LONE_OUTLIER | PASS | +2.0 pp | NORMAL | STALE | C / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 583.0, B 1207.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0301
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.030, surface_pool_high -0.030, surface_dev_loose +0.010, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tatjana Maria vs Madison Brengle -- W100 Templeton CA F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT04MARBRE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Madison Brengle (`KXITFWMATCH-26OCT04MARBRE-BRE`) | 0.05 / 0.95 (164) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tatjana Maria (`KXITFWMATCH-26OCT04MARBRE-MAR`) | 0.05 / 0.95 (142) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Simone Bolelli / Andrea Vavassori vs Austin Krajicek / Nikola Mektic -- ATP Tokyo SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-05T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT04BOLVAVKRAMEK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Simone Bolelli / Andrea Vavassori (`KXATPDOUBLES-26OCT04BOLVAVKRAMEK-BOLVAV`) | 0.59 / 0.60 (1897) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Austin Krajicek / Nikola Mektic (`KXATPDOUBLES-26OCT04BOLVAVKRAMEK-KRAMEK`) | 0.39 / 0.41 (829) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Belinda Bencic vs Ann Li -- WTA Beijing R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-05 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-05T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT04BENANN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ann Li (`KXWTAMATCH-26OCT04BENANN-ANN`) | 0.32 / 0.34 (99) | 33.0% | -- | -- | -- [-----] | 34.2% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Belinda Bencic (`KXWTAMATCH-26OCT04BENANN-BEN`) | 0.65 / 0.68 (4798) | 66.5% | -- | -- | -- [-----] | 65.8% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD

## Marie Bouzkova vs Qinwen Zheng -- WTA Beijing R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-05 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-05T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT04BOUZHE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marie Bouzkova (`KXWTAMATCH-26OCT04BOUZHE-BOU`) | 0.43 / 0.46 (7426) | 44.5% | -- | -- | -- [-----] | 44.4% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Qinwen Zheng (`KXWTAMATCH-26OCT04BOUZHE-ZHE`) | 0.54 / 0.57 (421) | 55.5% | -- | -- | -- [-----] | 55.6% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD

## Alina Charaeva vs Sonay Kartal -- WTA Beijing R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-05 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-05T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT04CHAKAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alina Charaeva (`KXWTAMATCH-26OCT04CHAKAR-CHA`) | 0.36 / 0.39 (3150) | 37.5% | -- | -- | -- [-----] | 38.4% | -- | 38.4% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sonay Kartal (`KXWTAMATCH-26OCT04CHAKAR-KAR`) | 0.60 / 0.64 (4531) | 62.0% | -- | -- | -- [-----] | 61.6% | -- | 61.6% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE; WIDE_SPREAD

## Coco Gauff vs Xinran Sun -- WTA Beijing R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-05 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-05T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT04GAUSUN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Coco Gauff (`KXWTAMATCH-26OCT04GAUSUN-GAU`) | 0.91 / 0.92 (352) | 91.5% | -- | -- | -- [-----] | 92.0% | -- | 92.0% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xinran Sun (`KXWTAMATCH-26OCT04GAUSUN-SUN`) | 0.06 / 0.08 (3806) | 7.0% | -- | -- | -- [-----] | 8.0% | -- | 8.0% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Iva Jovic vs Kamilla Rakhimova -- WTA Beijing R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-05 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-04 04:41Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-05T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT04JOVRAK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iva Jovic (`KXWTAMATCH-26OCT04JOVRAK-JOV`) | 0.79 / 0.82 (5474) | 80.5% | -- | -- | -- [-----] | 78.6% | -- | 78.6% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kamilla Rakhimova (`KXWTAMATCH-26OCT04JOVRAK-RAK`) | 0.18 / 0.20 (150) | 19.0% | -- | -- | -- [-----] | 21.4% | -- | 21.4% | KALSHI_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE; WIDE_SPREAD

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
