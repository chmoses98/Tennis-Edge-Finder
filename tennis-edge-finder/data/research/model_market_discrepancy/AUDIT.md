# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-23T17:33Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 50,680): 0-3 13.9%, 3-5 9.4%, 5-10 19.7%, 10-15 15.3%, 15-25 19.3%, 25-40 14.1%, 40+ 8.2%; median gap 12.15 pp.
* **Where the extremes live**: 97.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.9%, Challenger 11.9%, doubles 6.6%). Main tour: ATP 4.8% and WTA 5.1% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 11,321): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.5%, STALE_QUOTE 18.8%, BOOK_QUALITY 18.0%, POOR_DATA 8.8%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.5%, IN_PLAY_QUOTE 3.6%, LIMITED_DATA 3.6%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.5%, market_freshness 18.8%, execution 18.0%, data 12.4%, market_freshness/coverage 9.0%, mapping 4.5%, model_calibration_or_unknown 2.2%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.3% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 11,321 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.1% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.7% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 485.0 points vs 1668.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.041, Gen-2 0.842, Gen-1 ledger 0.864 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 553 model 0.2237 vs Kalshi 0.2093; n 112 model 0.2783 vs Kalshi 0.1982.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 218,861 model-market comparisons (356,413 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 72,547 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-23T17:19:40.976820+00:00'], shadow board 58,554 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-23T17:19:45.381267+00:00'], Model 4 27,361 rows, 19,475 settled tickers, 6,881 tickers with an external scan.
* By model: {"gen1_ledger": 49282, "gen1_elo": 29445, "fair_v1": 29445, "gen2": 29445, "gen1_sr": 29445, "model4_fundamental": 25913, "model4_conditioned": 25886}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 50,680 | 13.9 | 9.4 | 19.7 | 15.3 | 19.3 | 14.1 | 8.2 | 12.15 | 41.6% | 22.3% |
| MW fair_v1 | 29,445 | 12.8 | 8.5 | 18.4 | 15.6 | 19.8 | 15.0 | 9.9 | 13.21 | 44.7% | 24.9% |
| MW gen1_elo | 29,445 | 12.7 | 8.5 | 18.9 | 15.3 | 20.0 | 15.0 | 9.7 | 13.04 | 44.6% | 24.7% |
| MW gen1_ledger | 21,235 | 15.4 | 10.8 | 21.4 | 15.0 | 18.7 | 12.8 | 5.9 | 10.6 | 37.4% | 18.7% |
| MW gen1_sr | 29,445 | 10.1 | 7.0 | 16.5 | 13.6 | 20.9 | 18.9 | 12.9 | 16.09 | 52.7% | 31.8% |
| MW gen2 | 29,445 | 10.9 | 7.2 | 16.2 | 14.1 | 19.5 | 18.0 | 14.1 | 15.66 | 51.5% | 32.1% |
| all families model4_conditioned | 25,886 | 21.9 | 18.9 | 34.8 | 17.6 | 4.3 | 1.4 | 1.0 | 5.95 | 6.7% | 2.5% |
| all families model4_fundamental | 25,913 | 16.6 | 13.4 | 34.1 | 20.6 | 10.6 | 3.4 | 1.3 | 7.78 | 15.2% | 4.7% |

