# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-20T09:39Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 43,503): 0-3 14.3%, 3-5 9.5%, 5-10 19.8%, 10-15 15.4%, 15-25 19.2%, 25-40 13.8%, 40+ 7.9%; median gap 11.93 pp.
* **Where the extremes live**: 97.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 75.6%, Challenger 12.5%, doubles 7.0%). Main tour: ATP 4.6% and WTA 4.6% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 9,436): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.8%, BOOK_QUALITY 19.4%, STALE_QUOTE 18.2%, POOR_DATA 9.1%, POSSIBLY_IN_PLAY_QUOTE 5.2%, IDENTITY_AMBIGUOUS 4.5%, LIMITED_DATA 3.8%, IN_PLAY_QUOTE 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%. By class: coverage 33.8%, execution 19.4%, market_freshness 18.2%, data 12.9%, market_freshness/coverage 8.5%, mapping 4.5%, model_calibration_or_unknown 2.2%, model_calibration 0.7%.
* **Stale / settled / in-play**: 50.9% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.2% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 9,436 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.3% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.6%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 24.4% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 504.0 points vs 1761.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.057, Gen-2 0.854, Gen-1 ledger 0.881 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 441 model 0.223 vs Kalshi 0.2086; n 88 model 0.2969 vs Kalshi 0.1747.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 184,853 model-market comparisons (300,159 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 64,660 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-20T09:26:49.091241+00:00'], shadow board 48,388 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-20T09:26:53.689669+00:00'], Model 4 22,945 rows, 17,066 settled tickers, 5,885 tickers with an external scan.
* By model: {"gen1_ledger": 43605, "gen1_elo": 24326, "fair_v1": 24326, "gen2": 24326, "gen1_sr": 24326, "model4_fundamental": 21981, "model4_conditioned": 21963}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 43,503 | 14.3 | 9.5 | 19.8 | 15.4 | 19.2 | 13.8 | 7.9 | 11.93 | 40.9% | 21.7% |
| MW fair_v1 | 24,326 | 13.3 | 8.7 | 18.4 | 15.8 | 19.9 | 14.6 | 9.4 | 13.0 | 43.8% | 24.0% |
| MW gen1_elo | 24,326 | 13.1 | 8.9 | 19.4 | 15.2 | 19.8 | 14.5 | 9.1 | 12.67 | 43.4% | 23.6% |
| MW gen1_ledger | 19,177 | 15.5 | 10.7 | 21.6 | 15.0 | 18.5 | 12.8 | 6.0 | 10.54 | 37.3% | 18.8% |
| MW gen1_sr | 24,326 | 10.0 | 7.3 | 16.8 | 14.2 | 21.4 | 18.5 | 11.8 | 15.63 | 51.7% | 30.3% |
| MW gen2 | 24,326 | 11.3 | 7.4 | 16.4 | 14.2 | 20.1 | 17.7 | 13.0 | 15.4 | 50.7% | 30.6% |
| all families model4_conditioned | 21,963 | 21.9 | 19.2 | 34.4 | 17.5 | 4.6 | 1.4 | 1.0 | 5.92 | 7.0% | 2.4% |
| all families model4_fundamental | 21,981 | 16.3 | 13.0 | 34.2 | 20.4 | 11.3 | 3.4 | 1.3 | 7.89 | 16.0% | 4.7% |

