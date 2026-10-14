# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-14T12:35Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 32,455): 0-3 14.5%, 3-5 9.5%, 5-10 20.2%, 10-15 15.4%, 15-25 18.7%, 25-40 13.5%, 40+ 8.2%; median gap 11.77 pp.
* **Where the extremes live**: 98.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.3%, Challenger 12.4%, doubles 7.0%). Main tour: ATP 1.4% and WTA 6.3% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 7,035): MARKET_ALREADY_SETTLED_WHEN_PRICED 37.6%, BOOK_QUALITY 17.8%, STALE_QUOTE 16.5%, POOR_DATA 8.5%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.5%, LIMITED_DATA 4.1%, IN_PLAY_QUOTE 3.2%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.4%. By class: coverage 37.6%, execution 17.8%, market_freshness 16.5%, data 12.6%, market_freshness/coverage 8.7%, mapping 4.5%, model_calibration_or_unknown 2.0%, model_calibration 0.4%.
* **Stale / settled / in-play**: 53.0% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 46.2% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 7,035 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 3.5%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 20.8% of the time and with the model 0.6%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 576.0 points vs 1841.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.064, Gen-2 0.87, Gen-1 ledger 0.873 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 322 model 0.2255 vs Kalshi 0.2063; n 69 model 0.2933 vs Kalshi 0.1749.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 128,629 model-market comparisons (212,966 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 46,618 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-14T12:26:02.470954+00:00'], shadow board 34,963 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-14T12:26:06.214787+00:00'], Model 4 14,017 rows, 14,122 settled tickers, 4,491 tickers with an external scan.
* By model: {"gen1_ledger": 30622, "gen1_elo": 17571, "fair_v1": 17571, "gen2": 17571, "gen1_sr": 17571, "model4_fundamental": 13866, "model4_conditioned": 13857}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 32,455 | 14.5 | 9.5 | 20.2 | 15.4 | 18.7 | 13.5 | 8.2 | 11.77 | 40.4% | 21.7% |
| MW fair_v1 | 17,571 | 13.7 | 8.5 | 18.7 | 16.0 | 19.0 | 14.4 | 9.7 | 12.8 | 43.1% | 24.1% |
| MW gen1_elo | 17,571 | 13.3 | 9.1 | 20.0 | 15.2 | 18.9 | 14.3 | 9.2 | 12.32 | 42.5% | 23.6% |
| MW gen1_ledger | 14,884 | 15.4 | 10.6 | 22.0 | 14.7 | 18.4 | 12.4 | 6.3 | 10.48 | 37.2% | 18.8% |
| MW gen1_sr | 17,571 | 9.9 | 7.7 | 16.4 | 14.3 | 21.8 | 18.2 | 11.7 | 15.54 | 51.6% | 29.8% |
| MW gen2 | 17,571 | 11.7 | 7.2 | 16.4 | 14.2 | 20.4 | 17.1 | 13.0 | 15.25 | 50.4% | 30.1% |
| all families model4_conditioned | 13,857 | 21.7 | 20.1 | 35.5 | 16.5 | 4.3 | 1.1 | 0.9 | 5.81 | 6.3% | 2.0% |
| all families model4_fundamental | 13,866 | 16.7 | 13.4 | 35.8 | 19.7 | 10.6 | 2.6 | 1.1 | 7.6 | 14.4% | 3.7% |