Configurable thresholds (primary): >=5pp 76.7%, >=10pp 57.0%, >=15pp 41.6%, >=20pp 31.0%, >=25pp 22.3%, >=30pp 16.2%, >=40pp 8.2%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.53pp; >=10pp 45.6%, >=25pp 17.5%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,508 | 28.4 | 14.2 | 25.0 | 14.9 | 11.8 | 4.9 | 0.7 | 6.13 | 17.4% | 5.6% |
| CHALLENGER | 4,594 | 15.8 | 10.0 | 20.5 | 15.5 | 14.7 | 12.3 | 11.1 | 11.06 | 38.2% | 23.4% |
| ITF_MEN | 8,164 | 10.2 | 7.3 | 16.9 | 14.7 | 21.5 | 17.3 | 12.1 | 15.32 | 50.9% | 29.4% |
| ITF_WOMEN | 11,763 | 9.4 | 6.8 | 16.0 | 15.4 | 22.4 | 18.2 | 11.8 | 15.77 | 52.4% | 30.0% |
| WTA | 1,756 | 17.1 | 13.3 | 25.6 | 19.7 | 18.5 | 5.1 | 0.7 | 8.27 | 24.3% | 5.8% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,508 | 24.2 | 15.1 | 24.8 | 17.2 | 13.0 | 4.8 | 1.0 | 6.5 | 18.7% | 5.7% |
| CHALLENGER | 4,594 | 15.1 | 8.8 | 18.6 | 14.6 | 17.3 | 13.8 | 11.9 | 12.47 | 43.0% | 25.8% |
| ITF_MEN | 8,164 | 8.3 | 5.9 | 14.5 | 13.0 | 19.8 | 20.9 | 17.7 | 18.57 | 58.3% | 38.6% |
| ITF_WOMEN | 11,763 | 8.1 | 5.6 | 13.8 | 13.4 | 20.6 | 21.0 | 17.5 | 18.98 | 59.1% | 38.5% |
| WTA | 1,756 | 14.2 | 10.1 | 21.9 | 16.1 | 23.2 | 13.5 | 1.0 | 10.97 | 37.7% | 14.5% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,508 | 24.4 | 12.8 | 23.6 | 16.1 | 14.9 | 7.0 | 1.2 | 7.31 | 23.1% | 8.1% |
| CHALLENGER | 4,594 | 14.3 | 9.2 | 20.5 | 15.6 | 16.3 | 12.8 | 11.3 | 11.48 | 40.4% | 24.1% |
| ITF_MEN | 8,164 | 9.8 | 7.4 | 16.9 | 14.0 | 22.1 | 17.7 | 12.2 | 15.65 | 51.9% | 29.9% |
| ITF_WOMEN | 11,763 | 9.4 | 6.6 | 16.2 | 15.8 | 22.9 | 18.1 | 11.0 | 15.6 | 51.9% | 29.1% |
| WTA | 1,756 | 24.1 | 16.6 | 30.5 | 15.7 | 10.0 | 2.6 | 0.5 | 6.04 | 13.1% | 3.1% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,454 | 25.2 | 19.5 | 31.1 | 11.9 | 8.9 | 3.0 | 0.3 | 5.58 | 12.3% | 3.4% |
| CHALLENGER | 3,152 | 21.3 | 14.7 | 26.4 | 14.4 | 14.6 | 6.7 | 1.9 | 7.3 | 23.2% | 8.6% |
| DOUBLES | 1,585 | 5.4 | 4.3 | 11.5 | 10.4 | 21.1 | 26.1 | 21.1 | 23.85 | 68.3% | 47.3% |
| ITF_MEN | 6,056 | 13.8 | 9.0 | 19.9 | 16.1 | 21.3 | 13.3 | 6.6 | 12.22 | 41.2% | 19.9% |
| ITF_WOMEN | 7,052 | 12.7 | 9.0 | 19.3 | 15.1 | 21.6 | 16.2 | 6.1 | 12.84 | 43.9% | 22.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,055 | 22.3 | 16.0 | 29.6 | 18.1 | 10.1 | 3.6 | 0.4 | 6.86 | 14.0% | 4.0% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,438 | 28.7 | 14.4 | 25.4 | 14.9 | 11.6 | 4.5 | 0.5 | 5.96 | 16.6% | 5.0% |
| CHALLENGER | 3,240 | 20.7 | 12.4 | 25.1 | 17.9 | 15.2 | 6.7 | 1.9 | 8.33 | 23.8% | 8.6% |
| ITF_MEN | 6,006 | 12.3 | 8.8 | 20.2 | 16.6 | 22.6 | 14.3 | 5.2 | 12.52 | 42.1% | 19.5% |
| ITF_WOMEN | 8,800 | 11.2 | 8.2 | 18.2 | 17.4 | 24.3 | 15.3 | 5.4 | 13.52 | 45.1% | 20.7% |
| WTA | 1,706 | 17.4 | 13.1 | 25.6 | 19.9 | 18.5 | 4.8 | 0.8 | 8.25 | 24.0% | 5.6% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,438 | 24.4 | 15.4 | 25.0 | 17.1 | 13.0 | 4.5 | 0.6 | 6.43 | 18.1% | 5.1% |
| CHALLENGER | 3,240 | 19.1 | 11.2 | 23.1 | 17.4 | 17.6 | 9.4 | 2.2 | 9.08 | 29.2% | 11.6% |
| ITF_MEN | 6,007 | 9.8 | 7.1 | 16.8 | 14.9 | 21.7 | 19.3 | 10.5 | 15.49 | 51.4% | 29.8% |
| ITF_WOMEN | 8,801 | 9.2 | 6.5 | 15.2 | 14.9 | 22.6 | 20.4 | 11.1 | 16.57 | 54.1% | 31.5% |
| WTA | 1,706 | 14.2 | 10.1 | 21.9 | 16.1 | 23.3 | 13.4 | 1.0 | 11.0 | 37.7% | 14.4% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,408 | 25.4 | 19.7 | 31.1 | 12.1 | 8.4 | 2.9 | 0.2 | 5.52 | 11.6% | 3.1% |
| CHALLENGER | 2,747 | 22.8 | 15.8 | 27.9 | 14.3 | 13.9 | 4.7 | 0.6 | 6.72 | 19.2% | 5.2% |
| DOUBLES | 1,470 | 5.4 | 4.5 | 11.7 | 10.6 | 20.9 | 26.1 | 20.8 | 23.62 | 67.8% | 46.8% |
| ITF_MEN | 5,068 | 14.9 | 9.7 | 21.5 | 16.9 | 21.2 | 11.6 | 4.0 | 11.21 | 36.9% | 15.7% |
| ITF_WOMEN | 5,838 | 13.6 | 9.6 | 20.7 | 15.9 | 21.8 | 15.0 | 3.4 | 11.67 | 40.2% | 18.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,005 | 22.8 | 16.5 | 29.6 | 18.1 | 10.1 | 2.9 | 0.1 | 6.79 | 13.0% | 3.0% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,585 | 5.4 | 4.3 | 11.5 | 10.4 | 21.1 | 26.1 | 21.1 | 23.85 | 68.3% | 47.3% |
| singles | 19,650 | 16.2 | 11.3 | 22.2 | 15.3 | 18.5 | 11.8 | 4.7 | 10.04 | 34.9% | 16.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 6,548 | 13.0 | 8.9 | 19.2 | 15.6 | 18.7 | 14.6 | 9.9 | 12.83 | 43.2% | 24.5% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 18,191 | 13.2 | 8.5 | 18.5 | 15.2 | 19.9 | 14.8 | 9.8 | 13.15 | 44.5% | 24.7% |
| UNKNOWN | 4,469 | 10.8 | 7.6 | 17.2 | 17.0 | 20.7 | 16.2 | 10.6 | 14.09 | 47.5% | 26.8% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,207 | 19.5 | 11.9 | 21.4 | 16.5 | 15.3 | 9.1 | 6.4 | 9.17 | 30.7% | 15.4% |
| B | 3,661 | 12.3 | 8.7 | 20.0 | 16.3 | 19.2 | 12.6 | 10.8 | 12.54 | 42.6% | 23.4% |
| C | 4,162 | 11.4 | 8.7 | 19.8 | 15.1 | 19.5 | 14.8 | 10.6 | 13.19 | 44.9% | 25.4% |
| D | 4,633 | 12.2 | 7.7 | 17.2 | 15.5 | 21.5 | 15.7 | 10.2 | 14.0 | 47.4% | 25.9% |
| F | 8,782 | 7.6 | 5.5 | 15.0 | 14.7 | 23.4 | 21.3 | 12.5 | 17.79 | 57.1% | 33.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,961 | 22.9 | 15.9 | 28.9 | 15.1 | 11.6 | 4.1 | 1.5 | 6.68 | 17.2% | 5.6% |
| B | 2,908 | 16.2 | 10.3 | 23.2 | 16.3 | 19.3 | 10.7 | 4.0 | 10.04 | 33.9% | 14.6% |
| C | 4,188 | 11.3 | 7.4 | 18.2 | 14.3 | 21.6 | 16.7 | 10.6 | 14.36 | 48.8% | 27.3% |
| D | 2,980 | 14.5 | 9.8 | 19.8 | 14.5 | 21.0 | 14.3 | 6.1 | 12.04 | 41.4% | 20.4% |
| F | 5,198 | 10.2 | 8.4 | 15.4 | 14.9 | 22.8 | 20.1 | 8.2 | 15.52 | 51.0% | 28.2% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 9,432 | 17.7 | 10.6 | 20.8 | 16.3 | 15.8 | 9.9 | 8.8 | 10.26 | 34.6% | 18.8% |
| LIMITED | 6,274 | 13.3 | 10.0 | 20.5 | 15.6 | 19.3 | 13.5 | 7.8 | 11.96 | 40.6% | 21.3% |
| POOR | 13,739 | 9.2 | 6.3 | 15.9 | 15.0 | 22.7 | 19.2 | 11.7 | 16.19 | 53.5% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,713 | 26.3 | 20.1 | 34.2 | 12.5 | 5.0 | 1.7 | 0.2 | 5.37 | 6.9% | 1.9% |
| GAME_SPREAD | 4,736 | 22.2 | 15.2 | 33.5 | 17.4 | 9.0 | 2.3 | 0.3 | 6.73 | 11.7% | 2.6% |
| MATCH_WINNER | 21,235 | 15.4 | 10.8 | 21.4 | 15.0 | 18.7 | 12.8 | 5.9 | 10.6 | 37.4% | 18.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 10,053 | 29.3 | 17.1 | 31.0 | 12.4 | 8.0 | 1.8 | 0.4 | 5.46 | 10.2% | 2.2% |
| TOTAL_GAMES | 7,521 | 8.7 | 9.7 | 36.5 | 28.8 | 10.4 | 3.2 | 2.6 | 9.44 | 16.3% | 5.8% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,049 | 25.6 | 33.6 | 32.7 | 4.5 | 2.9 | 0.5 | 0.2 | 4.48 | 3.6% | 0.8% |
| GAME_SPREAD | 6,222 | 45.6 | 16.7 | 26.9 | 7.9 | 1.7 | 0.9 | 0.3 | 3.48 | 2.9% | 1.2% |
| TOTAL_GAMES | 10,615 | 5.0 | 7.8 | 41.1 | 34.5 | 6.9 | 2.5 | 2.1 | 9.58 | 11.6% | 4.6% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,052 | 24.2 | 17.8 | 35.7 | 12.6 | 6.9 | 2.4 | 0.3 | 5.81 | 9.6% | 2.8% |
| GAME_SPREAD | 6,225 | 19.4 | 13.4 | 27.9 | 20.8 | 13.3 | 4.3 | 0.9 | 7.97 | 18.6% | 5.3% |
| TOTAL_GAMES | 10,636 | 8.6 | 9.6 | 36.5 | 27.3 | 12.1 | 3.7 | 2.3 | 9.45 | 18.1% | 6.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 29,445 | 44.7% | 24.9% | 13.21 | 36.4% | 15.7% | 10.98 |
| gen1_elo | 29,445 | 44.6% | 24.7% | 13.04 | 36.1% | 15.8% | 10.82 |
| gen1_sr | 29,445 | 52.7% | 31.8% | 16.09 | 45.0% | 22.4% | 13.25 |
| gen2 | 29,445 | 51.5% | 32.1% | 15.66 | 44.8% | 24.0% | 13.14 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 14,915 | 15.7 | 10.3 | 21.2 | 17.2 | 20.2 | 12.0 | 3.4 | 10.8 | 35.6% | 15.4% |
| STALE | 14,530 | 9.8 | 6.6 | 15.6 | 13.9 | 19.3 | 18.1 | 16.7 | 16.97 | 54.1% | 34.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 14,703 | 16.4 | 11.3 | 22.2 | 15.1 | 17.9 | 12.3 | 4.8 | 10.01 | 35.0% | 17.1% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 50,680 | 14703 | 18387 | 17590 | 24.1 | 144.1 | 1400.4 |
| ge_15pp | 21,110 | 5145 | 6599 | 9366 | 26.0 | 439.4 | 1380.4 |
| ge_25pp | 11,321 | 2515 | 2884 | 5922 | 32.4 | 577.3 | 1380.4 |
| lt_10pp | 21,808 | 7345 | 8669 | 5794 | 22.4 | 48.3 | 1341.5 |

