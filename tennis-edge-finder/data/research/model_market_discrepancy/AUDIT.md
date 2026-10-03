# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-03T16:51Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 11,132): 0-3 13.2%, 3-5 8.9%, 5-10 19.3%, 10-15 14.9%, 15-25 19.7%, 25-40 14.3%, 40+ 9.6%; median gap 12.66 pp.
* **Where the extremes live**: 96.7% of >=25 pp gaps are off the ATP/WTA main tour (ITF 74.7%, Challenger 12.1%, doubles 6.9%). Main tour: ATP 4.1% and WTA 9.4% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 2,667): MARKET_ALREADY_SETTLED_WHEN_PRICED 47.5%, STALE_QUOTE 23.6%, POOR_DATA 6.2%, BOOK_QUALITY 5.7%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IN_PLAY_QUOTE 3.8%, LIMITED_DATA 3.0%, IDENTITY_AMBIGUOUS 2.7%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%. By class: coverage 47.5%, market_freshness 23.6%, market_freshness/coverage 9.2%, data 9.2%, execution 5.7%, mapping 2.7%, model_calibration_or_unknown 2.1%.
* **Stale / settled / in-play**: 70.2% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 56.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 2,667 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 14.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.4%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 7.7% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 827.0 points vs 1970.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.096, Gen-2 0.929, Gen-1 ledger 0.883 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 90 model 0.2352 vs Kalshi 0.181; n 26 model 0.3509 vs Kalshi 0.1453.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 35,585 model-market comparisons (61,602 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 16,650 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-03T16:47:06.285330+00:00'], shadow board 10,077 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-03T16:47:10.001786+00:00'], Model 4 2,930 rows, 8,278 settled tickers, 1,795 tickers with an external scan.
* By model: {"gen1_ledger": 9668, "gen1_elo": 5069, "fair_v1": 5069, "gen2": 5069, "gen1_sr": 5069, "model4_fundamental": 2825, "model4_conditioned": 2816}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 11,132 | 13.2 | 8.9 | 19.3 | 14.9 | 19.7 | 14.3 | 9.6 | 12.66 | 43.6% | 24.0% |
| MW fair_v1 | 5,069 | 13.3 | 8.3 | 18.5 | 15.1 | 18.7 | 15.0 | 11.0 | 13.12 | 44.8% | 26.1% |
| MW gen1_elo | 5,069 | 12.9 | 8.7 | 19.8 | 15.0 | 18.2 | 15.1 | 10.3 | 12.53 | 43.6% | 25.4% |
| MW gen1_ledger | 6,063 | 13.2 | 9.4 | 20.0 | 14.7 | 20.4 | 13.8 | 8.4 | 12.23 | 42.6% | 22.2% |
| MW gen1_sr | 5,069 | 9.6 | 6.9 | 16.6 | 13.4 | 22.3 | 18.6 | 12.5 | 16.46 | 53.5% | 31.1% |
| MW gen2 | 5,069 | 11.2 | 6.2 | 16.5 | 14.7 | 20.3 | 17.3 | 13.8 | 15.58 | 51.4% | 31.1% |
| all families model4_conditioned | 2,816 | 18.6 | 15.4 | 29.6 | 23.8 | 8.4 | 2.4 | 1.9 | 7.37 | 12.6% | 4.3% |
| all families model4_fundamental | 2,825 | 14.6 | 10.7 | 29.9 | 21.7 | 14.6 | 5.5 | 3.0 | 9.1 | 23.1% | 8.5% |