Configurable thresholds (primary): >=5pp 76.0%, >=10pp 55.8%, >=15pp 40.4%, >=20pp 29.9%, >=25pp 21.7%, >=30pp 15.8%, >=40pp 8.2%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.42pp; >=10pp 45.2%, >=25pp 17.3%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,319 | 30.2 | 14.7 | 25.0 | 17.7 | 10.4 | 1.1 | 0.8 | 5.84 | 12.4% | 2.0% |
| CHALLENGER | 3,069 | 15.5 | 10.0 | 20.2 | 15.8 | 14.9 | 11.9 | 11.7 | 11.53 | 38.5% | 23.6% |
| ITF_MEN | 4,922 | 11.3 | 8.4 | 18.0 | 15.0 | 19.4 | 15.7 | 12.2 | 13.99 | 47.3% | 27.9% |
| ITF_WOMEN | 6,783 | 10.3 | 6.5 | 16.1 | 16.2 | 22.0 | 18.5 | 10.4 | 15.37 | 50.8% | 28.9% |
| WTA | 908 | 21.9 | 10.8 | 24.8 | 15.8 | 19.8 | 5.7 | 1.2 | 8.06 | 26.8% | 6.9% |
| WTA125 | 570 | 12.8 | 7.7 | 22.6 | 21.1 | 19.8 | 14.0 | 1.9 | 11.31 | 35.8% | 16.0% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,319 | 24.3 | 14.5 | 24.8 | 19.0 | 14.6 | 1.9 | 1.0 | 6.76 | 17.4% | 2.9% |
| CHALLENGER | 3,069 | 15.1 | 7.6 | 19.4 | 13.5 | 18.2 | 14.0 | 12.3 | 12.73 | 44.5% | 26.4% |
| ITF_MEN | 4,922 | 9.8 | 7.1 | 16.1 | 14.2 | 20.0 | 18.3 | 14.5 | 16.08 | 52.8% | 32.8% |
| ITF_WOMEN | 6,783 | 8.8 | 5.9 | 13.1 | 13.2 | 21.9 | 20.6 | 16.5 | 18.76 | 59.1% | 37.1% |
| WTA | 908 | 18.2 | 8.0 | 18.9 | 16.1 | 22.7 | 14.9 | 1.2 | 11.74 | 38.8% | 16.1% |
| WTA125 | 570 | 6.0 | 4.2 | 17.7 | 17.7 | 25.6 | 19.1 | 9.7 | 17.24 | 54.4% | 28.8% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,319 | 27.5 | 14.6 | 28.8 | 15.4 | 10.3 | 2.5 | 0.9 | 6.03 | 13.7% | 3.4% |
| CHALLENGER | 3,069 | 14.8 | 10.2 | 20.5 | 15.2 | 15.7 | 11.8 | 11.8 | 11.1 | 39.3% | 23.6% |
| ITF_MEN | 4,922 | 10.3 | 8.3 | 18.8 | 14.1 | 20.0 | 16.1 | 12.4 | 14.25 | 48.5% | 28.5% |
| ITF_WOMEN | 6,783 | 9.9 | 6.9 | 16.5 | 15.9 | 22.7 | 18.8 | 9.3 | 15.39 | 50.8% | 28.1% |
| WTA | 908 | 22.2 | 15.5 | 32.8 | 16.0 | 10.5 | 2.2 | 0.8 | 6.15 | 13.4% | 3.0% |
| WTA125 | 570 | 22.6 | 12.1 | 29.1 | 15.3 | 14.2 | 6.3 | 0.3 | 7.54 | 20.9% | 6.7% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 716 | 30.9 | 22.8 | 35.8 | 8.9 | 1.3 | 0.4 | 0.0 | 4.71 | 1.7% | 0.4% |
| CHALLENGER | 2,099 | 22.0 | 15.3 | 27.6 | 15.0 | 13.1 | 5.0 | 2.0 | 7.01 | 20.1% | 7.0% |
| DOUBLES | 982 | 5.0 | 3.7 | 11.5 | 10.8 | 18.5 | 24.4 | 26.1 | 25.4 | 69.0% | 50.5% |
| ITF_MEN | 4,568 | 14.7 | 8.4 | 20.8 | 15.4 | 20.7 | 12.5 | 7.4 | 11.87 | 40.6% | 19.9% |
| ITF_WOMEN | 5,041 | 11.7 | 9.3 | 19.6 | 14.7 | 22.4 | 16.6 | 5.7 | 13.04 | 44.7% | 22.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 653 | 21.3 | 15.3 | 27.3 | 17.1 | 13.6 | 4.9 | 0.5 | 7.52 | 19.0% | 5.4% |
| WTA125 | 676 | 20.6 | 13.6 | 22.6 | 18.5 | 14.3 | 8.1 | 2.2 | 8.25 | 24.7% | 10.4% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,305 | 30.2 | 14.6 | 25.2 | 17.7 | 10.3 | 1.1 | 0.8 | 5.84 | 12.3% | 1.9% |
| CHALLENGER | 2,203 | 20.0 | 12.4 | 25.4 | 18.5 | 15.3 | 5.9 | 2.5 | 8.36 | 23.7% | 8.3% |
| ITF_MEN | 3,558 | 13.9 | 10.4 | 21.4 | 16.7 | 19.6 | 12.5 | 5.5 | 11.12 | 37.5% | 18.0% |
| ITF_WOMEN | 4,965 | 12.6 | 8.1 | 18.5 | 18.6 | 23.6 | 15.0 | 3.7 | 12.8 | 42.3% | 18.7% |
| WTA | 892 | 22.1 | 10.1 | 25.2 | 15.9 | 19.8 | 5.6 | 1.2 | 8.11 | 26.7% | 6.8% |
| WTA125 | 547 | 13.2 | 7.5 | 22.1 | 21.4 | 20.5 | 13.9 | 1.5 | 11.31 | 35.8% | 15.4% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,305 | 24.1 | 14.6 | 24.9 | 19.0 | 14.6 | 1.8 | 1.0 | 6.81 | 17.4% | 2.8% |
| CHALLENGER | 2,203 | 19.2 | 9.6 | 24.1 | 16.3 | 18.5 | 9.7 | 2.6 | 9.16 | 30.8% | 12.3% |
| ITF_MEN | 3,559 | 11.6 | 8.5 | 18.4 | 16.0 | 21.9 | 15.8 | 7.8 | 13.5 | 45.5% | 23.5% |
| ITF_WOMEN | 4,965 | 10.2 | 6.9 | 14.8 | 14.3 | 24.4 | 19.4 | 10.0 | 16.33 | 53.8% | 29.4% |
| WTA | 892 | 18.1 | 7.8 | 18.9 | 16.4 | 22.6 | 14.9 | 1.2 | 12.07 | 38.8% | 16.1% |
| WTA125 | 547 | 5.8 | 4.4 | 17.7 | 18.1 | 25.4 | 19.7 | 8.8 | 16.84 | 53.9% | 28.5% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 696 | 30.9 | 23.0 | 36.1 | 9.1 | 0.6 | 0.4 | 0.0 | 4.69 | 1.0% | 0.4% |
| CHALLENGER | 1,812 | 23.7 | 16.6 | 29.8 | 14.8 | 12.2 | 2.3 | 0.6 | 6.37 | 15.1% | 2.9% |
| DOUBLES | 911 | 5.0 | 3.7 | 11.9 | 10.8 | 18.7 | 24.1 | 25.8 | 24.89 | 68.6% | 50.0% |
| ITF_MEN | 3,760 | 16.2 | 9.2 | 22.7 | 16.3 | 20.6 | 10.5 | 4.4 | 10.55 | 35.6% | 14.9% |
| ITF_WOMEN | 4,135 | 12.9 | 10.0 | 21.4 | 15.6 | 22.6 | 15.0 | 2.6 | 11.64 | 40.2% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 619 | 21.8 | 16.0 | 27.5 | 17.1 | 13.9 | 3.7 | 0.0 | 7.21 | 17.6% | 3.7% |
| WTA125 | 573 | 22.5 | 15.0 | 24.1 | 20.2 | 12.7 | 5.1 | 0.3 | 7.35 | 18.1% | 5.4% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 982 | 5.0 | 3.7 | 11.5 | 10.8 | 18.5 | 24.4 | 26.1 | 25.4 | 69.0% | 50.5% |
| singles | 13,902 | 16.2 | 11.1 | 22.7 | 15.0 | 18.4 | 11.6 | 5.0 | 9.99 | 35.0% | 16.6% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 4,100 | 13.4 | 8.9 | 19.8 | 16.1 | 17.7 | 14.2 | 9.8 | 12.53 | 41.8% | 24.1% |
| Grass | 162 | 10.5 | 13.6 | 16.1 | 15.4 | 21.6 | 17.3 | 5.6 | 13.44 | 44.4% | 22.8% |
| Hard | 11,525 | 14.1 | 8.5 | 18.7 | 15.6 | 19.3 | 14.2 | 9.6 | 12.78 | 43.1% | 23.8% |
| UNKNOWN | 1,784 | 11.9 | 7.5 | 16.6 | 18.3 | 19.3 | 16.0 | 10.4 | 13.57 | 45.7% | 26.4% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,278 | 19.8 | 10.7 | 21.1 | 16.9 | 15.7 | 8.8 | 7.1 | 9.52 | 31.5% | 15.8% |
| B | 2,314 | 14.6 | 9.1 | 20.0 | 16.8 | 17.9 | 12.1 | 9.6 | 11.47 | 39.5% | 21.6% |
| C | 2,527 | 13.1 | 9.5 | 19.9 | 15.0 | 19.0 | 14.4 | 9.2 | 12.57 | 42.7% | 23.6% |
| D | 3,085 | 11.0 | 8.1 | 18.1 | 16.1 | 22.1 | 15.1 | 9.5 | 13.75 | 46.7% | 24.6% |
| F | 4,367 | 8.0 | 5.3 | 15.0 | 15.1 | 21.2 | 22.1 | 13.3 | 17.94 | 56.6% | 35.4% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,318 | 22.6 | 15.8 | 28.9 | 15.2 | 11.4 | 4.5 | 1.6 | 6.72 | 17.5% | 6.1% |
| B | 2,255 | 14.9 | 10.0 | 24.0 | 16.4 | 19.4 | 11.0 | 4.2 | 10.19 | 34.6% | 15.2% |
| C | 2,933 | 12.2 | 7.6 | 18.3 | 14.2 | 20.2 | 15.7 | 11.7 | 13.75 | 47.6% | 27.4% |
| D | 2,253 | 14.0 | 9.8 | 20.8 | 13.7 | 21.4 | 13.8 | 6.5 | 11.85 | 41.7% | 20.3% |
| F | 3,125 | 10.1 | 7.5 | 15.1 | 13.9 | 23.8 | 20.4 | 9.3 | 16.45 | 53.5% | 29.7% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 5,866 | 18.3 | 9.8 | 20.3 | 16.7 | 16.0 | 9.8 | 9.2 | 10.46 | 35.0% | 19.0% |
| LIMITED | 4,179 | 15.2 | 10.2 | 20.9 | 15.8 | 18.5 | 12.6 | 6.7 | 11.07 | 37.8% | 19.3% |
| POOR | 7,526 | 9.2 | 6.6 | 16.3 | 15.6 | 21.6 | 19.1 | 11.7 | 15.9 | 52.3% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,994 | 31.4 | 24.3 | 36.4 | 5.4 | 1.8 | 0.7 | 0.1 | 4.49 | 2.5% | 0.7% |
| GAME_SPREAD | 2,859 | 25.7 | 15.9 | 36.8 | 16.8 | 4.2 | 0.4 | 0.2 | 6.0 | 4.8% | 0.6% |
| MATCH_WINNER | 14,884 | 15.4 | 10.6 | 22.0 | 14.7 | 18.4 | 12.4 | 6.3 | 10.48 | 37.2% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 5,477 | 33.3 | 19.5 | 31.0 | 9.7 | 5.1 | 1.1 | 0.2 | 4.74 | 6.5% | 1.4% |
| TOTAL_GAMES | 4,384 | 6.7 | 9.1 | 39.0 | 29.7 | 10.4 | 2.7 | 2.4 | 9.47 | 15.5% | 5.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,869 | 25.6 | 38.1 | 31.6 | 0.3 | 3.9 | 0.4 | 0.1 | 4.3 | 4.5% | 0.5% |
| GAME_SPREAD | 3,473 | 45.1 | 16.4 | 29.0 | 7.3 | 1.1 | 0.7 | 0.4 | 3.58 | 2.2% | 1.1% |
| TOTAL_GAMES | 5,515 | 3.4 | 6.5 | 42.9 | 36.7 | 6.7 | 1.9 | 1.9 | 9.76 | 10.5% | 3.9% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,869 | 26.3 | 18.6 | 37.2 | 9.2 | 6.3 | 2.1 | 0.3 | 5.51 | 8.7% | 2.4% |
| GAME_SPREAD | 3,473 | 19.2 | 13.4 | 30.4 | 21.1 | 13.0 | 2.3 | 0.7 | 7.82 | 16.0% | 3.0% |
| TOTAL_GAMES | 5,524 | 6.6 | 8.9 | 37.9 | 28.2 | 13.0 | 3.2 | 2.1 | 9.66 | 18.3% | 5.3% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 17,571 | 43.1% | 24.1% | 12.8 | 33.8% | 14.3% | 10.45 |
| gen1_elo | 17,571 | 42.5% | 23.6% | 12.32 | 32.8% | 14.0% | 9.95 |
| gen1_sr | 17,571 | 51.6% | 29.8% | 15.54 | 43.3% | 20.0% | 12.89 |
| gen2 | 17,571 | 50.4% | 30.1% | 15.25 | 43.3% | 21.6% | 12.79 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 9,543 | 16.5 | 10.5 | 21.6 | 17.5 | 19.4 | 11.2 | 3.3 | 10.38 | 33.9% | 14.5% |
| STALE | 8,028 | 10.3 | 6.2 | 15.2 | 14.3 | 18.4 | 18.3 | 17.3 | 17.15 | 54.0% | 35.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 8,352 | 17.3 | 11.5 | 23.7 | 14.7 | 16.9 | 11.1 | 4.9 | 9.4 | 32.9% | 16.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 32,455 | 8352 | 13015 | 11088 | 24.1 | 140.4 | 1400.4 |
| ge_15pp | 13,112 | 2744 | 4523 | 5845 | 26.3 | 440.0 | 1380.4 |
| ge_25pp | 7,035 | 1335 | 1973 | 3727 | 33.3 | 574.5 | 1380.4 |
| lt_10pp | 14,341 | 4384 | 6273 | 3684 | 22.4 | 47.9 | 1341.5 |

