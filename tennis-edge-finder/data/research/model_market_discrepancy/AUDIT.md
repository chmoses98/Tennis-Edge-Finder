# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-24T05:40Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 51,404): 0-3 13.9%, 3-5 9.5%, 5-10 19.7%, 10-15 15.3%, 15-25 19.2%, 25-40 14.1%, 40+ 8.3%; median gap 12.13 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.9%, Challenger 11.9%, doubles 6.6%). Main tour: ATP 4.6% and WTA 5.5% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 11,496): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.8%, STALE_QUOTE 18.7%, BOOK_QUALITY 17.9%, POOR_DATA 8.8%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.5%, IN_PLAY_QUOTE 3.6%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.8%, market_freshness 18.7%, execution 17.9%, data 12.2%, market_freshness/coverage 9.0%, mapping 4.5%, model_calibration_or_unknown 2.2%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.5% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 11,496 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.1% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.6% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 490.0 points vs 1680.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.033, Gen-2 0.838, Gen-1 ledger 0.861 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 559 model 0.224 vs Kalshi 0.2089; n 113 model 0.2806 vs Kalshi 0.1974.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 222,505 model-market comparisons (362,281 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 73,753 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-24T05:27:05.557008+00:00'], shadow board 59,569 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-24T05:27:09.374717+00:00'], Model 4 27,827 rows, 19,681 settled tickers, 7,002 tickers with an external scan.
* By model: {"gen1_ledger": 50166, "gen1_elo": 29957, "fair_v1": 29957, "gen2": 29957, "gen1_sr": 29957, "model4_fundamental": 26269, "model4_conditioned": 26242}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 51,404 | 13.9 | 9.5 | 19.7 | 15.3 | 19.2 | 14.1 | 8.3 | 12.13 | 41.6% | 22.4% |
| MW fair_v1 | 29,957 | 12.8 | 8.5 | 18.5 | 15.5 | 19.7 | 15.0 | 10.0 | 13.19 | 44.7% | 25.0% |
| MW gen1_elo | 29,957 | 12.7 | 8.5 | 18.9 | 15.2 | 19.9 | 15.0 | 9.7 | 13.02 | 44.6% | 24.7% |
| MW gen1_ledger | 21,447 | 15.5 | 10.8 | 21.4 | 15.0 | 18.6 | 12.8 | 5.9 | 10.55 | 37.2% | 18.6% |
| MW gen1_sr | 29,957 | 10.2 | 7.0 | 16.5 | 13.6 | 20.8 | 18.8 | 13.0 | 16.08 | 52.7% | 31.9% |
| MW gen2 | 29,957 | 10.9 | 7.3 | 16.2 | 14.0 | 19.4 | 18.0 | 14.2 | 15.67 | 51.6% | 32.2% |
| all families model4_conditioned | 26,242 | 21.9 | 18.9 | 34.8 | 17.6 | 4.3 | 1.5 | 1.0 | 5.96 | 6.8% | 2.5% |
| all families model4_fundamental | 26,269 | 16.7 | 13.3 | 34.2 | 20.5 | 10.6 | 3.4 | 1.3 | 7.76 | 15.2% | 4.7% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.9%, >=15pp 41.6%, >=20pp 31.0%, >=25pp 22.4%, >=30pp 16.2%, >=40pp 8.3%, >=50pp 3.9%
Executable gap (model outside the book, before fees): median 8.52pp; >=10pp 45.6%, >=25pp 17.5%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,584 | 28.4 | 14.2 | 24.9 | 15.2 | 11.8 | 4.7 | 0.7 | 6.06 | 17.2% | 5.4% |
| CHALLENGER | 4,635 | 15.8 | 10.0 | 20.5 | 15.4 | 14.7 | 12.4 | 11.2 | 11.06 | 38.3% | 23.6% |
| ITF_MEN | 8,300 | 10.1 | 7.3 | 16.9 | 14.6 | 21.5 | 17.4 | 12.2 | 15.41 | 51.0% | 29.5% |
| ITF_WOMEN | 11,921 | 9.4 | 6.9 | 16.0 | 15.3 | 22.3 | 18.2 | 12.0 | 15.79 | 52.5% | 30.2% |
| WTA | 1,857 | 17.1 | 13.1 | 26.1 | 19.3 | 17.9 | 5.7 | 0.7 | 8.25 | 24.3% | 6.3% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,584 | 24.2 | 15.1 | 24.8 | 17.4 | 13.0 | 4.6 | 0.9 | 6.5 | 18.5% | 5.6% |
| CHALLENGER | 4,635 | 15.1 | 8.8 | 18.5 | 14.5 | 17.3 | 13.9 | 12.0 | 12.48 | 43.1% | 25.9% |
| ITF_MEN | 8,300 | 8.2 | 5.9 | 14.4 | 12.9 | 19.7 | 21.0 | 17.8 | 18.71 | 58.5% | 38.8% |
| ITF_WOMEN | 11,921 | 8.1 | 5.7 | 13.7 | 13.3 | 20.6 | 21.0 | 17.7 | 19.09 | 59.2% | 38.7% |
| WTA | 1,857 | 13.7 | 10.2 | 22.3 | 16.4 | 22.8 | 13.2 | 1.4 | 10.97 | 37.4% | 14.5% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,584 | 24.0 | 12.7 | 23.6 | 16.5 | 15.1 | 7.0 | 1.1 | 7.45 | 23.2% | 8.1% |
| CHALLENGER | 4,635 | 14.4 | 9.2 | 20.4 | 15.5 | 16.2 | 13.0 | 11.3 | 11.48 | 40.5% | 24.3% |
| ITF_MEN | 8,300 | 9.7 | 7.3 | 16.9 | 13.9 | 22.1 | 17.7 | 12.3 | 15.74 | 52.1% | 30.0% |
| ITF_WOMEN | 11,921 | 9.4 | 6.6 | 16.3 | 15.8 | 22.7 | 18.1 | 11.1 | 15.6 | 51.9% | 29.2% |
| WTA | 1,857 | 23.9 | 17.1 | 30.5 | 15.3 | 10.1 | 2.6 | 0.5 | 6.04 | 13.2% | 3.1% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,537 | 25.7 | 19.4 | 30.2 | 12.4 | 9.0 | 2.9 | 0.3 | 5.54 | 12.3% | 3.2% |
| CHALLENGER | 3,173 | 21.6 | 14.6 | 26.4 | 14.4 | 14.5 | 6.7 | 1.9 | 7.29 | 23.1% | 8.6% |
| DOUBLES | 1,606 | 5.4 | 4.5 | 11.6 | 10.4 | 21.1 | 25.9 | 21.1 | 23.73 | 68.1% | 46.9% |
| ITF_MEN | 6,140 | 13.8 | 9.1 | 20.0 | 16.2 | 21.2 | 13.3 | 6.5 | 12.16 | 41.0% | 19.8% |
| ITF_WOMEN | 7,055 | 12.7 | 9.0 | 19.3 | 15.1 | 21.6 | 16.3 | 6.1 | 12.84 | 43.9% | 22.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,055 | 22.3 | 16.0 | 29.6 | 18.1 | 10.1 | 3.6 | 0.4 | 6.86 | 14.0% | 4.0% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,514 | 28.7 | 14.4 | 25.3 | 15.2 | 11.5 | 4.3 | 0.5 | 5.93 | 16.4% | 4.8% |
| CHALLENGER | 3,258 | 20.8 | 12.4 | 25.3 | 17.8 | 15.0 | 6.8 | 1.9 | 8.31 | 23.7% | 8.7% |
| ITF_MEN | 6,095 | 12.2 | 8.8 | 20.3 | 16.5 | 22.7 | 14.3 | 5.1 | 12.54 | 42.2% | 19.4% |
| ITF_WOMEN | 8,896 | 11.2 | 8.2 | 18.2 | 17.4 | 24.2 | 15.3 | 5.5 | 13.51 | 45.1% | 20.8% |
| WTA | 1,805 | 17.3 | 13.0 | 26.0 | 19.6 | 17.9 | 5.4 | 0.7 | 8.25 | 24.0% | 6.2% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,514 | 24.4 | 15.5 | 24.9 | 17.3 | 13.0 | 4.3 | 0.6 | 6.41 | 17.9% | 4.9% |
| CHALLENGER | 3,258 | 19.1 | 11.3 | 23.1 | 17.3 | 17.5 | 9.5 | 2.1 | 9.07 | 29.1% | 11.6% |
| ITF_MEN | 6,096 | 9.8 | 7.1 | 16.8 | 14.9 | 21.6 | 19.3 | 10.6 | 15.5 | 51.5% | 29.8% |
| ITF_WOMEN | 8,897 | 9.2 | 6.5 | 15.2 | 14.8 | 22.6 | 20.5 | 11.2 | 16.62 | 54.3% | 31.7% |
| WTA | 1,805 | 13.8 | 10.2 | 22.3 | 16.3 | 22.8 | 13.1 | 1.4 | 11.03 | 37.3% | 14.5% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,490 | 25.9 | 19.7 | 30.2 | 12.6 | 8.6 | 2.8 | 0.2 | 5.47 | 11.6% | 3.0% |
| CHALLENGER | 2,762 | 23.1 | 15.8 | 27.8 | 14.3 | 13.9 | 4.6 | 0.5 | 6.7 | 19.0% | 5.1% |
| DOUBLES | 1,489 | 5.4 | 4.7 | 11.8 | 10.5 | 21.0 | 25.9 | 20.7 | 23.62 | 67.6% | 46.5% |
| ITF_MEN | 5,144 | 14.9 | 9.7 | 21.7 | 17.0 | 21.1 | 11.6 | 4.0 | 11.16 | 36.7% | 15.6% |
| ITF_WOMEN | 5,832 | 13.6 | 9.6 | 20.7 | 16.0 | 21.8 | 15.0 | 3.4 | 11.66 | 40.1% | 18.3% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,005 | 22.8 | 16.5 | 29.6 | 18.1 | 10.1 | 2.9 | 0.1 | 6.79 | 13.0% | 3.0% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,606 | 5.4 | 4.5 | 11.6 | 10.4 | 21.1 | 25.9 | 21.1 | 23.73 | 68.1% | 46.9% |
| singles | 19,841 | 16.3 | 11.3 | 22.2 | 15.4 | 18.4 | 11.7 | 4.6 | 10.03 | 34.8% | 16.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 6,625 | 13.0 | 8.9 | 19.2 | 15.6 | 18.7 | 14.6 | 10.0 | 12.83 | 43.2% | 24.6% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 18,518 | 13.2 | 8.6 | 18.6 | 15.2 | 19.8 | 14.9 | 9.8 | 13.1 | 44.5% | 24.7% |
| UNKNOWN | 4,577 | 10.7 | 7.5 | 17.1 | 16.8 | 20.6 | 16.2 | 11.0 | 14.11 | 47.9% | 27.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,429 | 19.5 | 11.9 | 21.5 | 16.4 | 15.1 | 9.2 | 6.4 | 9.14 | 30.7% | 15.6% |
| B | 3,716 | 12.5 | 8.7 | 19.7 | 16.1 | 19.2 | 12.7 | 11.1 | 12.61 | 43.0% | 23.8% |
| C | 4,215 | 11.4 | 8.7 | 19.8 | 15.2 | 19.4 | 14.8 | 10.8 | 13.18 | 44.9% | 25.5% |
| D | 4,678 | 12.1 | 7.7 | 17.3 | 15.5 | 21.4 | 15.7 | 10.2 | 13.98 | 47.3% | 25.9% |
| F | 8,919 | 7.6 | 5.5 | 15.1 | 14.6 | 23.4 | 21.3 | 12.6 | 17.8 | 57.2% | 33.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,048 | 23.2 | 15.9 | 28.7 | 15.1 | 11.6 | 4.0 | 1.5 | 6.62 | 17.1% | 5.5% |
| B | 2,922 | 16.3 | 10.4 | 23.3 | 16.2 | 19.2 | 10.7 | 3.9 | 10.01 | 33.8% | 14.6% |
| C | 4,213 | 11.3 | 7.4 | 18.2 | 14.3 | 21.6 | 16.7 | 10.6 | 14.37 | 48.8% | 27.3% |
| D | 2,997 | 14.4 | 9.8 | 19.9 | 14.5 | 20.9 | 14.4 | 6.1 | 12.04 | 41.4% | 20.5% |
| F | 5,267 | 10.3 | 8.5 | 15.6 | 15.1 | 22.7 | 19.9 | 8.1 | 15.32 | 50.6% | 28.0% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 9,694 | 17.7 | 10.7 | 20.8 | 16.2 | 15.7 | 10.0 | 8.9 | 10.22 | 34.6% | 19.0% |
| LIMITED | 6,330 | 13.3 | 10.0 | 20.4 | 15.6 | 19.3 | 13.5 | 7.9 | 11.97 | 40.7% | 21.4% |
| POOR | 13,933 | 9.2 | 6.3 | 16.0 | 15.0 | 22.6 | 19.2 | 11.8 | 16.21 | 53.6% | 30.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,941 | 25.9 | 19.7 | 33.8 | 12.8 | 5.4 | 2.1 | 0.2 | 5.46 | 7.8% | 2.4% |
| GAME_SPREAD | 4,791 | 22.2 | 15.3 | 33.5 | 17.3 | 9.1 | 2.3 | 0.3 | 6.73 | 11.8% | 2.6% |
| MATCH_WINNER | 21,447 | 15.5 | 10.8 | 21.4 | 15.0 | 18.6 | 12.8 | 5.9 | 10.55 | 37.2% | 18.6% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 10,385 | 29.3 | 17.3 | 30.8 | 12.4 | 8.0 | 1.9 | 0.4 | 5.44 | 10.3% | 2.3% |
| TOTAL_GAMES | 7,578 | 9.0 | 9.8 | 36.5 | 28.6 | 10.4 | 3.2 | 2.6 | 9.4 | 16.1% | 5.8% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,245 | 25.3 | 33.2 | 32.6 | 4.8 | 3.2 | 0.7 | 0.2 | 4.5 | 4.1% | 0.9% |
| GAME_SPREAD | 6,277 | 45.6 | 16.7 | 26.8 | 7.9 | 1.7 | 0.9 | 0.3 | 3.47 | 2.9% | 1.2% |
| TOTAL_GAMES | 10,720 | 5.0 | 7.8 | 41.3 | 34.3 | 6.9 | 2.5 | 2.1 | 9.55 | 11.5% | 4.6% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,248 | 24.2 | 17.6 | 35.5 | 12.7 | 7.1 | 2.6 | 0.3 | 5.86 | 10.0% | 2.9% |
| GAME_SPREAD | 6,280 | 19.5 | 13.4 | 27.9 | 20.7 | 13.3 | 4.3 | 0.9 | 7.96 | 18.5% | 5.2% |
| TOTAL_GAMES | 10,741 | 8.6 | 9.6 | 36.8 | 27.1 | 12.0 | 3.6 | 2.3 | 9.42 | 17.9% | 5.9% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 29,957 | 44.7% | 25.0% | 13.19 | 36.3% | 15.7% | 10.96 |
| gen1_elo | 29,957 | 44.6% | 24.7% | 13.02 | 36.1% | 15.8% | 10.78 |
| gen1_sr | 29,957 | 52.7% | 31.9% | 16.08 | 44.9% | 22.4% | 13.19 |
| gen2 | 29,957 | 51.6% | 32.2% | 15.67 | 44.7% | 24.0% | 13.13 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 15,236 | 15.7 | 10.4 | 21.3 | 17.2 | 20.1 | 12.0 | 3.3 | 10.75 | 35.5% | 15.3% |
| STALE | 14,721 | 9.8 | 6.6 | 15.6 | 13.8 | 19.2 | 18.1 | 17.0 | 17.06 | 54.3% | 35.1% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 14,915 | 16.6 | 11.3 | 22.2 | 15.1 | 17.8 | 12.2 | 4.8 | 9.98 | 34.8% | 17.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 51,404 | 14915 | 18708 | 17781 | 24.2 | 148.5 | 1400.4 |
| ge_15pp | 21,385 | 5190 | 6695 | 9500 | 26.3 | 441.8 | 1380.4 |
| ge_25pp | 11,496 | 2533 | 2927 | 6036 | 32.7 | 583.5 | 1380.4 |
| lt_10pp | 22,156 | 7472 | 8843 | 5841 | 22.4 | 48.1 | 1341.5 |

