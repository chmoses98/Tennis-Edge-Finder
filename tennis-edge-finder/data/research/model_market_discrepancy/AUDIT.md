# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-09T06:45Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 26,467): 0-3 14.3%, 3-5 9.6%, 5-10 19.9%, 10-15 15.5%, 15-25 18.6%, 25-40 13.8%, 40+ 8.4%; median gap 11.92 pp.
* **Where the extremes live**: 98.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.8%, Challenger 12.1%, doubles 7.0%). Main tour: ATP 1.6% and WTA 7.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 5,882): MARKET_ALREADY_SETTLED_WHEN_PRICED 39.3%, STALE_QUOTE 17.0%, BOOK_QUALITY 16.8%, POOR_DATA 8.0%, POSSIBLY_IN_PLAY_QUOTE 5.5%, LIMITED_DATA 4.4%, IDENTITY_AMBIGUOUS 3.6%, IN_PLAY_QUOTE 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 1.8%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.3%. By class: coverage 39.3%, market_freshness 17.0%, execution 16.8%, data 12.3%, market_freshness/coverage 8.9%, mapping 3.6%, model_calibration_or_unknown 1.8%, model_calibration 0.3%.
* **Stale / settled / in-play**: 55.2% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 48.2% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 5,882 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 17.3% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 2.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 16.4% of the time and with the model 0.3%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 625.0 points vs 1798.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.098, Gen-2 0.87, Gen-1 ledger 0.92 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 244 model 0.2172 vs Kalshi 0.201; n 53 model 0.2878 vs Kalshi 0.1771.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 101,760 model-market comparisons (169,230 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 38,521 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-09T06:38:19.344684+00:00'], shadow board 27,634 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-09T06:38:22.808691+00:00'], Model 4 10,819 rows, 11,268 settled tickers, 3,094 tickers with an external scan.
* By model: {"gen1_ledger": 24877, "gen1_elo": 13884, "fair_v1": 13884, "gen2": 13884, "gen1_sr": 13884, "model4_fundamental": 10678, "model4_conditioned": 10669}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 26,467 | 14.3 | 9.6 | 19.9 | 15.5 | 18.6 | 13.8 | 8.4 | 11.92 | 40.8% | 22.2% |
| MW fair_v1 | 13,884 | 13.7 | 8.7 | 18.3 | 16.3 | 18.4 | 14.7 | 10.1 | 12.85 | 43.1% | 24.7% |
| MW gen1_elo | 13,884 | 13.1 | 8.9 | 20.1 | 14.9 | 19.0 | 14.4 | 9.5 | 12.43 | 43.0% | 23.9% |
| MW gen1_ledger | 12,583 | 15.1 | 10.5 | 21.6 | 14.6 | 18.7 | 12.9 | 6.6 | 10.78 | 38.2% | 19.5% |
| MW gen1_sr | 13,884 | 10.3 | 7.9 | 16.2 | 14.1 | 21.5 | 18.4 | 11.7 | 15.52 | 51.5% | 30.1% |
| MW gen2 | 13,884 | 12.2 | 7.2 | 16.1 | 14.2 | 19.8 | 17.2 | 13.2 | 15.12 | 50.2% | 30.4% |
| all families model4_conditioned | 10,669 | 22.4 | 20.4 | 36.0 | 15.7 | 3.9 | 0.8 | 0.8 | 5.68 | 5.5% | 1.6% |
| all families model4_fundamental | 10,678 | 16.8 | 13.3 | 35.7 | 20.0 | 10.6 | 2.6 | 1.1 | 7.59 | 14.3% | 3.7% |