Configurable thresholds (primary): >=5pp 76.2%, >=10pp 56.4%, >=15pp 40.9%, >=20pp 30.3%, >=25pp 21.7%, >=30pp 15.5%, >=40pp 7.9%, >=50pp 3.5%
Executable gap (model outside the book, before fees): median 8.33pp; >=10pp 44.8%, >=25pp 16.8%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,142 | 28.4 | 14.0 | 25.0 | 15.7 | 11.5 | 4.9 | 0.6 | 6.21 | 17.0% | 5.4% |
| CHALLENGER | 4,100 | 15.6 | 10.2 | 20.3 | 16.0 | 14.8 | 12.3 | 10.7 | 11.16 | 37.8% | 23.0% |
| ITF_MEN | 6,399 | 11.0 | 7.8 | 17.1 | 14.6 | 20.7 | 16.8 | 12.1 | 14.91 | 49.6% | 28.9% |
| ITF_WOMEN | 9,534 | 9.9 | 6.9 | 15.8 | 15.5 | 23.2 | 18.1 | 10.7 | 15.64 | 51.9% | 28.8% |
| WTA | 1,491 | 17.5 | 12.5 | 24.0 | 19.9 | 21.0 | 4.3 | 0.7 | 8.74 | 26.0% | 5.0% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,142 | 23.3 | 15.2 | 24.7 | 17.0 | 13.8 | 5.1 | 0.8 | 6.71 | 19.8% | 5.9% |
| CHALLENGER | 4,100 | 14.7 | 8.5 | 18.9 | 14.3 | 17.9 | 14.0 | 11.7 | 12.67 | 43.6% | 25.7% |
| ITF_MEN | 6,399 | 9.2 | 6.5 | 15.2 | 13.4 | 19.7 | 20.1 | 15.9 | 17.53 | 55.7% | 36.0% |
| ITF_WOMEN | 9,534 | 8.3 | 5.6 | 13.5 | 13.7 | 21.6 | 20.8 | 16.5 | 18.83 | 58.9% | 37.3% |
| WTA | 1,491 | 14.7 | 9.5 | 20.0 | 16.0 | 24.6 | 14.5 | 0.8 | 11.73 | 39.9% | 15.3% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,142 | 23.8 | 13.4 | 24.9 | 16.2 | 14.9 | 5.8 | 0.9 | 7.1 | 21.7% | 6.8% |
| CHALLENGER | 4,100 | 14.5 | 9.7 | 21.3 | 15.2 | 15.9 | 12.3 | 11.1 | 11.19 | 39.3% | 23.4% |
| ITF_MEN | 6,399 | 10.2 | 7.8 | 17.4 | 13.9 | 21.4 | 17.1 | 12.2 | 15.22 | 50.7% | 29.3% |
| ITF_WOMEN | 9,534 | 9.5 | 6.8 | 16.3 | 15.8 | 23.4 | 18.3 | 9.9 | 15.57 | 51.6% | 28.2% |
| WTA | 1,491 | 24.6 | 16.6 | 30.2 | 15.7 | 10.2 | 2.3 | 0.5 | 6.0 | 12.9% | 2.8% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,226 | 26.8 | 20.1 | 29.7 | 12.1 | 8.2 | 2.9 | 0.4 | 5.36 | 11.4% | 3.3% |
| CHALLENGER | 2,885 | 21.4 | 14.6 | 27.0 | 14.1 | 14.7 | 6.3 | 1.9 | 7.25 | 22.9% | 8.2% |
| DOUBLES | 1,366 | 4.5 | 4.1 | 11.5 | 10.5 | 20.9 | 26.1 | 22.5 | 24.11 | 69.4% | 48.5% |
| ITF_MEN | 5,360 | 14.2 | 8.7 | 20.6 | 15.9 | 20.5 | 13.3 | 6.8 | 11.92 | 40.6% | 20.1% |
| ITF_WOMEN | 6,458 | 12.2 | 8.9 | 19.1 | 15.2 | 21.9 | 16.6 | 6.1 | 13.07 | 44.5% | 22.7% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,001 | 22.3 | 15.9 | 29.3 | 18.2 | 10.4 | 3.7 | 0.3 | 6.97 | 14.4% | 4.0% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,100 | 28.6 | 14.1 | 25.3 | 15.5 | 11.4 | 4.6 | 0.6 | 6.17 | 16.6% | 5.2% |
| CHALLENGER | 2,934 | 20.4 | 12.5 | 25.1 | 18.3 | 15.2 | 6.5 | 1.9 | 8.35 | 23.7% | 8.5% |
| ITF_MEN | 4,711 | 13.4 | 9.6 | 20.2 | 16.4 | 21.1 | 13.8 | 5.5 | 11.98 | 40.4% | 19.3% |
| ITF_WOMEN | 7,210 | 11.5 | 8.2 | 17.8 | 17.5 | 24.8 | 15.3 | 4.8 | 13.48 | 45.0% | 20.1% |
| WTA | 1,450 | 17.7 | 12.3 | 23.9 | 20.1 | 21.0 | 4.3 | 0.8 | 8.81 | 26.0% | 5.0% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,100 | 23.5 | 15.4 | 24.7 | 17.1 | 13.7 | 5.0 | 0.7 | 6.58 | 19.4% | 5.7% |
| CHALLENGER | 2,934 | 18.4 | 10.8 | 23.4 | 17.2 | 18.3 | 9.6 | 2.3 | 9.34 | 30.2% | 11.9% |
| ITF_MEN | 4,712 | 10.8 | 7.7 | 17.5 | 15.1 | 21.7 | 18.2 | 9.2 | 14.59 | 49.0% | 27.3% |
| ITF_WOMEN | 7,210 | 9.2 | 6.4 | 14.8 | 15.0 | 23.7 | 20.4 | 10.5 | 16.73 | 54.6% | 30.9% |
| WTA | 1,450 | 14.7 | 9.4 | 19.9 | 15.8 | 24.6 | 14.7 | 0.8 | 11.88 | 40.1% | 15.5% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,188 | 26.9 | 20.3 | 29.9 | 12.3 | 7.7 | 2.7 | 0.2 | 5.3 | 10.6% | 2.9% |
| CHALLENGER | 2,519 | 22.9 | 15.7 | 28.8 | 13.9 | 14.0 | 4.1 | 0.6 | 6.68 | 18.7% | 4.7% |
| DOUBLES | 1,270 | 4.5 | 4.2 | 11.7 | 10.7 | 20.8 | 26.2 | 21.9 | 24.0 | 68.9% | 48.1% |
| ITF_MEN | 4,477 | 15.5 | 9.4 | 22.4 | 16.6 | 20.2 | 11.6 | 4.1 | 10.77 | 35.9% | 15.7% |
| ITF_WOMEN | 5,410 | 12.9 | 9.4 | 20.6 | 16.1 | 22.0 | 15.4 | 3.5 | 11.9 | 41.0% | 19.0% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 954 | 22.8 | 16.4 | 29.4 | 18.2 | 10.4 | 2.9 | 0.0 | 6.81 | 13.3% | 2.9% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,366 | 4.5 | 4.1 | 11.5 | 10.5 | 20.9 | 26.1 | 22.5 | 24.11 | 69.4% | 48.5% |
| singles | 17,811 | 16.3 | 11.2 | 22.4 | 15.3 | 18.3 | 11.8 | 4.7 | 10.03 | 34.8% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 5,509 | 13.5 | 9.0 | 19.4 | 15.8 | 18.5 | 14.6 | 9.2 | 12.6 | 42.3% | 23.8% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 15,506 | 13.7 | 8.7 | 18.4 | 15.5 | 20.1 | 14.4 | 9.3 | 13.0 | 43.9% | 23.7% |
| UNKNOWN | 3,074 | 11.6 | 8.0 | 16.9 | 17.4 | 20.5 | 15.9 | 9.8 | 13.57 | 46.2% | 25.7% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,085 | 19.6 | 11.5 | 21.3 | 17.0 | 16.0 | 8.8 | 5.7 | 9.3 | 30.5% | 14.5% |
| B | 3,133 | 12.8 | 9.2 | 20.2 | 17.1 | 18.6 | 11.8 | 10.3 | 12.01 | 40.7% | 22.1% |
| C | 3,421 | 12.6 | 9.0 | 18.9 | 14.7 | 19.9 | 15.1 | 9.8 | 13.02 | 44.8% | 24.9% |
| D | 4,024 | 12.3 | 8.0 | 16.9 | 15.7 | 22.0 | 15.5 | 9.5 | 13.93 | 47.0% | 25.0% |
| F | 6,663 | 7.8 | 5.6 | 15.1 | 14.4 | 23.2 | 21.3 | 12.5 | 17.82 | 57.0% | 33.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,503 | 23.3 | 15.9 | 28.4 | 15.2 | 11.7 | 4.0 | 1.5 | 6.66 | 17.2% | 5.5% |
| B | 2,684 | 15.8 | 10.4 | 24.1 | 16.2 | 18.9 | 10.7 | 3.8 | 9.93 | 33.5% | 14.5% |
| C | 3,781 | 10.8 | 7.3 | 18.3 | 14.5 | 21.9 | 16.3 | 10.8 | 14.49 | 49.1% | 27.2% |
| D | 2,776 | 14.0 | 9.7 | 19.9 | 14.7 | 21.0 | 14.7 | 6.2 | 12.09 | 41.9% | 20.9% |
| F | 4,433 | 10.3 | 7.9 | 15.7 | 14.4 | 22.3 | 20.8 | 8.6 | 15.9 | 51.7% | 29.4% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 8,024 | 17.9 | 10.4 | 20.7 | 17.0 | 16.4 | 9.5 | 8.1 | 10.27 | 34.0% | 17.6% |
| LIMITED | 5,394 | 14.2 | 10.3 | 20.1 | 15.5 | 19.2 | 13.4 | 7.2 | 11.61 | 39.8% | 20.6% |
| POOR | 10,908 | 9.5 | 6.6 | 15.9 | 15.0 | 22.7 | 19.0 | 11.3 | 16.02 | 53.0% | 30.3% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,724 | 26.7 | 21.1 | 34.7 | 11.7 | 4.1 | 1.4 | 0.2 | 5.17 | 5.7% | 1.6% |
| GAME_SPREAD | 4,142 | 23.2 | 15.5 | 33.4 | 17.0 | 8.3 | 2.3 | 0.3 | 6.49 | 10.9% | 2.6% |
| MATCH_WINNER | 19,177 | 15.5 | 10.7 | 21.6 | 15.0 | 18.5 | 12.8 | 6.0 | 10.54 | 37.3% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 8,806 | 30.1 | 17.0 | 30.4 | 12.5 | 8.1 | 1.5 | 0.4 | 5.34 | 10.0% | 1.9% |
| TOTAL_GAMES | 6,732 | 7.8 | 9.1 | 36.6 | 29.1 | 11.0 | 3.5 | 2.9 | 9.61 | 17.4% | 6.4% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,687 | 25.4 | 34.8 | 32.2 | 3.7 | 3.2 | 0.6 | 0.2 | 4.44 | 3.9% | 0.7% |
| GAME_SPREAD | 5,269 | 46.1 | 16.9 | 26.9 | 7.5 | 1.8 | 0.6 | 0.2 | 3.39 | 2.6% | 0.8% |
| TOTAL_GAMES | 9,007 | 4.8 | 7.3 | 40.6 | 35.2 | 7.4 | 2.5 | 2.2 | 9.72 | 12.2% | 4.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,690 | 24.4 | 17.9 | 35.6 | 12.2 | 7.2 | 2.5 | 0.3 | 5.79 | 10.0% | 2.8% |
| GAME_SPREAD | 5,272 | 19.1 | 13.3 | 28.4 | 19.9 | 14.3 | 4.0 | 0.9 | 7.96 | 19.3% | 5.0% |
| TOTAL_GAMES | 9,019 | 7.7 | 8.8 | 36.5 | 27.9 | 13.2 | 3.7 | 2.4 | 9.69 | 19.3% | 6.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 24,326 | 43.8% | 24.0% | 13.0 | 35.7% | 15.2% | 10.85 |
| gen1_elo | 24,326 | 43.4% | 23.6% | 12.67 | 34.9% | 15.2% | 10.48 |
| gen1_sr | 24,326 | 51.7% | 30.3% | 15.63 | 44.3% | 21.4% | 13.11 |
| gen2 | 24,326 | 50.7% | 30.6% | 15.4 | 44.4% | 23.0% | 13.09 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 12,842 | 16.0 | 10.5 | 21.2 | 17.4 | 20.2 | 11.5 | 3.2 | 10.65 | 35.0% | 14.8% |
| STALE | 11,484 | 10.3 | 6.6 | 15.3 | 14.0 | 19.4 | 18.1 | 16.2 | 16.87 | 53.7% | 34.3% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 12,645 | 16.7 | 11.2 | 22.6 | 15.1 | 17.5 | 12.1 | 4.8 | 9.85 | 34.4% | 16.9% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 43,503 | 12645 | 16314 | 14544 | 23.6 | 124.6 | 1400.4 |
| ge_15pp | 17,812 | 4352 | 5780 | 7680 | 25.7 | 418.8 | 1380.4 |
| ge_25pp | 9,436 | 2142 | 2487 | 4807 | 31.1 | 564.8 | 1380.4 |
| lt_10pp | 18,988 | 6389 | 7755 | 4844 | 21.7 | 47.3 | 1341.5 |