Configurable thresholds (primary): >=5pp 77.8%, >=10pp 58.5%, >=15pp 43.6%, >=20pp 33.1%, >=25pp 24.0%, >=30pp 17.7%, >=40pp 9.6%, >=50pp 4.4%
Executable gap (model outside the book, before fees): median 10.32pp; >=10pp 50.8%, >=25pp 21.3%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 242 | 22.3 | 17.4 | 27.3 | 12.8 | 14.9 | 1.6 | 3.7 | 6.19 | 20.2% | 5.4% |
| CHALLENGER | 881 | 14.5 | 9.4 | 15.9 | 16.4 | 15.6 | 15.3 | 12.9 | 13.33 | 43.8% | 28.3% |
| ITF_MEN | 1,637 | 11.8 | 8.3 | 19.8 | 15.1 | 17.6 | 14.7 | 12.7 | 12.81 | 45.0% | 27.4% |
| ITF_WOMEN | 1,790 | 10.4 | 6.2 | 15.6 | 15.1 | 21.7 | 19.1 | 12.0 | 16.12 | 52.7% | 31.0% |
| WTA | 435 | 23.0 | 10.6 | 25.8 | 12.6 | 18.9 | 6.7 | 2.5 | 8.16 | 28.1% | 9.2% |
| WTA125 | 84 | 14.3 | 4.8 | 17.9 | 23.8 | 20.2 | 14.3 | 4.8 | 12.4 | 39.3% | 19.1% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 242 | 23.1 | 12.8 | 24.8 | 16.1 | 17.4 | 1.6 | 4.1 | 7.29 | 23.1% | 5.8% |
| CHALLENGER | 881 | 11.1 | 5.1 | 17.7 | 16.4 | 19.2 | 17.7 | 12.8 | 14.94 | 49.7% | 30.5% |
| ITF_MEN | 1,637 | 9.9 | 6.3 | 17.5 | 15.4 | 20.3 | 16.6 | 14.1 | 15.41 | 50.9% | 30.7% |
| ITF_WOMEN | 1,790 | 8.8 | 6.0 | 13.8 | 12.6 | 20.7 | 20.0 | 18.2 | 18.8 | 58.8% | 38.2% |
| WTA | 435 | 20.5 | 5.5 | 16.8 | 15.6 | 22.3 | 16.8 | 2.5 | 12.98 | 41.6% | 19.3% |
| WTA125 | 84 | 6.0 | 6.0 | 16.7 | 20.2 | 22.6 | 15.5 | 13.1 | 15.56 | 51.2% | 28.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 242 | 28.1 | 12.8 | 28.5 | 10.7 | 9.1 | 7.0 | 3.7 | 6.53 | 19.8% | 10.7% |
| CHALLENGER | 881 | 15.2 | 8.1 | 21.7 | 13.6 | 13.4 | 14.4 | 13.6 | 11.49 | 41.4% | 28.0% |
| ITF_MEN | 1,637 | 10.1 | 9.5 | 18.6 | 16.0 | 18.1 | 15.5 | 12.2 | 13.18 | 45.8% | 27.6% |
| ITF_WOMEN | 1,790 | 9.7 | 6.5 | 16.4 | 14.4 | 23.8 | 18.9 | 10.3 | 16.64 | 53.1% | 29.3% |
| WTA | 435 | 23.4 | 14.0 | 29.4 | 15.6 | 11.5 | 4.4 | 1.6 | 6.99 | 17.5% | 6.0% |
| WTA125 | 84 | 16.7 | 6.0 | 22.6 | 29.8 | 13.1 | 10.7 | 1.2 | 10.92 | 25.0% | 11.9% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 72 | 23.6 | 22.2 | 34.7 | 12.5 | 6.9 | 0.0 | 0.0 | 6.26 | 6.9% | 0.0% |
| CHALLENGER | 813 | 21.2 | 13.9 | 26.6 | 16.0 | 13.3 | 6.5 | 2.6 | 7.45 | 22.4% | 9.1% |
| DOUBLES | 383 | 5.7 | 3.9 | 9.9 | 10.4 | 21.9 | 20.6 | 27.4 | 24.04 | 70.0% | 48.0% |
| ITF_MEN | 2,056 | 14.2 | 9.1 | 18.9 | 14.0 | 20.8 | 13.5 | 9.5 | 12.43 | 43.8% | 23.0% |
| ITF_WOMEN | 1,890 | 8.9 | 8.3 | 17.4 | 14.1 | 24.0 | 18.4 | 8.9 | 15.54 | 51.3% | 27.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 363 | 15.4 | 9.4 | 25.6 | 22.3 | 17.6 | 8.8 | 0.8 | 9.8 | 27.3% | 9.6% |
| WTA125 | 337 | 13.3 | 9.5 | 21.7 | 16.9 | 22.9 | 11.9 | 3.9 | 11.35 | 38.6% | 15.7% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 241 | 22.0 | 17.4 | 27.4 | 12.9 | 14.9 | 1.7 | 3.7 | 6.21 | 20.3% | 5.4% |
| CHALLENGER | 644 | 18.5 | 11.8 | 19.4 | 19.7 | 16.8 | 8.8 | 5.0 | 10.18 | 30.6% | 13.8% |
| ITF_MEN | 1,027 | 15.8 | 11.8 | 24.9 | 16.9 | 17.3 | 9.4 | 3.8 | 9.47 | 30.6% | 13.2% |
| ITF_WOMEN | 1,194 | 14.2 | 8.1 | 18.7 | 17.4 | 23.2 | 13.6 | 4.8 | 12.71 | 41.5% | 18.3% |
| WTA | 434 | 23.0 | 10.6 | 25.8 | 12.7 | 18.9 | 6.5 | 2.5 | 8.16 | 27.9% | 9.0% |
| WTA125 | 81 | 14.8 | 4.9 | 18.5 | 24.7 | 19.8 | 12.3 | 4.9 | 11.65 | 37.0% | 17.3% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 241 | 23.2 | 12.4 | 24.9 | 16.2 | 17.4 | 1.7 | 4.2 | 7.5 | 23.2% | 5.8% |
| CHALLENGER | 644 | 14.0 | 6.5 | 22.4 | 20.0 | 20.5 | 12.6 | 4.0 | 11.83 | 37.1% | 16.6% |
| ITF_MEN | 1,027 | 13.4 | 7.7 | 21.9 | 17.8 | 21.4 | 12.5 | 5.3 | 11.78 | 39.1% | 17.7% |
| ITF_WOMEN | 1,194 | 10.6 | 8.0 | 15.8 | 12.3 | 23.8 | 17.8 | 11.7 | 16.24 | 53.3% | 29.6% |
| WTA | 434 | 20.5 | 5.5 | 16.8 | 15.7 | 22.4 | 16.6 | 2.5 | 12.96 | 41.5% | 19.1% |
| WTA125 | 81 | 6.2 | 6.2 | 16.1 | 21.0 | 23.5 | 16.1 | 11.1 | 15.33 | 50.6% | 27.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 62 | 24.2 | 25.8 | 35.5 | 12.9 | 1.6 | 0.0 | 0.0 | 5.45 | 1.6% | 0.0% |
| CHALLENGER | 662 | 23.6 | 16.3 | 29.5 | 15.7 | 12.4 | 2.4 | 0.1 | 6.68 | 14.9% | 2.6% |
| DOUBLES | 344 | 5.8 | 3.8 | 10.2 | 10.5 | 21.8 | 20.9 | 27.0 | 24.02 | 69.8% | 48.0% |
| ITF_MEN | 1,459 | 17.3 | 11.1 | 22.1 | 15.2 | 20.8 | 9.9 | 3.5 | 9.9 | 34.3% | 13.4% |
| ITF_WOMEN | 1,279 | 11.0 | 9.8 | 21.0 | 16.2 | 25.1 | 14.7 | 2.1 | 12.17 | 41.9% | 16.8% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 334 | 15.6 | 9.9 | 26.4 | 23.1 | 18.3 | 6.9 | 0.0 | 9.55 | 25.1% | 6.9% |
| WTA125 | 259 | 15.8 | 10.4 | 25.9 | 20.1 | 21.2 | 6.2 | 0.4 | 9.54 | 27.8% | 6.6% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 383 | 5.7 | 3.9 | 9.9 | 10.4 | 21.9 | 20.6 | 27.4 | 24.04 | 70.0% | 48.0% |
| singles | 5,680 | 13.7 | 9.8 | 20.7 | 15.0 | 20.3 | 13.3 | 7.2 | 11.81 | 40.8% | 20.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 1,095 | 15.3 | 8.6 | 18.8 | 14.6 | 15.8 | 13.8 | 13.1 | 12.37 | 42.6% | 26.9% |
| Hard | 3,629 | 12.6 | 8.5 | 18.8 | 14.9 | 19.5 | 15.4 | 10.4 | 13.33 | 45.3% | 25.8% |
| UNKNOWN | 345 | 14.8 | 5.8 | 14.2 | 18.8 | 19.7 | 15.4 | 11.3 | 13.77 | 46.4% | 26.7% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,575 | 17.2 | 10.2 | 20.7 | 14.7 | 17.2 | 11.4 | 8.6 | 10.44 | 37.2% | 20.0% |
| B | 736 | 17.0 | 10.6 | 17.0 | 16.9 | 16.2 | 10.6 | 11.8 | 11.5 | 38.6% | 22.4% |
| C | 834 | 12.0 | 8.2 | 22.5 | 13.3 | 16.8 | 15.7 | 11.5 | 12.95 | 44.0% | 27.2% |
| D | 942 | 11.0 | 7.5 | 17.4 | 14.5 | 20.9 | 15.8 | 12.7 | 14.59 | 49.5% | 28.6% |
| F | 982 | 7.6 | 4.5 | 13.5 | 16.6 | 22.6 | 22.8 | 12.3 | 18.45 | 57.7% | 35.1% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,869 | 18.7 | 12.0 | 26.1 | 16.7 | 16.4 | 7.0 | 3.2 | 8.65 | 26.5% | 10.1% |
| B | 1,002 | 13.7 | 9.6 | 21.4 | 16.1 | 19.5 | 12.5 | 7.4 | 11.64 | 39.3% | 19.9% |
| C | 1,250 | 11.2 | 8.4 | 15.8 | 13.8 | 22.2 | 15.4 | 13.2 | 15.33 | 50.8% | 28.6% |
| D | 931 | 11.1 | 8.1 | 20.5 | 11.9 | 24.3 | 15.4 | 8.8 | 14.28 | 48.4% | 24.2% |
| F | 1,011 | 7.0 | 7.1 | 12.2 | 13.3 | 23.1 | 24.2 | 13.0 | 18.91 | 60.3% | 37.2% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 1,960 | 16.5 | 9.5 | 19.7 | 15.8 | 16.8 | 11.6 | 10.1 | 11.0 | 38.5% | 21.6% |
| LIMITED | 1,167 | 14.4 | 10.2 | 21.6 | 13.3 | 16.4 | 13.7 | 10.4 | 11.67 | 40.5% | 24.1% |
| POOR | 1,942 | 9.4 | 5.9 | 15.3 | 15.6 | 22.0 | 19.3 | 12.4 | 16.69 | 53.7% | 31.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 341 | 34.3 | 22.9 | 33.1 | 6.5 | 2.4 | 0.9 | 0.0 | 4.16 | 3.2% | 0.9% |
| GAME_SPREAD | 406 | 19.9 | 16.5 | 37.0 | 16.0 | 8.9 | 1.2 | 0.5 | 6.59 | 10.6% | 1.7% |
| MATCH_WINNER | 6,063 | 13.2 | 9.4 | 20.0 | 14.7 | 20.4 | 13.8 | 8.4 | 12.23 | 42.6% | 22.2% |
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
| fair_v1 | 5,069 | 44.8% | 26.1% | 13.12 | 33.3% | 14.1% | 10.04 |
| gen1_elo | 5,069 | 43.6% | 25.4% | 12.53 | 31.5% | 14.1% | 9.53 |
| gen1_sr | 5,069 | 53.5% | 31.1% | 16.46 | 43.4% | 19.6% | 12.81 |
| gen2 | 5,069 | 51.4% | 31.1% | 15.58 | 42.9% | 21.0% | 12.86 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 1,919 | 17.6 | 12.0 | 23.0 | 15.8 | 18.6 | 9.7 | 3.2 | 9.45 | 31.5% | 13.0% |
| STALE | 3,150 | 10.7 | 6.0 | 15.7 | 14.7 | 18.8 | 18.2 | 15.8 | 16.56 | 52.9% | 34.0% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,284 | 15.2 | 10.4 | 21.9 | 15.9 | 19.9 | 12.0 | 4.6 | 10.71 | 36.5% | 16.7% |
| STALE | 2,779 | 10.9 | 8.3 | 17.7 | 13.2 | 21.1 | 15.8 | 12.9 | 14.87 | 49.8% | 28.7% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 11,132 | 0 | 5203 | 5929 | 31.2 | 218.5 | 1400.4 |
| ge_15pp | 4,855 | 0 | 1805 | 3050 | 39.7 | 513.8 | 1380.4 |
| ge_25pp | 2,667 | 0 | 796 | 1871 | 54.3 | 636.6 | 1380.4 |
| lt_10pp | 4,619 | 0 | 2572 | 2047 | 28.4 | 54.9 | 1201.9 |