Configurable thresholds (primary): >=5pp 76.1%, >=10pp 56.3%, >=15pp 40.8%, >=20pp 30.5%, >=25pp 22.2%, >=30pp 16.3%, >=40pp 8.4%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.52pp; >=10pp 45.6%, >=25pp 17.9%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,079 | 29.3 | 14.7 | 24.5 | 17.4 | 11.8 | 1.3 | 1.0 | 5.93 | 14.1% | 2.3% |
| CHALLENGER | 2,320 | 15.6 | 10.9 | 18.6 | 16.3 | 12.8 | 13.0 | 12.8 | 11.86 | 38.7% | 25.8% |
| ITF_MEN | 4,007 | 11.6 | 8.7 | 18.5 | 15.0 | 19.1 | 14.8 | 12.2 | 13.59 | 46.2% | 27.1% |
| ITF_WOMEN | 5,586 | 10.4 | 6.6 | 15.8 | 16.4 | 21.8 | 18.6 | 10.3 | 15.29 | 50.7% | 28.9% |
| WTA | 551 | 24.5 | 9.3 | 25.6 | 16.0 | 16.7 | 6.0 | 2.0 | 7.78 | 24.7% | 8.0% |
| WTA125 | 341 | 11.4 | 6.2 | 21.7 | 26.1 | 16.1 | 16.1 | 2.4 | 11.51 | 34.6% | 18.5% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,079 | 23.7 | 13.9 | 24.6 | 18.4 | 16.1 | 2.1 | 1.2 | 6.9 | 19.5% | 3.3% |
| CHALLENGER | 2,320 | 15.3 | 7.5 | 18.1 | 13.4 | 18.2 | 14.3 | 13.3 | 13.11 | 45.7% | 27.5% |
| ITF_MEN | 4,007 | 10.7 | 7.6 | 16.9 | 14.8 | 20.0 | 17.2 | 12.9 | 15.12 | 50.1% | 30.1% |
| ITF_WOMEN | 5,586 | 9.2 | 6.0 | 12.8 | 13.0 | 20.8 | 21.3 | 16.9 | 18.93 | 59.0% | 38.2% |
| WTA | 551 | 22.7 | 5.3 | 18.9 | 14.9 | 20.5 | 15.8 | 2.0 | 11.64 | 38.3% | 17.8% |
| WTA125 | 341 | 4.4 | 2.6 | 17.3 | 20.5 | 22.6 | 21.4 | 11.1 | 17.24 | 55.1% | 32.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,079 | 26.4 | 13.7 | 29.2 | 15.3 | 11.3 | 3.0 | 1.1 | 6.48 | 15.4% | 4.1% |
| CHALLENGER | 2,320 | 15.9 | 10.6 | 20.3 | 14.4 | 13.9 | 12.1 | 12.8 | 10.76 | 38.8% | 24.9% |
| ITF_MEN | 4,007 | 10.5 | 8.9 | 19.1 | 13.8 | 20.1 | 15.3 | 12.2 | 13.94 | 47.7% | 27.6% |
| ITF_WOMEN | 5,586 | 9.8 | 6.7 | 16.8 | 15.7 | 23.2 | 18.6 | 9.2 | 15.46 | 51.0% | 27.8% |
| WTA | 551 | 23.4 | 12.9 | 35.8 | 14.2 | 9.1 | 3.5 | 1.3 | 6.73 | 13.8% | 4.7% |
| WTA125 | 341 | 22.0 | 11.1 | 31.4 | 16.4 | 13.8 | 4.7 | 0.6 | 7.99 | 19.1% | 5.3% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 596 | 30.4 | 22.8 | 35.2 | 9.7 | 1.5 | 0.3 | 0.0 | 4.72 | 1.8% | 0.3% |
| CHALLENGER | 1,512 | 23.7 | 17.4 | 25.9 | 13.7 | 12.0 | 5.4 | 2.0 | 6.47 | 19.3% | 7.3% |
| DOUBLES | 811 | 4.1 | 3.3 | 10.7 | 11.6 | 19.2 | 24.3 | 26.8 | 25.6 | 70.3% | 51.0% |
| ITF_MEN | 3,922 | 14.8 | 8.5 | 21.1 | 15.2 | 20.4 | 12.4 | 7.7 | 11.76 | 40.4% | 20.0% |
| ITF_WOMEN | 4,635 | 11.5 | 9.3 | 19.9 | 14.5 | 22.5 | 16.7 | 5.6 | 13.01 | 44.8% | 22.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 447 | 21.5 | 11.6 | 25.3 | 18.6 | 15.2 | 7.2 | 0.7 | 8.4 | 23.0% | 7.8% |
| WTA125 | 511 | 16.6 | 12.9 | 22.5 | 20.4 | 16.2 | 8.6 | 2.7 | 9.32 | 27.6% | 11.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,071 | 29.2 | 14.7 | 24.6 | 17.5 | 11.8 | 1.3 | 1.0 | 5.93 | 14.1% | 2.3% |
| CHALLENGER | 1,635 | 20.6 | 13.9 | 23.9 | 19.3 | 13.0 | 6.5 | 2.8 | 7.99 | 22.3% | 9.3% |
| ITF_MEN | 2,863 | 14.4 | 10.9 | 21.9 | 16.7 | 19.1 | 11.9 | 5.1 | 10.81 | 36.1% | 17.0% |
| ITF_WOMEN | 3,988 | 12.8 | 8.3 | 18.5 | 18.9 | 23.4 | 14.8 | 3.2 | 12.63 | 41.4% | 18.0% |
| WTA | 548 | 24.4 | 9.3 | 25.7 | 15.9 | 16.8 | 5.8 | 2.0 | 7.77 | 24.6% | 7.8% |
| WTA125 | 328 | 11.9 | 6.4 | 21.0 | 26.5 | 16.5 | 16.2 | 1.5 | 11.49 | 34.2% | 17.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,071 | 23.6 | 13.9 | 24.6 | 18.3 | 16.1 | 2.1 | 1.2 | 6.9 | 19.5% | 3.4% |
| CHALLENGER | 1,635 | 20.2 | 9.8 | 22.9 | 16.3 | 18.6 | 9.4 | 2.7 | 9.08 | 30.7% | 12.1% |
| ITF_MEN | 2,864 | 12.6 | 9.2 | 19.6 | 16.6 | 21.4 | 14.8 | 5.9 | 12.44 | 42.0% | 20.7% |
| ITF_WOMEN | 3,988 | 10.8 | 7.2 | 14.4 | 14.2 | 23.1 | 20.3 | 10.1 | 16.26 | 53.5% | 30.3% |
| WTA | 548 | 22.6 | 5.3 | 19.0 | 15.0 | 20.4 | 15.7 | 2.0 | 11.63 | 38.1% | 17.7% |
| WTA125 | 328 | 4.6 | 2.7 | 17.4 | 21.3 | 21.9 | 21.9 | 10.1 | 17.02 | 54.0% | 32.0% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 578 | 30.4 | 23.2 | 35.5 | 9.9 | 0.7 | 0.3 | 0.0 | 4.69 | 1.0% | 0.4% |
| CHALLENGER | 1,280 | 25.8 | 19.7 | 28.1 | 13.3 | 11.0 | 2.0 | 0.1 | 5.76 | 13.1% | 2.1% |
| DOUBLES | 750 | 4.0 | 3.3 | 10.9 | 11.6 | 19.5 | 24.0 | 26.7 | 25.57 | 70.1% | 50.7% |
| ITF_MEN | 3,161 | 16.6 | 9.5 | 23.4 | 16.1 | 20.1 | 9.9 | 4.4 | 10.07 | 34.4% | 14.3% |
| ITF_WOMEN | 3,775 | 12.8 | 10.0 | 21.8 | 15.4 | 22.8 | 14.9 | 2.3 | 11.5 | 40.0% | 17.2% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 417 | 22.1 | 12.2 | 25.9 | 18.7 | 15.6 | 5.5 | 0.0 | 8.27 | 21.1% | 5.5% |
| WTA125 | 426 | 18.5 | 14.3 | 24.9 | 23.2 | 14.3 | 4.5 | 0.2 | 8.2 | 19.0% | 4.7% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 811 | 4.1 | 3.3 | 10.7 | 11.6 | 19.2 | 24.3 | 26.8 | 25.6 | 70.3% | 51.0% |
| singles | 11,772 | 15.8 | 11.0 | 22.4 | 14.8 | 18.7 | 12.1 | 5.2 | 10.18 | 36.0% | 17.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 3,207 | 13.6 | 9.5 | 20.1 | 16.0 | 16.1 | 14.2 | 10.3 | 12.18 | 40.7% | 24.6% |
| Hard | 9,300 | 14.0 | 8.4 | 18.1 | 16.1 | 19.0 | 14.5 | 9.9 | 12.9 | 43.4% | 24.4% |
| UNKNOWN | 1,377 | 11.6 | 8.2 | 15.1 | 18.2 | 20.0 | 16.6 | 10.2 | 13.98 | 46.8% | 26.8% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,067 | 19.9 | 10.6 | 20.4 | 17.3 | 14.6 | 9.3 | 7.9 | 9.71 | 31.8% | 17.2% |
| B | 1,857 | 15.4 | 9.5 | 19.4 | 17.3 | 16.6 | 11.8 | 9.8 | 11.18 | 38.3% | 21.7% |
| C | 2,147 | 12.5 | 9.9 | 19.5 | 15.3 | 18.6 | 14.8 | 9.4 | 12.69 | 42.8% | 24.2% |
| D | 2,625 | 10.9 | 8.4 | 17.4 | 16.5 | 22.1 | 14.9 | 9.9 | 13.97 | 46.9% | 24.8% |
| F | 3,188 | 7.7 | 5.1 | 14.8 | 14.9 | 21.1 | 22.8 | 13.5 | 18.39 | 57.5% | 36.4% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,512 | 22.4 | 15.7 | 27.8 | 15.3 | 11.9 | 5.0 | 1.9 | 6.88 | 18.7% | 6.8% |
| B | 1,977 | 14.7 | 9.6 | 24.5 | 16.1 | 18.9 | 11.6 | 4.6 | 10.35 | 35.1% | 16.2% |
| C | 2,595 | 11.8 | 7.9 | 18.0 | 14.4 | 20.7 | 15.7 | 11.6 | 13.95 | 47.9% | 27.2% |
| D | 2,084 | 14.0 | 9.3 | 21.4 | 13.2 | 22.0 | 14.0 | 6.2 | 12.04 | 42.3% | 20.2% |
| F | 2,415 | 9.2 | 7.8 | 14.2 | 13.7 | 23.6 | 21.5 | 10.1 | 16.93 | 55.2% | 31.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 4,578 | 18.5 | 9.8 | 19.6 | 17.3 | 14.9 | 9.9 | 10.0 | 10.57 | 34.8% | 19.9% |
| LIMITED | 3,452 | 14.8 | 10.5 | 20.5 | 16.1 | 17.6 | 13.3 | 7.2 | 11.31 | 38.1% | 20.5% |
| POOR | 5,854 | 9.2 | 6.7 | 15.9 | 15.7 | 21.6 | 19.2 | 11.8 | 16.04 | 52.6% | 31.0% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,472 | 29.9 | 24.9 | 37.2 | 5.4 | 1.9 | 0.6 | 0.1 | 4.56 | 2.5% | 0.7% |
| GAME_SPREAD | 2,325 | 25.0 | 15.7 | 36.6 | 17.5 | 4.7 | 0.3 | 0.2 | 6.14 | 5.1% | 0.4% |
| MATCH_WINNER | 12,583 | 15.1 | 10.5 | 21.6 | 14.6 | 18.7 | 12.9 | 6.6 | 10.78 | 38.2% | 19.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 4,170 | 31.8 | 19.8 | 30.4 | 10.0 | 6.4 | 1.4 | 0.3 | 4.82 | 8.0% | 1.7% |
| TOTAL_GAMES | 3,303 | 7.2 | 9.4 | 38.9 | 30.6 | 9.1 | 2.9 | 2.0 | 9.39 | 14.0% | 4.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,976 | 24.8 | 38.2 | 31.4 | 0.2 | 4.7 | 0.5 | 0.1 | 4.34 | 5.4% | 0.7% |
| GAME_SPREAD | 2,778 | 45.7 | 14.4 | 29.6 | 8.0 | 1.1 | 0.8 | 0.3 | 3.57 | 2.2% | 1.1% |
| TOTAL_GAMES | 3,915 | 3.4 | 6.6 | 45.2 | 36.9 | 5.1 | 1.2 | 1.7 | 9.52 | 8.0% | 2.9% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,976 | 25.6 | 18.3 | 36.4 | 9.8 | 6.9 | 2.5 | 0.4 | 5.6 | 9.8% | 2.9% |
| GAME_SPREAD | 2,778 | 19.0 | 13.1 | 28.5 | 21.7 | 14.4 | 2.7 | 0.7 | 8.06 | 17.8% | 3.4% |
| TOTAL_GAMES | 3,924 | 6.2 | 8.3 | 40.1 | 29.1 | 11.5 | 2.7 | 2.0 | 9.5 | 16.3% | 4.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 13,884 | 43.1% | 24.7% | 12.85 | 33.0% | 14.2% | 10.34 |
| gen1_elo | 13,884 | 43.0% | 23.9% | 12.43 | 32.6% | 13.8% | 9.75 |
| gen1_sr | 13,884 | 51.5% | 30.1% | 15.52 | 42.5% | 19.7% | 12.65 |
| gen2 | 13,884 | 50.2% | 30.4% | 15.12 | 42.5% | 21.4% | 12.57 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 7,052 | 16.6 | 10.9 | 21.2 | 17.7 | 18.6 | 11.5 | 3.4 | 10.31 | 33.5% | 14.9% |
| STALE | 6,832 | 10.6 | 6.3 | 15.2 | 14.9 | 18.3 | 17.9 | 16.9 | 16.71 | 53.1% | 34.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 6,051 | 17.2 | 11.6 | 23.6 | 14.4 | 16.8 | 11.5 | 4.8 | 9.35 | 33.2% | 16.3% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 26,467 | 6051 | 10524 | 9892 | 24.9 | 159.1 | 1400.4 |
| ge_15pp | 10,794 | 2008 | 3649 | 5137 | 28.6 | 452.9 | 1380.4 |
| ge_25pp | 5,882 | 989 | 1643 | 3250 | 35.9 | 573.0 | 1380.4 |
| lt_10pp | 11,574 | 3172 | 5075 | 3327 | 23.3 | 49.5 | 1230.8 |

