# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-15T01:59Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 33,289): 0-3 14.4%, 3-5 9.5%, 5-10 20.1%, 10-15 15.3%, 15-25 18.8%, 25-40 13.6%, 40+ 8.2%; median gap 11.83 pp.
* **Where the extremes live**: 98.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.6%, Challenger 12.3%, doubles 7.0%). Main tour: ATP 1.4% and WTA 6.2% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 7,250): MARKET_ALREADY_SETTLED_WHEN_PRICED 37.6%, BOOK_QUALITY 17.6%, STALE_QUOTE 16.8%, POOR_DATA 8.3%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IDENTITY_AMBIGUOUS 4.4%, LIMITED_DATA 4.0%, IN_PLAY_QUOTE 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.4%. By class: coverage 37.6%, execution 17.6%, market_freshness 16.8%, data 12.4%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 1.9%, model_calibration 0.4%.
* **Stale / settled / in-play**: 53.4% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 46.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 7,250 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.8% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 3.5%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 21.6% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 556.0 points vs 1797.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.056, Gen-2 0.862, Gen-1 ledger 0.868 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 343 model 0.2273 vs Kalshi 0.2081; n 72 model 0.29 vs Kalshi 0.1741.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 131,915 model-market comparisons (219,077 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 47,068 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-15T01:51:23.555301+00:00'], shadow board 36,302 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-15T01:51:27.559828+00:00'], Model 4 14,179 rows, 14,465 settled tickers, 4,612 tickers with an external scan.
* By model: {"gen1_ledger": 30908, "gen1_elo": 18244, "fair_v1": 18244, "gen2": 18244, "gen1_sr": 18244, "model4_fundamental": 14020, "model4_conditioned": 14011}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 33,289 | 14.4 | 9.5 | 20.1 | 15.3 | 18.8 | 13.6 | 8.2 | 11.83 | 40.6% | 21.8% |
| MW fair_v1 | 18,244 | 13.6 | 8.5 | 18.6 | 15.9 | 19.2 | 14.5 | 9.7 | 12.91 | 43.4% | 24.2% |
| MW gen1_elo | 18,244 | 13.2 | 9.0 | 19.9 | 15.2 | 19.0 | 14.3 | 9.4 | 12.42 | 42.7% | 23.7% |
| MW gen1_ledger | 15,045 | 15.5 | 10.7 | 21.9 | 14.6 | 18.4 | 12.4 | 6.3 | 10.45 | 37.2% | 18.8% |
| MW gen1_sr | 18,244 | 9.8 | 7.6 | 16.3 | 14.2 | 21.8 | 18.4 | 11.8 | 15.74 | 52.1% | 30.2% |
| MW gen2 | 18,244 | 11.6 | 7.1 | 16.3 | 14.3 | 20.4 | 17.2 | 13.1 | 15.36 | 50.7% | 30.3% |
| all families model4_conditioned | 14,011 | 21.6 | 20.1 | 35.3 | 16.6 | 4.4 | 1.1 | 0.9 | 5.82 | 6.4% | 2.0% |
| all families model4_fundamental | 14,020 | 16.7 | 13.5 | 35.7 | 19.7 | 10.6 | 2.6 | 1.1 | 7.59 | 14.4% | 3.7% |

