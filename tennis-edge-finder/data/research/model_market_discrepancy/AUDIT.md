# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-21T22:27Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 48,240): 0-3 14.0%, 3-5 9.4%, 5-10 19.7%, 10-15 15.3%, 15-25 19.4%, 25-40 14.1%, 40+ 8.2%; median gap 12.15 pp.
* **Where the extremes live**: 97.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.5%, Challenger 12.1%, doubles 6.8%). Main tour: ATP 5.0% and WTA 4.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 10,732): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.7%, BOOK_QUALITY 18.5%, STALE_QUOTE 18.1%, POOR_DATA 8.8%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IDENTITY_AMBIGUOUS 4.5%, LIMITED_DATA 3.6%, IN_PLAY_QUOTE 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%. By class: coverage 34.7%, execution 18.5%, market_freshness 18.1%, data 12.5%, market_freshness/coverage 9.0%, mapping 4.5%, model_calibration_or_unknown 2.1%, model_calibration 0.7%.
* **Stale / settled / in-play**: 51.9% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.7% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 10,732 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.8% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.9%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.9% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 490.0 points vs 1680.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.049, Gen-2 0.85, Gen-1 ledger 0.871 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 518 model 0.2249 vs Kalshi 0.2103; n 104 model 0.2868 vs Kalshi 0.1908.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 206,667 model-market comparisons (336,430 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 69,755 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-21T22:12:42.731313+00:00'], shadow board 54,958 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-21T22:12:48.280232+00:00'], Model 4 25,945 rows, 18,575 settled tickers, 6,444 tickers with an external scan.
* By model: {"gen1_ledger": 47138, "gen1_elo": 27638, "fair_v1": 27638, "gen2": 27638, "gen1_sr": 27638, "model4_fundamental": 24502, "model4_conditioned": 24475}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 48,240 | 14.0 | 9.4 | 19.7 | 15.3 | 19.4 | 14.1 | 8.2 | 12.15 | 41.6% | 22.2% |
| MW fair_v1 | 27,638 | 12.9 | 8.5 | 18.3 | 15.6 | 19.9 | 15.0 | 9.8 | 13.25 | 44.7% | 24.8% |
| MW gen1_elo | 27,638 | 12.9 | 8.6 | 18.9 | 15.1 | 20.0 | 15.0 | 9.5 | 13.01 | 44.6% | 24.6% |
| MW gen1_ledger | 20,602 | 15.4 | 10.7 | 21.5 | 14.8 | 18.7 | 12.9 | 5.9 | 10.58 | 37.5% | 18.8% |
| MW gen1_sr | 27,638 | 9.9 | 7.0 | 16.5 | 13.8 | 21.2 | 18.8 | 12.7 | 16.09 | 52.8% | 31.5% |
| MW gen2 | 27,638 | 10.9 | 7.2 | 16.1 | 14.2 | 19.8 | 17.9 | 13.9 | 15.66 | 51.5% | 31.8% |
| all families model4_conditioned | 24,475 | 21.7 | 19.1 | 34.5 | 17.7 | 4.4 | 1.4 | 1.0 | 5.95 | 6.9% | 2.5% |
| all families model4_fundamental | 24,502 | 16.5 | 13.2 | 34.0 | 20.4 | 11.1 | 3.5 | 1.3 | 7.85 | 15.9% | 4.8% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.9%, >=15pp 41.6%, >=20pp 31.0%, >=25pp 22.2%, >=30pp 16.0%, >=40pp 8.2%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.48pp; >=10pp 45.4%, >=25pp 17.3%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,382 | 28.8 | 13.9 | 24.3 | 14.7 | 12.3 | 5.1 | 0.8 | 6.17 | 18.2% | 5.9% |
| CHALLENGER | 4,407 | 15.8 | 9.9 | 20.3 | 15.7 | 14.8 | 12.5 | 11.0 | 11.17 | 38.3% | 23.5% |
| ITF_MEN | 7,529 | 10.5 | 7.5 | 16.8 | 14.6 | 21.4 | 17.2 | 11.9 | 15.18 | 50.6% | 29.1% |
| ITF_WOMEN | 11,022 | 9.4 | 6.8 | 15.8 | 15.4 | 22.6 | 18.3 | 11.6 | 15.89 | 52.6% | 29.9% |
| WTA | 1,638 | 16.9 | 12.9 | 25.5 | 20.0 | 19.6 | 4.5 | 0.7 | 8.47 | 24.8% | 5.2% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,382 | 23.6 | 14.8 | 24.8 | 17.0 | 13.7 | 5.0 | 1.0 | 6.7 | 19.7% | 6.0% |
| CHALLENGER | 4,407 | 14.7 | 8.5 | 18.6 | 14.8 | 17.5 | 14.1 | 11.9 | 12.69 | 43.5% | 25.9% |
| ITF_MEN | 7,529 | 8.6 | 6.1 | 14.4 | 13.2 | 19.9 | 20.4 | 17.5 | 18.35 | 57.7% | 37.9% |
| ITF_WOMEN | 11,022 | 8.1 | 5.6 | 13.7 | 13.4 | 20.9 | 21.0 | 17.3 | 18.96 | 59.2% | 38.3% |
| WTA | 1,638 | 14.4 | 9.7 | 21.1 | 16.5 | 23.8 | 13.8 | 0.7 | 11.28 | 38.3% | 14.5% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,382 | 24.3 | 12.7 | 24.0 | 15.9 | 14.9 | 7.0 | 1.2 | 7.3 | 23.1% | 8.2% |
| CHALLENGER | 4,407 | 14.2 | 9.4 | 20.8 | 15.2 | 16.3 | 12.8 | 11.2 | 11.43 | 40.4% | 24.1% |
| ITF_MEN | 7,529 | 10.0 | 7.5 | 16.9 | 14.0 | 22.0 | 17.5 | 12.1 | 15.52 | 51.5% | 29.6% |
| ITF_WOMEN | 11,022 | 9.5 | 6.6 | 16.1 | 15.5 | 23.1 | 18.4 | 10.8 | 15.88 | 52.3% | 29.2% |
| WTA | 1,638 | 24.3 | 16.8 | 29.6 | 16.2 | 10.3 | 2.4 | 0.4 | 6.04 | 13.1% | 2.8% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,370 | 25.7 | 19.4 | 30.7 | 11.8 | 9.0 | 3.1 | 0.4 | 5.53 | 12.4% | 3.4% |
| CHALLENGER | 3,050 | 21.3 | 14.9 | 26.7 | 14.0 | 14.7 | 6.6 | 1.9 | 7.27 | 23.2% | 8.5% |
| DOUBLES | 1,520 | 5.3 | 4.1 | 11.5 | 10.2 | 20.9 | 26.4 | 21.5 | 24.05 | 68.8% | 47.9% |
| ITF_MEN | 5,806 | 13.8 | 8.8 | 20.2 | 15.9 | 21.2 | 13.3 | 6.7 | 12.14 | 41.2% | 20.0% |
| ITF_WOMEN | 6,947 | 12.7 | 9.0 | 19.3 | 15.1 | 21.6 | 16.3 | 6.1 | 12.87 | 44.0% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,028 | 22.3 | 15.9 | 29.6 | 18.2 | 10.1 | 3.6 | 0.3 | 6.97 | 14.0% | 3.9% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,317 | 29.2 | 14.2 | 24.7 | 14.6 | 12.1 | 4.7 | 0.5 | 5.99 | 17.3% | 5.2% |
| CHALLENGER | 3,110 | 20.6 | 12.3 | 25.1 | 18.2 | 15.2 | 6.7 | 2.0 | 8.35 | 23.9% | 8.7% |
| ITF_MEN | 5,520 | 12.8 | 9.0 | 20.1 | 16.5 | 22.4 | 14.1 | 5.0 | 12.35 | 41.6% | 19.1% |
| ITF_WOMEN | 8,205 | 11.2 | 8.2 | 17.9 | 17.6 | 24.6 | 15.4 | 5.1 | 13.53 | 45.1% | 20.5% |
| WTA | 1,590 | 17.2 | 12.7 | 25.5 | 20.2 | 19.6 | 4.2 | 0.7 | 8.45 | 24.5% | 4.9% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,317 | 23.9 | 15.2 | 25.0 | 16.9 | 13.7 | 4.7 | 0.7 | 6.49 | 19.0% | 5.3% |
| CHALLENGER | 3,110 | 18.6 | 10.8 | 23.2 | 17.6 | 17.8 | 9.7 | 2.2 | 9.4 | 29.7% | 12.0% |
| ITF_MEN | 5,521 | 10.2 | 7.3 | 16.7 | 15.0 | 21.7 | 18.8 | 10.3 | 15.38 | 50.7% | 29.1% |
| ITF_WOMEN | 8,206 | 9.1 | 6.5 | 15.1 | 15.0 | 23.0 | 20.5 | 10.8 | 16.59 | 54.3% | 31.3% |
| WTA | 1,590 | 14.5 | 9.7 | 21.1 | 16.4 | 23.8 | 13.7 | 0.8 | 11.28 | 38.3% | 14.5% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,328 | 25.9 | 19.6 | 30.7 | 12.1 | 8.5 | 2.9 | 0.2 | 5.42 | 11.7% | 3.2% |
| CHALLENGER | 2,655 | 22.8 | 16.0 | 28.2 | 13.9 | 14.1 | 4.5 | 0.6 | 6.68 | 19.1% | 5.1% |
| DOUBLES | 1,413 | 5.3 | 4.3 | 11.8 | 10.4 | 20.9 | 26.3 | 21.0 | 23.87 | 68.2% | 47.3% |
| ITF_MEN | 4,846 | 15.0 | 9.5 | 21.9 | 16.7 | 21.1 | 11.6 | 4.1 | 11.12 | 36.9% | 15.7% |
| ITF_WOMEN | 5,763 | 13.6 | 9.5 | 20.7 | 15.9 | 21.8 | 15.1 | 3.4 | 11.71 | 40.3% | 18.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 978 | 22.8 | 16.5 | 29.6 | 18.2 | 10.1 | 2.9 | 0.0 | 6.82 | 13.0% | 2.9% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,520 | 5.3 | 4.1 | 11.5 | 10.2 | 20.9 | 26.4 | 21.5 | 24.05 | 68.8% | 47.9% |
| singles | 19,082 | 16.2 | 11.2 | 22.3 | 15.2 | 18.5 | 11.8 | 4.7 | 10.04 | 35.0% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 6,180 | 13.2 | 8.8 | 18.9 | 15.7 | 18.9 | 14.9 | 9.7 | 12.94 | 43.5% | 24.6% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 17,266 | 13.3 | 8.5 | 18.4 | 15.2 | 20.1 | 14.8 | 9.7 | 13.24 | 44.6% | 24.5% |
| UNKNOWN | 3,955 | 11.2 | 7.8 | 16.9 | 17.0 | 20.5 | 16.0 | 10.5 | 13.84 | 47.0% | 26.5% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,719 | 19.7 | 11.6 | 21.2 | 16.5 | 15.7 | 9.0 | 6.3 | 9.23 | 30.9% | 15.2% |
| B | 3,464 | 12.5 | 8.9 | 19.9 | 16.7 | 19.2 | 12.3 | 10.5 | 12.34 | 41.9% | 22.8% |
| C | 3,895 | 11.7 | 8.8 | 19.3 | 14.9 | 19.6 | 15.3 | 10.5 | 13.36 | 45.4% | 25.9% |
| D | 4,489 | 12.1 | 7.8 | 17.0 | 15.6 | 21.7 | 15.8 | 10.0 | 14.06 | 47.5% | 25.8% |
| F | 8,071 | 7.7 | 5.5 | 14.9 | 14.6 | 23.4 | 21.4 | 12.4 | 17.87 | 57.2% | 33.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,782 | 22.9 | 15.9 | 28.9 | 15.0 | 11.8 | 4.1 | 1.5 | 6.68 | 17.3% | 5.6% |
| B | 2,836 | 16.3 | 10.5 | 23.4 | 16.0 | 19.1 | 10.7 | 3.9 | 9.95 | 33.7% | 14.6% |
| C | 4,072 | 11.3 | 7.3 | 18.4 | 14.2 | 21.5 | 16.6 | 10.7 | 14.32 | 48.8% | 27.3% |
| D | 2,939 | 14.5 | 9.8 | 19.8 | 14.4 | 21.0 | 14.4 | 6.1 | 12.04 | 41.5% | 20.5% |
| F | 4,973 | 10.1 | 8.1 | 15.5 | 14.7 | 22.8 | 20.4 | 8.3 | 15.82 | 51.5% | 28.7% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 8,820 | 17.8 | 10.4 | 20.5 | 16.5 | 16.3 | 9.8 | 8.7 | 10.38 | 34.8% | 18.5% |
| LIMITED | 5,985 | 13.5 | 10.1 | 20.2 | 15.6 | 19.2 | 13.7 | 7.7 | 11.92 | 40.6% | 21.4% |
| POOR | 12,833 | 9.3 | 6.4 | 15.8 | 15.0 | 22.8 | 19.2 | 11.6 | 16.19 | 53.5% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,255 | 26.6 | 20.4 | 34.3 | 12.3 | 4.8 | 1.5 | 0.2 | 5.3 | 6.5% | 1.7% |
| GAME_SPREAD | 4,521 | 22.4 | 15.2 | 33.5 | 17.2 | 9.0 | 2.3 | 0.3 | 6.67 | 11.7% | 2.6% |
| MATCH_WINNER | 20,602 | 15.4 | 10.7 | 21.5 | 14.8 | 18.7 | 12.9 | 5.9 | 10.58 | 37.5% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 9,479 | 29.5 | 16.9 | 30.8 | 12.5 | 8.2 | 1.7 | 0.4 | 5.46 | 10.3% | 2.1% |
| TOTAL_GAMES | 7,257 | 8.4 | 9.5 | 36.5 | 29.0 | 10.6 | 3.3 | 2.7 | 9.52 | 16.6% | 6.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,553 | 25.4 | 34.1 | 32.5 | 4.2 | 3.0 | 0.6 | 0.2 | 4.48 | 3.8% | 0.8% |
| GAME_SPREAD | 5,860 | 45.5 | 17.1 | 27.0 | 7.7 | 1.8 | 0.8 | 0.2 | 3.47 | 2.8% | 1.0% |
| TOTAL_GAMES | 10,062 | 4.8 | 7.6 | 40.6 | 35.0 | 7.2 | 2.5 | 2.2 | 9.7 | 11.9% | 4.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,556 | 24.2 | 17.9 | 35.4 | 12.5 | 7.2 | 2.5 | 0.3 | 5.81 | 10.0% | 2.9% |
| GAME_SPREAD | 5,863 | 19.3 | 13.2 | 28.0 | 20.2 | 13.9 | 4.5 | 0.9 | 7.97 | 19.3% | 5.4% |
| TOTAL_GAMES | 10,083 | 8.3 | 9.1 | 36.4 | 27.4 | 12.7 | 3.8 | 2.4 | 9.56 | 18.8% | 6.2% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 27,638 | 44.7% | 24.8% | 13.25 | 36.2% | 15.4% | 10.98 |
| gen1_elo | 27,638 | 44.6% | 24.6% | 13.01 | 35.9% | 15.6% | 10.67 |
| gen1_sr | 27,638 | 52.8% | 31.5% | 16.09 | 45.0% | 22.2% | 13.28 |
| gen2 | 27,638 | 51.5% | 31.8% | 15.66 | 44.8% | 23.8% | 13.2 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 14,154 | 15.8 | 10.3 | 21.1 | 17.2 | 20.4 | 11.9 | 3.3 | 10.81 | 35.6% | 15.2% |
| STALE | 13,484 | 9.9 | 6.6 | 15.4 | 13.9 | 19.4 | 18.3 | 16.6 | 17.08 | 54.3% | 34.9% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 14,070 | 16.5 | 11.2 | 22.4 | 14.8 | 17.9 | 12.3 | 4.9 | 9.97 | 35.0% | 17.2% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 48,240 | 14070 | 17626 | 16544 | 24.0 | 140.4 | 1400.4 |
| ge_15pp | 20,089 | 4928 | 6332 | 8829 | 25.8 | 436.6 | 1380.4 |
| ge_25pp | 10,732 | 2413 | 2745 | 5574 | 31.6 | 575.6 | 1380.4 |
| lt_10pp | 20,791 | 7052 | 8308 | 5431 | 21.8 | 47.5 | 1341.5 |