Current slate `SL-20261009T064519Z-96a0de7f`: 636 priced rows, quote age at build {'median': 7.4, 'max': 7.5}, freshness {'FRESH': 636}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 4 | 0.0 | 0.0 | 25.0 | 0.0 | 75.0 | 0.0 | 0.0 | 20.45 | 75.0% | 0.0% |
| EXTERNAL_LONE_OUTLIER | 3 | 33.3 | 66.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 3.05 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 787 | 24.5 | 11.3 | 21.0 | 20.7 | 15.1 | 7.0 | 0.4 | 8.03 | 22.5% | 7.4% |
| MARKETS_AGREE | 105 | 78.1 | 21.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.74 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 176 | 0.0 | 3.4 | 33.0 | 34.7 | 19.3 | 9.1 | 0.6 | 11.81 | 29.0% | 9.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 13,884 | 1075 (7.7%) | 16.4% | 0.3% | {"EXTERNAL_STALE": 787, "AGREES_WITH_KALSHI": 176, "ALL_AGREE": 105, "SUPPORTS_MODEL_DIRECTION": 3, "EXTERNAL_OUTLIER": 3, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 5,987 | 231 (3.9%) | 22.1% | 1.3% | {"EXTERNAL_STALE": 177, "AGREES_WITH_KALSHI": 51, "SUPPORTS_MODEL_DIRECTION": 3} |
| fair_v1_ge_25pp | 3,431 | 75 (2.2%) | 22.7% | 0.0% | {"EXTERNAL_STALE": 58, "AGREES_WITH_KALSHI": 17} |
| fair_v1_ge_25pp_pregame_clean | 1,484 | 73 (4.9%) | 23.3% | 0.0% | {"EXTERNAL_STALE": 56, "AGREES_WITH_KALSHI": 17} |
| fair_v1_lt_10pp | 5,633 | 620 (11.0%) | 10.3% | 0.0% | {"EXTERNAL_STALE": 447, "ALL_AGREE": 105, "AGREES_WITH_KALSHI": 64, "EXTERNAL_OUTLIER": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 2,832 | 11.8 | 8.3 | 19.7 | 15.5 | 20.7 | 13.8 | 10.1 | 13.0 | 44.7% | 23.9% |
| 4-10x | 1,966 | 11.2 | 9.3 | 18.4 | 15.4 | 20.1 | 16.5 | 9.2 | 13.54 | 45.8% | 25.7% |
| <2x | 7,336 | 15.7 | 9.2 | 18.3 | 17.3 | 16.7 | 13.1 | 9.7 | 11.95 | 39.4% | 22.8% |
| >=10x | 1,750 | 10.7 | 6.3 | 15.5 | 14.3 | 20.1 | 20.5 | 12.5 | 16.49 | 53.1% | 33.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 3,623 | 14.4 | 8.6 | 19.1 | 16.0 | 18.1 | 12.9 | 10.9 | 12.22 | 41.8% | 23.7% |
| 300-1000 | 3,428 | 11.8 | 9.2 | 16.6 | 16.4 | 20.9 | 15.9 | 9.1 | 13.68 | 45.9% | 25.0% |
| <300 | 3,678 | 8.2 | 5.9 | 15.7 | 15.0 | 21.1 | 20.9 | 13.1 | 17.18 | 55.2% | 34.0% |
| >=3000 | 3,155 | 21.1 | 11.4 | 22.0 | 18.0 | 12.8 | 8.1 | 6.6 | 8.8 | 27.5% | 14.7% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 439 | 0.5424 | 0.4098 | 0.4852 | +0.057 | -0.075 | 0.0027 ± 0.0071 |
| ratio 4-10x | 304 | 0.5817 | 0.4399 | 0.523 | +0.059 | -0.083 | -0.0024 ± 0.009 |
| ratio <2x | 926 | 0.5436 | 0.4191 | 0.4579 | +0.086 | -0.039 | 0.0112 ± 0.0047 |
| ratio >=10x | 292 | 0.5481 | 0.3781 | 0.4384 | +0.110 | -0.060 | 0.0135 ± 0.0103 |
| thinner_sample 1000-3000 | 532 | 0.5468 | 0.4227 | 0.4662 | +0.081 | -0.043 | 0.006 ± 0.0062 |
| thinner_sample 300-1000 | 540 | 0.5701 | 0.4291 | 0.4981 | +0.072 | -0.069 | 0.0016 ± 0.0068 |
| thinner_sample <300 | 594 | 0.5429 | 0.3821 | 0.463 | +0.080 | -0.081 | 0.0089 ± 0.0069 |
| thinner_sample >=3000 | 295 | 0.5327 | 0.4361 | 0.4475 | +0.085 | -0.011 | 0.0187 ± 0.0067 |
| data_status ADEQUATE | 514 | 0.5309 | 0.4268 | 0.4436 | +0.087 | -0.017 | 0.0128 ± 0.0054 |
| data_status LIMITED | 508 | 0.5641 | 0.4315 | 0.4941 | +0.070 | -0.063 | 0.0013 ± 0.0067 |
| data_status POOR | 939 | 0.5526 | 0.3979 | 0.4739 | +0.079 | -0.076 | 0.0081 ± 0.0054 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 297 | 0.1885 | 0.1897 | -0.0012 ± 0.0009 | 0.5532 | 0.5562 | 0.4951 | 0.4806 | 0.5152 | -0.073 ± 0.0265 | -0.01 (3) |
| 3-5 | 199 | 0.1849 | 0.1857 | -0.0008 ± 0.0025 | 0.5486 | 0.5482 | 0.5111 | 0.4711 | 0.4975 | -0.072 ± 0.031 | 0.02 (1) |
| 5-10 | 400 | 0.2006 | 0.203 | -0.0024 ± 0.0034 | 0.5877 | 0.5932 | 0.5227 | 0.4488 | 0.4925 | -0.085 ± 0.0235 | -0.0125 (4) |
| 10-15 | 350 | 0.2124 | 0.207 | +0.0053 ± 0.0061 | 0.6113 | 0.5952 | 0.5206 | 0.3966 | 0.4343 | -0.094 ± 0.0244 | -0.0633 (3) |
| 15-25 | 418 | 0.2236 | 0.2126 | +0.0110 ± 0.0088 | 0.6393 | 0.613 | 0.5738 | 0.3781 | 0.4474 | -0.084 ± 0.0225 | -0.0133 (6) |
| 25-40 | 244 | 0.2172 | 0.201 | +0.0162 ± 0.017 | 0.6233 | 0.5774 | 0.6487 | 0.3395 | 0.4672 | -0.072 ± 0.0254 | -0.01 (1) |
| 40+ | 53 | 0.2878 | 0.1771 | +0.1107 ± 0.0514 | 0.7805 | 0.5305 | 0.7594 | 0.311 | 0.4151 | -0.127 ± 0.0502 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1469 | 0.1682 | 0.169 | -0.0008 ± 0.0004 | 0.5049 | 0.5056 | 0.4742 | 0.4595 | 0.4922 | -0.029 ± 0.0109 | -0.0188 (8) |
| 3-5 | 959 | 0.1905 | 0.1866 | +0.0039 ± 0.0011 | 0.5618 | 0.5467 | 0.4781 | 0.4384 | 0.4056 | -0.094 ± 0.0142 | 0.02 (1) |
| 5-10 | 2045 | 0.1928 | 0.1905 | +0.0022 ± 0.0014 | 0.5684 | 0.5609 | 0.4916 | 0.4179 | 0.4347 | -0.055 ± 0.0098 | -0.0082 (17) |
| 10-15 | 1869 | 0.1986 | 0.1818 | +0.0168 ± 0.0025 | 0.5815 | 0.5342 | 0.4718 | 0.3472 | 0.3419 | -0.075 ± 0.0098 | -0.0475 (4) |
| 15-25 | 2181 | 0.2002 | 0.1638 | +0.0364 ± 0.0034 | 0.5898 | 0.4881 | 0.4891 | 0.293 | 0.2989 | -0.070 ± 0.0087 | -0.0048 (29) |
| 25-40 | 1843 | 0.2162 | 0.1234 | +0.0928 ± 0.0051 | 0.6245 | 0.3819 | 0.5269 | 0.2134 | 0.2246 | -0.059 ± 0.0079 | -0.01 (1) |
| 40+ | 1276 | 0.371 | 0.0453 | +0.3257 ± 0.0066 | 0.9673 | 0.1778 | 0.6228 | 0.1065 | 0.0596 | -0.083 ± 0.0056 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 231 | 0.1964 | 0.1969 | -0.0004 ± 0.001 | 0.5763 | 0.5776 | 0.4909 | 0.4758 | 0.4848 | -0.096 ± 0.0309 | -0.01 (1) |
| 3-5 | 149 | 0.2036 | 0.2049 | -0.0014 ± 0.003 | 0.586 | 0.5915 | 0.52 | 0.48 | 0.5101 | -0.060 ± 0.039 | 0.02 (1) |
| 5-10 | 341 | 0.192 | 0.1891 | +0.0029 ± 0.0035 | 0.5658 | 0.5591 | 0.5681 | 0.4932 | 0.5073 | -0.098 ± 0.0244 | -0.01 (4) |
| 10-15 | 333 | 0.217 | 0.2107 | +0.0063 ± 0.0063 | 0.6202 | 0.6083 | 0.5807 | 0.4561 | 0.4985 | -0.096 ± 0.0261 | -0.05 (4) |
| 15-25 | 469 | 0.2244 | 0.2067 | +0.0177 ± 0.0083 | 0.6377 | 0.5951 | 0.5982 | 0.4009 | 0.4606 | -0.097 ± 0.0215 | -0.01 (5) |
| 25-40 | 319 | 0.2724 | 0.2018 | +0.0707 ± 0.0159 | 0.7637 | 0.5841 | 0.6727 | 0.3586 | 0.4044 | -0.140 ± 0.0252 | -0.025 (2) |
| 40+ | 119 | 0.3395 | 0.1867 | +0.1527 ± 0.0384 | 0.9544 | 0.5477 | 0.7618 | 0.2833 | 0.3782 | -0.068 ± 0.0368 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1328 | 0.1743 | 0.1751 | -0.0008 ± 0.0004 | 0.5208 | 0.5226 | 0.493 | 0.4786 | 0.5083 | -0.029 ± 0.012 | -0.0217 (6) |
| 3-5 | 803 | 0.1885 | 0.1857 | +0.0028 ± 0.0012 | 0.5488 | 0.5426 | 0.5214 | 0.4817 | 0.467 | -0.068 ± 0.0154 | 0.02 (1) |
| 5-10 | 1808 | 0.1837 | 0.1797 | +0.0040 ± 0.0015 | 0.5485 | 0.5346 | 0.5192 | 0.4459 | 0.4574 | -0.055 ± 0.0101 | -0.01 (5) |
| 10-15 | 1634 | 0.1947 | 0.1812 | +0.0135 ± 0.0026 | 0.5751 | 0.5305 | 0.5153 | 0.391 | 0.4021 | -0.064 ± 0.0107 | -0.02 (14) |
| 15-25 | 2281 | 0.2144 | 0.1726 | +0.0418 ± 0.0034 | 0.625 | 0.511 | 0.5285 | 0.3328 | 0.327 | -0.085 ± 0.0088 | -0.0026 (27) |
| 25-40 | 2110 | 0.2486 | 0.1373 | +0.1113 ± 0.0051 | 0.706 | 0.4186 | 0.5617 | 0.245 | 0.2289 | -0.089 ± 0.0081 | -0.015 (6) |
| 40+ | 1678 | 0.4024 | 0.0675 | +0.3349 ± 0.0073 | 1.0539 | 0.2371 | 0.6686 | 0.1308 | 0.1019 | -0.071 ± 0.0061 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 301 | 0.191 | 0.1937 | -0.0027 ± 0.0009 | 0.5604 | 0.5679 | 0.499 | 0.4837 | 0.5515 | -0.020 ± 0.0256 | -0.0133 (6) |
| 3-5 | 207 | 0.1863 | 0.1848 | +0.0014 ± 0.0024 | 0.5478 | 0.5435 | 0.4978 | 0.4586 | 0.4638 | -0.119 ± 0.0316 | -0.01 (1) |
| 5-10 | 424 | 0.1978 | 0.1974 | +0.0004 ± 0.0033 | 0.5816 | 0.579 | 0.5112 | 0.4373 | 0.467 | -0.090 ± 0.0225 | -0.01 (4) |
| 10-15 | 329 | 0.2148 | 0.2127 | +0.0021 ± 0.0063 | 0.6195 | 0.6089 | 0.5342 | 0.4113 | 0.465 | -0.086 ± 0.0251 | -0.044 (5) |
| 15-25 | 408 | 0.2249 | 0.2081 | +0.0168 ± 0.0088 | 0.6461 | 0.6011 | 0.5796 | 0.3862 | 0.4387 | -0.101 ± 0.0224 | -0.03 (1) |
| 25-40 | 245 | 0.2005 | 0.2068 | -0.0063 ± 0.0169 | 0.5836 | 0.5929 | 0.6563 | 0.3445 | 0.5061 | -0.047 ± 0.0247 | 0.0 (1) |
| 40+ | 47 | 0.3129 | 0.1765 | +0.1364 ± 0.0556 | 0.8395 | 0.5287 | 0.7528 | 0.2988 | 0.383 | -0.139 ± 0.0556 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1389 | 0.1796 | 0.1804 | -0.0008 ± 0.0004 | 0.5322 | 0.534 | 0.4855 | 0.4703 | 0.4989 | -0.031 ± 0.0114 | -0.0183 (23) |
| 3-5 | 965 | 0.184 | 0.1812 | +0.0027 ± 0.0011 | 0.5426 | 0.5356 | 0.4678 | 0.4286 | 0.4135 | -0.084 ± 0.0142 | -0.0243 (7) |
| 5-10 | 2196 | 0.1855 | 0.1806 | +0.0049 ± 0.0014 | 0.5522 | 0.536 | 0.4805 | 0.4062 | 0.4117 | -0.061 ± 0.0091 | -0.01 (18) |
| 10-15 | 1738 | 0.1954 | 0.1791 | +0.0163 ± 0.0025 | 0.5751 | 0.5258 | 0.488 | 0.3645 | 0.3585 | -0.079 ± 0.01 | -0.03 (9) |
| 15-25 | 2350 | 0.2037 | 0.1677 | +0.0360 ± 0.0033 | 0.5993 | 0.4985 | 0.493 | 0.2974 | 0.3043 | -0.066 ± 0.0085 | -0.03 (2) |
| 25-40 | 1792 | 0.2116 | 0.1193 | +0.0923 ± 0.0051 | 0.6138 | 0.3703 | 0.523 | 0.2055 | 0.2221 | -0.057 ± 0.0077 | 0.0 (1) |
| 40+ | 1212 | 0.3855 | 0.0468 | +0.3388 ± 0.007 | 1.0071 | 0.1824 | 0.6308 | 0.1076 | 0.0569 | -0.086 ± 0.0059 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 586 | 0.2015 | 0.2016 | -0.0001 ± 0.0006 | 0.5858 | 0.5855 | 0.4989 | 0.484 | 0.4846 | -0.049 ± 0.0185 | -0.0226 (46) |
| 3-5 | 437 | 0.1954 | 0.194 | +0.0014 ± 0.0017 | 0.5719 | 0.5667 | 0.4795 | 0.44 | 0.4439 | -0.052 ± 0.0211 | -0.0058 (33) |
| 5-10 | 892 | 0.1922 | 0.1871 | +0.0050 ± 0.0022 | 0.5687 | 0.5555 | 0.4794 | 0.406 | 0.4092 | -0.058 ± 0.0148 | -0.0049 (73) |
| 10-15 | 582 | 0.2039 | 0.1948 | +0.0091 ± 0.0046 | 0.5968 | 0.5712 | 0.483 | 0.3602 | 0.3832 | -0.042 ± 0.0182 | 0.0014 (64) |
| 15-25 | 784 | 0.2333 | 0.2082 | +0.0252 ± 0.0064 | 0.6611 | 0.6015 | 0.5486 | 0.3544 | 0.3878 | -0.057 ± 0.0164 | -0.0216 (58) |
| 25-40 | 448 | 0.2436 | 0.1859 | +0.0578 ± 0.0126 | 0.6864 | 0.5455 | 0.6286 | 0.3152 | 0.3772 | -0.074 ± 0.019 | -0.0216 (25) |
| 40+ | 149 | 0.3493 | 0.1859 | +0.1634 ± 0.0358 | 0.9929 | 0.5499 | 0.7782 | 0.2869 | 0.3893 | -0.060 ± 0.0322 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1734 | 0.1862 | 0.1861 | +0.0001 ± 0.0004 | 0.5473 | 0.5461 | 0.4993 | 0.4842 | 0.4844 | -0.044 ± 0.0103 | -0.0155 (82) |
| 3-5 | 1223 | 0.1877 | 0.1849 | +0.0028 ± 0.001 | 0.5497 | 0.5433 | 0.4912 | 0.4518 | 0.4391 | -0.060 ± 0.0123 | -0.0148 (63) |
| 5-10 | 2507 | 0.1908 | 0.183 | +0.0079 ± 0.0013 | 0.5657 | 0.5437 | 0.4763 | 0.4026 | 0.3901 | -0.066 ± 0.0087 | -0.0087 (125) |
| 10-15 | 1712 | 0.2 | 0.1858 | +0.0142 ± 0.0026 | 0.5877 | 0.5494 | 0.4963 | 0.3732 | 0.3762 | -0.057 ± 0.0103 | -0.0053 (105) |
| 15-25 | 2212 | 0.2263 | 0.1955 | +0.0309 ± 0.0037 | 0.6516 | 0.5698 | 0.5428 | 0.3478 | 0.3666 | -0.057 ± 0.0095 | -0.0255 (106) |
| 25-40 | 1555 | 0.2394 | 0.1605 | +0.0788 ± 0.0064 | 0.6783 | 0.4786 | 0.59 | 0.2754 | 0.3093 | -0.061 ± 0.0098 | -0.0206 (47) |
| 40+ | 742 | 0.3623 | 0.1138 | +0.2485 ± 0.0132 | 0.9953 | 0.355 | 0.6828 | 0.1775 | 0.1954 | -0.060 ± 0.0115 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 1961 | 1.098 ± 0.064 | 1.191 | 0.1712 | 0.1699 | 0.2086 | 0.201 |
| gen2 | 1961 | 0.87 ± 0.056 | 1.128 | 0.1874 | 0.1694 | 0.2274 | 0.201 |
| gen1_elo | 1961 | 1.086 ± 0.063 | 1.185 | 0.1752 | 0.1705 | 0.2071 | 0.201 |
| gen1_sr | 1961 | 1.08 ± 0.072 | 1.202 | 0.1449 | 0.1718 | 0.2225 | 0.2008 |
| gen1_ledger | 3878 | 0.92 ± 0.041 | 1.077 | 0.1731 | 0.1909 | 0.216 | 0.1953 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 10,794)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,941 | 27.3% |
| STALE_QUOTE | market_freshness | 2,230 | 20.7% |
| BOOK_QUALITY | execution | 1,869 | 17.3% |
| POOR_DATA | data | 1,158 | 10.7% |
| LIMITED_DATA | data | 826 | 7.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 585 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 472 | 4.4% |
| IDENTITY_AMBIGUOUS | mapping | 335 | 3.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 327 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 51 | 0.5% |

Cause class: coverage 27.3%, market_freshness 20.7%, data 18.4%, execution 17.3%, market_freshness/coverage 8.5%, model_calibration_or_unknown 4.4%, mapping 3.1%, model_calibration 0.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.2%, START_UNVERIFIABLE 96.3%, LOW_DATA_QUALITY 68.9%, STALE_PLAYER_DATA 57.6%, THIN_PLAYER_HISTORY 57.1%, STALE_KALSHI_QUOTE 47.6%, MODEL_INTERNAL_DISAGREEMENT 37.3%, ASYMMETRIC_SAMPLE_SIZE 30.5%, WIDE_SPREAD 23.2%, MODEL_HIGH_UNCERTAINTY 16.2%, PLAYER_IDENTITY_RISK 11.3%, LEVEL_TRANSFER_RISK 8.9%, EVENT_MAPPING_RISK 8.0%, LOW_DISPLAYED_LIQUIDITY 7.3%, MODEL_CALIBRATION_OUTLIER 3.4%, EXTERNAL_MARKET_REJECTION 0.8%, UNKNOWN 0.5%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 29.8%, POST_SETTLEMENT_OBSERVATION 27.3%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### >= ge_25 pp (N = 5,882)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,309 | 39.3% |
| STALE_QUOTE | market_freshness | 997 | 17.0% |
| BOOK_QUALITY | execution | 989 | 16.8% |
| POOR_DATA | data | 468 | 8.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 321 | 5.5% |
| LIMITED_DATA | data | 257 | 4.4% |
| IDENTITY_AMBIGUOUS | mapping | 213 | 3.6% |
| IN_PLAY_QUOTE | market_freshness/coverage | 205 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 108 | 1.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 15 | 0.3% |

Cause class: coverage 39.3%, market_freshness 17.0%, execution 16.8%, data 12.3%, market_freshness/coverage 8.9%, mapping 3.6%, model_calibration_or_unknown 1.8%, model_calibration 0.3%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.6%, START_UNVERIFIABLE 98.2%, LOW_DATA_QUALITY 71.7%, THIN_PLAYER_HISTORY 58.5%, STALE_KALSHI_QUOTE 55.2%, STALE_PLAYER_DATA 52.3%, MODEL_INTERNAL_DISAGREEMENT 38.5%, ASYMMETRIC_SAMPLE_SIZE 32.1%, WIDE_SPREAD 22.8%, MODEL_HIGH_UNCERTAINTY 17.6%, PLAYER_IDENTITY_RISK 14.5%, EVENT_MAPPING_RISK 9.8%, LOW_DISPLAYED_LIQUIDITY 7.6%, LEVEL_TRANSFER_RISK 7.6%, MODEL_CALIBRATION_OUTLIER 4.3%, EXTERNAL_MARKET_REJECTION 0.4%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 42.2%, POST_SETTLEMENT_OBSERVATION 39.3%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 4867, "IDENTITY_AMBIGUOUS": 1015}; ticker orientation: {"VERIFIED": 5882}.