Configurable thresholds (primary): >=5pp 76.1%, >=10pp 56.0%, >=15pp 40.6%, >=20pp 30.1%, >=25pp 21.8%, >=30pp 15.8%, >=40pp 8.2%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.45pp; >=10pp 45.2%, >=25pp 17.4%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,328 | 30.5 | 14.6 | 25.1 | 17.6 | 10.3 | 1.1 | 0.8 | 5.69 | 12.3% | 2.0% |
| CHALLENGER | 3,119 | 15.5 | 10.0 | 20.1 | 15.8 | 14.8 | 12.1 | 11.7 | 11.62 | 38.6% | 23.8% |
| ITF_MEN | 5,174 | 11.1 | 8.3 | 17.9 | 14.9 | 19.5 | 16.1 | 12.2 | 14.14 | 47.8% | 28.3% |
| ITF_WOMEN | 7,106 | 10.4 | 6.6 | 16.2 | 15.9 | 22.2 | 18.1 | 10.5 | 15.37 | 50.9% | 28.6% |
| WTA | 932 | 21.6 | 10.6 | 24.7 | 15.8 | 20.6 | 5.6 | 1.2 | 8.18 | 27.4% | 6.8% |
| WTA125 | 585 | 13.0 | 7.5 | 22.4 | 21.2 | 20.2 | 13.8 | 1.9 | 11.33 | 35.9% | 15.7% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,328 | 24.7 | 14.5 | 24.6 | 18.9 | 14.5 | 1.9 | 1.0 | 6.58 | 17.3% | 2.9% |
| CHALLENGER | 3,119 | 14.9 | 7.6 | 19.5 | 13.5 | 18.2 | 14.1 | 12.3 | 12.74 | 44.6% | 26.4% |
| ITF_MEN | 5,174 | 9.6 | 6.9 | 16.0 | 14.1 | 20.0 | 18.5 | 14.9 | 16.33 | 53.3% | 33.4% |
| ITF_WOMEN | 7,106 | 8.8 | 5.8 | 13.2 | 13.4 | 22.0 | 20.6 | 16.3 | 18.68 | 58.9% | 36.9% |
| WTA | 932 | 17.7 | 8.1 | 18.6 | 16.4 | 23.2 | 14.9 | 1.2 | 12.1 | 39.3% | 16.1% |
| WTA125 | 585 | 6.2 | 4.4 | 17.3 | 17.6 | 25.6 | 19.5 | 9.4 | 17.24 | 54.5% | 28.9% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,328 | 27.8 | 14.5 | 28.6 | 15.4 | 10.4 | 2.5 | 0.9 | 6.03 | 13.8% | 3.4% |
| CHALLENGER | 3,119 | 14.8 | 10.2 | 20.4 | 15.2 | 15.6 | 11.8 | 12.0 | 11.11 | 39.3% | 23.8% |
| ITF_MEN | 5,174 | 10.2 | 8.1 | 18.6 | 14.2 | 20.2 | 16.4 | 12.3 | 14.52 | 49.0% | 28.8% |
| ITF_WOMEN | 7,106 | 10.0 | 6.8 | 16.6 | 15.9 | 22.8 | 18.4 | 9.5 | 15.36 | 50.8% | 27.9% |
| WTA | 932 | 22.4 | 15.7 | 32.6 | 15.9 | 10.5 | 2.1 | 0.8 | 6.12 | 13.4% | 2.9% |
| WTA125 | 585 | 22.4 | 12.5 | 29.4 | 15.0 | 14.2 | 6.2 | 0.3 | 7.52 | 20.7% | 6.5% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 725 | 31.2 | 22.6 | 35.5 | 9.1 | 1.2 | 0.4 | 0.0 | 4.69 | 1.7% | 0.4% |
| CHALLENGER | 2,133 | 22.1 | 15.5 | 27.5 | 14.9 | 13.0 | 5.0 | 2.0 | 6.98 | 20.0% | 7.0% |
| DOUBLES | 1,010 | 5.2 | 3.7 | 11.7 | 10.7 | 18.8 | 24.4 | 25.6 | 24.98 | 68.8% | 50.0% |
| ITF_MEN | 4,628 | 14.7 | 8.5 | 20.8 | 15.4 | 20.7 | 12.5 | 7.4 | 11.86 | 40.6% | 19.9% |
| ITF_WOMEN | 5,071 | 11.7 | 9.3 | 19.6 | 14.7 | 22.3 | 16.6 | 5.7 | 13.01 | 44.7% | 22.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 653 | 21.3 | 15.3 | 27.3 | 17.1 | 13.6 | 4.9 | 0.5 | 7.52 | 19.0% | 5.4% |
| WTA125 | 676 | 20.6 | 13.6 | 22.6 | 18.5 | 14.3 | 8.1 | 2.2 | 8.25 | 24.7% | 10.4% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,314 | 30.4 | 14.5 | 25.3 | 17.6 | 10.3 | 1.1 | 0.8 | 5.75 | 12.2% | 1.9% |
| CHALLENGER | 2,227 | 20.1 | 12.5 | 25.3 | 18.5 | 15.3 | 5.9 | 2.4 | 8.33 | 23.6% | 8.3% |
| ITF_MEN | 3,733 | 13.8 | 10.3 | 21.4 | 16.7 | 19.9 | 12.8 | 5.3 | 11.23 | 37.9% | 18.1% |
| ITF_WOMEN | 5,216 | 12.6 | 8.1 | 18.6 | 18.3 | 23.7 | 14.8 | 3.9 | 12.81 | 42.4% | 18.7% |
| WTA | 916 | 21.7 | 9.9 | 25.1 | 15.9 | 20.6 | 5.5 | 1.2 | 8.2 | 27.3% | 6.7% |
| WTA125 | 561 | 13.4 | 7.3 | 21.8 | 21.6 | 20.9 | 13.7 | 1.4 | 11.33 | 36.0% | 15.2% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,314 | 24.6 | 14.5 | 24.7 | 18.9 | 14.5 | 1.8 | 1.0 | 6.58 | 17.3% | 2.8% |
| CHALLENGER | 2,227 | 19.1 | 9.7 | 24.2 | 16.3 | 18.5 | 9.6 | 2.6 | 9.13 | 30.7% | 12.2% |
| ITF_MEN | 3,734 | 11.6 | 8.2 | 18.4 | 16.0 | 22.0 | 15.8 | 8.0 | 13.57 | 45.8% | 23.8% |
| ITF_WOMEN | 5,216 | 10.1 | 6.7 | 14.9 | 14.7 | 24.2 | 19.4 | 10.0 | 16.26 | 53.6% | 29.4% |
| WTA | 916 | 17.6 | 7.9 | 18.6 | 16.7 | 23.1 | 15.0 | 1.2 | 12.18 | 39.3% | 16.2% |
| WTA125 | 561 | 5.9 | 4.6 | 17.3 | 18.0 | 25.5 | 20.1 | 8.6 | 17.24 | 54.2% | 28.7% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 705 | 31.2 | 22.8 | 35.7 | 9.2 | 0.6 | 0.4 | 0.0 | 4.68 | 1.0% | 0.4% |
| CHALLENGER | 1,838 | 23.9 | 16.8 | 29.6 | 14.6 | 12.1 | 2.3 | 0.5 | 6.36 | 15.0% | 2.8% |
| DOUBLES | 931 | 5.3 | 3.8 | 12.0 | 10.7 | 18.9 | 24.3 | 25.0 | 24.29 | 68.2% | 49.3% |
| ITF_MEN | 3,804 | 16.2 | 9.3 | 22.8 | 16.2 | 20.6 | 10.5 | 4.4 | 10.51 | 35.5% | 14.9% |
| ITF_WOMEN | 4,141 | 12.9 | 10.1 | 21.4 | 15.5 | 22.6 | 15.0 | 2.6 | 11.56 | 40.1% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 619 | 21.8 | 16.0 | 27.5 | 17.1 | 13.9 | 3.7 | 0.0 | 7.21 | 17.6% | 3.7% |
| WTA125 | 572 | 22.6 | 15.0 | 24.1 | 20.1 | 12.8 | 5.1 | 0.3 | 7.33 | 18.2% | 5.4% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,010 | 5.2 | 3.7 | 11.7 | 10.7 | 18.8 | 24.4 | 25.6 | 24.98 | 68.8% | 50.0% |
| singles | 14,035 | 16.2 | 11.2 | 22.7 | 14.9 | 18.4 | 11.6 | 5.0 | 9.95 | 35.0% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 4,271 | 13.2 | 9.0 | 19.6 | 16.0 | 18.0 | 14.3 | 9.8 | 12.64 | 42.2% | 24.1% |
| Grass | 183 | 12.0 | 12.0 | 15.3 | 15.3 | 21.3 | 18.0 | 6.0 | 14.16 | 45.4% | 24.0% |
| Hard | 11,914 | 14.0 | 8.4 | 18.6 | 15.4 | 19.6 | 14.3 | 9.7 | 12.85 | 43.5% | 24.0% |
| UNKNOWN | 1,876 | 12.0 | 7.3 | 16.7 | 18.7 | 19.2 | 15.9 | 10.2 | 13.45 | 45.3% | 26.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,383 | 19.7 | 10.7 | 20.9 | 16.9 | 15.9 | 8.8 | 7.0 | 9.56 | 31.7% | 15.8% |
| B | 2,380 | 14.4 | 9.0 | 20.1 | 16.6 | 18.1 | 12.1 | 9.5 | 11.51 | 39.8% | 21.6% |
| C | 2,625 | 13.0 | 9.5 | 19.9 | 14.7 | 19.4 | 14.2 | 9.3 | 12.59 | 43.0% | 23.5% |
| D | 3,186 | 11.3 | 8.0 | 17.8 | 16.0 | 22.0 | 15.4 | 9.3 | 13.82 | 46.8% | 24.8% |
| F | 4,670 | 8.0 | 5.3 | 15.0 | 15.0 | 21.5 | 21.8 | 13.5 | 17.94 | 56.7% | 35.3% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,354 | 22.8 | 15.8 | 28.9 | 15.1 | 11.3 | 4.4 | 1.6 | 6.7 | 17.4% | 6.1% |
| B | 2,265 | 14.8 | 10.0 | 24.1 | 16.4 | 19.5 | 11.0 | 4.2 | 10.19 | 34.7% | 15.2% |
| C | 2,975 | 12.2 | 7.8 | 18.4 | 14.1 | 20.2 | 15.7 | 11.6 | 13.64 | 47.6% | 27.3% |
| D | 2,271 | 14.0 | 9.8 | 20.7 | 13.7 | 21.3 | 13.9 | 6.6 | 11.86 | 41.8% | 20.5% |
| F | 3,180 | 10.1 | 7.5 | 15.2 | 13.9 | 23.7 | 20.4 | 9.2 | 16.38 | 53.2% | 29.5% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 6,019 | 18.1 | 9.7 | 20.2 | 16.7 | 16.2 | 9.9 | 9.1 | 10.51 | 35.3% | 19.0% |
| LIMITED | 4,277 | 15.1 | 10.4 | 20.9 | 15.6 | 18.7 | 12.5 | 6.9 | 11.09 | 38.1% | 19.4% |
| POOR | 7,948 | 9.4 | 6.5 | 16.2 | 15.4 | 21.6 | 19.1 | 11.7 | 15.92 | 52.5% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,030 | 31.2 | 24.5 | 36.4 | 5.5 | 1.8 | 0.7 | 0.1 | 4.49 | 2.5% | 0.7% |
| GAME_SPREAD | 2,885 | 25.8 | 16.0 | 36.7 | 16.8 | 4.1 | 0.4 | 0.2 | 5.99 | 4.7% | 0.6% |
| MATCH_WINNER | 15,045 | 15.5 | 10.7 | 21.9 | 14.6 | 18.4 | 12.4 | 6.3 | 10.45 | 37.2% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 5,513 | 33.5 | 19.5 | 31.0 | 9.6 | 5.1 | 1.1 | 0.2 | 4.72 | 6.4% | 1.4% |
| TOTAL_GAMES | 4,411 | 6.7 | 9.2 | 39.2 | 29.5 | 10.4 | 2.7 | 2.3 | 9.45 | 15.4% | 5.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,905 | 25.6 | 38.2 | 31.5 | 0.3 | 3.9 | 0.4 | 0.1 | 4.3 | 4.4% | 0.5% |
| GAME_SPREAD | 3,498 | 45.3 | 16.4 | 28.8 | 7.3 | 1.1 | 0.7 | 0.4 | 3.56 | 2.2% | 1.1% |
| TOTAL_GAMES | 5,608 | 3.5 | 6.5 | 42.7 | 36.7 | 6.8 | 1.9 | 1.9 | 9.78 | 10.7% | 3.9% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,905 | 26.4 | 18.8 | 37.1 | 9.1 | 6.2 | 2.1 | 0.3 | 5.47 | 8.6% | 2.4% |
| GAME_SPREAD | 3,498 | 19.4 | 13.5 | 30.3 | 20.9 | 12.9 | 2.3 | 0.7 | 7.75 | 15.9% | 3.0% |
| TOTAL_GAMES | 5,617 | 6.7 | 8.9 | 37.9 | 28.1 | 13.1 | 3.3 | 2.1 | 9.66 | 18.4% | 5.4% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 18,244 | 43.4% | 24.2% | 12.91 | 34.1% | 14.4% | 10.5 |
| gen1_elo | 18,244 | 42.7% | 23.7% | 12.42 | 33.0% | 14.1% | 9.99 |
| gen1_sr | 18,244 | 52.1% | 30.2% | 15.74 | 43.8% | 20.4% | 13.01 |
| gen2 | 18,244 | 50.7% | 30.3% | 15.36 | 43.5% | 21.8% | 12.85 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 9,789 | 16.4 | 10.4 | 21.6 | 17.4 | 19.6 | 11.2 | 3.3 | 10.42 | 34.2% | 14.5% |
| STALE | 8,455 | 10.3 | 6.2 | 15.2 | 14.2 | 18.6 | 18.3 | 17.2 | 17.15 | 54.1% | 35.5% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 8,513 | 17.3 | 11.6 | 23.7 | 14.5 | 16.9 | 11.2 | 4.9 | 9.38 | 32.9% | 16.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 33,289 | 8513 | 13261 | 11515 | 24.2 | 146.2 | 1400.4 |
| ge_15pp | 13,523 | 2802 | 4636 | 6085 | 26.5 | 451.3 | 1380.4 |
| ge_25pp | 7,250 | 1365 | 2014 | 3871 | 34.4 | 582.7 | 1380.4 |
| lt_10pp | 14,663 | 4473 | 6375 | 3815 | 22.6 | 48.8 | 1341.5 |

