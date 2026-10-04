# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-04T05:19Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 11,519): 0-3 13.3%, 3-5 9.0%, 5-10 19.3%, 10-15 14.9%, 15-25 19.6%, 25-40 14.4%, 40+ 9.5%; median gap 12.58 pp.
* **Where the extremes live**: 96.8% of >=25 pp gaps are off the ATP/WTA main tour (ITF 74.8%, Challenger 12.4%, doubles 6.7%). Main tour: ATP 4.1% and WTA 9.4% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 2,754): MARKET_ALREADY_SETTLED_WHEN_PRICED 46.8%, STALE_QUOTE 24.0%, POOR_DATA 6.1%, BOOK_QUALITY 6.0%, POSSIBLY_IN_PLAY_QUOTE 5.3%, IN_PLAY_QUOTE 3.7%, LIMITED_DATA 3.1%, IDENTITY_AMBIGUOUS 2.7%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%. By class: coverage 46.8%, market_freshness 24.0%, data 9.2%, market_freshness/coverage 9.0%, execution 6.0%, mapping 2.7%, model_calibration_or_unknown 2.2%.
* **Stale / settled / in-play**: 69.9% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 55.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 2,754 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 14.7% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.6%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 7.0% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 824.0 points vs 1948.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.1, Gen-2 0.92, Gen-1 ledger 0.885 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 92 model 0.2371 vs Kalshi 0.1839; n 26 model 0.3509 vs Kalshi 0.1453.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 36,851 model-market comparisons (64,126 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 16,844 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-04T05:15:37.325408+00:00'], shadow board 10,661 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-04T05:15:40.001895+00:00'], Model 4 2,930 rows, 8,298 settled tickers, 1,894 tickers with an external scan.
* By model: {"gen1_ledger": 9762, "gen1_elo": 5362, "fair_v1": 5362, "gen2": 5362, "gen1_sr": 5362, "model4_fundamental": 2825, "model4_conditioned": 2816}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 11,519 | 13.3 | 9.0 | 19.3 | 14.9 | 19.6 | 14.4 | 9.5 | 12.58 | 43.5% | 23.9% |
| MW fair_v1 | 5,362 | 13.4 | 8.4 | 18.5 | 15.2 | 18.5 | 15.2 | 10.7 | 12.99 | 44.4% | 25.9% |
| MW gen1_elo | 5,362 | 13.2 | 8.7 | 19.9 | 14.8 | 18.3 | 15.0 | 10.0 | 12.49 | 43.3% | 25.1% |
| MW gen1_ledger | 6,157 | 13.2 | 9.5 | 20.0 | 14.7 | 20.5 | 13.8 | 8.3 | 12.22 | 42.6% | 22.2% |
| MW gen1_sr | 5,362 | 9.5 | 7.2 | 16.6 | 13.6 | 22.2 | 18.3 | 12.6 | 16.19 | 53.1% | 30.9% |
| MW gen2 | 5,362 | 11.3 | 6.6 | 16.4 | 14.4 | 20.3 | 17.1 | 13.8 | 15.56 | 51.2% | 31.0% |
| all families model4_conditioned | 2,816 | 18.6 | 15.4 | 29.6 | 23.8 | 8.4 | 2.4 | 1.9 | 7.37 | 12.6% | 4.3% |
| all families model4_fundamental | 2,825 | 14.6 | 10.7 | 29.9 | 21.7 | 14.6 | 5.5 | 3.0 | 9.1 | 23.1% | 8.5% |