Checks: discipline:AMBIGUOUS 414, discipline:PASS 5468, identity_confidence:AMBIGUOUS 852, identity_confidence:PASS 5030, level_mapping:NA 426, level_mapping:PASS 5456, market_pair:AMBIGUOUS 220, market_pair:NA 130, market_pair:PASS 5532, model_complement:NA 97, model_complement:PASS 5785, namesake:PASS 5882, physical_match_id:NA 2451, physical_match_id:PASS 3431, player_ids:PASS 5882, same_pair_other_event:PASS 5882, ticker_orientation:PASS 5882

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,675 | 1.6% | 1.6% | 0.5% | {"market_freshness": 20, "execution": 7} | 5.38 | 0.2202 / 0.2109 (147) | 18.4% | 0.1% | 5.6% | 1.6% |
| CHALLENGER | 3,832 | 18.5% | 6.1% | 12.1% | {"coverage": 446, "market_freshness": 107, "market_freshness/coverage": 85, "model_calibration_or_unknown": 39, "data": 26, "execution": 4, "model_calibration": 3} | 6.7 | 0.2239 / 0.206 (898) | 45.3% | 4.7% | 1.7% | 23.9% |
| DOUBLES | 811 | 51.0% | 50.7% | 7.0% | {"execution": 150, "mapping": 124, "market_freshness": 106, "market_freshness/coverage": 27, "coverage": 7} | 25.57 | 0.3176 / 0.2272 (214) | 28.8% | 0.0% | 100.0% | 7.5% |
| ITF_MEN | 7,929 | 23.6% | 15.6% | 31.8% | {"coverage": 769, "execution": 383, "data": 269, "market_freshness": 267, "market_freshness/coverage": 163, "mapping": 19, "model_calibration_or_unknown": 1} | 10.45 | 0.2103 / 0.1929 (1937) | 38.1% | 54.0% | 6.2% | 24.0% |
| ITF_WOMEN | 10,221 | 25.9% | 17.6% | 45.0% | {"coverage": 1070, "market_freshness": 439, "execution": 428, "data": 406, "market_freshness/coverage": 210, "mapping": 64, "model_calibration_or_unknown": 22, "model_calibration": 9} | 12.17 | 0.2014 / 0.1921 (2161) | 39.1% | 57.4% | 9.6% | 24.1% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 998 | 7.9% | 6.8% | 1.3% | {"market_freshness": 34, "model_calibration_or_unknown": 16, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 7.98 | 0.2039 / 0.1997 (149) | 33.5% | 2.1% | 1.2% | 3.3% |
| WTA125 | 852 | 14.2% | 10.3% | 2.1% | {"market_freshness/coverage": 31, "model_calibration_or_unknown": 28, "market_freshness": 22, "data": 13, "coverage": 12, "execution": 8, "mapping": 4, "model_calibration": 3} | 10.01 | 0.2284 / 0.2139 (291) | 25.6% | 6.2% | 4.0% | 11.5% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 5 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 6 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 207 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 8 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 9 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 10 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 11 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 12 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 14 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 16 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 22.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1345 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 17 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 18 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 19 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 20 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 21 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 765 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 22 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 23 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 24 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 25 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 26 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 27 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 28 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 29 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 30 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 64 min (STALE); no external reference |
| 31 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 32 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 33 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 34 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 36 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 799 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 37 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 38 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 39 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 40 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 41 | `KXITFWMATCH-26OCT08ARISAV-SAV` | ITF_WOMEN | fair_v1 | 75% / 2% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 43 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 687 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 44 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 45 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 46 | `KXITFWMATCH-26OCT08ARAWAN-ARA` | ITF_WOMEN | fair_v1 | 77% / 6% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 123 min (STALE); data POOR (grade D, thinner serve sample 553.0, ratio 3.97); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 708 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 49 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 50 | `KXITFWMATCH-26OCT08YANZHE-YAN` | ITF_WOMEN | fair_v1 | 90% / 18% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 61 min before settlement (in-play print); quote age at model time 166 min (STALE); data LIMITED (grade C, thinner serve sample 1212.0, ratio 2.36); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.982, "by_level_share_of_ge_25pp": {"ATP": 0.0046, "CHALLENGER": 0.1207, "DOUBLES": 0.0704, "ITF_MEN": 0.3181, "ITF_WOMEN": 0.4502, "OTHER": 0.002, "WTA": 0.0134, "WTA125": 0.0206}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5525, "share_primary_cause_market_settled_or_in_play": 0.4821, "share_primary_cause_stale_quote_only": 0.1695}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 5882, "identity_ambiguous_share": 0.1726, "ticker_orientation": {"VERIFIED": 5882}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 3431, "with_external": 75, "coverage": 0.0219, "external_status": {"EXTERNAL_STALE": 58, "AGREES_WITH_KALSHI": 17}, "triangulation": {"INSUFFICIENT_INPUTS": 58, "MODEL_LONE_OUTLIER": 17}, "share_external_agrees_with_kalshi": 0.2267, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 1484, "with_external": 73, "coverage": 0.0492, "external_status": {"EXTERNAL_STALE": 56, "AGREES_WITH_KALSHI": 17}, "triangulation": {"INSUFFICIENT_INPUTS": 56, "MODEL_LONE_OUTLIER": 17}, "share_external_agrees_with_kalshi": 0.2329, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 625.0, "median_sample_ratio": 2.31, "median_min_matches": 21.0, "median_max_days_since_last": 196.5, "share_severe_asymmetry": 0.1734, "data_status": {"POOR": 3011, "LIMITED": 1813, "ADEQUATE": 1058}, "comparison_lt_10pp": {"median_thinner_serve_points": 1798.0, "median_sample_ratio": 1.72, "median_min_matches": 79.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 439, "model_minus_observed": 0.0572, "kalshi_minus_observed": -0.0754, "brier_diff_model_minus_kalshi": 0.0027}, "4-10x": {"n": 304, "model_minus_observed": 0.0587, "kalshi_minus_observed": -0.0831, "brier_diff_model_minus_kalshi": -0.0024}, "<2x": {"n": 926, "model_minus_observed": 0.0857, "kalshi_minus_observed": -0.0387, "brier_diff_model_minus_kalshi": 0.0112}, ">=10x": {"n": 292, "model_minus_observed": 0.1097, "kalshi_minus_observed": -0.0603, "brier_diff_model_minus_kalshi": 0.0135}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 1961, "model": {"intercept": -0.559, "slope": 0.87, "slope_se": 0.056}, "kalshi_mid_same_rows": {"intercept": 0.228, "slope": 1.128, "slope_se": 0.065}, "mean_extremity_model": 0.1874, "mean_extremity_kalshi": 0.1694, "model_brier": 0.2274, "kalshi_brier": 0.201, "brier_diff_model_minus_kalshi": 0.0264, "brier_diff_se": 0.0043, "model_logloss": 0.6508, "kalshi_logloss": 0.5841}, "fair_v1": {"n": 1961, "model": {"intercept": -0.404, "slope": 1.098, "slope_se": 0.064}, "kalshi_mid_same_rows": {"intercept": 0.341, "slope": 1.191, "slope_se": 0.067}, "mean_extremity_model": 0.1712, "mean_extremity_kalshi": 0.1699, "model_brier": 0.2086, "kalshi_brier": 0.201, "brier_diff_model_minus_kalshi": 0.0076, "brier_diff_se": 0.0034, "model_logloss": 0.6034, "kalshi_logloss": 0.5839}, "gen1_elo": {"n": 1961, "model": {"intercept": -0.375, "slope": 1.086, "slope_se": 0.063}, "kalshi_mid_same_rows": {"intercept": 0.353, "slope": 1.185, "slope_se": 0.066}, "mean_extremity_model": 0.1752, "mean_extremity_kalshi": 0.1705, "model_brier": 0.2071, "kalshi_brier": 0.201, "brier_diff_model_minus_kalshi": 0.0061, "brier_diff_se": 0.0034, "model_logloss": 0.601, "kalshi_logloss": 0.5837}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2471, "share_ge_15": 0.4312, "median_abs_gap": 12.85, "n": 13884}, "gen1_elo": {"share_ge_25": 0.2395, "share_ge_15": 0.4299, "median_abs_gap": 12.43, "n": 13884}, "gen1_sr": {"share_ge_25": 0.3006, "share_ge_15": 0.5153, "median_abs_gap": 15.52, "n": 13884}, "gen2": {"share_ge_25": 0.3042, "share_ge_15": 0.502, "median_abs_gap": 15.12, "n": 13884}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1422, "share_ge_15": 0.3304, "median_abs_gap": 10.34, "n": 10433}, "gen1_elo": {"share_ge_25": 0.1384, "share_ge_15": 0.326, "median_abs_gap": 9.75, "n": 10432}, "gen1_sr": {"share_ge_25": 0.197, "share_ge_15": 0.425, "median_abs_gap": 12.65, "n": 10433}, "gen2": {"share_ge_25": 0.2145, "share_ge_15": 0.425, "median_abs_gap": 12.57, "n": 10434}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.38, "share_ge_25_all": 0.0161, "share_ge_25_pregame_clean": 0.0164}, "WTA": {"median_abs_gap_pregame_clean": 7.98, "share_ge_25_all": 0.0792, "share_ge_25_pregame_clean": 0.0684}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2388, "share_within_10pp_all": 0.4373, "share_within_10pp_pregame_clean": 0.5013, "corr_model_vs_mid_pregame_clean": 0.8501}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 297, "model_brier": 0.1885, "kalshi_brier": 0.1897, "brier_diff_model_minus_kalshi": -0.0012}, "10-15": {"n_settled": 350, "model_brier": 0.2124, "kalshi_brier": 0.207, "brier_diff_model_minus_kalshi": 0.0053}, "15-25": {"n_settled": 418, "model_brier": 0.2236, "kalshi_brier": 0.2126, "brier_diff_model_minus_kalshi": 0.011}, "25-40": {"n_settled": 244, "model_brier": 0.2172, "kalshi_brier": 0.201, "brier_diff_model_minus_kalshi": 0.0162}, "3-5": {"n_settled": 199, "model_brier": 0.1849, "kalshi_brier": 0.1857, "brier_diff_model_minus_kalshi": -0.0008}, "40+": {"n_settled": 53, "model_brier": 0.2878, "kalshi_brier": 0.1771, "brier_diff_model_minus_kalshi": 0.1107}, "5-10": {"n_settled": 400, "model_brier": 0.2006, "kalshi_brier": 0.203, "brier_diff_model_minus_kalshi": -0.0024}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.559, "slope": 0.87, "slope_se": 0.056}, "kalshi_slope": {"intercept": 0.228, "slope": 1.128, "slope_se": 0.065}, "n": 1961}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 214, "model_brier": 0.3176, "kalshi_brier": 0.2272, "brier_diff_model_minus_kalshi": 0.0903, "brier_diff_se": 0.0215, "corr_model_outcome": -0.0001, "corr_kalshi_outcome": 0.3199}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
