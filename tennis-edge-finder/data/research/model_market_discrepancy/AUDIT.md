# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-11T22:32Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 29,387): 0-3 14.6%, 3-5 9.7%, 5-10 20.2%, 10-15 15.4%, 15-25 18.4%, 25-40 13.5%, 40+ 8.2%; median gap 11.67 pp.
* **Where the extremes live**: 98.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.4%, Challenger 12.2%, doubles 7.2%). Main tour: ATP 1.4% and WTA 6.5% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 6,373): MARKET_ALREADY_SETTLED_WHEN_PRICED 39.3%, BOOK_QUALITY 17.5%, STALE_QUOTE 16.1%, POOR_DATA 7.8%, POSSIBLY_IN_PLAY_QUOTE 5.7%, LIMITED_DATA 4.2%, IDENTITY_AMBIGUOUS 3.7%, IN_PLAY_QUOTE 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 1.8%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.4%. By class: coverage 39.3%, execution 17.5%, market_freshness 16.1%, data 12.0%, market_freshness/coverage 9.2%, mapping 3.7%, model_calibration_or_unknown 1.8%, model_calibration 0.4%.
* **Stale / settled / in-play**: 54.3% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 48.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 6,373 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 17.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 2.7%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 20.1% of the time and with the model 0.5%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 620.0 points vs 1937.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.076, Gen-2 0.872, Gen-1 ledger 0.878 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 273 model 0.218 vs Kalshi 0.2006; n 59 model 0.2961 vs Kalshi 0.17.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 117,133 model-market comparisons (192,357 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 43,921 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-11T22:23:46.895991+00:00'], shadow board 30,895 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-11T22:23:51.599530+00:00'], Model 4 13,195 rows, 12,783 settled tickers, 3,576 tickers with an external scan.
* By model: {"gen1_ledger": 28950, "gen1_elo": 15526, "fair_v1": 15526, "gen2": 15526, "gen1_sr": 15526, "model4_fundamental": 13044, "model4_conditioned": 13035}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 29,387 | 14.6 | 9.7 | 20.2 | 15.4 | 18.4 | 13.5 | 8.2 | 11.67 | 40.1% | 21.7% |
| MW fair_v1 | 15,526 | 13.9 | 8.7 | 18.7 | 16.1 | 18.4 | 14.4 | 9.8 | 12.69 | 42.6% | 24.2% |
| MW gen1_elo | 15,526 | 13.4 | 9.1 | 20.3 | 15.0 | 18.6 | 14.3 | 9.3 | 12.16 | 42.2% | 23.6% |
| MW gen1_ledger | 13,861 | 15.4 | 10.7 | 21.9 | 14.6 | 18.5 | 12.5 | 6.3 | 10.48 | 37.3% | 18.8% |
| MW gen1_sr | 15,526 | 10.1 | 7.9 | 16.6 | 14.5 | 21.6 | 17.9 | 11.5 | 15.37 | 50.9% | 29.4% |
| MW gen2 | 15,526 | 12.1 | 7.4 | 16.4 | 14.2 | 20.1 | 16.9 | 12.9 | 14.97 | 49.9% | 29.8% |
| all families model4_conditioned | 13,035 | 21.9 | 20.1 | 35.8 | 16.0 | 4.3 | 1.0 | 0.9 | 5.77 | 6.2% | 1.9% |
| all families model4_fundamental | 13,044 | 16.7 | 13.3 | 36.0 | 19.8 | 10.6 | 2.6 | 1.1 | 7.63 | 14.3% | 3.7% |