Configurable thresholds (primary): >=5pp 77.7%, >=10pp 58.4%, >=15pp 43.5%, >=20pp 33.0%, >=25pp 23.9%, >=30pp 17.5%, >=40pp 9.5%, >=50pp 4.3%
Executable gap (model outside the book, before fees): median 10.21pp; >=10pp 50.6%, >=25pp 21.2%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 242 | 22.3 | 17.4 | 27.3 | 12.8 | 14.9 | 1.6 | 3.7 | 6.19 | 20.2% | 5.4% |
| CHALLENGER | 1,002 | 15.4 | 10.5 | 16.3 | 16.2 | 15.3 | 14.7 | 11.8 | 12.71 | 41.7% | 26.5% |
| ITF_MEN | 1,679 | 11.8 | 8.3 | 19.9 | 14.9 | 17.6 | 14.7 | 12.6 | 12.8 | 45.0% | 27.3% |
| ITF_WOMEN | 1,916 | 10.3 | 6.0 | 15.7 | 15.4 | 21.4 | 19.5 | 11.6 | 15.99 | 52.5% | 31.1% |
| WTA | 435 | 23.0 | 10.6 | 25.8 | 12.6 | 18.9 | 6.7 | 2.5 | 8.16 | 28.1% | 9.2% |
| WTA125 | 88 | 13.6 | 4.5 | 18.2 | 26.1 | 19.3 | 13.6 | 4.5 | 11.83 | 37.5% | 18.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 242 | 23.1 | 12.8 | 24.8 | 16.1 | 17.4 | 1.6 | 4.1 | 7.29 | 23.1% | 5.8% |
| CHALLENGER | 1,002 | 12.9 | 5.8 | 18.5 | 15.7 | 18.5 | 17.0 | 11.8 | 14.22 | 47.2% | 28.7% |
| ITF_MEN | 1,679 | 9.7 | 6.8 | 17.4 | 15.2 | 20.2 | 16.6 | 14.1 | 15.41 | 50.9% | 30.6% |
| ITF_WOMEN | 1,916 | 8.6 | 6.4 | 13.3 | 12.4 | 20.9 | 19.9 | 18.6 | 19.12 | 59.4% | 38.5% |
| WTA | 435 | 20.5 | 5.5 | 16.8 | 15.6 | 22.3 | 16.8 | 2.5 | 12.98 | 41.6% | 19.3% |
| WTA125 | 88 | 5.7 | 5.7 | 15.9 | 20.4 | 25.0 | 14.8 | 12.5 | 15.96 | 52.3% | 27.3% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 242 | 28.1 | 12.8 | 28.5 | 10.7 | 9.1 | 7.0 | 3.7 | 6.53 | 19.8% | 10.7% |
| CHALLENGER | 1,002 | 16.2 | 9.2 | 22.1 | 13.2 | 13.5 | 13.5 | 12.5 | 10.75 | 39.4% | 25.9% |
| ITF_MEN | 1,679 | 10.3 | 9.3 | 18.5 | 15.7 | 18.6 | 15.3 | 12.3 | 13.47 | 46.2% | 27.6% |
| ITF_WOMEN | 1,916 | 9.9 | 6.4 | 16.5 | 14.5 | 23.5 | 19.2 | 9.9 | 16.56 | 52.7% | 29.1% |
| WTA | 435 | 23.4 | 14.0 | 29.4 | 15.6 | 11.5 | 4.4 | 1.6 | 6.99 | 17.5% | 6.0% |
| WTA125 | 88 | 17.1 | 5.7 | 23.9 | 29.6 | 12.5 | 10.2 | 1.1 | 10.72 | 23.9% | 11.4% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 72 | 23.6 | 22.2 | 34.7 | 12.5 | 6.9 | 0.0 | 0.0 | 6.26 | 6.9% | 0.0% |
| CHALLENGER | 853 | 21.2 | 14.3 | 26.0 | 15.6 | 13.9 | 6.3 | 2.6 | 7.42 | 22.9% | 8.9% |
| DOUBLES | 384 | 5.7 | 3.9 | 9.9 | 10.4 | 21.9 | 20.8 | 27.3 | 24.07 | 70.0% | 48.2% |
| ITF_MEN | 2,065 | 14.1 | 9.2 | 18.9 | 14.0 | 20.8 | 13.5 | 9.5 | 12.43 | 43.8% | 23.0% |
| ITF_WOMEN | 1,933 | 8.9 | 8.3 | 17.4 | 14.2 | 23.9 | 18.6 | 8.8 | 15.54 | 51.3% | 27.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 363 | 15.4 | 9.4 | 25.6 | 22.3 | 17.6 | 8.8 | 0.8 | 9.8 | 27.3% | 9.6% |
| WTA125 | 338 | 13.3 | 9.8 | 21.6 | 16.9 | 22.8 | 11.8 | 3.9 | 11.33 | 38.5% | 15.7% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 241 | 22.0 | 17.4 | 27.4 | 12.9 | 14.9 | 1.7 | 3.7 | 6.21 | 20.3% | 5.4% |
| CHALLENGER | 760 | 19.1 | 12.9 | 19.5 | 19.1 | 16.3 | 8.7 | 4.5 | 9.68 | 29.5% | 13.2% |
| ITF_MEN | 1,057 | 15.8 | 11.7 | 25.1 | 16.6 | 17.4 | 9.5 | 3.9 | 9.43 | 30.8% | 13.3% |
| ITF_WOMEN | 1,303 | 13.9 | 7.9 | 18.6 | 17.7 | 22.6 | 14.7 | 4.5 | 12.71 | 41.8% | 19.2% |
| WTA | 434 | 23.0 | 10.6 | 25.8 | 12.7 | 18.9 | 6.5 | 2.5 | 8.16 | 27.9% | 9.0% |
| WTA125 | 85 | 14.1 | 4.7 | 18.8 | 27.1 | 18.8 | 11.8 | 4.7 | 11.65 | 35.3% | 16.5% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 241 | 23.2 | 12.4 | 24.9 | 16.2 | 17.4 | 1.7 | 4.2 | 7.5 | 23.2% | 5.8% |
| CHALLENGER | 760 | 15.9 | 7.2 | 22.8 | 18.7 | 19.3 | 12.4 | 3.7 | 11.16 | 35.4% | 16.1% |
| ITF_MEN | 1,057 | 13.2 | 8.4 | 21.9 | 17.6 | 21.3 | 12.4 | 5.3 | 11.65 | 39.0% | 17.7% |
| ITF_WOMEN | 1,303 | 10.1 | 8.4 | 15.0 | 12.1 | 23.9 | 18.0 | 12.6 | 16.93 | 54.5% | 30.6% |
| WTA | 434 | 20.5 | 5.5 | 16.8 | 15.7 | 22.4 | 16.6 | 2.5 | 12.96 | 41.5% | 19.1% |
| WTA125 | 85 | 5.9 | 5.9 | 15.3 | 21.2 | 25.9 | 15.3 | 10.6 | 15.79 | 51.8% | 25.9% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 62 | 24.2 | 25.8 | 35.5 | 12.9 | 1.6 | 0.0 | 0.0 | 5.45 | 1.6% | 0.0% |
| CHALLENGER | 702 | 23.5 | 16.7 | 28.6 | 15.2 | 13.2 | 2.4 | 0.3 | 6.68 | 16.0% | 2.7% |
| DOUBLES | 345 | 5.8 | 3.8 | 10.1 | 10.4 | 21.7 | 21.2 | 27.0 | 24.1 | 69.9% | 48.1% |
| ITF_MEN | 1,467 | 17.2 | 11.1 | 22.1 | 15.3 | 20.8 | 10.0 | 3.5 | 9.92 | 34.4% | 13.6% |
| ITF_WOMEN | 1,317 | 10.9 | 9.8 | 21.0 | 16.3 | 24.8 | 15.0 | 2.0 | 12.2 | 41.9% | 17.1% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 334 | 15.6 | 9.9 | 26.4 | 23.1 | 18.3 | 6.9 | 0.0 | 9.55 | 25.1% | 6.9% |
| WTA125 | 260 | 15.8 | 10.8 | 25.8 | 20.0 | 21.1 | 6.2 | 0.4 | 9.43 | 27.7% | 6.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 384 | 5.7 | 3.9 | 9.9 | 10.4 | 21.9 | 20.8 | 27.3 | 24.07 | 70.0% | 48.2% |
| singles | 5,773 | 13.7 | 9.9 | 20.6 | 15.0 | 20.4 | 13.4 | 7.1 | 11.8 | 40.8% | 20.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 1,176 | 15.2 | 8.8 | 19.5 | 14.6 | 15.7 | 13.3 | 12.8 | 12.01 | 41.8% | 26.1% |
| Hard | 3,803 | 12.7 | 8.6 | 18.6 | 15.0 | 19.4 | 15.6 | 10.1 | 13.27 | 45.1% | 25.7% |
| UNKNOWN | 383 | 14.1 | 6.0 | 15.1 | 19.3 | 18.5 | 16.4 | 10.4 | 13.49 | 45.4% | 26.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,633 | 17.2 | 10.2 | 20.8 | 14.9 | 17.0 | 11.6 | 8.4 | 10.44 | 37.0% | 20.0% |
| B | 806 | 16.5 | 10.7 | 17.2 | 17.6 | 16.1 | 10.6 | 11.3 | 11.23 | 38.0% | 21.8% |
| C | 876 | 12.6 | 8.7 | 22.4 | 13.0 | 16.3 | 15.6 | 11.4 | 12.62 | 43.4% | 27.1% |
| D | 978 | 11.2 | 7.9 | 17.2 | 14.6 | 20.8 | 15.8 | 12.5 | 14.5 | 49.1% | 28.3% |
| F | 1,069 | 7.8 | 4.4 | 14.1 | 16.4 | 22.5 | 23.1 | 11.7 | 18.31 | 57.3% | 34.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,891 | 18.7 | 12.1 | 25.9 | 16.7 | 16.5 | 6.9 | 3.1 | 8.66 | 26.6% | 10.1% |
| B | 1,021 | 13.5 | 9.7 | 21.4 | 15.9 | 19.7 | 12.4 | 7.4 | 11.66 | 39.6% | 19.9% |
| C | 1,260 | 11.2 | 8.6 | 15.7 | 13.9 | 22.1 | 15.4 | 13.1 | 15.25 | 50.6% | 28.5% |
| D | 943 | 11.3 | 8.2 | 20.5 | 11.9 | 24.2 | 15.3 | 8.7 | 14.24 | 48.1% | 24.0% |
| F | 1,042 | 6.9 | 7.1 | 12.5 | 13.3 | 23.0 | 24.5 | 12.7 | 18.91 | 60.2% | 37.1% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 2,057 | 16.5 | 9.6 | 19.7 | 16.0 | 16.7 | 11.6 | 9.9 | 10.98 | 38.2% | 21.5% |
| LIMITED | 1,240 | 14.5 | 10.5 | 21.6 | 13.5 | 16.1 | 13.7 | 10.2 | 11.28 | 39.9% | 23.9% |
| POOR | 2,065 | 9.5 | 6.0 | 15.5 | 15.5 | 21.9 | 19.6 | 12.0 | 16.53 | 53.4% | 31.5% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 341 | 34.3 | 22.9 | 33.1 | 6.5 | 2.4 | 0.9 | 0.0 | 4.16 | 3.2% | 0.9% |
| GAME_SPREAD | 406 | 19.9 | 16.5 | 37.0 | 16.0 | 8.9 | 1.2 | 0.5 | 6.59 | 10.6% | 1.7% |
| MATCH_WINNER | 6,157 | 13.2 | 9.5 | 20.0 | 14.7 | 20.5 | 13.8 | 8.3 | 12.22 | 42.6% | 22.2% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 1,702 | 21.7 | 13.4 | 30.6 | 17.2 | 13.6 | 2.8 | 0.7 | 7.04 | 17.0% | 3.4% |
| TOTAL_GAMES | 1,132 | 9.9 | 9.4 | 26.5 | 24.9 | 17.0 | 8.0 | 4.4 | 10.66 | 29.3% | 12.4% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 887 | 28.6 | 32.6 | 26.8 | 0.7 | 9.1 | 1.7 | 0.5 | 4.28 | 11.3% | 2.1% |
| GAME_SPREAD | 565 | 36.6 | 15.0 | 25.3 | 17.9 | 2.5 | 1.9 | 0.7 | 4.55 | 5.1% | 2.6% |
| TOTAL_GAMES | 1,364 | 4.5 | 4.5 | 33.1 | 41.3 | 10.3 | 3.1 | 3.2 | 10.72 | 16.6% | 6.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 887 | 26.2 | 16.7 | 33.6 | 8.1 | 9.9 | 4.5 | 1.0 | 5.79 | 15.4% | 5.5% |
| GAME_SPREAD | 565 | 17.5 | 10.3 | 25.5 | 23.2 | 15.9 | 5.1 | 2.5 | 9.56 | 23.5% | 7.6% |
| TOTAL_GAMES | 1,373 | 5.8 | 7.0 | 29.4 | 29.9 | 17.0 | 6.3 | 4.4 | 10.91 | 27.8% | 10.8% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5,362 | 44.4% | 25.9% | 12.99 | 33.4% | 14.4% | 10.05 |
| gen1_elo | 5,362 | 43.3% | 25.1% | 12.49 | 31.7% | 14.2% | 9.51 |
| gen1_sr | 5,362 | 53.1% | 30.9% | 16.19 | 43.4% | 19.7% | 12.87 |
| gen2 | 5,362 | 51.2% | 31.0% | 15.56 | 43.1% | 21.3% | 12.84 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 2,040 | 17.6 | 12.0 | 22.9 | 15.8 | 18.4 | 10.1 | 3.3 | 9.48 | 31.8% | 13.4% |
| STALE | 3,322 | 10.8 | 6.2 | 15.8 | 14.9 | 18.6 | 18.3 | 15.3 | 16.28 | 52.2% | 33.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,334 | 15.2 | 10.5 | 21.8 | 15.9 | 20.0 | 12.0 | 4.6 | 10.71 | 36.7% | 16.7% |
| STALE | 2,823 | 10.8 | 8.4 | 17.8 | 13.2 | 21.0 | 15.9 | 12.8 | 14.82 | 49.7% | 28.7% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 11,519 | 0 | 5374 | 6145 | 30.9 | 217.5 | 1400.4 |
| ge_15pp | 5,008 | 0 | 1871 | 3137 | 38.8 | 512.5 | 1380.4 |
| ge_25pp | 2,754 | 0 | 828 | 1926 | 53.9 | 636.1 | 1380.4 |
| lt_10pp | 4,790 | 0 | 2651 | 2139 | 28.7 | 55.1 | 1201.9 |