Current slate `SL-20261021T222735Z-05bbd396`: 610 priced rows, quote age at build {'median': 15.2, 'max': 15.3}, freshness {'AGING': 610}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 22 | 0.0 | 0.0 | 22.7 | 4.5 | 40.9 | 31.8 | 0.0 | 20.48 | 72.7% | 31.8% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,539 | 19.6 | 10.7 | 23.9 | 18.8 | 18.9 | 7.3 | 0.8 | 9.1 | 26.9% | 8.0% |
| KALSHI_LONE_OUTLIER | 17 | 5.9 | 5.9 | 76.5 | 0.0 | 5.9 | 5.9 | 0.0 | 6.11 | 11.8% | 5.9% |
| MARKETS_AGREE | 488 | 66.0 | 34.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,075 | 0.0 | 2.2 | 34.2 | 25.9 | 25.9 | 10.9 | 0.8 | 12.77 | 37.7% | 11.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 27,638 | 4153 (15.0%) | 25.9% | 0.9% | {"EXTERNAL_STALE": 2539, "AGREES_WITH_KALSHI": 1075, "ALL_AGREE": 488, "SUPPORTS_MODEL_DIRECTION": 21, "AGREES_WITH_MODEL": 17, "EXTERNAL_OUTLIER": 12, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 12,362 | 1107 (8.9%) | 36.6% | 1.6% | {"EXTERNAL_STALE": 684, "AGREES_WITH_KALSHI": 405, "SUPPORTS_MODEL_DIRECTION": 16, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 6,857 | 338 (4.9%) | 37.3% | 2.4% | {"EXTERNAL_STALE": 204, "AGREES_WITH_KALSHI": 126, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,302 | 315 (9.5%) | 37.8% | 2.5% | {"EXTERNAL_STALE": 188, "AGREES_WITH_KALSHI": 119, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 10,970 | 2289 (20.9%) | 17.1% | 0.8% | {"EXTERNAL_STALE": 1377, "ALL_AGREE": 488, "AGREES_WITH_KALSHI": 392, "AGREES_WITH_MODEL": 15, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 4, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,265 | 10.5 | 7.6 | 19.3 | 14.3 | 22.2 | 16.0 | 10.0 | 14.12 | 48.2% | 26.0% |
| 4-10x | 3,624 | 11.0 | 8.4 | 18.7 | 15.5 | 21.2 | 14.9 | 10.3 | 13.84 | 46.4% | 25.2% |
| <2x | 14,056 | 14.9 | 9.6 | 18.8 | 16.6 | 18.0 | 13.2 | 8.9 | 12.0 | 40.2% | 22.1% |
| >=10x | 4,693 | 11.2 | 6.3 | 15.2 | 14.1 | 22.0 | 19.4 | 11.8 | 16.24 | 53.1% | 31.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 6,959 | 12.3 | 8.4 | 19.4 | 16.2 | 19.6 | 13.6 | 10.5 | 13.0 | 43.7% | 24.1% |
| 300-1000 | 6,003 | 11.6 | 8.7 | 17.0 | 15.3 | 20.8 | 16.6 | 10.1 | 14.1 | 47.5% | 26.7% |
| <300 | 9,019 | 8.9 | 5.7 | 15.4 | 14.8 | 23.0 | 20.1 | 12.2 | 16.96 | 55.3% | 32.3% |
| >=3000 | 5,657 | 21.6 | 12.8 | 22.9 | 16.5 | 14.5 | 7.0 | 4.8 | 8.01 | 26.2% | 11.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 796 | 0.5461 | 0.4087 | 0.5 | +0.046 | -0.091 | -0.0041 ± 0.0054 |
| ratio 4-10x | 548 | 0.5843 | 0.4388 | 0.4891 | +0.095 | -0.050 | 0.0142 ± 0.0069 |
| ratio <2x | 1969 | 0.5363 | 0.4122 | 0.4459 | +0.090 | -0.034 | 0.0126 ± 0.0032 |
| ratio >=10x | 700 | 0.5661 | 0.3898 | 0.46 | +0.106 | -0.070 | 0.0063 ± 0.0069 |
| thinner_sample 1000-3000 | 1090 | 0.5421 | 0.4142 | 0.4486 | +0.093 | -0.035 | 0.0107 ± 0.0044 |
| thinner_sample 300-1000 | 933 | 0.5629 | 0.4204 | 0.492 | +0.071 | -0.071 | 0.0006 ± 0.0053 |
| thinner_sample <300 | 1329 | 0.5553 | 0.3888 | 0.4597 | +0.096 | -0.071 | 0.0097 ± 0.0049 |
| thinner_sample >=3000 | 661 | 0.534 | 0.4385 | 0.4644 | +0.070 | -0.026 | 0.0129 ± 0.0046 |
| data_status ADEQUATE | 1143 | 0.5377 | 0.4309 | 0.4523 | +0.085 | -0.021 | 0.0126 ± 0.0037 |
| data_status LIMITED | 950 | 0.548 | 0.4154 | 0.4768 | +0.071 | -0.061 | 0.0044 ± 0.0049 |
| data_status POOR | 1920 | 0.5583 | 0.3974 | 0.4667 | +0.092 | -0.069 | 0.0078 ± 0.004 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 588 | 0.1978 | 0.1989 | -0.0011 ± 0.0006 | 0.5745 | 0.5768 | 0.4974 | 0.4826 | 0.5289 | -0.058 ± 0.0192 | -0.01 (5) |
| 3-5 | 377 | 0.2022 | 0.2016 | +0.0006 ± 0.0019 | 0.588 | 0.5848 | 0.5004 | 0.4603 | 0.4721 | -0.095 ± 0.0238 | 0.02 (1) |
| 5-10 | 817 | 0.2026 | 0.2021 | +0.0005 ± 0.0024 | 0.5912 | 0.5877 | 0.5119 | 0.4374 | 0.4663 | -0.089 ± 0.0164 | -0.0167 (6) |
| 10-15 | 694 | 0.2129 | 0.2034 | +0.0094 ± 0.0043 | 0.6153 | 0.5881 | 0.5235 | 0.3994 | 0.4222 | -0.101 ± 0.0171 | -0.048 (5) |
| 15-25 | 915 | 0.2228 | 0.2124 | +0.0103 ± 0.0059 | 0.6401 | 0.6085 | 0.5751 | 0.3794 | 0.4514 | -0.084 ± 0.015 | -0.0033 (9) |
| 25-40 | 518 | 0.2249 | 0.2103 | +0.0147 ± 0.012 | 0.638 | 0.6042 | 0.6565 | 0.3468 | 0.4749 | -0.073 ± 0.0185 | -0.01 (1) |
| 40+ | 104 | 0.2868 | 0.1908 | +0.0961 ± 0.0376 | 0.7842 | 0.5653 | 0.7516 | 0.3041 | 0.4231 | -0.092 ± 0.0368 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2987 | 0.1838 | 0.1847 | -0.0010 ± 0.0003 | 0.5418 | 0.5427 | 0.4841 | 0.469 | 0.5039 | -0.021 ± 0.0079 | -0.0129 (17) |
| 3-5 | 1977 | 0.1988 | 0.1975 | +0.0012 ± 0.0008 | 0.5782 | 0.572 | 0.4824 | 0.4425 | 0.4461 | -0.053 ± 0.0102 | 0.0 (2) |
| 5-10 | 4186 | 0.1981 | 0.1953 | +0.0028 ± 0.001 | 0.579 | 0.5698 | 0.4815 | 0.4075 | 0.4245 | -0.045 ± 0.0069 | -0.0119 (21) |
| 10-15 | 3622 | 0.1999 | 0.1821 | +0.0177 ± 0.0018 | 0.5863 | 0.536 | 0.4837 | 0.3592 | 0.3501 | -0.072 ± 0.0071 | -0.0281 (16) |
| 15-25 | 4577 | 0.2059 | 0.1694 | +0.0365 ± 0.0024 | 0.6047 | 0.5018 | 0.5015 | 0.3051 | 0.3111 | -0.067 ± 0.006 | -0.0025 (44) |
| 25-40 | 3587 | 0.2237 | 0.1313 | +0.0924 ± 0.0038 | 0.6419 | 0.4004 | 0.5317 | 0.2189 | 0.2308 | -0.059 ± 0.0059 | -0.01 (1) |
| 40+ | 2347 | 0.3803 | 0.0441 | +0.3363 ± 0.0049 | 0.9902 | 0.1725 | 0.6315 | 0.1064 | 0.0609 | -0.081 ± 0.0041 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 445 | 0.2039 | 0.2043 | -0.0005 ± 0.0007 | 0.5898 | 0.5907 | 0.5048 | 0.4898 | 0.5056 | -0.105 ± 0.0231 | -0.01 (3) |
| 3-5 | 330 | 0.2207 | 0.2195 | +0.0012 ± 0.0021 | 0.6266 | 0.6242 | 0.5139 | 0.4739 | 0.4727 | -0.109 ± 0.0276 | 0.02 (1) |
| 5-10 | 708 | 0.203 | 0.2034 | -0.0004 ± 0.0025 | 0.5906 | 0.591 | 0.5448 | 0.47 | 0.5113 | -0.074 ± 0.0174 | -0.01 (4) |
| 10-15 | 662 | 0.2161 | 0.2094 | +0.0067 ± 0.0044 | 0.6219 | 0.6046 | 0.563 | 0.4388 | 0.4758 | -0.101 ± 0.0184 | -0.04 (5) |
| 15-25 | 954 | 0.2294 | 0.209 | +0.0205 ± 0.0058 | 0.6518 | 0.5998 | 0.5894 | 0.3933 | 0.4434 | -0.100 ± 0.0151 | -0.0133 (9) |
| 25-40 | 666 | 0.2606 | 0.2002 | +0.0604 ± 0.0109 | 0.7281 | 0.582 | 0.6555 | 0.3399 | 0.4039 | -0.106 ± 0.017 | -0.0075 (4) |
| 40+ | 248 | 0.3605 | 0.1725 | +0.1880 ± 0.0261 | 0.9954 | 0.5156 | 0.7336 | 0.2504 | 0.3105 | -0.076 ± 0.0253 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2512 | 0.1952 | 0.1953 | -0.0001 ± 0.0003 | 0.568 | 0.5681 | 0.5083 | 0.4935 | 0.506 | -0.045 ± 0.0091 | -0.0133 (15) |
| 3-5 | 1687 | 0.2006 | 0.2004 | +0.0002 ± 0.0009 | 0.5798 | 0.5785 | 0.5109 | 0.4709 | 0.4867 | -0.038 ± 0.0111 | 0.02 (1) |
| 5-10 | 3730 | 0.193 | 0.192 | +0.0010 ± 0.0011 | 0.5684 | 0.562 | 0.5038 | 0.4299 | 0.4619 | -0.029 ± 0.0073 | -0.0117 (6) |
| 10-15 | 3274 | 0.1987 | 0.1876 | +0.0110 ± 0.0019 | 0.5842 | 0.5478 | 0.5129 | 0.3888 | 0.4078 | -0.050 ± 0.0077 | -0.0189 (18) |
| 15-25 | 4635 | 0.2148 | 0.1775 | +0.0373 ± 0.0024 | 0.6254 | 0.5217 | 0.5255 | 0.3295 | 0.3355 | -0.068 ± 0.0062 | -0.0086 (42) |
| 25-40 | 4156 | 0.2501 | 0.1396 | +0.1105 ± 0.0037 | 0.7053 | 0.4264 | 0.5601 | 0.2434 | 0.2305 | -0.080 ± 0.0058 | -0.0044 (18) |
| 40+ | 3289 | 0.3955 | 0.0628 | +0.3327 ± 0.005 | 1.0422 | 0.2227 | 0.6538 | 0.1202 | 0.0885 | -0.070 ± 0.0043 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 563 | 0.1987 | 0.2011 | -0.0024 ± 0.0007 | 0.5773 | 0.583 | 0.4955 | 0.4802 | 0.5524 | -0.016 ± 0.0193 | -0.0137 (8) |
| 3-5 | 404 | 0.1978 | 0.1959 | +0.0019 ± 0.0018 | 0.5746 | 0.5701 | 0.5025 | 0.4629 | 0.4604 | -0.116 ± 0.0229 | 0.0067 (3) |
| 5-10 | 846 | 0.2017 | 0.1982 | +0.0035 ± 0.0023 | 0.5904 | 0.5781 | 0.5087 | 0.4348 | 0.4456 | -0.100 ± 0.0158 | -0.0071 (7) |
| 10-15 | 698 | 0.2089 | 0.2052 | +0.0037 ± 0.0043 | 0.6052 | 0.5928 | 0.5373 | 0.414 | 0.4628 | -0.085 ± 0.0171 | -0.0317 (6) |
| 15-25 | 855 | 0.23 | 0.2113 | +0.0187 ± 0.0061 | 0.6581 | 0.6055 | 0.5843 | 0.3903 | 0.4386 | -0.108 ± 0.0156 | -0.03 (1) |
| 25-40 | 537 | 0.2135 | 0.2173 | -0.0038 ± 0.0118 | 0.6146 | 0.6204 | 0.6665 | 0.3549 | 0.514 | -0.051 ± 0.018 | 0.015 (2) |
| 40+ | 110 | 0.3006 | 0.2046 | +0.0960 ± 0.0379 | 0.8265 | 0.5957 | 0.7598 | 0.3102 | 0.4364 | -0.083 ± 0.0397 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2922 | 0.1884 | 0.1892 | -0.0007 ± 0.0003 | 0.5518 | 0.5531 | 0.4896 | 0.4744 | 0.4925 | -0.034 ± 0.0081 | -0.0163 (35) |
| 3-5 | 1979 | 0.191 | 0.1887 | +0.0023 ± 0.0008 | 0.5598 | 0.5542 | 0.4847 | 0.4452 | 0.4376 | -0.067 ± 0.01 | -0.0094 (18) |
| 5-10 | 4336 | 0.196 | 0.1901 | +0.0060 ± 0.001 | 0.5766 | 0.5565 | 0.4849 | 0.411 | 0.4068 | -0.063 ± 0.0067 | -0.01 (31) |
| 10-15 | 3469 | 0.1949 | 0.1782 | +0.0167 ± 0.0018 | 0.5737 | 0.5254 | 0.4974 | 0.374 | 0.3684 | -0.071 ± 0.0071 | -0.015 (12) |
| 15-25 | 4722 | 0.2091 | 0.1716 | +0.0375 ± 0.0024 | 0.6118 | 0.5068 | 0.5096 | 0.3147 | 0.3158 | -0.070 ± 0.006 | -0.03 (2) |
| 25-40 | 3568 | 0.219 | 0.1341 | +0.0850 ± 0.0039 | 0.6322 | 0.4062 | 0.5364 | 0.2202 | 0.2455 | -0.049 ± 0.0059 | 0.01 (3) |
| 40+ | 2287 | 0.3947 | 0.0494 | +0.3453 ± 0.0053 | 1.0313 | 0.1862 | 0.644 | 0.1132 | 0.0669 | -0.083 ± 0.0044 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 935 | 0.1948 | 0.195 | -0.0002 ± 0.0005 | 0.5686 | 0.5688 | 0.508 | 0.4929 | 0.4963 | -0.058 ± 0.0147 | -0.0224 (49) |
| 3-5 | 650 | 0.1916 | 0.1911 | +0.0005 ± 0.0014 | 0.5603 | 0.558 | 0.4855 | 0.4457 | 0.4569 | -0.052 ± 0.0173 | -0.0194 (34) |
| 5-10 | 1378 | 0.2003 | 0.1938 | +0.0065 ± 0.0018 | 0.5893 | 0.5695 | 0.4947 | 0.4213 | 0.4158 | -0.073 ± 0.0121 | -0.005 (78) |
| 10-15 | 904 | 0.2091 | 0.1984 | +0.0107 ± 0.0037 | 0.6063 | 0.5788 | 0.5172 | 0.394 | 0.4104 | -0.064 ± 0.0151 | 0.0014 (64) |
| 15-25 | 1205 | 0.2306 | 0.2104 | +0.0202 ± 0.0052 | 0.6588 | 0.606 | 0.5721 | 0.3774 | 0.4241 | -0.065 ± 0.0132 | -0.0214 (59) |
| 25-40 | 733 | 0.2492 | 0.205 | +0.0442 ± 0.0103 | 0.7073 | 0.5902 | 0.6666 | 0.3538 | 0.4379 | -0.085 ± 0.0157 | -0.0219 (26) |
| 40+ | 251 | 0.3522 | 0.1961 | +0.1561 ± 0.0277 | 1.0175 | 0.5737 | 0.8065 | 0.3233 | 0.4223 | -0.092 ± 0.0251 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3064 | 0.1836 | 0.1837 | -0.0001 ± 0.0003 | 0.5398 | 0.5393 | 0.508 | 0.4927 | 0.501 | -0.039 ± 0.0078 | -0.0157 (88) |
| 3-5 | 2112 | 0.1916 | 0.1896 | +0.0020 ± 0.0008 | 0.5602 | 0.5558 | 0.4927 | 0.453 | 0.4479 | -0.053 ± 0.0096 | -0.0209 (69) |
| 5-10 | 4263 | 0.1979 | 0.1891 | +0.0088 ± 0.001 | 0.5815 | 0.556 | 0.4903 | 0.4167 | 0.3964 | -0.074 ± 0.0067 | -0.0082 (132) |
| 10-15 | 2939 | 0.2053 | 0.1903 | +0.0151 ± 0.002 | 0.5989 | 0.5591 | 0.5242 | 0.4011 | 0.4005 | -0.062 ± 0.0081 | -0.0053 (105) |
| 15-25 | 3651 | 0.2275 | 0.1983 | +0.0292 ± 0.0029 | 0.6569 | 0.5758 | 0.565 | 0.3696 | 0.3936 | -0.061 ± 0.0074 | -0.0253 (107) |
| 25-40 | 2549 | 0.2595 | 0.1827 | +0.0768 ± 0.0054 | 0.7357 | 0.5339 | 0.6279 | 0.3136 | 0.3511 | -0.077 ± 0.0083 | -0.0229 (51) |
| 40+ | 1161 | 0.3768 | 0.1429 | +0.2339 ± 0.0117 | 1.0701 | 0.4311 | 0.7283 | 0.2245 | 0.2567 | -0.072 ± 0.0104 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4013 | 1.049 ± 0.045 | 1.149 | 0.1678 | 0.1656 | 0.2133 | 0.2049 |
| gen2 | 4013 | 0.85 ± 0.041 | 1.108 | 0.1701 | 0.1661 | 0.2323 | 0.2047 |
| gen1_elo | 4013 | 1.023 ± 0.043 | 1.137 | 0.1747 | 0.1657 | 0.2125 | 0.2051 |
| gen1_sr | 4013 | 1.047 ± 0.054 | 1.18 | 0.1308 | 0.1681 | 0.2286 | 0.2043 |
| gen1_ledger | 6056 | 0.871 ± 0.031 | 1.081 | 0.1819 | 0.1803 | 0.2181 | 0.1992 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 20,089)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,647 | 23.1% |
| STALE_QUOTE | market_freshness | 4,259 | 21.2% |
| BOOK_QUALITY | execution | 3,803 | 18.9% |
| POOR_DATA | data | 2,280 | 11.3% |
| LIMITED_DATA | data | 1,278 | 6.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,098 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 955 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 843 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 599 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 327 | 1.6% |

Cause class: coverage 23.1%, market_freshness 21.2%, execution 18.9%, data 17.7%, market_freshness/coverage 8.5%, model_calibration_or_unknown 4.8%, mapping 4.2%, model_calibration 1.6%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 94.3%, LOW_DATA_QUALITY 71.1%, THIN_PLAYER_HISTORY 59.9%, STALE_PLAYER_DATA 51.0%, STALE_KALSHI_QUOTE 44.0%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 33.2%, WIDE_SPREAD 25.1%, MODEL_HIGH_UNCERTAINTY 17.7%, PLAYER_IDENTITY_RISK 16.0%, LEVEL_TRANSFER_RISK 10.8%, EVENT_MAPPING_RISK 8.1%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 3.1%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.7%, POST_SETTLEMENT_OBSERVATION 23.1%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 10,732)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,724 | 34.7% |
| BOOK_QUALITY | execution | 1,981 | 18.5% |
| STALE_QUOTE | market_freshness | 1,947 | 18.1% |
| POOR_DATA | data | 949 | 8.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 587 | 5.5% |
| IDENTITY_AMBIGUOUS | mapping | 478 | 4.5% |
| LIMITED_DATA | data | 390 | 3.6% |
| IN_PLAY_QUOTE | market_freshness/coverage | 377 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 224 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 75 | 0.7% |

Cause class: coverage 34.7%, execution 18.5%, market_freshness 18.1%, data 12.5%, market_freshness/coverage 9.0%, mapping 4.5%, model_calibration_or_unknown 2.1%, model_calibration 0.7%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.1%, LOW_DATA_QUALITY 74.9%, THIN_PLAYER_HISTORY 62.3%, STALE_KALSHI_QUOTE 51.9%, STALE_PLAYER_DATA 45.8%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 34.5%, WIDE_SPREAD 24.4%, PLAYER_IDENTITY_RISK 19.3%, MODEL_HIGH_UNCERTAINTY 18.0%, EVENT_MAPPING_RISK 9.7%, LEVEL_TRANSFER_RISK 9.7%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.8%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.8%, POST_SETTLEMENT_OBSERVATION 34.7%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 8391, "IDENTITY_AMBIGUOUS": 2341}; ticker orientation: {"VERIFIED": 10732}.

Checks: discipline:AMBIGUOUS 728, discipline:PASS 10004, identity_confidence:AMBIGUOUS 2072, identity_confidence:PASS 8660, level_mapping:NA 740, level_mapping:PASS 9992, market_pair:AMBIGUOUS 377, market_pair:NA 267, market_pair:PASS 10088, model_complement:NA 234, model_complement:PASS 10498, namesake:PASS 10732, physical_match_id:NA 3875, physical_match_id:PASS 6857, player_ids:PASS 10732, same_pair_other_event:PASS 10732, ticker_orientation:PASS 10732

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,752 | 5.0% | 4.5% | 1.7% | {"market_freshness": 53, "model_calibration_or_unknown": 43, "data": 35, "execution": 19, "market_freshness/coverage": 13, "model_calibration": 13, "coverage": 11} | 5.84 | 0.2247 / 0.2175 (427) | 18.9% | 4.0% | 3.3% | 2.9% |
| CHALLENGER | 7,457 | 17.4% | 7.0% | 12.1% | {"coverage": 730, "market_freshness/coverage": 161, "market_freshness": 147, "data": 128, "model_calibration_or_unknown": 58, "execution": 30, "model_calibration": 27, "mapping": 15} | 7.44 | 0.2177 / 0.2068 (1800) | 35.1% | 17.4% | 3.9% | 22.7% |
| DOUBLES | 1,520 | 47.9% | 47.3% | 6.8% | {"execution": 373, "mapping": 190, "market_freshness": 106, "market_freshness/coverage": 52, "coverage": 7} | 23.87 | 0.3161 / 0.2355 (385) | 15.4% | 0.0% | 100.0% | 7.0% |
| ITF_MEN | 13,335 | 25.1% | 17.5% | 31.2% | {"coverage": 1249, "execution": 661, "market_freshness": 551, "data": 447, "market_freshness/coverage": 286, "mapping": 157, "model_calibration_or_unknown": 2, "model_calibration": 1} | 11.76 | 0.2136 / 0.1954 (2981) | 37.1% | 68.2% | 18.6% | 22.3% |
| ITF_WOMEN | 17,969 | 27.0% | 19.7% | 45.2% | {"coverage": 1705, "market_freshness": 1012, "execution": 867, "data": 695, "market_freshness/coverage": 403, "mapping": 110, "model_calibration_or_unknown": 53, "model_calibration": 11} | 12.85 | 0.2034 / 0.1944 (3511) | 39.1% | 57.1% | 9.9% | 22.3% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,666 | 4.7% | 4.1% | 1.2% | {"market_freshness": 38, "model_calibration_or_unknown": 27, "execution": 17, "model_calibration": 12, "data": 11, "market_freshness/coverage": 10, "coverage": 9, "mapping": 1} | 7.84 | 0.2379 / 0.2309 (435) | 24.3% | 1.3% | 1.4% | 3.7% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.6% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 769 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 15 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 16 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 17 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 18 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 19 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 20 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 21 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 22 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 23 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 24 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 25 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 26 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 27 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 28 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 29 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 463 min (STALE); no external reference |
| 30 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 31 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 32 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 33 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 34 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 35 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 36 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 12.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 768 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 37 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 38 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 39 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 40 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 41 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 42 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 468 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 43 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 44 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 45 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 46 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 47 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 48 | `KXITFWMATCH-26OCT20CHAAPI-CHA` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 895 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 122.0, ratio 20.3); no external reference |
| 49 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.2h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 196 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |
| 50 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9709, "by_level_share_of_ge_25pp": {"ATP": 0.0174, "CHALLENGER": 0.1208, "DOUBLES": 0.0678, "ITF_MEN": 0.3125, "ITF_WOMEN": 0.4525, "OTHER": 0.0011, "WTA": 0.0116, "WTA125": 0.0162}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5194, "share_primary_cause_market_settled_or_in_play": 0.4368, "share_primary_cause_stale_quote_only": 0.1814}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 10732, "identity_ambiguous_share": 0.2181, "ticker_orientation": {"VERIFIED": 10732}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 6857, "with_external": 338, "coverage": 0.0493, "external_status": {"EXTERNAL_STALE": 204, "AGREES_WITH_KALSHI": 126, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 204, "MODEL_LONE_OUTLIER": 126, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3728, "share_external_supports_model": 0.0237}, "pregame_clean_ge_25pp": {"n": 3302, "with_external": 315, "coverage": 0.0954, "external_status": {"EXTERNAL_STALE": 188, "AGREES_WITH_KALSHI": 119, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 188, "MODEL_LONE_OUTLIER": 119, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3778, "share_external_supports_model": 0.0254}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 490.0, "median_sample_ratio": 2.44, "median_min_matches": 20.0, "median_max_days_since_last": 225.0, "share_severe_asymmetry": 0.2114, "data_status": {"POOR": 5992, "LIMITED": 2874, "ADEQUATE": 1866}, "comparison_lt_10pp": {"median_thinner_serve_points": 1680.0, "median_sample_ratio": 1.71, "median_min_matches": 92.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 796, "model_minus_observed": 0.0461, "kalshi_minus_observed": -0.0913, "brier_diff_model_minus_kalshi": -0.0041}, "4-10x": {"n": 548, "model_minus_observed": 0.0953, "kalshi_minus_observed": -0.0502, "brier_diff_model_minus_kalshi": 0.0142}, "<2x": {"n": 1969, "model_minus_observed": 0.0904, "kalshi_minus_observed": -0.0337, "brier_diff_model_minus_kalshi": 0.0126}, ">=10x": {"n": 700, "model_minus_observed": 0.1061, "kalshi_minus_observed": -0.0702, "brier_diff_model_minus_kalshi": 0.0063}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4013, "model": {"intercept": -0.541, "slope": 0.85, "slope_se": 0.041}, "kalshi_mid_same_rows": {"intercept": 0.23, "slope": 1.108, "slope_se": 0.046}, "mean_extremity_model": 0.1701, "mean_extremity_kalshi": 0.1661, "model_brier": 0.2323, "kalshi_brier": 0.2047, "brier_diff_model_minus_kalshi": 0.0276, "brier_diff_se": 0.003, "model_logloss": 0.661, "kalshi_logloss": 0.5919}, "fair_v1": {"n": 4013, "model": {"intercept": -0.412, "slope": 1.049, "slope_se": 0.045}, "kalshi_mid_same_rows": {"intercept": 0.313, "slope": 1.149, "slope_se": 0.047}, "mean_extremity_model": 0.1678, "mean_extremity_kalshi": 0.1656, "model_brier": 0.2133, "kalshi_brier": 0.2049, "brier_diff_model_minus_kalshi": 0.0084, "brier_diff_se": 0.0025, "model_logloss": 0.6148, "kalshi_logloss": 0.5922}, "gen1_elo": {"n": 4013, "model": {"intercept": -0.397, "slope": 1.023, "slope_se": 0.043}, "kalshi_mid_same_rows": {"intercept": 0.318, "slope": 1.137, "slope_se": 0.046}, "mean_extremity_model": 0.1747, "mean_extremity_kalshi": 0.1657, "model_brier": 0.2125, "kalshi_brier": 0.2051, "brier_diff_model_minus_kalshi": 0.0073, "brier_diff_se": 0.0025, "model_logloss": 0.6137, "kalshi_logloss": 0.5925}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2481, "share_ge_15": 0.4473, "median_abs_gap": 13.25, "n": 27638}, "gen1_elo": {"share_ge_25": 0.2456, "share_ge_15": 0.4457, "median_abs_gap": 13.01, "n": 27638}, "gen1_sr": {"share_ge_25": 0.3154, "share_ge_15": 0.5275, "median_abs_gap": 16.09, "n": 27638}, "gen2": {"share_ge_25": 0.3178, "share_ge_15": 0.5153, "median_abs_gap": 15.66, "n": 27638}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1545, "share_ge_15": 0.3624, "median_abs_gap": 10.98, "n": 21376}, "gen1_elo": {"share_ge_25": 0.156, "share_ge_15": 0.3587, "median_abs_gap": 10.67, "n": 21373}, "gen1_sr": {"share_ge_25": 0.2218, "share_ge_15": 0.4496, "median_abs_gap": 13.28, "n": 21377}, "gen2": {"share_ge_25": 0.2375, "share_ge_15": 0.4479, "median_abs_gap": 13.2, "n": 21378}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.84, "share_ge_25_all": 0.0498, "share_ge_25_pregame_clean": 0.0447}, "WTA": {"median_abs_gap_pregame_clean": 7.84, "share_ge_25_all": 0.0469, "share_ge_25_pregame_clean": 0.0413}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2344, "share_within_10pp_all": 0.431, "share_within_10pp_pregame_clean": 0.4841, "corr_model_vs_mid_pregame_clean": 0.8445}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 588, "model_brier": 0.1978, "kalshi_brier": 0.1989, "brier_diff_model_minus_kalshi": -0.0011}, "10-15": {"n_settled": 694, "model_brier": 0.2129, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": 0.0094}, "15-25": {"n_settled": 915, "model_brier": 0.2228, "kalshi_brier": 0.2124, "brier_diff_model_minus_kalshi": 0.0103}, "25-40": {"n_settled": 518, "model_brier": 0.2249, "kalshi_brier": 0.2103, "brier_diff_model_minus_kalshi": 0.0147}, "3-5": {"n_settled": 377, "model_brier": 0.2022, "kalshi_brier": 0.2016, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 104, "model_brier": 0.2868, "kalshi_brier": 0.1908, "brier_diff_model_minus_kalshi": 0.0961}, "5-10": {"n_settled": 817, "model_brier": 0.2026, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": 0.0005}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.541, "slope": 0.85, "slope_se": 0.041}, "kalshi_slope": {"intercept": 0.23, "slope": 1.108, "slope_se": 0.046}, "n": 4013}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.513, "slope": 0.871, "slope_se": 0.031}, "kalshi_slope": {"intercept": 0.157, "slope": 1.081, "slope_se": 0.036}, "n": 6056}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 385, "model_brier": 0.3161, "kalshi_brier": 0.2355, "brier_diff_model_minus_kalshi": 0.0806, "brier_diff_se": 0.0158, "corr_model_outcome": 0.0277, "corr_kalshi_outcome": 0.2551}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
