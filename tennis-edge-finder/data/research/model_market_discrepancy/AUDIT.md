# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-12T06:53Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 29,829): 0-3 14.6%, 3-5 9.7%, 5-10 20.3%, 10-15 15.4%, 15-25 18.5%, 25-40 13.4%, 40+ 8.1%; median gap 11.66 pp.
* **Where the extremes live**: 98.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.2%, Challenger 12.2%, doubles 7.1%). Main tour: ATP 1.5% and WTA 6.4% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 6,428): MARKET_ALREADY_SETTLED_WHEN_PRICED 39.0%, BOOK_QUALITY 17.5%, STALE_QUOTE 16.2%, POOR_DATA 8.0%, POSSIBLY_IN_PLAY_QUOTE 5.7%, LIMITED_DATA 4.2%, IDENTITY_AMBIGUOUS 3.7%, IN_PLAY_QUOTE 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.4%. By class: coverage 39.0%, execution 17.5%, market_freshness 16.2%, data 12.2%, market_freshness/coverage 9.1%, mapping 3.7%, model_calibration_or_unknown 1.9%, model_calibration 0.4%.
* **Stale / settled / in-play**: 54.1% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 48.1% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 6,428 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 17.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 2.8%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 21.2% of the time and with the model 0.6%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 618.0 points vs 1911.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.079, Gen-2 0.873, Gen-1 ledger 0.878 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 275 model 0.2188 vs Kalshi 0.1998; n 59 model 0.2961 vs Kalshi 0.17.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 119,226 model-market comparisons (195,783 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 44,331 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-12T06:48:48.223241+00:00'], shadow board 31,489 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-12T06:48:51.399025+00:00'], Model 4 13,515 rows, 12,835 settled tickers, 3,677 tickers with an external scan.
* By model: {"gen1_ledger": 29215, "gen1_elo": 15823, "fair_v1": 15823, "gen2": 15823, "gen1_sr": 15823, "model4_fundamental": 13364, "model4_conditioned": 13355}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 29,829 | 14.6 | 9.7 | 20.3 | 15.4 | 18.5 | 13.4 | 8.1 | 11.66 | 40.1% | 21.6% |
| MW fair_v1 | 15,823 | 13.9 | 8.8 | 18.7 | 16.0 | 18.6 | 14.3 | 9.7 | 12.66 | 42.6% | 24.1% |
| MW gen1_elo | 15,823 | 13.5 | 9.1 | 20.3 | 15.0 | 18.7 | 14.2 | 9.2 | 12.08 | 42.1% | 23.4% |
| MW gen1_ledger | 14,006 | 15.4 | 10.7 | 22.0 | 14.7 | 18.5 | 12.4 | 6.3 | 10.45 | 37.2% | 18.7% |
| MW gen1_sr | 15,823 | 10.1 | 7.9 | 16.6 | 14.5 | 21.6 | 17.9 | 11.4 | 15.31 | 50.8% | 29.3% |
| MW gen2 | 15,823 | 12.1 | 7.4 | 16.4 | 14.3 | 20.1 | 16.9 | 12.8 | 14.93 | 49.8% | 29.7% |
| all families model4_conditioned | 13,355 | 21.9 | 20.1 | 35.8 | 16.1 | 4.2 | 1.0 | 0.9 | 5.79 | 6.2% | 1.9% |
| all families model4_fundamental | 13,364 | 16.7 | 13.3 | 35.9 | 19.8 | 10.6 | 2.6 | 1.1 | 7.63 | 14.3% | 3.7% |