Current slate `SL-20261003T165127Z-fef184b8`: 76 priced rows, quote age at build {'median': 27.5, 'max': 52.8}, freshness {'AGING': 60, 'STALE': 16}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 135 | 21.5 | 11.8 | 20.7 | 22.2 | 19.3 | 4.4 | 0.0 | 7.82 | 23.7% | 4.4% |
| MARKETS_AGREE | 8 | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.96 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 12 | 0.0 | 0.0 | 8.3 | 50.0 | 41.7 | 0.0 | 0.0 | 14.32 | 41.7% | 0.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 5,069 | 156 (3.1%) | 7.7% | 0.0% | {"EXTERNAL_STALE": 135, "AGREES_WITH_KALSHI": 12, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 2,270 | 37 (1.6%) | 13.5% | 0.0% | {"EXTERNAL_STALE": 32, "AGREES_WITH_KALSHI": 5} |
| fair_v1_ge_25pp | 1,321 | 6 (0.4%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 6} |
| fair_v1_ge_25pp_pregame_clean | 510 | 6 (1.2%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 6} |
| fair_v1_lt_10pp | 2,032 | 83 (4.1%) | 1.2% | 0.0% | {"EXTERNAL_STALE": 73, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1, "AGREES_WITH_KALSHI": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 998 | 11.9 | 7.1 | 18.6 | 15.5 | 20.1 | 16.2 | 10.4 | 13.77 | 46.8% | 26.7% |
| 4-10x | 674 | 11.9 | 8.8 | 18.2 | 15.6 | 17.7 | 16.3 | 11.6 | 13.67 | 45.6% | 27.9% |
| <2x | 2,798 | 14.7 | 9.2 | 19.1 | 14.8 | 18.2 | 13.1 | 10.9 | 12.14 | 42.1% | 24.0% |
| >=10x | 599 | 10.7 | 5.5 | 15.5 | 15.4 | 20.2 | 20.7 | 12.0 | 16.44 | 52.9% | 32.7% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 1,378 | 14.2 | 8.7 | 20.2 | 15.3 | 17.3 | 12.3 | 12.0 | 12.01 | 41.6% | 24.2% |
| 300-1000 | 1,229 | 12.8 | 7.3 | 16.9 | 15.9 | 20.2 | 16.3 | 10.7 | 14.14 | 47.1% | 26.9% |
| <300 | 1,188 | 8.5 | 5.7 | 15.0 | 14.5 | 21.5 | 21.6 | 13.2 | 18.21 | 56.3% | 34.8% |
| >=3000 | 1,274 | 17.4 | 11.2 | 21.4 | 14.8 | 16.2 | 10.7 | 8.3 | 10.01 | 35.2% | 19.0% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 198 | 0.5178 | 0.3853 | 0.4242 | +0.094 | -0.039 | 0.012 ± 0.0104 |
| ratio 4-10x | 140 | 0.5855 | 0.4495 | 0.4857 | +0.100 | -0.036 | 0.0121 ± 0.0125 |
| ratio <2x | 408 | 0.5338 | 0.4157 | 0.4657 | +0.068 | -0.050 | 0.0106 ± 0.0068 |
| ratio >=10x | 136 | 0.5529 | 0.3918 | 0.4559 | +0.097 | -0.064 | 0.0197 ± 0.0156 |
| thinner_sample 1000-3000 | 237 | 0.5397 | 0.4205 | 0.4599 | +0.080 | -0.039 | 0.0086 ± 0.009 |
| thinner_sample 300-1000 | 251 | 0.5561 | 0.4275 | 0.4701 | +0.086 | -0.043 | 0.0059 ± 0.0092 |
| thinner_sample <300 | 272 | 0.5392 | 0.3807 | 0.4485 | +0.091 | -0.068 | 0.0212 ± 0.0104 |
| thinner_sample >=3000 | 122 | 0.5191 | 0.4227 | 0.4508 | +0.068 | -0.028 | 0.0148 ± 0.01 |
| data_status ADEQUATE | 259 | 0.5284 | 0.4207 | 0.4556 | +0.073 | -0.035 | 0.0079 ± 0.0076 |
| data_status LIMITED | 193 | 0.5584 | 0.4368 | 0.5026 | +0.056 | -0.066 | 0.0015 ± 0.0106 |
| data_status POOR | 430 | 0.5415 | 0.3926 | 0.4395 | +0.102 | -0.047 | 0.0203 ± 0.0078 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 147 | 0.1771 | 0.1778 | -0.0007 ± 0.0012 | 0.5273 | 0.5292 | 0.498 | 0.4835 | 0.4966 | -0.093 ± 0.0378 | -0.01 (3) |
| 3-5 | 92 | 0.1755 | 0.1747 | +0.0009 ± 0.0036 | 0.5322 | 0.5255 | 0.5215 | 0.4805 | 0.4891 | -0.084 ± 0.0466 | 0.02 (1) |
| 5-10 | 187 | 0.2028 | 0.2064 | -0.0036 ± 0.005 | 0.5918 | 0.6002 | 0.5163 | 0.4416 | 0.4973 | -0.045 ± 0.0336 | -0.0167 (3) |
| 10-15 | 151 | 0.2178 | 0.2129 | +0.0049 ± 0.0094 | 0.6192 | 0.6089 | 0.5242 | 0.4002 | 0.4437 | -0.063 ± 0.0371 | -0.0633 (3) |
| 15-25 | 189 | 0.2136 | 0.2094 | +0.0043 ± 0.013 | 0.6146 | 0.5999 | 0.5626 | 0.3664 | 0.455 | -0.025 ± 0.0324 | -0.02 (4) |
| 25-40 | 90 | 0.2352 | 0.181 | +0.0542 ± 0.0277 | 0.6592 | 0.5337 | 0.6174 | 0.3041 | 0.3667 | -0.077 ± 0.0423 | -0.01 (1) |
| 40+ | 26 | 0.3509 | 0.1453 | +0.2057 ± 0.0675 | 0.9495 | 0.453 | 0.7195 | 0.2762 | 0.2692 | -0.176 ± 0.0753 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 447 | 0.1662 | 0.1673 | -0.0011 ± 0.0007 | 0.4991 | 0.5018 | 0.508 | 0.4932 | 0.5324 | -0.023 ± 0.0203 | -0.0188 (8) |
| 3-5 | 277 | 0.1778 | 0.1779 | -0.0001 ± 0.0021 | 0.537 | 0.5306 | 0.4977 | 0.4575 | 0.4801 | -0.036 ± 0.0261 | 0.02 (1) |
| 5-10 | 648 | 0.1868 | 0.1857 | +0.0011 ± 0.0025 | 0.5543 | 0.5498 | 0.4751 | 0.4012 | 0.4321 | -0.027 ± 0.0171 | -0.0129 (7) |
| 10-15 | 531 | 0.1967 | 0.1816 | +0.0151 ± 0.0046 | 0.5754 | 0.5296 | 0.4784 | 0.3544 | 0.3559 | -0.060 ± 0.0183 | -0.0633 (3) |
| 15-25 | 700 | 0.1936 | 0.1591 | +0.0346 ± 0.006 | 0.5748 | 0.4719 | 0.4816 | 0.2841 | 0.2929 | -0.049 ± 0.0148 | -0.017 (10) |
| 25-40 | 631 | 0.2123 | 0.0945 | +0.1179 ± 0.0077 | 0.6172 | 0.3098 | 0.5026 | 0.1882 | 0.1601 | -0.075 ± 0.0119 | -0.01 (1) |
| 40+ | 470 | 0.3724 | 0.0347 | +0.3377 ± 0.0093 | 0.97 | 0.1492 | 0.618 | 0.1032 | 0.0426 | -0.092 ± 0.008 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 89 | 0.1802 | 0.1819 | -0.0017 ± 0.0015 | 0.534 | 0.5367 | 0.533 | 0.5183 | 0.573 | -0.036 ± 0.044 | -0.01 (1) |
| 3-5 | 68 | 0.2129 | 0.2106 | +0.0023 ± 0.0045 | 0.6073 | 0.6089 | 0.4972 | 0.4582 | 0.4412 | -0.089 ± 0.0584 | 0.02 (1) |
| 5-10 | 175 | 0.1872 | 0.1837 | +0.0034 ± 0.005 | 0.5569 | 0.547 | 0.5713 | 0.4955 | 0.5029 | -0.096 ± 0.033 | -0.01 (4) |
| 10-15 | 155 | 0.2236 | 0.2113 | +0.0123 ± 0.0094 | 0.6363 | 0.6093 | 0.5757 | 0.451 | 0.471 | -0.080 ± 0.0379 | -0.0667 (3) |
| 15-25 | 215 | 0.2244 | 0.1966 | +0.0278 ± 0.012 | 0.6344 | 0.5691 | 0.5854 | 0.3887 | 0.4233 | -0.085 ± 0.0308 | -0.0167 (3) |
| 25-40 | 126 | 0.253 | 0.1958 | +0.0573 ± 0.0243 | 0.7065 | 0.5672 | 0.6571 | 0.3465 | 0.4048 | -0.089 ± 0.0404 | -0.025 (2) |
| 40+ | 54 | 0.3802 | 0.1959 | +0.1843 ± 0.0606 | 1.0546 | 0.5767 | 0.7524 | 0.2608 | 0.3333 | -0.055 ± 0.0597 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 354 | 0.1612 | 0.1632 | -0.0021 ± 0.0007 | 0.4841 | 0.4897 | 0.5546 | 0.54 | 0.596 | +0.005 ± 0.0216 | -0.0217 (6) |
| 3-5 | 221 | 0.1785 | 0.1753 | +0.0032 ± 0.0022 | 0.5277 | 0.5256 | 0.5445 | 0.5052 | 0.4842 | -0.070 ± 0.0282 | 0.02 (1) |
| 5-10 | 582 | 0.1799 | 0.179 | +0.0009 ± 0.0027 | 0.537 | 0.53 | 0.5178 | 0.4425 | 0.4708 | -0.029 ± 0.0176 | -0.01 (5) |
| 10-15 | 530 | 0.191 | 0.1778 | +0.0132 ± 0.0046 | 0.5658 | 0.524 | 0.5148 | 0.3907 | 0.4075 | -0.041 ± 0.0185 | -0.0575 (4) |
| 15-25 | 746 | 0.2083 | 0.1593 | +0.0489 ± 0.0058 | 0.6053 | 0.476 | 0.5161 | 0.32 | 0.2989 | -0.086 ± 0.0146 | -0.0143 (7) |
| 25-40 | 682 | 0.2241 | 0.1177 | +0.1064 ± 0.0084 | 0.6504 | 0.365 | 0.5451 | 0.2295 | 0.2199 | -0.065 ± 0.0133 | -0.015 (6) |
| 40+ | 589 | 0.4034 | 0.0597 | +0.3437 ± 0.0117 | 1.0587 | 0.2174 | 0.6614 | 0.123 | 0.0866 | -0.070 ± 0.0097 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 141 | 0.1849 | 0.1865 | -0.0016 ± 0.0013 | 0.5419 | 0.5463 | 0.5173 | 0.5028 | 0.5319 | -0.054 ± 0.0367 | -0.01 (5) |
| 3-5 | 101 | 0.1706 | 0.1683 | +0.0022 ± 0.0033 | 0.5148 | 0.5094 | 0.5008 | 0.4614 | 0.4554 | -0.108 ± 0.0433 | -- (0) |
| 5-10 | 181 | 0.2073 | 0.2075 | -0.0002 ± 0.0051 | 0.6065 | 0.6013 | 0.5066 | 0.4339 | 0.4696 | -0.058 ± 0.0341 | -0.01 (3) |
| 10-15 | 154 | 0.2102 | 0.2073 | +0.0030 ± 0.0092 | 0.6065 | 0.5965 | 0.5522 | 0.4285 | 0.487 | -0.062 ± 0.037 | -0.044 (5) |
| 15-25 | 185 | 0.2115 | 0.2016 | +0.0099 ± 0.0128 | 0.6139 | 0.5837 | 0.5767 | 0.3837 | 0.4541 | -0.044 ± 0.0317 | -0.03 (1) |
| 25-40 | 99 | 0.2331 | 0.1935 | +0.0396 ± 0.0272 | 0.658 | 0.5651 | 0.608 | 0.2951 | 0.3838 | -0.057 ± 0.0411 | 0.0 (1) |
| 40+ | 21 | 0.3707 | 0.1604 | +0.2102 ± 0.0791 | 0.9917 | 0.4892 | 0.7365 | 0.2879 | 0.2857 | -0.191 ± 0.0908 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 430 | 0.1756 | 0.1757 | -0.0001 ± 0.0007 | 0.5218 | 0.5226 | 0.5092 | 0.4948 | 0.5023 | -0.051 ± 0.0203 | -0.0162 (13) |
| 3-5 | 301 | 0.1792 | 0.1746 | +0.0046 ± 0.0019 | 0.5342 | 0.5214 | 0.4874 | 0.4482 | 0.4153 | -0.092 ± 0.0243 | -0.01 (2) |
| 5-10 | 637 | 0.1926 | 0.187 | +0.0056 ± 0.0026 | 0.5699 | 0.5467 | 0.4698 | 0.3961 | 0.3972 | -0.053 ± 0.0172 | -0.01 (3) |
| 10-15 | 541 | 0.1914 | 0.1775 | +0.0139 ± 0.0045 | 0.5652 | 0.5246 | 0.4875 | 0.3639 | 0.3715 | -0.056 ± 0.0181 | -0.03 (9) |
| 15-25 | 738 | 0.1852 | 0.1493 | +0.0359 ± 0.0057 | 0.558 | 0.4499 | 0.4904 | 0.2917 | 0.3008 | -0.048 ± 0.0139 | -0.03 (2) |
| 25-40 | 614 | 0.213 | 0.0973 | +0.1157 ± 0.0079 | 0.6185 | 0.3142 | 0.497 | 0.1797 | 0.158 | -0.072 ± 0.0121 | 0.0 (1) |
| 40+ | 443 | 0.3904 | 0.0345 | +0.3559 ± 0.0097 | 1.0186 | 0.1504 | 0.6253 | 0.1037 | 0.0339 | -0.100 ± 0.0082 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 424 | 0.2049 | 0.2049 | -0.0000 ± 0.0007 | 0.5922 | 0.5927 | 0.5002 | 0.4856 | 0.4882 | -0.040 ± 0.0221 | -0.0226 (46) |
| 3-5 | 310 | 0.1942 | 0.193 | +0.0012 ± 0.002 | 0.5701 | 0.5637 | 0.4628 | 0.423 | 0.4323 | -0.040 ± 0.0248 | -0.0059 (32) |
| 5-10 | 649 | 0.1888 | 0.1841 | +0.0046 ± 0.0025 | 0.5612 | 0.5484 | 0.4612 | 0.3878 | 0.3945 | -0.038 ± 0.0169 | -0.005 (72) |
| 10-15 | 430 | 0.2051 | 0.1936 | +0.0115 ± 0.0053 | 0.5998 | 0.567 | 0.4595 | 0.3359 | 0.3512 | -0.036 ± 0.0211 | 0.0016 (63) |
| 15-25 | 577 | 0.2335 | 0.2092 | +0.0243 ± 0.0074 | 0.66 | 0.6049 | 0.53 | 0.3371 | 0.3709 | -0.029 ± 0.019 | -0.0216 (58) |
| 25-40 | 274 | 0.2689 | 0.1707 | +0.0982 ± 0.0156 | 0.7429 | 0.5118 | 0.577 | 0.2657 | 0.2628 | -0.068 ± 0.0246 | -0.0216 (25) |
| 40+ | 94 | 0.4254 | 0.1611 | +0.2643 ± 0.0443 | 1.1952 | 0.4956 | 0.7368 | 0.2289 | 0.2447 | -0.060 ± 0.0429 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 783 | 0.1941 | 0.1936 | +0.0005 ± 0.0005 | 0.5667 | 0.5651 | 0.4945 | 0.48 | 0.4674 | -0.053 ± 0.0157 | -0.0155 (82) |
| 3-5 | 559 | 0.1975 | 0.1957 | +0.0018 ± 0.0015 | 0.5752 | 0.5679 | 0.4687 | 0.4289 | 0.4275 | -0.046 ± 0.0187 | -0.018 (54) |
| 5-10 | 1186 | 0.1878 | 0.1815 | +0.0063 ± 0.0019 | 0.5586 | 0.5396 | 0.4466 | 0.3726 | 0.371 | -0.043 ± 0.0125 | -0.0089 (122) |
| 10-15 | 867 | 0.1996 | 0.1862 | +0.0134 ± 0.0037 | 0.586 | 0.5479 | 0.4503 | 0.3267 | 0.3345 | -0.038 ± 0.0145 | -0.0053 (99) |
| 15-25 | 1206 | 0.2214 | 0.1871 | +0.0343 ± 0.0049 | 0.638 | 0.5491 | 0.5041 | 0.3086 | 0.3184 | -0.041 ± 0.0125 | -0.0255 (106) |
| 25-40 | 827 | 0.2447 | 0.1281 | +0.1165 ± 0.0078 | 0.6908 | 0.4006 | 0.5283 | 0.2131 | 0.1874 | -0.071 ± 0.0123 | -0.0206 (47) |
| 40+ | 493 | 0.3885 | 0.0786 | +0.3098 ± 0.0138 | 1.0614 | 0.2646 | 0.6521 | 0.1365 | 0.1055 | -0.075 ± 0.0129 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 882 | 1.096 ± 0.095 | 1.206 | 0.1712 | 0.1831 | 0.2082 | 0.1957 |
| gen2 | 882 | 0.929 ± 0.085 | 1.134 | 0.188 | 0.1822 | 0.2252 | 0.1961 |
| gen1_elo | 882 | 1.075 ± 0.093 | 1.185 | 0.1763 | 0.1834 | 0.2077 | 0.1957 |
| gen1_sr | 882 | 1.123 ± 0.11 | 1.202 | 0.1436 | 0.1846 | 0.2208 | 0.1956 |
| gen1_ledger | 2758 | 0.883 ± 0.051 | 1.055 | 0.1623 | 0.1991 | 0.2198 | 0.1929 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 4,855)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,633 | 33.6% |
| STALE_QUOTE | market_freshness | 1,417 | 29.2% |
| POOR_DATA | data | 388 | 8.0% |
| BOOK_QUALITY | execution | 318 | 6.6% |
| LIMITED_DATA | data | 301 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 287 | 5.9% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 242 | 5.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 169 | 3.5% |
| IDENTITY_AMBIGUOUS | mapping | 97 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 3 | 0.1% |

Cause class: coverage 33.6%, market_freshness 29.2%, data 14.2%, market_freshness/coverage 9.4%, execution 6.6%, model_calibration_or_unknown 5.0%, mapping 2.0%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 94.3%, LOW_DATA_QUALITY 63.8%, STALE_KALSHI_QUOTE 62.8%, STALE_PLAYER_DATA 53.7%, THIN_PLAYER_HISTORY 51.5%, MODEL_INTERNAL_DISAGREEMENT 32.9%, ASYMMETRIC_SAMPLE_SIZE 28.0%, WIDE_SPREAD 14.7%, MODEL_HIGH_UNCERTAINTY 13.9%, PLAYER_IDENTITY_RISK 10.7%, LEVEL_TRANSFER_RISK 8.3%, EVENT_MAPPING_RISK 6.7%, LOW_DISPLAYED_LIQUIDITY 4.9%, MODEL_CALIBRATION_OUTLIER 2.2%, UNKNOWN 0.8%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.2%, POST_SETTLEMENT_OBSERVATION 33.6%, POSSIBLE_IN_PLAY_QUOTE 6.7%, CONFIRMED_IN_PLAY_QUOTE 1.2%

### >= ge_25 pp (N = 2,667)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,268 | 47.5% |
| STALE_QUOTE | market_freshness | 629 | 23.6% |
| POOR_DATA | data | 166 | 6.2% |
| BOOK_QUALITY | execution | 152 | 5.7% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 144 | 5.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 102 | 3.8% |
| LIMITED_DATA | data | 79 | 3.0% |
| IDENTITY_AMBIGUOUS | mapping | 71 | 2.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 56 | 2.1% |

Cause class: coverage 47.5%, market_freshness 23.6%, market_freshness/coverage 9.2%, data 9.2%, execution 5.7%, mapping 2.7%, model_calibration_or_unknown 2.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 96.7%, STALE_KALSHI_QUOTE 70.2%, LOW_DATA_QUALITY 67.5%, THIN_PLAYER_HISTORY 53.8%, STALE_PLAYER_DATA 51.3%, MODEL_INTERNAL_DISAGREEMENT 33.8%, ASYMMETRIC_SAMPLE_SIZE 30.3%, MODEL_HIGH_UNCERTAINTY 15.3%, PLAYER_IDENTITY_RISK 13.4%, WIDE_SPREAD 13.3%, EVENT_MAPPING_RISK 8.1%, LEVEL_TRANSFER_RISK 7.7%, LOW_DISPLAYED_LIQUIDITY 5.4%, MODEL_CALIBRATION_OUTLIER 3.1%, UNKNOWN 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 50.4%, POST_SETTLEMENT_OBSERVATION 47.5%, POSSIBLE_IN_PLAY_QUOTE 6.3%, CONFIRMED_IN_PLAY_QUOTE 1.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 2279, "IDENTITY_AMBIGUOUS": 388}; ticker orientation: {"VERIFIED": 2667}.

