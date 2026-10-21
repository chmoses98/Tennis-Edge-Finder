# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-21T16:13Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 47,208): 0-3 14.1%, 3-5 9.5%, 5-10 19.7%, 10-15 15.3%, 15-25 19.4%, 25-40 14.0%, 40+ 8.0%; median gap 12.07 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.1%, Challenger 12.3%, doubles 6.9%). Main tour: ATP 5.0% and WTA 4.6% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 10,391): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.0%, BOOK_QUALITY 18.8%, STALE_QUOTE 18.1%, POOR_DATA 9.1%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.5%, LIMITED_DATA 3.7%, IN_PLAY_QUOTE 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%. By class: coverage 34.0%, execution 18.8%, market_freshness 18.1%, data 12.9%, market_freshness/coverage 8.9%, mapping 4.5%, model_calibration_or_unknown 2.2%, model_calibration 0.7%.
* **Stale / settled / in-play**: 51.1% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.9% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 10,391 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.8% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.1%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.9% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 492.0 points vs 1701.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.043, Gen-2 0.844, Gen-1 ledger 0.869 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 505 model 0.2247 vs Kalshi 0.2096; n 102 model 0.2915 vs Kalshi 0.1869.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 201,945 model-market comparisons (328,360 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 68,873 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-21T16:00:12.676708+00:00'], shadow board 53,384 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-21T16:00:17.858471+00:00'], Model 4 25,345 rows, 18,335 settled tickers, 6,378 tickers with an external scan.
* By model: {"gen1_ledger": 46514, "gen1_elo": 26842, "fair_v1": 26842, "gen2": 26842, "gen1_sr": 26842, "model4_fundamental": 24045, "model4_conditioned": 24018}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 47,208 | 14.1 | 9.5 | 19.7 | 15.3 | 19.4 | 14.0 | 8.0 | 12.07 | 41.4% | 22.0% |
| MW fair_v1 | 26,842 | 13.1 | 8.6 | 18.3 | 15.7 | 20.0 | 14.9 | 9.5 | 13.14 | 44.4% | 24.4% |
| MW gen1_elo | 26,842 | 12.9 | 8.6 | 19.1 | 15.2 | 20.0 | 15.0 | 9.2 | 12.93 | 44.2% | 24.2% |
| MW gen1_ledger | 20,366 | 15.5 | 10.7 | 21.6 | 14.8 | 18.6 | 12.8 | 6.0 | 10.55 | 37.4% | 18.8% |
| MW gen1_sr | 26,842 | 9.9 | 7.1 | 16.6 | 13.9 | 21.3 | 18.8 | 12.3 | 15.96 | 52.4% | 31.1% |
| MW gen2 | 26,842 | 11.1 | 7.3 | 16.2 | 14.2 | 19.9 | 17.8 | 13.5 | 15.55 | 51.2% | 31.3% |
| all families model4_conditioned | 24,018 | 21.8 | 19.2 | 34.4 | 17.7 | 4.5 | 1.4 | 1.1 | 5.94 | 6.9% | 2.4% |
| all families model4_fundamental | 24,045 | 16.4 | 13.1 | 34.0 | 20.4 | 11.2 | 3.5 | 1.3 | 7.87 | 16.0% | 4.8% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.7%, >=15pp 41.4%, >=20pp 30.7%, >=25pp 22.0%, >=30pp 15.8%, >=40pp 8.0%, >=50pp 3.6%
Executable gap (model outside the book, before fees): median 8.43pp; >=10pp 45.2%, >=25pp 17.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,337 | 28.8 | 13.9 | 24.2 | 14.8 | 12.5 | 5.2 | 0.6 | 6.19 | 18.4% | 5.9% |
| CHALLENGER | 4,353 | 15.7 | 10.0 | 20.2 | 15.8 | 14.8 | 12.5 | 10.9 | 11.21 | 38.3% | 23.5% |
| ITF_MEN | 7,226 | 10.7 | 7.6 | 16.9 | 14.6 | 21.3 | 17.2 | 11.8 | 15.09 | 50.2% | 29.0% |
| ITF_WOMEN | 10,655 | 9.6 | 6.9 | 15.8 | 15.6 | 22.8 | 18.2 | 11.2 | 15.69 | 52.2% | 29.3% |
| WTA | 1,611 | 17.1 | 12.6 | 25.2 | 20.1 | 19.9 | 4.4 | 0.7 | 8.65 | 25.0% | 5.1% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,337 | 23.5 | 14.8 | 24.5 | 17.2 | 13.9 | 5.1 | 0.9 | 6.81 | 20.0% | 6.0% |
| CHALLENGER | 4,353 | 14.7 | 8.4 | 18.8 | 14.6 | 17.6 | 14.0 | 11.9 | 12.67 | 43.6% | 25.9% |
| ITF_MEN | 7,226 | 8.7 | 6.2 | 14.6 | 13.2 | 19.9 | 20.4 | 16.9 | 18.05 | 57.2% | 37.3% |
| ITF_WOMEN | 10,655 | 8.2 | 5.7 | 13.8 | 13.4 | 21.2 | 20.9 | 16.9 | 18.8 | 58.9% | 37.8% |
| WTA | 1,611 | 14.5 | 9.6 | 20.8 | 16.6 | 24.0 | 13.8 | 0.7 | 11.36 | 38.6% | 14.6% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,337 | 24.2 | 12.8 | 24.2 | 15.8 | 15.0 | 6.9 | 1.1 | 7.3 | 23.0% | 8.0% |
| CHALLENGER | 4,353 | 14.1 | 9.5 | 20.8 | 15.2 | 16.4 | 12.8 | 11.2 | 11.42 | 40.3% | 24.0% |
| ITF_MEN | 7,226 | 10.1 | 7.6 | 17.2 | 13.9 | 21.9 | 17.4 | 11.9 | 15.48 | 51.2% | 29.4% |
| ITF_WOMEN | 10,655 | 9.6 | 6.7 | 16.3 | 15.6 | 23.1 | 18.4 | 10.3 | 15.59 | 51.8% | 28.7% |
| WTA | 1,611 | 24.4 | 16.6 | 29.9 | 16.2 | 10.2 | 2.2 | 0.4 | 6.04 | 12.9% | 2.7% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,342 | 26.1 | 19.4 | 30.1 | 11.9 | 8.9 | 3.1 | 0.4 | 5.46 | 12.4% | 3.5% |
| CHALLENGER | 3,024 | 21.3 | 14.8 | 26.7 | 14.1 | 14.7 | 6.5 | 1.9 | 7.27 | 23.1% | 8.4% |
| DOUBLES | 1,482 | 5.2 | 4.2 | 11.6 | 10.3 | 20.5 | 26.2 | 22.0 | 24.07 | 68.7% | 48.2% |
| ITF_MEN | 5,697 | 13.9 | 8.8 | 20.3 | 15.9 | 21.0 | 13.3 | 6.7 | 12.09 | 41.1% | 20.1% |
| ITF_WOMEN | 6,912 | 12.6 | 9.0 | 19.3 | 15.1 | 21.6 | 16.3 | 6.0 | 12.85 | 44.0% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,028 | 22.3 | 15.9 | 29.6 | 18.2 | 10.1 | 3.6 | 0.3 | 6.97 | 14.0% | 3.9% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,276 | 29.1 | 14.1 | 24.6 | 14.7 | 12.3 | 4.8 | 0.5 | 6.04 | 17.6% | 5.3% |
| CHALLENGER | 3,077 | 20.4 | 12.3 | 24.9 | 18.3 | 15.2 | 6.8 | 2.0 | 8.41 | 24.1% | 8.8% |
| ITF_MEN | 5,330 | 12.9 | 9.1 | 20.1 | 16.4 | 22.1 | 14.1 | 5.2 | 12.27 | 41.4% | 19.3% |
| ITF_WOMEN | 8,010 | 11.3 | 8.2 | 17.9 | 17.7 | 24.6 | 15.3 | 5.0 | 13.47 | 44.9% | 20.3% |
| WTA | 1,566 | 17.3 | 12.4 | 25.2 | 20.3 | 19.9 | 4.3 | 0.7 | 8.62 | 24.8% | 5.0% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,276 | 23.9 | 15.1 | 24.6 | 17.0 | 13.9 | 4.8 | 0.7 | 6.58 | 19.4% | 5.5% |
| CHALLENGER | 3,077 | 18.5 | 10.7 | 23.3 | 17.5 | 17.9 | 9.8 | 2.3 | 9.46 | 30.0% | 12.1% |
| ITF_MEN | 5,331 | 10.3 | 7.4 | 16.8 | 14.9 | 21.9 | 18.6 | 10.1 | 15.28 | 50.5% | 28.6% |
| ITF_WOMEN | 8,011 | 9.2 | 6.5 | 15.1 | 14.9 | 23.2 | 20.4 | 10.7 | 16.55 | 54.3% | 31.1% |
| WTA | 1,566 | 14.5 | 9.6 | 20.8 | 16.5 | 24.0 | 13.9 | 0.8 | 11.36 | 38.7% | 14.7% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,301 | 26.4 | 19.7 | 30.2 | 12.1 | 8.4 | 3.0 | 0.2 | 5.38 | 11.6% | 3.2% |
| CHALLENGER | 2,635 | 22.8 | 15.9 | 28.4 | 14.0 | 14.0 | 4.4 | 0.6 | 6.68 | 19.0% | 4.9% |
| DOUBLES | 1,377 | 5.2 | 4.4 | 11.8 | 10.5 | 20.6 | 26.1 | 21.5 | 23.92 | 68.1% | 47.6% |
| ITF_MEN | 4,751 | 15.2 | 9.5 | 22.0 | 16.7 | 20.8 | 11.7 | 4.1 | 11.02 | 36.6% | 15.8% |
| ITF_WOMEN | 5,761 | 13.6 | 9.5 | 20.7 | 15.9 | 21.8 | 15.1 | 3.4 | 11.73 | 40.4% | 18.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 978 | 22.8 | 16.5 | 29.6 | 18.2 | 10.1 | 2.9 | 0.0 | 6.82 | 13.0% | 2.9% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,482 | 5.2 | 4.2 | 11.6 | 10.3 | 20.5 | 26.2 | 22.0 | 24.07 | 68.7% | 48.2% |
| singles | 18,884 | 16.3 | 11.2 | 22.4 | 15.2 | 18.4 | 11.8 | 4.7 | 10.03 | 34.9% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 6,044 | 13.2 | 8.8 | 19.0 | 15.7 | 18.9 | 14.9 | 9.4 | 12.88 | 43.2% | 24.3% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 16,817 | 13.4 | 8.6 | 18.3 | 15.3 | 20.1 | 14.8 | 9.5 | 13.14 | 44.4% | 24.2% |
| UNKNOWN | 3,744 | 11.3 | 7.9 | 17.1 | 17.1 | 20.8 | 15.7 | 10.0 | 13.68 | 46.5% | 25.8% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,587 | 19.7 | 11.6 | 21.2 | 16.6 | 15.9 | 9.0 | 6.0 | 9.25 | 30.9% | 15.0% |
| B | 3,388 | 12.5 | 9.0 | 20.0 | 17.1 | 19.0 | 12.1 | 10.3 | 12.22 | 41.5% | 22.4% |
| C | 3,768 | 11.9 | 9.0 | 19.1 | 15.0 | 19.7 | 15.2 | 10.2 | 13.25 | 45.1% | 25.4% |
| D | 4,381 | 12.2 | 7.8 | 17.0 | 15.5 | 22.1 | 15.8 | 9.6 | 14.03 | 47.4% | 25.4% |
| F | 7,718 | 7.8 | 5.6 | 15.1 | 14.5 | 23.4 | 21.4 | 12.2 | 17.71 | 57.0% | 33.6% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,741 | 23.1 | 15.8 | 28.7 | 15.1 | 11.8 | 4.1 | 1.5 | 6.68 | 17.3% | 5.6% |
| B | 2,816 | 16.2 | 10.5 | 23.6 | 16.2 | 19.0 | 10.7 | 3.9 | 9.95 | 33.6% | 14.6% |
| C | 4,022 | 11.3 | 7.4 | 18.5 | 14.2 | 21.3 | 16.5 | 10.8 | 14.25 | 48.6% | 27.2% |
| D | 2,918 | 14.4 | 9.8 | 19.8 | 14.4 | 20.9 | 14.5 | 6.1 | 12.04 | 41.6% | 20.6% |
| F | 4,869 | 10.2 | 8.1 | 15.6 | 14.6 | 22.7 | 20.5 | 8.4 | 15.83 | 51.5% | 28.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 8,632 | 17.9 | 10.4 | 20.5 | 16.7 | 16.4 | 9.8 | 8.4 | 10.37 | 34.6% | 18.2% |
| LIMITED | 5,854 | 13.7 | 10.3 | 20.2 | 15.7 | 19.2 | 13.5 | 7.5 | 11.8 | 40.2% | 21.0% |
| POOR | 12,356 | 9.4 | 6.5 | 15.8 | 15.0 | 22.9 | 19.2 | 11.3 | 16.1 | 53.3% | 30.4% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,145 | 26.6 | 20.6 | 34.3 | 12.2 | 4.6 | 1.5 | 0.2 | 5.25 | 6.3% | 1.7% |
| GAME_SPREAD | 4,445 | 22.6 | 15.3 | 33.3 | 17.2 | 8.9 | 2.4 | 0.3 | 6.6 | 11.6% | 2.7% |
| MATCH_WINNER | 20,366 | 15.5 | 10.7 | 21.6 | 14.8 | 18.6 | 12.8 | 6.0 | 10.55 | 37.4% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 9,367 | 29.7 | 16.9 | 30.6 | 12.6 | 8.2 | 1.7 | 0.4 | 5.44 | 10.3% | 2.1% |
| TOTAL_GAMES | 7,167 | 8.3 | 9.4 | 36.4 | 29.1 | 10.7 | 3.3 | 2.7 | 9.54 | 16.8% | 6.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,390 | 25.3 | 34.4 | 32.4 | 4.1 | 3.1 | 0.6 | 0.2 | 4.47 | 3.8% | 0.7% |
| GAME_SPREAD | 5,752 | 45.6 | 17.1 | 26.9 | 7.7 | 1.8 | 0.7 | 0.2 | 3.46 | 2.7% | 0.9% |
| TOTAL_GAMES | 9,876 | 4.8 | 7.5 | 40.5 | 35.2 | 7.2 | 2.5 | 2.3 | 9.72 | 12.0% | 4.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,393 | 24.2 | 17.9 | 35.3 | 12.4 | 7.3 | 2.6 | 0.3 | 5.81 | 10.1% | 2.9% |
| GAME_SPREAD | 5,755 | 19.3 | 13.1 | 28.1 | 20.1 | 14.2 | 4.4 | 0.9 | 7.98 | 19.5% | 5.3% |
| TOTAL_GAMES | 9,897 | 8.2 | 9.0 | 36.4 | 27.4 | 12.8 | 3.8 | 2.5 | 9.59 | 19.0% | 6.2% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 26,842 | 44.4% | 24.4% | 13.14 | 36.1% | 15.4% | 10.97 |
| gen1_elo | 26,842 | 44.2% | 24.2% | 12.93 | 35.7% | 15.5% | 10.58 |
| gen1_sr | 26,842 | 52.4% | 31.1% | 15.96 | 44.9% | 22.1% | 13.25 |
| gen2 | 26,842 | 51.2% | 31.3% | 15.55 | 44.8% | 23.5% | 13.17 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 13,989 | 15.8 | 10.3 | 21.1 | 17.2 | 20.4 | 11.9 | 3.3 | 10.8 | 35.5% | 15.2% |
| STALE | 12,853 | 10.1 | 6.6 | 15.3 | 13.9 | 19.6 | 18.2 | 16.3 | 17.01 | 54.1% | 34.5% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 13,834 | 16.6 | 11.2 | 22.4 | 14.9 | 17.7 | 12.2 | 4.9 | 9.93 | 34.8% | 17.1% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 47,208 | 13834 | 17461 | 15913 | 23.9 | 126.9 | 1400.4 |
| ge_15pp | 19,536 | 4815 | 6259 | 8462 | 25.7 | 415.9 | 1380.4 |
| ge_25pp | 10,391 | 2367 | 2714 | 5310 | 31.1 | 561.1 | 1380.4 |
| lt_10pp | 20,442 | 6958 | 8239 | 5245 | 21.8 | 47.4 | 1341.5 |