Configurable thresholds (primary): >=5pp 75.7%, >=10pp 55.5%, >=15pp 40.1%, >=20pp 29.8%, >=25pp 21.6%, >=30pp 15.8%, >=40pp 8.1%, >=50pp 3.6%
Executable gap (model outside the book, before fees): median 8.26pp; >=10pp 44.7%, >=25pp 17.3%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,289 | 30.4 | 14.5 | 24.5 | 17.9 | 10.6 | 1.2 | 0.8 | 5.84 | 12.7% | 2.0% |
| CHALLENGER | 2,790 | 15.8 | 10.1 | 20.1 | 16.1 | 14.5 | 12.0 | 11.4 | 11.5 | 37.9% | 23.4% |
| ITF_MEN | 4,379 | 11.6 | 8.8 | 18.3 | 14.8 | 19.1 | 15.3 | 12.1 | 13.76 | 46.6% | 27.5% |
| ITF_WOMEN | 6,053 | 10.2 | 6.6 | 15.9 | 16.2 | 21.6 | 18.7 | 10.8 | 15.46 | 51.0% | 29.5% |
| WTA | 816 | 21.6 | 11.0 | 25.5 | 16.1 | 18.9 | 5.6 | 1.4 | 7.96 | 25.9% | 7.0% |
| WTA125 | 496 | 12.7 | 8.3 | 23.6 | 19.6 | 19.1 | 14.7 | 2.0 | 11.14 | 35.9% | 16.7% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,289 | 24.1 | 14.6 | 24.3 | 19.2 | 14.9 | 1.9 | 1.0 | 6.9 | 17.8% | 2.9% |
| CHALLENGER | 2,790 | 15.4 | 7.5 | 19.4 | 13.4 | 18.2 | 14.1 | 12.0 | 12.72 | 44.3% | 26.1% |
| ITF_MEN | 4,379 | 10.3 | 7.5 | 16.7 | 14.7 | 19.8 | 17.9 | 13.2 | 15.43 | 50.8% | 31.0% |
| ITF_WOMEN | 6,053 | 8.9 | 5.9 | 12.8 | 12.9 | 21.6 | 20.9 | 17.1 | 19.1 | 59.6% | 38.0% |
| WTA | 816 | 19.1 | 8.6 | 18.1 | 15.6 | 22.6 | 14.7 | 1.4 | 11.63 | 38.6% | 16.1% |
| WTA125 | 496 | 4.8 | 4.0 | 19.1 | 19.1 | 24.4 | 18.6 | 9.9 | 16.84 | 52.8% | 28.4% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,289 | 27.4 | 14.3 | 29.3 | 15.0 | 10.6 | 2.6 | 0.9 | 6.1 | 14.0% | 3.5% |
| CHALLENGER | 2,790 | 15.3 | 10.2 | 20.9 | 15.5 | 14.9 | 11.7 | 11.4 | 10.75 | 38.0% | 23.1% |
| ITF_MEN | 4,379 | 10.6 | 8.8 | 18.9 | 13.7 | 20.0 | 15.7 | 12.3 | 14.03 | 48.0% | 28.0% |
| ITF_WOMEN | 6,053 | 9.8 | 6.7 | 16.6 | 15.7 | 22.6 | 19.0 | 9.6 | 15.52 | 51.2% | 28.6% |
| WTA | 816 | 22.6 | 14.7 | 33.8 | 15.4 | 10.2 | 2.5 | 0.9 | 6.21 | 13.5% | 3.3% |
| WTA125 | 496 | 22.0 | 10.9 | 29.8 | 15.1 | 14.5 | 7.3 | 0.4 | 7.84 | 22.2% | 7.7% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 703 | 30.7 | 22.5 | 36.0 | 9.1 | 1.3 | 0.4 | 0.0 | 4.73 | 1.7% | 0.4% |
| CHALLENGER | 1,936 | 22.2 | 15.7 | 27.3 | 14.9 | 13.1 | 4.9 | 2.0 | 6.94 | 19.9% | 6.9% |
| DOUBLES | 909 | 4.5 | 3.2 | 11.4 | 11.2 | 19.4 | 24.8 | 25.5 | 25.37 | 69.6% | 50.3% |
| ITF_MEN | 4,175 | 14.9 | 8.5 | 21.1 | 15.5 | 20.4 | 12.2 | 7.4 | 11.72 | 40.0% | 19.6% |
| ITF_WOMEN | 4,872 | 11.6 | 9.3 | 19.6 | 14.5 | 22.5 | 16.7 | 5.8 | 13.09 | 45.0% | 22.5% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 625 | 21.1 | 14.9 | 27.0 | 17.3 | 14.1 | 5.1 | 0.5 | 7.78 | 19.7% | 5.6% |
| WTA125 | 637 | 19.6 | 13.8 | 22.0 | 18.7 | 14.9 | 8.6 | 2.4 | 8.37 | 25.9% | 11.0% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,277 | 30.3 | 14.4 | 24.7 | 18.0 | 10.6 | 1.2 | 0.9 | 5.84 | 12.6% | 2.0% |
| CHALLENGER | 2,036 | 20.1 | 12.5 | 25.1 | 18.7 | 15.1 | 6.0 | 2.5 | 8.32 | 23.6% | 8.5% |
| ITF_MEN | 3,101 | 14.5 | 11.1 | 21.9 | 16.6 | 19.1 | 11.9 | 4.9 | 10.63 | 36.0% | 16.8% |
| ITF_WOMEN | 4,299 | 12.6 | 8.4 | 18.6 | 18.9 | 23.3 | 14.9 | 3.3 | 12.65 | 41.5% | 18.2% |
| WTA | 805 | 21.6 | 10.4 | 25.8 | 16.1 | 19.0 | 5.6 | 1.4 | 8.09 | 26.0% | 7.0% |
| WTA125 | 475 | 13.3 | 8.0 | 22.9 | 20.0 | 19.8 | 14.5 | 1.5 | 11.31 | 35.8% | 16.0% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,277 | 24.0 | 14.6 | 24.4 | 19.2 | 14.9 | 2.0 | 1.0 | 6.9 | 17.8% | 3.0% |
| CHALLENGER | 2,036 | 19.6 | 9.5 | 24.0 | 16.1 | 18.6 | 9.6 | 2.6 | 9.16 | 30.8% | 12.2% |
| ITF_MEN | 3,102 | 12.4 | 9.1 | 19.4 | 16.5 | 21.5 | 15.0 | 6.0 | 12.51 | 42.5% | 21.0% |
| ITF_WOMEN | 4,299 | 10.4 | 7.0 | 14.6 | 14.1 | 24.4 | 19.5 | 10.1 | 16.35 | 53.9% | 29.5% |
| WTA | 805 | 18.9 | 8.3 | 18.3 | 15.8 | 22.6 | 14.8 | 1.4 | 11.73 | 38.8% | 16.2% |
| WTA125 | 475 | 4.8 | 4.2 | 19.4 | 19.6 | 24.0 | 19.2 | 8.8 | 16.64 | 52.0% | 28.0% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 683 | 30.8 | 22.7 | 36.3 | 9.2 | 0.6 | 0.4 | 0.0 | 4.7 | 1.0% | 0.4% |
| CHALLENGER | 1,665 | 24.0 | 17.2 | 29.5 | 14.8 | 12.1 | 1.9 | 0.4 | 6.31 | 14.5% | 2.3% |
| DOUBLES | 842 | 4.5 | 3.2 | 11.8 | 11.3 | 19.5 | 24.6 | 25.2 | 24.68 | 69.2% | 49.8% |
| ITF_MEN | 3,375 | 16.6 | 9.4 | 23.3 | 16.4 | 20.2 | 9.9 | 4.2 | 10.15 | 34.2% | 14.0% |
| ITF_WOMEN | 3,982 | 12.8 | 10.0 | 21.5 | 15.4 | 22.8 | 15.0 | 2.6 | 11.64 | 40.4% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 591 | 21.7 | 15.6 | 27.2 | 17.3 | 14.4 | 3.9 | 0.0 | 7.28 | 18.3% | 3.9% |
| WTA125 | 539 | 21.5 | 15.4 | 23.6 | 20.6 | 13.2 | 5.4 | 0.4 | 7.56 | 18.9% | 5.8% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 909 | 4.5 | 3.2 | 11.4 | 11.2 | 19.4 | 24.8 | 25.5 | 25.37 | 69.6% | 50.3% |
| singles | 13,097 | 16.2 | 11.2 | 22.8 | 14.9 | 18.4 | 11.6 | 5.0 | 9.95 | 34.9% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 3,613 | 13.4 | 9.4 | 20.8 | 15.9 | 16.8 | 13.7 | 9.9 | 12.01 | 40.5% | 23.7% |
| Grass | 81 | 11.1 | 22.2 | 14.8 | 7.4 | 25.9 | 18.5 | 0.0 | 10.35 | 44.4% | 18.5% |
| Hard | 10,558 | 14.4 | 8.5 | 18.6 | 15.9 | 18.9 | 14.2 | 9.6 | 12.67 | 42.6% | 23.8% |
| UNKNOWN | 1,571 | 11.7 | 8.0 | 15.5 | 17.8 | 19.9 | 16.8 | 10.3 | 14.09 | 47.0% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,934 | 20.1 | 10.8 | 21.1 | 17.0 | 15.2 | 8.7 | 7.1 | 9.45 | 31.0% | 15.8% |
| B | 2,139 | 14.3 | 9.3 | 20.1 | 17.2 | 17.3 | 12.0 | 9.8 | 11.42 | 39.1% | 21.7% |
| C | 2,328 | 13.3 | 9.7 | 19.5 | 14.6 | 19.0 | 14.7 | 9.2 | 12.61 | 42.9% | 23.9% |
| D | 2,816 | 10.8 | 8.4 | 18.0 | 16.0 | 22.1 | 14.7 | 9.9 | 13.84 | 46.7% | 24.6% |
| F | 3,606 | 7.9 | 5.3 | 14.8 | 14.9 | 20.8 | 23.0 | 13.3 | 18.33 | 57.1% | 36.3% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,146 | 22.3 | 15.8 | 28.8 | 15.3 | 11.7 | 4.5 | 1.7 | 6.82 | 17.9% | 6.2% |
| B | 2,177 | 15.2 | 9.8 | 24.0 | 16.3 | 19.1 | 11.2 | 4.3 | 10.18 | 34.6% | 15.5% |
| C | 2,785 | 12.2 | 7.6 | 18.1 | 14.4 | 20.5 | 15.8 | 11.4 | 13.64 | 47.6% | 27.2% |
| D | 2,184 | 14.1 | 9.8 | 21.1 | 13.3 | 21.7 | 13.8 | 6.3 | 11.84 | 41.8% | 20.1% |
| F | 2,714 | 9.4 | 7.5 | 14.8 | 13.9 | 23.7 | 20.9 | 9.8 | 16.79 | 54.4% | 30.7% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 5,429 | 18.4 | 9.8 | 20.3 | 17.1 | 15.3 | 9.6 | 9.4 | 10.42 | 34.4% | 19.1% |
| LIMITED | 3,922 | 15.3 | 10.5 | 20.7 | 15.6 | 18.4 | 12.8 | 6.7 | 11.04 | 37.9% | 19.5% |
| POOR | 6,472 | 9.2 | 6.8 | 16.2 | 15.4 | 21.4 | 19.2 | 11.7 | 15.98 | 52.4% | 31.0% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,906 | 31.2 | 24.1 | 36.5 | 5.6 | 1.8 | 0.7 | 0.1 | 4.52 | 2.6% | 0.8% |
| GAME_SPREAD | 2,799 | 25.5 | 15.8 | 36.9 | 17.0 | 4.2 | 0.4 | 0.2 | 6.05 | 4.9% | 0.6% |
| MATCH_WINNER | 14,006 | 15.4 | 10.7 | 22.0 | 14.7 | 18.5 | 12.4 | 6.3 | 10.45 | 37.2% | 18.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 5,277 | 33.0 | 19.4 | 31.0 | 9.9 | 5.3 | 1.2 | 0.2 | 4.78 | 6.7% | 1.4% |
| TOTAL_GAMES | 4,203 | 6.7 | 8.9 | 39.1 | 29.8 | 10.3 | 2.8 | 2.4 | 9.5 | 15.5% | 5.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,774 | 25.6 | 37.8 | 31.7 | 0.3 | 4.0 | 0.4 | 0.1 | 4.32 | 4.5% | 0.6% |
| GAME_SPREAD | 3,392 | 44.9 | 16.2 | 29.2 | 7.4 | 1.1 | 0.7 | 0.4 | 3.59 | 2.3% | 1.1% |
| TOTAL_GAMES | 5,189 | 3.3 | 6.4 | 43.8 | 36.2 | 6.5 | 1.8 | 1.9 | 9.66 | 10.2% | 3.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,774 | 26.1 | 18.5 | 37.2 | 9.3 | 6.4 | 2.1 | 0.3 | 5.54 | 8.9% | 2.5% |
| GAME_SPREAD | 3,392 | 19.0 | 13.0 | 30.3 | 21.4 | 13.3 | 2.4 | 0.7 | 7.89 | 16.4% | 3.1% |
| TOTAL_GAMES | 5,198 | 6.5 | 8.6 | 38.5 | 28.4 | 12.7 | 3.2 | 2.1 | 9.66 | 18.0% | 5.3% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 15,823 | 42.6% | 24.1% | 12.66 | 32.7% | 13.6% | 10.15 |
| gen1_elo | 15,823 | 42.1% | 23.4% | 12.08 | 31.9% | 13.4% | 9.57 |
| gen1_sr | 15,823 | 50.8% | 29.3% | 15.31 | 41.8% | 18.8% | 12.49 |
| gen2 | 15,823 | 49.8% | 29.7% | 14.93 | 42.1% | 20.6% | 12.41 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 8,361 | 16.8 | 11.0 | 21.7 | 17.5 | 18.7 | 11.1 | 3.2 | 10.13 | 33.0% | 14.3% |
| STALE | 7,462 | 10.6 | 6.3 | 15.4 | 14.4 | 18.4 | 18.0 | 16.9 | 16.85 | 53.3% | 34.9% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 7,474 | 17.4 | 11.7 | 24.0 | 14.6 | 16.7 | 10.9 | 4.6 | 9.22 | 32.3% | 15.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 29,829 | 7474 | 11833 | 10522 | 24.3 | 143.0 | 1400.4 |
| ge_15pp | 11,950 | 2411 | 4050 | 5489 | 27.6 | 445.5 | 1380.4 |
| ge_25pp | 6,428 | 1161 | 1788 | 3479 | 34.5 | 575.5 | 1380.4 |
| lt_10pp | 13,285 | 3971 | 5768 | 3546 | 22.6 | 49.1 | 1341.5 |