Current slate `SL-20261023T173318Z-233d821a`: 430 priced rows, quote age at build {'median': 13.9, 'max': 14.0}, freshness {'AGING': 430}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 23 | 0.0 | 0.0 | 21.7 | 4.3 | 39.1 | 34.8 | 0.0 | 20.49 | 73.9% | 34.8% |
| EXTERNAL_LONE_OUTLIER | 13 | 69.2 | 30.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.3 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,766 | 19.1 | 11.3 | 24.5 | 18.7 | 18.4 | 7.3 | 0.7 | 8.96 | 26.4% | 8.0% |
| KALSHI_LONE_OUTLIER | 17 | 5.9 | 5.9 | 76.5 | 0.0 | 5.9 | 5.9 | 0.0 | 6.11 | 11.8% | 5.9% |
| MARKETS_AGREE | 545 | 65.0 | 35.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,166 | 0.0 | 2.2 | 35.5 | 26.1 | 24.7 | 10.7 | 0.8 | 12.27 | 36.2% | 11.5% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 29,445 | 4530 (15.4%) | 25.7% | 0.9% | {"EXTERNAL_STALE": 2766, "AGREES_WITH_KALSHI": 1166, "ALL_AGREE": 545, "SUPPORTS_MODEL_DIRECTION": 22, "AGREES_WITH_MODEL": 17, "EXTERNAL_OUTLIER": 13, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 13,166 | 1171 (8.9%) | 36.0% | 1.6% | {"EXTERNAL_STALE": 730, "AGREES_WITH_KALSHI": 422, "SUPPORTS_MODEL_DIRECTION": 17, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 7,344 | 365 (5.0%) | 36.7% | 2.5% | {"EXTERNAL_STALE": 222, "AGREES_WITH_KALSHI": 134, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,584 | 342 (9.5%) | 37.1% | 2.6% | {"EXTERNAL_STALE": 206, "AGREES_WITH_KALSHI": 127, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 11,694 | 2536 (21.7%) | 17.3% | 0.8% | {"EXTERNAL_STALE": 1518, "ALL_AGREE": 545, "AGREES_WITH_KALSHI": 440, "AGREES_WITH_MODEL": 15, "EXTERNAL_OUTLIER": 13, "SUPPORTS_MODEL_DIRECTION": 4, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,617 | 10.1 | 7.5 | 19.4 | 14.3 | 22.5 | 16.0 | 10.1 | 14.29 | 48.6% | 26.1% |
| 4-10x | 3,856 | 11.0 | 8.2 | 19.1 | 15.4 | 21.1 | 15.0 | 10.1 | 13.76 | 46.3% | 25.2% |
| <2x | 14,872 | 14.9 | 9.7 | 19.0 | 16.5 | 17.7 | 13.1 | 9.2 | 11.91 | 40.0% | 22.3% |
| >=10x | 5,100 | 11.0 | 6.3 | 15.2 | 14.4 | 21.9 | 19.4 | 11.8 | 16.24 | 53.1% | 31.2% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 7,460 | 12.3 | 8.5 | 19.6 | 16.0 | 19.3 | 13.7 | 10.7 | 12.96 | 43.6% | 24.4% |
| 300-1000 | 6,335 | 11.7 | 8.5 | 17.2 | 15.3 | 20.7 | 16.3 | 10.3 | 13.99 | 47.3% | 26.6% |
| <300 | 9,717 | 8.7 | 5.7 | 15.5 | 14.8 | 23.0 | 20.1 | 12.3 | 16.92 | 55.3% | 32.4% |
| >=3000 | 5,933 | 21.4 | 13.0 | 23.1 | 16.4 | 14.2 | 7.0 | 4.8 | 7.96 | 26.0% | 11.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 841 | 0.5482 | 0.4093 | 0.4994 | +0.049 | -0.090 | -0.0031 ± 0.0053 |
| ratio 4-10x | 578 | 0.5878 | 0.442 | 0.4965 | +0.091 | -0.054 | 0.0125 ± 0.0067 |
| ratio <2x | 2076 | 0.5382 | 0.4144 | 0.4461 | +0.092 | -0.032 | 0.0126 ± 0.0032 |
| ratio >=10x | 773 | 0.5693 | 0.3941 | 0.4657 | +0.104 | -0.072 | 0.0054 ± 0.0065 |
| thinner_sample 1000-3000 | 1151 | 0.5421 | 0.4146 | 0.4448 | +0.097 | -0.030 | 0.0114 ± 0.0042 |
| thinner_sample 300-1000 | 982 | 0.5667 | 0.4233 | 0.4929 | +0.074 | -0.070 | 0.001 ± 0.0052 |
| thinner_sample <300 | 1443 | 0.559 | 0.3925 | 0.4671 | +0.092 | -0.074 | 0.0081 ± 0.0047 |
| thinner_sample >=3000 | 692 | 0.5362 | 0.4414 | 0.4668 | +0.069 | -0.025 | 0.0135 ± 0.0044 |
| data_status ADEQUATE | 1212 | 0.5387 | 0.4331 | 0.4505 | +0.088 | -0.017 | 0.013 ± 0.0036 |
| data_status LIMITED | 990 | 0.5503 | 0.4167 | 0.4798 | +0.070 | -0.063 | 0.0045 ± 0.0048 |
| data_status POOR | 2066 | 0.5617 | 0.4004 | 0.4705 | +0.091 | -0.070 | 0.0071 ± 0.0038 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 621 | 0.1998 | 0.2009 | -0.0011 ± 0.0006 | 0.58 | 0.5822 | 0.5034 | 0.4885 | 0.533 | -0.060 ± 0.0188 | -0.01 (5) |
| 3-5 | 395 | 0.2022 | 0.2016 | +0.0006 ± 0.0018 | 0.5875 | 0.5843 | 0.5025 | 0.4625 | 0.4734 | -0.099 ± 0.0233 | 0.02 (1) |
| 5-10 | 880 | 0.2013 | 0.2012 | +0.0001 ± 0.0023 | 0.5889 | 0.5855 | 0.5101 | 0.4359 | 0.4682 | -0.088 ± 0.0157 | -0.0167 (6) |
| 10-15 | 734 | 0.2143 | 0.2039 | +0.0105 ± 0.0042 | 0.6194 | 0.5893 | 0.5291 | 0.405 | 0.4237 | -0.106 ± 0.0166 | -0.048 (5) |
| 15-25 | 973 | 0.2244 | 0.2134 | +0.0110 ± 0.0058 | 0.6434 | 0.6105 | 0.5776 | 0.3818 | 0.4512 | -0.091 ± 0.0147 | -0.0033 (9) |
| 25-40 | 553 | 0.2237 | 0.2093 | +0.0145 ± 0.0116 | 0.6356 | 0.6017 | 0.6566 | 0.347 | 0.4756 | -0.074 ± 0.0179 | -0.01 (1) |
| 40+ | 112 | 0.2783 | 0.1982 | +0.0800 ± 0.0365 | 0.7629 | 0.5814 | 0.7564 | 0.3087 | 0.4464 | -0.077 ± 0.0358 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3215 | 0.1835 | 0.1845 | -0.0010 ± 0.0003 | 0.5421 | 0.5432 | 0.4931 | 0.478 | 0.5142 | -0.019 ± 0.0076 | -0.0129 (17) |
| 3-5 | 2108 | 0.1973 | 0.196 | +0.0013 ± 0.0008 | 0.5748 | 0.5688 | 0.4854 | 0.4455 | 0.4492 | -0.053 ± 0.0098 | 0.0 (2) |
| 5-10 | 4583 | 0.1975 | 0.1946 | +0.0029 ± 0.001 | 0.579 | 0.5686 | 0.4803 | 0.4063 | 0.4233 | -0.045 ± 0.0066 | -0.0119 (21) |
| 10-15 | 3921 | 0.1973 | 0.179 | +0.0184 ± 0.0017 | 0.5804 | 0.5285 | 0.4855 | 0.361 | 0.3489 | -0.075 ± 0.0067 | -0.0281 (16) |
| 15-25 | 4948 | 0.2079 | 0.1692 | +0.0387 ± 0.0023 | 0.6089 | 0.5011 | 0.5051 | 0.3087 | 0.3092 | -0.073 ± 0.0058 | -0.0025 (44) |
| 25-40 | 3854 | 0.2231 | 0.1303 | +0.0928 ± 0.0036 | 0.6404 | 0.398 | 0.5314 | 0.2183 | 0.2302 | -0.059 ± 0.0056 | -0.01 (1) |
| 40+ | 2500 | 0.38 | 0.0464 | +0.3336 ± 0.0049 | 0.99 | 0.1773 | 0.6333 | 0.1079 | 0.066 | -0.078 ± 0.004 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 484 | 0.2047 | 0.2052 | -0.0005 ± 0.0007 | 0.5911 | 0.5921 | 0.5054 | 0.4904 | 0.5103 | -0.108 ± 0.0221 | -0.01 (3) |
| 3-5 | 352 | 0.2231 | 0.2212 | +0.0020 ± 0.002 | 0.6326 | 0.6285 | 0.5134 | 0.4736 | 0.4631 | -0.118 ± 0.0267 | 0.02 (1) |
| 5-10 | 761 | 0.2052 | 0.2047 | +0.0005 ± 0.0025 | 0.5966 | 0.5942 | 0.547 | 0.4722 | 0.5085 | -0.082 ± 0.0169 | -0.01 (4) |
| 10-15 | 706 | 0.2174 | 0.2092 | +0.0082 ± 0.0043 | 0.6245 | 0.604 | 0.5665 | 0.4422 | 0.4731 | -0.112 ± 0.0179 | -0.04 (5) |
| 15-25 | 995 | 0.2302 | 0.2102 | +0.0201 ± 0.0057 | 0.6535 | 0.6031 | 0.5878 | 0.392 | 0.4432 | -0.101 ± 0.0148 | -0.0133 (9) |
| 25-40 | 704 | 0.2623 | 0.1982 | +0.0641 ± 0.0106 | 0.7318 | 0.577 | 0.6535 | 0.3378 | 0.3963 | -0.112 ± 0.0164 | -0.0075 (4) |
| 40+ | 266 | 0.3583 | 0.1726 | +0.1858 ± 0.0252 | 0.9861 | 0.5157 | 0.7316 | 0.2472 | 0.312 | -0.070 ± 0.0245 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2714 | 0.193 | 0.1932 | -0.0002 ± 0.0003 | 0.5626 | 0.5629 | 0.5099 | 0.495 | 0.5096 | -0.044 ± 0.0087 | -0.0133 (15) |
| 3-5 | 1808 | 0.1979 | 0.1974 | +0.0005 ± 0.0008 | 0.5737 | 0.5719 | 0.5146 | 0.4747 | 0.4873 | -0.041 ± 0.0107 | 0.02 (1) |
| 5-10 | 4055 | 0.1952 | 0.1935 | +0.0017 ± 0.001 | 0.5754 | 0.5664 | 0.5083 | 0.4342 | 0.4626 | -0.032 ± 0.007 | -0.0117 (6) |
| 10-15 | 3555 | 0.2009 | 0.1886 | +0.0123 ± 0.0018 | 0.5886 | 0.5498 | 0.5126 | 0.3887 | 0.402 | -0.056 ± 0.0074 | -0.0189 (18) |
| 15-25 | 4895 | 0.2161 | 0.1779 | +0.0382 ± 0.0024 | 0.6279 | 0.5234 | 0.5253 | 0.3295 | 0.3336 | -0.070 ± 0.0061 | -0.0086 (42) |
| 25-40 | 4532 | 0.2522 | 0.1381 | +0.1142 ± 0.0035 | 0.7092 | 0.4234 | 0.5587 | 0.2418 | 0.2229 | -0.085 ± 0.0055 | -0.0044 (18) |
| 40+ | 3570 | 0.3938 | 0.0613 | +0.3325 ± 0.0047 | 1.037 | 0.2186 | 0.651 | 0.1195 | 0.0854 | -0.072 ± 0.004 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 596 | 0.2 | 0.2022 | -0.0022 ± 0.0007 | 0.5809 | 0.5862 | 0.5004 | 0.4851 | 0.5503 | -0.026 ± 0.019 | -0.0137 (8) |
| 3-5 | 426 | 0.2003 | 0.1985 | +0.0018 ± 0.0017 | 0.5825 | 0.5768 | 0.506 | 0.4663 | 0.4648 | -0.118 ± 0.0223 | 0.0067 (3) |
| 5-10 | 897 | 0.2003 | 0.1971 | +0.0032 ± 0.0022 | 0.5869 | 0.5752 | 0.5068 | 0.4328 | 0.4459 | -0.101 ± 0.0152 | -0.0071 (7) |
| 10-15 | 742 | 0.2085 | 0.2051 | +0.0034 ± 0.0041 | 0.6061 | 0.5925 | 0.539 | 0.4153 | 0.465 | -0.084 ± 0.0165 | -0.0317 (6) |
| 15-25 | 916 | 0.2309 | 0.2122 | +0.0188 ± 0.0059 | 0.6596 | 0.6074 | 0.5879 | 0.3936 | 0.441 | -0.112 ± 0.0152 | -0.03 (1) |
| 25-40 | 573 | 0.2139 | 0.2178 | -0.0039 ± 0.0114 | 0.616 | 0.6214 | 0.6684 | 0.3571 | 0.5166 | -0.053 ± 0.0176 | 0.015 (2) |
| 40+ | 118 | 0.2919 | 0.209 | +0.0829 ± 0.0368 | 0.8038 | 0.6052 | 0.7657 | 0.3158 | 0.4576 | -0.070 ± 0.0381 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3148 | 0.1852 | 0.1857 | -0.0005 ± 0.0003 | 0.5448 | 0.5457 | 0.4912 | 0.476 | 0.4908 | -0.037 ± 0.0077 | -0.0163 (35) |
| 3-5 | 2126 | 0.1943 | 0.192 | +0.0023 ± 0.0008 | 0.5706 | 0.5633 | 0.488 | 0.4483 | 0.4403 | -0.068 ± 0.0097 | -0.0094 (18) |
| 5-10 | 4646 | 0.1957 | 0.19 | +0.0057 ± 0.001 | 0.5754 | 0.5566 | 0.4826 | 0.4086 | 0.4074 | -0.061 ± 0.0064 | -0.01 (31) |
| 10-15 | 3811 | 0.1902 | 0.1741 | +0.0162 ± 0.0017 | 0.5638 | 0.516 | 0.4978 | 0.3743 | 0.37 | -0.069 ± 0.0067 | -0.015 (12) |
| 15-25 | 5107 | 0.2104 | 0.1717 | +0.0387 ± 0.0023 | 0.6145 | 0.5069 | 0.5139 | 0.3189 | 0.3172 | -0.073 ± 0.0058 | -0.03 (2) |
| 25-40 | 3862 | 0.2194 | 0.1338 | +0.0855 ± 0.0037 | 0.6328 | 0.4057 | 0.5376 | 0.2213 | 0.246 | -0.049 ± 0.0057 | 0.01 (3) |
| 40+ | 2429 | 0.3943 | 0.0509 | +0.3434 ± 0.0052 | 1.0305 | 0.1892 | 0.6453 | 0.1142 | 0.0704 | -0.081 ± 0.0044 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 980 | 0.195 | 0.1951 | -0.0002 ± 0.0005 | 0.5693 | 0.5692 | 0.5047 | 0.4896 | 0.4959 | -0.057 ± 0.0143 | -0.0224 (49) |
| 3-5 | 683 | 0.1913 | 0.1906 | +0.0007 ± 0.0013 | 0.5596 | 0.5567 | 0.4893 | 0.4494 | 0.4583 | -0.057 ± 0.0171 | -0.0194 (34) |
| 5-10 | 1420 | 0.2008 | 0.1948 | +0.0060 ± 0.0018 | 0.5907 | 0.5718 | 0.4959 | 0.4225 | 0.4197 | -0.072 ± 0.0119 | -0.005 (78) |
| 10-15 | 943 | 0.2099 | 0.1985 | +0.0115 ± 0.0036 | 0.6094 | 0.5791 | 0.5207 | 0.3975 | 0.4104 | -0.067 ± 0.0148 | 0.0014 (64) |
| 15-25 | 1269 | 0.2311 | 0.21 | +0.0211 ± 0.005 | 0.6598 | 0.6047 | 0.576 | 0.3812 | 0.4255 | -0.071 ± 0.0129 | -0.0214 (59) |
| 25-40 | 774 | 0.2475 | 0.2068 | +0.0407 ± 0.01 | 0.7031 | 0.5949 | 0.6714 | 0.3591 | 0.4496 | -0.085 ± 0.0153 | -0.0219 (26) |
| 40+ | 258 | 0.354 | 0.1967 | +0.1573 ± 0.0273 | 1.0218 | 0.5751 | 0.808 | 0.3255 | 0.4225 | -0.096 ± 0.0249 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3193 | 0.1824 | 0.1826 | -0.0002 ± 0.0003 | 0.5378 | 0.5373 | 0.5055 | 0.4902 | 0.5017 | -0.037 ± 0.0076 | -0.0157 (88) |
| 3-5 | 2214 | 0.192 | 0.1902 | +0.0018 ± 0.0007 | 0.5616 | 0.5571 | 0.495 | 0.4552 | 0.4521 | -0.053 ± 0.0094 | -0.0209 (69) |
| 5-10 | 4415 | 0.1971 | 0.1887 | +0.0084 ± 0.001 | 0.58 | 0.5552 | 0.4913 | 0.4178 | 0.4005 | -0.071 ± 0.0066 | -0.0082 (132) |
| 10-15 | 3075 | 0.2053 | 0.1895 | +0.0158 ± 0.002 | 0.599 | 0.5574 | 0.5272 | 0.404 | 0.4007 | -0.065 ± 0.0079 | -0.0053 (105) |
| 15-25 | 3860 | 0.2293 | 0.1994 | +0.0298 ± 0.0028 | 0.6614 | 0.5782 | 0.5684 | 0.3729 | 0.3951 | -0.064 ± 0.0072 | -0.0253 (107) |
| 25-40 | 2670 | 0.2593 | 0.1842 | +0.0751 ± 0.0052 | 0.7347 | 0.5373 | 0.6314 | 0.3176 | 0.3573 | -0.078 ± 0.0081 | -0.0229 (51) |
| 40+ | 1186 | 0.3778 | 0.1441 | +0.2337 ± 0.0116 | 1.0713 | 0.4344 | 0.7292 | 0.2259 | 0.258 | -0.071 ± 0.0104 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4268 | 1.041 ± 0.043 | 1.137 | 0.1689 | 0.1647 | 0.2136 | 0.2054 |
| gen2 | 4268 | 0.842 ± 0.04 | 1.094 | 0.169 | 0.1653 | 0.2334 | 0.2051 |
| gen1_elo | 4268 | 1.015 ± 0.042 | 1.126 | 0.1758 | 0.1648 | 0.2126 | 0.2057 |
| gen1_sr | 4268 | 1.032 ± 0.052 | 1.168 | 0.1297 | 0.1674 | 0.2295 | 0.2047 |
| gen1_ledger | 6327 | 0.864 ± 0.03 | 1.077 | 0.1836 | 0.1793 | 0.2183 | 0.1995 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 21,110)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,857 | 23.0% |
| STALE_QUOTE | market_freshness | 4,597 | 21.8% |
| BOOK_QUALITY | execution | 3,923 | 18.6% |
| POOR_DATA | data | 2,402 | 11.4% |
| LIMITED_DATA | data | 1,315 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,150 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 991 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 895 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 635 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 344 | 1.6% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 23.0%, market_freshness 21.8%, execution 18.6%, data 17.6%, market_freshness/coverage 8.5%, model_calibration_or_unknown 4.7%, mapping 4.2%, model_calibration 1.6%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 94.4%, LOW_DATA_QUALITY 71.1%, THIN_PLAYER_HISTORY 60.1%, STALE_PLAYER_DATA 49.8%, STALE_KALSHI_QUOTE 44.4%, MODEL_INTERNAL_DISAGREEMENT 42.5%, ASYMMETRIC_SAMPLE_SIZE 33.6%, WIDE_SPREAD 24.7%, MODEL_HIGH_UNCERTAINTY 17.8%, PLAYER_IDENTITY_RISK 16.3%, LEVEL_TRANSFER_RISK 11.1%, LOW_DISPLAYED_LIQUIDITY 8.1%, EVENT_MAPPING_RISK 8.0%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.1%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.6%, POST_SETTLEMENT_OBSERVATION 23.0%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 11,321)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,905 | 34.5% |
| STALE_QUOTE | market_freshness | 2,123 | 18.8% |
| BOOK_QUALITY | execution | 2,040 | 18.0% |
| POOR_DATA | data | 999 | 8.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 616 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 509 | 4.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 403 | 3.6% |
| LIMITED_DATA | data | 403 | 3.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 244 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 78 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.5%, market_freshness 18.8%, execution 18.0%, data 12.4%, market_freshness/coverage 9.0%, mapping 4.5%, model_calibration_or_unknown 2.2%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.1%, LOW_DATA_QUALITY 74.6%, THIN_PLAYER_HISTORY 62.3%, STALE_KALSHI_QUOTE 52.3%, STALE_PLAYER_DATA 44.5%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 34.8%, WIDE_SPREAD 23.9%, PLAYER_IDENTITY_RISK 19.6%, MODEL_HIGH_UNCERTAINTY 18.1%, LEVEL_TRANSFER_RISK 9.8%, EVENT_MAPPING_RISK 9.5%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.6%, POST_SETTLEMENT_OBSERVATION 34.5%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 8821, "IDENTITY_AMBIGUOUS": 2500}; ticker orientation: {"VERIFIED": 11321}.

Checks: discipline:AMBIGUOUS 749, discipline:PASS 10572, identity_confidence:AMBIGUOUS 2220, identity_confidence:PASS 9101, level_mapping:NA 761, level_mapping:PASS 10560, market_pair:AMBIGUOUS 395, market_pair:NA 284, market_pair:PASS 10642, model_complement:NA 251, model_complement:PASS 11070, namesake:PASS 11321, physical_match_id:NA 3977, physical_match_id:PASS 7344, player_ids:PASS 11321, same_pair_other_event:PASS 11321, ticker_orientation:PASS 11321

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,962 | 4.8% | 4.3% | 1.7% | {"market_freshness": 53, "model_calibration_or_unknown": 43, "data": 35, "execution": 21, "market_freshness/coverage": 13, "model_calibration": 13, "coverage": 11} | 5.87 | 0.2166 / 0.2108 (461) | 18.9% | 3.8% | 3.2% | 2.9% |
| CHALLENGER | 7,746 | 17.4% | 7.1% | 11.9% | {"coverage": 760, "market_freshness/coverage": 164, "market_freshness": 148, "data": 140, "model_calibration_or_unknown": 61, "execution": 31, "model_calibration": 28, "mapping": 15, "possible_market_error": 1} | 7.44 | 0.2202 / 0.2083 (1862) | 35.0% | 17.7% | 3.8% | 22.7% |
| DOUBLES | 1,585 | 47.3% | 46.8% | 6.6% | {"execution": 384, "mapping": 198, "market_freshness": 106, "market_freshness/coverage": 54, "coverage": 7} | 23.62 | 0.3102 / 0.2354 (420) | 14.8% | 0.0% | 100.0% | 7.3% |
| ITF_MEN | 14,220 | 25.3% | 17.7% | 31.8% | {"coverage": 1329, "execution": 688, "market_freshness": 619, "data": 481, "market_freshness/coverage": 310, "mapping": 173, "model_calibration_or_unknown": 2, "model_calibration": 2} | 11.91 | 0.2146 / 0.1973 (3207) | 37.6% | 69.7% | 19.8% | 22.1% |
| ITF_WOMEN | 18,815 | 27.1% | 19.8% | 45.1% | {"coverage": 1776, "market_freshness": 1109, "execution": 879, "data": 712, "market_freshness/coverage": 429, "mapping": 117, "model_calibration_or_unknown": 68, "model_calibration": 11} | 12.84 | 0.2029 / 0.1941 (3664) | 39.8% | 56.1% | 9.9% | 22.2% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,811 | 5.1% | 4.6% | 1.3% | {"market_freshness": 48, "model_calibration_or_unknown": 29, "execution": 23, "model_calibration": 13, "data": 11, "market_freshness/coverage": 10, "coverage": 9, "mapping": 1} | 7.73 | 0.2385 / 0.2306 (451) | 24.8% | 1.3% | 1.5% | 3.6% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.5% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 15 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 16 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 17 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 18 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 19 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 20 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 21 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 22 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 23 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 365 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 24 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 25 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 26 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 27 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 28 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 29 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 30 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 31 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 32 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 33 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 34 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 35 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 36 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 37 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 12.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 768 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 39 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 40 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 41 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 42 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 43 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 44 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 752 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 45 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 46 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 47 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 48 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 49 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 50 | `KXITFWMATCH-26OCT20CHAAPI-CHA` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 555 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 122.0, ratio 20.3); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9707, "by_level_share_of_ge_25pp": {"ATP": 0.0167, "CHALLENGER": 0.1191, "DOUBLES": 0.0662, "ITF_MEN": 0.3183, "ITF_WOMEN": 0.4506, "OTHER": 0.0011, "WTA": 0.0127, "WTA125": 0.0154}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5231, "share_primary_cause_market_settled_or_in_play": 0.4349, "share_primary_cause_stale_quote_only": 0.1875}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 11321, "identity_ambiguous_share": 0.2208, "ticker_orientation": {"VERIFIED": 11321}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 7344, "with_external": 365, "coverage": 0.0497, "external_status": {"EXTERNAL_STALE": 222, "AGREES_WITH_KALSHI": 134, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 222, "MODEL_LONE_OUTLIER": 134, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3671, "share_external_supports_model": 0.0247}, "pregame_clean_ge_25pp": {"n": 3584, "with_external": 342, "coverage": 0.0954, "external_status": {"EXTERNAL_STALE": 206, "AGREES_WITH_KALSHI": 127, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 206, "MODEL_LONE_OUTLIER": 127, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3713, "share_external_supports_model": 0.0263}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 485.0, "median_sample_ratio": 2.44, "median_min_matches": 21.0, "median_max_days_since_last": 225.0, "share_severe_asymmetry": 0.2145, "data_status": {"POOR": 6331, "LIMITED": 2975, "ADEQUATE": 2015}, "comparison_lt_10pp": {"median_thinner_serve_points": 1668.0, "median_sample_ratio": 1.71, "median_min_matches": 93.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 841, "model_minus_observed": 0.0488, "kalshi_minus_observed": -0.0901, "brier_diff_model_minus_kalshi": -0.0031}, "4-10x": {"n": 578, "model_minus_observed": 0.0913, "kalshi_minus_observed": -0.0545, "brier_diff_model_minus_kalshi": 0.0125}, "<2x": {"n": 2076, "model_minus_observed": 0.0921, "kalshi_minus_observed": -0.0316, "brier_diff_model_minus_kalshi": 0.0126}, ">=10x": {"n": 773, "model_minus_observed": 0.1036, "kalshi_minus_observed": -0.0716, "brier_diff_model_minus_kalshi": 0.0054}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4268, "model": {"intercept": -0.546, "slope": 0.842, "slope_se": 0.04}, "kalshi_mid_same_rows": {"intercept": 0.213, "slope": 1.094, "slope_se": 0.044}, "mean_extremity_model": 0.169, "mean_extremity_kalshi": 0.1653, "model_brier": 0.2334, "kalshi_brier": 0.2051, "brier_diff_model_minus_kalshi": 0.0284, "brier_diff_se": 0.0029, "model_logloss": 0.6634, "kalshi_logloss": 0.5927}, "fair_v1": {"n": 4268, "model": {"intercept": -0.411, "slope": 1.041, "slope_se": 0.043}, "kalshi_mid_same_rows": {"intercept": 0.307, "slope": 1.137, "slope_se": 0.045}, "mean_extremity_model": 0.1689, "mean_extremity_kalshi": 0.1647, "model_brier": 0.2136, "kalshi_brier": 0.2054, "brier_diff_model_minus_kalshi": 0.0082, "brier_diff_se": 0.0024, "model_logloss": 0.6158, "kalshi_logloss": 0.5933}, "gen1_elo": {"n": 4268, "model": {"intercept": -0.396, "slope": 1.015, "slope_se": 0.042}, "kalshi_mid_same_rows": {"intercept": 0.316, "slope": 1.126, "slope_se": 0.044}, "mean_extremity_model": 0.1758, "mean_extremity_kalshi": 0.1648, "model_brier": 0.2126, "kalshi_brier": 0.2057, "brier_diff_model_minus_kalshi": 0.0069, "brier_diff_se": 0.0024, "model_logloss": 0.6145, "kalshi_logloss": 0.5939}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2494, "share_ge_15": 0.4471, "median_abs_gap": 13.21, "n": 29445}, "gen1_elo": {"share_ge_25": 0.2468, "share_ge_15": 0.4464, "median_abs_gap": 13.04, "n": 29445}, "gen1_sr": {"share_ge_25": 0.3179, "share_ge_15": 0.5273, "median_abs_gap": 16.09, "n": 29445}, "gen2": {"share_ge_25": 0.3207, "share_ge_15": 0.5155, "median_abs_gap": 15.66, "n": 29445}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.157, "share_ge_15": 0.3636, "median_abs_gap": 10.98, "n": 22824}, "gen1_elo": {"share_ge_25": 0.1582, "share_ge_15": 0.3613, "median_abs_gap": 10.82, "n": 22821}, "gen1_sr": {"share_ge_25": 0.2245, "share_ge_15": 0.4496, "median_abs_gap": 13.25, "n": 22825}, "gen2": {"share_ge_25": 0.2401, "share_ge_15": 0.4478, "median_abs_gap": 13.14, "n": 22826}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.87, "share_ge_25_all": 0.0477, "share_ge_25_pregame_clean": 0.0429}, "WTA": {"median_abs_gap_pregame_clean": 7.73, "share_ge_25_all": 0.0512, "share_ge_25_pregame_clean": 0.0461}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2334, "share_within_10pp_all": 0.4303, "share_within_10pp_pregame_clean": 0.4832, "corr_model_vs_mid_pregame_clean": 0.8438}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 621, "model_brier": 0.1998, "kalshi_brier": 0.2009, "brier_diff_model_minus_kalshi": -0.0011}, "10-15": {"n_settled": 734, "model_brier": 0.2143, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0105}, "15-25": {"n_settled": 973, "model_brier": 0.2244, "kalshi_brier": 0.2134, "brier_diff_model_minus_kalshi": 0.011}, "25-40": {"n_settled": 553, "model_brier": 0.2237, "kalshi_brier": 0.2093, "brier_diff_model_minus_kalshi": 0.0145}, "3-5": {"n_settled": 395, "model_brier": 0.2022, "kalshi_brier": 0.2016, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 112, "model_brier": 0.2783, "kalshi_brier": 0.1982, "brier_diff_model_minus_kalshi": 0.08}, "5-10": {"n_settled": 880, "model_brier": 0.2013, "kalshi_brier": 0.2012, "brier_diff_model_minus_kalshi": 0.0001}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.546, "slope": 0.842, "slope_se": 0.04}, "kalshi_slope": {"intercept": 0.213, "slope": 1.094, "slope_se": 0.044}, "n": 4268}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.507, "slope": 0.864, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.159, "slope": 1.077, "slope_se": 0.035}, "n": 6327}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 420, "model_brier": 0.3102, "kalshi_brier": 0.2354, "brier_diff_model_minus_kalshi": 0.0748, "brier_diff_se": 0.0149, "corr_model_outcome": 0.0445, "corr_kalshi_outcome": 0.2577}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