Current slate `SL-20261014T123548Z-f59cd6e5`: 425 priced rows, quote age at build {'median': 10.2, 'max': 10.2}, freshness {'AGING': 425}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 8 | 0.0 | 0.0 | 37.5 | 0.0 | 37.5 | 25.0 | 0.0 | 20.45 | 62.5% | 25.0% |
| EXTERNAL_LONE_OUTLIER | 11 | 72.7 | 27.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,419 | 21.0 | 10.7 | 22.8 | 18.8 | 19.3 | 6.7 | 0.6 | 8.88 | 26.6% | 7.3% |
| KALSHI_LONE_OUTLIER | 5 | 20.0 | 0.0 | 60.0 | 0.0 | 20.0 | 0.0 | 0.0 | 5.14 | 20.0% | 0.0% |
| MARKETS_AGREE | 242 | 71.9 | 28.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.03 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 444 | 0.0 | 3.8 | 34.5 | 30.4 | 22.3 | 8.3 | 0.7 | 11.62 | 31.3% | 9.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 17,571 | 2129 (12.1%) | 20.8% | 0.6% | {"EXTERNAL_STALE": 1419, "AGREES_WITH_KALSHI": 444, "ALL_AGREE": 242, "EXTERNAL_OUTLIER": 11, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 5, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 7,569 | 523 (6.9%) | 26.6% | 1.1% | {"EXTERNAL_STALE": 378, "AGREES_WITH_KALSHI": 139, "SUPPORTS_MODEL_DIRECTION": 5, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp | 4,238 | 146 (3.5%) | 27.4% | 1.4% | {"EXTERNAL_STALE": 104, "AGREES_WITH_KALSHI": 40, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_ge_25pp_pregame_clean | 1,921 | 138 (7.2%) | 27.5% | 1.5% | {"EXTERNAL_STALE": 98, "AGREES_WITH_KALSHI": 38, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_lt_10pp | 7,188 | 1204 (16.8%) | 14.1% | 0.5% | {"EXTERNAL_STALE": 774, "ALL_AGREE": 242, "AGREES_WITH_KALSHI": 170, "EXTERNAL_OUTLIER": 11, "AGREES_WITH_MODEL": 4, "SUPPORTS_MODEL_DIRECTION": 2, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,455 | 11.6 | 8.1 | 20.0 | 14.9 | 21.4 | 14.3 | 9.8 | 13.28 | 45.5% | 24.1% |
| 4-10x | 2,326 | 11.9 | 8.8 | 19.4 | 15.7 | 19.8 | 15.4 | 9.0 | 13.02 | 44.2% | 24.4% |
| <2x | 9,269 | 15.7 | 9.2 | 18.9 | 16.9 | 17.5 | 12.8 | 9.1 | 11.81 | 39.3% | 21.8% |
| >=10x | 2,521 | 10.8 | 6.6 | 15.7 | 14.4 | 20.3 | 19.9 | 12.4 | 16.17 | 52.6% | 32.3% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 4,588 | 14.1 | 8.2 | 19.5 | 16.0 | 19.3 | 12.6 | 10.3 | 12.53 | 42.2% | 22.9% |
| 300-1000 | 4,042 | 11.9 | 8.6 | 17.7 | 16.2 | 21.1 | 15.7 | 8.8 | 13.52 | 45.6% | 24.5% |
| <300 | 4,962 | 8.7 | 6.2 | 15.8 | 14.9 | 21.0 | 20.6 | 12.8 | 16.86 | 54.4% | 33.5% |
| >=3000 | 3,979 | 21.2 | 11.8 | 22.6 | 17.1 | 13.9 | 7.5 | 5.9 | 8.49 | 27.3% | 13.5% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 570 | 0.5362 | 0.4051 | 0.486 | +0.050 | -0.081 | 0.0004 ± 0.0061 |
| ratio 4-10x | 381 | 0.5867 | 0.4466 | 0.5197 | +0.067 | -0.073 | 0.0048 ± 0.0081 |
| ratio <2x | 1370 | 0.5382 | 0.4164 | 0.4599 | +0.078 | -0.043 | 0.0101 ± 0.0038 |
| ratio >=10x | 435 | 0.5484 | 0.3814 | 0.4299 | +0.118 | -0.048 | 0.0151 ± 0.0085 |
| thinner_sample 1000-3000 | 765 | 0.5445 | 0.4198 | 0.4758 | +0.069 | -0.056 | 0.0039 ± 0.0052 |
| thinner_sample 300-1000 | 683 | 0.5608 | 0.4228 | 0.4846 | +0.076 | -0.062 | 0.0039 ± 0.0059 |
| thinner_sample <300 | 825 | 0.545 | 0.3848 | 0.4521 | +0.093 | -0.067 | 0.0126 ± 0.006 |
| thinner_sample >=3000 | 483 | 0.5297 | 0.4351 | 0.4638 | +0.066 | -0.029 | 0.0133 ± 0.0053 |
| data_status ADEQUATE | 788 | 0.5328 | 0.4291 | 0.4619 | +0.071 | -0.033 | 0.0077 ± 0.0044 |
| data_status LIMITED | 720 | 0.553 | 0.4243 | 0.4889 | +0.064 | -0.065 | 0.0032 ± 0.0054 |
| data_status POOR | 1248 | 0.5505 | 0.3957 | 0.4615 | +0.089 | -0.066 | 0.0113 ± 0.0048 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 422 | 0.1944 | 0.1957 | -0.0013 ± 0.0008 | 0.5672 | 0.57 | 0.492 | 0.477 | 0.5237 | -0.049 ± 0.0225 | -0.01 (3) |
| 3-5 | 279 | 0.1897 | 0.1906 | -0.0009 ± 0.0021 | 0.5591 | 0.56 | 0.5103 | 0.4704 | 0.4982 | -0.064 ± 0.0267 | 0.02 (1) |
| 5-10 | 578 | 0.1953 | 0.197 | -0.0017 ± 0.0028 | 0.5747 | 0.5775 | 0.5135 | 0.4391 | 0.4792 | -0.077 ± 0.0192 | -0.0125 (4) |
| 10-15 | 490 | 0.2112 | 0.2041 | +0.0071 ± 0.0051 | 0.6098 | 0.5893 | 0.5205 | 0.397 | 0.4286 | -0.084 ± 0.0203 | -0.0633 (3) |
| 15-25 | 596 | 0.2269 | 0.2161 | +0.0107 ± 0.0074 | 0.6486 | 0.6189 | 0.5748 | 0.3801 | 0.4513 | -0.071 ± 0.019 | -0.0133 (6) |
| 25-40 | 322 | 0.2255 | 0.2063 | +0.0193 ± 0.0152 | 0.6425 | 0.5927 | 0.6488 | 0.3394 | 0.4627 | -0.070 ± 0.023 | -0.01 (1) |
| 40+ | 69 | 0.2933 | 0.1749 | +0.1184 ± 0.0449 | 0.7955 | 0.5246 | 0.7498 | 0.3022 | 0.3913 | -0.123 ± 0.0441 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1986 | 0.1783 | 0.1794 | -0.0011 ± 0.0003 | 0.531 | 0.5322 | 0.4802 | 0.4652 | 0.5005 | -0.022 ± 0.0096 | -0.0188 (8) |
| 3-5 | 1250 | 0.1941 | 0.1927 | +0.0014 ± 0.001 | 0.569 | 0.5616 | 0.4814 | 0.4418 | 0.4408 | -0.060 ± 0.0127 | 0.02 (1) |
| 5-10 | 2726 | 0.1916 | 0.1904 | +0.0012 ± 0.0013 | 0.5646 | 0.5596 | 0.4866 | 0.4127 | 0.438 | -0.041 ± 0.0085 | -0.0082 (17) |
| 10-15 | 2359 | 0.2013 | 0.1832 | +0.0181 ± 0.0022 | 0.5886 | 0.5382 | 0.4792 | 0.3548 | 0.3446 | -0.075 ± 0.0088 | -0.0475 (4) |
| 15-25 | 2809 | 0.206 | 0.1715 | +0.0346 ± 0.0031 | 0.6043 | 0.5063 | 0.4996 | 0.3038 | 0.3154 | -0.062 ± 0.0078 | -0.0048 (29) |
| 25-40 | 2228 | 0.2196 | 0.1243 | +0.0953 ± 0.0047 | 0.6325 | 0.3839 | 0.5286 | 0.2149 | 0.2235 | -0.063 ± 0.0072 | -0.01 (1) |
| 40+ | 1523 | 0.3734 | 0.0434 | +0.3300 ± 0.006 | 0.9726 | 0.172 | 0.6249 | 0.1061 | 0.0578 | -0.086 ± 0.005 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 321 | 0.1957 | 0.196 | -0.0003 ± 0.0009 | 0.5724 | 0.5732 | 0.5011 | 0.486 | 0.5016 | -0.087 ± 0.0261 | -0.01 (1) |
| 3-5 | 217 | 0.2112 | 0.21 | +0.0012 ± 0.0025 | 0.6046 | 0.6033 | 0.518 | 0.478 | 0.4793 | -0.085 ± 0.0328 | 0.02 (1) |
| 5-10 | 502 | 0.1973 | 0.1971 | +0.0002 ± 0.003 | 0.5766 | 0.5772 | 0.5561 | 0.4811 | 0.5179 | -0.067 ± 0.0206 | -0.01 (4) |
| 10-15 | 451 | 0.217 | 0.2066 | +0.0104 ± 0.0054 | 0.621 | 0.5986 | 0.5744 | 0.45 | 0.4745 | -0.101 ± 0.0222 | -0.05 (4) |
| 15-25 | 665 | 0.2252 | 0.2082 | +0.0169 ± 0.007 | 0.6415 | 0.599 | 0.5901 | 0.3928 | 0.4526 | -0.082 ± 0.018 | -0.01 (5) |
| 25-40 | 434 | 0.2676 | 0.1989 | +0.0688 ± 0.0135 | 0.7493 | 0.5775 | 0.6654 | 0.3509 | 0.4009 | -0.119 ± 0.0213 | -0.025 (2) |
| 40+ | 166 | 0.3515 | 0.1883 | +0.1632 ± 0.0328 | 0.9793 | 0.5516 | 0.7465 | 0.2663 | 0.3494 | -0.058 ± 0.0325 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1701 | 0.1817 | 0.182 | -0.0004 ± 0.0004 | 0.5383 | 0.539 | 0.4963 | 0.4817 | 0.5056 | -0.033 ± 0.0107 | -0.0217 (6) |
| 3-5 | 1085 | 0.1946 | 0.1938 | +0.0008 ± 0.0011 | 0.5644 | 0.5627 | 0.5175 | 0.4776 | 0.4866 | -0.042 ± 0.0136 | 0.02 (1) |
| 5-10 | 2376 | 0.19 | 0.1879 | +0.0021 ± 0.0013 | 0.5617 | 0.5539 | 0.5156 | 0.4419 | 0.4663 | -0.038 ± 0.0091 | -0.01 (5) |
| 10-15 | 2074 | 0.197 | 0.1818 | +0.0152 ± 0.0023 | 0.5796 | 0.5334 | 0.523 | 0.3986 | 0.4031 | -0.066 ± 0.0095 | -0.02 (14) |
| 15-25 | 2996 | 0.2153 | 0.176 | +0.0393 ± 0.003 | 0.6266 | 0.5195 | 0.5342 | 0.338 | 0.3391 | -0.075 ± 0.0077 | -0.0026 (27) |
| 25-40 | 2606 | 0.248 | 0.1384 | +0.1096 ± 0.0046 | 0.7041 | 0.4211 | 0.5623 | 0.2463 | 0.2329 | -0.083 ± 0.0073 | -0.015 (6) |
| 40+ | 2043 | 0.4008 | 0.0691 | +0.3317 ± 0.0067 | 1.0521 | 0.2397 | 0.6665 | 0.1288 | 0.1028 | -0.067 ± 0.0057 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 416 | 0.1953 | 0.198 | -0.0027 ± 0.0008 | 0.5708 | 0.5777 | 0.4928 | 0.4776 | 0.5553 | -0.001 ± 0.0221 | -0.0133 (6) |
| 3-5 | 300 | 0.184 | 0.1823 | +0.0017 ± 0.002 | 0.5429 | 0.5387 | 0.493 | 0.4536 | 0.4533 | -0.113 ± 0.0259 | -0.01 (1) |
| 5-10 | 616 | 0.1989 | 0.1966 | +0.0022 ± 0.0027 | 0.584 | 0.5758 | 0.5046 | 0.4309 | 0.4497 | -0.088 ± 0.0184 | -0.01 (4) |
| 10-15 | 470 | 0.2104 | 0.2117 | -0.0013 ± 0.0052 | 0.6088 | 0.6069 | 0.538 | 0.4153 | 0.4851 | -0.058 ± 0.021 | -0.044 (5) |
| 15-25 | 557 | 0.2308 | 0.2113 | +0.0195 ± 0.0076 | 0.6609 | 0.6073 | 0.5809 | 0.3877 | 0.4345 | -0.095 ± 0.0193 | -0.03 (1) |
| 25-40 | 335 | 0.2123 | 0.2106 | +0.0017 ± 0.0148 | 0.613 | 0.6034 | 0.6546 | 0.3432 | 0.4925 | -0.049 ± 0.0222 | 0.0 (1) |
| 40+ | 62 | 0.3217 | 0.1756 | +0.1460 ± 0.0486 | 0.8627 | 0.5269 | 0.7561 | 0.3015 | 0.371 | -0.136 ± 0.049 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1892 | 0.1869 | 0.1882 | -0.0013 ± 0.0004 | 0.5506 | 0.5532 | 0.4863 | 0.4711 | 0.5085 | -0.016 ± 0.01 | -0.0183 (23) |
| 3-5 | 1319 | 0.1848 | 0.1827 | +0.0021 ± 0.0009 | 0.5458 | 0.5407 | 0.4768 | 0.4375 | 0.4314 | -0.070 ± 0.0122 | -0.0243 (7) |
| 5-10 | 2914 | 0.1919 | 0.1866 | +0.0053 ± 0.0012 | 0.567 | 0.5497 | 0.4804 | 0.4067 | 0.4063 | -0.062 ± 0.0081 | -0.01 (18) |
| 10-15 | 2219 | 0.1965 | 0.1824 | +0.0141 ± 0.0022 | 0.5778 | 0.5344 | 0.4948 | 0.3717 | 0.3763 | -0.064 ± 0.009 | -0.03 (9) |
| 15-25 | 2879 | 0.2083 | 0.1712 | +0.0370 ± 0.003 | 0.6112 | 0.5068 | 0.5032 | 0.3079 | 0.313 | -0.066 ± 0.0078 | -0.03 (2) |
| 25-40 | 2204 | 0.2141 | 0.1215 | +0.0926 ± 0.0047 | 0.62 | 0.3754 | 0.5241 | 0.2078 | 0.2232 | -0.059 ± 0.007 | 0.0 (1) |
| 40+ | 1454 | 0.3874 | 0.0451 | +0.3423 ± 0.0063 | 1.012 | 0.177 | 0.6329 | 0.1081 | 0.0557 | -0.089 ± 0.0053 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 735 | 0.1989 | 0.1995 | -0.0006 ± 0.0006 | 0.579 | 0.5803 | 0.506 | 0.491 | 0.5075 | -0.037 ± 0.0164 | -0.0226 (46) |
| 3-5 | 527 | 0.1949 | 0.1943 | +0.0006 ± 0.0015 | 0.5687 | 0.5656 | 0.4796 | 0.4398 | 0.4497 | -0.047 ± 0.0193 | -0.0058 (33) |
| 5-10 | 1108 | 0.1932 | 0.1879 | +0.0054 ± 0.002 | 0.5716 | 0.5568 | 0.4839 | 0.4105 | 0.4116 | -0.062 ± 0.0133 | -0.0049 (73) |
| 10-15 | 702 | 0.2068 | 0.1967 | +0.0101 ± 0.0042 | 0.6022 | 0.5752 | 0.4994 | 0.3766 | 0.396 | -0.049 ± 0.0168 | 0.0014 (64) |
| 15-25 | 943 | 0.2305 | 0.2116 | +0.0189 ± 0.0059 | 0.6588 | 0.6092 | 0.5598 | 0.3655 | 0.4146 | -0.047 ± 0.015 | -0.0216 (58) |
| 25-40 | 533 | 0.2544 | 0.1922 | +0.0622 ± 0.0118 | 0.7164 | 0.5602 | 0.6439 | 0.3309 | 0.3865 | -0.088 ± 0.0177 | -0.0216 (25) |
| 40+ | 184 | 0.3686 | 0.1934 | +0.1752 ± 0.033 | 1.0717 | 0.568 | 0.7946 | 0.3029 | 0.3913 | -0.075 ± 0.0297 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2219 | 0.1899 | 0.1901 | -0.0002 ± 0.0003 | 0.5555 | 0.5549 | 0.5039 | 0.4886 | 0.5025 | -0.031 ± 0.0092 | -0.0155 (82) |
| 3-5 | 1521 | 0.1884 | 0.1859 | +0.0025 ± 0.0009 | 0.5515 | 0.5453 | 0.4867 | 0.447 | 0.4359 | -0.058 ± 0.0111 | -0.0148 (63) |
| 5-10 | 3122 | 0.1908 | 0.1832 | +0.0076 ± 0.0012 | 0.5654 | 0.544 | 0.478 | 0.4044 | 0.3933 | -0.064 ± 0.0078 | -0.0087 (125) |
| 10-15 | 2098 | 0.2012 | 0.1882 | +0.0131 ± 0.0024 | 0.5894 | 0.5545 | 0.5069 | 0.3839 | 0.3923 | -0.050 ± 0.0094 | -0.0053 (105) |
| 15-25 | 2642 | 0.229 | 0.1987 | +0.0302 ± 0.0034 | 0.6614 | 0.5772 | 0.5534 | 0.3586 | 0.3796 | -0.057 ± 0.0087 | -0.0255 (106) |
| 25-40 | 1781 | 0.2545 | 0.167 | +0.0874 ± 0.0061 | 0.7216 | 0.4945 | 0.6059 | 0.2911 | 0.3122 | -0.079 ± 0.0094 | -0.0206 (47) |
| 40+ | 869 | 0.3866 | 0.1279 | +0.2586 ± 0.013 | 1.0991 | 0.3925 | 0.7098 | 0.2012 | 0.214 | -0.073 ± 0.0115 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2756 | 1.064 ± 0.053 | 1.184 | 0.1694 | 0.1706 | 0.2102 | 0.2021 |
| gen2 | 2756 | 0.87 ± 0.048 | 1.123 | 0.1797 | 0.1706 | 0.2285 | 0.202 |
| gen1_elo | 2756 | 1.04 ± 0.052 | 1.173 | 0.1738 | 0.171 | 0.2095 | 0.202 |
| gen1_sr | 2756 | 1.072 ± 0.063 | 1.198 | 0.1386 | 0.1725 | 0.2246 | 0.2018 |
| gen1_ledger | 4732 | 0.873 ± 0.036 | 1.087 | 0.1763 | 0.1867 | 0.2174 | 0.1971 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 13,112)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,344 | 25.5% |
| STALE_QUOTE | market_freshness | 2,556 | 19.5% |
| BOOK_QUALITY | execution | 2,402 | 18.3% |
| POOR_DATA | data | 1,471 | 11.2% |
| LIMITED_DATA | data | 989 | 7.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 703 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 642 | 4.9% |
| IDENTITY_AMBIGUOUS | mapping | 511 | 3.9% |
| IN_PLAY_QUOTE | market_freshness/coverage | 369 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 125 | 0.9% |

Cause class: coverage 25.5%, market_freshness 19.5%, data 18.8%, execution 18.3%, market_freshness/coverage 8.2%, model_calibration_or_unknown 4.9%, mapping 3.9%, model_calibration 0.9%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.4%, START_UNVERIFIABLE 95.9%, LOW_DATA_QUALITY 68.6%, THIN_PLAYER_HISTORY 57.4%, STALE_PLAYER_DATA 55.2%, STALE_KALSHI_QUOTE 44.6%, MODEL_INTERNAL_DISAGREEMENT 38.6%, ASYMMETRIC_SAMPLE_SIZE 31.4%, WIDE_SPREAD 23.8%, MODEL_HIGH_UNCERTAINTY 16.6%, PLAYER_IDENTITY_RISK 13.2%, LEVEL_TRANSFER_RISK 8.7%, EVENT_MAPPING_RISK 7.8%, LOW_DISPLAYED_LIQUIDITY 7.4%, MODEL_CALIBRATION_OUTLIER 3.5%, EXTERNAL_MARKET_REJECTION 1.6%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 27.9%, POST_SETTLEMENT_OBSERVATION 25.5%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 7,035)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,642 | 37.6% |
| BOOK_QUALITY | execution | 1,250 | 17.8% |
| STALE_QUOTE | market_freshness | 1,159 | 16.5% |
| POOR_DATA | data | 595 | 8.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 381 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 318 | 4.5% |
| LIMITED_DATA | data | 291 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 228 | 3.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 142 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 29 | 0.4% |

Cause class: coverage 37.6%, execution 17.8%, market_freshness 16.5%, data 12.6%, market_freshness/coverage 8.7%, mapping 4.5%, model_calibration_or_unknown 2.0%, model_calibration 0.4%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.1%, START_UNVERIFIABLE 98.2%, LOW_DATA_QUALITY 72.4%, THIN_PLAYER_HISTORY 59.6%, STALE_KALSHI_QUOTE 53.0%, STALE_PLAYER_DATA 50.2%, MODEL_INTERNAL_DISAGREEMENT 39.7%, ASYMMETRIC_SAMPLE_SIZE 33.2%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 17.3%, PLAYER_IDENTITY_RISK 17.0%, EVENT_MAPPING_RISK 9.7%, LOW_DISPLAYED_LIQUIDITY 7.6%, LEVEL_TRANSFER_RISK 7.6%, MODEL_CALIBRATION_OUTLIER 4.5%, EXTERNAL_MARKET_REJECTION 0.8%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 40.3%, POST_SETTLEMENT_OBSERVATION 37.6%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 5665, "IDENTITY_AMBIGUOUS": 1370}; ticker orientation: {"VERIFIED": 7035}.

Checks: discipline:AMBIGUOUS 496, discipline:PASS 6539, identity_confidence:AMBIGUOUS 1196, identity_confidence:PASS 5839, level_mapping:NA 508, level_mapping:PASS 6527, market_pair:AMBIGUOUS 242, market_pair:NA 171, market_pair:PASS 6622, model_complement:NA 138, model_complement:PASS 6897, namesake:PASS 7035, physical_match_id:NA 2797, physical_match_id:PASS 4238, player_ids:PASS 7035, same_pair_other_event:PASS 7035, ticker_orientation:PASS 7035

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,035 | 1.4% | 1.4% | 0.4% | {"market_freshness": 20, "execution": 8, "market_freshness/coverage": 1} | 5.25 | 0.2114 / 0.2132 (249) | 16.3% | 0.5% | 5.5% | 1.7% |
| CHALLENGER | 5,168 | 16.9% | 5.9% | 12.4% | {"coverage": 531, "market_freshness": 109, "market_freshness/coverage": 105, "data": 57, "model_calibration_or_unknown": 47, "execution": 13, "mapping": 6, "model_calibration": 5} | 7.26 | 0.2171 / 0.2035 (1328) | 37.7% | 8.9% | 2.4% | 22.3% |
| DOUBLES | 982 | 50.5% | 50.0% | 7.0% | {"execution": 196, "mapping": 153, "market_freshness": 106, "market_freshness/coverage": 34, "coverage": 7} | 24.89 | 0.337 / 0.2344 (281) | 23.8% | 0.0% | 100.0% | 7.2% |
| ITF_MEN | 9,490 | 24.1% | 16.4% | 32.5% | {"coverage": 896, "execution": 486, "market_freshness": 319, "data": 313, "market_freshness/coverage": 188, "mapping": 80, "model_calibration_or_unknown": 2} | 10.88 | 0.2103 / 0.193 (2364) | 35.6% | 58.2% | 10.1% | 22.9% |
| ITF_WOMEN | 11,824 | 26.1% | 18.2% | 43.8% | {"coverage": 1191, "market_freshness": 532, "execution": 526, "data": 482, "market_freshness/coverage": 236, "mapping": 73, "model_calibration_or_unknown": 32, "model_calibration": 10} | 12.35 | 0.203 / 0.1925 (2533) | 37.8% | 58.1% | 9.8% | 23.0% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,561 | 6.3% | 5.6% | 1.4% | {"market_freshness": 36, "model_calibration_or_unknown": 22, "data": 11, "market_freshness/coverage": 10, "model_calibration": 7, "execution": 7, "coverage": 4, "mapping": 1} | 7.78 | 0.2346 / 0.2285 (273) | 26.0% | 1.4% | 1.7% | 3.2% |
| WTA125 | 1,246 | 12.9% | 10.3% | 2.3% | {"model_calibration_or_unknown": 37, "market_freshness": 35, "market_freshness/coverage": 34, "data": 23, "coverage": 12, "execution": 9, "model_calibration": 7, "mapping": 4} | 9.39 | 0.2185 / 0.2103 (418) | 22.9% | 8.2% | 4.2% | 10.1% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 5 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 6 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 7 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 151 min (STALE); no external reference |
| 8 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 9 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 10 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 11 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 12 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 13 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 14 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 15 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 16 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 17 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 18 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 19 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 20 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 21 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 22 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 23 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 24 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 25 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 26 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 27 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 28 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 29 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 30 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 31 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 32 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 33 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 547 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 34 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 36 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 37 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 38 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 39 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 40 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 41 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 42 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 43 | `KXATPCHALLENGERMATCH-26OCT13GIUSEA-SEA` | CHALLENGER | fair_v1 | 76% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 243 min (STALE); no external reference |
| 44 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 64 min (STALE); no external reference |
| 45 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 46 | `KXITFWMATCH-26OCT13MAMSTR-MAM` | ITF_WOMEN | fair_v1 | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 406 min (STALE); data LIMITED (grade C, thinner serve sample 879.0, ratio 2.64); no external reference |
| 47 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 48 | `KXITFMATCH-26OCT13VISMUE-MUE` | ITF_MEN | fair_v1 | 25% / 98% | -74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 103 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 0.0); no external reference |
| 49 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 50 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.982, "by_level_share_of_ge_25pp": {"ATP": 0.0041, "CHALLENGER": 0.1241, "DOUBLES": 0.0705, "ITF_MEN": 0.3247, "ITF_WOMEN": 0.4381, "OTHER": 0.0017, "WTA": 0.0139, "WTA125": 0.0229}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5298, "share_primary_cause_market_settled_or_in_play": 0.4622, "share_primary_cause_stale_quote_only": 0.1647}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 7035, "identity_ambiguous_share": 0.1947, "ticker_orientation": {"VERIFIED": 7035}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 4238, "with_external": 146, "coverage": 0.0345, "external_status": {"EXTERNAL_STALE": 104, "AGREES_WITH_KALSHI": 40, "SUPPORTS_MODEL_DIRECTION": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 104, "MODEL_LONE_OUTLIER": 40, "ALL_THREE_DISAGREE": 2}, "share_external_agrees_with_kalshi": 0.274, "share_external_supports_model": 0.0137}, "pregame_clean_ge_25pp": {"n": 1921, "with_external": 138, "coverage": 0.0718, "external_status": {"EXTERNAL_STALE": 98, "AGREES_WITH_KALSHI": 38, "SUPPORTS_MODEL_DIRECTION": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 98, "MODEL_LONE_OUTLIER": 38, "ALL_THREE_DISAGREE": 2}, "share_external_agrees_with_kalshi": 0.2754, "share_external_supports_model": 0.0145}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 576.0, "median_sample_ratio": 2.36, "median_min_matches": 20.0, "median_max_days_since_last": 204.0, "share_severe_asymmetry": 0.1952, "data_status": {"POOR": 3717, "LIMITED": 2038, "ADEQUATE": 1280}, "comparison_lt_10pp": {"median_thinner_serve_points": 1841.0, "median_sample_ratio": 1.68, "median_min_matches": 85.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 570, "model_minus_observed": 0.0503, "kalshi_minus_observed": -0.0809, "brier_diff_model_minus_kalshi": 0.0004}, "4-10x": {"n": 381, "model_minus_observed": 0.067, "kalshi_minus_observed": -0.0731, "brier_diff_model_minus_kalshi": 0.0048}, "<2x": {"n": 1370, "model_minus_observed": 0.0783, "kalshi_minus_observed": -0.0434, "brier_diff_model_minus_kalshi": 0.0101}, ">=10x": {"n": 435, "model_minus_observed": 0.1185, "kalshi_minus_observed": -0.0484, "brier_diff_model_minus_kalshi": 0.0151}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2756, "model": {"intercept": -0.548, "slope": 0.87, "slope_se": 0.048}, "kalshi_mid_same_rows": {"intercept": 0.231, "slope": 1.123, "slope_se": 0.055}, "mean_extremity_model": 0.1797, "mean_extremity_kalshi": 0.1706, "model_brier": 0.2285, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0265, "brier_diff_se": 0.0036, "model_logloss": 0.6527, "kalshi_logloss": 0.5861}, "fair_v1": {"n": 2756, "model": {"intercept": -0.379, "slope": 1.064, "slope_se": 0.053}, "kalshi_mid_same_rows": {"intercept": 0.341, "slope": 1.184, "slope_se": 0.056}, "mean_extremity_model": 0.1694, "mean_extremity_kalshi": 0.1706, "model_brier": 0.2102, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": 0.0082, "brier_diff_se": 0.0029, "model_logloss": 0.6077, "kalshi_logloss": 0.5861}, "gen1_elo": {"n": 2756, "model": {"intercept": -0.357, "slope": 1.04, "slope_se": 0.052}, "kalshi_mid_same_rows": {"intercept": 0.344, "slope": 1.173, "slope_se": 0.056}, "mean_extremity_model": 0.1738, "mean_extremity_kalshi": 0.171, "model_brier": 0.2095, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0075, "brier_diff_se": 0.0029, "model_logloss": 0.6071, "kalshi_logloss": 0.586}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2412, "share_ge_15": 0.4308, "median_abs_gap": 12.8, "n": 17571}, "gen1_elo": {"share_ge_25": 0.2358, "share_ge_15": 0.4247, "median_abs_gap": 12.32, "n": 17571}, "gen1_sr": {"share_ge_25": 0.2984, "share_ge_15": 0.5164, "median_abs_gap": 15.54, "n": 17571}, "gen2": {"share_ge_25": 0.301, "share_ge_15": 0.5045, "median_abs_gap": 15.25, "n": 17571}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1426, "share_ge_15": 0.3378, "median_abs_gap": 10.45, "n": 13470}, "gen1_elo": {"share_ge_25": 0.1404, "share_ge_15": 0.328, "median_abs_gap": 9.95, "n": 13469}, "gen1_sr": {"share_ge_25": 0.2002, "share_ge_15": 0.4329, "median_abs_gap": 12.89, "n": 13470}, "gen2": {"share_ge_25": 0.2158, "share_ge_15": 0.4334, "median_abs_gap": 12.79, "n": 13471}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.25, "share_ge_25_all": 0.0143, "share_ge_25_pregame_clean": 0.014}, "WTA": {"median_abs_gap_pregame_clean": 7.78, "share_ge_25_all": 0.0628, "share_ge_25_pregame_clean": 0.0556}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2399, "share_within_10pp_all": 0.4419, "share_within_10pp_pregame_clean": 0.5006, "corr_model_vs_mid_pregame_clean": 0.8489}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 422, "model_brier": 0.1944, "kalshi_brier": 0.1957, "brier_diff_model_minus_kalshi": -0.0013}, "10-15": {"n_settled": 490, "model_brier": 0.2112, "kalshi_brier": 0.2041, "brier_diff_model_minus_kalshi": 0.0071}, "15-25": {"n_settled": 596, "model_brier": 0.2269, "kalshi_brier": 0.2161, "brier_diff_model_minus_kalshi": 0.0107}, "25-40": {"n_settled": 322, "model_brier": 0.2255, "kalshi_brier": 0.2063, "brier_diff_model_minus_kalshi": 0.0193}, "3-5": {"n_settled": 279, "model_brier": 0.1897, "kalshi_brier": 0.1906, "brier_diff_model_minus_kalshi": -0.0009}, "40+": {"n_settled": 69, "model_brier": 0.2933, "kalshi_brier": 0.1749, "brier_diff_model_minus_kalshi": 0.1184}, "5-10": {"n_settled": 578, "model_brier": 0.1953, "kalshi_brier": 0.197, "brier_diff_model_minus_kalshi": -0.0017}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.548, "slope": 0.87, "slope_se": 0.048}, "kalshi_slope": {"intercept": 0.231, "slope": 1.123, "slope_se": 0.055}, "n": 2756}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.5, "slope": 0.873, "slope_se": 0.036}, "kalshi_slope": {"intercept": 0.164, "slope": 1.087, "slope_se": 0.04}, "n": 4732}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 281, "model_brier": 0.337, "kalshi_brier": 0.2344, "brier_diff_model_minus_kalshi": 0.1026, "brier_diff_se": 0.0194, "corr_model_outcome": -0.044, "corr_kalshi_outcome": 0.2544}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