Current slate `SL-20261004T051911Z-0dfe4d41`: 228 priced rows, quote age at build {'median': 33.8, 'max': 83.1}, freshness {'STALE': 228}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 151 | 23.8 | 11.9 | 19.2 | 19.9 | 19.9 | 4.6 | 0.7 | 7.69 | 25.2% | 5.3% |
| MARKETS_AGREE | 8 | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.96 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 12 | 0.0 | 0.0 | 8.3 | 50.0 | 41.7 | 0.0 | 0.0 | 14.32 | 41.7% | 0.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 5,362 | 172 (3.2%) | 7.0% | 0.0% | {"EXTERNAL_STALE": 151, "AGREES_WITH_KALSHI": 12, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 2,383 | 43 (1.8%) | 11.6% | 0.0% | {"EXTERNAL_STALE": 38, "AGREES_WITH_KALSHI": 5} |
| fair_v1_ge_25pp | 1,389 | 8 (0.6%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 8} |
| fair_v1_ge_25pp_pregame_clean | 557 | 8 (1.4%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 8} |
| fair_v1_lt_10pp | 2,162 | 93 (4.3%) | 1.1% | 0.0% | {"EXTERNAL_STALE": 83, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1, "AGREES_WITH_KALSHI": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 1,071 | 12.5 | 7.3 | 18.9 | 15.9 | 20.0 | 15.6 | 9.8 | 13.32 | 45.4% | 25.4% |
| 4-10x | 708 | 12.2 | 9.3 | 17.8 | 15.2 | 17.5 | 16.4 | 11.6 | 13.67 | 45.5% | 28.0% |
| <2x | 2,922 | 14.6 | 9.3 | 19.2 | 15.0 | 17.9 | 13.2 | 10.8 | 12.11 | 41.9% | 24.0% |
| >=10x | 661 | 10.7 | 5.6 | 15.4 | 15.3 | 20.0 | 21.8 | 11.2 | 16.24 | 52.9% | 33.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 1,493 | 14.4 | 9.0 | 20.4 | 15.7 | 16.9 | 12.1 | 11.5 | 11.8 | 40.5% | 23.6% |
| 300-1000 | 1,279 | 13.1 | 7.8 | 16.8 | 15.6 | 20.0 | 16.1 | 10.6 | 14.1 | 46.7% | 26.7% |
| <300 | 1,283 | 8.6 | 5.6 | 15.1 | 14.7 | 21.4 | 22.1 | 12.5 | 17.89 | 56.0% | 34.5% |
| >=3000 | 1,307 | 17.2 | 11.2 | 21.4 | 14.8 | 16.1 | 11.0 | 8.3 | 10.05 | 35.4% | 19.4% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 199 | 0.5165 | 0.3843 | 0.4221 | +0.094 | -0.038 | 0.0121 ± 0.0103 |
| ratio 4-10x | 142 | 0.5839 | 0.4465 | 0.4789 | +0.105 | -0.032 | 0.0147 ± 0.0125 |
| ratio <2x | 413 | 0.5342 | 0.4149 | 0.4649 | +0.069 | -0.050 | 0.0105 ± 0.0068 |
| ratio >=10x | 138 | 0.5484 | 0.3885 | 0.4493 | +0.099 | -0.061 | 0.02 ± 0.0154 |
| thinner_sample 1000-3000 | 240 | 0.5399 | 0.4191 | 0.4583 | +0.082 | -0.039 | 0.0088 ± 0.0091 |
| thinner_sample 300-1000 | 253 | 0.5553 | 0.4266 | 0.4704 | +0.085 | -0.044 | 0.0052 ± 0.0091 |
| thinner_sample <300 | 277 | 0.5365 | 0.3781 | 0.4404 | +0.096 | -0.062 | 0.0229 ± 0.0103 |
| thinner_sample >=3000 | 122 | 0.5191 | 0.4227 | 0.4508 | +0.068 | -0.028 | 0.0148 ± 0.01 |
| data_status ADEQUATE | 261 | 0.5293 | 0.4204 | 0.4559 | +0.073 | -0.035 | 0.0077 ± 0.0078 |
| data_status LIMITED | 194 | 0.5575 | 0.4354 | 0.5 | +0.058 | -0.065 | 0.0021 ± 0.0106 |
| data_status POOR | 437 | 0.5393 | 0.3905 | 0.4348 | +0.105 | -0.044 | 0.0209 ± 0.0077 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 148 | 0.1761 | 0.1768 | -0.0007 ± 0.0012 | 0.5249 | 0.5268 | 0.4957 | 0.4813 | 0.4932 | -0.093 ± 0.0376 | -0.01 (3) |
| 3-5 | 92 | 0.1755 | 0.1747 | +0.0009 ± 0.0036 | 0.5322 | 0.5255 | 0.5215 | 0.4805 | 0.4891 | -0.084 ± 0.0466 | 0.02 (1) |
| 5-10 | 188 | 0.2021 | 0.2055 | -0.0034 ± 0.005 | 0.5903 | 0.5982 | 0.5149 | 0.4403 | 0.4947 | -0.046 ± 0.0335 | -0.0167 (3) |
| 10-15 | 154 | 0.2164 | 0.2101 | +0.0063 ± 0.0092 | 0.6163 | 0.6024 | 0.5211 | 0.397 | 0.4351 | -0.067 ± 0.0364 | -0.0633 (3) |
| 15-25 | 192 | 0.2146 | 0.2092 | +0.0053 ± 0.013 | 0.6169 | 0.5995 | 0.563 | 0.3664 | 0.4531 | -0.028 ± 0.0324 | -0.02 (4) |
| 25-40 | 92 | 0.2371 | 0.1839 | +0.0532 ± 0.0276 | 0.6633 | 0.5404 | 0.6174 | 0.304 | 0.3696 | -0.071 ± 0.0424 | -0.01 (1) |
| 40+ | 26 | 0.3509 | 0.1453 | +0.2057 ± 0.0675 | 0.9495 | 0.453 | 0.7195 | 0.2762 | 0.2692 | -0.176 ± 0.0753 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 451 | 0.165 | 0.166 | -0.0011 ± 0.0006 | 0.4963 | 0.499 | 0.5079 | 0.4932 | 0.5322 | -0.023 ± 0.0201 | -0.0188 (8) |
| 3-5 | 277 | 0.1778 | 0.1779 | -0.0001 ± 0.0021 | 0.537 | 0.5306 | 0.4977 | 0.4575 | 0.4801 | -0.036 ± 0.0261 | 0.02 (1) |
| 5-10 | 656 | 0.1858 | 0.1843 | +0.0015 ± 0.0025 | 0.5522 | 0.5467 | 0.474 | 0.4001 | 0.4284 | -0.029 ± 0.0169 | -0.0129 (7) |
| 10-15 | 549 | 0.1952 | 0.1786 | +0.0166 ± 0.0045 | 0.5724 | 0.523 | 0.4746 | 0.3507 | 0.3461 | -0.065 ± 0.0179 | -0.0633 (3) |
| 15-25 | 716 | 0.1938 | 0.1592 | +0.0347 ± 0.0059 | 0.5755 | 0.4722 | 0.4821 | 0.2843 | 0.2933 | -0.049 ± 0.0147 | -0.017 (10) |
| 25-40 | 648 | 0.2126 | 0.096 | +0.1166 ± 0.0076 | 0.6176 | 0.3129 | 0.502 | 0.1877 | 0.162 | -0.072 ± 0.0119 | -0.01 (1) |
| 40+ | 484 | 0.3749 | 0.0343 | +0.3406 ± 0.0091 | 0.9751 | 0.1486 | 0.6196 | 0.1036 | 0.0413 | -0.093 ± 0.0078 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 90 | 0.1786 | 0.1803 | -0.0017 ± 0.0015 | 0.5306 | 0.5331 | 0.5293 | 0.5147 | 0.5667 | -0.038 ± 0.0436 | -0.01 (1) |
| 3-5 | 69 | 0.2103 | 0.2079 | +0.0025 ± 0.0044 | 0.6015 | 0.6024 | 0.4928 | 0.4536 | 0.4348 | -0.091 ± 0.0576 | 0.02 (1) |
| 5-10 | 177 | 0.1858 | 0.1828 | +0.0030 ± 0.0049 | 0.5535 | 0.5449 | 0.5736 | 0.4979 | 0.5085 | -0.092 ± 0.0327 | -0.01 (4) |
| 10-15 | 155 | 0.2236 | 0.2113 | +0.0123 ± 0.0094 | 0.6363 | 0.6093 | 0.5757 | 0.451 | 0.471 | -0.080 ± 0.0379 | -0.0667 (3) |
| 15-25 | 217 | 0.2236 | 0.1964 | +0.0272 ± 0.0119 | 0.6329 | 0.5686 | 0.5845 | 0.3879 | 0.424 | -0.083 ± 0.0307 | -0.0167 (3) |
| 25-40 | 129 | 0.2562 | 0.1974 | +0.0587 ± 0.0242 | 0.7152 | 0.5708 | 0.6564 | 0.3457 | 0.4031 | -0.090 ± 0.0405 | -0.025 (2) |
| 40+ | 55 | 0.3882 | 0.1943 | +0.1940 ± 0.0603 | 1.0783 | 0.5734 | 0.7552 | 0.262 | 0.3273 | -0.061 ± 0.0589 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 363 | 0.1582 | 0.16 | -0.0019 ± 0.0007 | 0.4775 | 0.4825 | 0.5457 | 0.531 | 0.5813 | -0.001 ± 0.0211 | -0.0217 (6) |
| 3-5 | 224 | 0.1771 | 0.1739 | +0.0032 ± 0.0022 | 0.5247 | 0.5225 | 0.5424 | 0.503 | 0.4821 | -0.070 ± 0.0279 | 0.02 (1) |
| 5-10 | 592 | 0.1779 | 0.1775 | +0.0005 ± 0.0027 | 0.5325 | 0.5268 | 0.5217 | 0.4464 | 0.478 | -0.025 ± 0.0174 | -0.01 (5) |
| 10-15 | 533 | 0.1906 | 0.1778 | +0.0128 ± 0.0046 | 0.5648 | 0.5238 | 0.5146 | 0.3905 | 0.409 | -0.039 ± 0.0185 | -0.0575 (4) |
| 15-25 | 763 | 0.2066 | 0.1585 | +0.0481 ± 0.0057 | 0.6017 | 0.4736 | 0.5139 | 0.3176 | 0.2988 | -0.083 ± 0.0144 | -0.0143 (7) |
| 25-40 | 698 | 0.2261 | 0.1195 | +0.1066 ± 0.0083 | 0.6554 | 0.3693 | 0.5454 | 0.23 | 0.2206 | -0.065 ± 0.0133 | -0.015 (6) |
| 40+ | 608 | 0.4088 | 0.0589 | +0.3499 ± 0.0115 | 1.0745 | 0.2158 | 0.664 | 0.1237 | 0.0839 | -0.073 ± 0.0094 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 142 | 0.1838 | 0.1854 | -0.0016 ± 0.0013 | 0.5394 | 0.5437 | 0.5148 | 0.5004 | 0.5282 | -0.055 ± 0.0364 | -0.01 (5) |
| 3-5 | 101 | 0.1706 | 0.1683 | +0.0022 ± 0.0033 | 0.5148 | 0.5094 | 0.5008 | 0.4614 | 0.4554 | -0.108 ± 0.0433 | -- (0) |
| 5-10 | 183 | 0.2072 | 0.2068 | +0.0004 ± 0.005 | 0.6062 | 0.5997 | 0.5056 | 0.4329 | 0.4645 | -0.064 ± 0.0341 | -0.01 (3) |
| 10-15 | 156 | 0.2085 | 0.2049 | +0.0036 ± 0.009 | 0.6028 | 0.591 | 0.5486 | 0.425 | 0.4808 | -0.064 ± 0.0365 | -0.044 (5) |
| 15-25 | 188 | 0.211 | 0.201 | +0.0099 ± 0.0126 | 0.6129 | 0.5825 | 0.5756 | 0.3829 | 0.4521 | -0.044 ± 0.0314 | -0.03 (1) |
| 25-40 | 101 | 0.2341 | 0.1959 | +0.0382 ± 0.0271 | 0.6601 | 0.5706 | 0.6076 | 0.2951 | 0.3861 | -0.052 ± 0.0411 | 0.0 (1) |
| 40+ | 21 | 0.3707 | 0.1604 | +0.2102 ± 0.0791 | 0.9917 | 0.4892 | 0.7365 | 0.2879 | 0.2857 | -0.191 ± 0.0908 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 435 | 0.174 | 0.1741 | -0.0001 ± 0.0007 | 0.5181 | 0.5189 | 0.5097 | 0.4954 | 0.5034 | -0.050 ± 0.0201 | -0.0162 (13) |
| 3-5 | 301 | 0.1792 | 0.1746 | +0.0046 ± 0.0019 | 0.5342 | 0.5214 | 0.4874 | 0.4482 | 0.4153 | -0.092 ± 0.0243 | -0.01 (2) |
| 5-10 | 644 | 0.1921 | 0.186 | +0.0061 ± 0.0026 | 0.5687 | 0.5445 | 0.4685 | 0.3948 | 0.3929 | -0.057 ± 0.0171 | -0.01 (3) |
| 10-15 | 555 | 0.1896 | 0.1752 | +0.0144 ± 0.0044 | 0.5612 | 0.5192 | 0.4835 | 0.3602 | 0.3658 | -0.057 ± 0.0178 | -0.03 (9) |
| 15-25 | 760 | 0.1847 | 0.1487 | +0.0360 ± 0.0056 | 0.557 | 0.4488 | 0.4895 | 0.2911 | 0.2987 | -0.048 ± 0.0137 | -0.03 (2) |
| 25-40 | 634 | 0.2138 | 0.0987 | +0.1151 ± 0.0078 | 0.6201 | 0.3174 | 0.4972 | 0.18 | 0.1593 | -0.070 ± 0.012 | 0.0 (1) |
| 40+ | 452 | 0.3918 | 0.0339 | +0.3578 ± 0.0096 | 1.0213 | 0.1489 | 0.6261 | 0.1031 | 0.0332 | -0.100 ± 0.008 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 425 | 0.2044 | 0.2045 | -0.0000 ± 0.0007 | 0.5913 | 0.5917 | 0.4995 | 0.4848 | 0.4871 | -0.041 ± 0.022 | -0.0226 (46) |
| 3-5 | 310 | 0.1942 | 0.193 | +0.0012 ± 0.002 | 0.5701 | 0.5637 | 0.4628 | 0.423 | 0.4323 | -0.040 ± 0.0248 | -0.0059 (32) |
| 5-10 | 649 | 0.1888 | 0.1841 | +0.0046 ± 0.0025 | 0.5612 | 0.5484 | 0.4612 | 0.3878 | 0.3945 | -0.038 ± 0.0169 | -0.005 (72) |
| 10-15 | 433 | 0.2047 | 0.1928 | +0.0119 ± 0.0053 | 0.5989 | 0.5652 | 0.4589 | 0.3353 | 0.3487 | -0.037 ± 0.021 | 0.0016 (63) |
| 15-25 | 580 | 0.233 | 0.2088 | +0.0242 ± 0.0074 | 0.659 | 0.6039 | 0.5296 | 0.3367 | 0.3707 | -0.029 ± 0.0189 | -0.0216 (58) |
| 25-40 | 275 | 0.2693 | 0.1705 | +0.0988 ± 0.0156 | 0.7437 | 0.5114 | 0.5771 | 0.2659 | 0.2618 | -0.069 ± 0.0245 | -0.0216 (25) |
| 40+ | 94 | 0.4254 | 0.1611 | +0.2643 ± 0.0443 | 1.1952 | 0.4956 | 0.7368 | 0.2289 | 0.2447 | -0.060 ± 0.0429 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 787 | 0.1933 | 0.1927 | +0.0006 ± 0.0005 | 0.5648 | 0.5632 | 0.4929 | 0.4784 | 0.4651 | -0.054 ± 0.0156 | -0.0155 (82) |
| 3-5 | 559 | 0.1975 | 0.1957 | +0.0018 ± 0.0015 | 0.5752 | 0.5679 | 0.4687 | 0.4289 | 0.4275 | -0.046 ± 0.0187 | -0.018 (54) |
| 5-10 | 1188 | 0.1876 | 0.1812 | +0.0064 ± 0.0019 | 0.5582 | 0.5391 | 0.4463 | 0.3723 | 0.3704 | -0.043 ± 0.0124 | -0.0089 (122) |
| 10-15 | 873 | 0.1991 | 0.1853 | +0.0138 ± 0.0036 | 0.5849 | 0.5459 | 0.4495 | 0.3259 | 0.3322 | -0.039 ± 0.0145 | -0.0053 (99) |
| 15-25 | 1222 | 0.2206 | 0.1863 | +0.0344 ± 0.0049 | 0.6364 | 0.5472 | 0.5036 | 0.308 | 0.3175 | -0.041 ± 0.0124 | -0.0255 (106) |
| 25-40 | 832 | 0.2452 | 0.1279 | +0.1173 ± 0.0078 | 0.6918 | 0.4001 | 0.5285 | 0.2133 | 0.1863 | -0.073 ± 0.0122 | -0.0206 (47) |
| 40+ | 494 | 0.3886 | 0.0785 | +0.3102 ± 0.0138 | 1.0617 | 0.2642 | 0.6522 | 0.1364 | 0.1053 | -0.075 ± 0.0128 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 892 | 1.1 ± 0.095 | 1.211 | 0.1712 | 0.1835 | 0.2081 | 0.1952 |
| gen2 | 892 | 0.92 ± 0.084 | 1.141 | 0.1885 | 0.1827 | 0.2254 | 0.1956 |
| gen1_elo | 892 | 1.085 ± 0.093 | 1.19 | 0.1761 | 0.1839 | 0.2073 | 0.1952 |
| gen1_sr | 892 | 1.121 ± 0.109 | 1.209 | 0.1439 | 0.185 | 0.2209 | 0.1951 |
| gen1_ledger | 2766 | 0.885 ± 0.051 | 1.058 | 0.1623 | 0.1992 | 0.2196 | 0.1926 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 5,008)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,659 | 33.1% |
| STALE_QUOTE | market_freshness | 1,478 | 29.5% |
| POOR_DATA | data | 397 | 7.9% |
| BOOK_QUALITY | execution | 337 | 6.7% |
| LIMITED_DATA | data | 317 | 6.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 289 | 5.8% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 252 | 5.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 173 | 3.5% |
| IDENTITY_AMBIGUOUS | mapping | 103 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 3 | 0.1% |

Cause class: coverage 33.1%, market_freshness 29.5%, data 14.3%, market_freshness/coverage 9.2%, execution 6.7%, model_calibration_or_unknown 5.0%, mapping 2.1%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 94.5%, LOW_DATA_QUALITY 63.7%, STALE_KALSHI_QUOTE 62.6%, STALE_PLAYER_DATA 53.4%, THIN_PLAYER_HISTORY 51.6%, MODEL_INTERNAL_DISAGREEMENT 33.4%, ASYMMETRIC_SAMPLE_SIZE 28.4%, WIDE_SPREAD 14.8%, MODEL_HIGH_UNCERTAINTY 14.3%, PLAYER_IDENTITY_RISK 10.8%, LEVEL_TRANSFER_RISK 8.2%, EVENT_MAPPING_RISK 6.5%, LOW_DISPLAYED_LIQUIDITY 5.0%, MODEL_CALIBRATION_OUTLIER 2.1%, UNKNOWN 0.8%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 35.7%, POST_SETTLEMENT_OBSERVATION 33.1%, POSSIBLE_IN_PLAY_QUOTE 6.6%, CONFIRMED_IN_PLAY_QUOTE 1.2%

### >= ge_25 pp (N = 2,754)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,290 | 46.8% |
| STALE_QUOTE | market_freshness | 662 | 24.0% |
| POOR_DATA | data | 168 | 6.1% |
| BOOK_QUALITY | execution | 165 | 6.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 146 | 5.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 102 | 3.7% |
| LIMITED_DATA | data | 86 | 3.1% |
| IDENTITY_AMBIGUOUS | mapping | 75 | 2.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 60 | 2.2% |

Cause class: coverage 46.8%, market_freshness 24.0%, data 9.2%, market_freshness/coverage 9.0%, execution 6.0%, mapping 2.7%, model_calibration_or_unknown 2.2%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 96.8%, STALE_KALSHI_QUOTE 69.9%, LOW_DATA_QUALITY 67.5%, THIN_PLAYER_HISTORY 53.9%, STALE_PLAYER_DATA 51.0%, MODEL_INTERNAL_DISAGREEMENT 34.5%, ASYMMETRIC_SAMPLE_SIZE 30.8%, MODEL_HIGH_UNCERTAINTY 15.7%, PLAYER_IDENTITY_RISK 13.6%, WIDE_SPREAD 13.5%, EVENT_MAPPING_RISK 7.9%, LEVEL_TRANSFER_RISK 7.7%, LOW_DISPLAYED_LIQUIDITY 5.5%, MODEL_CALIBRATION_OUTLIER 3.1%, UNKNOWN 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 49.6%, POST_SETTLEMENT_OBSERVATION 46.8%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 1.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 2348, "IDENTITY_AMBIGUOUS": 406}; ticker orientation: {"VERIFIED": 2754}.

