# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-22T01:50Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 48,525): 0-3 14.0%, 3-5 9.4%, 5-10 19.7%, 10-15 15.2%, 15-25 19.4%, 25-40 14.1%, 40+ 8.1%; median gap 12.15 pp.
* **Where the extremes live**: 97.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.5%, Challenger 12.0%, doubles 6.8%). Main tour: ATP 5.0% and WTA 4.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 10,777): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.6%, BOOK_QUALITY 18.4%, STALE_QUOTE 18.4%, POOR_DATA 8.8%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IDENTITY_AMBIGUOUS 4.5%, LIMITED_DATA 3.6%, IN_PLAY_QUOTE 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%. By class: coverage 34.6%, execution 18.4%, market_freshness 18.4%, data 12.4%, market_freshness/coverage 8.9%, mapping 4.5%, model_calibration_or_unknown 2.1%, model_calibration 0.7%.
* **Stale / settled / in-play**: 52.0% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 10,777 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.9% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.7% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 484.0 points vs 1670.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.045, Gen-2 0.849, Gen-1 ledger 0.869 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 520 model 0.225 vs Kalshi 0.2111; n 104 model 0.2868 vs Kalshi 0.1908.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 208,028 model-market comparisons (338,717 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 70,027 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-22T01:37:54.583138+00:00'], shadow board 55,387 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-22T01:37:58.097455+00:00'], Model 4 26,097 rows, 18,611 settled tickers, 6,508 tickers with an external scan.
* By model: {"gen1_ledger": 47339, "gen1_elo": 27853, "fair_v1": 27853, "gen2": 27853, "gen1_sr": 27853, "model4_fundamental": 24652, "model4_conditioned": 24625}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 48,525 | 14.0 | 9.4 | 19.7 | 15.2 | 19.4 | 14.1 | 8.1 | 12.15 | 41.6% | 22.2% |
| MW fair_v1 | 27,853 | 12.9 | 8.5 | 18.3 | 15.6 | 19.9 | 15.0 | 9.8 | 13.24 | 44.7% | 24.7% |
| MW gen1_elo | 27,853 | 12.9 | 8.6 | 18.9 | 15.2 | 20.0 | 15.0 | 9.5 | 13.01 | 44.5% | 24.5% |
| MW gen1_ledger | 20,672 | 15.4 | 10.7 | 21.5 | 14.8 | 18.7 | 12.9 | 5.9 | 10.59 | 37.5% | 18.8% |
| MW gen1_sr | 27,853 | 9.9 | 7.0 | 16.5 | 13.8 | 21.2 | 18.8 | 12.7 | 16.09 | 52.7% | 31.5% |
| MW gen2 | 27,853 | 10.9 | 7.2 | 16.2 | 14.2 | 19.7 | 17.9 | 13.8 | 15.65 | 51.5% | 31.8% |
| all families model4_conditioned | 24,625 | 21.7 | 19.1 | 34.5 | 17.7 | 4.4 | 1.4 | 1.0 | 5.96 | 6.9% | 2.5% |
| all families model4_fundamental | 24,652 | 16.5 | 13.2 | 34.0 | 20.4 | 11.0 | 3.5 | 1.3 | 7.84 | 15.8% | 4.8% |

