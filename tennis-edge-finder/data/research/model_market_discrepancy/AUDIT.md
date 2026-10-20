# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-20T03:10Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 42,061): 0-3 14.3%, 3-5 9.5%, 5-10 19.9%, 10-15 15.4%, 15-25 19.2%, 25-40 13.7%, 40+ 8.0%; median gap 11.92 pp.
* **Where the extremes live**: 97.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 75.3%, Challenger 12.6%, doubles 7.2%). Main tour: ATP 4.3% and WTA 4.6% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 9,128): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.6%, BOOK_QUALITY 19.5%, STALE_QUOTE 17.8%, POOR_DATA 8.8%, POSSIBLY_IN_PLAY_QUOTE 5.2%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 3.8%, IN_PLAY_QUOTE 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.6%. By class: coverage 34.6%, execution 19.5%, market_freshness 17.8%, data 12.6%, market_freshness/coverage 8.6%, mapping 4.3%, model_calibration_or_unknown 2.1%, model_calibration 0.6%.
* **Stale / settled / in-play**: 51.3% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.1% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 9,128 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 24.0% of the time and with the model 0.6%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 527.0 points vs 1795.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.056, Gen-2 0.849, Gen-1 ledger 0.882 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 438 model 0.2236 vs Kalshi 0.2081; n 87 model 0.297 vs Kalshi 0.1766.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 178,847 model-market comparisons (290,380 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 62,810 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-20T03:03:26.930429+00:00'], shadow board 46,830 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-20T03:03:29.300099+00:00'], Model 4 22,070 rows, 16,898 settled tickers, 5,783 tickers with an external scan.
* By model: {"gen1_ledger": 42445, "gen1_elo": 23546, "fair_v1": 23546, "gen2": 23546, "gen1_sr": 23546, "model4_fundamental": 21118, "model4_conditioned": 21100}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 42,061 | 14.3 | 9.5 | 19.9 | 15.4 | 19.2 | 13.7 | 8.0 | 11.92 | 40.9% | 21.7% |
| MW fair_v1 | 23,546 | 13.4 | 8.6 | 18.4 | 15.9 | 19.7 | 14.6 | 9.5 | 12.99 | 43.7% | 24.1% |
| MW gen1_elo | 23,546 | 13.0 | 9.0 | 19.4 | 15.2 | 19.6 | 14.5 | 9.2 | 12.66 | 43.3% | 23.7% |
| MW gen1_ledger | 18,515 | 15.5 | 10.7 | 21.7 | 14.9 | 18.6 | 12.7 | 6.0 | 10.53 | 37.3% | 18.7% |
| MW gen1_sr | 23,546 | 10.0 | 7.3 | 16.8 | 14.2 | 21.4 | 18.4 | 11.8 | 15.62 | 51.7% | 30.3% |
| MW gen2 | 23,546 | 11.3 | 7.3 | 16.4 | 14.3 | 20.0 | 17.6 | 13.1 | 15.37 | 50.7% | 30.7% |
| all families model4_conditioned | 21,100 | 21.8 | 19.0 | 34.4 | 17.6 | 4.7 | 1.4 | 1.1 | 5.96 | 7.2% | 2.5% |
| all families model4_fundamental | 21,118 | 16.2 | 12.9 | 34.3 | 20.5 | 11.3 | 3.4 | 1.3 | 7.91 | 16.1% | 4.7% |