Current slate `SL-20261012T065354Z-efb8dbb8`: 488 priced rows, quote age at build {'median': 5.3, 'max': 5.4}, freshness {'FRESH': 488}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 8 | 0.0 | 0.0 | 37.5 | 0.0 | 37.5 | 25.0 | 0.0 | 20.45 | 62.5% | 25.0% |
| EXTERNAL_LONE_OUTLIER | 8 | 62.5 | 37.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.43 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,155 | 22.2 | 11.2 | 22.9 | 18.9 | 18.4 | 6.2 | 0.4 | 8.52 | 24.9% | 6.6% |
| KALSHI_LONE_OUTLIER | 3 | 0.0 | 0.0 | 66.7 | 0.0 | 33.3 | 0.0 | 0.0 | 5.14 | 33.3% | 0.0% |
| MARKETS_AGREE | 202 | 72.3 | 27.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.99 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 370 | 0.0 | 4.0 | 37.0 | 30.8 | 20.0 | 7.6 | 0.5 | 11.09 | 28.1% | 8.1% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 15,823 | 1746 (11.0%) | 21.2% | 0.6% | {"EXTERNAL_STALE": 1155, "AGREES_WITH_KALSHI": 370, "ALL_AGREE": 202, "EXTERNAL_OUTLIER": 8, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 3, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 6,740 | 398 (5.9%) | 26.1% | 1.5% | {"EXTERNAL_STALE": 288, "AGREES_WITH_KALSHI": 104, "SUPPORTS_MODEL_DIRECTION": 5, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp | 3,805 | 108 (2.8%) | 27.8% | 1.8% | {"EXTERNAL_STALE": 76, "AGREES_WITH_KALSHI": 30, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_ge_25pp_pregame_clean | 1,636 | 103 (6.3%) | 27.2% | 1.9% | {"EXTERNAL_STALE": 73, "AGREES_WITH_KALSHI": 28, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_lt_10pp | 6,545 | 1016 (15.5%) | 15.0% | 0.4% | {"EXTERNAL_STALE": 649, "ALL_AGREE": 202, "AGREES_WITH_KALSHI": 152, "EXTERNAL_OUTLIER": 8, "AGREES_WITH_MODEL": 2, "SUPPORTS_MODEL_DIRECTION": 2, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,137 | 11.7 | 8.4 | 19.7 | 15.1 | 21.2 | 13.9 | 10.0 | 13.24 | 45.1% | 23.8% |
| 4-10x | 2,121 | 11.8 | 9.0 | 19.3 | 15.2 | 19.6 | 15.8 | 9.2 | 13.06 | 44.6% | 25.0% |
| <2x | 8,528 | 15.9 | 9.3 | 18.9 | 17.2 | 17.0 | 12.6 | 9.0 | 11.66 | 38.6% | 21.6% |
| >=10x | 2,037 | 10.8 | 6.6 | 16.0 | 13.4 | 19.8 | 21.0 | 12.5 | 16.51 | 53.3% | 33.4% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 4,195 | 14.0 | 8.4 | 19.4 | 16.0 | 18.8 | 12.7 | 10.7 | 12.46 | 42.2% | 23.4% |
| 300-1000 | 3,707 | 12.1 | 8.9 | 17.3 | 16.0 | 21.0 | 15.6 | 9.1 | 13.57 | 45.7% | 24.7% |
| <300 | 4,139 | 8.6 | 6.2 | 15.9 | 14.6 | 20.7 | 21.2 | 12.8 | 17.1 | 54.8% | 34.0% |
| >=3000 | 3,782 | 21.3 | 11.8 | 22.5 | 17.7 | 13.5 | 7.4 | 5.8 | 8.46 | 26.7% | 13.2% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 500 | 0.5381 | 0.4069 | 0.48 | +0.058 | -0.073 | 0.0018 ± 0.0065 |
| ratio 4-10x | 339 | 0.5803 | 0.4396 | 0.5162 | +0.064 | -0.077 | 0.0027 ± 0.0086 |
| ratio <2x | 1173 | 0.5386 | 0.4179 | 0.4578 | +0.081 | -0.040 | 0.0111 ± 0.0041 |
| ratio >=10x | 338 | 0.5479 | 0.3801 | 0.4349 | +0.113 | -0.055 | 0.0152 ± 0.0095 |
| thinner_sample 1000-3000 | 660 | 0.5451 | 0.422 | 0.4773 | +0.068 | -0.055 | 0.0048 ± 0.0055 |
| thinner_sample 300-1000 | 604 | 0.564 | 0.4248 | 0.4868 | +0.077 | -0.062 | 0.0026 ± 0.0063 |
| thinner_sample <300 | 670 | 0.5424 | 0.3825 | 0.4507 | +0.092 | -0.068 | 0.0129 ± 0.0065 |
| thinner_sample >=3000 | 416 | 0.5261 | 0.432 | 0.4519 | +0.074 | -0.020 | 0.016 ± 0.0056 |
| data_status ADEQUATE | 657 | 0.5303 | 0.4284 | 0.4505 | +0.080 | -0.022 | 0.0114 ± 0.0047 |
| data_status LIMITED | 647 | 0.5548 | 0.425 | 0.493 | +0.062 | -0.068 | 0.0015 ± 0.0058 |
| data_status POOR | 1046 | 0.5501 | 0.3964 | 0.4627 | +0.087 | -0.066 | 0.0111 ± 0.0051 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 365 | 0.1903 | 0.1917 | -0.0014 ± 0.0008 | 0.5569 | 0.5602 | 0.4906 | 0.4758 | 0.5205 | -0.051 ± 0.0239 | -0.01 (3) |
| 3-5 | 241 | 0.1899 | 0.1912 | -0.0012 ± 0.0022 | 0.5596 | 0.5608 | 0.5097 | 0.47 | 0.5021 | -0.060 ± 0.0285 | 0.02 (1) |
| 5-10 | 490 | 0.2004 | 0.2021 | -0.0017 ± 0.0031 | 0.5854 | 0.5891 | 0.5165 | 0.4424 | 0.4816 | -0.084 ± 0.0212 | -0.0125 (4) |
| 10-15 | 421 | 0.2111 | 0.2047 | +0.0064 ± 0.0055 | 0.61 | 0.5904 | 0.5172 | 0.3933 | 0.4252 | -0.090 ± 0.022 | -0.0633 (3) |
| 15-25 | 499 | 0.2259 | 0.2132 | +0.0126 ± 0.0081 | 0.6461 | 0.6136 | 0.5759 | 0.3811 | 0.4469 | -0.080 ± 0.0205 | -0.0133 (6) |
| 25-40 | 275 | 0.2188 | 0.1998 | +0.0190 ± 0.016 | 0.6273 | 0.5751 | 0.648 | 0.34 | 0.4618 | -0.077 ± 0.0239 | -0.01 (1) |
| 40+ | 59 | 0.2961 | 0.17 | +0.1261 ± 0.0478 | 0.8068 | 0.513 | 0.7522 | 0.3075 | 0.3898 | -0.142 ± 0.0474 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1825 | 0.1734 | 0.1744 | -0.0010 ± 0.0003 | 0.5174 | 0.5187 | 0.4767 | 0.4618 | 0.4964 | -0.022 ± 0.0099 | -0.0188 (8) |
| 3-5 | 1143 | 0.1928 | 0.1905 | +0.0024 ± 0.001 | 0.5666 | 0.5562 | 0.4794 | 0.4399 | 0.4269 | -0.072 ± 0.0131 | 0.02 (1) |
| 5-10 | 2473 | 0.1941 | 0.1918 | +0.0023 ± 0.0013 | 0.5702 | 0.5622 | 0.4861 | 0.4124 | 0.4294 | -0.051 ± 0.009 | -0.0082 (17) |
| 10-15 | 2155 | 0.1997 | 0.1819 | +0.0178 ± 0.0023 | 0.585 | 0.5351 | 0.4765 | 0.3521 | 0.3425 | -0.076 ± 0.0092 | -0.0475 (4) |
| 15-25 | 2522 | 0.2031 | 0.1676 | +0.0355 ± 0.0032 | 0.598 | 0.4974 | 0.4969 | 0.3008 | 0.3105 | -0.065 ± 0.0081 | -0.0048 (29) |
| 25-40 | 2072 | 0.219 | 0.1227 | +0.0963 ± 0.0048 | 0.6311 | 0.3801 | 0.5277 | 0.2141 | 0.2206 | -0.065 ± 0.0074 | -0.01 (1) |
| 40+ | 1413 | 0.3714 | 0.0431 | +0.3283 ± 0.0061 | 0.9688 | 0.1719 | 0.6223 | 0.1059 | 0.0566 | -0.086 ± 0.0052 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 277 | 0.1943 | 0.1947 | -0.0003 ± 0.0009 | 0.569 | 0.5703 | 0.4935 | 0.4786 | 0.491 | -0.086 ± 0.0281 | -0.01 (1) |
| 3-5 | 184 | 0.2082 | 0.2086 | -0.0003 ± 0.0027 | 0.5969 | 0.5994 | 0.5252 | 0.4852 | 0.5054 | -0.064 ± 0.0352 | 0.02 (1) |
| 5-10 | 428 | 0.1967 | 0.1947 | +0.0020 ± 0.0032 | 0.5751 | 0.5708 | 0.5566 | 0.4815 | 0.5047 | -0.086 ± 0.0221 | -0.01 (4) |
| 10-15 | 393 | 0.2132 | 0.2046 | +0.0086 ± 0.0058 | 0.6124 | 0.595 | 0.5766 | 0.4518 | 0.4835 | -0.097 ± 0.0235 | -0.05 (4) |
| 15-25 | 572 | 0.2238 | 0.2088 | +0.0150 ± 0.0075 | 0.6362 | 0.5999 | 0.5977 | 0.4007 | 0.4668 | -0.081 ± 0.0194 | -0.01 (5) |
| 25-40 | 361 | 0.2737 | 0.198 | +0.0757 ± 0.0148 | 0.7668 | 0.5754 | 0.6717 | 0.3577 | 0.3961 | -0.141 ± 0.0233 | -0.025 (2) |
| 40+ | 135 | 0.3489 | 0.1865 | +0.1624 ± 0.0361 | 0.9805 | 0.5461 | 0.7554 | 0.2786 | 0.363 | -0.069 ± 0.0353 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1575 | 0.1776 | 0.178 | -0.0004 ± 0.0004 | 0.5267 | 0.5279 | 0.4911 | 0.4766 | 0.5016 | -0.030 ± 0.011 | -0.0217 (6) |
| 3-5 | 987 | 0.1924 | 0.1918 | +0.0006 ± 0.0011 | 0.5589 | 0.5574 | 0.5197 | 0.4798 | 0.4924 | -0.038 ± 0.0141 | 0.02 (1) |
| 5-10 | 2176 | 0.1886 | 0.1851 | +0.0035 ± 0.0014 | 0.5587 | 0.5463 | 0.5134 | 0.4398 | 0.4554 | -0.049 ± 0.0094 | -0.01 (5) |
| 10-15 | 1891 | 0.1948 | 0.1805 | +0.0143 ± 0.0025 | 0.5753 | 0.5302 | 0.5205 | 0.3961 | 0.4035 | -0.064 ± 0.0099 | -0.02 (14) |
| 15-25 | 2729 | 0.2136 | 0.1744 | +0.0392 ± 0.0032 | 0.6227 | 0.5159 | 0.5347 | 0.3389 | 0.3404 | -0.076 ± 0.0081 | -0.0026 (27) |
| 25-40 | 2382 | 0.2496 | 0.1363 | +0.1133 ± 0.0048 | 0.709 | 0.4159 | 0.5618 | 0.2458 | 0.2263 | -0.090 ± 0.0076 | -0.015 (6) |
| 40+ | 1863 | 0.4029 | 0.0671 | +0.3358 ± 0.0069 | 1.056 | 0.2355 | 0.667 | 0.1299 | 0.0998 | -0.071 ± 0.0058 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 362 | 0.193 | 0.1956 | -0.0027 ± 0.0008 | 0.5636 | 0.5706 | 0.4986 | 0.4835 | 0.5608 | -0.003 ± 0.0234 | -0.0133 (6) |
| 3-5 | 254 | 0.187 | 0.1855 | +0.0014 ± 0.0021 | 0.5498 | 0.5465 | 0.5004 | 0.4611 | 0.4646 | -0.111 ± 0.0284 | -0.01 (1) |
| 5-10 | 526 | 0.2004 | 0.1983 | +0.0021 ± 0.0029 | 0.5878 | 0.5802 | 0.507 | 0.4331 | 0.4506 | -0.093 ± 0.0202 | -0.01 (4) |
| 10-15 | 404 | 0.2125 | 0.213 | -0.0004 ± 0.0057 | 0.614 | 0.6091 | 0.5363 | 0.4137 | 0.4777 | -0.069 ± 0.0229 | -0.044 (5) |
| 15-25 | 473 | 0.2294 | 0.207 | +0.0224 ± 0.0082 | 0.6581 | 0.5982 | 0.5798 | 0.3867 | 0.4271 | -0.107 ± 0.0206 | -0.03 (1) |
| 25-40 | 280 | 0.2007 | 0.2058 | -0.0051 ± 0.0157 | 0.5843 | 0.5905 | 0.655 | 0.3435 | 0.5036 | -0.047 ± 0.0232 | 0.0 (1) |
| 40+ | 51 | 0.3152 | 0.173 | +0.1422 ± 0.0527 | 0.8532 | 0.5189 | 0.7494 | 0.2986 | 0.3725 | -0.150 ± 0.0537 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1709 | 0.1818 | 0.1828 | -0.0010 ± 0.0004 | 0.5358 | 0.5378 | 0.4854 | 0.4704 | 0.505 | -0.021 ± 0.0104 | -0.0183 (23) |
| 3-5 | 1193 | 0.1847 | 0.1823 | +0.0024 ± 0.001 | 0.5452 | 0.5392 | 0.4791 | 0.4398 | 0.4292 | -0.075 ± 0.0128 | -0.0243 (7) |
| 5-10 | 2642 | 0.1905 | 0.1854 | +0.0051 ± 0.0013 | 0.564 | 0.547 | 0.4809 | 0.4071 | 0.408 | -0.062 ± 0.0085 | -0.01 (18) |
| 10-15 | 2039 | 0.1955 | 0.1814 | +0.0141 ± 0.0023 | 0.5753 | 0.5316 | 0.4927 | 0.3697 | 0.3732 | -0.066 ± 0.0094 | -0.03 (9) |
| 15-25 | 2637 | 0.2079 | 0.1691 | +0.0388 ± 0.0031 | 0.6107 | 0.5022 | 0.5004 | 0.3052 | 0.3057 | -0.072 ± 0.008 | -0.03 (2) |
| 25-40 | 2040 | 0.2125 | 0.1192 | +0.0933 ± 0.0048 | 0.6158 | 0.3697 | 0.5228 | 0.2061 | 0.2206 | -0.060 ± 0.0072 | 0.0 (1) |
| 40+ | 1343 | 0.3851 | 0.0452 | +0.3398 ± 0.0065 | 1.0069 | 0.1777 | 0.63 | 0.1074 | 0.0551 | -0.088 ± 0.0055 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 669 | 0.2008 | 0.2014 | -0.0006 ± 0.0006 | 0.5831 | 0.5839 | 0.5015 | 0.4865 | 0.5007 | -0.037 ± 0.0174 | -0.0226 (46) |
| 3-5 | 486 | 0.1984 | 0.1973 | +0.0011 ± 0.0016 | 0.577 | 0.5725 | 0.4798 | 0.4401 | 0.4444 | -0.051 ± 0.0201 | -0.0058 (33) |
| 5-10 | 1001 | 0.1921 | 0.1866 | +0.0055 ± 0.0021 | 0.5681 | 0.5537 | 0.4799 | 0.4063 | 0.4066 | -0.062 ± 0.0139 | -0.0049 (73) |
| 10-15 | 636 | 0.2038 | 0.1932 | +0.0106 ± 0.0044 | 0.5957 | 0.5679 | 0.4921 | 0.3693 | 0.3868 | -0.050 ± 0.0175 | 0.0014 (64) |
| 15-25 | 862 | 0.2346 | 0.2099 | +0.0247 ± 0.0061 | 0.6684 | 0.6054 | 0.5535 | 0.3593 | 0.3944 | -0.058 ± 0.0157 | -0.0216 (58) |
| 25-40 | 485 | 0.2517 | 0.189 | +0.0627 ± 0.0123 | 0.7098 | 0.5526 | 0.6407 | 0.3272 | 0.3814 | -0.089 ± 0.0184 | -0.0216 (25) |
| 40+ | 166 | 0.3602 | 0.1898 | +0.1703 ± 0.0347 | 1.0519 | 0.5591 | 0.7926 | 0.2989 | 0.3976 | -0.071 ± 0.0308 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2099 | 0.1905 | 0.1907 | -0.0002 ± 0.0003 | 0.5565 | 0.5555 | 0.5024 | 0.4871 | 0.4964 | -0.035 ± 0.0095 | -0.0155 (82) |
| 3-5 | 1442 | 0.19 | 0.1873 | +0.0027 ± 0.0009 | 0.5548 | 0.5482 | 0.4866 | 0.4471 | 0.4341 | -0.058 ± 0.0114 | -0.0148 (63) |
| 5-10 | 2910 | 0.19 | 0.1822 | +0.0079 ± 0.0012 | 0.5634 | 0.5413 | 0.4751 | 0.4014 | 0.3887 | -0.065 ± 0.008 | -0.0087 (125) |
| 10-15 | 1969 | 0.1994 | 0.1851 | +0.0143 ± 0.0024 | 0.5855 | 0.5478 | 0.5026 | 0.3796 | 0.3829 | -0.055 ± 0.0096 | -0.0053 (105) |
| 15-25 | 2507 | 0.2293 | 0.1974 | +0.0319 ± 0.0035 | 0.6626 | 0.5742 | 0.5501 | 0.3552 | 0.3722 | -0.060 ± 0.009 | -0.0255 (106) |
| 25-40 | 1705 | 0.2531 | 0.1645 | +0.0886 ± 0.0062 | 0.7188 | 0.488 | 0.6027 | 0.2877 | 0.3067 | -0.080 ± 0.0095 | -0.0206 (47) |
| 40+ | 839 | 0.3857 | 0.1235 | +0.2622 ± 0.0131 | 1.0979 | 0.3813 | 0.7065 | 0.1974 | 0.2086 | -0.075 ± 0.0115 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2350 | 1.079 ± 0.058 | 1.2 | 0.1692 | 0.1697 | 0.2096 | 0.2011 |
| gen2 | 2350 | 0.873 ± 0.052 | 1.142 | 0.1845 | 0.1692 | 0.2272 | 0.2009 |
| gen1_elo | 2350 | 1.071 ± 0.057 | 1.185 | 0.1733 | 0.1701 | 0.2083 | 0.2011 |
| gen1_sr | 2350 | 1.076 ± 0.066 | 1.223 | 0.143 | 0.1714 | 0.2229 | 0.2007 |
| gen1_ledger | 4305 | 0.878 ± 0.038 | 1.083 | 0.1748 | 0.1879 | 0.2176 | 0.1961 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 11,950)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,172 | 26.5% |
| STALE_QUOTE | market_freshness | 2,365 | 19.8% |
| BOOK_QUALITY | execution | 2,143 | 17.9% |
| POOR_DATA | data | 1,253 | 10.5% |
| LIMITED_DATA | data | 931 | 7.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 671 | 5.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 570 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 387 | 3.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 358 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 100 | 0.8% |

Cause class: coverage 26.5%, market_freshness 19.8%, data 18.3%, execution 17.9%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.8%, mapping 3.2%, model_calibration 0.8%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.5%, START_UNVERIFIABLE 95.7%, LOW_DATA_QUALITY 67.7%, STALE_PLAYER_DATA 56.5%, THIN_PLAYER_HISTORY 56.0%, STALE_KALSHI_QUOTE 45.9%, MODEL_INTERNAL_DISAGREEMENT 37.8%, ASYMMETRIC_SAMPLE_SIZE 30.3%, WIDE_SPREAD 23.8%, MODEL_HIGH_UNCERTAINTY 16.4%, PLAYER_IDENTITY_RISK 11.8%, LEVEL_TRANSFER_RISK 9.0%, EVENT_MAPPING_RISK 7.9%, LOW_DISPLAYED_LIQUIDITY 7.4%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 1.4%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 29.1%, POST_SETTLEMENT_OBSERVATION 26.5%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### >= ge_25 pp (N = 6,428)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,506 | 39.0% |
| BOOK_QUALITY | execution | 1,126 | 17.5% |
| STALE_QUOTE | market_freshness | 1,042 | 16.2% |
| POOR_DATA | data | 511 | 8.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 364 | 5.7% |
| LIMITED_DATA | data | 273 | 4.2% |
| IDENTITY_AMBIGUOUS | mapping | 238 | 3.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 222 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 123 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 23 | 0.4% |

Cause class: coverage 39.0%, execution 17.5%, market_freshness 16.2%, data 12.2%, market_freshness/coverage 9.1%, mapping 3.7%, model_calibration_or_unknown 1.9%, model_calibration 0.4%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.2%, START_UNVERIFIABLE 98.1%, LOW_DATA_QUALITY 71.3%, THIN_PLAYER_HISTORY 58.4%, STALE_KALSHI_QUOTE 54.1%, STALE_PLAYER_DATA 51.2%, MODEL_INTERNAL_DISAGREEMENT 39.0%, ASYMMETRIC_SAMPLE_SIZE 32.5%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 17.5%, PLAYER_IDENTITY_RISK 15.1%, EVENT_MAPPING_RISK 9.8%, LEVEL_TRANSFER_RISK 7.8%, LOW_DISPLAYED_LIQUIDITY 7.6%, MODEL_CALIBRATION_OUTLIER 4.7%, EXTERNAL_MARKET_REJECTION 0.7%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 41.9%, POST_SETTLEMENT_OBSERVATION 39.0%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 5294, "IDENTITY_AMBIGUOUS": 1134}; ticker orientation: {"VERIFIED": 6428}.

Checks: discipline:AMBIGUOUS 457, discipline:PASS 5971, identity_confidence:AMBIGUOUS 968, identity_confidence:PASS 5460, level_mapping:NA 469, level_mapping:PASS 5959, market_pair:AMBIGUOUS 226, market_pair:NA 153, market_pair:PASS 6049, model_complement:NA 120, model_complement:PASS 6308, namesake:PASS 6428, physical_match_id:NA 2623, physical_match_id:PASS 3805, player_ids:PASS 6428, same_pair_other_event:PASS 6428, ticker_orientation:PASS 6428

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,992 | 1.5% | 1.5% | 0.4% | {"market_freshness": 20, "execution": 8, "model_calibration_or_unknown": 1} | 5.28 | 0.2056 / 0.2047 (221) | 16.6% | 0.4% | 5.6% | 1.6% |
| CHALLENGER | 4,726 | 16.7% | 5.7% | 12.2% | {"coverage": 473, "market_freshness": 109, "market_freshness/coverage": 102, "data": 43, "model_calibration_or_unknown": 40, "execution": 12, "model_calibration": 4, "mapping": 4} | 7.2 | 0.2167 / 0.2017 (1082) | 38.9% | 8.0% | 2.3% | 21.7% |
| DOUBLES | 909 | 50.3% | 49.8% | 7.1% | {"execution": 176, "mapping": 137, "market_freshness": 106, "market_freshness/coverage": 31, "coverage": 7} | 24.68 | 0.3367 / 0.2302 (252) | 25.7% | 0.0% | 100.0% | 7.4% |
| ITF_MEN | 8,554 | 23.6% | 15.4% | 31.4% | {"coverage": 842, "execution": 422, "market_freshness": 277, "data": 273, "market_freshness/coverage": 182, "mapping": 22, "model_calibration_or_unknown": 2} | 10.41 | 0.2103 / 0.1932 (2111) | 37.3% | 54.1% | 6.9% | 24.3% |
| ITF_WOMEN | 10,925 | 26.3% | 17.9% | 44.8% | {"coverage": 1167, "execution": 488, "market_freshness": 460, "data": 434, "market_freshness/coverage": 227, "mapping": 69, "model_calibration_or_unknown": 24, "model_calibration": 9} | 12.23 | 0.205 / 0.1935 (2379) | 38.6% | 57.7% | 9.6% | 24.2% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,441 | 6.4% | 5.7% | 1.4% | {"market_freshness": 36, "model_calibration_or_unknown": 21, "data": 11, "market_freshness/coverage": 9, "execution": 6, "model_calibration": 4, "coverage": 4, "mapping": 1} | 7.78 | 0.2218 / 0.2175 (211) | 27.6% | 1.5% | 1.7% | 3.1% |
| WTA125 | 1,133 | 13.5% | 10.5% | 2.4% | {"market_freshness/coverage": 34, "model_calibration_or_unknown": 33, "market_freshness": 32, "data": 23, "coverage": 12, "execution": 9, "model_calibration": 6, "mapping": 4} | 9.32 | 0.2245 / 0.2104 (357) | 23.9% | 8.0% | 4.2% | 10.5% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 5 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 6 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 207 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 8 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 9 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 10 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 11 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 12 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 13 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 14 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 15 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 16 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 18 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 9.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 553 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 19 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 20 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 21 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 22 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 23 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 24 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
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
| 36 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 110 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 37 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 39 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 153 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 40 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 41 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 42 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 43 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 44 | `KXITFWMATCH-26OCT08ARISAV-SAV` | ITF_WOMEN | fair_v1 | 75% / 2% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 45 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 256 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 46 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 114 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 47 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 48 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 49 | `KXITFMATCH-26OCT09DELSTE-DEL` | ITF_MEN | fair_v1 | 78% / 6% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 229 min (STALE); data POOR (grade F, thinner serve sample 477.0, ratio 8.93); no external reference |
| 50 | `KXITFWMATCH-26OCT08ARAWAN-ARA` | ITF_WOMEN | fair_v1 | 77% / 6% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 21.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1321 min (STALE); data POOR (grade D, thinner serve sample 553.0, ratio 3.97); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9812, "by_level_share_of_ge_25pp": {"ATP": 0.0045, "CHALLENGER": 0.1224, "DOUBLES": 0.0711, "ITF_MEN": 0.3143, "ITF_WOMEN": 0.4477, "OTHER": 0.0019, "WTA": 0.0143, "WTA125": 0.0238}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5412, "share_primary_cause_market_settled_or_in_play": 0.481, "share_primary_cause_stale_quote_only": 0.1621}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 6428, "identity_ambiguous_share": 0.1764, "ticker_orientation": {"VERIFIED": 6428}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 3805, "with_external": 108, "coverage": 0.0284, "external_status": {"EXTERNAL_STALE": 76, "AGREES_WITH_KALSHI": 30, "SUPPORTS_MODEL_DIRECTION": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 76, "MODEL_LONE_OUTLIER": 30, "ALL_THREE_DISAGREE": 2}, "share_external_agrees_with_kalshi": 0.2778, "share_external_supports_model": 0.0185}, "pregame_clean_ge_25pp": {"n": 1636, "with_external": 103, "coverage": 0.063, "external_status": {"EXTERNAL_STALE": 73, "AGREES_WITH_KALSHI": 28, "SUPPORTS_MODEL_DIRECTION": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 73, "MODEL_LONE_OUTLIER": 28, "ALL_THREE_DISAGREE": 2}, "share_external_agrees_with_kalshi": 0.2718, "share_external_supports_model": 0.0194}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 618.0, "median_sample_ratio": 2.31, "median_min_matches": 21.0, "median_max_days_since_last": 197.0, "share_severe_asymmetry": 0.184, "data_status": {"POOR": 3292, "LIMITED": 1941, "ADEQUATE": 1195}, "comparison_lt_10pp": {"median_thinner_serve_points": 1911.0, "median_sample_ratio": 1.66, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 500, "model_minus_observed": 0.0581, "kalshi_minus_observed": -0.0731, "brier_diff_model_minus_kalshi": 0.0018}, "4-10x": {"n": 339, "model_minus_observed": 0.0641, "kalshi_minus_observed": -0.0767, "brier_diff_model_minus_kalshi": 0.0027}, "<2x": {"n": 1173, "model_minus_observed": 0.0808, "kalshi_minus_observed": -0.0399, "brier_diff_model_minus_kalshi": 0.0111}, ">=10x": {"n": 338, "model_minus_observed": 0.113, "kalshi_minus_observed": -0.0548, "brier_diff_model_minus_kalshi": 0.0152}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2350, "model": {"intercept": -0.549, "slope": 0.873, "slope_se": 0.052}, "kalshi_mid_same_rows": {"intercept": 0.228, "slope": 1.142, "slope_se": 0.06}, "mean_extremity_model": 0.1845, "mean_extremity_kalshi": 0.1692, "model_brier": 0.2272, "kalshi_brier": 0.2009, "brier_diff_model_minus_kalshi": 0.0263, "brier_diff_se": 0.0039, "model_logloss": 0.6499, "kalshi_logloss": 0.5834}, "fair_v1": {"n": 2350, "model": {"intercept": -0.395, "slope": 1.079, "slope_se": 0.058}, "kalshi_mid_same_rows": {"intercept": 0.331, "slope": 1.2, "slope_se": 0.062}, "mean_extremity_model": 0.1692, "mean_extremity_kalshi": 0.1697, "model_brier": 0.2096, "kalshi_brier": 0.2011, "brier_diff_model_minus_kalshi": 0.0085, "brier_diff_se": 0.0031, "model_logloss": 0.6061, "kalshi_logloss": 0.5836}, "gen1_elo": {"n": 2350, "model": {"intercept": -0.374, "slope": 1.071, "slope_se": 0.057}, "kalshi_mid_same_rows": {"intercept": 0.331, "slope": 1.185, "slope_se": 0.061}, "mean_extremity_model": 0.1733, "mean_extremity_kalshi": 0.1701, "model_brier": 0.2083, "kalshi_brier": 0.2011, "brier_diff_model_minus_kalshi": 0.0071, "brier_diff_se": 0.003, "model_logloss": 0.604, "kalshi_logloss": 0.5836}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2405, "share_ge_15": 0.426, "median_abs_gap": 12.66, "n": 15823}, "gen1_elo": {"share_ge_25": 0.2345, "share_ge_15": 0.4211, "median_abs_gap": 12.08, "n": 15823}, "gen1_sr": {"share_ge_25": 0.2926, "share_ge_15": 0.5083, "median_abs_gap": 15.31, "n": 15823}, "gen2": {"share_ge_25": 0.2967, "share_ge_15": 0.4976, "median_abs_gap": 14.93, "n": 15823}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1364, "share_ge_15": 0.3267, "median_abs_gap": 10.15, "n": 11993}, "gen1_elo": {"share_ge_25": 0.1343, "share_ge_15": 0.3186, "median_abs_gap": 9.57, "n": 11992}, "gen1_sr": {"share_ge_25": 0.1883, "share_ge_15": 0.4183, "median_abs_gap": 12.49, "n": 11993}, "gen2": {"share_ge_25": 0.2059, "share_ge_15": 0.4211, "median_abs_gap": 12.41, "n": 11994}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.28, "share_ge_25_all": 0.0146, "share_ge_25_pregame_clean": 0.0148}, "WTA": {"median_abs_gap_pregame_clean": 7.78, "share_ge_25_all": 0.0638, "share_ge_25_pregame_clean": 0.0566}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2426, "share_within_10pp_all": 0.4454, "share_within_10pp_pregame_clean": 0.5079, "corr_model_vs_mid_pregame_clean": 0.8526}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 365, "model_brier": 0.1903, "kalshi_brier": 0.1917, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 421, "model_brier": 0.2111, "kalshi_brier": 0.2047, "brier_diff_model_minus_kalshi": 0.0064}, "15-25": {"n_settled": 499, "model_brier": 0.2259, "kalshi_brier": 0.2132, "brier_diff_model_minus_kalshi": 0.0126}, "25-40": {"n_settled": 275, "model_brier": 0.2188, "kalshi_brier": 0.1998, "brier_diff_model_minus_kalshi": 0.019}, "3-5": {"n_settled": 241, "model_brier": 0.1899, "kalshi_brier": 0.1912, "brier_diff_model_minus_kalshi": -0.0012}, "40+": {"n_settled": 59, "model_brier": 0.2961, "kalshi_brier": 0.17, "brier_diff_model_minus_kalshi": 0.1261}, "5-10": {"n_settled": 490, "model_brier": 0.2004, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": -0.0017}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.549, "slope": 0.873, "slope_se": 0.052}, "kalshi_slope": {"intercept": 0.228, "slope": 1.142, "slope_se": 0.06}, "n": 2350}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.524, "slope": 0.878, "slope_se": 0.038}, "kalshi_slope": {"intercept": 0.141, "slope": 1.083, "slope_se": 0.042}, "n": 4305}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 252, "model_brier": 0.3367, "kalshi_brier": 0.2302, "brier_diff_model_minus_kalshi": 0.1064, "brier_diff_se": 0.0205, "corr_model_outcome": -0.0259, "corr_kalshi_outcome": 0.2792}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