Checks: discipline:AMBIGUOUS 184, discipline:PASS 2483, identity_confidence:AMBIGUOUS 356, identity_confidence:PASS 2311, level_mapping:NA 196, level_mapping:PASS 2471, market_pair:AMBIGUOUS 62, market_pair:NA 75, market_pair:PASS 2530, model_complement:NA 46, model_complement:PASS 2621, namesake:PASS 2667, physical_match_id:NA 1346, physical_match_id:PASS 1321, player_ids:PASS 2667, same_pair_other_event:PASS 2667, ticker_orientation:PASS 2667

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 314 | 4.1% | 4.3% | 0.5% | {"market_freshness": 12, "execution": 1} | 6.16 | 0.1791 / 0.1823 (49) | 39.2% | 0.0% | 0.6% | 3.5% |
| CHALLENGER | 1,694 | 19.1% | 8.1% | 12.1% | {"coverage": 178, "market_freshness": 74, "market_freshness/coverage": 39, "data": 17, "model_calibration_or_unknown": 12, "execution": 3} | 7.83 | 0.2253 / 0.2085 (548) | 52.1% | 3.9% | 0.7% | 22.9% |
| DOUBLES | 383 | 48.0% | 48.0% | 6.9% | {"market_freshness": 106, "execution": 32, "mapping": 27, "market_freshness/coverage": 12, "coverage": 7} | 24.02 | 0.3217 / 0.2283 (162) | 61.1% | 0.0% | 100.0% | 10.2% |
| ITF_MEN | 3,693 | 24.9% | 13.4% | 34.5% | {"coverage": 516, "market_freshness": 163, "data": 87, "market_freshness/coverage": 72, "execution": 71, "mapping": 10, "model_calibration_or_unknown": 1} | 9.73 | 0.2137 / 0.1889 (1323) | 55.3% | 49.0% | 5.2% | 32.7% |
| ITF_WOMEN | 3,680 | 29.1% | 17.5% | 40.2% | {"coverage": 554, "market_freshness": 227, "data": 122, "market_freshness/coverage": 83, "execution": 36, "mapping": 32, "model_calibration_or_unknown": 17} | 12.49 | 0.2066 / 0.1869 (1168) | 58.1% | 53.9% | 6.3% | 32.8% |
| OTHER | 149 | 8.1% | 7.3% | 0.4% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 798 | 9.4% | 8.1% | 2.8% | {"market_freshness": 34, "model_calibration_or_unknown": 12, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.66 | 0.2006 / 0.1964 (129) | 40.5% | 2.6% | 1.5% | 3.8% |
| WTA125 | 421 | 16.4% | 9.1% | 2.6% | {"market_freshness/coverage": 30, "model_calibration_or_unknown": 12, "market_freshness": 11, "data": 8, "coverage": 8} | 10.39 | 0.2261 / 0.2035 (219) | 34.4% | 9.0% | 0.5% | 19.2% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 3 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 4 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 5 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 6 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 8 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
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
| 19 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 110 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 20 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 21 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 22 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 23 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 24 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 25 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 26 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 230 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 27 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 687 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 28 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 29 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 30 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 66 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 31 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 32 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 33 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 34 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 35 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 36 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 114 min (STALE); data LIMITED (grade B, thinner serve sample 2163.0, ratio 2.0); no external reference |
| 37 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 407 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 38 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |
| 39 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 40 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 41 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 42 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 43 | `KXITFWMATCH-26SEP30KOKUEM-KOK` | ITF_WOMEN | fair_v1 | 79% / 10% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 86 min (STALE); data LIMITED (grade C, thinner serve sample 824.0, ratio 2.35); no external reference |
| 44 | `KXITFMATCH-26SEP20WILRAH-RAH` | ITF_MEN | gen1_ledger | 72% / 4% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade B, thinner serve sample 2782.0, ratio 1.84); no external reference |
| 45 | `KXITFMATCH-26SEP26NAGTHO-NAG` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 89 min (STALE); data LIMITED (grade C, thinner serve sample 1323.0, ratio 4.45); no external reference |
| 46 | `KXITFWMATCH-26SEP26PERPRE-PER` | ITF_WOMEN | gen1_ledger | 78% / 10% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 102 min (STALE); data POOR (grade D, thinner serve sample 1020.0, ratio 2.77); no external reference |
| 47 | `KXITFMATCH-26SEP22YILAGA-AGA` | ITF_MEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 203 min (STALE); data LIMITED (grade B, thinner serve sample 2786.0, ratio 2.08); no external reference |
| 48 | `KXITFMATCH-26SEP30DIMURA-URA` | ITF_MEN | fair_v1 | 71% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.5h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 819 min (STALE); data POOR (grade F, thinner serve sample 174.0, ratio 2.63); no external reference |
| 49 | `KXITFWMATCH-26OCT01TANVED-TAN` | ITF_WOMEN | fair_v1 | 76% / 8% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 8.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 492 min (STALE); no external reference |
| 50 | `KXITFWMATCH-26SEP20LLIBON-BON` | ITF_WOMEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 69 min (STALE); data POOR (grade D, thinner serve sample 1210.0, ratio 3.0); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9671, "by_level_share_of_ge_25pp": {"ATP": 0.0049, "CHALLENGER": 0.1211, "DOUBLES": 0.069, "ITF_MEN": 0.345, "ITF_WOMEN": 0.4016, "OTHER": 0.0045, "WTA": 0.0281, "WTA125": 0.0259}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.7015, "share_primary_cause_market_settled_or_in_play": 0.5676, "share_primary_cause_stale_quote_only": 0.2358}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 2667, "identity_ambiguous_share": 0.1455, "ticker_orientation": {"VERIFIED": 2667}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 1321, "with_external": 6, "coverage": 0.0045, "external_status": {"EXTERNAL_STALE": 6}, "triangulation": {"INSUFFICIENT_INPUTS": 6}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 510, "with_external": 6, "coverage": 0.0118, "external_status": {"EXTERNAL_STALE": 6}, "triangulation": {"INSUFFICIENT_INPUTS": 6}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 827.0, "median_sample_ratio": 2.25, "median_min_matches": 28.0, "median_max_days_since_last": 172.0, "share_severe_asymmetry": 0.1642, "data_status": {"POOR": 1228, "LIMITED": 904, "ADEQUATE": 535}, "comparison_lt_10pp": {"median_thinner_serve_points": 1970.0, "median_sample_ratio": 1.71, "median_min_matches": 80.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 198, "model_minus_observed": 0.0936, "kalshi_minus_observed": -0.039, "brier_diff_model_minus_kalshi": 0.012}, "4-10x": {"n": 140, "model_minus_observed": 0.0998, "kalshi_minus_observed": -0.0362, "brier_diff_model_minus_kalshi": 0.0121}, "<2x": {"n": 408, "model_minus_observed": 0.0681, "kalshi_minus_observed": -0.05, "brier_diff_model_minus_kalshi": 0.0106}, ">=10x": {"n": 136, "model_minus_observed": 0.097, "kalshi_minus_observed": -0.0641, "brier_diff_model_minus_kalshi": 0.0197}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 882, "model": {"intercept": -0.626, "slope": 0.929, "slope_se": 0.085}, "kalshi_mid_same_rows": {"intercept": 0.187, "slope": 1.134, "slope_se": 0.093}, "mean_extremity_model": 0.188, "mean_extremity_kalshi": 0.1822, "model_brier": 0.2252, "kalshi_brier": 0.1961, "brier_diff_model_minus_kalshi": 0.0291, "brier_diff_se": 0.0063, "model_logloss": 0.6432, "kalshi_logloss": 0.5718}, "fair_v1": {"n": 882, "model": {"intercept": -0.415, "slope": 1.096, "slope_se": 0.095}, "kalshi_mid_same_rows": {"intercept": 0.318, "slope": 1.206, "slope_se": 0.097}, "mean_extremity_model": 0.1712, "mean_extremity_kalshi": 0.1831, "model_brier": 0.2082, "kalshi_brier": 0.1957, "brier_diff_model_minus_kalshi": 0.0126, "brier_diff_se": 0.005, "model_logloss": 0.6018, "kalshi_logloss": 0.5709}, "gen1_elo": {"n": 882, "model": {"intercept": -0.414, "slope": 1.075, "slope_se": 0.093}, "kalshi_mid_same_rows": {"intercept": 0.3, "slope": 1.185, "slope_se": 0.095}, "mean_extremity_model": 0.1763, "mean_extremity_kalshi": 0.1834, "model_brier": 0.2077, "kalshi_brier": 0.1957, "brier_diff_model_minus_kalshi": 0.012, "brier_diff_se": 0.005, "model_logloss": 0.6022, "kalshi_logloss": 0.5707}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2606, "share_ge_15": 0.4478, "median_abs_gap": 13.12, "n": 5069}, "gen1_elo": {"share_ge_25": 0.2535, "share_ge_15": 0.4358, "median_abs_gap": 12.53, "n": 5069}, "gen1_sr": {"share_ge_25": 0.3115, "share_ge_15": 0.5346, "median_abs_gap": 16.46, "n": 5069}, "gen2": {"share_ge_25": 0.3109, "share_ge_15": 0.5139, "median_abs_gap": 15.58, "n": 5069}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1408, "share_ge_15": 0.3333, "median_abs_gap": 10.04, "n": 3621}, "gen1_elo": {"share_ge_25": 0.1414, "share_ge_15": 0.3151, "median_abs_gap": 9.53, "n": 3621}, "gen1_sr": {"share_ge_25": 0.1964, "share_ge_15": 0.4344, "median_abs_gap": 12.81, "n": 3621}, "gen2": {"share_ge_25": 0.2102, "share_ge_15": 0.4294, "median_abs_gap": 12.86, "n": 3621}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 6.16, "share_ge_25_all": 0.0414, "share_ge_25_pregame_clean": 0.0429}, "WTA": {"median_abs_gap_pregame_clean": 8.66, "share_ge_25_all": 0.094, "share_ge_25_pregame_clean": 0.0807}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2218, "share_within_10pp_all": 0.4149, "share_within_10pp_pregame_clean": 0.4965, "corr_model_vs_mid_pregame_clean": 0.8281}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 147, "model_brier": 0.1771, "kalshi_brier": 0.1778, "brier_diff_model_minus_kalshi": -0.0007}, "10-15": {"n_settled": 151, "model_brier": 0.2178, "kalshi_brier": 0.2129, "brier_diff_model_minus_kalshi": 0.0049}, "15-25": {"n_settled": 189, "model_brier": 0.2136, "kalshi_brier": 0.2094, "brier_diff_model_minus_kalshi": 0.0043}, "25-40": {"n_settled": 90, "model_brier": 0.2352, "kalshi_brier": 0.181, "brier_diff_model_minus_kalshi": 0.0542}, "3-5": {"n_settled": 92, "model_brier": 0.1755, "kalshi_brier": 0.1747, "brier_diff_model_minus_kalshi": 0.0009}, "40+": {"n_settled": 26, "model_brier": 0.3509, "kalshi_brier": 0.1453, "brier_diff_model_minus_kalshi": 0.2057}, "5-10": {"n_settled": 187, "model_brier": 0.2028, "kalshi_brier": 0.2064, "brier_diff_model_minus_kalshi": -0.0036}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.553, "slope": 0.883, "slope_se": 0.051}, "kalshi_slope": {"intercept": 0.092, "slope": 1.055, "slope_se": 0.053}, "n": 2758}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 162, "model_brier": 0.3217, "kalshi_brier": 0.2283, "brier_diff_model_minus_kalshi": 0.0934, "brier_diff_se": 0.0257, "corr_model_outcome": -0.0972, "corr_kalshi_outcome": 0.3367}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