Configurable thresholds (primary): >=5pp 75.7%, >=10pp 55.5%, >=15pp 40.1%, >=20pp 29.9%, >=25pp 21.7%, >=30pp 15.9%, >=40pp 8.2%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.25pp; >=10pp 44.8%, >=25pp 17.4%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,268 | 30.5 | 14.4 | 24.7 | 17.7 | 10.7 | 1.1 | 0.9 | 5.84 | 12.7% | 2.0% |
| CHALLENGER | 2,706 | 15.8 | 10.2 | 19.9 | 15.9 | 14.2 | 12.3 | 11.6 | 11.59 | 38.2% | 23.9% |
| ITF_MEN | 4,330 | 11.5 | 8.8 | 18.3 | 14.8 | 19.0 | 15.3 | 12.2 | 13.74 | 46.6% | 27.6% |
| ITF_WOMEN | 5,993 | 10.2 | 6.6 | 16.0 | 16.2 | 21.5 | 18.7 | 10.8 | 15.44 | 51.0% | 29.5% |
| WTA | 774 | 22.1 | 10.7 | 25.4 | 16.5 | 18.0 | 5.8 | 1.4 | 7.83 | 25.2% | 7.2% |
| WTA125 | 455 | 13.0 | 8.3 | 23.7 | 21.1 | 17.4 | 14.7 | 1.8 | 11.07 | 33.9% | 16.5% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,268 | 24.1 | 14.4 | 24.6 | 19.1 | 14.9 | 1.9 | 1.0 | 6.9 | 17.8% | 2.9% |
| CHALLENGER | 2,706 | 15.5 | 7.4 | 19.1 | 13.2 | 18.3 | 14.1 | 12.3 | 12.86 | 44.8% | 26.5% |
| ITF_MEN | 4,330 | 10.3 | 7.4 | 16.7 | 14.6 | 19.9 | 17.8 | 13.2 | 15.43 | 50.8% | 31.0% |
| ITF_WOMEN | 5,993 | 8.9 | 5.9 | 12.8 | 12.8 | 21.6 | 20.9 | 17.1 | 19.09 | 59.6% | 38.0% |
| WTA | 774 | 19.6 | 8.4 | 18.2 | 15.5 | 21.8 | 15.0 | 1.4 | 11.56 | 38.2% | 16.4% |
| WTA125 | 455 | 4.8 | 4.0 | 18.5 | 20.0 | 24.6 | 18.2 | 9.9 | 16.74 | 52.8% | 28.1% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,268 | 27.2 | 14.3 | 29.5 | 15.0 | 10.6 | 2.5 | 0.9 | 6.14 | 14.0% | 3.5% |
| CHALLENGER | 2,706 | 15.3 | 10.4 | 20.6 | 15.5 | 14.8 | 11.9 | 11.5 | 10.88 | 38.2% | 23.4% |
| ITF_MEN | 4,330 | 10.5 | 8.8 | 19.0 | 13.7 | 19.9 | 15.7 | 12.4 | 14.02 | 48.0% | 28.1% |
| ITF_WOMEN | 5,993 | 9.8 | 6.7 | 16.6 | 15.6 | 22.6 | 19.0 | 9.6 | 15.52 | 51.2% | 28.6% |
| WTA | 774 | 22.4 | 14.7 | 33.7 | 15.5 | 10.2 | 2.6 | 0.9 | 6.3 | 13.7% | 3.5% |
| WTA125 | 455 | 23.7 | 10.6 | 30.3 | 15.2 | 13.4 | 6.4 | 0.4 | 7.52 | 20.2% | 6.8% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 697 | 30.9 | 22.5 | 35.9 | 9.0 | 1.3 | 0.4 | 0.0 | 4.72 | 1.7% | 0.4% |
| CHALLENGER | 1,855 | 22.4 | 16.0 | 26.9 | 14.8 | 12.9 | 5.0 | 1.9 | 6.81 | 19.8% | 6.9% |
| DOUBLES | 908 | 4.5 | 3.2 | 11.3 | 11.2 | 19.4 | 24.8 | 25.6 | 25.4 | 69.7% | 50.3% |
| ITF_MEN | 4,140 | 14.9 | 8.6 | 21.1 | 15.4 | 20.3 | 12.2 | 7.4 | 11.71 | 40.0% | 19.6% |
| ITF_WOMEN | 4,872 | 11.6 | 9.3 | 19.6 | 14.5 | 22.5 | 16.7 | 5.8 | 13.09 | 45.0% | 22.5% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 625 | 21.1 | 14.9 | 27.0 | 17.3 | 14.1 | 5.1 | 0.5 | 7.78 | 19.7% | 5.6% |
| WTA125 | 615 | 20.3 | 13.7 | 21.8 | 18.4 | 15.0 | 8.5 | 2.4 | 8.37 | 25.9% | 10.9% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,256 | 30.4 | 14.3 | 24.8 | 17.8 | 10.7 | 1.1 | 0.9 | 5.84 | 12.7% | 2.0% |
| CHALLENGER | 1,953 | 20.3 | 12.8 | 25.0 | 18.5 | 14.8 | 6.1 | 2.4 | 8.31 | 23.4% | 8.6% |
| ITF_MEN | 3,054 | 14.5 | 11.1 | 22.0 | 16.7 | 19.0 | 11.9 | 4.9 | 10.62 | 35.8% | 16.8% |
| ITF_WOMEN | 4,239 | 12.6 | 8.3 | 18.8 | 19.0 | 23.1 | 14.8 | 3.3 | 12.62 | 41.2% | 18.1% |
| WTA | 769 | 22.0 | 10.8 | 25.6 | 16.5 | 17.9 | 5.7 | 1.4 | 7.82 | 25.1% | 7.1% |
| WTA125 | 434 | 13.6 | 8.1 | 23.0 | 21.7 | 18.0 | 14.5 | 1.1 | 11.08 | 33.6% | 15.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,256 | 23.9 | 14.5 | 24.7 | 19.1 | 14.9 | 1.9 | 1.0 | 6.9 | 17.8% | 2.9% |
| CHALLENGER | 1,953 | 19.9 | 9.4 | 23.9 | 15.8 | 18.8 | 9.5 | 2.7 | 9.08 | 30.9% | 12.1% |
| ITF_MEN | 3,055 | 12.5 | 9.0 | 19.5 | 16.5 | 21.6 | 14.9 | 5.9 | 12.52 | 42.4% | 20.8% |
| ITF_WOMEN | 4,239 | 10.5 | 7.0 | 14.6 | 14.0 | 24.5 | 19.4 | 10.0 | 16.32 | 53.9% | 29.4% |
| WTA | 769 | 19.6 | 8.4 | 18.2 | 15.6 | 21.7 | 14.9 | 1.4 | 11.5 | 38.1% | 16.4% |
| WTA125 | 434 | 4.8 | 4.2 | 18.7 | 20.5 | 24.2 | 18.9 | 8.8 | 16.14 | 51.8% | 27.7% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 677 | 30.9 | 22.8 | 36.2 | 9.2 | 0.6 | 0.4 | 0.0 | 4.69 | 1.0% | 0.4% |
| CHALLENGER | 1,584 | 24.4 | 17.7 | 29.2 | 14.7 | 11.9 | 2.0 | 0.2 | 6.17 | 14.0% | 2.1% |
| DOUBLES | 841 | 4.5 | 3.2 | 11.7 | 11.3 | 19.5 | 24.6 | 25.2 | 24.85 | 69.3% | 49.8% |
| ITF_MEN | 3,340 | 16.7 | 9.4 | 23.4 | 16.4 | 20.1 | 9.8 | 4.2 | 10.07 | 34.1% | 14.0% |
| ITF_WOMEN | 3,982 | 12.8 | 10.0 | 21.5 | 15.4 | 22.8 | 15.0 | 2.6 | 11.64 | 40.4% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 595 | 21.5 | 15.5 | 27.6 | 17.3 | 14.3 | 3.9 | 0.0 | 7.33 | 18.1% | 3.9% |
| WTA125 | 517 | 22.4 | 15.3 | 23.4 | 20.3 | 13.2 | 5.0 | 0.4 | 7.42 | 18.6% | 5.4% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 908 | 4.5 | 3.2 | 11.3 | 11.2 | 19.4 | 24.8 | 25.6 | 25.4 | 69.7% | 50.3% |
| singles | 12,953 | 16.2 | 11.2 | 22.7 | 14.9 | 18.4 | 11.6 | 5.0 | 9.95 | 35.0% | 16.6% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 3,546 | 13.4 | 9.5 | 20.7 | 15.8 | 16.8 | 13.8 | 9.9 | 12.04 | 40.6% | 23.8% |
| Grass | 57 | 12.3 | 28.1 | 14.0 | 7.0 | 22.8 | 15.8 | 0.0 | 8.85 | 38.6% | 15.8% |
| Hard | 10,392 | 14.4 | 8.4 | 18.5 | 15.9 | 18.7 | 14.3 | 9.7 | 12.69 | 42.7% | 24.0% |
| UNKNOWN | 1,531 | 11.5 | 8.2 | 15.6 | 17.8 | 19.7 | 16.9 | 10.4 | 14.09 | 47.0% | 27.3% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,832 | 20.2 | 10.7 | 21.1 | 17.1 | 14.9 | 8.8 | 7.2 | 9.45 | 30.9% | 16.0% |
| B | 2,100 | 14.4 | 9.4 | 19.7 | 17.3 | 17.2 | 12.1 | 9.9 | 11.5 | 39.2% | 22.1% |
| C | 2,303 | 13.2 | 9.7 | 19.4 | 14.6 | 19.0 | 14.8 | 9.3 | 12.69 | 43.1% | 24.1% |
| D | 2,776 | 10.8 | 8.4 | 18.1 | 16.1 | 21.9 | 14.8 | 9.9 | 13.78 | 46.6% | 24.7% |
| F | 3,515 | 7.8 | 5.2 | 14.9 | 14.8 | 20.6 | 23.1 | 13.5 | 18.39 | 57.2% | 36.6% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,097 | 22.4 | 15.9 | 28.6 | 15.3 | 11.6 | 4.5 | 1.7 | 6.78 | 17.8% | 6.2% |
| B | 2,160 | 15.2 | 9.8 | 24.0 | 16.2 | 19.3 | 11.2 | 4.3 | 10.19 | 34.8% | 15.6% |
| C | 2,767 | 12.2 | 7.6 | 17.9 | 14.4 | 20.6 | 15.8 | 11.4 | 13.77 | 47.8% | 27.3% |
| D | 2,172 | 14.1 | 9.7 | 21.2 | 13.3 | 21.6 | 13.9 | 6.3 | 11.83 | 41.8% | 20.1% |
| F | 2,665 | 9.4 | 7.5 | 14.8 | 13.7 | 23.7 | 21.1 | 9.9 | 16.87 | 54.7% | 31.0% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 5,308 | 18.5 | 9.8 | 20.3 | 17.2 | 15.0 | 9.7 | 9.6 | 10.42 | 34.3% | 19.3% |
| LIMITED | 3,883 | 15.2 | 10.6 | 20.6 | 15.7 | 18.4 | 12.8 | 6.8 | 11.08 | 38.0% | 19.6% |
| POOR | 6,335 | 9.2 | 6.7 | 16.3 | 15.4 | 21.2 | 19.4 | 11.8 | 15.99 | 52.4% | 31.2% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,870 | 31.0 | 24.3 | 36.5 | 5.6 | 1.9 | 0.7 | 0.1 | 4.54 | 2.6% | 0.8% |
| GAME_SPREAD | 2,775 | 25.4 | 15.8 | 36.9 | 16.9 | 4.3 | 0.4 | 0.2 | 6.05 | 4.9% | 0.6% |
| MATCH_WINNER | 13,861 | 15.4 | 10.7 | 21.9 | 14.6 | 18.5 | 12.5 | 6.3 | 10.48 | 37.3% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 5,241 | 32.9 | 19.4 | 31.0 | 9.9 | 5.3 | 1.2 | 0.2 | 4.79 | 6.8% | 1.4% |
| TOTAL_GAMES | 4,179 | 6.7 | 8.9 | 38.8 | 30.0 | 10.4 | 2.8 | 2.4 | 9.53 | 15.6% | 5.2% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,690 | 25.5 | 37.9 | 31.7 | 0.3 | 4.0 | 0.5 | 0.1 | 4.32 | 4.6% | 0.6% |
| GAME_SPREAD | 3,329 | 44.9 | 15.9 | 29.4 | 7.5 | 1.2 | 0.8 | 0.4 | 3.6 | 2.3% | 1.1% |
| TOTAL_GAMES | 5,016 | 3.2 | 6.4 | 43.8 | 36.3 | 6.5 | 1.7 | 2.0 | 9.66 | 10.2% | 3.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,690 | 26.0 | 18.6 | 37.1 | 9.4 | 6.4 | 2.1 | 0.3 | 5.54 | 8.9% | 2.5% |
| GAME_SPREAD | 3,329 | 18.9 | 12.9 | 30.4 | 21.2 | 13.4 | 2.4 | 0.7 | 7.91 | 16.5% | 3.1% |
| TOTAL_GAMES | 5,025 | 6.5 | 8.5 | 38.5 | 28.6 | 12.6 | 3.1 | 2.2 | 9.65 | 17.8% | 5.3% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 15,526 | 42.6% | 24.2% | 12.69 | 32.4% | 13.6% | 10.1 |
| gen1_elo | 15,526 | 42.2% | 23.6% | 12.16 | 31.8% | 13.4% | 9.56 |
| gen1_sr | 15,526 | 50.9% | 29.4% | 15.37 | 41.7% | 18.7% | 12.48 |
| gen2 | 15,526 | 49.9% | 29.8% | 14.97 | 42.1% | 20.5% | 12.39 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 8,187 | 16.9 | 11.0 | 21.7 | 17.6 | 18.5 | 11.1 | 3.2 | 10.09 | 32.9% | 14.3% |
| STALE | 7,339 | 10.6 | 6.2 | 15.4 | 14.4 | 18.2 | 18.2 | 17.1 | 16.93 | 53.4% | 35.3% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 7,329 | 17.5 | 11.7 | 23.9 | 14.5 | 16.7 | 11.0 | 4.7 | 9.22 | 32.4% | 15.7% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 29,387 | 7329 | 11659 | 10399 | 24.4 | 149.7 | 1400.4 |
| ge_15pp | 11,785 | 2371 | 3981 | 5433 | 27.8 | 454.2 | 1380.4 |
| ge_25pp | 6,373 | 1147 | 1765 | 3461 | 34.6 | 579.8 | 1380.4 |
| lt_10pp | 13,080 | 3895 | 5690 | 3495 | 22.7 | 49.2 | 1341.5 |