Current slate `SL-20261021T161333Z-3d6a3a9e`: 521 priced rows, quote age at build {'median': 13.7, 'max': 13.7}, freshness {'AGING': 521}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 22 | 0.0 | 0.0 | 22.7 | 4.5 | 40.9 | 31.8 | 0.0 | 20.48 | 72.7% | 31.8% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,496 | 19.8 | 10.8 | 23.6 | 18.7 | 19.1 | 7.3 | 0.7 | 9.12 | 27.1% | 8.1% |
| KALSHI_LONE_OUTLIER | 17 | 5.9 | 5.9 | 76.5 | 0.0 | 5.9 | 5.9 | 0.0 | 6.11 | 11.8% | 5.9% |
| MARKETS_AGREE | 467 | 66.2 | 33.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.21 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,052 | 0.0 | 2.3 | 33.6 | 26.1 | 26.2 | 10.8 | 0.9 | 12.8 | 37.9% | 11.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 26,842 | 4066 (15.2%) | 25.9% | 0.9% | {"EXTERNAL_STALE": 2496, "AGREES_WITH_KALSHI": 1052, "ALL_AGREE": 467, "SUPPORTS_MODEL_DIRECTION": 21, "AGREES_WITH_MODEL": 17, "EXTERNAL_OUTLIER": 12, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 11,922 | 1094 (9.2%) | 36.5% | 1.7% | {"EXTERNAL_STALE": 677, "AGREES_WITH_KALSHI": 399, "SUPPORTS_MODEL_DIRECTION": 16, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 6,562 | 332 (5.1%) | 37.0% | 2.4% | {"EXTERNAL_STALE": 201, "AGREES_WITH_KALSHI": 123, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,219 | 311 (9.7%) | 37.6% | 2.6% | {"EXTERNAL_STALE": 186, "AGREES_WITH_KALSHI": 117, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 10,715 | 2229 (20.8%) | 17.0% | 0.9% | {"EXTERNAL_STALE": 1352, "ALL_AGREE": 467, "AGREES_WITH_KALSHI": 378, "AGREES_WITH_MODEL": 15, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 4, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,133 | 10.7 | 7.7 | 19.3 | 14.5 | 22.3 | 15.7 | 9.8 | 14.01 | 47.9% | 25.6% |
| 4-10x | 3,504 | 11.2 | 8.5 | 18.8 | 15.5 | 21.1 | 14.9 | 10.0 | 13.67 | 46.0% | 24.8% |
| <2x | 13,717 | 15.1 | 9.6 | 18.8 | 16.7 | 18.1 | 13.2 | 8.6 | 11.93 | 39.9% | 21.7% |
| >=10x | 4,488 | 11.2 | 6.3 | 15.2 | 14.1 | 22.0 | 19.4 | 11.8 | 16.23 | 53.2% | 31.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 6,780 | 12.4 | 8.5 | 19.5 | 16.3 | 19.6 | 13.5 | 10.1 | 12.91 | 43.3% | 23.6% |
| 300-1000 | 5,835 | 11.8 | 8.8 | 16.9 | 15.4 | 20.9 | 16.3 | 9.8 | 13.97 | 47.1% | 26.2% |
| <300 | 8,646 | 9.0 | 5.7 | 15.4 | 14.7 | 23.0 | 20.2 | 11.9 | 16.86 | 55.2% | 32.1% |
| >=3000 | 5,581 | 21.6 | 12.7 | 22.7 | 16.6 | 14.6 | 7.0 | 4.8 | 8.07 | 26.3% | 11.7% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 783 | 0.5464 | 0.4094 | 0.5006 | +0.046 | -0.091 | -0.0034 ± 0.0055 |
| ratio 4-10x | 539 | 0.5852 | 0.4395 | 0.4935 | +0.092 | -0.054 | 0.013 ± 0.007 |
| ratio <2x | 1935 | 0.5368 | 0.4131 | 0.4475 | +0.089 | -0.034 | 0.0129 ± 0.0032 |
| ratio >=10x | 690 | 0.567 | 0.3912 | 0.4638 | +0.103 | -0.072 | 0.0055 ± 0.007 |
| thinner_sample 1000-3000 | 1067 | 0.5418 | 0.4144 | 0.4489 | +0.093 | -0.035 | 0.0105 ± 0.0044 |
| thinner_sample 300-1000 | 915 | 0.5657 | 0.4231 | 0.4973 | +0.068 | -0.074 | 0.0002 ± 0.0053 |
| thinner_sample <300 | 1312 | 0.5549 | 0.3891 | 0.4611 | +0.094 | -0.072 | 0.0097 ± 0.0049 |
| thinner_sample >=3000 | 653 | 0.5349 | 0.4396 | 0.4671 | +0.068 | -0.028 | 0.0137 ± 0.0046 |
| data_status ADEQUATE | 1123 | 0.5372 | 0.4313 | 0.4533 | +0.084 | -0.022 | 0.013 ± 0.0037 |
| data_status LIMITED | 938 | 0.5499 | 0.4171 | 0.4787 | +0.071 | -0.062 | 0.0045 ± 0.0049 |
| data_status POOR | 1886 | 0.5588 | 0.3983 | 0.4698 | +0.089 | -0.071 | 0.0075 ± 0.004 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 579 | 0.1976 | 0.199 | -0.0013 ± 0.0006 | 0.574 | 0.5768 | 0.4989 | 0.4841 | 0.5354 | -0.052 ± 0.0192 | -0.01 (5) |
| 3-5 | 372 | 0.2016 | 0.201 | +0.0006 ± 0.0019 | 0.5866 | 0.5836 | 0.5013 | 0.4612 | 0.4731 | -0.094 ± 0.0238 | 0.02 (1) |
| 5-10 | 806 | 0.2031 | 0.2028 | +0.0002 ± 0.0024 | 0.5922 | 0.5895 | 0.5133 | 0.4388 | 0.4702 | -0.088 ± 0.0165 | -0.0167 (6) |
| 10-15 | 685 | 0.2128 | 0.2039 | +0.0090 ± 0.0043 | 0.6151 | 0.5891 | 0.5242 | 0.4002 | 0.4248 | -0.100 ± 0.0172 | -0.048 (5) |
| 15-25 | 898 | 0.2237 | 0.2137 | +0.0100 ± 0.006 | 0.6422 | 0.6114 | 0.5751 | 0.3794 | 0.4521 | -0.083 ± 0.0152 | -0.0033 (9) |
| 25-40 | 505 | 0.2247 | 0.2096 | +0.0151 ± 0.0121 | 0.6374 | 0.6026 | 0.6574 | 0.3479 | 0.4752 | -0.074 ± 0.0187 | -0.01 (1) |
| 40+ | 102 | 0.2915 | 0.1869 | +0.1046 ± 0.0378 | 0.7955 | 0.5569 | 0.7502 | 0.3025 | 0.4118 | -0.100 ± 0.037 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2917 | 0.1832 | 0.1843 | -0.0010 ± 0.0003 | 0.5408 | 0.5418 | 0.4842 | 0.4691 | 0.505 | -0.020 ± 0.008 | -0.0129 (17) |
| 3-5 | 1930 | 0.1995 | 0.1981 | +0.0014 ± 0.0008 | 0.5802 | 0.5736 | 0.4848 | 0.4449 | 0.4466 | -0.055 ± 0.0103 | 0.0 (2) |
| 5-10 | 4078 | 0.1979 | 0.1948 | +0.0031 ± 0.001 | 0.5786 | 0.5687 | 0.4831 | 0.4091 | 0.4245 | -0.047 ± 0.007 | -0.0119 (21) |
| 10-15 | 3540 | 0.2015 | 0.1836 | +0.0179 ± 0.0018 | 0.5901 | 0.5398 | 0.4857 | 0.3612 | 0.3511 | -0.074 ± 0.0072 | -0.0281 (16) |
| 15-25 | 4474 | 0.2073 | 0.1704 | +0.0369 ± 0.0024 | 0.6078 | 0.5041 | 0.5008 | 0.3044 | 0.3093 | -0.068 ± 0.0061 | -0.0025 (44) |
| 25-40 | 3434 | 0.2241 | 0.1311 | +0.0930 ± 0.0039 | 0.6425 | 0.4007 | 0.5333 | 0.2204 | 0.2312 | -0.061 ± 0.006 | -0.01 (1) |
| 40+ | 2212 | 0.3793 | 0.045 | +0.3343 ± 0.0051 | 0.9878 | 0.1749 | 0.6315 | 0.1072 | 0.0628 | -0.081 ± 0.0042 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 439 | 0.2037 | 0.2043 | -0.0005 ± 0.0008 | 0.5895 | 0.5905 | 0.5043 | 0.4894 | 0.508 | -0.101 ± 0.0232 | -0.01 (3) |
| 3-5 | 321 | 0.2207 | 0.2197 | +0.0010 ± 0.0021 | 0.6267 | 0.6247 | 0.5129 | 0.4728 | 0.4735 | -0.105 ± 0.0282 | 0.02 (1) |
| 5-10 | 698 | 0.2025 | 0.2033 | -0.0008 ± 0.0026 | 0.5897 | 0.5913 | 0.5456 | 0.4707 | 0.5143 | -0.072 ± 0.0175 | -0.01 (4) |
| 10-15 | 650 | 0.2167 | 0.2105 | +0.0063 ± 0.0045 | 0.6234 | 0.6069 | 0.5634 | 0.4391 | 0.4785 | -0.098 ± 0.0186 | -0.04 (5) |
| 15-25 | 938 | 0.2299 | 0.2094 | +0.0205 ± 0.0059 | 0.6528 | 0.601 | 0.5909 | 0.3947 | 0.4446 | -0.100 ± 0.0152 | -0.0133 (9) |
| 25-40 | 659 | 0.2612 | 0.2015 | +0.0596 ± 0.011 | 0.7293 | 0.5851 | 0.6569 | 0.341 | 0.4067 | -0.105 ± 0.0171 | -0.0075 (4) |
| 40+ | 242 | 0.361 | 0.1692 | +0.1919 ± 0.0262 | 0.9972 | 0.5074 | 0.733 | 0.2502 | 0.3058 | -0.080 ± 0.0253 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2451 | 0.1927 | 0.1928 | -0.0001 ± 0.0003 | 0.563 | 0.5629 | 0.5071 | 0.4922 | 0.5039 | -0.046 ± 0.0092 | -0.0133 (15) |
| 3-5 | 1646 | 0.2008 | 0.2004 | +0.0003 ± 0.0009 | 0.5804 | 0.5789 | 0.5113 | 0.4713 | 0.486 | -0.039 ± 0.0113 | 0.02 (1) |
| 5-10 | 3642 | 0.1937 | 0.1929 | +0.0008 ± 0.0011 | 0.5703 | 0.5642 | 0.5031 | 0.4292 | 0.4618 | -0.029 ± 0.0074 | -0.0117 (6) |
| 10-15 | 3192 | 0.1991 | 0.1886 | +0.0105 ± 0.0019 | 0.5853 | 0.55 | 0.5129 | 0.3887 | 0.4098 | -0.049 ± 0.0078 | -0.0189 (18) |
| 15-25 | 4512 | 0.2161 | 0.1784 | +0.0378 ± 0.0025 | 0.6286 | 0.5242 | 0.5282 | 0.332 | 0.3367 | -0.070 ± 0.0063 | -0.0086 (42) |
| 25-40 | 4030 | 0.2507 | 0.1412 | +0.1095 ± 0.0038 | 0.7067 | 0.4306 | 0.5624 | 0.246 | 0.2342 | -0.080 ± 0.0059 | -0.0044 (18) |
| 40+ | 3112 | 0.3968 | 0.0626 | +0.3343 ± 0.0051 | 1.0452 | 0.2223 | 0.6561 | 0.1215 | 0.0887 | -0.071 ± 0.0044 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 554 | 0.1972 | 0.1996 | -0.0024 ± 0.0007 | 0.5743 | 0.58 | 0.4955 | 0.4802 | 0.5542 | -0.014 ± 0.0193 | -0.0137 (8) |
| 3-5 | 402 | 0.1982 | 0.1962 | +0.0020 ± 0.0018 | 0.5753 | 0.5706 | 0.5032 | 0.4635 | 0.4602 | -0.117 ± 0.0229 | 0.0067 (3) |
| 5-10 | 837 | 0.2027 | 0.1992 | +0.0035 ± 0.0023 | 0.5927 | 0.5806 | 0.51 | 0.436 | 0.4468 | -0.101 ± 0.0159 | -0.0071 (7) |
| 10-15 | 688 | 0.209 | 0.2058 | +0.0032 ± 0.0043 | 0.6054 | 0.594 | 0.5394 | 0.4161 | 0.4666 | -0.084 ± 0.0172 | -0.0317 (6) |
| 15-25 | 834 | 0.231 | 0.2122 | +0.0188 ± 0.0062 | 0.6606 | 0.6074 | 0.5832 | 0.3894 | 0.4376 | -0.108 ± 0.0158 | -0.03 (1) |
| 25-40 | 526 | 0.2139 | 0.2171 | -0.0032 ± 0.0119 | 0.6152 | 0.62 | 0.6666 | 0.3548 | 0.5133 | -0.051 ± 0.0183 | 0.015 (2) |
| 40+ | 106 | 0.3012 | 0.2027 | +0.0985 ± 0.0386 | 0.8237 | 0.5925 | 0.7598 | 0.3095 | 0.434 | -0.081 ± 0.0399 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2848 | 0.1871 | 0.1879 | -0.0008 ± 0.0003 | 0.5491 | 0.5505 | 0.4908 | 0.4756 | 0.4944 | -0.034 ± 0.0082 | -0.0163 (35) |
| 3-5 | 1946 | 0.1908 | 0.1882 | +0.0026 ± 0.0008 | 0.5597 | 0.5534 | 0.4842 | 0.4446 | 0.4327 | -0.072 ± 0.0101 | -0.0094 (18) |
| 5-10 | 4258 | 0.1965 | 0.1907 | +0.0058 ± 0.001 | 0.577 | 0.5579 | 0.4854 | 0.4115 | 0.4086 | -0.062 ± 0.0067 | -0.01 (31) |
| 10-15 | 3384 | 0.1964 | 0.1804 | +0.0160 ± 0.0018 | 0.5774 | 0.5311 | 0.501 | 0.3775 | 0.3747 | -0.069 ± 0.0073 | -0.015 (12) |
| 15-25 | 4574 | 0.2111 | 0.1728 | +0.0383 ± 0.0024 | 0.6166 | 0.5097 | 0.5088 | 0.3142 | 0.3131 | -0.073 ± 0.0061 | -0.03 (2) |
| 25-40 | 3431 | 0.2204 | 0.1325 | +0.0879 ± 0.0039 | 0.6347 | 0.4032 | 0.536 | 0.2197 | 0.2405 | -0.055 ± 0.0059 | 0.01 (3) |
| 40+ | 2144 | 0.3946 | 0.0502 | +0.3444 ± 0.0055 | 1.0307 | 0.1884 | 0.6445 | 0.1141 | 0.0681 | -0.083 ± 0.0046 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 919 | 0.1958 | 0.196 | -0.0002 ± 0.0005 | 0.5712 | 0.5713 | 0.5068 | 0.4917 | 0.494 | -0.059 ± 0.0148 | -0.0224 (49) |
| 3-5 | 645 | 0.1918 | 0.1912 | +0.0006 ± 0.0014 | 0.5606 | 0.5582 | 0.4853 | 0.4455 | 0.4558 | -0.053 ± 0.0174 | -0.0194 (34) |
| 5-10 | 1363 | 0.2002 | 0.1939 | +0.0063 ± 0.0018 | 0.5891 | 0.5697 | 0.494 | 0.4206 | 0.416 | -0.072 ± 0.0121 | -0.005 (78) |
| 10-15 | 895 | 0.2095 | 0.1987 | +0.0107 ± 0.0037 | 0.607 | 0.5796 | 0.5167 | 0.3935 | 0.4101 | -0.064 ± 0.0152 | 0.0014 (64) |
| 15-25 | 1189 | 0.2315 | 0.2106 | +0.0209 ± 0.0052 | 0.6609 | 0.6065 | 0.5724 | 0.3777 | 0.423 | -0.066 ± 0.0133 | -0.0214 (59) |
| 25-40 | 727 | 0.2482 | 0.205 | +0.0432 ± 0.0103 | 0.7041 | 0.5903 | 0.6659 | 0.3531 | 0.4388 | -0.083 ± 0.0157 | -0.0219 (26) |
| 40+ | 247 | 0.3535 | 0.1963 | +0.1573 ± 0.028 | 1.0213 | 0.5742 | 0.8062 | 0.3221 | 0.4211 | -0.090 ± 0.0252 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2996 | 0.1838 | 0.1839 | -0.0001 ± 0.0003 | 0.5405 | 0.54 | 0.5069 | 0.4916 | 0.4987 | -0.040 ± 0.0079 | -0.0157 (88) |
| 3-5 | 2075 | 0.1906 | 0.1886 | +0.0021 ± 0.0008 | 0.5574 | 0.5531 | 0.4906 | 0.4509 | 0.4443 | -0.055 ± 0.0096 | -0.0209 (69) |
| 5-10 | 4188 | 0.1978 | 0.1891 | +0.0088 ± 0.001 | 0.5812 | 0.5559 | 0.4898 | 0.4162 | 0.3964 | -0.074 ± 0.0068 | -0.0082 (132) |
| 10-15 | 2898 | 0.206 | 0.1911 | +0.0149 ± 0.002 | 0.6005 | 0.5609 | 0.5235 | 0.4004 | 0.401 | -0.061 ± 0.0081 | -0.0053 (105) |
| 15-25 | 3576 | 0.2293 | 0.198 | +0.0313 ± 0.0029 | 0.6613 | 0.5753 | 0.5648 | 0.3695 | 0.3887 | -0.066 ± 0.0075 | -0.0253 (107) |
| 25-40 | 2518 | 0.2587 | 0.1827 | +0.0760 ± 0.0054 | 0.7332 | 0.5339 | 0.6278 | 0.3133 | 0.3523 | -0.076 ± 0.0083 | -0.0229 (51) |
| 40+ | 1133 | 0.3797 | 0.1399 | +0.2398 ± 0.0117 | 1.0776 | 0.424 | 0.727 | 0.2235 | 0.2507 | -0.076 ± 0.0104 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3947 | 1.043 ± 0.045 | 1.149 | 0.1677 | 0.1652 | 0.2136 | 0.2052 |
| gen2 | 3947 | 0.844 ± 0.041 | 1.108 | 0.1704 | 0.1658 | 0.2325 | 0.205 |
| gen1_elo | 3947 | 1.021 ± 0.043 | 1.134 | 0.1744 | 0.1654 | 0.2127 | 0.2053 |
| gen1_sr | 3947 | 1.041 ± 0.054 | 1.179 | 0.131 | 0.1678 | 0.2288 | 0.2046 |
| gen1_ledger | 5985 | 0.869 ± 0.031 | 1.077 | 0.1815 | 0.1802 | 0.2184 | 0.1994 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 19,536)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,427 | 22.7% |
| STALE_QUOTE | market_freshness | 4,113 | 21.1% |
| BOOK_QUALITY | execution | 3,734 | 19.1% |
| POOR_DATA | data | 2,256 | 11.6% |
| LIMITED_DATA | data | 1,272 | 6.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,061 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 952 | 4.9% |
| IDENTITY_AMBIGUOUS | mapping | 819 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 578 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 324 | 1.7% |

Cause class: coverage 22.7%, market_freshness 21.1%, execution 19.1%, data 18.1%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.9%, mapping 4.2%, model_calibration 1.7%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 94.2%, LOW_DATA_QUALITY 70.9%, THIN_PLAYER_HISTORY 59.6%, STALE_PLAYER_DATA 51.8%, STALE_KALSHI_QUOTE 43.3%, MODEL_INTERNAL_DISAGREEMENT 42.0%, ASYMMETRIC_SAMPLE_SIZE 33.0%, WIDE_SPREAD 25.2%, MODEL_HIGH_UNCERTAINTY 17.8%, PLAYER_IDENTITY_RISK 15.8%, LEVEL_TRANSFER_RISK 10.8%, EVENT_MAPPING_RISK 8.1%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 3.1%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.2%, POST_SETTLEMENT_OBSERVATION 22.7%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 10,391)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,530 | 34.0% |
| BOOK_QUALITY | execution | 1,951 | 18.8% |
| STALE_QUOTE | market_freshness | 1,877 | 18.1% |
| POOR_DATA | data | 949 | 9.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 563 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 466 | 4.5% |
| LIMITED_DATA | data | 388 | 3.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 365 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 227 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 75 | 0.7% |

Cause class: coverage 34.0%, execution 18.8%, market_freshness 18.1%, data 12.9%, market_freshness/coverage 8.9%, mapping 4.5%, model_calibration_or_unknown 2.2%, model_calibration 0.7%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.1%, LOW_DATA_QUALITY 74.7%, THIN_PLAYER_HISTORY 62.1%, STALE_KALSHI_QUOTE 51.1%, STALE_PLAYER_DATA 46.9%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 34.5%, WIDE_SPREAD 24.8%, PLAYER_IDENTITY_RISK 19.2%, MODEL_HIGH_UNCERTAINTY 18.1%, EVENT_MAPPING_RISK 9.9%, LEVEL_TRANSFER_RISK 9.7%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 5.0%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.0%, POST_SETTLEMENT_OBSERVATION 34.0%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 8131, "IDENTITY_AMBIGUOUS": 2260}; ticker orientation: {"VERIFIED": 10391}.

Checks: discipline:AMBIGUOUS 714, discipline:PASS 9677, identity_confidence:AMBIGUOUS 1993, identity_confidence:PASS 8398, level_mapping:NA 726, level_mapping:PASS 9665, market_pair:AMBIGUOUS 374, market_pair:NA 252, market_pair:PASS 9765, model_complement:NA 219, model_complement:PASS 10172, namesake:PASS 10391, physical_match_id:NA 3829, physical_match_id:PASS 6562, player_ids:PASS 10391, same_pair_other_event:PASS 10391, ticker_orientation:PASS 10391

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,679 | 5.0% | 4.6% | 1.8% | {"market_freshness": 53, "model_calibration_or_unknown": 43, "data": 35, "execution": 19, "market_freshness/coverage": 13, "model_calibration": 13, "coverage": 8} | 5.86 | 0.2271 / 0.2178 (413) | 18.5% | 4.0% | 3.4% | 2.8% |
| CHALLENGER | 7,377 | 17.3% | 7.0% | 12.3% | {"coverage": 715, "market_freshness/coverage": 158, "market_freshness": 147, "data": 125, "model_calibration_or_unknown": 59, "execution": 30, "model_calibration": 27, "mapping": 14} | 7.45 | 0.2177 / 0.2068 (1782) | 34.9% | 17.3% | 3.9% | 22.6% |
| DOUBLES | 1,482 | 48.2% | 47.6% | 6.9% | {"execution": 365, "mapping": 184, "market_freshness": 106, "market_freshness/coverage": 52, "coverage": 7} | 23.92 | 0.3192 / 0.2353 (380) | 15.8% | 0.0% | 100.0% | 7.1% |
| ITF_MEN | 12,923 | 25.1% | 17.6% | 31.1% | {"coverage": 1185, "execution": 646, "market_freshness": 529, "data": 444, "market_freshness/coverage": 274, "mapping": 156, "model_calibration_or_unknown": 2, "model_calibration": 1} | 11.66 | 0.2141 / 0.1956 (2951) | 36.5% | 67.3% | 18.0% | 22.0% |
| ITF_WOMEN | 17,567 | 26.6% | 19.6% | 45.0% | {"coverage": 1596, "market_freshness": 964, "execution": 860, "data": 699, "market_freshness/coverage": 382, "mapping": 106, "model_calibration_or_unknown": 55, "model_calibration": 11} | 12.83 | 0.2031 / 0.1949 (3441) | 38.2% | 57.3% | 10.0% | 21.6% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,639 | 4.6% | 4.2% | 1.2% | {"market_freshness": 38, "model_calibration_or_unknown": 27, "execution": 17, "model_calibration": 12, "data": 11, "market_freshness/coverage": 10, "coverage": 6, "mapping": 1} | 7.89 | 0.2379 / 0.2309 (435) | 23.8% | 1.3% | 1.4% | 3.6% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.7% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 311 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 769 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 15 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 16 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 17 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 18 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 19 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 20 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 21 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 365 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 22 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 23 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 24 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 25 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 26 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 27 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 28 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 29 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 30 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 31 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 32 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 33 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 34 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 12.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 768 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 36 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 37 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 38 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 39 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 41 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 468 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 42 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 43 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 44 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 45 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 46 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 47 | `KXITFWMATCH-26OCT20CHAAPI-CHA` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 555 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 122.0, ratio 20.3); no external reference |
| 48 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 535 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |
| 49 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 547 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 50 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9705, "by_level_share_of_ge_25pp": {"ATP": 0.0177, "CHALLENGER": 0.1227, "DOUBLES": 0.0687, "ITF_MEN": 0.3115, "ITF_WOMEN": 0.4497, "OTHER": 0.0012, "WTA": 0.0117, "WTA125": 0.0167}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.511, "share_primary_cause_market_settled_or_in_play": 0.429, "share_primary_cause_stale_quote_only": 0.1806}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 10391, "identity_ambiguous_share": 0.2175, "ticker_orientation": {"VERIFIED": 10391}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 6562, "with_external": 332, "coverage": 0.0506, "external_status": {"EXTERNAL_STALE": 201, "AGREES_WITH_KALSHI": 123, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 201, "MODEL_LONE_OUTLIER": 123, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3705, "share_external_supports_model": 0.0241}, "pregame_clean_ge_25pp": {"n": 3219, "with_external": 311, "coverage": 0.0966, "external_status": {"EXTERNAL_STALE": 186, "AGREES_WITH_KALSHI": 117, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 186, "MODEL_LONE_OUTLIER": 117, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3762, "share_external_supports_model": 0.0257}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 492.0, "median_sample_ratio": 2.44, "median_min_matches": 20.0, "median_max_days_since_last": 224.0, "share_severe_asymmetry": 0.211, "data_status": {"POOR": 5783, "LIMITED": 2805, "ADEQUATE": 1803}, "comparison_lt_10pp": {"median_thinner_serve_points": 1701.0, "median_sample_ratio": 1.7, "median_min_matches": 92.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 783, "model_minus_observed": 0.0457, "kalshi_minus_observed": -0.0912, "brier_diff_model_minus_kalshi": -0.0034}, "4-10x": {"n": 539, "model_minus_observed": 0.0917, "kalshi_minus_observed": -0.054, "brier_diff_model_minus_kalshi": 0.013}, "<2x": {"n": 1935, "model_minus_observed": 0.0892, "kalshi_minus_observed": -0.0344, "brier_diff_model_minus_kalshi": 0.0129}, ">=10x": {"n": 690, "model_minus_observed": 0.1032, "kalshi_minus_observed": -0.0725, "brier_diff_model_minus_kalshi": 0.0055}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3947, "model": {"intercept": -0.532, "slope": 0.844, "slope_se": 0.041}, "kalshi_mid_same_rows": {"intercept": 0.236, "slope": 1.108, "slope_se": 0.046}, "mean_extremity_model": 0.1704, "mean_extremity_kalshi": 0.1658, "model_brier": 0.2325, "kalshi_brier": 0.205, "brier_diff_model_minus_kalshi": 0.0275, "brier_diff_se": 0.003, "model_logloss": 0.6615, "kalshi_logloss": 0.5926}, "fair_v1": {"n": 3947, "model": {"intercept": -0.402, "slope": 1.043, "slope_se": 0.045}, "kalshi_mid_same_rows": {"intercept": 0.318, "slope": 1.149, "slope_se": 0.047}, "mean_extremity_model": 0.1677, "mean_extremity_kalshi": 0.1652, "model_brier": 0.2136, "kalshi_brier": 0.2052, "brier_diff_model_minus_kalshi": 0.0084, "brier_diff_se": 0.0025, "model_logloss": 0.6154, "kalshi_logloss": 0.5928}, "gen1_elo": {"n": 3947, "model": {"intercept": -0.393, "slope": 1.021, "slope_se": 0.043}, "kalshi_mid_same_rows": {"intercept": 0.318, "slope": 1.134, "slope_se": 0.046}, "mean_extremity_model": 0.1744, "mean_extremity_kalshi": 0.1654, "model_brier": 0.2127, "kalshi_brier": 0.2053, "brier_diff_model_minus_kalshi": 0.0074, "brier_diff_se": 0.0025, "model_logloss": 0.6141, "kalshi_logloss": 0.5931}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2445, "share_ge_15": 0.4442, "median_abs_gap": 13.14, "n": 26842}, "gen1_elo": {"share_ge_25": 0.242, "share_ge_15": 0.4418, "median_abs_gap": 12.93, "n": 26842}, "gen1_sr": {"share_ge_25": 0.3111, "share_ge_15": 0.5243, "median_abs_gap": 15.96, "n": 26842}, "gen2": {"share_ge_25": 0.3132, "share_ge_15": 0.5125, "median_abs_gap": 15.55, "n": 26842}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.154, "share_ge_15": 0.3615, "median_abs_gap": 10.97, "n": 20893}, "gen1_elo": {"share_ge_25": 0.1551, "share_ge_15": 0.3566, "median_abs_gap": 10.58, "n": 20890}, "gen1_sr": {"share_ge_25": 0.2205, "share_ge_15": 0.4488, "median_abs_gap": 13.25, "n": 20894}, "gen2": {"share_ge_25": 0.2355, "share_ge_15": 0.4475, "median_abs_gap": 13.17, "n": 20895}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.86, "share_ge_25_all": 0.05, "share_ge_25_pregame_clean": 0.0456}, "WTA": {"median_abs_gap_pregame_clean": 7.89, "share_ge_25_all": 0.0462, "share_ge_25_pregame_clean": 0.0417}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2359, "share_within_10pp_all": 0.433, "share_within_10pp_pregame_clean": 0.4848, "corr_model_vs_mid_pregame_clean": 0.8447}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 579, "model_brier": 0.1976, "kalshi_brier": 0.199, "brier_diff_model_minus_kalshi": -0.0013}, "10-15": {"n_settled": 685, "model_brier": 0.2128, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.009}, "15-25": {"n_settled": 898, "model_brier": 0.2237, "kalshi_brier": 0.2137, "brier_diff_model_minus_kalshi": 0.01}, "25-40": {"n_settled": 505, "model_brier": 0.2247, "kalshi_brier": 0.2096, "brier_diff_model_minus_kalshi": 0.0151}, "3-5": {"n_settled": 372, "model_brier": 0.2016, "kalshi_brier": 0.201, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 102, "model_brier": 0.2915, "kalshi_brier": 0.1869, "brier_diff_model_minus_kalshi": 0.1046}, "5-10": {"n_settled": 806, "model_brier": 0.2031, "kalshi_brier": 0.2028, "brier_diff_model_minus_kalshi": 0.0002}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.532, "slope": 0.844, "slope_se": 0.041}, "kalshi_slope": {"intercept": 0.236, "slope": 1.108, "slope_se": 0.046}, "n": 3947}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.513, "slope": 0.869, "slope_se": 0.031}, "kalshi_slope": {"intercept": 0.155, "slope": 1.077, "slope_se": 0.036}, "n": 5985}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 380, "model_brier": 0.3192, "kalshi_brier": 0.2353, "brier_diff_model_minus_kalshi": 0.0839, "brier_diff_se": 0.016, "corr_model_outcome": 0.0162, "corr_kalshi_outcome": 0.2541}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