Current slate `SL-20261024T054044Z-6e2da660`: 451 priced rows, quote age at build {'median': 14.0, 'max': 14.0}, freshness {'AGING': 451}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 24 | 0.0 | 0.0 | 25.0 | 4.2 | 37.5 | 33.3 | 0.0 | 20.48 | 70.8% | 33.3% |
| EXTERNAL_LONE_OUTLIER | 14 | 71.4 | 28.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.4 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,866 | 19.2 | 11.1 | 24.9 | 18.7 | 18.2 | 7.2 | 0.7 | 8.82 | 26.0% | 7.8% |
| KALSHI_LONE_OUTLIER | 17 | 5.9 | 5.9 | 76.5 | 0.0 | 5.9 | 5.9 | 0.0 | 6.11 | 11.8% | 5.9% |
| MARKETS_AGREE | 570 | 64.2 | 35.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.34 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,204 | 0.0 | 2.2 | 35.7 | 25.8 | 24.7 | 10.9 | 0.8 | 12.25 | 36.3% | 11.6% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 29,957 | 4695 (15.7%) | 25.6% | 0.9% | {"EXTERNAL_STALE": 2866, "AGREES_WITH_KALSHI": 1204, "ALL_AGREE": 570, "SUPPORTS_MODEL_DIRECTION": 23, "AGREES_WITH_MODEL": 17, "EXTERNAL_OUTLIER": 14, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 13,396 | 1201 (9.0%) | 36.4% | 1.6% | {"EXTERNAL_STALE": 745, "AGREES_WITH_KALSHI": 437, "SUPPORTS_MODEL_DIRECTION": 17, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 7,501 | 373 (5.0%) | 37.5% | 2.4% | {"EXTERNAL_STALE": 224, "AGREES_WITH_KALSHI": 140, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,645 | 350 (9.6%) | 38.0% | 2.6% | {"EXTERNAL_STALE": 208, "AGREES_WITH_KALSHI": 133, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 11,915 | 2646 (22.2%) | 17.3% | 0.8% | {"EXTERNAL_STALE": 1584, "ALL_AGREE": 570, "AGREES_WITH_KALSHI": 457, "AGREES_WITH_MODEL": 15, "EXTERNAL_OUTLIER": 14, "SUPPORTS_MODEL_DIRECTION": 5, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,720 | 10.2 | 7.5 | 19.4 | 14.4 | 22.3 | 16.0 | 10.2 | 14.25 | 48.5% | 26.2% |
| 4-10x | 3,924 | 11.0 | 8.2 | 19.2 | 15.3 | 21.2 | 15.0 | 10.1 | 13.75 | 46.3% | 25.1% |
| <2x | 15,138 | 14.9 | 9.7 | 19.0 | 16.4 | 17.6 | 13.1 | 9.3 | 11.89 | 40.0% | 22.4% |
| >=10x | 5,175 | 10.9 | 6.3 | 15.3 | 14.3 | 21.9 | 19.5 | 11.9 | 16.35 | 53.3% | 31.4% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 7,627 | 12.3 | 8.6 | 19.6 | 16.0 | 19.0 | 13.7 | 10.9 | 12.94 | 43.6% | 24.6% |
| 300-1000 | 6,419 | 11.7 | 8.6 | 17.3 | 15.3 | 20.5 | 16.3 | 10.3 | 13.95 | 47.2% | 26.6% |
| <300 | 9,842 | 8.6 | 5.7 | 15.5 | 14.7 | 23.0 | 20.1 | 12.4 | 17.01 | 55.5% | 32.5% |
| >=3000 | 6,069 | 21.4 | 13.0 | 23.2 | 16.4 | 14.2 | 7.0 | 4.8 | 7.93 | 26.0% | 11.9% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 851 | 0.5483 | 0.4101 | 0.4994 | +0.049 | -0.089 | -0.0032 ± 0.0053 |
| ratio 4-10x | 585 | 0.587 | 0.4411 | 0.494 | +0.093 | -0.053 | 0.0124 ± 0.0066 |
| ratio <2x | 2095 | 0.5378 | 0.4143 | 0.4453 | +0.092 | -0.031 | 0.0129 ± 0.0031 |
| ratio >=10x | 783 | 0.5716 | 0.3963 | 0.4649 | +0.107 | -0.069 | 0.0065 ± 0.0065 |
| thinner_sample 1000-3000 | 1163 | 0.5415 | 0.4145 | 0.4437 | +0.098 | -0.029 | 0.0116 ± 0.0042 |
| thinner_sample 300-1000 | 989 | 0.5666 | 0.4232 | 0.4934 | +0.073 | -0.070 | 0.0008 ± 0.0051 |
| thinner_sample <300 | 1461 | 0.5606 | 0.3943 | 0.4648 | +0.096 | -0.070 | 0.0089 ± 0.0046 |
| thinner_sample >=3000 | 701 | 0.5349 | 0.4403 | 0.4679 | +0.067 | -0.028 | 0.0133 ± 0.0044 |
| data_status ADEQUATE | 1228 | 0.5377 | 0.4327 | 0.4511 | +0.087 | -0.018 | 0.0127 ± 0.0036 |
| data_status LIMITED | 997 | 0.5501 | 0.4165 | 0.4784 | +0.072 | -0.062 | 0.0051 ± 0.0048 |
| data_status POOR | 2089 | 0.5627 | 0.4015 | 0.4691 | +0.093 | -0.068 | 0.0076 ± 0.0038 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 628 | 0.2007 | 0.2017 | -0.0010 ± 0.0006 | 0.5819 | 0.5841 | 0.5026 | 0.4878 | 0.5303 | -0.063 ± 0.0188 | -0.01 (5) |
| 3-5 | 401 | 0.2028 | 0.2023 | +0.0005 ± 0.0018 | 0.5888 | 0.586 | 0.5019 | 0.4617 | 0.4738 | -0.097 ± 0.0232 | 0.02 (1) |
| 5-10 | 892 | 0.2021 | 0.2015 | +0.0006 ± 0.0023 | 0.5909 | 0.5861 | 0.511 | 0.4368 | 0.4652 | -0.091 ± 0.0156 | -0.0167 (6) |
| 10-15 | 743 | 0.214 | 0.2042 | +0.0098 ± 0.0042 | 0.6186 | 0.59 | 0.5295 | 0.4054 | 0.4266 | -0.104 ± 0.0165 | -0.048 (5) |
| 15-25 | 978 | 0.2249 | 0.2133 | +0.0117 ± 0.0058 | 0.6448 | 0.6103 | 0.5777 | 0.3819 | 0.4499 | -0.093 ± 0.0147 | -0.0033 (9) |
| 25-40 | 559 | 0.224 | 0.2089 | +0.0151 ± 0.0115 | 0.6366 | 0.6009 | 0.6576 | 0.3479 | 0.4758 | -0.076 ± 0.0178 | -0.01 (1) |
| 40+ | 113 | 0.2806 | 0.1974 | +0.0832 ± 0.0363 | 0.768 | 0.5798 | 0.7562 | 0.3089 | 0.4425 | -0.080 ± 0.0356 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3238 | 0.1842 | 0.1852 | -0.0010 ± 0.0003 | 0.5439 | 0.545 | 0.4928 | 0.4777 | 0.5136 | -0.019 ± 0.0076 | -0.0129 (17) |
| 3-5 | 2145 | 0.1992 | 0.1981 | +0.0011 ± 0.0008 | 0.5796 | 0.5742 | 0.4841 | 0.4441 | 0.449 | -0.052 ± 0.0098 | 0.0 (2) |
| 5-10 | 4664 | 0.1977 | 0.1944 | +0.0032 ± 0.001 | 0.5793 | 0.5681 | 0.4803 | 0.4064 | 0.4211 | -0.047 ± 0.0065 | -0.0119 (21) |
| 10-15 | 3967 | 0.1974 | 0.1791 | +0.0182 ± 0.0017 | 0.5803 | 0.5289 | 0.4864 | 0.3619 | 0.3504 | -0.074 ± 0.0067 | -0.0281 (16) |
| 15-25 | 4987 | 0.2086 | 0.1699 | +0.0387 ± 0.0023 | 0.6105 | 0.5024 | 0.5058 | 0.3094 | 0.3098 | -0.073 ± 0.0058 | -0.0025 (44) |
| 25-40 | 3916 | 0.2231 | 0.1295 | +0.0936 ± 0.0036 | 0.6403 | 0.396 | 0.5316 | 0.2184 | 0.2293 | -0.059 ± 0.0056 | -0.01 (1) |
| 40+ | 2564 | 0.3807 | 0.0455 | +0.3352 ± 0.0048 | 0.9918 | 0.1749 | 0.6332 | 0.1071 | 0.0644 | -0.078 ± 0.0039 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 495 | 0.2059 | 0.2066 | -0.0007 ± 0.0007 | 0.5937 | 0.5951 | 0.5075 | 0.4923 | 0.5152 | -0.103 ± 0.0219 | -0.01 (3) |
| 3-5 | 357 | 0.2238 | 0.2215 | +0.0023 ± 0.002 | 0.6341 | 0.6292 | 0.5137 | 0.4737 | 0.4594 | -0.123 ± 0.0265 | 0.02 (1) |
| 5-10 | 770 | 0.2055 | 0.2057 | -0.0002 ± 0.0025 | 0.5973 | 0.5966 | 0.5467 | 0.4719 | 0.513 | -0.077 ± 0.0168 | -0.01 (4) |
| 10-15 | 715 | 0.2172 | 0.209 | +0.0082 ± 0.0043 | 0.624 | 0.6036 | 0.5661 | 0.4419 | 0.4727 | -0.112 ± 0.0178 | -0.04 (5) |
| 15-25 | 1003 | 0.2296 | 0.2099 | +0.0197 ± 0.0057 | 0.6522 | 0.6024 | 0.5876 | 0.3918 | 0.4437 | -0.101 ± 0.0147 | -0.0133 (9) |
| 25-40 | 706 | 0.2622 | 0.1978 | +0.0644 ± 0.0105 | 0.7316 | 0.576 | 0.653 | 0.3374 | 0.3952 | -0.112 ± 0.0164 | -0.0075 (4) |
| 40+ | 268 | 0.3604 | 0.1718 | +0.1886 ± 0.0251 | 0.9908 | 0.5142 | 0.732 | 0.2474 | 0.3097 | -0.073 ± 0.0243 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2773 | 0.1936 | 0.194 | -0.0004 ± 0.0003 | 0.5639 | 0.5646 | 0.5109 | 0.4959 | 0.5139 | -0.040 ± 0.0087 | -0.0133 (15) |
| 3-5 | 1842 | 0.1991 | 0.1983 | +0.0008 ± 0.0008 | 0.5763 | 0.574 | 0.5143 | 0.4744 | 0.4843 | -0.044 ± 0.0106 | 0.02 (1) |
| 5-10 | 4104 | 0.1958 | 0.1941 | +0.0017 ± 0.001 | 0.5767 | 0.5676 | 0.5084 | 0.4343 | 0.4625 | -0.032 ± 0.007 | -0.0117 (6) |
| 10-15 | 3590 | 0.2009 | 0.1887 | +0.0122 ± 0.0018 | 0.5886 | 0.5501 | 0.5131 | 0.3891 | 0.4028 | -0.056 ± 0.0074 | -0.0189 (18) |
| 15-25 | 4950 | 0.2159 | 0.1777 | +0.0381 ± 0.0024 | 0.6273 | 0.5232 | 0.5248 | 0.3289 | 0.3333 | -0.069 ± 0.006 | -0.0086 (42) |
| 25-40 | 4579 | 0.2517 | 0.1377 | +0.1139 ± 0.0035 | 0.708 | 0.4224 | 0.5579 | 0.2409 | 0.2223 | -0.084 ± 0.0054 | -0.0044 (18) |
| 40+ | 3643 | 0.3942 | 0.0607 | +0.3334 ± 0.0047 | 1.0377 | 0.2169 | 0.6507 | 0.1186 | 0.0843 | -0.071 ± 0.004 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 603 | 0.1993 | 0.2014 | -0.0021 ± 0.0006 | 0.5792 | 0.5844 | 0.5007 | 0.4854 | 0.5489 | -0.029 ± 0.0188 | -0.0137 (8) |
| 3-5 | 428 | 0.2018 | 0.1997 | +0.0021 ± 0.0018 | 0.5865 | 0.5798 | 0.5069 | 0.4672 | 0.4626 | -0.122 ± 0.0224 | 0.0067 (3) |
| 5-10 | 906 | 0.2011 | 0.1977 | +0.0035 ± 0.0022 | 0.5886 | 0.5766 | 0.5075 | 0.4335 | 0.4448 | -0.102 ± 0.0151 | -0.0071 (7) |
| 10-15 | 753 | 0.2085 | 0.2052 | +0.0032 ± 0.0041 | 0.6058 | 0.5927 | 0.5393 | 0.4157 | 0.4661 | -0.083 ± 0.0164 | -0.0317 (6) |
| 15-25 | 925 | 0.2315 | 0.2125 | +0.0191 ± 0.0059 | 0.6611 | 0.6081 | 0.5881 | 0.3937 | 0.4411 | -0.112 ± 0.0151 | -0.03 (1) |
| 25-40 | 580 | 0.2135 | 0.2175 | -0.0039 ± 0.0113 | 0.615 | 0.6207 | 0.6689 | 0.3578 | 0.5172 | -0.052 ± 0.0175 | 0.015 (2) |
| 40+ | 119 | 0.2963 | 0.2093 | +0.0869 ± 0.0367 | 0.8166 | 0.606 | 0.7668 | 0.3173 | 0.4538 | -0.078 ± 0.0385 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3184 | 0.1849 | 0.1854 | -0.0004 ± 0.0003 | 0.5444 | 0.545 | 0.4904 | 0.4752 | 0.4874 | -0.040 ± 0.0077 | -0.0163 (35) |
| 3-5 | 2140 | 0.1952 | 0.1929 | +0.0023 ± 0.0008 | 0.5731 | 0.5659 | 0.4881 | 0.4484 | 0.4402 | -0.068 ± 0.0097 | -0.0094 (18) |
| 5-10 | 4699 | 0.1961 | 0.1904 | +0.0058 ± 0.001 | 0.5765 | 0.5574 | 0.4826 | 0.4086 | 0.4067 | -0.061 ± 0.0064 | -0.01 (31) |
| 10-15 | 3873 | 0.191 | 0.1754 | +0.0157 ± 0.0017 | 0.5655 | 0.5189 | 0.4987 | 0.3752 | 0.3731 | -0.066 ± 0.0067 | -0.015 (12) |
| 15-25 | 5164 | 0.2106 | 0.1719 | +0.0387 ± 0.0023 | 0.6151 | 0.5072 | 0.5145 | 0.3196 | 0.3178 | -0.073 ± 0.0058 | -0.03 (2) |
| 25-40 | 3937 | 0.2191 | 0.1334 | +0.0858 ± 0.0037 | 0.6324 | 0.4043 | 0.5377 | 0.2214 | 0.2459 | -0.048 ± 0.0056 | 0.01 (3) |
| 40+ | 2484 | 0.3954 | 0.0501 | +0.3453 ± 0.0051 | 1.0333 | 0.1871 | 0.6455 | 0.1135 | 0.0688 | -0.081 ± 0.0043 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 985 | 0.1951 | 0.1953 | -0.0002 ± 0.0005 | 0.5696 | 0.5697 | 0.5038 | 0.4887 | 0.4954 | -0.056 ± 0.0143 | -0.0224 (49) |
| 3-5 | 688 | 0.1914 | 0.1908 | +0.0006 ± 0.0013 | 0.5598 | 0.5571 | 0.4898 | 0.4499 | 0.4593 | -0.057 ± 0.017 | -0.0194 (34) |
| 5-10 | 1430 | 0.2013 | 0.1951 | +0.0062 ± 0.0018 | 0.5919 | 0.5726 | 0.4966 | 0.4232 | 0.4189 | -0.073 ± 0.0119 | -0.005 (78) |
| 10-15 | 953 | 0.2107 | 0.1986 | +0.0121 ± 0.0036 | 0.6109 | 0.5793 | 0.5213 | 0.3981 | 0.4082 | -0.071 ± 0.0148 | 0.0014 (64) |
| 15-25 | 1281 | 0.2316 | 0.2099 | +0.0217 ± 0.005 | 0.661 | 0.6044 | 0.5766 | 0.3818 | 0.4247 | -0.073 ± 0.0128 | -0.0214 (59) |
| 25-40 | 781 | 0.248 | 0.2071 | +0.0409 ± 0.01 | 0.7046 | 0.5954 | 0.6727 | 0.3602 | 0.4507 | -0.086 ± 0.0153 | -0.0219 (26) |
| 40+ | 259 | 0.3527 | 0.1969 | +0.1558 ± 0.0272 | 1.0182 | 0.5756 | 0.8085 | 0.3262 | 0.4247 | -0.096 ± 0.0248 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3218 | 0.1829 | 0.1831 | -0.0002 ± 0.0003 | 0.5388 | 0.5385 | 0.5048 | 0.4894 | 0.5009 | -0.037 ± 0.0076 | -0.0157 (88) |
| 3-5 | 2239 | 0.1943 | 0.1924 | +0.0018 ± 0.0007 | 0.567 | 0.5629 | 0.4952 | 0.4554 | 0.452 | -0.053 ± 0.0094 | -0.0209 (69) |
| 5-10 | 4454 | 0.1973 | 0.1889 | +0.0084 ± 0.001 | 0.5805 | 0.5556 | 0.4915 | 0.4181 | 0.4003 | -0.072 ± 0.0066 | -0.0082 (132) |
| 10-15 | 3112 | 0.206 | 0.1899 | +0.0161 ± 0.0019 | 0.6004 | 0.5582 | 0.528 | 0.4049 | 0.4004 | -0.066 ± 0.0078 | -0.0053 (105) |
| 15-25 | 3895 | 0.2297 | 0.1993 | +0.0304 ± 0.0028 | 0.6622 | 0.5777 | 0.569 | 0.3735 | 0.3944 | -0.066 ± 0.0072 | -0.0253 (107) |
| 25-40 | 2697 | 0.2589 | 0.1842 | +0.0747 ± 0.0052 | 0.7339 | 0.5375 | 0.6324 | 0.3185 | 0.3589 | -0.077 ± 0.0081 | -0.0229 (51) |
| 40+ | 1191 | 0.3768 | 0.1449 | +0.2319 ± 0.0116 | 1.0685 | 0.4362 | 0.7295 | 0.2262 | 0.2603 | -0.070 ± 0.0104 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4314 | 1.033 ± 0.043 | 1.13 | 0.169 | 0.1647 | 0.2141 | 0.2056 |
| gen2 | 4314 | 0.838 ± 0.04 | 1.094 | 0.1688 | 0.1652 | 0.2335 | 0.2052 |
| gen1_elo | 4314 | 1.009 ± 0.041 | 1.12 | 0.1759 | 0.1647 | 0.213 | 0.2059 |
| gen1_sr | 4314 | 1.027 ± 0.052 | 1.17 | 0.1297 | 0.1672 | 0.2296 | 0.2049 |
| gen1_ledger | 6377 | 0.861 ± 0.03 | 1.073 | 0.1838 | 0.179 | 0.2186 | 0.1997 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 21,385)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,957 | 23.2% |
| STALE_QUOTE | market_freshness | 4,636 | 21.7% |
| BOOK_QUALITY | execution | 3,964 | 18.5% |
| POOR_DATA | data | 2,428 | 11.3% |
| LIMITED_DATA | data | 1,313 | 6.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,167 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,016 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 904 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 643 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 356 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 23.2%, market_freshness 21.7%, execution 18.5%, data 17.5%, market_freshness/coverage 8.5%, model_calibration_or_unknown 4.8%, mapping 4.2%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 94.2%, LOW_DATA_QUALITY 71.0%, THIN_PLAYER_HISTORY 60.0%, STALE_PLAYER_DATA 49.4%, STALE_KALSHI_QUOTE 44.4%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 33.6%, WIDE_SPREAD 24.6%, MODEL_HIGH_UNCERTAINTY 18.0%, PLAYER_IDENTITY_RISK 16.4%, LEVEL_TRANSFER_RISK 11.1%, LOW_DISPLAYED_LIQUIDITY 8.0%, EVENT_MAPPING_RISK 7.9%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.2%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.8%, POST_SETTLEMENT_OBSERVATION 23.2%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 11,496)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,998 | 34.8% |
| STALE_QUOTE | market_freshness | 2,149 | 18.7% |
| BOOK_QUALITY | execution | 2,059 | 17.9% |
| POOR_DATA | data | 1,008 | 8.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 623 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 511 | 4.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 410 | 3.6% |
| LIMITED_DATA | data | 400 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 257 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 80 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.8%, market_freshness 18.7%, execution 17.9%, data 12.2%, market_freshness/coverage 9.0%, mapping 4.5%, model_calibration_or_unknown 2.2%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 74.3%, THIN_PLAYER_HISTORY 62.1%, STALE_KALSHI_QUOTE 52.5%, STALE_PLAYER_DATA 44.0%, MODEL_INTERNAL_DISAGREEMENT 42.9%, ASYMMETRIC_SAMPLE_SIZE 34.7%, WIDE_SPREAD 23.7%, PLAYER_IDENTITY_RISK 19.6%, MODEL_HIGH_UNCERTAINTY 18.4%, LEVEL_TRANSFER_RISK 9.8%, EVENT_MAPPING_RISK 9.4%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.9%, POST_SETTLEMENT_OBSERVATION 34.8%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 8955, "IDENTITY_AMBIGUOUS": 2541}; ticker orientation: {"VERIFIED": 11496}.

Checks: discipline:AMBIGUOUS 754, discipline:PASS 10742, identity_confidence:AMBIGUOUS 2258, identity_confidence:PASS 9238, level_mapping:NA 766, level_mapping:PASS 10730, market_pair:AMBIGUOUS 398, market_pair:NA 290, market_pair:PASS 10808, model_complement:NA 257, model_complement:PASS 11239, namesake:PASS 11496, physical_match_id:NA 3995, physical_match_id:PASS 7501, player_ids:PASS 11496, same_pair_other_event:PASS 11496, ticker_orientation:PASS 11496

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,121 | 4.6% | 4.2% | 1.7% | {"market_freshness": 53, "model_calibration_or_unknown": 43, "data": 35, "execution": 22, "market_freshness/coverage": 13, "model_calibration": 13, "coverage": 11} | 5.84 | 0.2176 / 0.2124 (475) | 18.2% | 3.8% | 3.1% | 2.8% |
| CHALLENGER | 7,808 | 17.5% | 7.1% | 11.9% | {"coverage": 773, "market_freshness/coverage": 167, "market_freshness": 148, "data": 138, "model_calibration_or_unknown": 64, "execution": 31, "model_calibration": 28, "mapping": 15, "possible_market_error": 1} | 7.4 | 0.2197 / 0.2081 (1880) | 34.9% | 17.7% | 3.8% | 22.9% |
| DOUBLES | 1,606 | 46.9% | 46.5% | 6.6% | {"execution": 388, "mapping": 199, "market_freshness": 106, "market_freshness/coverage": 54, "coverage": 7} | 23.62 | 0.3098 / 0.2355 (424) | 14.6% | 0.0% | 100.0% | 7.3% |
| ITF_MEN | 14,440 | 25.4% | 17.7% | 31.9% | {"coverage": 1367, "execution": 697, "market_freshness": 624, "data": 487, "market_freshness/coverage": 316, "mapping": 173, "model_calibration_or_unknown": 2, "model_calibration": 2} | 11.9 | 0.2158 / 0.1977 (3237) | 37.5% | 70.1% | 19.9% | 22.2% |
| ITF_WOMEN | 18,976 | 27.3% | 19.8% | 45.0% | {"coverage": 1818, "market_freshness": 1126, "execution": 882, "data": 714, "market_freshness/coverage": 434, "mapping": 118, "model_calibration_or_unknown": 70, "model_calibration": 11} | 12.84 | 0.2034 / 0.1943 (3690) | 40.0% | 55.9% | 9.9% | 22.4% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,912 | 5.5% | 5.0% | 1.4% | {"market_freshness": 52, "model_calibration_or_unknown": 37, "execution": 25, "model_calibration": 15, "data": 11, "market_freshness/coverage": 10, "coverage": 9, "mapping": 1} | 7.7 | 0.2376 / 0.2293 (455) | 24.4% | 1.4% | 1.5% | 3.5% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.5% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 15 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 16 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 17 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 18 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 19 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 20 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 21 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 22 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 23 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 24 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 25 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 26 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 27 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 28 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 29 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 30 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 31 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 32 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 33 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 34 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 35 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 36 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 37 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 39 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 22.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1345 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 41 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 42 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 43 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 44 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 46 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 47 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 48 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 49 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 50 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9695, "by_level_share_of_ge_25pp": {"ATP": 0.0165, "CHALLENGER": 0.1187, "DOUBLES": 0.0656, "ITF_MEN": 0.3191, "ITF_WOMEN": 0.45, "OTHER": 0.001, "WTA": 0.0139, "WTA125": 0.0151}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5251, "share_primary_cause_market_settled_or_in_play": 0.4377, "share_primary_cause_stale_quote_only": 0.1869}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 11496, "identity_ambiguous_share": 0.221, "ticker_orientation": {"VERIFIED": 11496}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 7501, "with_external": 373, "coverage": 0.0497, "external_status": {"EXTERNAL_STALE": 224, "AGREES_WITH_KALSHI": 140, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 224, "MODEL_LONE_OUTLIER": 140, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3753, "share_external_supports_model": 0.0241}, "pregame_clean_ge_25pp": {"n": 3645, "with_external": 350, "coverage": 0.096, "external_status": {"EXTERNAL_STALE": 208, "AGREES_WITH_KALSHI": 133, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 208, "MODEL_LONE_OUTLIER": 133, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.38, "share_external_supports_model": 0.0257}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 490.0, "median_sample_ratio": 2.43, "median_min_matches": 21.0, "median_max_days_since_last": 225.0, "share_severe_asymmetry": 0.2148, "data_status": {"POOR": 6414, "LIMITED": 2998, "ADEQUATE": 2084}, "comparison_lt_10pp": {"median_thinner_serve_points": 1680.0, "median_sample_ratio": 1.71, "median_min_matches": 94.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 851, "model_minus_observed": 0.0489, "kalshi_minus_observed": -0.0893, "brier_diff_model_minus_kalshi": -0.0032}, "4-10x": {"n": 585, "model_minus_observed": 0.0929, "kalshi_minus_observed": -0.0529, "brier_diff_model_minus_kalshi": 0.0124}, "<2x": {"n": 2095, "model_minus_observed": 0.0924, "kalshi_minus_observed": -0.031, "brier_diff_model_minus_kalshi": 0.0129}, ">=10x": {"n": 783, "model_minus_observed": 0.1067, "kalshi_minus_observed": -0.0686, "brier_diff_model_minus_kalshi": 0.0065}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4314, "model": {"intercept": -0.539, "slope": 0.838, "slope_se": 0.04}, "kalshi_mid_same_rows": {"intercept": 0.216, "slope": 1.094, "slope_se": 0.044}, "mean_extremity_model": 0.1688, "mean_extremity_kalshi": 0.1652, "model_brier": 0.2335, "kalshi_brier": 0.2052, "brier_diff_model_minus_kalshi": 0.0283, "brier_diff_se": 0.0029, "model_logloss": 0.6635, "kalshi_logloss": 0.5932}, "fair_v1": {"n": 4314, "model": {"intercept": -0.414, "slope": 1.033, "slope_se": 0.043}, "kalshi_mid_same_rows": {"intercept": 0.299, "slope": 1.13, "slope_se": 0.045}, "mean_extremity_model": 0.169, "mean_extremity_kalshi": 0.1647, "model_brier": 0.2141, "kalshi_brier": 0.2056, "brier_diff_model_minus_kalshi": 0.0085, "brier_diff_se": 0.0024, "model_logloss": 0.6169, "kalshi_logloss": 0.5937}, "gen1_elo": {"n": 4314, "model": {"intercept": -0.399, "slope": 1.009, "slope_se": 0.041}, "kalshi_mid_same_rows": {"intercept": 0.31, "slope": 1.12, "slope_se": 0.044}, "mean_extremity_model": 0.1759, "mean_extremity_kalshi": 0.1647, "model_brier": 0.213, "kalshi_brier": 0.2059, "brier_diff_model_minus_kalshi": 0.0072, "brier_diff_se": 0.0024, "model_logloss": 0.6155, "kalshi_logloss": 0.5943}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2504, "share_ge_15": 0.4472, "median_abs_gap": 13.19, "n": 29957}, "gen1_elo": {"share_ge_25": 0.2474, "share_ge_15": 0.4463, "median_abs_gap": 13.02, "n": 29957}, "gen1_sr": {"share_ge_25": 0.3185, "share_ge_15": 0.5267, "median_abs_gap": 16.08, "n": 29957}, "gen2": {"share_ge_25": 0.3216, "share_ge_15": 0.5157, "median_abs_gap": 15.67, "n": 29957}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1571, "share_ge_15": 0.3629, "median_abs_gap": 10.96, "n": 23202}, "gen1_elo": {"share_ge_25": 0.1577, "share_ge_15": 0.3606, "median_abs_gap": 10.78, "n": 23199}, "gen1_sr": {"share_ge_25": 0.2243, "share_ge_15": 0.4485, "median_abs_gap": 13.19, "n": 23203}, "gen2": {"share_ge_25": 0.2404, "share_ge_15": 0.4473, "median_abs_gap": 13.13, "n": 23204}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.84, "share_ge_25_all": 0.0461, "share_ge_25_pregame_clean": 0.0415}, "WTA": {"median_abs_gap_pregame_clean": 7.7, "share_ge_25_all": 0.0549, "share_ge_25_pregame_clean": 0.0502}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2339, "share_within_10pp_all": 0.431, "share_within_10pp_pregame_clean": 0.4845, "corr_model_vs_mid_pregame_clean": 0.8435}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 628, "model_brier": 0.2007, "kalshi_brier": 0.2017, "brier_diff_model_minus_kalshi": -0.001}, "10-15": {"n_settled": 743, "model_brier": 0.214, "kalshi_brier": 0.2042, "brier_diff_model_minus_kalshi": 0.0098}, "15-25": {"n_settled": 978, "model_brier": 0.2249, "kalshi_brier": 0.2133, "brier_diff_model_minus_kalshi": 0.0117}, "25-40": {"n_settled": 559, "model_brier": 0.224, "kalshi_brier": 0.2089, "brier_diff_model_minus_kalshi": 0.0151}, "3-5": {"n_settled": 401, "model_brier": 0.2028, "kalshi_brier": 0.2023, "brier_diff_model_minus_kalshi": 0.0005}, "40+": {"n_settled": 113, "model_brier": 0.2806, "kalshi_brier": 0.1974, "brier_diff_model_minus_kalshi": 0.0832}, "5-10": {"n_settled": 892, "model_brier": 0.2021, "kalshi_brier": 0.2015, "brier_diff_model_minus_kalshi": 0.0006}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.539, "slope": 0.838, "slope_se": 0.04}, "kalshi_slope": {"intercept": 0.216, "slope": 1.094, "slope_se": 0.044}, "n": 4314}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.511, "slope": 0.861, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.153, "slope": 1.073, "slope_se": 0.035}, "n": 6377}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 424, "model_brier": 0.3098, "kalshi_brier": 0.2355, "brier_diff_model_minus_kalshi": 0.0743, "brier_diff_se": 0.0148, "corr_model_outcome": 0.0452, "corr_kalshi_outcome": 0.2564}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