Current slate `SL-20261011T223213Z-d79fbee4`: 510 priced rows, quote age at build {'median': 8.7, 'max': 8.8}, freshness {'FRESH': 510}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 8 | 0.0 | 0.0 | 37.5 | 0.0 | 37.5 | 25.0 | 0.0 | 20.45 | 62.5% | 25.0% |
| EXTERNAL_LONE_OUTLIER | 8 | 62.5 | 37.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.43 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,097 | 23.0 | 11.2 | 23.1 | 19.0 | 17.3 | 6.1 | 0.4 | 8.38 | 23.8% | 6.5% |
| KALSHI_LONE_OUTLIER | 1 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 5.14 | 0.0% | 0.0% |
| MARKETS_AGREE | 192 | 72.4 | 27.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.99 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 329 | 0.0 | 4.0 | 37.1 | 31.3 | 19.4 | 7.9 | 0.3 | 11.24 | 27.7% | 8.2% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 15,526 | 1635 (10.5%) | 20.1% | 0.5% | {"EXTERNAL_STALE": 1097, "AGREES_WITH_KALSHI": 329, "ALL_AGREE": 192, "EXTERNAL_OUTLIER": 8, "SUPPORTS_MODEL_DIRECTION": 7, "ALL_DISAGREE": 1, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_15pp | 6,615 | 357 (5.4%) | 25.5% | 1.4% | {"EXTERNAL_STALE": 261, "AGREES_WITH_KALSHI": 91, "SUPPORTS_MODEL_DIRECTION": 5} |
| fair_v1_ge_25pp | 3,764 | 100 (2.7%) | 27.0% | 2.0% | {"EXTERNAL_STALE": 71, "AGREES_WITH_KALSHI": 27, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_ge_25pp_pregame_clean | 1,596 | 95 (5.9%) | 26.3% | 2.1% | {"EXTERNAL_STALE": 68, "AGREES_WITH_KALSHI": 25, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_lt_10pp | 6,416 | 967 (15.1%) | 14.0% | 0.3% | {"EXTERNAL_STALE": 628, "ALL_AGREE": 192, "AGREES_WITH_KALSHI": 135, "EXTERNAL_OUTLIER": 8, "SUPPORTS_MODEL_DIRECTION": 2, "ALL_DISAGREE": 1, "AGREES_WITH_MODEL": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,094 | 11.7 | 8.4 | 19.6 | 15.3 | 21.0 | 13.9 | 10.1 | 13.24 | 45.0% | 24.0% |
| 4-10x | 2,095 | 11.7 | 9.0 | 19.4 | 15.1 | 19.6 | 15.9 | 9.3 | 13.1 | 44.8% | 25.2% |
| <2x | 8,357 | 16.0 | 9.3 | 18.9 | 17.2 | 16.8 | 12.7 | 9.2 | 11.68 | 38.7% | 21.9% |
| >=10x | 1,980 | 11.0 | 6.4 | 15.9 | 13.5 | 19.6 | 21.0 | 12.6 | 16.49 | 53.2% | 33.6% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 4,117 | 14.1 | 8.4 | 19.4 | 16.0 | 18.5 | 12.8 | 10.9 | 12.46 | 42.1% | 23.6% |
| 300-1000 | 3,653 | 12.0 | 8.9 | 17.1 | 16.1 | 21.0 | 15.8 | 9.1 | 13.67 | 45.9% | 24.9% |
| <300 | 4,041 | 8.5 | 6.1 | 15.9 | 14.7 | 20.6 | 21.3 | 12.9 | 17.11 | 54.8% | 34.2% |
| >=3000 | 3,715 | 21.4 | 11.7 | 22.5 | 17.7 | 13.3 | 7.5 | 5.9 | 8.45 | 26.7% | 13.4% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 498 | 0.5381 | 0.4072 | 0.4799 | +0.058 | -0.073 | 0.0019 ± 0.0065 |
| ratio 4-10x | 339 | 0.5803 | 0.4396 | 0.5162 | +0.064 | -0.077 | 0.0027 ± 0.0086 |
| ratio <2x | 1167 | 0.539 | 0.4181 | 0.4584 | +0.081 | -0.040 | 0.0109 ± 0.0041 |
| ratio >=10x | 335 | 0.5482 | 0.3808 | 0.4358 | +0.112 | -0.055 | 0.0146 ± 0.0096 |
| thinner_sample 1000-3000 | 660 | 0.5451 | 0.422 | 0.4773 | +0.068 | -0.055 | 0.0048 ± 0.0055 |
| thinner_sample 300-1000 | 600 | 0.5641 | 0.4249 | 0.4867 | +0.077 | -0.062 | 0.0024 ± 0.0063 |
| thinner_sample <300 | 666 | 0.5431 | 0.3832 | 0.452 | +0.091 | -0.069 | 0.0126 ± 0.0066 |
| thinner_sample >=3000 | 413 | 0.5264 | 0.4326 | 0.4528 | +0.074 | -0.020 | 0.0159 ± 0.0056 |
| data_status ADEQUATE | 654 | 0.5305 | 0.4288 | 0.4511 | +0.080 | -0.022 | 0.0113 ± 0.0047 |
| data_status LIMITED | 643 | 0.5548 | 0.4251 | 0.493 | +0.062 | -0.068 | 0.0013 ± 0.0058 |
| data_status POOR | 1042 | 0.5505 | 0.3969 | 0.4635 | +0.087 | -0.067 | 0.0109 ± 0.0051 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 363 | 0.1904 | 0.1917 | -0.0014 ± 0.0008 | 0.5569 | 0.5602 | 0.4909 | 0.4761 | 0.5207 | -0.051 ± 0.0241 | -0.01 (3) |
| 3-5 | 241 | 0.1899 | 0.1912 | -0.0012 ± 0.0022 | 0.5596 | 0.5608 | 0.5097 | 0.47 | 0.5021 | -0.060 ± 0.0285 | 0.02 (1) |
| 5-10 | 488 | 0.2006 | 0.2022 | -0.0016 ± 0.0031 | 0.586 | 0.5894 | 0.5171 | 0.4431 | 0.4816 | -0.085 ± 0.0212 | -0.0125 (4) |
| 10-15 | 420 | 0.2112 | 0.2046 | +0.0066 ± 0.0055 | 0.6102 | 0.5901 | 0.517 | 0.393 | 0.4238 | -0.091 ± 0.022 | -0.0633 (3) |
| 15-25 | 495 | 0.2262 | 0.2139 | +0.0123 ± 0.0081 | 0.6468 | 0.6153 | 0.5764 | 0.3816 | 0.4485 | -0.079 ± 0.0206 | -0.0133 (6) |
| 25-40 | 273 | 0.218 | 0.2006 | +0.0175 ± 0.0161 | 0.6257 | 0.5766 | 0.6486 | 0.3402 | 0.4652 | -0.075 ± 0.024 | -0.01 (1) |
| 40+ | 59 | 0.2961 | 0.17 | +0.1261 ± 0.0478 | 0.8068 | 0.513 | 0.7522 | 0.3075 | 0.3898 | -0.142 ± 0.0474 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1816 | 0.1734 | 0.1744 | -0.0010 ± 0.0003 | 0.5174 | 0.5186 | 0.4763 | 0.4614 | 0.4945 | -0.023 ± 0.0099 | -0.0188 (8) |
| 3-5 | 1131 | 0.1921 | 0.1895 | +0.0026 ± 0.001 | 0.5651 | 0.554 | 0.4797 | 0.4402 | 0.4235 | -0.076 ± 0.0131 | 0.02 (1) |
| 5-10 | 2468 | 0.1941 | 0.1916 | +0.0025 ± 0.0013 | 0.5702 | 0.5619 | 0.4862 | 0.4125 | 0.4287 | -0.052 ± 0.009 | -0.0082 (17) |
| 10-15 | 2152 | 0.1997 | 0.1817 | +0.0180 ± 0.0023 | 0.585 | 0.5347 | 0.4764 | 0.3519 | 0.3415 | -0.077 ± 0.0092 | -0.0475 (4) |
| 15-25 | 2505 | 0.203 | 0.1679 | +0.0351 ± 0.0032 | 0.5977 | 0.4979 | 0.4969 | 0.3009 | 0.3114 | -0.064 ± 0.0082 | -0.0048 (29) |
| 25-40 | 2067 | 0.2189 | 0.1229 | +0.0961 ± 0.0048 | 0.6309 | 0.3803 | 0.5278 | 0.2141 | 0.2211 | -0.064 ± 0.0074 | -0.01 (1) |
| 40+ | 1412 | 0.3715 | 0.0432 | +0.3284 ± 0.0061 | 0.969 | 0.1719 | 0.6224 | 0.1059 | 0.0567 | -0.086 ± 0.0052 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 276 | 0.1946 | 0.1949 | -0.0003 ± 0.0009 | 0.5695 | 0.5707 | 0.4929 | 0.478 | 0.4891 | -0.088 ± 0.0282 | -0.01 (1) |
| 3-5 | 184 | 0.2082 | 0.2086 | -0.0003 ± 0.0027 | 0.5969 | 0.5994 | 0.5252 | 0.4852 | 0.5054 | -0.064 ± 0.0352 | 0.02 (1) |
| 5-10 | 426 | 0.1963 | 0.1945 | +0.0019 ± 0.0032 | 0.5743 | 0.5703 | 0.5565 | 0.4814 | 0.5047 | -0.085 ± 0.0221 | -0.01 (4) |
| 10-15 | 392 | 0.2132 | 0.2043 | +0.0089 ± 0.0058 | 0.6124 | 0.5943 | 0.5767 | 0.4519 | 0.4821 | -0.099 ± 0.0235 | -0.05 (4) |
| 15-25 | 570 | 0.2241 | 0.209 | +0.0151 ± 0.0076 | 0.6369 | 0.6005 | 0.5981 | 0.4009 | 0.4667 | -0.081 ± 0.0195 | -0.01 (5) |
| 25-40 | 356 | 0.2737 | 0.1995 | +0.0743 ± 0.015 | 0.7672 | 0.5787 | 0.6727 | 0.3589 | 0.3989 | -0.140 ± 0.0236 | -0.025 (2) |
| 40+ | 135 | 0.3489 | 0.1865 | +0.1624 ± 0.0361 | 0.9805 | 0.5461 | 0.7554 | 0.2786 | 0.363 | -0.069 ± 0.0353 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1571 | 0.1774 | 0.1778 | -0.0004 ± 0.0004 | 0.5264 | 0.5275 | 0.491 | 0.4765 | 0.5003 | -0.031 ± 0.011 | -0.0217 (6) |
| 3-5 | 978 | 0.1922 | 0.1914 | +0.0009 ± 0.0011 | 0.5584 | 0.5563 | 0.5193 | 0.4794 | 0.4877 | -0.042 ± 0.0142 | 0.02 (1) |
| 5-10 | 2172 | 0.1884 | 0.1849 | +0.0035 ± 0.0014 | 0.5584 | 0.5461 | 0.5133 | 0.4396 | 0.4553 | -0.048 ± 0.0094 | -0.01 (5) |
| 10-15 | 1884 | 0.1949 | 0.1801 | +0.0148 ± 0.0025 | 0.5754 | 0.5292 | 0.5202 | 0.3958 | 0.4013 | -0.066 ± 0.0099 | -0.02 (14) |
| 15-25 | 2720 | 0.2138 | 0.1747 | +0.0392 ± 0.0032 | 0.6233 | 0.5165 | 0.5351 | 0.3393 | 0.3408 | -0.076 ± 0.0081 | -0.0026 (27) |
| 25-40 | 2366 | 0.2491 | 0.1365 | +0.1126 ± 0.0048 | 0.7081 | 0.4161 | 0.5614 | 0.2454 | 0.227 | -0.089 ± 0.0076 | -0.015 (6) |
| 40+ | 1860 | 0.4033 | 0.0667 | +0.3366 ± 0.0068 | 1.0568 | 0.2344 | 0.6668 | 0.1298 | 0.0989 | -0.072 ± 0.0058 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 360 | 0.1927 | 0.1955 | -0.0027 ± 0.0008 | 0.563 | 0.5702 | 0.4988 | 0.4836 | 0.5639 | -0.001 ± 0.0234 | -0.0133 (6) |
| 3-5 | 253 | 0.1866 | 0.1853 | +0.0013 ± 0.0022 | 0.5489 | 0.5459 | 0.5003 | 0.4609 | 0.4664 | -0.108 ± 0.0284 | -0.01 (1) |
| 5-10 | 525 | 0.2007 | 0.1987 | +0.0021 ± 0.0029 | 0.5885 | 0.581 | 0.5075 | 0.4336 | 0.4514 | -0.093 ± 0.0202 | -0.01 (4) |
| 10-15 | 403 | 0.2127 | 0.2129 | -0.0002 ± 0.0057 | 0.6143 | 0.6089 | 0.5362 | 0.4135 | 0.4764 | -0.069 ± 0.0229 | -0.044 (5) |
| 15-25 | 467 | 0.2294 | 0.2081 | +0.0213 ± 0.0082 | 0.6583 | 0.6008 | 0.5807 | 0.3877 | 0.4304 | -0.104 ± 0.0207 | -0.03 (1) |
| 25-40 | 280 | 0.2007 | 0.2058 | -0.0051 ± 0.0157 | 0.5843 | 0.5905 | 0.655 | 0.3435 | 0.5036 | -0.047 ± 0.0232 | 0.0 (1) |
| 40+ | 51 | 0.3152 | 0.173 | +0.1422 ± 0.0527 | 0.8532 | 0.5189 | 0.7494 | 0.2986 | 0.3725 | -0.150 ± 0.0537 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1697 | 0.1815 | 0.1825 | -0.0010 ± 0.0004 | 0.5352 | 0.5371 | 0.4848 | 0.4697 | 0.505 | -0.020 ± 0.0104 | -0.0183 (23) |
| 3-5 | 1182 | 0.1839 | 0.1813 | +0.0026 ± 0.001 | 0.5433 | 0.537 | 0.4794 | 0.4401 | 0.4281 | -0.076 ± 0.0128 | -0.0243 (7) |
| 5-10 | 2637 | 0.1905 | 0.1852 | +0.0052 ± 0.0013 | 0.564 | 0.5467 | 0.481 | 0.4072 | 0.4073 | -0.063 ± 0.0085 | -0.01 (18) |
| 10-15 | 2032 | 0.1955 | 0.1816 | +0.0139 ± 0.0023 | 0.5755 | 0.5321 | 0.4929 | 0.3698 | 0.374 | -0.065 ± 0.0094 | -0.03 (9) |
| 15-25 | 2622 | 0.2079 | 0.1693 | +0.0385 ± 0.0031 | 0.6105 | 0.5026 | 0.5005 | 0.3054 | 0.3063 | -0.070 ± 0.0081 | -0.03 (2) |
| 25-40 | 2039 | 0.2125 | 0.1192 | +0.0932 ± 0.0048 | 0.6159 | 0.3698 | 0.5229 | 0.2061 | 0.2207 | -0.060 ± 0.0072 | 0.0 (1) |
| 40+ | 1342 | 0.3852 | 0.0453 | +0.3399 ± 0.0065 | 1.0072 | 0.1778 | 0.6301 | 0.1074 | 0.0551 | -0.088 ± 0.0055 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 667 | 0.2008 | 0.2014 | -0.0006 ± 0.0006 | 0.5831 | 0.584 | 0.5017 | 0.4867 | 0.5022 | -0.035 ± 0.0174 | -0.0226 (46) |
| 3-5 | 486 | 0.1984 | 0.1973 | +0.0011 ± 0.0016 | 0.577 | 0.5725 | 0.4798 | 0.4401 | 0.4444 | -0.051 ± 0.0201 | -0.0058 (33) |
| 5-10 | 998 | 0.1918 | 0.1864 | +0.0055 ± 0.0021 | 0.5675 | 0.5533 | 0.4799 | 0.4063 | 0.4068 | -0.062 ± 0.0139 | -0.0049 (73) |
| 10-15 | 635 | 0.204 | 0.1935 | +0.0105 ± 0.0044 | 0.5961 | 0.5685 | 0.4924 | 0.3697 | 0.3874 | -0.049 ± 0.0175 | 0.0014 (64) |
| 15-25 | 857 | 0.2346 | 0.2103 | +0.0243 ± 0.0061 | 0.6684 | 0.6063 | 0.5536 | 0.3595 | 0.3956 | -0.057 ± 0.0157 | -0.0216 (58) |
| 25-40 | 483 | 0.2513 | 0.1887 | +0.0625 ± 0.0123 | 0.7086 | 0.552 | 0.6399 | 0.3265 | 0.381 | -0.088 ± 0.0184 | -0.0216 (25) |
| 40+ | 166 | 0.3602 | 0.1898 | +0.1703 ± 0.0347 | 1.0519 | 0.5591 | 0.7926 | 0.2989 | 0.3976 | -0.071 ± 0.0308 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2085 | 0.1904 | 0.1906 | -0.0002 ± 0.0003 | 0.5562 | 0.5553 | 0.5024 | 0.4871 | 0.4969 | -0.034 ± 0.0095 | -0.0155 (82) |
| 3-5 | 1440 | 0.1898 | 0.1872 | +0.0026 ± 0.0009 | 0.5545 | 0.548 | 0.4866 | 0.4471 | 0.4347 | -0.058 ± 0.0114 | -0.0148 (63) |
| 5-10 | 2896 | 0.1895 | 0.1815 | +0.0080 ± 0.0012 | 0.5622 | 0.5398 | 0.4747 | 0.4009 | 0.3874 | -0.066 ± 0.008 | -0.0087 (125) |
| 10-15 | 1960 | 0.1996 | 0.1854 | +0.0142 ± 0.0024 | 0.586 | 0.5486 | 0.5032 | 0.3802 | 0.3837 | -0.055 ± 0.0097 | -0.0053 (105) |
| 15-25 | 2498 | 0.2292 | 0.1976 | +0.0316 ± 0.0035 | 0.6625 | 0.5746 | 0.5502 | 0.3552 | 0.3727 | -0.059 ± 0.009 | -0.0255 (106) |
| 25-40 | 1697 | 0.2515 | 0.1641 | +0.0874 ± 0.0062 | 0.7149 | 0.4871 | 0.6017 | 0.2868 | 0.3076 | -0.077 ± 0.0095 | -0.0206 (47) |
| 40+ | 839 | 0.3857 | 0.1235 | +0.2622 ± 0.0131 | 1.0979 | 0.3813 | 0.7065 | 0.1974 | 0.2086 | -0.075 ± 0.0115 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2339 | 1.076 ± 0.058 | 1.195 | 0.1694 | 0.1698 | 0.2097 | 0.2013 |
| gen2 | 2339 | 0.872 ± 0.052 | 1.138 | 0.1848 | 0.1692 | 0.2272 | 0.2011 |
| gen1_elo | 2339 | 1.068 ± 0.057 | 1.183 | 0.1734 | 0.1701 | 0.2082 | 0.2014 |
| gen1_sr | 2339 | 1.073 ± 0.066 | 1.22 | 0.1434 | 0.1714 | 0.2228 | 0.2009 |
| gen1_ledger | 4292 | 0.878 ± 0.038 | 1.084 | 0.1748 | 0.188 | 0.2175 | 0.1962 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 11,785)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,170 | 26.9% |
| STALE_QUOTE | market_freshness | 2,311 | 19.6% |
| BOOK_QUALITY | execution | 2,109 | 17.9% |
| POOR_DATA | data | 1,223 | 10.4% |
| LIMITED_DATA | data | 925 | 7.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 671 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 542 | 4.6% |
| IDENTITY_AMBIGUOUS | mapping | 383 | 3.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 357 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 94 | 0.8% |

Cause class: coverage 26.9%, market_freshness 19.6%, data 18.2%, execution 17.9%, market_freshness/coverage 8.7%, model_calibration_or_unknown 4.6%, mapping 3.2%, model_calibration 0.8%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.7%, START_UNVERIFIABLE 95.8%, LOW_DATA_QUALITY 67.8%, STALE_PLAYER_DATA 56.9%, THIN_PLAYER_HISTORY 56.1%, STALE_KALSHI_QUOTE 46.1%, MODEL_INTERNAL_DISAGREEMENT 37.5%, ASYMMETRIC_SAMPLE_SIZE 30.3%, WIDE_SPREAD 23.7%, MODEL_HIGH_UNCERTAINTY 16.3%, PLAYER_IDENTITY_RISK 11.8%, LEVEL_TRANSFER_RISK 8.9%, EVENT_MAPPING_RISK 8.0%, LOW_DISPLAYED_LIQUIDITY 7.3%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 1.2%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 29.5%, POST_SETTLEMENT_OBSERVATION 26.9%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### >= ge_25 pp (N = 6,373)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,505 | 39.3% |
| BOOK_QUALITY | execution | 1,114 | 17.5% |
| STALE_QUOTE | market_freshness | 1,025 | 16.1% |
| POOR_DATA | data | 498 | 7.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 364 | 5.7% |
| LIMITED_DATA | data | 270 | 4.2% |
| IDENTITY_AMBIGUOUS | mapping | 236 | 3.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 222 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 117 | 1.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 22 | 0.4% |

Cause class: coverage 39.3%, execution 17.5%, market_freshness 16.1%, data 12.0%, market_freshness/coverage 9.2%, mapping 3.7%, model_calibration_or_unknown 1.8%, model_calibration 0.4%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.3%, START_UNVERIFIABLE 98.1%, LOW_DATA_QUALITY 71.3%, THIN_PLAYER_HISTORY 58.2%, STALE_KALSHI_QUOTE 54.3%, STALE_PLAYER_DATA 51.3%, MODEL_INTERNAL_DISAGREEMENT 38.8%, ASYMMETRIC_SAMPLE_SIZE 32.4%, WIDE_SPREAD 23.4%, MODEL_HIGH_UNCERTAINTY 17.5%, PLAYER_IDENTITY_RISK 15.0%, EVENT_MAPPING_RISK 9.8%, LEVEL_TRANSFER_RISK 7.8%, LOW_DISPLAYED_LIQUIDITY 7.6%, MODEL_CALIBRATION_OUTLIER 4.7%, EXTERNAL_MARKET_REJECTION 0.6%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 42.3%, POST_SETTLEMENT_OBSERVATION 39.3%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 5249, "IDENTITY_AMBIGUOUS": 1124}; ticker orientation: {"VERIFIED": 6373}.

Checks: discipline:AMBIGUOUS 457, discipline:PASS 5916, identity_confidence:AMBIGUOUS 958, identity_confidence:PASS 5415, level_mapping:NA 469, level_mapping:PASS 5904, market_pair:AMBIGUOUS 226, market_pair:NA 153, market_pair:PASS 5994, model_complement:NA 120, model_complement:PASS 6253, namesake:PASS 6373, physical_match_id:NA 2609, physical_match_id:PASS 3764, player_ids:PASS 6373, same_pair_other_event:PASS 6373, ticker_orientation:PASS 6373

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,965 | 1.4% | 1.5% | 0.4% | {"market_freshness": 20, "execution": 8} | 5.28 | 0.2052 / 0.2035 (219) | 16.7% | 0.2% | 5.7% | 1.6% |
| CHALLENGER | 4,561 | 17.0% | 5.7% | 12.2% | {"coverage": 473, "market_freshness": 109, "market_freshness/coverage": 102, "model_calibration_or_unknown": 40, "data": 32, "execution": 12, "model_calibration": 4, "mapping": 4} | 7.01 | 0.2172 / 0.2023 (1078) | 39.6% | 7.0% | 2.2% | 22.4% |
| DOUBLES | 908 | 50.3% | 49.8% | 7.2% | {"execution": 176, "mapping": 137, "market_freshness": 106, "market_freshness/coverage": 31, "coverage": 7} | 24.85 | 0.3344 / 0.2293 (250) | 25.8% | 0.0% | 100.0% | 7.4% |
| ITF_MEN | 8,470 | 23.7% | 15.4% | 31.5% | {"coverage": 841, "execution": 415, "data": 272, "market_freshness": 272, "market_freshness/coverage": 182, "mapping": 21, "model_calibration_or_unknown": 2} | 10.38 | 0.2102 / 0.1933 (2101) | 37.5% | 53.7% | 6.6% | 24.5% |
| ITF_WOMEN | 10,865 | 26.3% | 17.9% | 44.9% | {"coverage": 1167, "execution": 484, "market_freshness": 452, "data": 431, "market_freshness/coverage": 227, "mapping": 68, "model_calibration_or_unknown": 24, "model_calibration": 9} | 12.2 | 0.2051 / 0.1934 (2377) | 38.5% | 57.6% | 9.6% | 24.3% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,399 | 6.5% | 5.7% | 1.4% | {"market_freshness": 36, "model_calibration_or_unknown": 20, "data": 11, "market_freshness/coverage": 9, "execution": 6, "model_calibration": 4, "coverage": 4, "mapping": 1} | 7.69 | 0.2224 / 0.2198 (207) | 27.2% | 1.5% | 1.6% | 2.5% |
| WTA125 | 1,070 | 13.3% | 10.1% | 2.2% | {"market_freshness/coverage": 34, "model_calibration_or_unknown": 29, "market_freshness": 28, "data": 22, "coverage": 12, "execution": 8, "model_calibration": 5, "mapping": 4} | 9.08 | 0.2245 / 0.2104 (357) | 23.5% | 7.9% | 4.1% | 11.1% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 5 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 6 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 15.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 928 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 8 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 9 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 10 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 11 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 12 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 13 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 14 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 15 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 16 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 18 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 9.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 553 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 19 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 20 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 21 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 22 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 23 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 24 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 25 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 26 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 27 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 28 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 29 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 30 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 31 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 32 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 33 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 189 min (STALE); no external reference |
| 34 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 35 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 36 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 37 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 39 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 253 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 40 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 41 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 22 min (AGING); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 42 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 43 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 44 | `KXITFWMATCH-26OCT08ARISAV-SAV` | ITF_WOMEN | fair_v1 | 75% / 2% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 45 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 230 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 46 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 114 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 47 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 48 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 49 | `KXITFMATCH-26OCT09DELSTE-DEL` | ITF_MEN | fair_v1 | 78% / 6% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 229 min (STALE); data POOR (grade F, thinner serve sample 477.0, ratio 8.93); no external reference |
| 50 | `KXITFWMATCH-26OCT08ARAWAN-ARA` | ITF_WOMEN | fair_v1 | 77% / 6% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 341 min (STALE); data POOR (grade D, thinner serve sample 553.0, ratio 3.97); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9814, "by_level_share_of_ge_25pp": {"ATP": 0.0044, "CHALLENGER": 0.1218, "DOUBLES": 0.0717, "ITF_MEN": 0.3146, "ITF_WOMEN": 0.4491, "OTHER": 0.0019, "WTA": 0.0143, "WTA125": 0.0223}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5431, "share_primary_cause_market_settled_or_in_play": 0.485, "share_primary_cause_stale_quote_only": 0.1608}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 6373, "identity_ambiguous_share": 0.1764, "ticker_orientation": {"VERIFIED": 6373}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 3764, "with_external": 100, "coverage": 0.0266, "external_status": {"EXTERNAL_STALE": 71, "AGREES_WITH_KALSHI": 27, "SUPPORTS_MODEL_DIRECTION": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 71, "MODEL_LONE_OUTLIER": 27, "ALL_THREE_DISAGREE": 2}, "share_external_agrees_with_kalshi": 0.27, "share_external_supports_model": 0.02}, "pregame_clean_ge_25pp": {"n": 1596, "with_external": 95, "coverage": 0.0595, "external_status": {"EXTERNAL_STALE": 68, "AGREES_WITH_KALSHI": 25, "SUPPORTS_MODEL_DIRECTION": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 68, "MODEL_LONE_OUTLIER": 25, "ALL_THREE_DISAGREE": 2}, "share_external_agrees_with_kalshi": 0.2632, "share_external_supports_model": 0.0211}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 620.0, "median_sample_ratio": 2.31, "median_min_matches": 21.0, "median_max_days_since_last": 197.0, "share_severe_asymmetry": 0.1823, "data_status": {"POOR": 3254, "LIMITED": 1935, "ADEQUATE": 1184}, "comparison_lt_10pp": {"median_thinner_serve_points": 1937.0, "median_sample_ratio": 1.66, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 498, "model_minus_observed": 0.0582, "kalshi_minus_observed": -0.0727, "brier_diff_model_minus_kalshi": 0.0019}, "4-10x": {"n": 339, "model_minus_observed": 0.0641, "kalshi_minus_observed": -0.0767, "brier_diff_model_minus_kalshi": 0.0027}, "<2x": {"n": 1167, "model_minus_observed": 0.0805, "kalshi_minus_observed": -0.0403, "brier_diff_model_minus_kalshi": 0.0109}, ">=10x": {"n": 335, "model_minus_observed": 0.1124, "kalshi_minus_observed": -0.055, "brier_diff_model_minus_kalshi": 0.0146}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2339, "model": {"intercept": -0.548, "slope": 0.872, "slope_se": 0.052}, "kalshi_mid_same_rows": {"intercept": 0.225, "slope": 1.138, "slope_se": 0.06}, "mean_extremity_model": 0.1848, "mean_extremity_kalshi": 0.1692, "model_brier": 0.2272, "kalshi_brier": 0.2011, "brier_diff_model_minus_kalshi": 0.0261, "brier_diff_se": 0.0039, "model_logloss": 0.65, "kalshi_logloss": 0.5839}, "fair_v1": {"n": 2339, "model": {"intercept": -0.393, "slope": 1.076, "slope_se": 0.058}, "kalshi_mid_same_rows": {"intercept": 0.33, "slope": 1.195, "slope_se": 0.062}, "mean_extremity_model": 0.1694, "mean_extremity_kalshi": 0.1698, "model_brier": 0.2097, "kalshi_brier": 0.2013, "brier_diff_model_minus_kalshi": 0.0083, "brier_diff_se": 0.0031, "model_logloss": 0.6062, "kalshi_logloss": 0.5841}, "gen1_elo": {"n": 2339, "model": {"intercept": -0.368, "slope": 1.068, "slope_se": 0.057}, "kalshi_mid_same_rows": {"intercept": 0.336, "slope": 1.183, "slope_se": 0.061}, "mean_extremity_model": 0.1734, "mean_extremity_kalshi": 0.1701, "model_brier": 0.2082, "kalshi_brier": 0.2014, "brier_diff_model_minus_kalshi": 0.0069, "brier_diff_se": 0.003, "model_logloss": 0.604, "kalshi_logloss": 0.5841}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2424, "share_ge_15": 0.4261, "median_abs_gap": 12.69, "n": 15526}, "gen1_elo": {"share_ge_25": 0.2362, "share_ge_15": 0.4224, "median_abs_gap": 12.16, "n": 15526}, "gen1_sr": {"share_ge_25": 0.2937, "share_ge_15": 0.5095, "median_abs_gap": 15.37, "n": 15526}, "gen2": {"share_ge_25": 0.2979, "share_ge_15": 0.499, "median_abs_gap": 14.97, "n": 15526}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1363, "share_ge_15": 0.3243, "median_abs_gap": 10.1, "n": 11705}, "gen1_elo": {"share_ge_25": 0.1339, "share_ge_15": 0.3176, "median_abs_gap": 9.56, "n": 11704}, "gen1_sr": {"share_ge_25": 0.1871, "share_ge_15": 0.4174, "median_abs_gap": 12.48, "n": 11705}, "gen2": {"share_ge_25": 0.2052, "share_ge_15": 0.4208, "median_abs_gap": 12.39, "n": 11706}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.28, "share_ge_25_all": 0.0142, "share_ge_25_pregame_clean": 0.0145}, "WTA": {"median_abs_gap_pregame_clean": 7.69, "share_ge_25_all": 0.065, "share_ge_25_pregame_clean": 0.0572}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2428, "share_within_10pp_all": 0.4451, "share_within_10pp_pregame_clean": 0.5089, "corr_model_vs_mid_pregame_clean": 0.8531}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 363, "model_brier": 0.1904, "kalshi_brier": 0.1917, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 420, "model_brier": 0.2112, "kalshi_brier": 0.2046, "brier_diff_model_minus_kalshi": 0.0066}, "15-25": {"n_settled": 495, "model_brier": 0.2262, "kalshi_brier": 0.2139, "brier_diff_model_minus_kalshi": 0.0123}, "25-40": {"n_settled": 273, "model_brier": 0.218, "kalshi_brier": 0.2006, "brier_diff_model_minus_kalshi": 0.0175}, "3-5": {"n_settled": 241, "model_brier": 0.1899, "kalshi_brier": 0.1912, "brier_diff_model_minus_kalshi": -0.0012}, "40+": {"n_settled": 59, "model_brier": 0.2961, "kalshi_brier": 0.17, "brier_diff_model_minus_kalshi": 0.1261}, "5-10": {"n_settled": 488, "model_brier": 0.2006, "kalshi_brier": 0.2022, "brier_diff_model_minus_kalshi": -0.0016}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.548, "slope": 0.872, "slope_se": 0.052}, "kalshi_slope": {"intercept": 0.225, "slope": 1.138, "slope_se": 0.06}, "n": 2339}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.522, "slope": 0.878, "slope_se": 0.038}, "kalshi_slope": {"intercept": 0.144, "slope": 1.084, "slope_se": 0.042}, "n": 4292}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 250, "model_brier": 0.3344, "kalshi_brier": 0.2293, "brier_diff_model_minus_kalshi": 0.1051, "brier_diff_se": 0.0206, "corr_model_outcome": -0.0224, "corr_kalshi_outcome": 0.2891}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