Configurable thresholds (primary): >=5pp 76.2%, >=10pp 56.3%, >=15pp 40.9%, >=20pp 30.2%, >=25pp 21.7%, >=30pp 15.6%, >=40pp 8.0%, >=50pp 3.6%
Executable gap (model outside the book, before fees): median 8.26pp; >=10pp 44.7%, >=25pp 16.8%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,065 | 28.8 | 13.5 | 25.0 | 16.1 | 11.6 | 4.5 | 0.6 | 6.33 | 16.7% | 5.0% |
| CHALLENGER | 3,979 | 15.3 | 10.3 | 20.2 | 16.1 | 14.8 | 12.3 | 11.0 | 11.36 | 38.1% | 23.4% |
| ITF_MEN | 6,191 | 10.8 | 7.8 | 17.2 | 14.8 | 20.4 | 16.6 | 12.4 | 14.81 | 49.3% | 28.9% |
| ITF_WOMEN | 9,203 | 10.0 | 6.8 | 15.7 | 15.6 | 22.9 | 18.1 | 10.8 | 15.61 | 51.9% | 28.9% |
| WTA | 1,448 | 17.9 | 12.5 | 24.3 | 19.5 | 20.8 | 4.2 | 0.8 | 8.57 | 25.8% | 5.0% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,065 | 23.5 | 15.3 | 24.2 | 17.2 | 13.9 | 4.9 | 0.9 | 6.81 | 19.7% | 5.8% |
| CHALLENGER | 3,979 | 14.7 | 8.2 | 18.7 | 14.2 | 18.0 | 14.2 | 12.0 | 12.84 | 44.2% | 26.2% |
| ITF_MEN | 6,191 | 9.3 | 6.5 | 15.5 | 13.4 | 19.6 | 19.8 | 15.9 | 17.43 | 55.3% | 35.7% |
| ITF_WOMEN | 9,203 | 8.2 | 5.6 | 13.6 | 13.7 | 21.5 | 20.8 | 16.6 | 18.87 | 58.9% | 37.4% |
| WTA | 1,448 | 15.1 | 9.4 | 20.0 | 16.2 | 24.0 | 14.6 | 0.8 | 11.63 | 39.4% | 15.4% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,065 | 23.8 | 13.7 | 25.2 | 16.4 | 14.6 | 5.5 | 0.8 | 7.04 | 20.9% | 6.3% |
| CHALLENGER | 3,979 | 14.4 | 9.8 | 21.2 | 15.1 | 15.9 | 12.3 | 11.4 | 11.29 | 39.5% | 23.6% |
| ITF_MEN | 6,191 | 9.9 | 7.9 | 17.6 | 14.1 | 21.2 | 16.9 | 12.4 | 15.11 | 50.5% | 29.3% |
| ITF_WOMEN | 9,203 | 9.5 | 6.9 | 16.2 | 15.8 | 23.1 | 18.4 | 10.1 | 15.58 | 51.6% | 28.5% |
| WTA | 1,448 | 24.6 | 16.9 | 30.0 | 15.3 | 10.4 | 2.4 | 0.5 | 6.0 | 13.2% | 2.8% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,196 | 27.0 | 20.3 | 30.3 | 11.6 | 7.8 | 2.8 | 0.2 | 5.3 | 10.8% | 3.0% |
| CHALLENGER | 2,769 | 21.7 | 14.7 | 27.2 | 13.8 | 14.6 | 6.2 | 1.9 | 7.16 | 22.6% | 8.1% |
| DOUBLES | 1,352 | 4.5 | 4.1 | 10.9 | 10.7 | 21.0 | 26.1 | 22.6 | 24.13 | 69.8% | 48.7% |
| ITF_MEN | 5,169 | 14.3 | 8.7 | 20.7 | 15.9 | 20.8 | 12.8 | 6.9 | 11.9 | 40.5% | 19.7% |
| ITF_WOMEN | 6,164 | 11.9 | 8.8 | 19.2 | 15.2 | 22.0 | 16.7 | 6.1 | 13.16 | 44.8% | 22.8% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 984 | 22.5 | 16.1 | 29.2 | 17.9 | 10.4 | 3.8 | 0.3 | 6.88 | 14.4% | 4.1% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,023 | 29.0 | 13.5 | 25.3 | 15.9 | 11.5 | 4.2 | 0.6 | 6.17 | 16.3% | 4.8% |
| CHALLENGER | 2,819 | 20.1 | 12.7 | 25.0 | 18.6 | 15.2 | 6.4 | 2.0 | 8.36 | 23.5% | 8.4% |
| ITF_MEN | 4,519 | 13.3 | 9.6 | 20.5 | 16.7 | 20.9 | 13.4 | 5.5 | 11.9 | 39.8% | 19.0% |
| ITF_WOMEN | 6,918 | 11.7 | 8.1 | 17.7 | 17.7 | 24.5 | 15.4 | 4.8 | 13.4 | 44.8% | 20.2% |
| WTA | 1,412 | 18.1 | 12.2 | 24.2 | 19.6 | 21.0 | 4.2 | 0.8 | 8.65 | 25.9% | 5.0% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,023 | 23.6 | 15.6 | 24.2 | 17.2 | 13.8 | 4.8 | 0.7 | 6.7 | 19.3% | 5.5% |
| CHALLENGER | 2,819 | 18.5 | 10.5 | 23.4 | 17.2 | 18.4 | 9.6 | 2.4 | 9.46 | 30.5% | 12.0% |
| ITF_MEN | 4,520 | 10.9 | 7.8 | 17.9 | 15.2 | 21.6 | 17.7 | 8.9 | 14.38 | 48.2% | 26.6% |
| ITF_WOMEN | 6,918 | 9.1 | 6.4 | 14.9 | 15.0 | 23.6 | 20.3 | 10.6 | 16.73 | 54.5% | 30.9% |
| WTA | 1,412 | 15.0 | 9.4 | 19.9 | 16.0 | 24.1 | 14.7 | 0.8 | 11.7 | 39.7% | 15.6% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,158 | 27.2 | 20.6 | 30.5 | 11.8 | 7.2 | 2.6 | 0.1 | 5.24 | 9.9% | 2.7% |
| CHALLENGER | 2,407 | 23.2 | 15.9 | 29.1 | 13.5 | 13.9 | 3.9 | 0.5 | 6.54 | 18.3% | 4.4% |
| DOUBLES | 1,256 | 4.5 | 4.3 | 11.1 | 10.8 | 20.9 | 26.3 | 22.1 | 24.07 | 69.3% | 48.3% |
| ITF_MEN | 4,299 | 15.6 | 9.4 | 22.5 | 16.8 | 20.5 | 11.0 | 4.1 | 10.71 | 35.7% | 15.1% |
| ITF_WOMEN | 5,133 | 12.7 | 9.4 | 20.7 | 16.1 | 22.2 | 15.5 | 3.5 | 11.94 | 41.2% | 19.0% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 938 | 22.9 | 16.5 | 29.2 | 17.9 | 10.4 | 3.0 | 0.0 | 6.8 | 13.4% | 3.0% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,352 | 4.5 | 4.1 | 10.9 | 10.7 | 21.0 | 26.1 | 22.6 | 24.13 | 69.8% | 48.7% |
| singles | 17,163 | 16.3 | 11.2 | 22.5 | 15.2 | 18.4 | 11.6 | 4.7 | 9.97 | 34.7% | 16.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 5,321 | 13.5 | 9.0 | 19.4 | 15.9 | 18.4 | 14.4 | 9.4 | 12.6 | 42.2% | 23.9% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 15,109 | 13.7 | 8.6 | 18.4 | 15.5 | 20.0 | 14.3 | 9.5 | 12.99 | 43.8% | 23.8% |
| UNKNOWN | 2,879 | 11.2 | 7.8 | 16.7 | 18.1 | 20.1 | 16.0 | 10.0 | 13.55 | 46.1% | 26.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,901 | 19.6 | 11.3 | 21.3 | 17.1 | 16.0 | 8.8 | 5.8 | 9.34 | 30.6% | 14.6% |
| B | 3,045 | 12.9 | 9.1 | 20.0 | 17.0 | 18.5 | 11.8 | 10.6 | 12.07 | 40.9% | 22.4% |
| C | 3,338 | 12.7 | 9.1 | 19.0 | 14.8 | 19.7 | 14.9 | 9.9 | 12.91 | 44.4% | 24.7% |
| D | 3,929 | 12.2 | 8.0 | 17.0 | 15.8 | 22.0 | 15.4 | 9.5 | 13.94 | 47.0% | 25.0% |
| F | 6,333 | 7.7 | 5.6 | 15.1 | 14.6 | 22.7 | 21.4 | 12.8 | 17.82 | 57.0% | 34.2% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,383 | 23.3 | 16.0 | 28.6 | 15.1 | 11.5 | 4.0 | 1.4 | 6.61 | 17.0% | 5.5% |
| B | 2,602 | 15.6 | 10.1 | 24.1 | 16.4 | 19.1 | 10.8 | 3.9 | 10.04 | 33.8% | 14.7% |
| C | 3,692 | 11.0 | 7.4 | 18.1 | 14.4 | 21.9 | 16.4 | 10.9 | 14.59 | 49.2% | 27.3% |
| D | 2,697 | 13.9 | 9.8 | 20.1 | 14.3 | 21.0 | 14.6 | 6.3 | 12.08 | 41.9% | 20.9% |
| F | 4,141 | 10.2 | 7.7 | 15.5 | 14.5 | 22.8 | 20.6 | 8.7 | 16.01 | 52.1% | 29.4% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 7,835 | 17.9 | 10.2 | 20.7 | 17.1 | 16.4 | 9.5 | 8.2 | 10.34 | 34.1% | 17.7% |
| LIMITED | 5,236 | 14.3 | 10.2 | 20.1 | 15.5 | 19.1 | 13.3 | 7.3 | 11.61 | 39.8% | 20.6% |
| POOR | 10,475 | 9.5 | 6.6 | 15.9 | 15.2 | 22.4 | 19.0 | 11.5 | 15.99 | 52.9% | 30.5% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,608 | 26.8 | 21.3 | 34.8 | 11.5 | 4.1 | 1.4 | 0.2 | 5.15 | 5.6% | 1.5% |
| GAME_SPREAD | 4,059 | 23.4 | 15.4 | 33.6 | 17.2 | 7.9 | 2.2 | 0.3 | 6.46 | 10.3% | 2.5% |
| MATCH_WINNER | 18,515 | 15.5 | 10.7 | 21.7 | 14.9 | 18.6 | 12.7 | 6.0 | 10.53 | 37.3% | 18.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 8,633 | 30.4 | 17.2 | 30.3 | 12.4 | 8.0 | 1.3 | 0.4 | 5.29 | 9.8% | 1.7% |
| TOTAL_GAMES | 6,606 | 7.5 | 9.0 | 36.9 | 29.1 | 11.1 | 3.5 | 3.0 | 9.64 | 17.5% | 6.4% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,385 | 25.4 | 34.4 | 32.4 | 3.8 | 3.3 | 0.6 | 0.2 | 4.46 | 4.0% | 0.7% |
| GAME_SPREAD | 5,044 | 46.2 | 16.8 | 27.1 | 7.3 | 1.7 | 0.6 | 0.3 | 3.4 | 2.6% | 0.9% |
| TOTAL_GAMES | 8,671 | 4.7 | 7.0 | 40.4 | 35.4 | 7.6 | 2.6 | 2.3 | 9.79 | 12.5% | 4.9% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,388 | 24.3 | 17.8 | 35.8 | 12.0 | 7.2 | 2.5 | 0.3 | 5.81 | 10.1% | 2.8% |
| GAME_SPREAD | 5,047 | 19.3 | 13.3 | 28.4 | 20.0 | 14.1 | 3.9 | 0.9 | 7.93 | 19.0% | 4.9% |
| TOTAL_GAMES | 8,683 | 7.5 | 8.6 | 36.5 | 27.9 | 13.3 | 3.8 | 2.4 | 9.7 | 19.5% | 6.2% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 23,546 | 43.7% | 24.1% | 12.99 | 35.4% | 15.0% | 10.8 |
| gen1_elo | 23,546 | 43.3% | 23.7% | 12.66 | 34.6% | 15.0% | 10.41 |
| gen1_sr | 23,546 | 51.7% | 30.3% | 15.62 | 44.1% | 21.2% | 13.04 |
| gen2 | 23,546 | 50.7% | 30.7% | 15.37 | 44.2% | 22.8% | 13.04 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 12,544 | 16.1 | 10.4 | 21.2 | 17.4 | 20.1 | 11.5 | 3.2 | 10.63 | 34.8% | 14.7% |
| STALE | 11,002 | 10.3 | 6.5 | 15.2 | 14.1 | 19.2 | 18.0 | 16.6 | 17.01 | 53.9% | 34.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 11,983 | 16.8 | 11.3 | 22.8 | 14.9 | 17.5 | 11.9 | 4.8 | 9.77 | 34.2% | 16.7% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 42,061 | 11983 | 16016 | 14062 | 23.5 | 134.4 | 1400.4 |
| ge_15pp | 17,197 | 4103 | 5657 | 7437 | 25.7 | 437.5 | 1380.4 |
| ge_25pp | 9,128 | 2004 | 2438 | 4686 | 31.9 | 575.5 | 1380.4 |
| lt_10pp | 18,368 | 6089 | 7620 | 4659 | 21.7 | 47.8 | 1341.5 |