Current slate `SL-20261020T093940Z-22eaf4d7`: 644 priced rows, quote age at build {'median': 13.3, 'max': 13.4}, freshness {'AGING': 644}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 12 | 0.0 | 0.0 | 33.3 | 0.0 | 50.0 | 16.7 | 0.0 | 20.33 | 66.7% | 16.7% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,286 | 20.2 | 10.7 | 23.6 | 18.8 | 19.1 | 7.0 | 0.7 | 9.02 | 26.8% | 7.7% |
| KALSHI_LONE_OUTLIER | 14 | 7.1 | 7.1 | 71.4 | 0.0 | 7.1 | 7.1 | 0.0 | 5.35 | 14.3% | 7.1% |
| MARKETS_AGREE | 403 | 68.0 | 32.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.11 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 880 | 0.0 | 2.7 | 34.8 | 27.6 | 24.4 | 9.9 | 0.6 | 12.27 | 34.9% | 10.4% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 24,326 | 3607 (14.8%) | 24.4% | 0.7% | {"EXTERNAL_STALE": 2286, "AGREES_WITH_KALSHI": 880, "ALL_AGREE": 403, "AGREES_WITH_MODEL": 14, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 11, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 10,661 | 929 (8.7%) | 33.1% | 1.1% | {"EXTERNAL_STALE": 612, "AGREES_WITH_KALSHI": 307, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 5,832 | 270 (4.6%) | 34.1% | 1.1% | {"EXTERNAL_STALE": 175, "AGREES_WITH_KALSHI": 92, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,886 | 256 (8.9%) | 35.2% | 1.2% | {"EXTERNAL_STALE": 163, "AGREES_WITH_KALSHI": 90, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 9,830 | 2006 (20.4%) | 16.4% | 0.8% | {"EXTERNAL_STALE": 1245, "ALL_AGREE": 403, "AGREES_WITH_KALSHI": 330, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 12, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 4,681 | 10.8 | 7.9 | 19.5 | 14.8 | 22.0 | 15.4 | 9.6 | 13.83 | 47.0% | 25.0% |
| 4-10x | 3,180 | 11.6 | 8.5 | 18.6 | 15.6 | 20.8 | 15.0 | 9.8 | 13.54 | 45.6% | 24.8% |
| <2x | 12,569 | 15.3 | 9.7 | 18.9 | 16.9 | 18.3 | 12.7 | 8.3 | 11.74 | 39.2% | 21.0% |
| >=10x | 3,896 | 11.3 | 6.5 | 15.4 | 13.5 | 21.6 | 19.5 | 12.2 | 16.32 | 53.4% | 31.8% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 6,202 | 12.7 | 8.6 | 19.8 | 16.2 | 19.7 | 13.2 | 9.8 | 12.69 | 42.7% | 23.0% |
| 300-1000 | 5,318 | 12.0 | 8.8 | 16.8 | 15.7 | 21.0 | 16.1 | 9.6 | 13.82 | 46.6% | 25.7% |
| <300 | 7,541 | 9.1 | 5.8 | 15.5 | 14.5 | 22.9 | 20.2 | 12.1 | 16.93 | 55.1% | 32.2% |
| >=3000 | 5,265 | 21.5 | 12.7 | 22.6 | 17.0 | 14.6 | 6.8 | 4.8 | 8.09 | 26.2% | 11.6% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 716 | 0.5439 | 0.4092 | 0.4972 | +0.047 | -0.088 | -0.001 ± 0.0056 |
| ratio 4-10x | 491 | 0.5927 | 0.4499 | 0.5132 | +0.080 | -0.063 | 0.0083 ± 0.0072 |
| ratio <2x | 1757 | 0.5376 | 0.4164 | 0.4519 | +0.086 | -0.035 | 0.012 ± 0.0034 |
| ratio >=10x | 601 | 0.5639 | 0.3902 | 0.4493 | +0.115 | -0.059 | 0.0117 ± 0.0075 |
| thinner_sample 1000-3000 | 982 | 0.5434 | 0.4173 | 0.4582 | +0.085 | -0.041 | 0.0095 ± 0.0045 |
| thinner_sample 300-1000 | 847 | 0.5667 | 0.426 | 0.4994 | +0.067 | -0.073 | -0.0001 ± 0.0054 |
| thinner_sample <300 | 1127 | 0.5554 | 0.3922 | 0.4552 | +0.100 | -0.063 | 0.0129 ± 0.0052 |
| thinner_sample >=3000 | 609 | 0.5325 | 0.4391 | 0.4696 | +0.063 | -0.030 | 0.0125 ± 0.0047 |
| data_status ADEQUATE | 1038 | 0.5354 | 0.4312 | 0.4595 | +0.076 | -0.028 | 0.0111 ± 0.0038 |
| data_status LIMITED | 871 | 0.5531 | 0.4223 | 0.4879 | +0.065 | -0.066 | 0.0032 ± 0.005 |
| data_status POOR | 1656 | 0.5594 | 0.4013 | 0.465 | +0.095 | -0.064 | 0.0103 ± 0.0042 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 538 | 0.1954 | 0.1967 | -0.0014 ± 0.0007 | 0.5692 | 0.572 | 0.4984 | 0.4835 | 0.5372 | -0.049 ± 0.02 | -0.01 (5) |
| 3-5 | 342 | 0.1988 | 0.1981 | +0.0007 ± 0.0019 | 0.58 | 0.5769 | 0.5058 | 0.4657 | 0.4766 | -0.091 ± 0.0247 | 0.02 (1) |
| 5-10 | 740 | 0.2005 | 0.201 | -0.0005 ± 0.0025 | 0.5869 | 0.5864 | 0.5129 | 0.4385 | 0.4743 | -0.082 ± 0.0172 | -0.0167 (6) |
| 10-15 | 630 | 0.2144 | 0.2054 | +0.0090 ± 0.0045 | 0.6189 | 0.593 | 0.5264 | 0.4021 | 0.427 | -0.098 ± 0.018 | -0.048 (5) |
| 15-25 | 786 | 0.2267 | 0.2146 | +0.0122 ± 0.0064 | 0.6472 | 0.6139 | 0.5803 | 0.385 | 0.4517 | -0.088 ± 0.0164 | -0.0033 (9) |
| 25-40 | 441 | 0.223 | 0.2086 | +0.0144 ± 0.0129 | 0.6341 | 0.5998 | 0.6552 | 0.3473 | 0.4762 | -0.074 ± 0.0197 | -0.01 (1) |
| 40+ | 88 | 0.2969 | 0.1747 | +0.1221 ± 0.0399 | 0.8097 | 0.5224 | 0.7569 | 0.308 | 0.3977 | -0.126 ± 0.0384 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2567 | 0.1801 | 0.1815 | -0.0014 ± 0.0003 | 0.535 | 0.5368 | 0.4805 | 0.4653 | 0.5072 | -0.016 ± 0.0085 | -0.0129 (17) |
| 3-5 | 1654 | 0.1939 | 0.1923 | +0.0016 ± 0.0009 | 0.5685 | 0.5609 | 0.483 | 0.4431 | 0.442 | -0.060 ± 0.011 | 0.0 (2) |
| 5-10 | 3576 | 0.197 | 0.1946 | +0.0025 ± 0.0011 | 0.5768 | 0.5684 | 0.4856 | 0.4119 | 0.4306 | -0.045 ± 0.0075 | -0.0119 (21) |
| 10-15 | 3164 | 0.2047 | 0.187 | +0.0177 ± 0.0019 | 0.5971 | 0.5472 | 0.4882 | 0.3636 | 0.3549 | -0.073 ± 0.0077 | -0.0281 (16) |
| 15-25 | 3863 | 0.2083 | 0.1711 | +0.0372 ± 0.0026 | 0.6078 | 0.5062 | 0.5011 | 0.305 | 0.3093 | -0.070 ± 0.0066 | -0.0025 (44) |
| 25-40 | 2937 | 0.2221 | 0.1264 | +0.0958 ± 0.0041 | 0.6386 | 0.389 | 0.5313 | 0.2186 | 0.2254 | -0.068 ± 0.0063 | -0.01 (1) |
| 40+ | 1943 | 0.3798 | 0.0426 | +0.3372 ± 0.0052 | 0.9884 | 0.1692 | 0.6298 | 0.1069 | 0.0566 | -0.088 ± 0.0044 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 403 | 0.2003 | 0.2008 | -0.0005 ± 0.0008 | 0.5826 | 0.5837 | 0.5036 | 0.4887 | 0.5087 | -0.091 ± 0.0239 | -0.01 (3) |
| 3-5 | 291 | 0.2179 | 0.2169 | +0.0011 ± 0.0022 | 0.6207 | 0.6186 | 0.5167 | 0.4768 | 0.4777 | -0.100 ± 0.0291 | 0.02 (1) |
| 5-10 | 631 | 0.199 | 0.1996 | -0.0006 ± 0.0027 | 0.5814 | 0.5825 | 0.5465 | 0.4715 | 0.5135 | -0.071 ± 0.0183 | -0.01 (4) |
| 10-15 | 595 | 0.2173 | 0.2106 | +0.0068 ± 0.0047 | 0.6248 | 0.607 | 0.5669 | 0.4425 | 0.4807 | -0.098 ± 0.0196 | -0.04 (5) |
| 15-25 | 854 | 0.2305 | 0.2101 | +0.0204 ± 0.0062 | 0.6529 | 0.6031 | 0.592 | 0.3956 | 0.4461 | -0.097 ± 0.0159 | -0.0133 (9) |
| 25-40 | 581 | 0.2621 | 0.1998 | +0.0623 ± 0.0117 | 0.7324 | 0.5807 | 0.6647 | 0.3493 | 0.4096 | -0.116 ± 0.0181 | -0.0075 (4) |
| 40+ | 210 | 0.3648 | 0.1747 | +0.1901 ± 0.0285 | 1.0134 | 0.5194 | 0.7429 | 0.2609 | 0.319 | -0.082 ± 0.0277 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2184 | 0.1865 | 0.1871 | -0.0006 ± 0.0003 | 0.5498 | 0.5508 | 0.5026 | 0.4877 | 0.5119 | -0.034 ± 0.0096 | -0.0133 (15) |
| 3-5 | 1414 | 0.1968 | 0.1964 | +0.0004 ± 0.0009 | 0.5706 | 0.5693 | 0.5166 | 0.4767 | 0.4901 | -0.041 ± 0.012 | 0.02 (1) |
| 5-10 | 3176 | 0.1919 | 0.1914 | +0.0005 ± 0.0012 | 0.5663 | 0.5613 | 0.5076 | 0.4335 | 0.4682 | -0.028 ± 0.0079 | -0.0117 (6) |
| 10-15 | 2791 | 0.1999 | 0.1883 | +0.0117 ± 0.0021 | 0.5878 | 0.5487 | 0.5184 | 0.3938 | 0.4117 | -0.054 ± 0.0083 | -0.0189 (18) |
| 15-25 | 3972 | 0.2167 | 0.1791 | +0.0375 ± 0.0027 | 0.6277 | 0.5265 | 0.5307 | 0.3343 | 0.3404 | -0.069 ± 0.0068 | -0.0086 (42) |
| 25-40 | 3477 | 0.2499 | 0.1383 | +0.1115 ± 0.004 | 0.7054 | 0.4231 | 0.5632 | 0.2472 | 0.2307 | -0.087 ± 0.0063 | -0.0044 (18) |
| 40+ | 2690 | 0.4004 | 0.0651 | +0.3353 ± 0.0056 | 1.0564 | 0.2284 | 0.6615 | 0.1253 | 0.0937 | -0.072 ± 0.0048 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 515 | 0.1984 | 0.201 | -0.0026 ± 0.0007 | 0.5777 | 0.5837 | 0.4983 | 0.483 | 0.5592 | -0.012 ± 0.0201 | -0.0137 (8) |
| 3-5 | 378 | 0.1945 | 0.1925 | +0.0020 ± 0.0018 | 0.5667 | 0.5619 | 0.5012 | 0.4616 | 0.4577 | -0.118 ± 0.0236 | 0.0067 (3) |
| 5-10 | 771 | 0.201 | 0.1979 | +0.0032 ± 0.0024 | 0.5889 | 0.5779 | 0.5089 | 0.4351 | 0.4475 | -0.099 ± 0.0165 | -0.0071 (7) |
| 10-15 | 621 | 0.2086 | 0.2059 | +0.0027 ± 0.0045 | 0.605 | 0.5947 | 0.5399 | 0.4166 | 0.4702 | -0.079 ± 0.018 | -0.0317 (6) |
| 15-25 | 735 | 0.2342 | 0.2128 | +0.0215 ± 0.0066 | 0.6672 | 0.61 | 0.5892 | 0.3959 | 0.4367 | -0.113 ± 0.017 | -0.03 (1) |
| 25-40 | 455 | 0.211 | 0.2147 | -0.0037 ± 0.0127 | 0.6083 | 0.6135 | 0.6631 | 0.3532 | 0.5121 | -0.052 ± 0.0194 | 0.015 (2) |
| 40+ | 90 | 0.3104 | 0.1912 | +0.1192 ± 0.0412 | 0.8452 | 0.5593 | 0.763 | 0.3113 | 0.4111 | -0.112 ± 0.0425 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2489 | 0.1883 | 0.1891 | -0.0008 ± 0.0003 | 0.5537 | 0.5553 | 0.488 | 0.4728 | 0.4934 | -0.034 ± 0.0088 | -0.0163 (35) |
| 3-5 | 1735 | 0.1888 | 0.1862 | +0.0026 ± 0.0008 | 0.5552 | 0.5488 | 0.4846 | 0.4451 | 0.4323 | -0.075 ± 0.0107 | -0.0094 (18) |
| 5-10 | 3774 | 0.1961 | 0.1902 | +0.0059 ± 0.0011 | 0.5764 | 0.557 | 0.4842 | 0.4104 | 0.4059 | -0.065 ± 0.0071 | -0.01 (31) |
| 10-15 | 2959 | 0.1976 | 0.1814 | +0.0162 ± 0.0019 | 0.5805 | 0.5329 | 0.4998 | 0.3763 | 0.3724 | -0.071 ± 0.0078 | -0.015 (12) |
| 15-25 | 3951 | 0.2111 | 0.1721 | +0.0389 ± 0.0026 | 0.616 | 0.5087 | 0.5087 | 0.314 | 0.3121 | -0.074 ± 0.0066 | -0.03 (2) |
| 25-40 | 2918 | 0.2186 | 0.1263 | +0.0923 ± 0.0041 | 0.6305 | 0.3875 | 0.5315 | 0.216 | 0.231 | -0.063 ± 0.0063 | 0.01 (3) |
| 40+ | 1878 | 0.3942 | 0.0473 | +0.3469 ± 0.0057 | 1.0288 | 0.1816 | 0.6411 | 0.1121 | 0.0607 | -0.089 ± 0.0048 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 867 | 0.1968 | 0.197 | -0.0002 ± 0.0005 | 0.5741 | 0.5744 | 0.5069 | 0.4917 | 0.4971 | -0.056 ± 0.0153 | -0.0224 (49) |
| 3-5 | 608 | 0.1931 | 0.1925 | +0.0006 ± 0.0014 | 0.5642 | 0.5616 | 0.4825 | 0.4427 | 0.4523 | -0.054 ± 0.0179 | -0.0194 (34) |
| 5-10 | 1294 | 0.1999 | 0.1938 | +0.0061 ± 0.0018 | 0.5873 | 0.5696 | 0.4901 | 0.4168 | 0.4134 | -0.069 ± 0.0125 | -0.005 (78) |
| 10-15 | 823 | 0.2085 | 0.1978 | +0.0107 ± 0.0039 | 0.605 | 0.5777 | 0.5148 | 0.3917 | 0.4083 | -0.063 ± 0.0157 | 0.0014 (64) |
| 15-25 | 1109 | 0.2316 | 0.211 | +0.0206 ± 0.0054 | 0.6603 | 0.6078 | 0.5716 | 0.3767 | 0.4229 | -0.064 ± 0.0138 | -0.0214 (59) |
| 25-40 | 656 | 0.2484 | 0.2016 | +0.0468 ± 0.0108 | 0.7037 | 0.5822 | 0.6596 | 0.3472 | 0.4268 | -0.087 ± 0.0164 | -0.0219 (26) |
| 40+ | 229 | 0.3492 | 0.194 | +0.1552 ± 0.0291 | 1.0088 | 0.5691 | 0.8045 | 0.3186 | 0.4236 | -0.081 ± 0.0256 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2737 | 0.1874 | 0.1875 | -0.0001 ± 0.0003 | 0.5498 | 0.5492 | 0.5064 | 0.491 | 0.4987 | -0.040 ± 0.0083 | -0.0157 (88) |
| 3-5 | 1882 | 0.1906 | 0.1881 | +0.0025 ± 0.0008 | 0.5576 | 0.5519 | 0.4889 | 0.4492 | 0.4384 | -0.059 ± 0.0101 | -0.0209 (69) |
| 5-10 | 3825 | 0.1967 | 0.1883 | +0.0084 ± 0.0011 | 0.5782 | 0.5546 | 0.4879 | 0.4144 | 0.3966 | -0.070 ± 0.0071 | -0.0082 (132) |
| 10-15 | 2610 | 0.2037 | 0.1891 | +0.0145 ± 0.0021 | 0.5944 | 0.5563 | 0.5203 | 0.3973 | 0.3992 | -0.060 ± 0.0085 | -0.0053 (105) |
| 15-25 | 3262 | 0.2283 | 0.1972 | +0.0311 ± 0.0031 | 0.6575 | 0.5741 | 0.5627 | 0.3674 | 0.3872 | -0.065 ± 0.0078 | -0.0253 (107) |
| 25-40 | 2217 | 0.2554 | 0.1755 | +0.0800 ± 0.0056 | 0.7233 | 0.5156 | 0.6196 | 0.3058 | 0.3387 | -0.080 ± 0.0087 | -0.0229 (51) |
| 40+ | 1042 | 0.3746 | 0.1365 | +0.2381 ± 0.0121 | 1.0629 | 0.4146 | 0.7219 | 0.2179 | 0.2476 | -0.072 ± 0.0106 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3565 | 1.057 ± 0.048 | 1.185 | 0.1668 | 0.1638 | 0.213 | 0.2042 |
| gen2 | 3565 | 0.854 ± 0.043 | 1.141 | 0.1725 | 0.1643 | 0.2314 | 0.2041 |
| gen1_elo | 3565 | 1.034 ± 0.046 | 1.168 | 0.173 | 0.1642 | 0.2122 | 0.2042 |
| gen1_sr | 3565 | 1.057 ± 0.057 | 1.218 | 0.1327 | 0.1661 | 0.2275 | 0.2039 |
| gen1_ledger | 5586 | 0.881 ± 0.033 | 1.09 | 0.1786 | 0.1799 | 0.218 | 0.1991 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 17,812)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,025 | 22.6% |
| STALE_QUOTE | market_freshness | 3,738 | 21.0% |
| BOOK_QUALITY | execution | 3,473 | 19.5% |
| POOR_DATA | data | 2,044 | 11.5% |
| LIMITED_DATA | data | 1,206 | 6.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 930 | 5.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 891 | 5.0% |
| IDENTITY_AMBIGUOUS | mapping | 724 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 505 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 275 | 1.5% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.6%, market_freshness 21.0%, execution 19.5%, data 18.2%, market_freshness/coverage 8.1%, model_calibration_or_unknown 5.0%, mapping 4.1%, model_calibration 1.5%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.2%, START_UNVERIFIABLE 94.2%, LOW_DATA_QUALITY 70.3%, THIN_PLAYER_HISTORY 59.0%, STALE_PLAYER_DATA 53.0%, STALE_KALSHI_QUOTE 43.1%, MODEL_INTERNAL_DISAGREEMENT 41.4%, ASYMMETRIC_SAMPLE_SIZE 32.7%, WIDE_SPREAD 25.5%, MODEL_HIGH_UNCERTAINTY 17.9%, PLAYER_IDENTITY_RISK 15.2%, LEVEL_TRANSFER_RISK 10.2%, EVENT_MAPPING_RISK 8.3%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 2.7%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.0%, POST_SETTLEMENT_OBSERVATION 22.6%, POSSIBLE_IN_PLAY_QUOTE 5.5%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 9,436)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,185 | 33.8% |
| BOOK_QUALITY | execution | 1,826 | 19.4% |
| STALE_QUOTE | market_freshness | 1,717 | 18.2% |
| POOR_DATA | data | 859 | 9.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 490 | 5.2% |
| IDENTITY_AMBIGUOUS | mapping | 420 | 4.5% |
| LIMITED_DATA | data | 359 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 311 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 206 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 63 | 0.7% |

Cause class: coverage 33.8%, execution 19.4%, market_freshness 18.2%, data 12.9%, market_freshness/coverage 8.5%, mapping 4.5%, model_calibration_or_unknown 2.2%, model_calibration 0.7%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.4%, START_UNVERIFIABLE 97.1%, LOW_DATA_QUALITY 74.4%, THIN_PLAYER_HISTORY 61.7%, STALE_KALSHI_QUOTE 50.9%, STALE_PLAYER_DATA 48.5%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 34.7%, WIDE_SPREAD 25.3%, PLAYER_IDENTITY_RISK 18.7%, MODEL_HIGH_UNCERTAINTY 18.2%, EVENT_MAPPING_RISK 10.1%, LEVEL_TRANSFER_RISK 9.4%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 5.1%, EXTERNAL_MARKET_REJECTION 1.5%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.6%, POST_SETTLEMENT_OBSERVATION 33.8%, POSSIBLE_IN_PLAY_QUOTE 5.6%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 7427, "IDENTITY_AMBIGUOUS": 2009}; ticker orientation: {"VERIFIED": 9436}.

Checks: discipline:AMBIGUOUS 663, discipline:PASS 8773, identity_confidence:AMBIGUOUS 1762, identity_confidence:PASS 7674, level_mapping:NA 675, level_mapping:PASS 8761, market_pair:AMBIGUOUS 347, market_pair:NA 221, market_pair:PASS 8868, model_complement:NA 188, model_complement:PASS 9248, namesake:PASS 9436, physical_match_id:NA 3604, physical_match_id:PASS 5832, player_ids:PASS 9436, same_pair_other_event:PASS 9436, ticker_orientation:PASS 9436

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,368 | 4.6% | 4.4% | 1.7% | {"market_freshness": 51, "model_calibration_or_unknown": 34, "data": 29, "execution": 18, "model_calibration": 12, "market_freshness/coverage": 10, "coverage": 2} | 5.87 | 0.22 / 0.2116 (359) | 18.8% | 3.6% | 3.7% | 2.4% |
| CHALLENGER | 6,985 | 16.9% | 6.7% | 12.5% | {"coverage": 668, "market_freshness/coverage": 145, "market_freshness": 141, "data": 106, "model_calibration_or_unknown": 57, "execution": 30, "model_calibration": 19, "mapping": 14} | 7.38 | 0.2171 / 0.206 (1684) | 35.2% | 16.6% | 3.6% | 21.9% |
| DOUBLES | 1,366 | 48.5% | 48.1% | 7.0% | {"execution": 329, "mapping": 176, "market_freshness": 106, "market_freshness/coverage": 45, "coverage": 7} | 24.0 | 0.3206 / 0.2346 (352) | 17.1% | 0.0% | 100.0% | 7.0% |
| ITF_MEN | 11,759 | 24.9% | 17.6% | 31.0% | {"coverage": 1082, "execution": 605, "market_freshness": 478, "data": 399, "market_freshness/coverage": 230, "mapping": 129, "model_calibration_or_unknown": 2, "model_calibration": 1} | 11.43 | 0.2151 / 0.1955 (2712) | 36.0% | 64.4% | 15.7% | 21.9% |
| ITF_WOMEN | 15,992 | 26.3% | 19.6% | 44.6% | {"coverage": 1409, "market_freshness": 864, "execution": 813, "data": 650, "market_freshness/coverage": 322, "mapping": 95, "model_calibration_or_unknown": 47, "model_calibration": 10} | 12.88 | 0.2021 / 0.1942 (3107) | 37.7% | 58.1% | 10.2% | 21.1% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,492 | 4.6% | 4.2% | 1.2% | {"market_freshness": 37, "model_calibration_or_unknown": 25, "execution": 17, "data": 11, "market_freshness/coverage": 10, "model_calibration": 10, "coverage": 4, "mapping": 1} | 7.89 | 0.2355 / 0.2304 (407) | 23.8% | 1.4% | 1.5% | 3.5% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.8% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 5 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 6 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 7 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 8 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 9 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 10 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 11 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 12 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 13 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 14 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 15 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 16 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 17 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 18 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 19 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | POOR_DATA | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 20 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 21 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 22 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 23 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 24 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 25 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 768 min (STALE); no external reference |
| 26 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 27 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 28 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 29 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 30 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 31 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 32 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 9.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 553 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 33 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 34 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 35 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 36 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 37 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 468 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 38 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 39 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 40 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 41 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 42 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 730 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |
| 43 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 547 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 44 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 45 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 46 | `KXITFWMATCH-26OCT16ESTLAB-LAB` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 68 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1475.0, ratio 2.28); no external reference |
| 47 | `KXITFWMATCH-26OCT19VLABOU-VLA` | ITF_WOMEN | fair_v1 | 77% / 2% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.2h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 140 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 3.13); no external reference |
| 48 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 49 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 50 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9714, "by_level_share_of_ge_25pp": {"ATP": 0.0165, "CHALLENGER": 0.1251, "DOUBLES": 0.0703, "ITF_MEN": 0.3101, "ITF_WOMEN": 0.4462, "OTHER": 0.0013, "WTA": 0.0122, "WTA125": 0.0184}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5094, "share_primary_cause_market_settled_or_in_play": 0.4224, "share_primary_cause_stale_quote_only": 0.182}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 9436, "identity_ambiguous_share": 0.2129, "ticker_orientation": {"VERIFIED": 9436}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 5832, "with_external": 270, "coverage": 0.0463, "external_status": {"EXTERNAL_STALE": 175, "AGREES_WITH_KALSHI": 92, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 175, "MODEL_LONE_OUTLIER": 92, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3407, "share_external_supports_model": 0.0111}, "pregame_clean_ge_25pp": {"n": 2886, "with_external": 256, "coverage": 0.0887, "external_status": {"EXTERNAL_STALE": 163, "AGREES_WITH_KALSHI": 90, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 163, "MODEL_LONE_OUTLIER": 90, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3516, "share_external_supports_model": 0.0117}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 504.0, "median_sample_ratio": 2.47, "median_min_matches": 20.0, "median_max_days_since_last": 223.0, "share_severe_asymmetry": 0.2104, "data_status": {"POOR": 5205, "LIMITED": 2602, "ADEQUATE": 1629}, "comparison_lt_10pp": {"median_thinner_serve_points": 1761.0, "median_sample_ratio": 1.68, "median_min_matches": 93.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 716, "model_minus_observed": 0.0467, "kalshi_minus_observed": -0.088, "brier_diff_model_minus_kalshi": -0.001}, "4-10x": {"n": 491, "model_minus_observed": 0.0795, "kalshi_minus_observed": -0.0634, "brier_diff_model_minus_kalshi": 0.0083}, "<2x": {"n": 1757, "model_minus_observed": 0.0857, "kalshi_minus_observed": -0.0355, "brier_diff_model_minus_kalshi": 0.012}, ">=10x": {"n": 601, "model_minus_observed": 0.1147, "kalshi_minus_observed": -0.0591, "brier_diff_model_minus_kalshi": 0.0117}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3565, "model": {"intercept": -0.532, "slope": 0.854, "slope_se": 0.043}, "kalshi_mid_same_rows": {"intercept": 0.241, "slope": 1.141, "slope_se": 0.05}, "mean_extremity_model": 0.1725, "mean_extremity_kalshi": 0.1643, "model_brier": 0.2314, "kalshi_brier": 0.2041, "brier_diff_model_minus_kalshi": 0.0273, "brier_diff_se": 0.0032, "model_logloss": 0.6592, "kalshi_logloss": 0.5906}, "fair_v1": {"n": 3565, "model": {"intercept": -0.397, "slope": 1.057, "slope_se": 0.048}, "kalshi_mid_same_rows": {"intercept": 0.323, "slope": 1.185, "slope_se": 0.051}, "mean_extremity_model": 0.1668, "mean_extremity_kalshi": 0.1638, "model_brier": 0.213, "kalshi_brier": 0.2042, "brier_diff_model_minus_kalshi": 0.0088, "brier_diff_se": 0.0026, "model_logloss": 0.6138, "kalshi_logloss": 0.5906}, "gen1_elo": {"n": 3565, "model": {"intercept": -0.388, "slope": 1.034, "slope_se": 0.046}, "kalshi_mid_same_rows": {"intercept": 0.318, "slope": 1.168, "slope_se": 0.05}, "mean_extremity_model": 0.173, "mean_extremity_kalshi": 0.1642, "model_brier": 0.2122, "kalshi_brier": 0.2042, "brier_diff_model_minus_kalshi": 0.008, "brier_diff_se": 0.0026, "model_logloss": 0.6128, "kalshi_logloss": 0.5907}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2397, "share_ge_15": 0.4383, "median_abs_gap": 13.0, "n": 24326}, "gen1_elo": {"share_ge_25": 0.2364, "share_ge_15": 0.4342, "median_abs_gap": 12.67, "n": 24326}, "gen1_sr": {"share_ge_25": 0.3029, "share_ge_15": 0.5173, "median_abs_gap": 15.63, "n": 24326}, "gen2": {"share_ge_25": 0.3064, "share_ge_15": 0.5075, "median_abs_gap": 15.4, "n": 24326}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1516, "share_ge_15": 0.3566, "median_abs_gap": 10.85, "n": 19039}, "gen1_elo": {"share_ge_25": 0.1516, "share_ge_15": 0.3493, "median_abs_gap": 10.48, "n": 19037}, "gen1_sr": {"share_ge_25": 0.2143, "share_ge_15": 0.4432, "median_abs_gap": 13.11, "n": 19039}, "gen2": {"share_ge_25": 0.2304, "share_ge_15": 0.4444, "median_abs_gap": 13.09, "n": 19040}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.87, "share_ge_25_all": 0.0463, "share_ge_25_pregame_clean": 0.0438}, "WTA": {"median_abs_gap_pregame_clean": 7.89, "share_ge_25_all": 0.0461, "share_ge_25_pregame_clean": 0.042}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2381, "share_within_10pp_all": 0.4365, "share_within_10pp_pregame_clean": 0.488, "corr_model_vs_mid_pregame_clean": 0.8429}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 538, "model_brier": 0.1954, "kalshi_brier": 0.1967, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 630, "model_brier": 0.2144, "kalshi_brier": 0.2054, "brier_diff_model_minus_kalshi": 0.009}, "15-25": {"n_settled": 786, "model_brier": 0.2267, "kalshi_brier": 0.2146, "brier_diff_model_minus_kalshi": 0.0122}, "25-40": {"n_settled": 441, "model_brier": 0.223, "kalshi_brier": 0.2086, "brier_diff_model_minus_kalshi": 0.0144}, "3-5": {"n_settled": 342, "model_brier": 0.1988, "kalshi_brier": 0.1981, "brier_diff_model_minus_kalshi": 0.0007}, "40+": {"n_settled": 88, "model_brier": 0.2969, "kalshi_brier": 0.1747, "brier_diff_model_minus_kalshi": 0.1221}, "5-10": {"n_settled": 740, "model_brier": 0.2005, "kalshi_brier": 0.201, "brier_diff_model_minus_kalshi": -0.0005}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.532, "slope": 0.854, "slope_se": 0.043}, "kalshi_slope": {"intercept": 0.241, "slope": 1.141, "slope_se": 0.05}, "n": 3565}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.509, "slope": 0.881, "slope_se": 0.033}, "kalshi_slope": {"intercept": 0.16, "slope": 1.09, "slope_se": 0.038}, "n": 5586}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 352, "model_brier": 0.3206, "kalshi_brier": 0.2346, "brier_diff_model_minus_kalshi": 0.0861, "brier_diff_se": 0.0167, "corr_model_outcome": 0.0143, "corr_kalshi_outcome": 0.2592}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