Current slate `SL-20261015T015947Z-9499ef3c`: 479 priced rows, quote age at build {'median': 8.6, 'max': 8.7}, freshness {'FRESH': 479}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 9 | 0.0 | 0.0 | 33.3 | 0.0 | 44.4 | 22.2 | 0.0 | 20.47 | 66.7% | 22.2% |
| EXTERNAL_LONE_OUTLIER | 11 | 72.7 | 27.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,449 | 21.2 | 10.7 | 22.8 | 18.6 | 19.2 | 6.9 | 0.6 | 8.86 | 26.7% | 7.5% |
| KALSHI_LONE_OUTLIER | 7 | 14.3 | 0.0 | 57.1 | 0.0 | 14.3 | 14.3 | 0.0 | 5.14 | 28.6% | 14.3% |
| MARKETS_AGREE | 253 | 71.9 | 28.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.04 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 476 | 0.0 | 3.8 | 34.2 | 29.8 | 23.5 | 8.0 | 0.6 | 11.66 | 32.1% | 8.6% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 18,244 | 2205 (12.1%) | 21.6% | 0.7% | {"EXTERNAL_STALE": 1449, "AGREES_WITH_KALSHI": 476, "ALL_AGREE": 253, "EXTERNAL_OUTLIER": 11, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 7, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 7,922 | 548 (6.9%) | 27.9% | 1.5% | {"EXTERNAL_STALE": 387, "AGREES_WITH_KALSHI": 153, "SUPPORTS_MODEL_DIRECTION": 6, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 4,423 | 153 (3.5%) | 26.8% | 2.0% | {"EXTERNAL_STALE": 109, "AGREES_WITH_KALSHI": 41, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,006 | 144 (7.2%) | 27.1% | 2.1% | {"EXTERNAL_STALE": 102, "AGREES_WITH_KALSHI": 39, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 7,421 | 1245 (16.8%) | 14.5% | 0.6% | {"EXTERNAL_STALE": 792, "ALL_AGREE": 253, "AGREES_WITH_KALSHI": 181, "EXTERNAL_OUTLIER": 11, "AGREES_WITH_MODEL": 5, "SUPPORTS_MODEL_DIRECTION": 2, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,573 | 11.5 | 8.0 | 20.0 | 14.9 | 21.6 | 14.2 | 9.8 | 13.35 | 45.6% | 24.0% |
| 4-10x | 2,396 | 12.2 | 8.8 | 19.4 | 15.5 | 19.6 | 15.4 | 9.0 | 12.93 | 44.0% | 24.4% |
| <2x | 9,548 | 15.5 | 9.2 | 18.8 | 16.9 | 17.7 | 12.9 | 9.0 | 11.89 | 39.7% | 21.9% |
| >=10x | 2,727 | 10.8 | 6.5 | 15.4 | 14.0 | 20.7 | 19.7 | 12.8 | 16.35 | 53.2% | 32.5% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 4,754 | 13.8 | 8.2 | 19.4 | 16.0 | 19.7 | 12.7 | 10.2 | 12.62 | 42.6% | 22.9% |
| 300-1000 | 4,164 | 12.1 | 8.7 | 17.5 | 16.1 | 21.0 | 15.7 | 8.9 | 13.52 | 45.6% | 24.6% |
| <300 | 5,300 | 8.8 | 6.0 | 15.8 | 14.7 | 21.2 | 20.6 | 12.9 | 16.91 | 54.7% | 33.4% |
| >=3000 | 4,026 | 21.2 | 11.7 | 22.6 | 17.1 | 14.0 | 7.5 | 5.9 | 8.46 | 27.4% | 13.4% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 596 | 0.5383 | 0.4066 | 0.4883 | +0.050 | -0.082 | 0.0 ± 0.006 |
| ratio 4-10x | 399 | 0.5869 | 0.4477 | 0.5138 | +0.073 | -0.066 | 0.0065 ± 0.0078 |
| ratio <2x | 1427 | 0.5376 | 0.4153 | 0.4569 | +0.081 | -0.042 | 0.011 ± 0.0038 |
| ratio >=10x | 472 | 0.548 | 0.3796 | 0.428 | +0.120 | -0.048 | 0.0151 ± 0.0082 |
| thinner_sample 1000-3000 | 805 | 0.5428 | 0.4181 | 0.4758 | +0.067 | -0.058 | 0.0038 ± 0.005 |
| thinner_sample 300-1000 | 708 | 0.5613 | 0.4237 | 0.4873 | +0.074 | -0.064 | 0.0023 ± 0.0058 |
| thinner_sample <300 | 890 | 0.5456 | 0.3844 | 0.4438 | +0.102 | -0.059 | 0.015 ± 0.0058 |
| thinner_sample >=3000 | 491 | 0.5312 | 0.4359 | 0.4623 | +0.069 | -0.026 | 0.0148 ± 0.0053 |
| data_status ADEQUATE | 821 | 0.5338 | 0.4295 | 0.4629 | +0.071 | -0.033 | 0.0084 ± 0.0044 |
| data_status LIMITED | 740 | 0.5518 | 0.4231 | 0.4905 | +0.061 | -0.067 | 0.003 ± 0.0054 |
| data_status POOR | 1333 | 0.5508 | 0.3953 | 0.4554 | +0.095 | -0.060 | 0.0122 ± 0.0046 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 441 | 0.1948 | 0.1963 | -0.0014 ± 0.0007 | 0.5682 | 0.5713 | 0.4921 | 0.4772 | 0.5283 | -0.042 ± 0.022 | -0.01 (3) |
| 3-5 | 286 | 0.1913 | 0.1914 | -0.0002 ± 0.0021 | 0.5627 | 0.5618 | 0.5097 | 0.4699 | 0.4895 | -0.072 ± 0.0264 | 0.02 (1) |
| 5-10 | 608 | 0.1963 | 0.1974 | -0.0012 ± 0.0027 | 0.5776 | 0.5784 | 0.5127 | 0.4381 | 0.4753 | -0.077 ± 0.0187 | -0.0125 (4) |
| 10-15 | 509 | 0.2108 | 0.2028 | +0.0080 ± 0.005 | 0.6089 | 0.5862 | 0.522 | 0.3984 | 0.4263 | -0.087 ± 0.0199 | -0.0633 (3) |
| 15-25 | 635 | 0.2296 | 0.2174 | +0.0122 ± 0.0072 | 0.6542 | 0.6211 | 0.5761 | 0.3812 | 0.4488 | -0.073 ± 0.0184 | -0.0133 (6) |
| 25-40 | 343 | 0.2273 | 0.2081 | +0.0192 ± 0.0147 | 0.6459 | 0.5977 | 0.6445 | 0.3362 | 0.4606 | -0.064 ± 0.0225 | -0.01 (1) |
| 40+ | 72 | 0.29 | 0.1741 | +0.1160 ± 0.0438 | 0.7878 | 0.5206 | 0.7443 | 0.2967 | 0.3889 | -0.113 ± 0.0433 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2055 | 0.1788 | 0.18 | -0.0012 ± 0.0003 | 0.5321 | 0.5336 | 0.4809 | 0.4658 | 0.5041 | -0.018 ± 0.0095 | -0.0188 (8) |
| 3-5 | 1289 | 0.195 | 0.1933 | +0.0017 ± 0.001 | 0.5711 | 0.563 | 0.4824 | 0.4428 | 0.4383 | -0.063 ± 0.0125 | 0.02 (1) |
| 5-10 | 2836 | 0.1931 | 0.1916 | +0.0015 ± 0.0012 | 0.5685 | 0.5621 | 0.4873 | 0.4134 | 0.4369 | -0.042 ± 0.0083 | -0.0082 (17) |
| 10-15 | 2441 | 0.2007 | 0.1823 | +0.0185 ± 0.0022 | 0.5873 | 0.5361 | 0.4799 | 0.3555 | 0.3437 | -0.076 ± 0.0086 | -0.0475 (4) |
| 15-25 | 2966 | 0.2072 | 0.1718 | +0.0354 ± 0.003 | 0.6066 | 0.5068 | 0.5007 | 0.3047 | 0.3142 | -0.063 ± 0.0076 | -0.0048 (29) |
| 25-40 | 2352 | 0.2199 | 0.1261 | +0.0938 ± 0.0046 | 0.6332 | 0.3882 | 0.528 | 0.2148 | 0.2262 | -0.059 ± 0.0071 | -0.01 (1) |
| 40+ | 1589 | 0.3737 | 0.0436 | +0.3300 ± 0.0059 | 0.973 | 0.172 | 0.6255 | 0.1055 | 0.0585 | -0.084 ± 0.0049 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 336 | 0.1981 | 0.1982 | -0.0001 ± 0.0009 | 0.5773 | 0.5777 | 0.5015 | 0.4864 | 0.5 | -0.086 ± 0.0256 | -0.01 (1) |
| 3-5 | 231 | 0.2113 | 0.2104 | +0.0008 ± 0.0025 | 0.605 | 0.6046 | 0.5192 | 0.4792 | 0.4848 | -0.081 ± 0.0317 | 0.02 (1) |
| 5-10 | 523 | 0.1985 | 0.1986 | -0.0002 ± 0.0029 | 0.5802 | 0.5808 | 0.5555 | 0.4807 | 0.5201 | -0.066 ± 0.0203 | -0.01 (4) |
| 10-15 | 472 | 0.2143 | 0.2069 | +0.0074 ± 0.0052 | 0.6152 | 0.5991 | 0.5713 | 0.4469 | 0.4831 | -0.087 ± 0.0217 | -0.05 (4) |
| 15-25 | 705 | 0.2283 | 0.2093 | +0.0190 ± 0.0068 | 0.6483 | 0.6013 | 0.5891 | 0.3922 | 0.4454 | -0.086 ± 0.0175 | -0.01 (5) |
| 25-40 | 452 | 0.2662 | 0.1979 | +0.0683 ± 0.0132 | 0.7456 | 0.5751 | 0.6637 | 0.3492 | 0.4004 | -0.116 ± 0.0208 | -0.025 (2) |
| 40+ | 175 | 0.3551 | 0.1843 | +0.1708 ± 0.0316 | 0.984 | 0.5419 | 0.7418 | 0.2616 | 0.3371 | -0.060 ± 0.0313 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1761 | 0.1828 | 0.1831 | -0.0003 ± 0.0003 | 0.5406 | 0.5412 | 0.4974 | 0.4827 | 0.5054 | -0.033 ± 0.0105 | -0.0217 (6) |
| 3-5 | 1130 | 0.1944 | 0.1937 | +0.0007 ± 0.0011 | 0.5642 | 0.5626 | 0.5171 | 0.4772 | 0.4876 | -0.041 ± 0.0133 | 0.02 (1) |
| 5-10 | 2468 | 0.1918 | 0.1899 | +0.0019 ± 0.0013 | 0.5665 | 0.5586 | 0.5169 | 0.4432 | 0.4688 | -0.037 ± 0.0089 | -0.01 (5) |
| 10-15 | 2166 | 0.1962 | 0.1831 | +0.0131 ± 0.0023 | 0.5778 | 0.5365 | 0.5215 | 0.3971 | 0.4095 | -0.057 ± 0.0093 | -0.02 (14) |
| 15-25 | 3155 | 0.216 | 0.1766 | +0.0394 ± 0.003 | 0.6278 | 0.5209 | 0.5332 | 0.3369 | 0.3379 | -0.074 ± 0.0076 | -0.0026 (27) |
| 25-40 | 2716 | 0.248 | 0.1371 | +0.1109 ± 0.0045 | 0.7038 | 0.4178 | 0.5613 | 0.2449 | 0.2301 | -0.084 ± 0.0071 | -0.015 (6) |
| 40+ | 2132 | 0.3995 | 0.0685 | +0.3310 ± 0.0065 | 1.0479 | 0.2376 | 0.6644 | 0.1274 | 0.1013 | -0.066 ± 0.0055 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 432 | 0.1945 | 0.1972 | -0.0027 ± 0.0008 | 0.569 | 0.5759 | 0.4928 | 0.4776 | 0.5556 | +0.000 ± 0.0216 | -0.0133 (6) |
| 3-5 | 310 | 0.1861 | 0.1841 | +0.0020 ± 0.0019 | 0.5476 | 0.5428 | 0.4913 | 0.4519 | 0.4484 | -0.115 ± 0.0256 | -0.01 (1) |
| 5-10 | 637 | 0.2005 | 0.1981 | +0.0024 ± 0.0027 | 0.5883 | 0.579 | 0.5056 | 0.4319 | 0.449 | -0.088 ± 0.0181 | -0.01 (4) |
| 10-15 | 501 | 0.2085 | 0.2091 | -0.0006 ± 0.005 | 0.6045 | 0.6012 | 0.5397 | 0.4169 | 0.483 | -0.059 ± 0.0202 | -0.044 (5) |
| 15-25 | 587 | 0.235 | 0.2118 | +0.0233 ± 0.0074 | 0.6697 | 0.6081 | 0.5829 | 0.3896 | 0.4259 | -0.103 ± 0.0188 | -0.03 (1) |
| 25-40 | 362 | 0.2116 | 0.2139 | -0.0024 ± 0.0142 | 0.6112 | 0.6112 | 0.6504 | 0.3403 | 0.4972 | -0.039 ± 0.0216 | 0.0 (1) |
| 40+ | 65 | 0.3165 | 0.1747 | +0.1418 ± 0.0472 | 0.8502 | 0.5223 | 0.7504 | 0.2955 | 0.3692 | -0.124 ± 0.0479 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1946 | 0.1864 | 0.1877 | -0.0013 ± 0.0003 | 0.5494 | 0.552 | 0.4862 | 0.4709 | 0.5082 | -0.016 ± 0.0099 | -0.0183 (23) |
| 3-5 | 1364 | 0.1849 | 0.1825 | +0.0025 ± 0.0009 | 0.5462 | 0.5403 | 0.4757 | 0.4364 | 0.426 | -0.073 ± 0.012 | -0.0243 (7) |
| 5-10 | 3013 | 0.1942 | 0.1887 | +0.0054 ± 0.0012 | 0.5726 | 0.5543 | 0.4816 | 0.4078 | 0.4059 | -0.063 ± 0.008 | -0.01 (18) |
| 10-15 | 2324 | 0.1957 | 0.1816 | +0.0141 ± 0.0022 | 0.5758 | 0.5328 | 0.4975 | 0.3743 | 0.3787 | -0.063 ± 0.0088 | -0.03 (9) |
| 15-25 | 3034 | 0.2093 | 0.1709 | +0.0384 ± 0.0029 | 0.6129 | 0.5056 | 0.5043 | 0.309 | 0.3102 | -0.069 ± 0.0075 | -0.03 (2) |
| 25-40 | 2317 | 0.2136 | 0.1248 | +0.0888 ± 0.0046 | 0.619 | 0.3836 | 0.5247 | 0.2091 | 0.2305 | -0.053 ± 0.007 | 0.0 (1) |
| 40+ | 1530 | 0.3874 | 0.0452 | +0.3422 ± 0.0061 | 1.0114 | 0.1765 | 0.6333 | 0.1075 | 0.0562 | -0.087 ± 0.0052 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 754 | 0.1976 | 0.1981 | -0.0005 ± 0.0006 | 0.5761 | 0.5771 | 0.5047 | 0.4897 | 0.504 | -0.040 ± 0.0162 | -0.0226 (46) |
| 3-5 | 540 | 0.1941 | 0.1935 | +0.0006 ± 0.0015 | 0.5668 | 0.5638 | 0.4798 | 0.4399 | 0.45 | -0.046 ± 0.0191 | -0.0058 (33) |
| 5-10 | 1142 | 0.1953 | 0.1899 | +0.0055 ± 0.0019 | 0.5763 | 0.5611 | 0.4866 | 0.4132 | 0.4133 | -0.062 ± 0.0131 | -0.0049 (73) |
| 10-15 | 719 | 0.2072 | 0.1968 | +0.0104 ± 0.0041 | 0.603 | 0.5755 | 0.5013 | 0.3784 | 0.3964 | -0.050 ± 0.0166 | 0.0014 (64) |
| 15-25 | 968 | 0.2316 | 0.2124 | +0.0192 ± 0.0058 | 0.6613 | 0.6108 | 0.5623 | 0.3678 | 0.4163 | -0.048 ± 0.0148 | -0.0216 (58) |
| 25-40 | 556 | 0.2542 | 0.1956 | +0.0586 ± 0.0116 | 0.7154 | 0.5685 | 0.6441 | 0.3314 | 0.3921 | -0.083 ± 0.0175 | -0.0216 (25) |
| 40+ | 192 | 0.3714 | 0.1911 | +0.1803 ± 0.0321 | 1.0746 | 0.5631 | 0.7938 | 0.303 | 0.3854 | -0.079 ± 0.0289 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2268 | 0.1887 | 0.1889 | -0.0002 ± 0.0003 | 0.5529 | 0.5523 | 0.5032 | 0.4878 | 0.5013 | -0.031 ± 0.0091 | -0.0155 (82) |
| 3-5 | 1549 | 0.1882 | 0.1857 | +0.0025 ± 0.0009 | 0.551 | 0.5451 | 0.4872 | 0.4475 | 0.4371 | -0.057 ± 0.011 | -0.0148 (63) |
| 5-10 | 3200 | 0.1924 | 0.185 | +0.0074 ± 0.0011 | 0.569 | 0.5479 | 0.4802 | 0.4066 | 0.3962 | -0.062 ± 0.0077 | -0.0087 (125) |
| 10-15 | 2153 | 0.2037 | 0.1893 | +0.0144 ± 0.0023 | 0.595 | 0.5567 | 0.5085 | 0.3855 | 0.3883 | -0.055 ± 0.0093 | -0.0053 (105) |
| 15-25 | 2707 | 0.2293 | 0.1989 | +0.0303 ± 0.0034 | 0.6617 | 0.5775 | 0.5548 | 0.3598 | 0.3809 | -0.057 ± 0.0086 | -0.0255 (106) |
| 25-40 | 1838 | 0.255 | 0.1689 | +0.0861 ± 0.0061 | 0.7224 | 0.4994 | 0.6065 | 0.2919 | 0.3145 | -0.076 ± 0.0093 | -0.0206 (47) |
| 40+ | 903 | 0.3857 | 0.1288 | +0.2569 ± 0.0128 | 1.0942 | 0.3947 | 0.7091 | 0.2019 | 0.2148 | -0.072 ± 0.0113 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2894 | 1.056 ± 0.052 | 1.172 | 0.1686 | 0.1708 | 0.2114 | 0.2027 |
| gen2 | 2894 | 0.862 ± 0.047 | 1.121 | 0.1778 | 0.1708 | 0.2294 | 0.2025 |
| gen1_elo | 2894 | 1.036 ± 0.051 | 1.16 | 0.1732 | 0.1712 | 0.2105 | 0.2026 |
| gen1_sr | 2894 | 1.066 ± 0.061 | 1.191 | 0.1371 | 0.1727 | 0.2253 | 0.2023 |
| gen1_ledger | 4871 | 0.868 ± 0.035 | 1.078 | 0.1768 | 0.1863 | 0.2182 | 0.1977 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 13,523)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,453 | 25.5% |
| STALE_QUOTE | market_freshness | 2,689 | 19.9% |
| BOOK_QUALITY | execution | 2,455 | 18.1% |
| POOR_DATA | data | 1,496 | 11.1% |
| LIMITED_DATA | data | 989 | 7.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 746 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 647 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 519 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 389 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 140 | 1.0% |

Cause class: coverage 25.5%, market_freshness 19.9%, data 18.4%, execution 18.1%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.8%, mapping 3.8%, model_calibration 1.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.2%, START_UNVERIFIABLE 95.9%, LOW_DATA_QUALITY 69.0%, THIN_PLAYER_HISTORY 57.8%, STALE_PLAYER_DATA 54.1%, STALE_KALSHI_QUOTE 45.0%, MODEL_INTERNAL_DISAGREEMENT 38.9%, ASYMMETRIC_SAMPLE_SIZE 31.7%, WIDE_SPREAD 23.8%, MODEL_HIGH_UNCERTAINTY 16.8%, PLAYER_IDENTITY_RISK 13.6%, LEVEL_TRANSFER_RISK 8.5%, EVENT_MAPPING_RISK 7.9%, LOW_DISPLAYED_LIQUIDITY 7.4%, MODEL_CALIBRATION_OUTLIER 3.5%, EXTERNAL_MARKET_REJECTION 1.7%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 28.0%, POST_SETTLEMENT_OBSERVATION 25.5%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 7,250)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,729 | 37.6% |
| BOOK_QUALITY | execution | 1,277 | 17.6% |
| STALE_QUOTE | market_freshness | 1,217 | 16.8% |
| POOR_DATA | data | 604 | 8.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 403 | 5.6% |
| IDENTITY_AMBIGUOUS | mapping | 317 | 4.4% |
| LIMITED_DATA | data | 293 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 240 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 141 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 29 | 0.4% |

Cause class: coverage 37.6%, execution 17.6%, market_freshness 16.8%, data 12.4%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 1.9%, model_calibration 0.4%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.1%, START_UNVERIFIABLE 98.2%, LOW_DATA_QUALITY 72.7%, THIN_PLAYER_HISTORY 60.1%, STALE_KALSHI_QUOTE 53.4%, STALE_PLAYER_DATA 49.1%, MODEL_INTERNAL_DISAGREEMENT 40.0%, ASYMMETRIC_SAMPLE_SIZE 33.6%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 17.4%, PLAYER_IDENTITY_RISK 17.3%, EVENT_MAPPING_RISK 9.7%, LOW_DISPLAYED_LIQUIDITY 7.7%, LEVEL_TRANSFER_RISK 7.4%, MODEL_CALIBRATION_OUTLIER 4.5%, EXTERNAL_MARKET_REJECTION 0.8%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 40.5%, POST_SETTLEMENT_OBSERVATION 37.6%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 5814, "IDENTITY_AMBIGUOUS": 1436}; ticker orientation: {"VERIFIED": 7250}.

Checks: discipline:AMBIGUOUS 505, discipline:PASS 6745, identity_confidence:AMBIGUOUS 1255, identity_confidence:PASS 5995, level_mapping:NA 517, level_mapping:PASS 6733, market_pair:AMBIGUOUS 256, market_pair:NA 173, market_pair:PASS 6821, model_complement:NA 140, model_complement:PASS 7110, namesake:PASS 7250, physical_match_id:NA 2827, physical_match_id:PASS 4423, player_ids:PASS 7250, same_pair_other_event:PASS 7250, ticker_orientation:PASS 7250

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,053 | 1.4% | 1.4% | 0.4% | {"market_freshness": 20, "execution": 8, "market_freshness/coverage": 1} | 5.24 | 0.2103 / 0.2125 (251) | 16.3% | 0.5% | 5.4% | 1.7% |
| CHALLENGER | 5,252 | 17.0% | 5.8% | 12.3% | {"coverage": 547, "market_freshness": 109, "market_freshness/coverage": 108, "data": 59, "model_calibration_or_unknown": 45, "execution": 13, "mapping": 6, "model_calibration": 5} | 7.24 | 0.2176 / 0.2038 (1368) | 37.6% | 9.0% | 2.4% | 22.6% |
| DOUBLES | 1,010 | 50.0% | 49.3% | 7.0% | {"execution": 202, "mapping": 151, "market_freshness": 106, "market_freshness/coverage": 39, "coverage": 7} | 24.29 | 0.3338 / 0.2309 (297) | 23.2% | 0.0% | 100.0% | 7.8% |
| ITF_MEN | 9,802 | 24.3% | 16.4% | 32.9% | {"coverage": 942, "execution": 497, "market_freshness": 341, "data": 319, "market_freshness/coverage": 201, "mapping": 81, "model_calibration_or_unknown": 2} | 10.94 | 0.2132 / 0.195 (2460) | 36.1% | 59.4% | 10.9% | 23.1% |
| ITF_WOMEN | 12,177 | 26.0% | 18.2% | 43.7% | {"coverage": 1216, "market_freshness": 567, "execution": 536, "data": 485, "market_freshness/coverage": 249, "mapping": 73, "model_calibration_or_unknown": 33, "model_calibration": 10} | 12.35 | 0.2029 / 0.1932 (2632) | 38.4% | 58.0% | 9.8% | 23.2% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,585 | 6.2% | 5.5% | 1.4% | {"market_freshness": 36, "model_calibration_or_unknown": 22, "data": 11, "market_freshness/coverage": 10, "model_calibration": 7, "execution": 7, "coverage": 4, "mapping": 1} | 7.85 | 0.2387 / 0.2306 (279) | 26.2% | 1.3% | 1.7% | 3.1% |
| WTA125 | 1,261 | 12.8% | 10.2% | 2.2% | {"model_calibration_or_unknown": 37, "market_freshness": 36, "market_freshness/coverage": 34, "data": 23, "coverage": 12, "execution": 9, "model_calibration": 7, "mapping": 4} | 9.51 | 0.2156 / 0.207 (436) | 23.2% | 8.1% | 4.3% | 10.2% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 5 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 6 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 7 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 15.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 928 min (STALE); no external reference |
| 8 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 9 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 10 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 11 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 12 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 13 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 14 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 15 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 16 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 17 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 18 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 19 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 20 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 21 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 22 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 23 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 92 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 24 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 25 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 26 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 27 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 28 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 29 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 30 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 31 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 32 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 547 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 33 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 34 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 36 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 37 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 38 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 624 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 39 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 40 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 41 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 42 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 43 | `KXATPCHALLENGERMATCH-26OCT13GIUSEA-SEA` | CHALLENGER | fair_v1 | 76% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 757 min (STALE); no external reference |
| 44 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 189 min (STALE); no external reference |
| 45 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 46 | `KXITFWMATCH-26OCT13MAMSTR-MAM` | ITF_WOMEN | fair_v1 | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 406 min (STALE); data LIMITED (grade C, thinner serve sample 879.0, ratio 2.64); no external reference |
| 47 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 48 | `KXITFMATCH-26OCT13VISMUE-MUE` | ITF_MEN | fair_v1 | 25% / 98% | -74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 617 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 0.0); no external reference |
| 49 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 110 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 50 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9825, "by_level_share_of_ge_25pp": {"ATP": 0.004, "CHALLENGER": 0.123, "DOUBLES": 0.0697, "ITF_MEN": 0.3287, "ITF_WOMEN": 0.4371, "OTHER": 0.0017, "WTA": 0.0135, "WTA125": 0.0223}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5339, "share_primary_cause_market_settled_or_in_play": 0.4651, "share_primary_cause_stale_quote_only": 0.1679}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 7250, "identity_ambiguous_share": 0.1981, "ticker_orientation": {"VERIFIED": 7250}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 4423, "with_external": 153, "coverage": 0.0346, "external_status": {"EXTERNAL_STALE": 109, "AGREES_WITH_KALSHI": 41, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 109, "MODEL_LONE_OUTLIER": 41, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.268, "share_external_supports_model": 0.0196}, "pregame_clean_ge_25pp": {"n": 2006, "with_external": 144, "coverage": 0.0718, "external_status": {"EXTERNAL_STALE": 102, "AGREES_WITH_KALSHI": 39, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 102, "MODEL_LONE_OUTLIER": 39, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2708, "share_external_supports_model": 0.0208}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 556.0, "median_sample_ratio": 2.38, "median_min_matches": 20.0, "median_max_days_since_last": 204.0, "share_severe_asymmetry": 0.1999, "data_status": {"POOR": 3870, "LIMITED": 2070, "ADEQUATE": 1310}, "comparison_lt_10pp": {"median_thinner_serve_points": 1797.0, "median_sample_ratio": 1.69, "median_min_matches": 85.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 596, "model_minus_observed": 0.05, "kalshi_minus_observed": -0.0816, "brier_diff_model_minus_kalshi": 0.0}, "4-10x": {"n": 399, "model_minus_observed": 0.0731, "kalshi_minus_observed": -0.0661, "brier_diff_model_minus_kalshi": 0.0065}, "<2x": {"n": 1427, "model_minus_observed": 0.0807, "kalshi_minus_observed": -0.0417, "brier_diff_model_minus_kalshi": 0.011}, ">=10x": {"n": 472, "model_minus_observed": 0.12, "kalshi_minus_observed": -0.0484, "brier_diff_model_minus_kalshi": 0.0151}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2894, "model": {"intercept": -0.539, "slope": 0.862, "slope_se": 0.047}, "kalshi_mid_same_rows": {"intercept": 0.235, "slope": 1.121, "slope_se": 0.053}, "mean_extremity_model": 0.1778, "mean_extremity_kalshi": 0.1708, "model_brier": 0.2294, "kalshi_brier": 0.2025, "brier_diff_model_minus_kalshi": 0.0269, "brier_diff_se": 0.0035, "model_logloss": 0.6544, "kalshi_logloss": 0.5871}, "fair_v1": {"n": 2894, "model": {"intercept": -0.389, "slope": 1.056, "slope_se": 0.052}, "kalshi_mid_same_rows": {"intercept": 0.328, "slope": 1.172, "slope_se": 0.055}, "mean_extremity_model": 0.1686, "mean_extremity_kalshi": 0.1708, "model_brier": 0.2114, "kalshi_brier": 0.2027, "brier_diff_model_minus_kalshi": 0.0088, "brier_diff_se": 0.0028, "model_logloss": 0.6104, "kalshi_logloss": 0.5873}, "gen1_elo": {"n": 2894, "model": {"intercept": -0.372, "slope": 1.036, "slope_se": 0.051}, "kalshi_mid_same_rows": {"intercept": 0.328, "slope": 1.16, "slope_se": 0.054}, "mean_extremity_model": 0.1732, "mean_extremity_kalshi": 0.1712, "model_brier": 0.2105, "kalshi_brier": 0.2026, "brier_diff_model_minus_kalshi": 0.0078, "brier_diff_se": 0.0028, "model_logloss": 0.6091, "kalshi_logloss": 0.5872}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2424, "share_ge_15": 0.4342, "median_abs_gap": 12.91, "n": 18244}, "gen1_elo": {"share_ge_25": 0.237, "share_ge_15": 0.4274, "median_abs_gap": 12.42, "n": 18244}, "gen1_sr": {"share_ge_25": 0.3023, "share_ge_15": 0.5206, "median_abs_gap": 15.74, "n": 18244}, "gen2": {"share_ge_25": 0.3029, "share_ge_15": 0.5069, "median_abs_gap": 15.36, "n": 18244}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1436, "share_ge_15": 0.3412, "median_abs_gap": 10.5, "n": 13967}, "gen1_elo": {"share_ge_25": 0.1415, "share_ge_15": 0.3303, "median_abs_gap": 9.99, "n": 13966}, "gen1_sr": {"share_ge_25": 0.2039, "share_ge_15": 0.4376, "median_abs_gap": 13.01, "n": 13967}, "gen2": {"share_ge_25": 0.2176, "share_ge_15": 0.4354, "median_abs_gap": 12.85, "n": 13968}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.24, "share_ge_25_all": 0.0141, "share_ge_25_pregame_clean": 0.0139}, "WTA": {"median_abs_gap_pregame_clean": 7.85, "share_ge_25_all": 0.0618, "share_ge_25_pregame_clean": 0.0547}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2393, "share_within_10pp_all": 0.4405, "share_within_10pp_pregame_clean": 0.5001, "corr_model_vs_mid_pregame_clean": 0.8486}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 441, "model_brier": 0.1948, "kalshi_brier": 0.1963, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 509, "model_brier": 0.2108, "kalshi_brier": 0.2028, "brier_diff_model_minus_kalshi": 0.008}, "15-25": {"n_settled": 635, "model_brier": 0.2296, "kalshi_brier": 0.2174, "brier_diff_model_minus_kalshi": 0.0122}, "25-40": {"n_settled": 343, "model_brier": 0.2273, "kalshi_brier": 0.2081, "brier_diff_model_minus_kalshi": 0.0192}, "3-5": {"n_settled": 286, "model_brier": 0.1913, "kalshi_brier": 0.1914, "brier_diff_model_minus_kalshi": -0.0002}, "40+": {"n_settled": 72, "model_brier": 0.29, "kalshi_brier": 0.1741, "brier_diff_model_minus_kalshi": 0.116}, "5-10": {"n_settled": 608, "model_brier": 0.1963, "kalshi_brier": 0.1974, "brier_diff_model_minus_kalshi": -0.0012}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.539, "slope": 0.862, "slope_se": 0.047}, "kalshi_slope": {"intercept": 0.235, "slope": 1.121, "slope_se": 0.053}, "n": 2894}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.503, "slope": 0.868, "slope_se": 0.035}, "kalshi_slope": {"intercept": 0.158, "slope": 1.078, "slope_se": 0.04}, "n": 4871}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 297, "model_brier": 0.3338, "kalshi_brier": 0.2309, "brier_diff_model_minus_kalshi": 0.1029, "brier_diff_se": 0.0187, "corr_model_outcome": -0.0178, "corr_kalshi_outcome": 0.2748}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