Configurable thresholds (primary): >=5pp 76.5%, >=10pp 56.9%, >=15pp 41.6%, >=20pp 30.9%, >=25pp 22.2%, >=30pp 16.0%, >=40pp 8.1%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.48pp; >=10pp 45.4%, >=25pp 17.3%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,395 | 28.9 | 14.0 | 24.3 | 14.7 | 12.3 | 5.1 | 0.8 | 6.17 | 18.1% | 5.9% |
| CHALLENGER | 4,422 | 15.8 | 9.9 | 20.4 | 15.7 | 14.8 | 12.5 | 11.0 | 11.15 | 38.2% | 23.4% |
| ITF_MEN | 7,615 | 10.4 | 7.5 | 16.9 | 14.7 | 21.5 | 17.1 | 11.8 | 15.17 | 50.5% | 29.0% |
| ITF_WOMEN | 11,115 | 9.4 | 6.9 | 15.8 | 15.4 | 22.7 | 18.3 | 11.6 | 15.87 | 52.5% | 29.9% |
| WTA | 1,646 | 16.9 | 13.0 | 25.5 | 19.9 | 19.5 | 4.5 | 0.7 | 8.45 | 24.7% | 5.2% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,395 | 23.6 | 14.8 | 24.9 | 17.0 | 13.6 | 5.0 | 1.0 | 6.63 | 19.6% | 6.0% |
| CHALLENGER | 4,422 | 14.7 | 8.6 | 18.6 | 14.8 | 17.5 | 14.0 | 11.8 | 12.67 | 43.3% | 25.9% |
| ITF_MEN | 7,615 | 8.6 | 6.1 | 14.4 | 13.2 | 19.8 | 20.5 | 17.5 | 18.38 | 57.8% | 38.0% |
| ITF_WOMEN | 11,115 | 8.0 | 5.6 | 13.7 | 13.4 | 20.9 | 21.1 | 17.2 | 18.94 | 59.2% | 38.2% |
| WTA | 1,646 | 14.5 | 9.7 | 21.2 | 16.5 | 23.8 | 13.7 | 0.7 | 11.23 | 38.2% | 14.5% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,395 | 24.3 | 12.7 | 24.0 | 15.9 | 14.8 | 7.0 | 1.2 | 7.3 | 23.0% | 8.2% |
| CHALLENGER | 4,422 | 14.3 | 9.4 | 20.8 | 15.2 | 16.3 | 12.8 | 11.2 | 11.42 | 40.3% | 24.0% |
| ITF_MEN | 7,615 | 10.0 | 7.5 | 17.0 | 14.1 | 22.0 | 17.5 | 12.0 | 15.51 | 51.4% | 29.5% |
| ITF_WOMEN | 11,115 | 9.5 | 6.6 | 16.1 | 15.5 | 23.1 | 18.4 | 10.7 | 15.83 | 52.2% | 29.1% |
| WTA | 1,646 | 24.3 | 16.8 | 29.6 | 16.2 | 10.3 | 2.4 | 0.4 | 6.04 | 13.1% | 2.8% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,379 | 25.6 | 19.6 | 30.6 | 11.8 | 9.0 | 3.0 | 0.4 | 5.5 | 12.4% | 3.4% |
| CHALLENGER | 3,061 | 21.4 | 14.9 | 26.6 | 13.9 | 14.7 | 6.6 | 1.9 | 7.27 | 23.2% | 8.5% |
| DOUBLES | 1,532 | 5.3 | 4.2 | 11.4 | 10.1 | 21.0 | 26.4 | 21.5 | 24.06 | 69.0% | 48.0% |
| ITF_MEN | 5,844 | 13.8 | 8.8 | 20.2 | 16.0 | 21.3 | 13.3 | 6.7 | 12.14 | 41.2% | 19.9% |
| ITF_WOMEN | 6,947 | 12.7 | 9.0 | 19.3 | 15.1 | 21.6 | 16.3 | 6.1 | 12.87 | 44.0% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,028 | 22.3 | 15.9 | 29.6 | 18.2 | 10.1 | 3.6 | 0.3 | 6.97 | 14.0% | 3.9% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,330 | 29.2 | 14.2 | 24.8 | 14.6 | 12.0 | 4.7 | 0.5 | 5.99 | 17.2% | 5.2% |
| CHALLENGER | 3,125 | 20.6 | 12.3 | 25.1 | 18.1 | 15.2 | 6.7 | 2.0 | 8.34 | 23.8% | 8.7% |
| ITF_MEN | 5,604 | 12.7 | 9.0 | 20.2 | 16.5 | 22.5 | 14.1 | 5.0 | 12.35 | 41.6% | 19.1% |
| ITF_WOMEN | 8,297 | 11.2 | 8.2 | 18.0 | 17.5 | 24.6 | 15.4 | 5.1 | 13.53 | 45.1% | 20.5% |
| WTA | 1,598 | 17.1 | 12.8 | 25.5 | 20.1 | 19.5 | 4.2 | 0.7 | 8.43 | 24.3% | 4.9% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,330 | 24.0 | 15.2 | 25.1 | 16.9 | 13.6 | 4.7 | 0.6 | 6.49 | 18.9% | 5.3% |
| CHALLENGER | 3,125 | 18.6 | 10.9 | 23.2 | 17.7 | 17.7 | 9.7 | 2.2 | 9.36 | 29.6% | 11.9% |
| ITF_MEN | 5,605 | 10.2 | 7.3 | 16.7 | 14.9 | 21.6 | 18.9 | 10.4 | 15.42 | 50.9% | 29.3% |
| ITF_WOMEN | 8,298 | 9.1 | 6.5 | 15.2 | 15.0 | 23.0 | 20.6 | 10.8 | 16.61 | 54.3% | 31.3% |
| WTA | 1,598 | 14.5 | 9.7 | 21.2 | 16.4 | 23.8 | 13.6 | 0.8 | 11.23 | 38.2% | 14.4% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,337 | 25.8 | 19.8 | 30.7 | 12.0 | 8.5 | 2.9 | 0.2 | 5.4 | 11.7% | 3.1% |
| CHALLENGER | 2,666 | 22.9 | 16.0 | 28.2 | 13.9 | 14.1 | 4.5 | 0.6 | 6.68 | 19.1% | 5.0% |
| DOUBLES | 1,424 | 5.3 | 4.3 | 11.7 | 10.3 | 20.9 | 26.4 | 21.1 | 23.9 | 68.4% | 47.5% |
| ITF_MEN | 4,883 | 15.0 | 9.5 | 21.9 | 16.8 | 21.2 | 11.6 | 4.0 | 11.13 | 36.9% | 15.7% |
| ITF_WOMEN | 5,763 | 13.6 | 9.5 | 20.7 | 15.9 | 21.8 | 15.1 | 3.4 | 11.71 | 40.3% | 18.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 978 | 22.8 | 16.5 | 29.6 | 18.2 | 10.1 | 2.9 | 0.0 | 6.82 | 13.0% | 2.9% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,532 | 5.3 | 4.2 | 11.4 | 10.1 | 21.0 | 26.4 | 21.5 | 24.06 | 69.0% | 48.0% |
| singles | 19,140 | 16.2 | 11.2 | 22.3 | 15.2 | 18.5 | 11.8 | 4.7 | 10.03 | 35.0% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 6,224 | 13.2 | 8.8 | 18.9 | 15.7 | 18.9 | 14.9 | 9.6 | 12.93 | 43.4% | 24.5% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 17,380 | 13.3 | 8.5 | 18.4 | 15.2 | 20.1 | 14.8 | 9.7 | 13.24 | 44.6% | 24.5% |
| UNKNOWN | 4,012 | 11.1 | 7.8 | 17.1 | 17.0 | 20.6 | 16.0 | 10.4 | 13.84 | 47.0% | 26.5% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,760 | 19.6 | 11.7 | 21.3 | 16.5 | 15.7 | 9.0 | 6.2 | 9.22 | 30.9% | 15.2% |
| B | 3,485 | 12.5 | 9.0 | 19.8 | 16.7 | 19.3 | 12.2 | 10.4 | 12.38 | 41.9% | 22.6% |
| C | 3,926 | 11.7 | 8.8 | 19.4 | 14.8 | 19.6 | 15.3 | 10.4 | 13.33 | 45.3% | 25.7% |
| D | 4,513 | 12.1 | 7.8 | 17.1 | 15.6 | 21.7 | 15.8 | 10.0 | 14.03 | 47.4% | 25.8% |
| F | 8,169 | 7.7 | 5.6 | 15.0 | 14.6 | 23.4 | 21.4 | 12.3 | 17.82 | 57.1% | 33.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,798 | 23.0 | 15.9 | 28.8 | 15.0 | 11.8 | 4.1 | 1.5 | 6.65 | 17.3% | 5.5% |
| B | 2,840 | 16.3 | 10.5 | 23.4 | 16.0 | 19.2 | 10.7 | 3.9 | 9.97 | 33.8% | 14.6% |
| C | 4,085 | 11.3 | 7.4 | 18.3 | 14.2 | 21.5 | 16.6 | 10.7 | 14.39 | 48.9% | 27.3% |
| D | 2,945 | 14.5 | 9.8 | 19.8 | 14.4 | 21.0 | 14.4 | 6.1 | 12.04 | 41.5% | 20.5% |
| F | 5,004 | 10.1 | 8.1 | 15.6 | 14.8 | 22.9 | 20.3 | 8.3 | 15.75 | 51.4% | 28.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 8,879 | 17.8 | 10.4 | 20.6 | 16.4 | 16.3 | 9.8 | 8.6 | 10.37 | 34.7% | 18.4% |
| LIMITED | 6,016 | 13.4 | 10.2 | 20.3 | 15.5 | 19.2 | 13.6 | 7.7 | 11.91 | 40.5% | 21.3% |
| POOR | 12,958 | 9.3 | 6.4 | 15.9 | 15.0 | 22.8 | 19.2 | 11.5 | 16.17 | 53.4% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,291 | 26.5 | 20.3 | 34.3 | 12.4 | 4.8 | 1.5 | 0.2 | 5.32 | 6.5% | 1.6% |
| GAME_SPREAD | 4,550 | 22.4 | 15.2 | 33.5 | 17.2 | 9.0 | 2.3 | 0.3 | 6.69 | 11.7% | 2.6% |
| MATCH_WINNER | 20,672 | 15.4 | 10.7 | 21.5 | 14.8 | 18.7 | 12.9 | 5.9 | 10.59 | 37.5% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 9,515 | 29.4 | 16.9 | 30.9 | 12.6 | 8.2 | 1.7 | 0.4 | 5.47 | 10.3% | 2.1% |
| TOTAL_GAMES | 7,287 | 8.4 | 9.6 | 36.5 | 29.0 | 10.6 | 3.2 | 2.7 | 9.51 | 16.6% | 5.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,604 | 25.3 | 34.1 | 32.5 | 4.3 | 3.0 | 0.6 | 0.2 | 4.48 | 3.7% | 0.7% |
| GAME_SPREAD | 5,898 | 45.5 | 17.0 | 27.0 | 7.7 | 1.8 | 0.8 | 0.2 | 3.47 | 2.8% | 1.1% |
| TOTAL_GAMES | 10,123 | 4.8 | 7.7 | 40.6 | 35.0 | 7.2 | 2.5 | 2.2 | 9.69 | 11.9% | 4.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,607 | 24.2 | 17.9 | 35.5 | 12.5 | 7.1 | 2.5 | 0.3 | 5.81 | 10.0% | 2.9% |
| GAME_SPREAD | 5,901 | 19.3 | 13.2 | 28.0 | 20.2 | 13.9 | 4.5 | 0.9 | 7.97 | 19.2% | 5.4% |
| TOTAL_GAMES | 10,144 | 8.4 | 9.2 | 36.3 | 27.3 | 12.6 | 3.8 | 2.4 | 9.54 | 18.8% | 6.2% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 27,853 | 44.7% | 24.7% | 13.24 | 36.3% | 15.4% | 10.98 |
| gen1_elo | 27,853 | 44.5% | 24.5% | 13.01 | 35.9% | 15.6% | 10.69 |
| gen1_sr | 27,853 | 52.7% | 31.5% | 16.09 | 45.0% | 22.2% | 13.3 |
| gen2 | 27,853 | 51.5% | 31.8% | 15.65 | 44.8% | 23.8% | 13.21 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 14,154 | 15.8 | 10.3 | 21.1 | 17.2 | 20.4 | 11.9 | 3.3 | 10.81 | 35.6% | 15.2% |
| STALE | 13,699 | 9.9 | 6.7 | 15.5 | 13.9 | 19.4 | 18.2 | 16.4 | 16.97 | 54.0% | 34.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 14,140 | 16.5 | 11.2 | 22.3 | 14.9 | 17.9 | 12.3 | 4.9 | 9.98 | 35.0% | 17.1% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 48,525 | 14140 | 17626 | 16759 | 24.0 | 137.7 | 1400.4 |
| ge_15pp | 20,200 | 4956 | 6332 | 8912 | 25.9 | 434.7 | 1380.4 |
| ge_25pp | 10,777 | 2424 | 2745 | 5608 | 31.9 | 574.8 | 1380.4 |
| lt_10pp | 20,926 | 7083 | 8308 | 5535 | 22.1 | 47.5 | 1341.5 |

