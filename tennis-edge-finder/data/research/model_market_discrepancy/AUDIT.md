# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-18T01:24Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 37,216): 0-3 14.4%, 3-5 9.5%, 5-10 19.9%, 10-15 15.3%, 15-25 18.8%, 25-40 13.7%, 40+ 8.3%; median gap 11.89 pp.
* **Where the extremes live**: 97.8% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.6%, Challenger 11.9%, doubles 7.0%). Main tour: ATP 2.7% and WTA 5.5% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 8,176): MARKET_ALREADY_SETTLED_WHEN_PRICED 36.2%, BOOK_QUALITY 18.3%, STALE_QUOTE 18.0%, POOR_DATA 8.4%, POSSIBLY_IN_PLAY_QUOTE 5.3%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 3.9%, IN_PLAY_QUOTE 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.5%. By class: coverage 36.2%, execution 18.3%, market_freshness 18.0%, data 12.2%, market_freshness/coverage 8.6%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.5%.
* **Stale / settled / in-play**: 53.2% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 44.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 8,176 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.4% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 3.9%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 22.9% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 553.0 points vs 1841.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.055, Gen-2 0.857, Gen-1 ledger 0.877 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 376 model 0.2247 vs Kalshi 0.2073; n 78 model 0.3044 vs Kalshi 0.1729.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 151,826 model-market comparisons (250,163 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 54,353 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-18T01:17:58.094793+00:00'], shadow board 41,232 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-18T01:18:00.937236+00:00'], Model 4 16,997 rows, 15,610 settled tickers, 5,326 tickers with an external scan.
* By model: {"gen1_ledger": 36261, "gen1_elo": 20738, "fair_v1": 20738, "gen2": 20738, "gen1_sr": 20738, "model4_fundamental": 16311, "model4_conditioned": 16302}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 37,216 | 14.4 | 9.5 | 19.9 | 15.3 | 18.8 | 13.7 | 8.3 | 11.89 | 40.8% | 22.0% |
| MW fair_v1 | 20,738 | 13.5 | 8.5 | 18.4 | 15.8 | 19.2 | 14.6 | 10.0 | 13.01 | 43.8% | 24.6% |
| MW gen1_elo | 20,738 | 13.1 | 9.0 | 19.5 | 15.1 | 19.3 | 14.3 | 9.6 | 12.53 | 43.2% | 23.9% |
| MW gen1_ledger | 16,478 | 15.6 | 10.7 | 21.8 | 14.8 | 18.4 | 12.4 | 6.2 | 10.45 | 37.0% | 18.6% |
| MW gen1_sr | 20,738 | 9.7 | 7.4 | 16.5 | 14.2 | 21.5 | 18.6 | 12.1 | 15.86 | 52.3% | 30.8% |
| MW gen2 | 20,738 | 11.4 | 7.1 | 16.5 | 14.1 | 19.9 | 17.6 | 13.3 | 15.45 | 50.9% | 31.0% |
| all families model4_conditioned | 16,302 | 21.4 | 19.4 | 34.4 | 17.3 | 4.8 | 1.6 | 1.1 | 5.92 | 7.5% | 2.7% |
| all families model4_fundamental | 16,311 | 16.3 | 13.1 | 34.8 | 20.0 | 11.1 | 3.3 | 1.4 | 7.83 | 15.8% | 4.7% |