Checks: discipline:AMBIGUOUS 185, discipline:PASS 2569, identity_confidence:AMBIGUOUS 374, identity_confidence:PASS 2380, level_mapping:NA 197, level_mapping:PASS 2557, market_pair:AMBIGUOUS 62, market_pair:NA 77, market_pair:PASS 2615, model_complement:NA 48, model_complement:PASS 2706, namesake:PASS 2754, physical_match_id:NA 1365, physical_match_id:PASS 1389, player_ids:PASS 2754, same_pair_other_event:PASS 2754, ticker_orientation:PASS 2754

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 314 | 4.1% | 4.3% | 0.5% | {"market_freshness": 12, "execution": 1} | 6.16 | 0.1791 / 0.1823 (49) | 39.2% | 0.0% | 0.6% | 3.5% |
| CHALLENGER | 1,855 | 18.4% | 8.1% | 12.4% | {"coverage": 183, "market_freshness": 80, "market_freshness/coverage": 39, "data": 21, "model_calibration_or_unknown": 14, "execution": 4} | 7.65 | 0.2253 / 0.2085 (548) | 51.9% | 4.3% | 0.9% | 21.2% |
| DOUBLES | 384 | 48.2% | 48.1% | 6.7% | {"market_freshness": 106, "execution": 32, "mapping": 28, "market_freshness/coverage": 12, "coverage": 7} | 24.1 | 0.3217 / 0.2283 (162) | 60.9% | 0.0% | 100.0% | 10.2% |
| ITF_MEN | 3,744 | 24.9% | 13.5% | 33.9% | {"coverage": 522, "market_freshness": 167, "data": 88, "execution": 74, "market_freshness/coverage": 72, "mapping": 10, "model_calibration_or_unknown": 1} | 9.73 | 0.2134 / 0.1883 (1329) | 55.3% | 49.0% | 5.1% | 32.6% |
| ITF_WOMEN | 3,849 | 29.2% | 18.1% | 40.8% | {"coverage": 565, "market_freshness": 250, "data": 126, "market_freshness/coverage": 85, "execution": 45, "mapping": 35, "model_calibration_or_unknown": 19} | 12.5 | 0.2066 / 0.1866 (1180) | 58.3% | 54.9% | 7.0% | 31.9% |
| OTHER | 149 | 8.1% | 7.3% | 0.4% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 798 | 9.4% | 8.1% | 2.7% | {"market_freshness": 34, "model_calibration_or_unknown": 12, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.66 | 0.2006 / 0.1964 (129) | 40.5% | 2.6% | 1.5% | 3.8% |
| WTA125 | 426 | 16.2% | 9.0% | 2.5% | {"market_freshness/coverage": 30, "model_calibration_or_unknown": 12, "market_freshness": 11, "data": 8, "coverage": 8} | 10.17 | 0.2261 / 0.2035 (219) | 34.5% | 8.9% | 0.5% | 19.0% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 3 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 4 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 5 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 6 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 7 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 8 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 9 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 10 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 11 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 12 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 14 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 15 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 16 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 17 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 18 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 19 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 20 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 21 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 22 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 23 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 22 min (AGING); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 24 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 25 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 26 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 256 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 27 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 114 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 28 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 29 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 30 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 66 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 31 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 32 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 33 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 34 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 35 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 36 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.9h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 671 min (STALE); no external reference |
| 37 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 183 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 38 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |
| 39 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 40 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 41 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 42 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 43 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 30 min (AGING); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 44 | `KXITFWMATCH-26SEP30KOKUEM-KOK` | ITF_WOMEN | fair_v1 | 79% / 10% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 776 min (STALE); data LIMITED (grade C, thinner serve sample 824.0, ratio 2.35); no external reference |
| 45 | `KXITFMATCH-26SEP20WILRAH-RAH` | ITF_MEN | gen1_ledger | 72% / 4% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade B, thinner serve sample 2782.0, ratio 1.84); no external reference |
| 46 | `KXITFMATCH-26SEP26NAGTHO-NAG` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 89 min (STALE); data LIMITED (grade C, thinner serve sample 1323.0, ratio 4.45); no external reference |
| 47 | `KXITFWMATCH-26SEP26PERPRE-PER` | ITF_WOMEN | gen1_ledger | 78% / 10% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 102 min (STALE); data POOR (grade D, thinner serve sample 1020.0, ratio 2.77); no external reference |
| 48 | `KXITFMATCH-26SEP22YILAGA-AGA` | ITF_MEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 203 min (STALE); data LIMITED (grade B, thinner serve sample 2786.0, ratio 2.08); no external reference |
| 49 | `KXITFMATCH-26SEP30DIMURA-URA` | ITF_MEN | fair_v1 | 71% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.5h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 220 min (STALE); data POOR (grade F, thinner serve sample 174.0, ratio 2.63); no external reference |
| 50 | `KXITFWMATCH-26OCT01TANVED-TAN` | ITF_WOMEN | fair_v1 | 76% / 8% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 167 min (STALE); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9681, "by_level_share_of_ge_25pp": {"ATP": 0.0047, "CHALLENGER": 0.1238, "DOUBLES": 0.0672, "ITF_MEN": 0.3391, "ITF_WOMEN": 0.4085, "OTHER": 0.0044, "WTA": 0.0272, "WTA125": 0.0251}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.6993, "share_primary_cause_market_settled_or_in_play": 0.5584, "share_primary_cause_stale_quote_only": 0.2404}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 2754, "identity_ambiguous_share": 0.1474, "ticker_orientation": {"VERIFIED": 2754}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 1389, "with_external": 8, "coverage": 0.0058, "external_status": {"EXTERNAL_STALE": 8}, "triangulation": {"INSUFFICIENT_INPUTS": 8}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 557, "with_external": 8, "coverage": 0.0144, "external_status": {"EXTERNAL_STALE": 8}, "triangulation": {"INSUFFICIENT_INPUTS": 8}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 824.0, "median_sample_ratio": 2.27, "median_min_matches": 28.0, "median_max_days_since_last": 173.0, "share_severe_asymmetry": 0.1703, "data_status": {"POOR": 1275, "LIMITED": 926, "ADEQUATE": 553}, "comparison_lt_10pp": {"median_thinner_serve_points": 1948.0, "median_sample_ratio": 1.73, "median_min_matches": 78.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 199, "model_minus_observed": 0.0944, "kalshi_minus_observed": -0.0378, "brier_diff_model_minus_kalshi": 0.0121}, "4-10x": {"n": 142, "model_minus_observed": 0.105, "kalshi_minus_observed": -0.0324, "brier_diff_model_minus_kalshi": 0.0147}, "<2x": {"n": 413, "model_minus_observed": 0.0693, "kalshi_minus_observed": -0.05, "brier_diff_model_minus_kalshi": 0.0105}, ">=10x": {"n": 138, "model_minus_observed": 0.0991, "kalshi_minus_observed": -0.0608, "brier_diff_model_minus_kalshi": 0.02}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 892, "model": {"intercept": -0.625, "slope": 0.92, "slope_se": 0.084}, "kalshi_mid_same_rows": {"intercept": 0.19, "slope": 1.141, "slope_se": 0.093}, "mean_extremity_model": 0.1885, "mean_extremity_kalshi": 0.1827, "model_brier": 0.2254, "kalshi_brier": 0.1956, "brier_diff_model_minus_kalshi": 0.0298, "brier_diff_se": 0.0063, "model_logloss": 0.6443, "kalshi_logloss": 0.5706}, "fair_v1": {"n": 892, "model": {"intercept": -0.425, "slope": 1.1, "slope_se": 0.095}, "kalshi_mid_same_rows": {"intercept": 0.314, "slope": 1.211, "slope_se": 0.096}, "mean_extremity_model": 0.1712, "mean_extremity_kalshi": 0.1835, "model_brier": 0.2081, "kalshi_brier": 0.1952, "brier_diff_model_minus_kalshi": 0.013, "brier_diff_se": 0.005, "model_logloss": 0.6017, "kalshi_logloss": 0.5697}, "gen1_elo": {"n": 892, "model": {"intercept": -0.425, "slope": 1.085, "slope_se": 0.093}, "kalshi_mid_same_rows": {"intercept": 0.296, "slope": 1.19, "slope_se": 0.094}, "mean_extremity_model": 0.1761, "mean_extremity_kalshi": 0.1839, "model_brier": 0.2073, "kalshi_brier": 0.1952, "brier_diff_model_minus_kalshi": 0.0121, "brier_diff_se": 0.005, "model_logloss": 0.6012, "kalshi_logloss": 0.5695}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.259, "share_ge_15": 0.4444, "median_abs_gap": 12.99, "n": 5362}, "gen1_elo": {"share_ge_25": 0.2505, "share_ge_15": 0.4334, "median_abs_gap": 12.49, "n": 5362}, "gen1_sr": {"share_ge_25": 0.3087, "share_ge_15": 0.531, "median_abs_gap": 16.19, "n": 5362}, "gen2": {"share_ge_25": 0.3098, "share_ge_15": 0.5125, "median_abs_gap": 15.56, "n": 5362}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1436, "share_ge_15": 0.3335, "median_abs_gap": 10.05, "n": 3880}, "gen1_elo": {"share_ge_25": 0.142, "share_ge_15": 0.3168, "median_abs_gap": 9.51, "n": 3880}, "gen1_sr": {"share_ge_25": 0.1972, "share_ge_15": 0.4335, "median_abs_gap": 12.87, "n": 3880}, "gen2": {"share_ge_25": 0.2131, "share_ge_15": 0.4307, "median_abs_gap": 12.84, "n": 3880}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 6.16, "share_ge_25_all": 0.0414, "share_ge_25_pregame_clean": 0.0429}, "WTA": {"median_abs_gap_pregame_clean": 8.66, "share_ge_25_all": 0.094, "share_ge_25_pregame_clean": 0.0807}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2229, "share_within_10pp_all": 0.4158, "share_within_10pp_pregame_clean": 0.4959, "corr_model_vs_mid_pregame_clean": 0.8303}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 148, "model_brier": 0.1761, "kalshi_brier": 0.1768, "brier_diff_model_minus_kalshi": -0.0007}, "10-15": {"n_settled": 154, "model_brier": 0.2164, "kalshi_brier": 0.2101, "brier_diff_model_minus_kalshi": 0.0063}, "15-25": {"n_settled": 192, "model_brier": 0.2146, "kalshi_brier": 0.2092, "brier_diff_model_minus_kalshi": 0.0053}, "25-40": {"n_settled": 92, "model_brier": 0.2371, "kalshi_brier": 0.1839, "brier_diff_model_minus_kalshi": 0.0532}, "3-5": {"n_settled": 92, "model_brier": 0.1755, "kalshi_brier": 0.1747, "brier_diff_model_minus_kalshi": 0.0009}, "40+": {"n_settled": 26, "model_brier": 0.3509, "kalshi_brier": 0.1453, "brier_diff_model_minus_kalshi": 0.2057}, "5-10": {"n_settled": 188, "model_brier": 0.2021, "kalshi_brier": 0.2055, "brier_diff_model_minus_kalshi": -0.0034}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.556, "slope": 0.885, "slope_se": 0.051}, "kalshi_slope": {"intercept": 0.091, "slope": 1.058, "slope_se": 0.053}, "n": 2766}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 162, "model_brier": 0.3217, "kalshi_brier": 0.2283, "brier_diff_model_minus_kalshi": 0.0934, "brier_diff_se": 0.0257, "corr_model_outcome": -0.0972, "corr_kalshi_outcome": 0.3367}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