Current slate `SL-20261022T015049Z-8d5d029c`: 645 priced rows, quote age at build {'median': 13.2, 'max': 13.3}, freshness {'AGING': 645}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 22 | 0.0 | 0.0 | 22.7 | 4.5 | 40.9 | 31.8 | 0.0 | 20.48 | 72.7% | 31.8% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,580 | 19.6 | 10.8 | 23.9 | 18.7 | 18.9 | 7.3 | 0.7 | 9.09 | 26.9% | 8.0% |
| KALSHI_LONE_OUTLIER | 17 | 5.9 | 5.9 | 76.5 | 0.0 | 5.9 | 5.9 | 0.0 | 6.11 | 11.8% | 5.9% |
| MARKETS_AGREE | 489 | 66.0 | 34.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,080 | 0.0 | 2.2 | 34.3 | 25.9 | 25.8 | 10.9 | 0.8 | 12.73 | 37.6% | 11.8% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 27,853 | 4200 (15.1%) | 25.7% | 0.9% | {"EXTERNAL_STALE": 2580, "AGREES_WITH_KALSHI": 1080, "ALL_AGREE": 489, "SUPPORTS_MODEL_DIRECTION": 21, "AGREES_WITH_MODEL": 17, "EXTERNAL_OUTLIER": 12, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 12,445 | 1119 (9.0%) | 36.3% | 1.6% | {"EXTERNAL_STALE": 695, "AGREES_WITH_KALSHI": 406, "SUPPORTS_MODEL_DIRECTION": 16, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 6,891 | 342 (5.0%) | 37.1% | 2.3% | {"EXTERNAL_STALE": 207, "AGREES_WITH_KALSHI": 127, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,333 | 319 (9.6%) | 37.6% | 2.5% | {"EXTERNAL_STALE": 191, "AGREES_WITH_KALSHI": 120, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 11,074 | 2317 (20.9%) | 17.0% | 0.8% | {"EXTERNAL_STALE": 1402, "ALL_AGREE": 489, "AGREES_WITH_KALSHI": 394, "AGREES_WITH_MODEL": 15, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 4, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,305 | 10.5 | 7.6 | 19.3 | 14.3 | 22.3 | 15.9 | 10.0 | 14.12 | 48.3% | 25.9% |
| 4-10x | 3,651 | 11.0 | 8.4 | 18.8 | 15.4 | 21.2 | 14.9 | 10.3 | 13.83 | 46.4% | 25.2% |
| <2x | 14,144 | 14.9 | 9.6 | 18.8 | 16.6 | 18.1 | 13.2 | 8.9 | 11.98 | 40.1% | 22.1% |
| >=10x | 4,753 | 11.2 | 6.4 | 15.3 | 14.1 | 21.9 | 19.3 | 11.7 | 16.17 | 53.0% | 31.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 7,008 | 12.3 | 8.5 | 19.4 | 16.2 | 19.7 | 13.5 | 10.4 | 13.0 | 43.6% | 23.9% |
| 300-1000 | 6,044 | 11.6 | 8.7 | 17.1 | 15.2 | 20.8 | 16.5 | 10.1 | 14.06 | 47.4% | 26.6% |
| <300 | 9,120 | 8.9 | 5.7 | 15.5 | 14.7 | 23.0 | 20.1 | 12.1 | 16.86 | 55.2% | 32.2% |
| >=3000 | 5,681 | 21.6 | 12.9 | 22.9 | 16.5 | 14.5 | 7.0 | 4.8 | 8.01 | 26.2% | 11.7% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 799 | 0.5467 | 0.4093 | 0.4994 | +0.047 | -0.090 | -0.0035 ± 0.0054 |
| ratio 4-10x | 549 | 0.5843 | 0.439 | 0.4882 | +0.096 | -0.049 | 0.0143 ± 0.0069 |
| ratio <2x | 1972 | 0.5363 | 0.412 | 0.4462 | +0.090 | -0.034 | 0.0123 ± 0.0032 |
| ratio >=10x | 701 | 0.5665 | 0.3902 | 0.4593 | +0.107 | -0.069 | 0.0066 ± 0.0069 |
| thinner_sample 1000-3000 | 1091 | 0.5419 | 0.4139 | 0.4482 | +0.094 | -0.034 | 0.0108 ± 0.0044 |
| thinner_sample 300-1000 | 936 | 0.5634 | 0.4209 | 0.4915 | +0.072 | -0.070 | 0.0012 ± 0.0053 |
| thinner_sample <300 | 1332 | 0.5555 | 0.3889 | 0.4595 | +0.096 | -0.071 | 0.0096 ± 0.0049 |
| thinner_sample >=3000 | 662 | 0.5343 | 0.4389 | 0.4653 | +0.069 | -0.026 | 0.0128 ± 0.0046 |
| data_status ADEQUATE | 1144 | 0.5378 | 0.4312 | 0.4528 | +0.085 | -0.022 | 0.0125 ± 0.0037 |
| data_status LIMITED | 952 | 0.548 | 0.4154 | 0.4769 | +0.071 | -0.061 | 0.0045 ± 0.0048 |
| data_status POOR | 1925 | 0.5586 | 0.3976 | 0.466 | +0.093 | -0.068 | 0.008 ± 0.004 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 590 | 0.1974 | 0.1985 | -0.0011 ± 0.0006 | 0.5736 | 0.5759 | 0.4982 | 0.4834 | 0.5305 | -0.057 ± 0.0191 | -0.01 (5) |
| 3-5 | 377 | 0.2022 | 0.2016 | +0.0006 ± 0.0019 | 0.588 | 0.5848 | 0.5004 | 0.4603 | 0.4721 | -0.095 ± 0.0238 | 0.02 (1) |
| 5-10 | 818 | 0.2027 | 0.2021 | +0.0006 ± 0.0024 | 0.5915 | 0.5878 | 0.512 | 0.4375 | 0.4658 | -0.090 ± 0.0164 | -0.0167 (6) |
| 10-15 | 694 | 0.2129 | 0.2034 | +0.0094 ± 0.0043 | 0.6153 | 0.5881 | 0.5235 | 0.3994 | 0.4222 | -0.101 ± 0.0171 | -0.048 (5) |
| 15-25 | 918 | 0.224 | 0.2128 | +0.0112 ± 0.0059 | 0.6429 | 0.6093 | 0.5758 | 0.38 | 0.4499 | -0.086 ± 0.015 | -0.0033 (9) |
| 25-40 | 520 | 0.225 | 0.2111 | +0.0139 ± 0.012 | 0.638 | 0.6066 | 0.6556 | 0.3459 | 0.475 | -0.072 ± 0.0185 | -0.01 (1) |
| 40+ | 104 | 0.2868 | 0.1908 | +0.0961 ± 0.0376 | 0.7842 | 0.5653 | 0.7516 | 0.3041 | 0.4231 | -0.092 ± 0.0368 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3000 | 0.1833 | 0.1843 | -0.0010 ± 0.0003 | 0.5408 | 0.5418 | 0.4852 | 0.4701 | 0.506 | -0.020 ± 0.0079 | -0.0129 (17) |
| 3-5 | 1977 | 0.1988 | 0.1975 | +0.0012 ± 0.0008 | 0.5782 | 0.572 | 0.4824 | 0.4425 | 0.4461 | -0.053 ± 0.0102 | 0.0 (2) |
| 5-10 | 4191 | 0.1983 | 0.1954 | +0.0029 ± 0.001 | 0.5793 | 0.5699 | 0.4816 | 0.4076 | 0.424 | -0.046 ± 0.0069 | -0.0119 (21) |
| 10-15 | 3624 | 0.2 | 0.1822 | +0.0178 ± 0.0018 | 0.5864 | 0.536 | 0.4838 | 0.3592 | 0.3499 | -0.072 ± 0.0071 | -0.0281 (16) |
| 15-25 | 4595 | 0.207 | 0.1698 | +0.0372 ± 0.0024 | 0.6073 | 0.5027 | 0.5021 | 0.3057 | 0.3099 | -0.069 ± 0.006 | -0.0025 (44) |
| 25-40 | 3601 | 0.2244 | 0.1324 | +0.0920 ± 0.0038 | 0.6433 | 0.4032 | 0.5318 | 0.2191 | 0.2316 | -0.058 ± 0.0059 | -0.01 (1) |
| 40+ | 2349 | 0.3806 | 0.044 | +0.3365 ± 0.0049 | 0.9907 | 0.1723 | 0.6316 | 0.1064 | 0.0609 | -0.081 ± 0.0041 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 446 | 0.2036 | 0.204 | -0.0004 ± 0.0007 | 0.5892 | 0.5901 | 0.5043 | 0.4893 | 0.5045 | -0.105 ± 0.023 | -0.01 (3) |
| 3-5 | 330 | 0.2207 | 0.2195 | +0.0012 ± 0.0021 | 0.6266 | 0.6242 | 0.5139 | 0.4739 | 0.4727 | -0.109 ± 0.0276 | 0.02 (1) |
| 5-10 | 710 | 0.2035 | 0.2039 | -0.0004 ± 0.0026 | 0.5916 | 0.5921 | 0.5446 | 0.4698 | 0.5113 | -0.074 ± 0.0174 | -0.01 (4) |
| 10-15 | 663 | 0.216 | 0.2092 | +0.0068 ± 0.0044 | 0.6217 | 0.6042 | 0.5628 | 0.4385 | 0.4751 | -0.101 ± 0.0184 | -0.04 (5) |
| 15-25 | 955 | 0.2296 | 0.209 | +0.0207 ± 0.0058 | 0.6523 | 0.5999 | 0.5895 | 0.3935 | 0.4429 | -0.101 ± 0.0151 | -0.0133 (9) |
| 25-40 | 668 | 0.2612 | 0.2 | +0.0611 ± 0.0109 | 0.7292 | 0.5814 | 0.6555 | 0.3398 | 0.4027 | -0.107 ± 0.017 | -0.0075 (4) |
| 40+ | 249 | 0.36 | 0.1751 | +0.1849 ± 0.0261 | 0.9941 | 0.523 | 0.7327 | 0.2498 | 0.3133 | -0.072 ± 0.0254 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2520 | 0.1948 | 0.195 | -0.0001 ± 0.0003 | 0.5673 | 0.5674 | 0.5081 | 0.4933 | 0.5056 | -0.045 ± 0.0091 | -0.0133 (15) |
| 3-5 | 1687 | 0.2006 | 0.2004 | +0.0002 ± 0.0009 | 0.5798 | 0.5785 | 0.5109 | 0.4709 | 0.4867 | -0.038 ± 0.0111 | 0.02 (1) |
| 5-10 | 3738 | 0.1934 | 0.1925 | +0.0009 ± 0.0011 | 0.5692 | 0.5632 | 0.5037 | 0.4297 | 0.4625 | -0.028 ± 0.0073 | -0.0117 (6) |
| 10-15 | 3284 | 0.1988 | 0.1875 | +0.0113 ± 0.0019 | 0.5846 | 0.5476 | 0.5129 | 0.3888 | 0.4065 | -0.051 ± 0.0077 | -0.0189 (18) |
| 15-25 | 4641 | 0.2151 | 0.1775 | +0.0375 ± 0.0024 | 0.626 | 0.5219 | 0.5257 | 0.3297 | 0.3351 | -0.069 ± 0.0062 | -0.0086 (42) |
| 25-40 | 4174 | 0.2506 | 0.1402 | +0.1104 ± 0.0037 | 0.7063 | 0.428 | 0.5603 | 0.2435 | 0.2307 | -0.079 ± 0.0058 | -0.0044 (18) |
| 40+ | 3293 | 0.3956 | 0.063 | +0.3326 ± 0.005 | 1.0424 | 0.2233 | 0.6539 | 0.1203 | 0.0887 | -0.069 ± 0.0043 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 563 | 0.1987 | 0.2011 | -0.0024 ± 0.0007 | 0.5773 | 0.583 | 0.4955 | 0.4802 | 0.5524 | -0.016 ± 0.0193 | -0.0137 (8) |
| 3-5 | 405 | 0.1981 | 0.1961 | +0.0020 ± 0.0018 | 0.5751 | 0.5704 | 0.5027 | 0.463 | 0.4593 | -0.118 ± 0.0229 | 0.0067 (3) |
| 5-10 | 848 | 0.2013 | 0.1979 | +0.0034 ± 0.0023 | 0.5895 | 0.5775 | 0.5094 | 0.4354 | 0.4469 | -0.099 ± 0.0157 | -0.0071 (7) |
| 10-15 | 699 | 0.2086 | 0.2049 | +0.0037 ± 0.0042 | 0.6047 | 0.5921 | 0.5369 | 0.4135 | 0.4621 | -0.085 ± 0.017 | -0.0317 (6) |
| 15-25 | 858 | 0.2312 | 0.2117 | +0.0195 ± 0.0061 | 0.6611 | 0.6064 | 0.5849 | 0.3909 | 0.4371 | -0.110 ± 0.0156 | -0.03 (1) |
| 25-40 | 538 | 0.2137 | 0.2185 | -0.0047 ± 0.0118 | 0.615 | 0.6236 | 0.666 | 0.3544 | 0.5149 | -0.049 ± 0.0181 | 0.015 (2) |
| 40+ | 110 | 0.3006 | 0.2046 | +0.0960 ± 0.0379 | 0.8265 | 0.5957 | 0.7598 | 0.3102 | 0.4364 | -0.083 ± 0.0397 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2922 | 0.1884 | 0.1892 | -0.0007 ± 0.0003 | 0.5518 | 0.5531 | 0.4896 | 0.4744 | 0.4925 | -0.034 ± 0.0081 | -0.0163 (35) |
| 3-5 | 1985 | 0.1906 | 0.1883 | +0.0023 ± 0.0008 | 0.5591 | 0.5534 | 0.4841 | 0.4445 | 0.4363 | -0.068 ± 0.01 | -0.0094 (18) |
| 5-10 | 4351 | 0.1958 | 0.1898 | +0.0060 ± 0.001 | 0.576 | 0.5561 | 0.4857 | 0.4118 | 0.4077 | -0.063 ± 0.0067 | -0.01 (31) |
| 10-15 | 3474 | 0.1947 | 0.1781 | +0.0166 ± 0.0018 | 0.5733 | 0.5251 | 0.4976 | 0.3742 | 0.3687 | -0.071 ± 0.0071 | -0.015 (12) |
| 15-25 | 4737 | 0.2104 | 0.1721 | +0.0383 ± 0.0024 | 0.6148 | 0.508 | 0.5105 | 0.3155 | 0.3148 | -0.072 ± 0.006 | -0.03 (2) |
| 25-40 | 3579 | 0.2196 | 0.1351 | +0.0844 ± 0.0039 | 0.6332 | 0.4089 | 0.5365 | 0.2203 | 0.2464 | -0.048 ± 0.0059 | 0.01 (3) |
| 40+ | 2289 | 0.3949 | 0.0494 | +0.3455 ± 0.0053 | 1.0318 | 0.1861 | 0.6441 | 0.1131 | 0.0668 | -0.083 ± 0.0044 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 937 | 0.1947 | 0.195 | -0.0002 ± 0.0005 | 0.5685 | 0.5687 | 0.5082 | 0.4931 | 0.4973 | -0.058 ± 0.0146 | -0.0224 (49) |
| 3-5 | 651 | 0.1914 | 0.191 | +0.0005 ± 0.0014 | 0.5598 | 0.5576 | 0.4859 | 0.4461 | 0.4578 | -0.051 ± 0.0173 | -0.0194 (34) |
| 5-10 | 1380 | 0.2002 | 0.1938 | +0.0065 ± 0.0018 | 0.5891 | 0.5693 | 0.4945 | 0.4211 | 0.4159 | -0.073 ± 0.0121 | -0.005 (78) |
| 10-15 | 905 | 0.2092 | 0.1984 | +0.0108 ± 0.0037 | 0.6065 | 0.5789 | 0.5172 | 0.3941 | 0.4099 | -0.064 ± 0.0151 | 0.0014 (64) |
| 15-25 | 1209 | 0.2311 | 0.2108 | +0.0203 ± 0.0052 | 0.6602 | 0.6069 | 0.5726 | 0.3779 | 0.4243 | -0.066 ± 0.0132 | -0.0214 (59) |
| 25-40 | 734 | 0.2494 | 0.2058 | +0.0435 ± 0.0103 | 0.7076 | 0.5926 | 0.6662 | 0.3535 | 0.4387 | -0.084 ± 0.0157 | -0.0219 (26) |
| 40+ | 252 | 0.3533 | 0.1959 | +0.1574 ± 0.0276 | 1.0198 | 0.5733 | 0.8064 | 0.3235 | 0.4206 | -0.094 ± 0.025 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3079 | 0.1832 | 0.1834 | -0.0001 ± 0.0003 | 0.5391 | 0.5387 | 0.5078 | 0.4925 | 0.5018 | -0.038 ± 0.0078 | -0.0157 (88) |
| 3-5 | 2115 | 0.1914 | 0.1895 | +0.0019 ± 0.0008 | 0.5599 | 0.5556 | 0.493 | 0.4533 | 0.4487 | -0.053 ± 0.0095 | -0.0209 (69) |
| 5-10 | 4277 | 0.1978 | 0.189 | +0.0088 ± 0.001 | 0.5811 | 0.5557 | 0.4907 | 0.4171 | 0.3975 | -0.073 ± 0.0067 | -0.0082 (132) |
| 10-15 | 2942 | 0.2054 | 0.1903 | +0.0151 ± 0.002 | 0.599 | 0.5592 | 0.5242 | 0.4011 | 0.4004 | -0.062 ± 0.0081 | -0.0053 (105) |
| 15-25 | 3679 | 0.2288 | 0.1998 | +0.0291 ± 0.0029 | 0.6604 | 0.5792 | 0.5656 | 0.3701 | 0.3944 | -0.061 ± 0.0074 | -0.0253 (107) |
| 25-40 | 2552 | 0.2596 | 0.183 | +0.0765 ± 0.0054 | 0.7358 | 0.5347 | 0.6279 | 0.3135 | 0.3515 | -0.077 ± 0.0083 | -0.0229 (51) |
| 40+ | 1163 | 0.3773 | 0.1429 | +0.2344 ± 0.0117 | 1.071 | 0.4312 | 0.7284 | 0.2248 | 0.2562 | -0.072 ± 0.0104 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4021 | 1.045 ± 0.045 | 1.143 | 0.1678 | 0.1656 | 0.2136 | 0.2051 |
| gen2 | 4021 | 0.849 ± 0.041 | 1.104 | 0.17 | 0.1661 | 0.2325 | 0.2048 |
| gen1_elo | 4021 | 1.02 ± 0.043 | 1.131 | 0.1748 | 0.1657 | 0.2127 | 0.2053 |
| gen1_sr | 4021 | 1.045 ± 0.054 | 1.174 | 0.1307 | 0.1681 | 0.2287 | 0.2044 |
| gen1_ledger | 6068 | 0.869 ± 0.031 | 1.079 | 0.182 | 0.1803 | 0.2182 | 0.1993 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 20,200)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,650 | 23.0% |
| STALE_QUOTE | market_freshness | 4,339 | 21.5% |
| BOOK_QUALITY | execution | 3,812 | 18.9% |
| POOR_DATA | data | 2,288 | 11.3% |
| LIMITED_DATA | data | 1,280 | 6.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,100 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 955 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 848 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 599 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 329 | 1.6% |

Cause class: coverage 23.0%, market_freshness 21.5%, execution 18.9%, data 17.7%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.7%, mapping 4.2%, model_calibration 1.6%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 94.3%, LOW_DATA_QUALITY 71.2%, THIN_PLAYER_HISTORY 59.9%, STALE_PLAYER_DATA 50.8%, STALE_KALSHI_QUOTE 44.1%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 33.3%, WIDE_SPREAD 25.1%, MODEL_HIGH_UNCERTAINTY 17.7%, PLAYER_IDENTITY_RISK 16.1%, LEVEL_TRANSFER_RISK 10.9%, EVENT_MAPPING_RISK 8.1%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.1%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.6%, POST_SETTLEMENT_OBSERVATION 23.0%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 10,777)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,727 | 34.6% |
| BOOK_QUALITY | execution | 1,987 | 18.4% |
| STALE_QUOTE | market_freshness | 1,978 | 18.4% |
| POOR_DATA | data | 951 | 8.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 588 | 5.5% |
| IDENTITY_AMBIGUOUS | mapping | 480 | 4.5% |
| LIMITED_DATA | data | 390 | 3.6% |
| IN_PLAY_QUOTE | market_freshness/coverage | 377 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 224 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 75 | 0.7% |

Cause class: coverage 34.6%, execution 18.4%, market_freshness 18.4%, data 12.4%, market_freshness/coverage 8.9%, mapping 4.5%, model_calibration_or_unknown 2.1%, model_calibration 0.7%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.1%, LOW_DATA_QUALITY 74.9%, THIN_PLAYER_HISTORY 62.4%, STALE_KALSHI_QUOTE 52.0%, STALE_PLAYER_DATA 45.7%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 34.6%, WIDE_SPREAD 24.5%, PLAYER_IDENTITY_RISK 19.4%, MODEL_HIGH_UNCERTAINTY 18.0%, EVENT_MAPPING_RISK 9.8%, LEVEL_TRANSFER_RISK 9.7%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.7%, POST_SETTLEMENT_OBSERVATION 34.6%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 8417, "IDENTITY_AMBIGUOUS": 2360}; ticker orientation: {"VERIFIED": 10777}.

Checks: discipline:AMBIGUOUS 735, discipline:PASS 10042, identity_confidence:AMBIGUOUS 2089, identity_confidence:PASS 8688, level_mapping:NA 747, level_mapping:PASS 10030, market_pair:AMBIGUOUS 381, market_pair:NA 268, market_pair:PASS 10128, model_complement:NA 235, model_complement:PASS 10542, namesake:PASS 10777, physical_match_id:NA 3886, physical_match_id:PASS 6891, player_ids:PASS 10777, same_pair_other_event:PASS 10777, ticker_orientation:PASS 10777

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,774 | 5.0% | 4.5% | 1.7% | {"market_freshness": 53, "model_calibration_or_unknown": 43, "data": 35, "execution": 19, "market_freshness/coverage": 13, "model_calibration": 13, "coverage": 11} | 5.84 | 0.224 / 0.2168 (429) | 19.2% | 4.0% | 3.3% | 2.8% |
| CHALLENGER | 7,483 | 17.3% | 7.0% | 12.0% | {"coverage": 730, "market_freshness/coverage": 161, "market_freshness": 147, "data": 128, "model_calibration_or_unknown": 58, "execution": 30, "model_calibration": 27, "mapping": 15} | 7.43 | 0.2176 / 0.2067 (1802) | 35.2% | 17.4% | 3.9% | 22.6% |
| DOUBLES | 1,532 | 48.0% | 47.5% | 6.8% | {"execution": 377, "mapping": 193, "market_freshness": 106, "market_freshness/coverage": 52, "coverage": 7} | 23.9 | 0.3147 / 0.2359 (389) | 15.3% | 0.0% | 100.0% | 7.0% |
| ITF_MEN | 13,459 | 25.1% | 17.5% | 31.3% | {"coverage": 1251, "execution": 663, "market_freshness": 564, "data": 449, "market_freshness/coverage": 287, "mapping": 156, "model_calibration_or_unknown": 2, "model_calibration": 1} | 11.77 | 0.2144 / 0.1961 (2989) | 37.4% | 68.4% | 18.8% | 22.1% |
| ITF_WOMEN | 18,062 | 27.0% | 19.7% | 45.2% | {"coverage": 1706, "market_freshness": 1030, "execution": 867, "data": 695, "market_freshness/coverage": 403, "mapping": 110, "model_calibration_or_unknown": 53, "model_calibration": 11} | 12.86 | 0.2035 / 0.1943 (3515) | 39.4% | 57.0% | 9.9% | 22.2% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,674 | 4.7% | 4.1% | 1.2% | {"market_freshness": 38, "model_calibration_or_unknown": 27, "execution": 17, "model_calibration": 12, "data": 11, "market_freshness/coverage": 10, "coverage": 9, "mapping": 1} | 7.83 | 0.2379 / 0.2309 (435) | 24.5% | 1.3% | 1.4% | 3.7% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.6% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 151 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 15 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 16 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 17 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 18 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 19 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 20 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 21 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 22 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 23 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 24 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 25 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 26 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 27 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 28 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 29 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 463 min (STALE); no external reference |
| 30 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 31 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 32 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 33 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 34 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 35 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 36 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 37 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 38 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 39 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 40 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 41 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 42 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 43 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 44 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 45 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 874 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 46 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 47 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 48 | `KXITFWMATCH-26OCT20CHAAPI-CHA` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 812 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 122.0, ratio 20.3); no external reference |
| 49 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 770 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |
| 50 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9711, "by_level_share_of_ge_25pp": {"ATP": 0.0174, "CHALLENGER": 0.1203, "DOUBLES": 0.0682, "ITF_MEN": 0.313, "ITF_WOMEN": 0.4524, "OTHER": 0.0011, "WTA": 0.0116, "WTA125": 0.0161}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5204, "share_primary_cause_market_settled_or_in_play": 0.4354, "share_primary_cause_stale_quote_only": 0.1835}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 10777, "identity_ambiguous_share": 0.219, "ticker_orientation": {"VERIFIED": 10777}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 6891, "with_external": 342, "coverage": 0.0496, "external_status": {"EXTERNAL_STALE": 207, "AGREES_WITH_KALSHI": 127, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 207, "MODEL_LONE_OUTLIER": 127, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3713, "share_external_supports_model": 0.0234}, "pregame_clean_ge_25pp": {"n": 3333, "with_external": 319, "coverage": 0.0957, "external_status": {"EXTERNAL_STALE": 191, "AGREES_WITH_KALSHI": 120, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 191, "MODEL_LONE_OUTLIER": 120, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3762, "share_external_supports_model": 0.0251}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 484.0, "median_sample_ratio": 2.44, "median_min_matches": 20.0, "median_max_days_since_last": 225.0, "share_severe_asymmetry": 0.2119, "data_status": {"POOR": 6024, "LIMITED": 2883, "ADEQUATE": 1870}, "comparison_lt_10pp": {"median_thinner_serve_points": 1670.0, "median_sample_ratio": 1.71, "median_min_matches": 92.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 799, "model_minus_observed": 0.0474, "kalshi_minus_observed": -0.09, "brier_diff_model_minus_kalshi": -0.0035}, "4-10x": {"n": 549, "model_minus_observed": 0.0961, "kalshi_minus_observed": -0.0492, "brier_diff_model_minus_kalshi": 0.0143}, "<2x": {"n": 1972, "model_minus_observed": 0.09, "kalshi_minus_observed": -0.0342, "brier_diff_model_minus_kalshi": 0.0123}, ">=10x": {"n": 701, "model_minus_observed": 0.1071, "kalshi_minus_observed": -0.0691, "brier_diff_model_minus_kalshi": 0.0066}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4021, "model": {"intercept": -0.541, "slope": 0.849, "slope_se": 0.041}, "kalshi_mid_same_rows": {"intercept": 0.228, "slope": 1.104, "slope_se": 0.046}, "mean_extremity_model": 0.17, "mean_extremity_kalshi": 0.1661, "model_brier": 0.2325, "kalshi_brier": 0.2048, "brier_diff_model_minus_kalshi": 0.0276, "brier_diff_se": 0.003, "model_logloss": 0.6614, "kalshi_logloss": 0.5923}, "fair_v1": {"n": 4021, "model": {"intercept": -0.412, "slope": 1.045, "slope_se": 0.045}, "kalshi_mid_same_rows": {"intercept": 0.309, "slope": 1.143, "slope_se": 0.047}, "mean_extremity_model": 0.1678, "mean_extremity_kalshi": 0.1656, "model_brier": 0.2136, "kalshi_brier": 0.2051, "brier_diff_model_minus_kalshi": 0.0085, "brier_diff_se": 0.0025, "model_logloss": 0.6154, "kalshi_logloss": 0.5926}, "gen1_elo": {"n": 4021, "model": {"intercept": -0.398, "slope": 1.02, "slope_se": 0.043}, "kalshi_mid_same_rows": {"intercept": 0.315, "slope": 1.131, "slope_se": 0.046}, "mean_extremity_model": 0.1748, "mean_extremity_kalshi": 0.1657, "model_brier": 0.2127, "kalshi_brier": 0.2053, "brier_diff_model_minus_kalshi": 0.0074, "brier_diff_se": 0.0025, "model_logloss": 0.6142, "kalshi_logloss": 0.5929}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2474, "share_ge_15": 0.4468, "median_abs_gap": 13.24, "n": 27853}, "gen1_elo": {"share_ge_25": 0.245, "share_ge_15": 0.4452, "median_abs_gap": 13.01, "n": 27853}, "gen1_sr": {"share_ge_25": 0.3152, "share_ge_15": 0.5274, "median_abs_gap": 16.09, "n": 27853}, "gen2": {"share_ge_25": 0.3178, "share_ge_15": 0.5151, "median_abs_gap": 15.65, "n": 27853}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1544, "share_ge_15": 0.3626, "median_abs_gap": 10.98, "n": 21588}, "gen1_elo": {"share_ge_25": 0.1559, "share_ge_15": 0.3587, "median_abs_gap": 10.69, "n": 21585}, "gen1_sr": {"share_ge_25": 0.2225, "share_ge_15": 0.4503, "median_abs_gap": 13.3, "n": 21589}, "gen2": {"share_ge_25": 0.2382, "share_ge_15": 0.4482, "median_abs_gap": 13.21, "n": 21590}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.84, "share_ge_25_all": 0.0495, "share_ge_25_pregame_clean": 0.0445}, "WTA": {"median_abs_gap_pregame_clean": 7.83, "share_ge_25_all": 0.0467, "share_ge_25_pregame_clean": 0.0411}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2345, "share_within_10pp_all": 0.4312, "share_within_10pp_pregame_clean": 0.4841, "corr_model_vs_mid_pregame_clean": 0.8449}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 590, "model_brier": 0.1974, "kalshi_brier": 0.1985, "brier_diff_model_minus_kalshi": -0.0011}, "10-15": {"n_settled": 694, "model_brier": 0.2129, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": 0.0094}, "15-25": {"n_settled": 918, "model_brier": 0.224, "kalshi_brier": 0.2128, "brier_diff_model_minus_kalshi": 0.0112}, "25-40": {"n_settled": 520, "model_brier": 0.225, "kalshi_brier": 0.2111, "brier_diff_model_minus_kalshi": 0.0139}, "3-5": {"n_settled": 377, "model_brier": 0.2022, "kalshi_brier": 0.2016, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 104, "model_brier": 0.2868, "kalshi_brier": 0.1908, "brier_diff_model_minus_kalshi": 0.0961}, "5-10": {"n_settled": 818, "model_brier": 0.2027, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": 0.0006}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.541, "slope": 0.849, "slope_se": 0.041}, "kalshi_slope": {"intercept": 0.228, "slope": 1.104, "slope_se": 0.046}, "n": 4021}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.511, "slope": 0.869, "slope_se": 0.031}, "kalshi_slope": {"intercept": 0.157, "slope": 1.079, "slope_se": 0.036}, "n": 6068}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 389, "model_brier": 0.3147, "kalshi_brier": 0.2359, "brier_diff_model_minus_kalshi": 0.0787, "brier_diff_se": 0.0157, "corr_model_outcome": 0.0207, "corr_kalshi_outcome": 0.2553}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