Configurable thresholds (primary): >=5pp 76.1%, >=10pp 56.1%, >=15pp 40.8%, >=20pp 30.4%, >=25pp 22.0%, >=30pp 15.9%, >=40pp 8.3%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.36pp; >=10pp 45.0%, >=25pp 17.3%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,610 | 29.6 | 13.9 | 24.6 | 17.3 | 11.4 | 2.5 | 0.8 | 6.04 | 14.6% | 3.2% |
| CHALLENGER | 3,392 | 15.9 | 10.1 | 20.2 | 15.7 | 14.3 | 12.3 | 11.5 | 11.32 | 38.1% | 23.8% |
| ITF_MEN | 5,837 | 10.9 | 8.0 | 17.5 | 14.9 | 19.9 | 16.3 | 12.5 | 14.52 | 48.7% | 28.8% |
| ITF_WOMEN | 8,102 | 10.3 | 6.7 | 15.9 | 15.4 | 22.2 | 18.2 | 11.3 | 15.69 | 51.7% | 29.5% |
| WTA | 1,146 | 19.8 | 12.2 | 24.2 | 18.1 | 19.6 | 5.2 | 1.0 | 8.18 | 25.7% | 6.1% |
| WTA125 | 651 | 13.2 | 7.5 | 23.8 | 20.1 | 20.0 | 13.4 | 2.0 | 11.08 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,610 | 23.8 | 14.1 | 24.6 | 18.5 | 14.5 | 3.4 | 1.1 | 6.9 | 19.0% | 4.5% |
| CHALLENGER | 3,392 | 14.7 | 8.1 | 19.3 | 13.7 | 17.8 | 14.4 | 12.1 | 12.68 | 44.2% | 26.4% |
| ITF_MEN | 5,837 | 9.3 | 6.7 | 15.7 | 13.6 | 19.8 | 19.4 | 15.4 | 16.96 | 54.7% | 34.9% |
| ITF_WOMEN | 8,102 | 8.5 | 5.7 | 13.7 | 13.2 | 21.1 | 20.8 | 16.9 | 18.91 | 58.8% | 37.7% |
| WTA | 1,146 | 17.4 | 7.8 | 20.2 | 15.7 | 22.6 | 15.2 | 1.1 | 11.64 | 38.8% | 16.2% |
| WTA125 | 651 | 6.6 | 4.8 | 17.2 | 17.7 | 25.8 | 19.1 | 8.9 | 16.74 | 53.8% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,610 | 26.6 | 13.6 | 26.6 | 16.5 | 12.9 | 3.0 | 0.8 | 6.53 | 16.8% | 3.9% |
| CHALLENGER | 3,392 | 14.9 | 10.3 | 20.7 | 15.1 | 15.5 | 11.9 | 11.7 | 11.02 | 39.1% | 23.6% |
| ITF_MEN | 5,837 | 10.0 | 8.1 | 17.9 | 14.2 | 20.6 | 16.7 | 12.5 | 14.97 | 49.9% | 29.2% |
| ITF_WOMEN | 8,102 | 9.7 | 6.9 | 16.4 | 15.5 | 22.9 | 18.2 | 10.4 | 15.57 | 51.5% | 28.6% |
| WTA | 1,146 | 23.2 | 16.3 | 31.5 | 15.3 | 11.0 | 2.1 | 0.6 | 6.07 | 13.7% | 2.7% |
| WTA125 | 651 | 22.4 | 12.3 | 29.5 | 15.7 | 14.0 | 5.8 | 0.3 | 7.73 | 20.1% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 985 | 28.6 | 20.4 | 32.7 | 11.8 | 4.6 | 1.8 | 0.1 | 5.03 | 6.5% | 1.9% |
| CHALLENGER | 2,337 | 22.5 | 15.2 | 27.6 | 14.3 | 13.2 | 5.2 | 2.0 | 6.93 | 20.4% | 7.2% |
| DOUBLES | 1,169 | 5.0 | 3.9 | 10.6 | 10.9 | 20.6 | 25.5 | 23.4 | 24.18 | 69.5% | 48.9% |
| ITF_MEN | 4,900 | 14.6 | 8.6 | 20.7 | 15.7 | 20.8 | 12.5 | 7.0 | 11.86 | 40.4% | 19.5% |
| ITF_WOMEN | 5,379 | 11.8 | 9.1 | 19.1 | 14.8 | 22.3 | 16.8 | 6.2 | 13.18 | 45.2% | 22.9% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 836 | 21.1 | 16.6 | 29.4 | 17.1 | 11.1 | 4.3 | 0.4 | 7.01 | 15.8% | 4.7% |
| WTA125 | 723 | 21.4 | 13.8 | 22.3 | 18.4 | 14.1 | 7.9 | 2.1 | 8.14 | 24.1% | 10.0% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,578 | 29.8 | 14.0 | 24.9 | 17.2 | 11.3 | 2.1 | 0.8 | 5.98 | 14.1% | 2.9% |
| CHALLENGER | 2,417 | 20.6 | 12.7 | 25.4 | 18.1 | 14.8 | 5.9 | 2.3 | 8.15 | 23.1% | 8.2% |
| ITF_MEN | 4,228 | 13.5 | 10.0 | 20.9 | 16.8 | 20.1 | 13.2 | 5.6 | 11.54 | 38.9% | 18.8% |
| ITF_WOMEN | 6,028 | 12.2 | 8.0 | 18.1 | 17.6 | 23.7 | 15.3 | 5.1 | 13.3 | 44.1% | 20.4% |
| WTA | 1,124 | 19.9 | 11.7 | 24.5 | 18.2 | 19.7 | 5.1 | 1.0 | 8.2 | 25.7% | 6.0% |
| WTA125 | 625 | 13.6 | 7.4 | 23.4 | 20.5 | 20.6 | 13.0 | 1.6 | 11.2 | 35.2% | 14.6% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,578 | 23.9 | 14.3 | 24.6 | 18.6 | 14.4 | 3.2 | 0.9 | 6.9 | 18.6% | 4.2% |
| CHALLENGER | 2,417 | 18.8 | 10.5 | 24.2 | 16.4 | 18.1 | 9.5 | 2.5 | 9.07 | 30.1% | 12.0% |
| ITF_MEN | 4,229 | 11.0 | 8.0 | 18.2 | 15.4 | 21.9 | 17.1 | 8.4 | 14.12 | 47.4% | 25.5% |
| ITF_WOMEN | 6,028 | 9.6 | 6.5 | 15.3 | 14.6 | 23.1 | 20.2 | 10.7 | 16.52 | 54.0% | 30.9% |
| WTA | 1,124 | 17.3 | 7.7 | 20.2 | 15.8 | 22.7 | 15.3 | 1.1 | 11.72 | 39.1% | 16.4% |
| WTA125 | 625 | 6.4 | 5.0 | 17.3 | 18.1 | 25.8 | 19.5 | 8.0 | 16.64 | 53.3% | 27.5% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 955 | 28.8 | 20.6 | 33.1 | 11.9 | 3.9 | 1.6 | 0.1 | 5.02 | 5.5% | 1.7% |
| CHALLENGER | 2,014 | 24.3 | 16.5 | 29.6 | 14.1 | 12.4 | 2.5 | 0.7 | 6.31 | 15.5% | 3.1% |
| DOUBLES | 1,078 | 5.1 | 4.0 | 10.8 | 11.1 | 20.4 | 25.7 | 22.8 | 24.07 | 68.9% | 48.5% |
| ITF_MEN | 4,050 | 16.1 | 9.4 | 22.6 | 16.6 | 20.6 | 10.6 | 4.2 | 10.61 | 35.4% | 14.8% |
| ITF_WOMEN | 4,425 | 12.8 | 9.8 | 20.8 | 15.7 | 22.5 | 15.2 | 3.3 | 11.84 | 41.0% | 18.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 799 | 21.4 | 17.1 | 29.7 | 17.1 | 11.3 | 3.4 | 0.0 | 6.82 | 14.6% | 3.4% |
| WTA125 | 613 | 23.5 | 15.3 | 23.8 | 19.9 | 12.4 | 4.7 | 0.3 | 7.2 | 17.5% | 5.1% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,169 | 5.0 | 3.9 | 10.6 | 10.9 | 20.6 | 25.5 | 23.4 | 24.18 | 69.5% | 48.9% |
| singles | 15,309 | 16.4 | 11.2 | 22.6 | 15.1 | 18.2 | 11.4 | 4.9 | 9.91 | 34.5% | 16.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 4,822 | 13.2 | 8.9 | 19.2 | 15.7 | 18.1 | 14.6 | 10.2 | 12.79 | 43.0% | 24.8% |
| Grass | 235 | 11.1 | 11.1 | 17.9 | 13.6 | 23.8 | 14.9 | 7.7 | 14.16 | 46.4% | 22.6% |
| Hard | 13,436 | 13.9 | 8.5 | 18.4 | 15.4 | 19.5 | 14.4 | 9.8 | 12.98 | 43.8% | 24.2% |
| UNKNOWN | 2,245 | 12.1 | 7.3 | 16.9 | 18.1 | 19.0 | 15.9 | 10.8 | 13.49 | 45.7% | 26.7% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,114 | 19.7 | 10.8 | 21.1 | 17.3 | 15.7 | 8.9 | 6.5 | 9.49 | 31.1% | 15.4% |
| B | 2,711 | 13.5 | 9.1 | 19.7 | 16.4 | 18.4 | 12.1 | 10.8 | 12.14 | 41.3% | 22.9% |
| C | 3,015 | 12.7 | 9.6 | 19.8 | 13.9 | 19.0 | 14.9 | 10.2 | 12.77 | 44.1% | 25.1% |
| D | 3,477 | 11.8 | 7.9 | 17.3 | 15.7 | 21.9 | 15.4 | 9.9 | 13.97 | 47.2% | 25.3% |
| F | 5,421 | 8.1 | 5.4 | 14.7 | 14.8 | 21.9 | 21.6 | 13.5 | 17.98 | 57.0% | 35.1% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,908 | 23.0 | 15.9 | 29.0 | 15.2 | 11.1 | 4.2 | 1.5 | 6.68 | 16.8% | 5.7% |
| B | 2,402 | 15.0 | 10.1 | 23.9 | 16.5 | 19.3 | 10.9 | 4.2 | 10.17 | 34.4% | 15.1% |
| C | 3,273 | 11.8 | 7.6 | 17.6 | 14.4 | 21.3 | 16.2 | 11.1 | 14.25 | 48.5% | 27.3% |
| D | 2,392 | 14.1 | 9.7 | 20.5 | 13.8 | 21.1 | 14.0 | 6.8 | 12.01 | 41.9% | 20.8% |
| F | 3,503 | 10.3 | 7.5 | 15.0 | 14.1 | 23.4 | 20.5 | 9.1 | 16.33 | 53.0% | 29.7% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 6,931 | 17.9 | 9.7 | 20.3 | 16.9 | 16.3 | 9.8 | 9.0 | 10.55 | 35.1% | 18.8% |
| LIMITED | 4,764 | 14.6 | 10.5 | 20.6 | 15.1 | 18.5 | 13.2 | 7.6 | 11.36 | 39.3% | 20.8% |
| POOR | 9,043 | 9.6 | 6.5 | 15.8 | 15.2 | 21.8 | 19.1 | 12.0 | 16.04 | 52.9% | 31.1% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,788 | 28.5 | 22.7 | 35.2 | 9.5 | 2.8 | 1.1 | 0.2 | 4.88 | 4.1% | 1.3% |
| GAME_SPREAD | 3,325 | 24.8 | 15.6 | 35.4 | 17.7 | 5.3 | 0.9 | 0.2 | 6.18 | 6.5% | 1.1% |
| MATCH_WINNER | 16,478 | 15.6 | 10.7 | 21.8 | 14.8 | 18.4 | 12.4 | 6.2 | 10.45 | 37.0% | 18.6% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 7,241 | 31.4 | 18.4 | 30.8 | 11.4 | 6.4 | 1.2 | 0.5 | 5.03 | 8.1% | 1.7% |
| TOTAL_GAMES | 5,405 | 6.7 | 8.8 | 37.4 | 28.6 | 11.7 | 3.8 | 3.0 | 9.68 | 18.5% | 6.8% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,687 | 25.1 | 36.3 | 31.2 | 2.6 | 3.8 | 0.7 | 0.2 | 4.39 | 4.8% | 0.9% |
| GAME_SPREAD | 3,944 | 45.6 | 16.6 | 27.9 | 7.5 | 1.4 | 0.7 | 0.3 | 3.48 | 2.4% | 1.0% |
| TOTAL_GAMES | 6,671 | 4.0 | 6.6 | 41.0 | 35.6 | 7.6 | 2.9 | 2.4 | 9.85 | 12.8% | 5.2% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,687 | 25.4 | 17.8 | 36.3 | 10.7 | 6.9 | 2.5 | 0.4 | 5.66 | 9.8% | 2.9% |
| GAME_SPREAD | 3,944 | 19.2 | 13.6 | 29.3 | 20.7 | 13.3 | 3.0 | 0.9 | 7.84 | 17.2% | 3.9% |
| TOTAL_GAMES | 6,680 | 6.8 | 8.8 | 36.7 | 27.6 | 13.4 | 4.2 | 2.6 | 9.75 | 20.1% | 6.8% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 20,738 | 43.8% | 24.6% | 13.01 | 34.9% | 15.2% | 10.69 |
| gen1_elo | 20,738 | 43.2% | 23.9% | 12.53 | 34.0% | 14.8% | 10.15 |
| gen1_sr | 20,738 | 52.3% | 30.8% | 15.86 | 44.4% | 21.3% | 13.18 |
| gen2 | 20,738 | 50.9% | 31.0% | 15.45 | 44.1% | 22.8% | 13.0 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 11,064 | 16.4 | 10.4 | 21.5 | 17.3 | 19.6 | 11.4 | 3.3 | 10.46 | 34.3% | 14.7% |
| STALE | 9,674 | 10.1 | 6.3 | 14.9 | 13.9 | 18.7 | 18.3 | 17.6 | 17.42 | 54.7% | 35.9% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 9,946 | 17.3 | 11.5 | 23.2 | 14.8 | 17.0 | 11.3 | 4.9 | 9.51 | 33.2% | 16.2% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 37,216 | 9946 | 14536 | 12734 | 23.9 | 153.8 | 1400.4 |
| ge_15pp | 15,186 | 3302 | 5085 | 6799 | 26.3 | 459.6 | 1380.4 |
| ge_25pp | 8,176 | 1611 | 2218 | 4347 | 33.9 | 596.1 | 1380.4 |
| lt_10pp | 16,321 | 5167 | 6982 | 4172 | 21.8 | 48.2 | 1341.5 |