Current slate `SL-20261020T031048Z-a33a2199`: 715 priced rows, quote age at build {'median': 7.7, 'max': 7.8}, freshness {'FRESH': 715}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 11 | 0.0 | 0.0 | 36.4 | 0.0 | 45.5 | 18.2 | 0.0 | 20.19 | 63.6% | 18.2% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,180 | 20.5 | 10.9 | 23.7 | 18.9 | 18.8 | 6.7 | 0.5 | 8.86 | 26.1% | 7.2% |
| KALSHI_LONE_OUTLIER | 11 | 9.1 | 0.0 | 72.7 | 0.0 | 9.1 | 9.1 | 0.0 | 5.2 | 18.2% | 9.1% |
| MARKETS_AGREE | 381 | 68.8 | 31.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.1 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 820 | 0.0 | 2.7 | 35.1 | 28.7 | 23.5 | 9.4 | 0.6 | 12.01 | 33.5% | 10.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 23,546 | 3415 (14.5%) | 24.0% | 0.6% | {"EXTERNAL_STALE": 2180, "AGREES_WITH_KALSHI": 820, "ALL_AGREE": 381, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 11, "SUPPORTS_MODEL_DIRECTION": 10, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 10,295 | 852 (8.3%) | 32.3% | 1.1% | {"EXTERNAL_STALE": 568, "AGREES_WITH_KALSHI": 275, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 5,662 | 243 (4.3%) | 33.7% | 1.2% | {"EXTERNAL_STALE": 158, "AGREES_WITH_KALSHI": 82, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,753 | 230 (8.3%) | 34.8% | 1.3% | {"EXTERNAL_STALE": 147, "AGREES_WITH_KALSHI": 80, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 9,510 | 1916 (20.2%) | 16.2% | 0.6% | {"EXTERNAL_STALE": 1200, "ALL_AGREE": 381, "AGREES_WITH_KALSHI": 310, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 9, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 4,521 | 10.9 | 7.8 | 19.4 | 15.0 | 21.9 | 15.3 | 9.8 | 13.83 | 47.0% | 25.1% |
| 4-10x | 3,081 | 11.8 | 8.7 | 18.7 | 15.8 | 20.0 | 15.0 | 9.9 | 13.26 | 45.0% | 25.0% |
| <2x | 12,207 | 15.4 | 9.6 | 19.0 | 16.9 | 18.1 | 12.6 | 8.4 | 11.72 | 39.2% | 21.0% |
| >=10x | 3,737 | 11.0 | 6.4 | 15.3 | 13.6 | 21.7 | 19.7 | 12.3 | 16.38 | 53.6% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 6,015 | 12.8 | 8.5 | 19.6 | 16.3 | 19.8 | 13.2 | 10.0 | 12.78 | 42.9% | 23.1% |
| 300-1000 | 5,187 | 12.1 | 8.8 | 16.8 | 15.8 | 20.9 | 16.1 | 9.6 | 13.82 | 46.5% | 25.7% |
| <300 | 7,194 | 8.9 | 5.9 | 15.5 | 14.8 | 22.4 | 20.1 | 12.4 | 16.86 | 54.9% | 32.5% |
| >=3000 | 5,150 | 21.6 | 12.4 | 22.8 | 17.1 | 14.5 | 6.8 | 4.8 | 8.1 | 26.2% | 11.7% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 709 | 0.5436 | 0.409 | 0.4937 | +0.050 | -0.085 | 0.0003 ± 0.0057 |
| ratio 4-10x | 485 | 0.5929 | 0.4504 | 0.5155 | +0.077 | -0.065 | 0.0081 ± 0.0072 |
| ratio <2x | 1733 | 0.538 | 0.4168 | 0.4507 | +0.087 | -0.034 | 0.0122 ± 0.0034 |
| ratio >=10x | 592 | 0.5639 | 0.3897 | 0.4493 | +0.115 | -0.060 | 0.0118 ± 0.0075 |
| thinner_sample 1000-3000 | 975 | 0.5439 | 0.4175 | 0.4585 | +0.086 | -0.041 | 0.0095 ± 0.0046 |
| thinner_sample 300-1000 | 839 | 0.5665 | 0.4256 | 0.4982 | +0.068 | -0.073 | 0.0005 ± 0.0054 |
| thinner_sample <300 | 1107 | 0.5557 | 0.3926 | 0.4553 | +0.100 | -0.063 | 0.0132 ± 0.0053 |
| thinner_sample >=3000 | 598 | 0.5325 | 0.4392 | 0.4649 | +0.068 | -0.026 | 0.0133 ± 0.0047 |
| data_status ADEQUATE | 1024 | 0.5354 | 0.431 | 0.457 | +0.078 | -0.026 | 0.0114 ± 0.0039 |
| data_status LIMITED | 864 | 0.5536 | 0.4226 | 0.4861 | +0.068 | -0.064 | 0.0038 ± 0.005 |
| data_status POOR | 1631 | 0.5596 | 0.4016 | 0.4654 | +0.094 | -0.064 | 0.0106 ± 0.0043 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 532 | 0.1959 | 0.1972 | -0.0013 ± 0.0007 | 0.5703 | 0.573 | 0.4968 | 0.4818 | 0.5338 | -0.049 ± 0.0201 | -0.01 (5) |
| 3-5 | 338 | 0.1985 | 0.1978 | +0.0007 ± 0.0019 | 0.5793 | 0.5762 | 0.5058 | 0.4658 | 0.4763 | -0.090 ± 0.0249 | 0.02 (1) |
| 5-10 | 728 | 0.199 | 0.1993 | -0.0002 ± 0.0025 | 0.5835 | 0.5821 | 0.5128 | 0.4384 | 0.4725 | -0.083 ± 0.0172 | -0.0167 (6) |
| 10-15 | 623 | 0.2147 | 0.2059 | +0.0088 ± 0.0046 | 0.6191 | 0.594 | 0.5268 | 0.4026 | 0.4286 | -0.096 ± 0.0181 | -0.048 (5) |
| 15-25 | 773 | 0.2275 | 0.2144 | +0.0131 ± 0.0065 | 0.6488 | 0.6137 | 0.5814 | 0.3862 | 0.4502 | -0.090 ± 0.0166 | -0.0033 (9) |
| 25-40 | 438 | 0.2236 | 0.2081 | +0.0155 ± 0.0129 | 0.6354 | 0.5987 | 0.6553 | 0.3474 | 0.4749 | -0.076 ± 0.0198 | -0.01 (1) |
| 40+ | 87 | 0.297 | 0.1766 | +0.1204 ± 0.0404 | 0.8103 | 0.527 | 0.7594 | 0.3102 | 0.4023 | -0.126 ± 0.0388 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2538 | 0.1803 | 0.1816 | -0.0013 ± 0.0003 | 0.5354 | 0.5368 | 0.4789 | 0.4639 | 0.5028 | -0.019 ± 0.0086 | -0.0129 (17) |
| 3-5 | 1634 | 0.1938 | 0.1919 | +0.0019 ± 0.0009 | 0.5681 | 0.5599 | 0.4822 | 0.4424 | 0.4376 | -0.063 ± 0.0111 | 0.0 (2) |
| 5-10 | 3483 | 0.1946 | 0.1914 | +0.0032 ± 0.0011 | 0.5714 | 0.5612 | 0.4853 | 0.4116 | 0.4246 | -0.051 ± 0.0075 | -0.0119 (21) |
| 10-15 | 3107 | 0.2051 | 0.1868 | +0.0183 ± 0.0019 | 0.5979 | 0.5468 | 0.4887 | 0.3641 | 0.3534 | -0.075 ± 0.0077 | -0.0281 (16) |
| 15-25 | 3762 | 0.2092 | 0.1724 | +0.0368 ± 0.0027 | 0.6097 | 0.509 | 0.5031 | 0.3069 | 0.3123 | -0.069 ± 0.0067 | -0.0025 (44) |
| 25-40 | 2898 | 0.2224 | 0.1272 | +0.0952 ± 0.0041 | 0.639 | 0.3912 | 0.5323 | 0.2196 | 0.2274 | -0.067 ± 0.0064 | -0.01 (1) |
| 40+ | 1931 | 0.3797 | 0.0428 | +0.3369 ± 0.0053 | 0.9881 | 0.1697 | 0.6299 | 0.107 | 0.057 | -0.087 ± 0.0044 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 398 | 0.1994 | 0.2 | -0.0006 ± 0.0008 | 0.5806 | 0.5819 | 0.5042 | 0.4892 | 0.5126 | -0.085 ± 0.0239 | -0.01 (3) |
| 3-5 | 288 | 0.2166 | 0.2157 | +0.0009 ± 0.0022 | 0.6166 | 0.6155 | 0.5162 | 0.4764 | 0.4792 | -0.097 ± 0.0292 | 0.02 (1) |
| 5-10 | 625 | 0.1988 | 0.1991 | -0.0003 ± 0.0027 | 0.581 | 0.5812 | 0.5461 | 0.4712 | 0.5104 | -0.073 ± 0.0184 | -0.01 (4) |
| 10-15 | 587 | 0.2172 | 0.2113 | +0.0058 ± 0.0048 | 0.6243 | 0.6088 | 0.5681 | 0.4437 | 0.4855 | -0.094 ± 0.0197 | -0.04 (5) |
| 15-25 | 841 | 0.2314 | 0.2098 | +0.0216 ± 0.0062 | 0.6549 | 0.6024 | 0.5921 | 0.3959 | 0.4435 | -0.099 ± 0.0161 | -0.0133 (9) |
| 25-40 | 576 | 0.2633 | 0.199 | +0.0643 ± 0.0117 | 0.7351 | 0.5788 | 0.6643 | 0.3491 | 0.4062 | -0.119 ± 0.0182 | -0.0075 (4) |
| 40+ | 204 | 0.3678 | 0.1756 | +0.1922 ± 0.0291 | 1.0227 | 0.5218 | 0.7445 | 0.2622 | 0.3186 | -0.084 ± 0.0283 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2170 | 0.1853 | 0.186 | -0.0007 ± 0.0003 | 0.547 | 0.5483 | 0.5024 | 0.4875 | 0.5134 | -0.031 ± 0.0096 | -0.0133 (15) |
| 3-5 | 1382 | 0.1968 | 0.1962 | +0.0007 ± 0.001 | 0.57 | 0.5682 | 0.5153 | 0.4754 | 0.4855 | -0.044 ± 0.0122 | 0.02 (1) |
| 5-10 | 3101 | 0.1908 | 0.1892 | +0.0017 ± 0.0012 | 0.5638 | 0.5564 | 0.5073 | 0.4334 | 0.4608 | -0.035 ± 0.0079 | -0.0117 (6) |
| 10-15 | 2735 | 0.2 | 0.189 | +0.0110 ± 0.0021 | 0.588 | 0.5503 | 0.5197 | 0.3951 | 0.4157 | -0.051 ± 0.0084 | -0.0189 (18) |
| 15-25 | 3895 | 0.2178 | 0.1798 | +0.0380 ± 0.0027 | 0.6302 | 0.5281 | 0.5318 | 0.3354 | 0.3404 | -0.070 ± 0.0069 | -0.0086 (42) |
| 25-40 | 3427 | 0.2504 | 0.138 | +0.1124 ± 0.004 | 0.7068 | 0.4225 | 0.5633 | 0.247 | 0.2294 | -0.089 ± 0.0063 | -0.0044 (18) |
| 40+ | 2643 | 0.4014 | 0.0646 | +0.3369 ± 0.0057 | 1.0591 | 0.2268 | 0.6618 | 0.1251 | 0.0927 | -0.072 ± 0.0048 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 511 | 0.1978 | 0.2004 | -0.0026 ± 0.0007 | 0.5762 | 0.5823 | 0.4984 | 0.4831 | 0.5577 | -0.012 ± 0.0201 | -0.0137 (8) |
| 3-5 | 374 | 0.1943 | 0.1921 | +0.0021 ± 0.0018 | 0.5663 | 0.5612 | 0.5 | 0.4604 | 0.4545 | -0.119 ± 0.0236 | 0.0067 (3) |
| 5-10 | 762 | 0.201 | 0.1978 | +0.0032 ± 0.0024 | 0.5889 | 0.5778 | 0.5081 | 0.4344 | 0.4462 | -0.098 ± 0.0166 | -0.0071 (7) |
| 10-15 | 610 | 0.2095 | 0.2072 | +0.0023 ± 0.0046 | 0.6068 | 0.5976 | 0.5416 | 0.4184 | 0.4738 | -0.076 ± 0.0182 | -0.0317 (6) |
| 15-25 | 721 | 0.234 | 0.2107 | +0.0232 ± 0.0067 | 0.6665 | 0.6055 | 0.59 | 0.3966 | 0.4327 | -0.117 ± 0.0171 | -0.03 (1) |
| 25-40 | 452 | 0.2115 | 0.2143 | -0.0028 ± 0.0127 | 0.6094 | 0.6126 | 0.6633 | 0.3535 | 0.5111 | -0.054 ± 0.0194 | 0.015 (2) |
| 40+ | 89 | 0.3108 | 0.1932 | +0.1177 ± 0.0416 | 0.8465 | 0.5643 | 0.7657 | 0.3136 | 0.4157 | -0.111 ± 0.043 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2427 | 0.1872 | 0.1882 | -0.0010 ± 0.0003 | 0.5511 | 0.5529 | 0.4876 | 0.4723 | 0.4986 | -0.028 ± 0.0089 | -0.0163 (35) |
| 3-5 | 1698 | 0.189 | 0.186 | +0.0030 ± 0.0008 | 0.5557 | 0.5484 | 0.4818 | 0.4423 | 0.4246 | -0.080 ± 0.0107 | -0.0094 (18) |
| 5-10 | 3720 | 0.195 | 0.1889 | +0.0062 ± 0.0011 | 0.5742 | 0.554 | 0.4849 | 0.411 | 0.404 | -0.068 ± 0.0072 | -0.01 (31) |
| 10-15 | 2901 | 0.1979 | 0.1818 | +0.0161 ± 0.002 | 0.581 | 0.5337 | 0.501 | 0.3774 | 0.3744 | -0.071 ± 0.0079 | -0.015 (12) |
| 15-25 | 3867 | 0.2118 | 0.1722 | +0.0396 ± 0.0026 | 0.6175 | 0.5088 | 0.5105 | 0.3159 | 0.3121 | -0.076 ± 0.0067 | -0.03 (2) |
| 25-40 | 2873 | 0.2187 | 0.1264 | +0.0922 ± 0.0042 | 0.6305 | 0.3881 | 0.5319 | 0.2163 | 0.2311 | -0.063 ± 0.0063 | 0.01 (3) |
| 40+ | 1867 | 0.3944 | 0.0475 | +0.3468 ± 0.0057 | 1.0292 | 0.1823 | 0.6414 | 0.1124 | 0.0611 | -0.089 ± 0.0048 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 857 | 0.1962 | 0.1964 | -0.0002 ± 0.0005 | 0.5727 | 0.573 | 0.5069 | 0.4919 | 0.4982 | -0.054 ± 0.0153 | -0.0224 (49) |
| 3-5 | 604 | 0.1937 | 0.1929 | +0.0007 ± 0.0014 | 0.5655 | 0.5626 | 0.4821 | 0.4423 | 0.4503 | -0.054 ± 0.0181 | -0.0194 (34) |
| 5-10 | 1280 | 0.1996 | 0.1933 | +0.0062 ± 0.0019 | 0.5866 | 0.5685 | 0.4905 | 0.4172 | 0.4125 | -0.069 ± 0.0125 | -0.005 (78) |
| 10-15 | 819 | 0.2085 | 0.1975 | +0.0110 ± 0.0039 | 0.605 | 0.5769 | 0.5147 | 0.3916 | 0.4066 | -0.064 ± 0.0157 | 0.0014 (64) |
| 15-25 | 1099 | 0.2325 | 0.2112 | +0.0213 ± 0.0054 | 0.6625 | 0.6085 | 0.5719 | 0.3769 | 0.4213 | -0.065 ± 0.0139 | -0.0214 (59) |
| 25-40 | 652 | 0.2473 | 0.2012 | +0.0461 ± 0.0108 | 0.7005 | 0.5814 | 0.6583 | 0.3463 | 0.4264 | -0.085 ± 0.0163 | -0.0219 (26) |
| 40+ | 229 | 0.3492 | 0.194 | +0.1552 ± 0.0291 | 1.0088 | 0.5691 | 0.8045 | 0.3186 | 0.4236 | -0.081 ± 0.0256 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2698 | 0.1868 | 0.1869 | -0.0001 ± 0.0003 | 0.5483 | 0.5476 | 0.5062 | 0.4909 | 0.4993 | -0.038 ± 0.0083 | -0.0157 (88) |
| 3-5 | 1860 | 0.1905 | 0.1878 | +0.0027 ± 0.0008 | 0.5572 | 0.551 | 0.488 | 0.4483 | 0.4349 | -0.061 ± 0.0101 | -0.0209 (69) |
| 5-10 | 3770 | 0.1964 | 0.1877 | +0.0086 ± 0.0011 | 0.5775 | 0.5534 | 0.4887 | 0.4152 | 0.3955 | -0.072 ± 0.0071 | -0.0082 (132) |
| 10-15 | 2561 | 0.2042 | 0.1895 | +0.0147 ± 0.0021 | 0.5953 | 0.5574 | 0.5213 | 0.3984 | 0.3991 | -0.061 ± 0.0086 | -0.0053 (105) |
| 15-25 | 3219 | 0.229 | 0.1979 | +0.0311 ± 0.0031 | 0.659 | 0.5758 | 0.5637 | 0.3684 | 0.3883 | -0.065 ± 0.0079 | -0.0253 (107) |
| 25-40 | 2196 | 0.2543 | 0.1759 | +0.0784 ± 0.0056 | 0.7201 | 0.5167 | 0.6192 | 0.3057 | 0.3406 | -0.077 ± 0.0087 | -0.0229 (51) |
| 40+ | 1036 | 0.3743 | 0.1373 | +0.2370 ± 0.0122 | 1.062 | 0.4167 | 0.7225 | 0.2189 | 0.249 | -0.072 ± 0.0106 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3519 | 1.056 ± 0.048 | 1.19 | 0.1672 | 0.1639 | 0.213 | 0.2038 |
| gen2 | 3519 | 0.849 ± 0.044 | 1.147 | 0.1727 | 0.1643 | 0.2315 | 0.2038 |
| gen1_elo | 3519 | 1.034 ± 0.046 | 1.172 | 0.1734 | 0.1642 | 0.2122 | 0.2039 |
| gen1_sr | 3519 | 1.055 ± 0.057 | 1.221 | 0.1329 | 0.1662 | 0.2275 | 0.2036 |
| gen1_ledger | 5540 | 0.882 ± 0.033 | 1.09 | 0.1787 | 0.1802 | 0.2181 | 0.1989 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 17,197)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,996 | 23.2% |
| STALE_QUOTE | market_freshness | 3,522 | 20.5% |
| BOOK_QUALITY | execution | 3,389 | 19.7% |
| POOR_DATA | data | 1,930 | 11.2% |
| LIMITED_DATA | data | 1,172 | 6.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 902 | 5.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 859 | 5.0% |
| IDENTITY_AMBIGUOUS | mapping | 694 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 486 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 247 | 1.4% |

Cause class: coverage 23.2%, market_freshness 20.5%, execution 19.7%, data 18.0%, market_freshness/coverage 8.1%, model_calibration_or_unknown 5.0%, mapping 4.0%, model_calibration 1.4%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.4%, START_UNVERIFIABLE 94.2%, LOW_DATA_QUALITY 70.0%, THIN_PLAYER_HISTORY 58.6%, STALE_PLAYER_DATA 52.3%, STALE_KALSHI_QUOTE 43.2%, MODEL_INTERNAL_DISAGREEMENT 40.9%, ASYMMETRIC_SAMPLE_SIZE 32.5%, WIDE_SPREAD 25.7%, MODEL_HIGH_UNCERTAINTY 18.0%, PLAYER_IDENTITY_RISK 15.1%, LEVEL_TRANSFER_RISK 9.7%, EVENT_MAPPING_RISK 8.5%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 2.5%, UNKNOWN 1.0%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.7%, POST_SETTLEMENT_OBSERVATION 23.2%, POSSIBLE_IN_PLAY_QUOTE 5.6%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 9,128)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,158 | 34.6% |
| BOOK_QUALITY | execution | 1,777 | 19.5% |
| STALE_QUOTE | market_freshness | 1,621 | 17.8% |
| POOR_DATA | data | 807 | 8.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 479 | 5.2% |
| IDENTITY_AMBIGUOUS | mapping | 397 | 4.3% |
| LIMITED_DATA | data | 346 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 301 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 190 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 52 | 0.6% |

Cause class: coverage 34.6%, execution 19.5%, market_freshness 17.8%, data 12.6%, market_freshness/coverage 8.6%, mapping 4.3%, model_calibration_or_unknown 2.1%, model_calibration 0.6%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.6%, START_UNVERIFIABLE 97.2%, LOW_DATA_QUALITY 74.1%, THIN_PLAYER_HISTORY 61.2%, STALE_KALSHI_QUOTE 51.3%, STALE_PLAYER_DATA 47.7%, MODEL_INTERNAL_DISAGREEMENT 41.8%, ASYMMETRIC_SAMPLE_SIZE 34.6%, WIDE_SPREAD 25.5%, PLAYER_IDENTITY_RISK 18.5%, MODEL_HIGH_UNCERTAINTY 18.2%, EVENT_MAPPING_RISK 10.3%, LEVEL_TRANSFER_RISK 8.7%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 5.1%, EXTERNAL_MARKET_REJECTION 1.3%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.5%, POST_SETTLEMENT_OBSERVATION 34.6%, POSSIBLE_IN_PLAY_QUOTE 5.6%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 7196, "IDENTITY_AMBIGUOUS": 1932}; ticker orientation: {"VERIFIED": 9128}.

Checks: discipline:AMBIGUOUS 659, discipline:PASS 8469, identity_confidence:AMBIGUOUS 1688, identity_confidence:PASS 7440, level_mapping:NA 671, level_mapping:PASS 8457, market_pair:AMBIGUOUS 341, market_pair:NA 219, market_pair:PASS 8568, model_complement:NA 186, model_complement:PASS 8942, namesake:PASS 9128, physical_match_id:NA 3466, physical_match_id:PASS 5662, player_ids:PASS 9128, same_pair_other_event:PASS 9128, ticker_orientation:PASS 9128

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,261 | 4.3% | 4.0% | 1.5% | {"market_freshness": 47, "data": 29, "model_calibration_or_unknown": 25, "execution": 17, "market_freshness/coverage": 10, "model_calibration": 10, "coverage": 2} | 5.84 | 0.2198 / 0.2114 (357) | 18.6% | 3.5% | 3.8% | 2.5% |
| CHALLENGER | 6,748 | 17.1% | 6.5% | 12.6% | {"coverage": 667, "market_freshness/coverage": 145, "market_freshness": 133, "data": 103, "model_calibration_or_unknown": 54, "execution": 26, "mapping": 14, "model_calibration": 12} | 7.35 | 0.2175 / 0.2064 (1674) | 35.4% | 16.1% | 3.6% | 22.6% |
| DOUBLES | 1,352 | 48.7% | 48.3% | 7.2% | {"execution": 326, "mapping": 175, "market_freshness": 106, "market_freshness/coverage": 45, "coverage": 7} | 24.07 | 0.3206 / 0.2346 (352) | 17.3% | 0.0% | 100.0% | 7.1% |
| ITF_MEN | 11,360 | 24.7% | 17.1% | 30.8% | {"coverage": 1077, "execution": 581, "market_freshness": 437, "data": 378, "market_freshness/coverage": 222, "mapping": 110, "model_calibration_or_unknown": 2} | 11.32 | 0.2153 / 0.1951 (2688) | 36.0% | 63.3% | 14.7% | 22.4% |
| ITF_WOMEN | 15,367 | 26.5% | 19.7% | 44.6% | {"coverage": 1388, "market_freshness": 822, "execution": 796, "data": 609, "market_freshness/coverage": 309, "mapping": 92, "model_calibration_or_unknown": 44, "model_calibration": 10} | 12.88 | 0.2014 / 0.1936 (3073) | 37.7% | 58.2% | 10.4% | 21.6% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,432 | 4.6% | 4.2% | 1.2% | {"market_freshness": 36, "model_calibration_or_unknown": 24, "execution": 17, "data": 11, "market_freshness/coverage": 10, "model_calibration": 9, "coverage": 4, "mapping": 1} | 7.82 | 0.2385 / 0.2317 (385) | 23.8% | 1.4% | 1.5% | 3.4% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.9% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

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
| 8 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 9 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 17.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1037 min (STALE); no external reference |
| 10 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 11 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 12 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 13 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 14 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 15 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 16 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 17 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 18 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 19 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 20 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 22 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 23 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 24 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 25 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 26 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 27 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 28 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 29 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 92 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 30 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 31 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 32 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 33 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 34 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 35 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 36 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 765 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 37 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 38 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 39 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 730 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |
| 40 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 41 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 33 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 42 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 43 | `KXITFWMATCH-26OCT16ESTLAB-LAB` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 68 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1475.0, ratio 2.28); no external reference |
| 44 | `KXITFWMATCH-26OCT19VLABOU-VLA` | ITF_WOMEN | fair_v1 | 77% / 2% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 625 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 3.13); no external reference |
| 45 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 46 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 47 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 48 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 49 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 50 | `KXATPDOUBLES-26OCT18COLGOFPOLZIE-COLGOF` | DOUBLES | gen1_ledger | 90% / 15% | +75 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9724, "by_level_share_of_ge_25pp": {"ATP": 0.0153, "CHALLENGER": 0.1264, "DOUBLES": 0.0722, "ITF_MEN": 0.3075, "ITF_WOMEN": 0.4459, "OTHER": 0.0013, "WTA": 0.0123, "WTA125": 0.0191}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5134, "share_primary_cause_market_settled_or_in_play": 0.4315, "share_primary_cause_stale_quote_only": 0.1776}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 9128, "identity_ambiguous_share": 0.2117, "ticker_orientation": {"VERIFIED": 9128}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 5662, "with_external": 243, "coverage": 0.0429, "external_status": {"EXTERNAL_STALE": 158, "AGREES_WITH_KALSHI": 82, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 158, "MODEL_LONE_OUTLIER": 82, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3374, "share_external_supports_model": 0.0123}, "pregame_clean_ge_25pp": {"n": 2753, "with_external": 230, "coverage": 0.0835, "external_status": {"EXTERNAL_STALE": 147, "AGREES_WITH_KALSHI": 80, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 147, "MODEL_LONE_OUTLIER": 80, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3478, "share_external_supports_model": 0.013}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 527.0, "median_sample_ratio": 2.46, "median_min_matches": 21.0, "median_max_days_since_last": 220.0, "share_severe_asymmetry": 0.2088, "data_status": {"POOR": 4988, "LIMITED": 2549, "ADEQUATE": 1591}, "comparison_lt_10pp": {"median_thinner_serve_points": 1795.0, "median_sample_ratio": 1.67, "median_min_matches": 94.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 709, "model_minus_observed": 0.05, "kalshi_minus_observed": -0.0847, "brier_diff_model_minus_kalshi": 0.0003}, "4-10x": {"n": 485, "model_minus_observed": 0.0774, "kalshi_minus_observed": -0.065, "brier_diff_model_minus_kalshi": 0.0081}, "<2x": {"n": 1733, "model_minus_observed": 0.0874, "kalshi_minus_observed": -0.0339, "brier_diff_model_minus_kalshi": 0.0122}, ">=10x": {"n": 592, "model_minus_observed": 0.1146, "kalshi_minus_observed": -0.0596, "brier_diff_model_minus_kalshi": 0.0118}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3519, "model": {"intercept": -0.529, "slope": 0.849, "slope_se": 0.044}, "kalshi_mid_same_rows": {"intercept": 0.242, "slope": 1.147, "slope_se": 0.05}, "mean_extremity_model": 0.1727, "mean_extremity_kalshi": 0.1643, "model_brier": 0.2315, "kalshi_brier": 0.2038, "brier_diff_model_minus_kalshi": 0.0278, "brier_diff_se": 0.0032, "model_logloss": 0.6596, "kalshi_logloss": 0.5899}, "fair_v1": {"n": 3519, "model": {"intercept": -0.401, "slope": 1.056, "slope_se": 0.048}, "kalshi_mid_same_rows": {"intercept": 0.322, "slope": 1.19, "slope_se": 0.051}, "mean_extremity_model": 0.1672, "mean_extremity_kalshi": 0.1639, "model_brier": 0.213, "kalshi_brier": 0.2038, "brier_diff_model_minus_kalshi": 0.0092, "brier_diff_se": 0.0026, "model_logloss": 0.6138, "kalshi_logloss": 0.5899}, "gen1_elo": {"n": 3519, "model": {"intercept": -0.394, "slope": 1.034, "slope_se": 0.046}, "kalshi_mid_same_rows": {"intercept": 0.314, "slope": 1.172, "slope_se": 0.05}, "mean_extremity_model": 0.1734, "mean_extremity_kalshi": 0.1642, "model_brier": 0.2122, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0083, "brier_diff_se": 0.0026, "model_logloss": 0.6128, "kalshi_logloss": 0.5899}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2405, "share_ge_15": 0.4372, "median_abs_gap": 12.99, "n": 23546}, "gen1_elo": {"share_ge_25": 0.2372, "share_ge_15": 0.4332, "median_abs_gap": 12.66, "n": 23546}, "gen1_sr": {"share_ge_25": 0.3029, "share_ge_15": 0.5172, "median_abs_gap": 15.62, "n": 23546}, "gen2": {"share_ge_25": 0.3068, "share_ge_15": 0.5068, "median_abs_gap": 15.37, "n": 23546}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1502, "share_ge_15": 0.3535, "median_abs_gap": 10.8, "n": 18325}, "gen1_elo": {"share_ge_25": 0.1503, "share_ge_15": 0.346, "median_abs_gap": 10.41, "n": 18323}, "gen1_sr": {"share_ge_25": 0.2121, "share_ge_15": 0.4412, "median_abs_gap": 13.04, "n": 18325}, "gen2": {"share_ge_25": 0.2284, "share_ge_15": 0.4421, "median_abs_gap": 13.04, "n": 18326}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.84, "share_ge_25_all": 0.0429, "share_ge_25_pregame_clean": 0.0402}, "WTA": {"median_abs_gap_pregame_clean": 7.82, "share_ge_25_all": 0.0461, "share_ge_25_pregame_clean": 0.0417}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2381, "share_within_10pp_all": 0.4367, "share_within_10pp_pregame_clean": 0.4894, "corr_model_vs_mid_pregame_clean": 0.8428}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 532, "model_brier": 0.1959, "kalshi_brier": 0.1972, "brier_diff_model_minus_kalshi": -0.0013}, "10-15": {"n_settled": 623, "model_brier": 0.2147, "kalshi_brier": 0.2059, "brier_diff_model_minus_kalshi": 0.0088}, "15-25": {"n_settled": 773, "model_brier": 0.2275, "kalshi_brier": 0.2144, "brier_diff_model_minus_kalshi": 0.0131}, "25-40": {"n_settled": 438, "model_brier": 0.2236, "kalshi_brier": 0.2081, "brier_diff_model_minus_kalshi": 0.0155}, "3-5": {"n_settled": 338, "model_brier": 0.1985, "kalshi_brier": 0.1978, "brier_diff_model_minus_kalshi": 0.0007}, "40+": {"n_settled": 87, "model_brier": 0.297, "kalshi_brier": 0.1766, "brier_diff_model_minus_kalshi": 0.1204}, "5-10": {"n_settled": 728, "model_brier": 0.199, "kalshi_brier": 0.1993, "brier_diff_model_minus_kalshi": -0.0002}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.529, "slope": 0.849, "slope_se": 0.044}, "kalshi_slope": {"intercept": 0.242, "slope": 1.147, "slope_se": 0.05}, "n": 3519}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.514, "slope": 0.882, "slope_se": 0.033}, "kalshi_slope": {"intercept": 0.156, "slope": 1.09, "slope_se": 0.038}, "n": 5540}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 352, "model_brier": 0.3206, "kalshi_brier": 0.2346, "brier_diff_model_minus_kalshi": 0.0861, "brier_diff_se": 0.0167, "corr_model_outcome": 0.0143, "corr_kalshi_outcome": 0.2592}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