Current slate `SL-20261018T012438Z-33317d90`: 988 priced rows, quote age at build {'median': 7.1, 'max': 7.2}, freshness {'FRESH': 988}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 11 | 0.0 | 0.0 | 36.4 | 0.0 | 45.5 | 18.2 | 0.0 | 20.19 | 63.6% | 18.2% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,853 | 21.5 | 10.8 | 22.8 | 18.7 | 18.8 | 6.8 | 0.5 | 8.65 | 26.2% | 7.4% |
| KALSHI_LONE_OUTLIER | 10 | 10.0 | 0.0 | 70.0 | 0.0 | 10.0 | 10.0 | 0.0 | 5.17 | 20.0% | 10.0% |
| MARKETS_AGREE | 330 | 69.1 | 30.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 657 | 0.0 | 3.2 | 35.5 | 28.5 | 23.6 | 8.5 | 0.8 | 11.81 | 32.9% | 9.3% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 20,738 | 2873 (13.9%) | 22.9% | 0.7% | {"EXTERNAL_STALE": 1853, "AGREES_WITH_KALSHI": 657, "ALL_AGREE": 330, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 10, "AGREES_WITH_MODEL": 10, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 9,085 | 710 (7.8%) | 30.4% | 1.3% | {"EXTERNAL_STALE": 485, "AGREES_WITH_KALSHI": 216, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 5,103 | 201 (3.9%) | 30.3% | 1.5% | {"EXTERNAL_STALE": 137, "AGREES_WITH_KALSHI": 61, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,426 | 189 (7.8%) | 31.2% | 1.6% | {"EXTERNAL_STALE": 127, "AGREES_WITH_KALSHI": 59, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 8,385 | 1629 (19.4%) | 15.6% | 0.7% | {"EXTERNAL_STALE": 1021, "ALL_AGREE": 330, "AGREES_WITH_KALSHI": 254, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 8, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 4,004 | 11.3 | 7.7 | 19.3 | 14.8 | 21.8 | 14.7 | 10.5 | 13.84 | 46.9% | 25.1% |
| 4-10x | 2,654 | 12.6 | 8.9 | 19.6 | 15.2 | 19.1 | 15.0 | 9.6 | 12.87 | 43.6% | 24.6% |
| <2x | 10,852 | 15.3 | 9.3 | 18.8 | 16.8 | 17.7 | 13.0 | 9.0 | 11.88 | 39.7% | 22.0% |
| >=10x | 3,228 | 10.8 | 6.3 | 15.0 | 13.8 | 21.2 | 19.8 | 13.1 | 16.54 | 54.0% | 32.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 5,511 | 13.3 | 8.3 | 19.2 | 15.9 | 19.6 | 13.1 | 10.4 | 12.84 | 43.2% | 23.6% |
| 300-1000 | 4,583 | 12.0 | 8.7 | 17.3 | 15.6 | 20.8 | 15.9 | 9.7 | 13.75 | 46.4% | 25.6% |
| <300 | 6,151 | 9.0 | 6.0 | 15.4 | 14.6 | 21.5 | 20.3 | 13.1 | 16.99 | 54.9% | 33.4% |
| >=3000 | 4,493 | 21.4 | 12.0 | 22.7 | 17.2 | 13.9 | 7.2 | 5.5 | 8.3 | 26.7% | 12.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 640 | 0.5384 | 0.4044 | 0.4844 | +0.054 | -0.080 | 0.0017 ± 0.0059 |
| ratio 4-10x | 428 | 0.5842 | 0.4473 | 0.5047 | +0.080 | -0.057 | 0.0087 ± 0.0075 |
| ratio <2x | 1595 | 0.5362 | 0.4149 | 0.4508 | +0.085 | -0.036 | 0.0123 ± 0.0036 |
| ratio >=10x | 519 | 0.5466 | 0.3785 | 0.42 | +0.127 | -0.042 | 0.0166 ± 0.0078 |
| thinner_sample 1000-3000 | 907 | 0.5425 | 0.4172 | 0.462 | +0.081 | -0.045 | 0.0077 ± 0.0047 |
| thinner_sample 300-1000 | 753 | 0.5616 | 0.4225 | 0.4861 | +0.076 | -0.064 | 0.0028 ± 0.0057 |
| thinner_sample <300 | 971 | 0.5428 | 0.3827 | 0.4315 | +0.111 | -0.049 | 0.0173 ± 0.0055 |
| thinner_sample >=3000 | 551 | 0.529 | 0.4361 | 0.4701 | +0.059 | -0.034 | 0.0128 ± 0.0049 |
| data_status ADEQUATE | 943 | 0.5328 | 0.4286 | 0.4602 | +0.072 | -0.032 | 0.01 ± 0.0041 |
| data_status LIMITED | 794 | 0.5517 | 0.4228 | 0.4861 | +0.066 | -0.063 | 0.0043 ± 0.0052 |
| data_status POOR | 1445 | 0.5489 | 0.3935 | 0.445 | +0.104 | -0.051 | 0.014 ± 0.0045 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 494 | 0.1925 | 0.1938 | -0.0014 ± 0.0007 | 0.563 | 0.5658 | 0.4942 | 0.4795 | 0.5304 | -0.042 ± 0.0207 | -0.01 (5) |
| 3-5 | 309 | 0.1951 | 0.1946 | +0.0005 ± 0.002 | 0.5712 | 0.5688 | 0.5059 | 0.466 | 0.479 | -0.079 ± 0.0257 | 0.02 (1) |
| 5-10 | 671 | 0.1978 | 0.1971 | +0.0006 ± 0.0026 | 0.5811 | 0.5776 | 0.5104 | 0.4361 | 0.4635 | -0.083 ± 0.0177 | -0.0167 (6) |
| 10-15 | 561 | 0.2134 | 0.2049 | +0.0086 ± 0.0048 | 0.6154 | 0.5915 | 0.5184 | 0.3945 | 0.4207 | -0.086 ± 0.0191 | -0.048 (5) |
| 15-25 | 693 | 0.2294 | 0.2128 | +0.0166 ± 0.0068 | 0.6533 | 0.6107 | 0.5757 | 0.3808 | 0.4372 | -0.084 ± 0.0175 | -0.0033 (9) |
| 25-40 | 376 | 0.2247 | 0.2073 | +0.0175 ± 0.014 | 0.6386 | 0.5967 | 0.6458 | 0.3371 | 0.4628 | -0.062 ± 0.0215 | -0.01 (1) |
| 40+ | 78 | 0.3044 | 0.1729 | +0.1315 ± 0.0422 | 0.8211 | 0.5186 | 0.7435 | 0.296 | 0.3718 | -0.122 ± 0.0414 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2309 | 0.1801 | 0.1813 | -0.0012 ± 0.0003 | 0.5349 | 0.5363 | 0.4792 | 0.4642 | 0.4998 | -0.019 ± 0.009 | -0.0129 (17) |
| 3-5 | 1441 | 0.193 | 0.191 | +0.0020 ± 0.0009 | 0.5662 | 0.5573 | 0.4796 | 0.4399 | 0.433 | -0.063 ± 0.0117 | 0.0 (2) |
| 5-10 | 3122 | 0.1937 | 0.1913 | +0.0025 ± 0.0012 | 0.5702 | 0.5615 | 0.4822 | 0.4084 | 0.427 | -0.044 ± 0.0079 | -0.0119 (21) |
| 10-15 | 2696 | 0.2012 | 0.1823 | +0.0189 ± 0.0021 | 0.5886 | 0.5366 | 0.4793 | 0.3546 | 0.3416 | -0.075 ± 0.0082 | -0.0281 (16) |
| 15-25 | 3299 | 0.208 | 0.1691 | +0.0389 ± 0.0028 | 0.6079 | 0.5007 | 0.5019 | 0.3057 | 0.3062 | -0.070 ± 0.0071 | -0.0025 (44) |
| 25-40 | 2587 | 0.2216 | 0.1254 | +0.0962 ± 0.0044 | 0.6367 | 0.3872 | 0.528 | 0.2149 | 0.2219 | -0.062 ± 0.0067 | -0.01 (1) |
| 40+ | 1769 | 0.3783 | 0.042 | +0.3363 ± 0.0055 | 0.9846 | 0.1678 | 0.6266 | 0.1052 | 0.0537 | -0.087 ± 0.0045 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 366 | 0.1976 | 0.198 | -0.0004 ± 0.0008 | 0.5765 | 0.5774 | 0.5015 | 0.4863 | 0.5055 | -0.081 ± 0.0245 | -0.01 (3) |
| 3-5 | 255 | 0.2114 | 0.2105 | +0.0009 ± 0.0023 | 0.6054 | 0.6045 | 0.5154 | 0.4755 | 0.4784 | -0.082 ± 0.0304 | 0.02 (1) |
| 5-10 | 583 | 0.1993 | 0.1987 | +0.0006 ± 0.0028 | 0.5822 | 0.5808 | 0.5472 | 0.4724 | 0.506 | -0.071 ± 0.019 | -0.01 (4) |
| 10-15 | 525 | 0.2178 | 0.2099 | +0.0079 ± 0.005 | 0.6236 | 0.6055 | 0.5669 | 0.4425 | 0.4762 | -0.090 ± 0.021 | -0.04 (5) |
| 15-25 | 761 | 0.2284 | 0.2073 | +0.0211 ± 0.0065 | 0.6484 | 0.5968 | 0.5874 | 0.3909 | 0.4389 | -0.088 ± 0.0167 | -0.0133 (9) |
| 25-40 | 502 | 0.2663 | 0.1958 | +0.0705 ± 0.0125 | 0.7431 | 0.5719 | 0.6582 | 0.3434 | 0.3904 | -0.114 ± 0.0196 | -0.0075 (4) |
| 40+ | 190 | 0.3623 | 0.1777 | +0.1846 ± 0.0302 | 1.0059 | 0.5264 | 0.74 | 0.2573 | 0.3211 | -0.069 ± 0.0295 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1945 | 0.1824 | 0.1828 | -0.0003 ± 0.0003 | 0.54 | 0.5406 | 0.502 | 0.4874 | 0.5069 | -0.035 ± 0.01 | -0.0133 (15) |
| 3-5 | 1231 | 0.1936 | 0.1927 | +0.0009 ± 0.001 | 0.5621 | 0.5598 | 0.5145 | 0.4745 | 0.4817 | -0.043 ± 0.0128 | 0.02 (1) |
| 5-10 | 2785 | 0.1924 | 0.1898 | +0.0026 ± 0.0012 | 0.5675 | 0.5583 | 0.5095 | 0.4355 | 0.4567 | -0.039 ± 0.0084 | -0.0117 (6) |
| 10-15 | 2392 | 0.1977 | 0.1868 | +0.0109 ± 0.0022 | 0.5811 | 0.5456 | 0.5189 | 0.3945 | 0.4156 | -0.047 ± 0.009 | -0.0189 (18) |
| 15-25 | 3437 | 0.2165 | 0.1755 | +0.0410 ± 0.0028 | 0.6284 | 0.5183 | 0.5312 | 0.3349 | 0.3317 | -0.076 ± 0.0072 | -0.0086 (42) |
| 25-40 | 3042 | 0.2495 | 0.135 | +0.1145 ± 0.0042 | 0.7056 | 0.4148 | 0.5584 | 0.2426 | 0.2209 | -0.088 ± 0.0067 | -0.0044 (18) |
| 40+ | 2391 | 0.3999 | 0.0656 | +0.3343 ± 0.006 | 1.0543 | 0.2298 | 0.6616 | 0.1246 | 0.0949 | -0.068 ± 0.0051 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 474 | 0.1942 | 0.1965 | -0.0022 ± 0.0007 | 0.5682 | 0.5737 | 0.4972 | 0.482 | 0.5464 | -0.015 ± 0.0208 | -0.0137 (8) |
| 3-5 | 351 | 0.1893 | 0.1874 | +0.0018 ± 0.0019 | 0.5552 | 0.5509 | 0.497 | 0.4574 | 0.4558 | -0.111 ± 0.0243 | 0.0067 (3) |
| 5-10 | 699 | 0.2017 | 0.1976 | +0.0041 ± 0.0025 | 0.5906 | 0.5773 | 0.5029 | 0.4291 | 0.4349 | -0.095 ± 0.0172 | -0.0071 (7) |
| 10-15 | 550 | 0.207 | 0.2054 | +0.0016 ± 0.0048 | 0.6015 | 0.5937 | 0.5373 | 0.4144 | 0.4727 | -0.065 ± 0.0191 | -0.0317 (6) |
| 15-25 | 642 | 0.2351 | 0.209 | +0.0261 ± 0.007 | 0.67 | 0.602 | 0.584 | 0.3907 | 0.419 | -0.109 ± 0.0179 | -0.03 (1) |
| 25-40 | 391 | 0.2118 | 0.2131 | -0.0012 ± 0.0136 | 0.6106 | 0.6097 | 0.6515 | 0.3422 | 0.4962 | -0.043 ± 0.0209 | 0.015 (2) |
| 40+ | 75 | 0.3237 | 0.1866 | +0.1371 ± 0.045 | 0.8679 | 0.5501 | 0.7473 | 0.2945 | 0.3733 | -0.107 ± 0.0471 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2200 | 0.1855 | 0.1863 | -0.0008 ± 0.0003 | 0.5474 | 0.5489 | 0.4844 | 0.4691 | 0.4936 | -0.027 ± 0.0093 | -0.0163 (35) |
| 3-5 | 1512 | 0.1875 | 0.1839 | +0.0035 ± 0.0009 | 0.5524 | 0.5439 | 0.4764 | 0.4369 | 0.4127 | -0.086 ± 0.0113 | -0.0094 (18) |
| 5-10 | 3310 | 0.1948 | 0.1885 | +0.0063 ± 0.0011 | 0.5748 | 0.5535 | 0.4807 | 0.4067 | 0.3988 | -0.067 ± 0.0076 | -0.01 (31) |
| 10-15 | 2559 | 0.1958 | 0.1804 | +0.0153 ± 0.0021 | 0.5761 | 0.5301 | 0.4964 | 0.373 | 0.3732 | -0.065 ± 0.0083 | -0.015 (12) |
| 15-25 | 3412 | 0.2075 | 0.1677 | +0.0397 ± 0.0027 | 0.6086 | 0.498 | 0.5044 | 0.3093 | 0.306 | -0.071 ± 0.007 | -0.03 (2) |
| 25-40 | 2537 | 0.2173 | 0.1237 | +0.0936 ± 0.0044 | 0.627 | 0.3815 | 0.5255 | 0.2095 | 0.2235 | -0.059 ± 0.0067 | 0.01 (3) |
| 40+ | 1693 | 0.3942 | 0.0461 | +0.3481 ± 0.0059 | 1.0278 | 0.1789 | 0.6382 | 0.1097 | 0.0561 | -0.089 ± 0.005 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 822 | 0.195 | 0.1952 | -0.0001 ± 0.0005 | 0.5704 | 0.5705 | 0.5076 | 0.4926 | 0.4964 | -0.051 ± 0.0154 | -0.0224 (49) |
| 3-5 | 577 | 0.1948 | 0.1939 | +0.0010 ± 0.0015 | 0.5679 | 0.5645 | 0.4795 | 0.4397 | 0.4454 | -0.052 ± 0.0185 | -0.0194 (34) |
| 5-10 | 1211 | 0.1975 | 0.1917 | +0.0058 ± 0.0019 | 0.5823 | 0.5653 | 0.4878 | 0.4143 | 0.4129 | -0.063 ± 0.0128 | -0.005 (78) |
| 10-15 | 770 | 0.2074 | 0.1964 | +0.0110 ± 0.004 | 0.6032 | 0.5744 | 0.5072 | 0.3842 | 0.4 | -0.054 ± 0.0161 | 0.0014 (64) |
| 15-25 | 1022 | 0.2336 | 0.2119 | +0.0217 ± 0.0057 | 0.6656 | 0.6098 | 0.5659 | 0.371 | 0.4139 | -0.056 ± 0.0144 | -0.0214 (59) |
| 25-40 | 589 | 0.248 | 0.1955 | +0.0525 ± 0.0112 | 0.7003 | 0.5686 | 0.6478 | 0.3358 | 0.4058 | -0.079 ± 0.0169 | -0.0219 (26) |
| 40+ | 198 | 0.3755 | 0.1901 | +0.1854 ± 0.0316 | 1.081 | 0.5609 | 0.7922 | 0.3012 | 0.3788 | -0.081 ± 0.0284 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2489 | 0.1872 | 0.1873 | -0.0000 ± 0.0003 | 0.5502 | 0.5493 | 0.5039 | 0.4886 | 0.4986 | -0.034 ± 0.0086 | -0.0157 (88) |
| 3-5 | 1692 | 0.1892 | 0.1869 | +0.0023 ± 0.0008 | 0.5535 | 0.5483 | 0.4848 | 0.4452 | 0.4374 | -0.053 ± 0.0106 | -0.0209 (69) |
| 5-10 | 3402 | 0.1938 | 0.1859 | +0.0079 ± 0.0011 | 0.5726 | 0.55 | 0.4824 | 0.4088 | 0.3956 | -0.065 ± 0.0075 | -0.0082 (132) |
| 10-15 | 2315 | 0.2041 | 0.1898 | +0.0143 ± 0.0023 | 0.5961 | 0.558 | 0.5107 | 0.3877 | 0.3914 | -0.055 ± 0.009 | -0.0053 (105) |
| 15-25 | 2881 | 0.229 | 0.1975 | +0.0315 ± 0.0033 | 0.6607 | 0.5745 | 0.5578 | 0.3625 | 0.3811 | -0.059 ± 0.0084 | -0.0253 (107) |
| 25-40 | 1942 | 0.2539 | 0.1685 | +0.0855 ± 0.0059 | 0.7191 | 0.499 | 0.6078 | 0.2937 | 0.3172 | -0.077 ± 0.009 | -0.0229 (51) |
| 40+ | 932 | 0.3875 | 0.13 | +0.2576 ± 0.0126 | 1.0967 | 0.398 | 0.7093 | 0.2029 | 0.2146 | -0.072 ± 0.0112 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3182 | 1.055 ± 0.05 | 1.17 | 0.168 | 0.1711 | 0.2121 | 0.2018 |
| gen2 | 3182 | 0.857 ± 0.045 | 1.127 | 0.1748 | 0.1711 | 0.2304 | 0.2018 |
| gen1_elo | 3182 | 1.04 ± 0.049 | 1.153 | 0.1735 | 0.1715 | 0.211 | 0.2016 |
| gen1_sr | 3182 | 1.054 ± 0.059 | 1.188 | 0.1347 | 0.1728 | 0.2266 | 0.2015 |
| gen1_ledger | 5189 | 0.877 ± 0.034 | 1.078 | 0.1774 | 0.1853 | 0.2179 | 0.1975 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 15,186)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,742 | 24.6% |
| STALE_QUOTE | market_freshness | 3,120 | 20.5% |
| BOOK_QUALITY | execution | 2,833 | 18.7% |
| POOR_DATA | data | 1,648 | 10.8% |
| LIMITED_DATA | data | 1,067 | 7.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 812 | 5.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 731 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 614 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 434 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 185 | 1.2% |

Cause class: coverage 24.6%, market_freshness 20.5%, execution 18.7%, data 17.9%, market_freshness/coverage 8.2%, model_calibration_or_unknown 4.8%, mapping 4.0%, model_calibration 1.2%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.8%, START_UNVERIFIABLE 95.2%, LOW_DATA_QUALITY 69.2%, THIN_PLAYER_HISTORY 57.6%, STALE_PLAYER_DATA 51.9%, STALE_KALSHI_QUOTE 44.8%, MODEL_INTERNAL_DISAGREEMENT 39.9%, ASYMMETRIC_SAMPLE_SIZE 31.9%, WIDE_SPREAD 24.4%, MODEL_HIGH_UNCERTAINTY 17.7%, PLAYER_IDENTITY_RISK 14.5%, LEVEL_TRANSFER_RISK 8.4%, EVENT_MAPPING_RISK 8.2%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 2.1%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 27.1%, POST_SETTLEMENT_OBSERVATION 24.6%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 8,176)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,959 | 36.2% |
| BOOK_QUALITY | execution | 1,494 | 18.3% |
| STALE_QUOTE | market_freshness | 1,469 | 18.0% |
| POOR_DATA | data | 685 | 8.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 436 | 5.3% |
| IDENTITY_AMBIGUOUS | mapping | 355 | 4.3% |
| LIMITED_DATA | data | 315 | 3.9% |
| IN_PLAY_QUOTE | market_freshness/coverage | 268 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 156 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 39 | 0.5% |

Cause class: coverage 36.2%, execution 18.3%, market_freshness 18.0%, data 12.2%, market_freshness/coverage 8.6%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.8%, START_UNVERIFIABLE 97.8%, LOW_DATA_QUALITY 73.0%, THIN_PLAYER_HISTORY 60.1%, STALE_KALSHI_QUOTE 53.2%, STALE_PLAYER_DATA 47.2%, MODEL_INTERNAL_DISAGREEMENT 40.9%, ASYMMETRIC_SAMPLE_SIZE 33.8%, WIDE_SPREAD 24.3%, MODEL_HIGH_UNCERTAINTY 18.1%, PLAYER_IDENTITY_RISK 17.8%, EVENT_MAPPING_RISK 9.9%, LOW_DISPLAYED_LIQUIDITY 7.9%, LEVEL_TRANSFER_RISK 7.5%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 1.1%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 39.0%, POST_SETTLEMENT_OBSERVATION 36.2%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 6509, "IDENTITY_AMBIGUOUS": 1667}; ticker orientation: {"VERIFIED": 8176}.

Checks: discipline:AMBIGUOUS 572, discipline:PASS 7604, identity_confidence:AMBIGUOUS 1457, identity_confidence:PASS 6719, level_mapping:NA 584, level_mapping:PASS 7592, market_pair:AMBIGUOUS 294, market_pair:NA 207, market_pair:PASS 7675, model_complement:NA 174, model_complement:PASS 8002, namesake:PASS 8176, physical_match_id:NA 3073, physical_match_id:PASS 5103, player_ids:PASS 8176, same_pair_other_event:PASS 8176, ticker_orientation:PASS 8176

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,595 | 2.7% | 2.4% | 0.9% | {"market_freshness": 30, "data": 16, "execution": 13, "market_freshness/coverage": 8, "model_calibration_or_unknown": 2, "coverage": 2} | 5.49 | 0.2088 / 0.2068 (295) | 16.3% | 2.2% | 4.7% | 2.4% |
| CHALLENGER | 5,729 | 17.0% | 5.9% | 11.9% | {"coverage": 588, "market_freshness/coverage": 125, "market_freshness": 117, "data": 67, "model_calibration_or_unknown": 46, "execution": 17, "model_calibration": 9, "mapping": 6} | 7.08 | 0.217 / 0.2049 (1485) | 36.7% | 10.2% | 2.4% | 22.7% |
| DOUBLES | 1,169 | 48.9% | 48.5% | 7.0% | {"execution": 253, "mapping": 164, "market_freshness": 106, "market_freshness/coverage": 42, "coverage": 7} | 24.07 | 0.3231 / 0.2339 (333) | 20.0% | 0.0% | 100.0% | 7.8% |
| ITF_MEN | 10,737 | 24.6% | 16.8% | 32.3% | {"coverage": 1040, "execution": 532, "market_freshness": 406, "data": 357, "market_freshness/coverage": 209, "mapping": 94, "model_calibration_or_unknown": 2} | 11.12 | 0.2135 / 0.194 (2622) | 36.4% | 61.5% | 12.8% | 22.9% |
| ITF_WOMEN | 13,481 | 26.9% | 19.6% | 44.3% | {"coverage": 1305, "market_freshness": 735, "execution": 650, "data": 526, "market_freshness/coverage": 271, "mapping": 85, "model_calibration_or_unknown": 43, "model_calibration": 10} | 12.72 | 0.2032 / 0.1913 (2773) | 39.0% | 56.9% | 10.2% | 22.5% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,982 | 5.5% | 4.9% | 1.3% | {"market_freshness": 36, "model_calibration_or_unknown": 23, "execution": 15, "data": 11, "market_freshness/coverage": 10, "model_calibration": 9, "coverage": 4, "mapping": 1} | 7.64 | 0.2355 / 0.2312 (339) | 23.1% | 1.7% | 1.8% | 3.0% |
| WTA125 | 1,374 | 12.5% | 9.8% | 2.1% | {"model_calibration_or_unknown": 38, "market_freshness/coverage": 38, "market_freshness": 37, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.2185 / 0.2069 (482) | 22.9% | 7.4% | 5.0% | 9.9% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 5 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 6 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 7 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 207 min (STALE); no external reference |
| 9 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 10 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 11 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 12 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 13 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 14 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 15 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 16 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 17 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 18 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 19 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 20 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 22 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 23 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 24 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 25 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 26 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 27 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 28 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 29 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 30 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 31 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 32 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 33 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 34 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 35 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 765 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 36 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 37 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 38 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 33 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 39 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 40 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 41 | `KXITFWMATCH-26OCT16ESTLAB-LAB` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 68 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1475.0, ratio 2.28); no external reference |
| 42 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 43 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 44 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 45 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 624 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 46 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 47 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 48 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 49 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 50 | `KXATPCHALLENGERMATCH-26OCT13GIUSEA-SEA` | CHALLENGER | fair_v1 | 76% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 757 min (STALE); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9781, "by_level_share_of_ge_25pp": {"ATP": 0.0087, "CHALLENGER": 0.1193, "DOUBLES": 0.07, "ITF_MEN": 0.3229, "ITF_WOMEN": 0.4434, "OTHER": 0.0015, "WTA": 0.0133, "WTA125": 0.021}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5317, "share_primary_cause_market_settled_or_in_play": 0.448, "share_primary_cause_stale_quote_only": 0.1797}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 8176, "identity_ambiguous_share": 0.2039, "ticker_orientation": {"VERIFIED": 8176}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 5103, "with_external": 201, "coverage": 0.0394, "external_status": {"EXTERNAL_STALE": 137, "AGREES_WITH_KALSHI": 61, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 137, "MODEL_LONE_OUTLIER": 61, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3035, "share_external_supports_model": 0.0149}, "pregame_clean_ge_25pp": {"n": 2426, "with_external": 189, "coverage": 0.0779, "external_status": {"EXTERNAL_STALE": 127, "AGREES_WITH_KALSHI": 59, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 127, "MODEL_LONE_OUTLIER": 59, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3122, "share_external_supports_model": 0.0159}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 553.0, "median_sample_ratio": 2.39, "median_min_matches": 21.0, "median_max_days_since_last": 208.0, "share_severe_asymmetry": 0.2066, "data_status": {"POOR": 4365, "LIMITED": 2329, "ADEQUATE": 1482}, "comparison_lt_10pp": {"median_thinner_serve_points": 1841.0, "median_sample_ratio": 1.67, "median_min_matches": 92.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 640, "model_minus_observed": 0.054, "kalshi_minus_observed": -0.08, "brier_diff_model_minus_kalshi": 0.0017}, "4-10x": {"n": 428, "model_minus_observed": 0.0796, "kalshi_minus_observed": -0.0574, "brier_diff_model_minus_kalshi": 0.0087}, "<2x": {"n": 1595, "model_minus_observed": 0.0854, "kalshi_minus_observed": -0.0359, "brier_diff_model_minus_kalshi": 0.0123}, ">=10x": {"n": 519, "model_minus_observed": 0.1265, "kalshi_minus_observed": -0.0415, "brier_diff_model_minus_kalshi": 0.0166}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3182, "model": {"intercept": -0.552, "slope": 0.857, "slope_se": 0.045}, "kalshi_mid_same_rows": {"intercept": 0.22, "slope": 1.127, "slope_se": 0.051}, "mean_extremity_model": 0.1748, "mean_extremity_kalshi": 0.1711, "model_brier": 0.2304, "kalshi_brier": 0.2018, "brier_diff_model_minus_kalshi": 0.0286, "brier_diff_se": 0.0033, "model_logloss": 0.6567, "kalshi_logloss": 0.5856}, "fair_v1": {"n": 3182, "model": {"intercept": -0.413, "slope": 1.055, "slope_se": 0.05}, "kalshi_mid_same_rows": {"intercept": 0.298, "slope": 1.17, "slope_se": 0.052}, "mean_extremity_model": 0.168, "mean_extremity_kalshi": 0.1711, "model_brier": 0.2121, "kalshi_brier": 0.2018, "brier_diff_model_minus_kalshi": 0.0104, "brier_diff_se": 0.0027, "model_logloss": 0.6118, "kalshi_logloss": 0.5854}, "gen1_elo": {"n": 3182, "model": {"intercept": -0.409, "slope": 1.04, "slope_se": 0.049}, "kalshi_mid_same_rows": {"intercept": 0.286, "slope": 1.153, "slope_se": 0.051}, "mean_extremity_model": 0.1735, "mean_extremity_kalshi": 0.1715, "model_brier": 0.211, "kalshi_brier": 0.2016, "brier_diff_model_minus_kalshi": 0.0094, "brier_diff_se": 0.0027, "model_logloss": 0.6103, "kalshi_logloss": 0.585}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2461, "share_ge_15": 0.4381, "median_abs_gap": 13.01, "n": 20738}, "gen1_elo": {"share_ge_25": 0.239, "share_ge_15": 0.4323, "median_abs_gap": 12.53, "n": 20738}, "gen1_sr": {"share_ge_25": 0.3076, "share_ge_15": 0.5227, "median_abs_gap": 15.86, "n": 20738}, "gen2": {"share_ge_25": 0.31, "share_ge_15": 0.5091, "median_abs_gap": 15.45, "n": 20738}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1516, "share_ge_15": 0.3494, "median_abs_gap": 10.69, "n": 16000}, "gen1_elo": {"share_ge_25": 0.1482, "share_ge_15": 0.3395, "median_abs_gap": 10.15, "n": 15999}, "gen1_sr": {"share_ge_25": 0.2134, "share_ge_15": 0.4438, "median_abs_gap": 13.18, "n": 16000}, "gen2": {"share_ge_25": 0.2282, "share_ge_15": 0.4408, "median_abs_gap": 13.0, "n": 16001}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.49, "share_ge_25_all": 0.0274, "share_ge_25_pregame_clean": 0.0241}, "WTA": {"median_abs_gap_pregame_clean": 7.64, "share_ge_25_all": 0.055, "share_ge_25_pregame_clean": 0.0494}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2394, "share_within_10pp_all": 0.4385, "share_within_10pp_pregame_clean": 0.4955, "corr_model_vs_mid_pregame_clean": 0.8419}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 494, "model_brier": 0.1925, "kalshi_brier": 0.1938, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 561, "model_brier": 0.2134, "kalshi_brier": 0.2049, "brier_diff_model_minus_kalshi": 0.0086}, "15-25": {"n_settled": 693, "model_brier": 0.2294, "kalshi_brier": 0.2128, "brier_diff_model_minus_kalshi": 0.0166}, "25-40": {"n_settled": 376, "model_brier": 0.2247, "kalshi_brier": 0.2073, "brier_diff_model_minus_kalshi": 0.0175}, "3-5": {"n_settled": 309, "model_brier": 0.1951, "kalshi_brier": 0.1946, "brier_diff_model_minus_kalshi": 0.0005}, "40+": {"n_settled": 78, "model_brier": 0.3044, "kalshi_brier": 0.1729, "brier_diff_model_minus_kalshi": 0.1315}, "5-10": {"n_settled": 671, "model_brier": 0.1978, "kalshi_brier": 0.1971, "brier_diff_model_minus_kalshi": 0.0006}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.552, "slope": 0.857, "slope_se": 0.045}, "kalshi_slope": {"intercept": 0.22, "slope": 1.127, "slope_se": 0.051}, "n": 3182}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.517, "slope": 0.877, "slope_se": 0.034}, "kalshi_slope": {"intercept": 0.14, "slope": 1.078, "slope_se": 0.038}, "n": 5189}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 333, "model_brier": 0.3231, "kalshi_brier": 0.2339, "brier_diff_model_minus_kalshi": 0.0893, "brier_diff_se": 0.0172, "corr_model_outcome": 0.0123, "corr_kalshi_outcome": 0.26}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
