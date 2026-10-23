# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-23T22:07Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 51,091): 0-3 13.9%, 3-5 9.4%, 5-10 19.7%, 10-15 15.3%, 15-25 19.3%, 25-40 14.1%, 40+ 8.3%; median gap 12.15 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.9%, Challenger 11.9%, doubles 6.6%). Main tour: ATP 4.7% and WTA 5.3% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 11,454): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.8%, STALE_QUOTE 18.7%, BOOK_QUALITY 17.9%, POOR_DATA 8.7%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.5%, IN_PLAY_QUOTE 3.6%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.8%, market_freshness 18.7%, execution 17.9%, data 12.2%, market_freshness/coverage 9.0%, mapping 4.5%, model_calibration_or_unknown 2.2%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.5% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 11,454 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.1% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.9%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.7% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 490.0 points vs 1670.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.034, Gen-2 0.84, Gen-1 ledger 0.861 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 556 model 0.2237 vs Kalshi 0.2087; n 112 model 0.2783 vs Kalshi 0.1982.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 220,767 model-market comparisons (359,609 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 73,131 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-23T21:53:42.981313+00:00'], shadow board 59,155 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-23T21:53:47.814172+00:00'], Model 4 27,563 rows, 19,611 settled tickers, 6,930 tickers with an external scan.
* By model: {"gen1_ledger": 49696, "gen1_elo": 29750, "fair_v1": 29750, "gen2": 29750, "gen1_sr": 29750, "model4_fundamental": 26049, "model4_conditioned": 26022}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 51,091 | 13.9 | 9.4 | 19.7 | 15.3 | 19.3 | 14.1 | 8.3 | 12.15 | 41.7% | 22.4% |
| MW fair_v1 | 29,750 | 12.8 | 8.5 | 18.4 | 15.5 | 19.7 | 15.0 | 10.1 | 13.24 | 44.8% | 25.1% |
| MW gen1_elo | 29,750 | 12.7 | 8.5 | 18.9 | 15.2 | 19.9 | 15.1 | 9.8 | 13.06 | 44.7% | 24.8% |
| MW gen1_ledger | 21,341 | 15.5 | 10.8 | 21.5 | 15.0 | 18.6 | 12.8 | 5.9 | 10.57 | 37.3% | 18.7% |
| MW gen1_sr | 29,750 | 10.2 | 7.0 | 16.5 | 13.6 | 20.8 | 18.9 | 13.1 | 16.12 | 52.8% | 31.9% |
| MW gen2 | 29,750 | 10.9 | 7.3 | 16.2 | 14.0 | 19.5 | 18.0 | 14.2 | 15.71 | 51.6% | 32.2% |
| all families model4_conditioned | 26,022 | 21.9 | 18.9 | 34.7 | 17.6 | 4.3 | 1.5 | 1.0 | 5.96 | 6.9% | 2.5% |
| all families model4_fundamental | 26,049 | 16.6 | 13.4 | 34.1 | 20.5 | 10.6 | 3.5 | 1.3 | 7.77 | 15.3% | 4.7% |

Configurable thresholds (primary): >=5pp 76.7%, >=10pp 57.0%, >=15pp 41.7%, >=20pp 31.1%, >=25pp 22.4%, >=30pp 16.2%, >=40pp 8.3%, >=50pp 3.9%
Executable gap (model outside the book, before fees): median 8.53pp; >=10pp 45.6%, >=25pp 17.6%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,542 | 28.4 | 14.2 | 24.9 | 15.1 | 11.8 | 4.8 | 0.7 | 6.07 | 17.3% | 5.5% |
| CHALLENGER | 4,622 | 15.8 | 10.0 | 20.4 | 15.5 | 14.8 | 12.4 | 11.2 | 11.09 | 38.3% | 23.6% |
| ITF_MEN | 8,248 | 10.2 | 7.3 | 16.8 | 14.7 | 21.5 | 17.4 | 12.2 | 15.39 | 51.0% | 29.6% |
| ITF_WOMEN | 11,870 | 9.3 | 6.8 | 16.0 | 15.3 | 22.3 | 18.2 | 12.0 | 15.82 | 52.5% | 30.2% |
| WTA | 1,808 | 17.1 | 13.3 | 25.8 | 19.5 | 18.2 | 5.4 | 0.7 | 8.25 | 24.3% | 6.1% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,542 | 24.2 | 15.1 | 24.8 | 17.3 | 13.0 | 4.7 | 0.9 | 6.5 | 18.6% | 5.7% |
| CHALLENGER | 4,622 | 15.0 | 8.8 | 18.5 | 14.5 | 17.3 | 13.8 | 12.1 | 12.49 | 43.2% | 25.9% |
| ITF_MEN | 8,248 | 8.2 | 5.9 | 14.4 | 12.9 | 19.7 | 21.0 | 17.9 | 18.69 | 58.5% | 38.8% |
| ITF_WOMEN | 11,870 | 8.1 | 5.6 | 13.7 | 13.3 | 20.6 | 21.0 | 17.7 | 19.09 | 59.2% | 38.6% |
| WTA | 1,808 | 13.9 | 10.2 | 22.1 | 16.3 | 23.1 | 13.3 | 1.2 | 11.0 | 37.6% | 14.5% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,542 | 24.2 | 12.8 | 23.6 | 16.2 | 14.9 | 7.0 | 1.1 | 7.34 | 23.1% | 8.1% |
| CHALLENGER | 4,622 | 14.3 | 9.1 | 20.4 | 15.6 | 16.2 | 13.0 | 11.3 | 11.49 | 40.5% | 24.3% |
| ITF_MEN | 8,248 | 9.7 | 7.4 | 16.9 | 13.9 | 22.0 | 17.7 | 12.3 | 15.73 | 52.1% | 30.1% |
| ITF_WOMEN | 11,870 | 9.4 | 6.6 | 16.2 | 15.8 | 22.7 | 18.1 | 11.1 | 15.65 | 52.0% | 29.3% |
| WTA | 1,808 | 24.0 | 16.9 | 30.5 | 15.4 | 10.1 | 2.6 | 0.5 | 6.04 | 13.2% | 3.1% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,495 | 25.6 | 19.3 | 30.8 | 12.2 | 8.9 | 3.0 | 0.3 | 5.58 | 12.2% | 3.3% |
| CHALLENGER | 3,162 | 21.4 | 14.6 | 26.4 | 14.4 | 14.6 | 6.7 | 1.9 | 7.29 | 23.2% | 8.6% |
| DOUBLES | 1,595 | 5.5 | 4.5 | 11.5 | 10.3 | 21.1 | 26.1 | 21.1 | 23.85 | 68.2% | 47.1% |
| ITF_MEN | 6,098 | 13.8 | 9.1 | 19.9 | 16.1 | 21.3 | 13.3 | 6.6 | 12.18 | 41.1% | 19.9% |
| ITF_WOMEN | 7,055 | 12.7 | 9.0 | 19.3 | 15.1 | 21.6 | 16.3 | 6.1 | 12.84 | 43.9% | 22.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,055 | 22.3 | 16.0 | 29.6 | 18.1 | 10.1 | 3.6 | 0.4 | 6.86 | 14.0% | 4.0% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,472 | 28.7 | 14.4 | 25.4 | 15.1 | 11.6 | 4.4 | 0.5 | 5.94 | 16.5% | 4.9% |
| CHALLENGER | 3,248 | 20.7 | 12.4 | 25.2 | 17.9 | 15.1 | 6.7 | 1.9 | 8.32 | 23.7% | 8.6% |
| ITF_MEN | 6,050 | 12.2 | 8.8 | 20.2 | 16.6 | 22.6 | 14.3 | 5.2 | 12.53 | 42.1% | 19.5% |
| ITF_WOMEN | 8,852 | 11.1 | 8.2 | 18.2 | 17.4 | 24.2 | 15.3 | 5.6 | 13.52 | 45.1% | 20.9% |
| WTA | 1,758 | 17.3 | 13.2 | 25.8 | 19.7 | 18.1 | 5.1 | 0.7 | 8.25 | 24.0% | 5.9% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,472 | 24.4 | 15.4 | 25.0 | 17.1 | 13.0 | 4.4 | 0.6 | 6.43 | 18.0% | 5.0% |
| CHALLENGER | 3,248 | 19.1 | 11.3 | 23.0 | 17.4 | 17.6 | 9.4 | 2.2 | 9.08 | 29.2% | 11.6% |
| ITF_MEN | 6,051 | 9.8 | 7.1 | 16.8 | 14.9 | 21.6 | 19.2 | 10.6 | 15.5 | 51.5% | 29.8% |
| ITF_WOMEN | 8,853 | 9.2 | 6.5 | 15.2 | 14.8 | 22.6 | 20.5 | 11.2 | 16.62 | 54.3% | 31.7% |
| WTA | 1,758 | 13.9 | 10.2 | 22.1 | 16.2 | 23.1 | 13.2 | 1.2 | 11.03 | 37.5% | 14.4% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,448 | 25.8 | 19.5 | 30.8 | 12.4 | 8.4 | 2.9 | 0.2 | 5.5 | 11.5% | 3.1% |
| CHALLENGER | 2,752 | 22.9 | 15.8 | 27.9 | 14.3 | 13.9 | 4.6 | 0.6 | 6.71 | 19.1% | 5.2% |
| DOUBLES | 1,478 | 5.4 | 4.6 | 11.8 | 10.5 | 21.0 | 26.1 | 20.7 | 23.62 | 67.7% | 46.8% |
| ITF_MEN | 5,104 | 14.9 | 9.7 | 21.6 | 16.9 | 21.2 | 11.6 | 4.0 | 11.17 | 36.8% | 15.6% |
| ITF_WOMEN | 5,832 | 13.6 | 9.6 | 20.7 | 16.0 | 21.8 | 15.0 | 3.4 | 11.66 | 40.1% | 18.3% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,005 | 22.8 | 16.5 | 29.6 | 18.1 | 10.1 | 2.9 | 0.1 | 6.79 | 13.0% | 3.0% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,595 | 5.5 | 4.5 | 11.5 | 10.3 | 21.1 | 26.1 | 21.1 | 23.85 | 68.2% | 47.1% |
| singles | 19,746 | 16.3 | 11.3 | 22.3 | 15.3 | 18.4 | 11.7 | 4.6 | 10.03 | 34.8% | 16.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 6,596 | 12.9 | 8.9 | 19.2 | 15.6 | 18.7 | 14.7 | 10.0 | 12.89 | 43.3% | 24.7% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 18,373 | 13.2 | 8.6 | 18.5 | 15.2 | 19.8 | 14.9 | 9.9 | 13.15 | 44.6% | 24.8% |
| UNKNOWN | 4,544 | 10.7 | 7.5 | 17.1 | 16.9 | 20.6 | 16.2 | 11.0 | 14.09 | 47.7% | 27.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,325 | 19.4 | 11.9 | 21.4 | 16.5 | 15.2 | 9.1 | 6.5 | 9.17 | 30.8% | 15.6% |
| B | 3,696 | 12.3 | 8.7 | 19.8 | 16.2 | 19.2 | 12.7 | 11.1 | 12.62 | 43.0% | 23.8% |
| C | 4,202 | 11.4 | 8.7 | 19.8 | 15.1 | 19.4 | 14.8 | 10.8 | 13.23 | 45.0% | 25.5% |
| D | 4,659 | 12.1 | 7.7 | 17.3 | 15.5 | 21.4 | 15.7 | 10.2 | 13.98 | 47.4% | 25.9% |
| F | 8,868 | 7.6 | 5.5 | 15.0 | 14.6 | 23.3 | 21.3 | 12.6 | 17.82 | 57.2% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,001 | 23.1 | 15.8 | 28.9 | 15.1 | 11.6 | 4.1 | 1.5 | 6.66 | 17.2% | 5.6% |
| B | 2,916 | 16.3 | 10.4 | 23.2 | 16.3 | 19.2 | 10.7 | 3.9 | 10.03 | 33.9% | 14.6% |
| C | 4,202 | 11.3 | 7.4 | 18.2 | 14.3 | 21.6 | 16.7 | 10.6 | 14.38 | 48.8% | 27.3% |
| D | 2,989 | 14.4 | 9.8 | 19.9 | 14.5 | 21.0 | 14.4 | 6.1 | 12.04 | 41.4% | 20.4% |
| F | 5,233 | 10.2 | 8.5 | 15.5 | 15.0 | 22.7 | 20.0 | 8.1 | 15.42 | 50.8% | 28.1% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 9,574 | 17.6 | 10.7 | 20.7 | 16.3 | 15.8 | 10.0 | 9.0 | 10.28 | 34.8% | 19.0% |
| LIMITED | 6,313 | 13.3 | 9.9 | 20.5 | 15.6 | 19.3 | 13.5 | 7.9 | 11.98 | 40.7% | 21.4% |
| POOR | 13,863 | 9.2 | 6.3 | 15.9 | 15.0 | 22.6 | 19.2 | 11.8 | 16.24 | 53.6% | 31.0% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,817 | 26.0 | 19.9 | 33.9 | 12.4 | 5.4 | 2.1 | 0.2 | 5.42 | 7.8% | 2.4% |
| GAME_SPREAD | 4,755 | 22.3 | 15.2 | 33.5 | 17.3 | 9.0 | 2.3 | 0.3 | 6.73 | 11.7% | 2.6% |
| MATCH_WINNER | 21,341 | 15.5 | 10.8 | 21.5 | 15.0 | 18.6 | 12.8 | 5.9 | 10.57 | 37.3% | 18.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 10,217 | 29.3 | 17.2 | 30.9 | 12.3 | 8.0 | 1.9 | 0.4 | 5.45 | 10.3% | 2.3% |
| TOTAL_GAMES | 7,542 | 8.8 | 9.7 | 36.5 | 28.7 | 10.4 | 3.2 | 2.6 | 9.43 | 16.2% | 5.8% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,121 | 25.4 | 33.4 | 32.6 | 4.5 | 3.1 | 0.7 | 0.2 | 4.49 | 4.1% | 0.9% |
| GAME_SPREAD | 6,241 | 45.6 | 16.7 | 26.9 | 7.9 | 1.7 | 0.9 | 0.3 | 3.47 | 2.9% | 1.2% |
| TOTAL_GAMES | 10,660 | 5.0 | 7.8 | 41.2 | 34.5 | 6.9 | 2.5 | 2.1 | 9.57 | 11.5% | 4.6% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,124 | 24.2 | 17.7 | 35.5 | 12.6 | 7.0 | 2.6 | 0.3 | 5.83 | 10.0% | 2.9% |
| GAME_SPREAD | 6,244 | 19.5 | 13.4 | 27.8 | 20.8 | 13.3 | 4.3 | 0.9 | 7.96 | 18.6% | 5.3% |
| TOTAL_GAMES | 10,681 | 8.6 | 9.6 | 36.6 | 27.2 | 12.1 | 3.6 | 2.3 | 9.43 | 18.0% | 5.9% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 29,750 | 44.8% | 25.1% | 13.24 | 36.3% | 15.7% | 10.98 |
| gen1_elo | 29,750 | 44.7% | 24.8% | 13.06 | 36.1% | 15.8% | 10.79 |
| gen1_sr | 29,750 | 52.8% | 31.9% | 16.12 | 44.9% | 22.5% | 13.24 |
| gen2 | 29,750 | 51.6% | 32.2% | 15.71 | 44.8% | 24.1% | 13.14 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 15,073 | 15.6 | 10.4 | 21.2 | 17.2 | 20.2 | 12.0 | 3.4 | 10.78 | 35.5% | 15.4% |
| STALE | 14,677 | 9.8 | 6.6 | 15.6 | 13.8 | 19.2 | 18.1 | 16.9 | 17.07 | 54.3% | 35.1% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 14,809 | 16.5 | 11.3 | 22.2 | 15.1 | 17.8 | 12.2 | 4.8 | 9.99 | 34.9% | 17.1% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 51,091 | 14809 | 18545 | 17737 | 24.2 | 150.6 | 1400.4 |
| ge_15pp | 21,293 | 5168 | 6647 | 9478 | 26.3 | 443.3 | 1380.4 |
| ge_25pp | 11,454 | 2526 | 2909 | 6019 | 32.8 | 584.3 | 1380.4 |
| lt_10pp | 21,983 | 7409 | 8754 | 5820 | 22.4 | 48.3 | 1341.5 |

Current slate `SL-20261023T220743Z-f6e51b84`: 418 priced rows, quote age at build {'median': 14.3, 'max': 14.4}, freshness {'AGING': 418}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 23 | 0.0 | 0.0 | 21.7 | 4.3 | 39.1 | 34.8 | 0.0 | 20.49 | 73.9% | 34.8% |
| EXTERNAL_LONE_OUTLIER | 14 | 71.4 | 28.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.4 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,796 | 19.1 | 11.2 | 24.7 | 18.7 | 18.4 | 7.3 | 0.7 | 8.93 | 26.3% | 8.0% |
| KALSHI_LONE_OUTLIER | 17 | 5.9 | 5.9 | 76.5 | 0.0 | 5.9 | 5.9 | 0.0 | 6.11 | 11.8% | 5.9% |
| MARKETS_AGREE | 556 | 63.9 | 36.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.35 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,180 | 0.0 | 2.2 | 35.8 | 25.9 | 24.7 | 10.8 | 0.8 | 12.25 | 36.2% | 11.5% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 29,750 | 4586 (15.4%) | 25.7% | 0.9% | {"EXTERNAL_STALE": 2796, "AGREES_WITH_KALSHI": 1180, "ALL_AGREE": 556, "SUPPORTS_MODEL_DIRECTION": 22, "AGREES_WITH_MODEL": 17, "EXTERNAL_OUTLIER": 14, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 13,326 | 1182 (8.9%) | 36.1% | 1.6% | {"EXTERNAL_STALE": 736, "AGREES_WITH_KALSHI": 427, "SUPPORTS_MODEL_DIRECTION": 17, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 7,466 | 368 (4.9%) | 37.0% | 2.5% | {"EXTERNAL_STALE": 223, "AGREES_WITH_KALSHI": 136, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,624 | 345 (9.5%) | 37.4% | 2.6% | {"EXTERNAL_STALE": 207, "AGREES_WITH_KALSHI": 129, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 11,805 | 2575 (21.8%) | 17.4% | 0.7% | {"EXTERNAL_STALE": 1537, "ALL_AGREE": 556, "AGREES_WITH_KALSHI": 448, "AGREES_WITH_MODEL": 15, "EXTERNAL_OUTLIER": 14, "SUPPORTS_MODEL_DIRECTION": 4, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,681 | 10.1 | 7.5 | 19.5 | 14.3 | 22.4 | 16.0 | 10.3 | 14.29 | 48.6% | 26.3% |
| 4-10x | 3,898 | 10.9 | 8.2 | 19.2 | 15.3 | 21.2 | 15.0 | 10.2 | 13.77 | 46.4% | 25.2% |
| <2x | 15,022 | 14.8 | 9.7 | 19.0 | 16.4 | 17.6 | 13.1 | 9.3 | 11.92 | 40.0% | 22.5% |
| >=10x | 5,149 | 10.9 | 6.3 | 15.2 | 14.3 | 21.8 | 19.5 | 11.9 | 16.34 | 53.2% | 31.4% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 7,559 | 12.2 | 8.5 | 19.6 | 16.0 | 19.1 | 13.7 | 10.9 | 12.99 | 43.7% | 24.6% |
| 300-1000 | 6,391 | 11.6 | 8.5 | 17.3 | 15.3 | 20.6 | 16.4 | 10.4 | 14.0 | 47.3% | 26.7% |
| <300 | 9,798 | 8.6 | 5.7 | 15.5 | 14.8 | 22.9 | 20.1 | 12.4 | 16.99 | 55.5% | 32.5% |
| >=3000 | 6,002 | 21.3 | 13.1 | 23.1 | 16.4 | 14.2 | 7.0 | 4.9 | 7.96 | 26.1% | 11.9% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 848 | 0.5489 | 0.4104 | 0.5 | +0.049 | -0.090 | -0.0031 ± 0.0053 |
| ratio 4-10x | 581 | 0.588 | 0.4419 | 0.4957 | +0.092 | -0.054 | 0.0126 ± 0.0067 |
| ratio <2x | 2089 | 0.5377 | 0.4143 | 0.4457 | +0.092 | -0.031 | 0.0127 ± 0.0031 |
| ratio >=10x | 778 | 0.5707 | 0.3955 | 0.4653 | +0.105 | -0.070 | 0.0061 ± 0.0065 |
| thinner_sample 1000-3000 | 1157 | 0.5422 | 0.4152 | 0.4451 | +0.097 | -0.030 | 0.0113 ± 0.0042 |
| thinner_sample 300-1000 | 987 | 0.5666 | 0.4232 | 0.4924 | +0.074 | -0.069 | 0.0012 ± 0.0051 |
| thinner_sample <300 | 1453 | 0.5603 | 0.3938 | 0.4659 | +0.094 | -0.072 | 0.0086 ± 0.0046 |
| thinner_sample >=3000 | 699 | 0.5346 | 0.4401 | 0.4678 | +0.067 | -0.028 | 0.0132 ± 0.0044 |
| data_status ADEQUATE | 1224 | 0.5378 | 0.4327 | 0.451 | +0.087 | -0.018 | 0.0128 ± 0.0036 |
| data_status LIMITED | 994 | 0.5503 | 0.4169 | 0.4799 | +0.070 | -0.063 | 0.0046 ± 0.0047 |
| data_status POOR | 2078 | 0.5626 | 0.4013 | 0.4697 | +0.093 | -0.068 | 0.0076 ± 0.0038 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 625 | 0.2008 | 0.2019 | -0.0011 ± 0.0006 | 0.5822 | 0.5845 | 0.5032 | 0.4884 | 0.5328 | -0.060 ± 0.0188 | -0.01 (5) |
| 3-5 | 399 | 0.2027 | 0.2024 | +0.0003 ± 0.0018 | 0.5886 | 0.5862 | 0.5021 | 0.462 | 0.4762 | -0.095 ± 0.0232 | 0.02 (1) |
| 5-10 | 889 | 0.2022 | 0.2017 | +0.0006 ± 0.0023 | 0.5911 | 0.5864 | 0.5109 | 0.4368 | 0.4657 | -0.091 ± 0.0156 | -0.0167 (6) |
| 10-15 | 738 | 0.2136 | 0.2035 | +0.0102 ± 0.0042 | 0.6178 | 0.5884 | 0.5296 | 0.4055 | 0.4255 | -0.105 ± 0.0165 | -0.048 (5) |
| 15-25 | 977 | 0.225 | 0.2135 | +0.0116 ± 0.0058 | 0.645 | 0.6107 | 0.5779 | 0.3821 | 0.4504 | -0.093 ± 0.0147 | -0.0033 (9) |
| 25-40 | 556 | 0.2237 | 0.2087 | +0.0150 ± 0.0115 | 0.6353 | 0.6004 | 0.6566 | 0.3471 | 0.4748 | -0.074 ± 0.0178 | -0.01 (1) |
| 40+ | 112 | 0.2783 | 0.1982 | +0.0800 ± 0.0365 | 0.7629 | 0.5814 | 0.7564 | 0.3087 | 0.4464 | -0.077 ± 0.0358 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3229 | 0.1841 | 0.1851 | -0.0010 ± 0.0003 | 0.5435 | 0.5447 | 0.4928 | 0.4777 | 0.5147 | -0.018 ± 0.0076 | -0.0129 (17) |
| 3-5 | 2136 | 0.1987 | 0.1978 | +0.0010 ± 0.0008 | 0.5783 | 0.5734 | 0.4839 | 0.4439 | 0.4508 | -0.049 ± 0.0098 | 0.0 (2) |
| 5-10 | 4628 | 0.1977 | 0.1945 | +0.0031 ± 0.001 | 0.5794 | 0.5684 | 0.4803 | 0.4064 | 0.4218 | -0.046 ± 0.0066 | -0.0119 (21) |
| 10-15 | 3949 | 0.197 | 0.1786 | +0.0184 ± 0.0017 | 0.5794 | 0.5277 | 0.4859 | 0.3615 | 0.3495 | -0.075 ± 0.0067 | -0.0281 (16) |
| 15-25 | 4978 | 0.2086 | 0.1695 | +0.0391 ± 0.0023 | 0.6106 | 0.5016 | 0.5057 | 0.3092 | 0.3088 | -0.074 ± 0.0058 | -0.0025 (44) |
| 25-40 | 3898 | 0.223 | 0.1297 | +0.0933 ± 0.0036 | 0.64 | 0.3965 | 0.5313 | 0.2182 | 0.2293 | -0.059 ± 0.0056 | -0.01 (1) |
| 40+ | 2554 | 0.3803 | 0.0456 | +0.3347 ± 0.0048 | 0.9907 | 0.1752 | 0.633 | 0.1072 | 0.0646 | -0.078 ± 0.004 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 492 | 0.2058 | 0.2065 | -0.0007 ± 0.0007 | 0.5934 | 0.5948 | 0.5068 | 0.4917 | 0.5142 | -0.104 ± 0.022 | -0.01 (3) |
| 3-5 | 355 | 0.2241 | 0.2217 | +0.0024 ± 0.002 | 0.6345 | 0.6296 | 0.5139 | 0.474 | 0.4592 | -0.123 ± 0.0267 | 0.02 (1) |
| 5-10 | 768 | 0.2053 | 0.2053 | +0.0000 ± 0.0025 | 0.5969 | 0.5957 | 0.5469 | 0.4721 | 0.5117 | -0.078 ± 0.0169 | -0.01 (4) |
| 10-15 | 711 | 0.2169 | 0.2086 | +0.0083 ± 0.0043 | 0.6233 | 0.6027 | 0.5662 | 0.442 | 0.4726 | -0.112 ± 0.0178 | -0.04 (5) |
| 15-25 | 998 | 0.2299 | 0.2102 | +0.0197 ± 0.0057 | 0.6528 | 0.6031 | 0.5879 | 0.392 | 0.4439 | -0.100 ± 0.0148 | -0.0133 (9) |
| 25-40 | 705 | 0.2622 | 0.198 | +0.0642 ± 0.0106 | 0.7317 | 0.5766 | 0.6532 | 0.3376 | 0.3957 | -0.112 ± 0.0164 | -0.0075 (4) |
| 40+ | 267 | 0.3591 | 0.1721 | +0.1870 ± 0.0251 | 0.9875 | 0.5146 | 0.7316 | 0.2471 | 0.3109 | -0.071 ± 0.0244 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2756 | 0.1938 | 0.1941 | -0.0003 ± 0.0003 | 0.5642 | 0.5648 | 0.5106 | 0.4956 | 0.5127 | -0.041 ± 0.0087 | -0.0133 (15) |
| 3-5 | 1831 | 0.199 | 0.1983 | +0.0006 ± 0.0008 | 0.576 | 0.5741 | 0.5147 | 0.4748 | 0.4866 | -0.042 ± 0.0106 | 0.02 (1) |
| 5-10 | 4082 | 0.1953 | 0.1936 | +0.0016 ± 0.001 | 0.5755 | 0.5666 | 0.5085 | 0.4344 | 0.4633 | -0.031 ± 0.007 | -0.0117 (6) |
| 10-15 | 3584 | 0.2008 | 0.1885 | +0.0123 ± 0.0018 | 0.5884 | 0.5498 | 0.5131 | 0.3892 | 0.4026 | -0.056 ± 0.0074 | -0.0189 (18) |
| 15-25 | 4930 | 0.216 | 0.178 | +0.0379 ± 0.0024 | 0.6276 | 0.5239 | 0.5251 | 0.3292 | 0.3341 | -0.069 ± 0.006 | -0.0086 (42) |
| 25-40 | 4563 | 0.2519 | 0.1374 | +0.1145 ± 0.0035 | 0.7086 | 0.4217 | 0.558 | 0.2411 | 0.2216 | -0.085 ± 0.0054 | -0.0044 (18) |
| 40+ | 3626 | 0.3939 | 0.0604 | +0.3335 ± 0.0047 | 1.037 | 0.2161 | 0.6506 | 0.1185 | 0.0841 | -0.072 ± 0.004 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 598 | 0.1999 | 0.202 | -0.0021 ± 0.0007 | 0.5806 | 0.5858 | 0.5008 | 0.4855 | 0.5502 | -0.026 ± 0.0189 | -0.0137 (8) |
| 3-5 | 427 | 0.2016 | 0.1996 | +0.0020 ± 0.0018 | 0.5861 | 0.5796 | 0.5069 | 0.4671 | 0.4637 | -0.120 ± 0.0224 | 0.0067 (3) |
| 5-10 | 904 | 0.2009 | 0.1976 | +0.0033 ± 0.0022 | 0.5881 | 0.5763 | 0.5074 | 0.4334 | 0.4458 | -0.101 ± 0.0152 | -0.0071 (7) |
| 10-15 | 752 | 0.2085 | 0.2052 | +0.0034 ± 0.0041 | 0.606 | 0.5926 | 0.5392 | 0.4156 | 0.4654 | -0.083 ± 0.0164 | -0.0317 (6) |
| 15-25 | 920 | 0.2316 | 0.2123 | +0.0194 ± 0.0059 | 0.6614 | 0.6077 | 0.5883 | 0.3939 | 0.4402 | -0.113 ± 0.0152 | -0.03 (1) |
| 25-40 | 577 | 0.2136 | 0.2174 | -0.0037 ± 0.0114 | 0.6153 | 0.6205 | 0.6682 | 0.3571 | 0.5165 | -0.052 ± 0.0175 | 0.015 (2) |
| 40+ | 118 | 0.2919 | 0.209 | +0.0829 ± 0.0368 | 0.8038 | 0.6052 | 0.7657 | 0.3158 | 0.4576 | -0.070 ± 0.0381 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3158 | 0.1851 | 0.1856 | -0.0005 ± 0.0003 | 0.5447 | 0.5455 | 0.4912 | 0.4761 | 0.4899 | -0.038 ± 0.0077 | -0.0163 (35) |
| 3-5 | 2137 | 0.1952 | 0.1929 | +0.0023 ± 0.0008 | 0.5731 | 0.5659 | 0.4879 | 0.4482 | 0.4403 | -0.067 ± 0.0097 | -0.0094 (18) |
| 5-10 | 4682 | 0.1957 | 0.19 | +0.0056 ± 0.001 | 0.5753 | 0.5566 | 0.4822 | 0.4082 | 0.4073 | -0.060 ± 0.0064 | -0.01 (31) |
| 10-15 | 3862 | 0.1909 | 0.175 | +0.0159 ± 0.0017 | 0.5651 | 0.518 | 0.4983 | 0.3749 | 0.3718 | -0.067 ± 0.0067 | -0.015 (12) |
| 15-25 | 5140 | 0.2107 | 0.1715 | +0.0393 ± 0.0023 | 0.6155 | 0.5063 | 0.5139 | 0.319 | 0.3158 | -0.074 ± 0.0058 | -0.03 (2) |
| 25-40 | 3919 | 0.2191 | 0.1335 | +0.0856 ± 0.0037 | 0.6324 | 0.4046 | 0.5375 | 0.2211 | 0.246 | -0.048 ± 0.0056 | 0.01 (3) |
| 40+ | 2474 | 0.395 | 0.0502 | +0.3448 ± 0.0051 | 1.032 | 0.1873 | 0.6453 | 0.1136 | 0.0691 | -0.081 ± 0.0043 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 983 | 0.1951 | 0.1953 | -0.0002 ± 0.0005 | 0.5697 | 0.5696 | 0.504 | 0.4889 | 0.4954 | -0.057 ± 0.0143 | -0.0224 (49) |
| 3-5 | 687 | 0.1917 | 0.191 | +0.0007 ± 0.0013 | 0.5606 | 0.5577 | 0.4891 | 0.4492 | 0.4585 | -0.057 ± 0.0171 | -0.0194 (34) |
| 5-10 | 1429 | 0.2014 | 0.1952 | +0.0061 ± 0.0018 | 0.5922 | 0.5729 | 0.4968 | 0.4234 | 0.4192 | -0.073 ± 0.0119 | -0.005 (78) |
| 10-15 | 948 | 0.2099 | 0.1981 | +0.0118 ± 0.0036 | 0.6093 | 0.5783 | 0.521 | 0.3978 | 0.4093 | -0.069 ± 0.0147 | 0.0014 (64) |
| 15-25 | 1275 | 0.2313 | 0.2099 | +0.0214 ± 0.005 | 0.6604 | 0.6045 | 0.5764 | 0.3816 | 0.4251 | -0.072 ± 0.0129 | -0.0214 (59) |
| 25-40 | 777 | 0.2476 | 0.2071 | +0.0405 ± 0.01 | 0.7034 | 0.5954 | 0.672 | 0.3596 | 0.4505 | -0.085 ± 0.0153 | -0.0219 (26) |
| 40+ | 258 | 0.354 | 0.1967 | +0.1573 ± 0.0273 | 1.0218 | 0.5751 | 0.808 | 0.3255 | 0.4225 | -0.096 ± 0.0249 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3207 | 0.1827 | 0.1829 | -0.0002 ± 0.0003 | 0.5384 | 0.538 | 0.5047 | 0.4893 | 0.5008 | -0.037 ± 0.0076 | -0.0157 (88) |
| 3-5 | 2232 | 0.1938 | 0.192 | +0.0018 ± 0.0007 | 0.5659 | 0.5619 | 0.4946 | 0.4549 | 0.4521 | -0.053 ± 0.0094 | -0.0209 (69) |
| 5-10 | 4438 | 0.1973 | 0.1887 | +0.0086 ± 0.001 | 0.5805 | 0.5554 | 0.4916 | 0.4181 | 0.3995 | -0.072 ± 0.0066 | -0.0082 (132) |
| 10-15 | 3099 | 0.2052 | 0.1893 | +0.0159 ± 0.0019 | 0.5987 | 0.557 | 0.5276 | 0.4045 | 0.4008 | -0.065 ± 0.0078 | -0.0053 (105) |
| 15-25 | 3879 | 0.2297 | 0.1995 | +0.0302 ± 0.0028 | 0.6623 | 0.5783 | 0.5689 | 0.3735 | 0.3947 | -0.065 ± 0.0072 | -0.0253 (107) |
| 25-40 | 2687 | 0.259 | 0.1842 | +0.0748 ± 0.0052 | 0.7341 | 0.5372 | 0.6318 | 0.3178 | 0.358 | -0.077 ± 0.0081 | -0.0229 (51) |
| 40+ | 1190 | 0.3771 | 0.1448 | +0.2323 ± 0.0116 | 1.0693 | 0.4359 | 0.7293 | 0.226 | 0.2597 | -0.070 ± 0.0104 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4296 | 1.034 ± 0.043 | 1.131 | 0.169 | 0.1648 | 0.214 | 0.2056 |
| gen2 | 4296 | 0.84 ± 0.04 | 1.093 | 0.1689 | 0.1654 | 0.2335 | 0.2052 |
| gen1_elo | 4296 | 1.011 ± 0.041 | 1.12 | 0.1759 | 0.1649 | 0.2129 | 0.2058 |
| gen1_sr | 4296 | 1.028 ± 0.052 | 1.168 | 0.1298 | 0.1674 | 0.2295 | 0.2048 |
| gen1_ledger | 6357 | 0.861 ± 0.03 | 1.073 | 0.1838 | 0.1793 | 0.2185 | 0.1997 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 21,293)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,943 | 23.2% |
| STALE_QUOTE | market_freshness | 4,628 | 21.7% |
| BOOK_QUALITY | execution | 3,950 | 18.6% |
| POOR_DATA | data | 2,411 | 11.3% |
| LIMITED_DATA | data | 1,308 | 6.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,166 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,002 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 895 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 643 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 346 | 1.6% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 23.2%, market_freshness 21.7%, execution 18.6%, data 17.5%, market_freshness/coverage 8.5%, model_calibration_or_unknown 4.7%, mapping 4.2%, model_calibration 1.6%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 94.3%, LOW_DATA_QUALITY 71.0%, THIN_PLAYER_HISTORY 60.0%, STALE_PLAYER_DATA 49.5%, STALE_KALSHI_QUOTE 44.5%, MODEL_INTERNAL_DISAGREEMENT 42.6%, ASYMMETRIC_SAMPLE_SIZE 33.6%, WIDE_SPREAD 24.6%, MODEL_HIGH_UNCERTAINTY 17.9%, PLAYER_IDENTITY_RISK 16.3%, LEVEL_TRANSFER_RISK 11.1%, LOW_DISPLAYED_LIQUIDITY 8.1%, EVENT_MAPPING_RISK 7.9%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.1%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.8%, POST_SETTLEMENT_OBSERVATION 23.2%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 11,454)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,984 | 34.8% |
| STALE_QUOTE | market_freshness | 2,146 | 18.7% |
| BOOK_QUALITY | execution | 2,053 | 17.9% |
| POOR_DATA | data | 1,001 | 8.7% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 623 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 510 | 4.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 410 | 3.6% |
| LIMITED_DATA | data | 398 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 250 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 78 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.8%, market_freshness 18.7%, execution 17.9%, data 12.2%, market_freshness/coverage 9.0%, mapping 4.5%, model_calibration_or_unknown 2.2%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 74.3%, THIN_PLAYER_HISTORY 62.2%, STALE_KALSHI_QUOTE 52.5%, STALE_PLAYER_DATA 44.1%, MODEL_INTERNAL_DISAGREEMENT 42.8%, ASYMMETRIC_SAMPLE_SIZE 34.8%, WIDE_SPREAD 23.7%, PLAYER_IDENTITY_RISK 19.6%, MODEL_HIGH_UNCERTAINTY 18.3%, LEVEL_TRANSFER_RISK 9.8%, EVENT_MAPPING_RISK 9.4%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.9%, POST_SETTLEMENT_OBSERVATION 34.8%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 8923, "IDENTITY_AMBIGUOUS": 2531}; ticker orientation: {"VERIFIED": 11454}.

Checks: discipline:AMBIGUOUS 752, discipline:PASS 10702, identity_confidence:AMBIGUOUS 2250, identity_confidence:PASS 9204, level_mapping:NA 764, level_mapping:PASS 10690, market_pair:AMBIGUOUS 396, market_pair:NA 290, market_pair:PASS 10768, model_complement:NA 257, model_complement:PASS 11197, namesake:PASS 11454, physical_match_id:NA 3988, physical_match_id:PASS 7466, player_ids:PASS 11454, same_pair_other_event:PASS 11454, ticker_orientation:PASS 11454

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,037 | 4.7% | 4.2% | 1.7% | {"market_freshness": 53, "model_calibration_or_unknown": 43, "data": 35, "execution": 22, "market_freshness/coverage": 13, "model_calibration": 13, "coverage": 11} | 5.86 | 0.2183 / 0.2125 (473) | 18.6% | 3.8% | 3.1% | 2.9% |
| CHALLENGER | 7,784 | 17.5% | 7.0% | 11.9% | {"coverage": 772, "market_freshness/coverage": 167, "market_freshness": 148, "data": 138, "model_calibration_or_unknown": 62, "execution": 31, "model_calibration": 28, "mapping": 15, "possible_market_error": 1} | 7.41 | 0.2198 / 0.2083 (1874) | 35.0% | 17.8% | 3.8% | 22.9% |
| DOUBLES | 1,595 | 47.1% | 46.8% | 6.6% | {"execution": 386, "mapping": 199, "market_freshness": 106, "market_freshness/coverage": 54, "coverage": 7} | 23.62 | 0.3098 / 0.2355 (422) | 14.7% | 0.0% | 100.0% | 7.3% |
| ITF_MEN | 14,346 | 25.4% | 17.7% | 31.9% | {"coverage": 1360, "execution": 693, "market_freshness": 624, "data": 481, "market_freshness/coverage": 316, "mapping": 172, "model_calibration_or_unknown": 2, "model_calibration": 2} | 11.9 | 0.2155 / 0.1976 (3223) | 37.6% | 69.9% | 19.9% | 22.2% |
| ITF_WOMEN | 18,925 | 27.3% | 19.9% | 45.1% | {"coverage": 1812, "market_freshness": 1126, "execution": 882, "data": 711, "market_freshness/coverage": 434, "mapping": 118, "model_calibration_or_unknown": 68, "model_calibration": 11} | 12.84 | 0.2031 / 0.1941 (3680) | 40.0% | 56.0% | 9.9% | 22.4% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,863 | 5.3% | 4.8% | 1.3% | {"market_freshness": 49, "model_calibration_or_unknown": 34, "execution": 25, "model_calibration": 13, "data": 11, "market_freshness/coverage": 10, "coverage": 9, "mapping": 1} | 7.7 | 0.2385 / 0.2306 (451) | 24.7% | 1.4% | 1.5% | 3.5% |
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
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 207 min (STALE); no external reference |
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
| 23 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 24 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 25 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 26 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 27 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 28 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 29 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 30 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 31 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 32 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 33 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 34 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 35 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 36 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 37 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 38 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 39 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 92 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 40 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 41 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 42 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 43 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 44 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 45 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 468 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 46 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 47 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 48 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 765 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 49 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 50 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9702, "by_level_share_of_ge_25pp": {"ATP": 0.0166, "CHALLENGER": 0.1189, "DOUBLES": 0.0657, "ITF_MEN": 0.3187, "ITF_WOMEN": 0.4507, "OTHER": 0.001, "WTA": 0.0133, "WTA125": 0.0152}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5255, "share_primary_cause_market_settled_or_in_play": 0.438, "share_primary_cause_stale_quote_only": 0.1874}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 11454, "identity_ambiguous_share": 0.221, "ticker_orientation": {"VERIFIED": 11454}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 7466, "with_external": 368, "coverage": 0.0493, "external_status": {"EXTERNAL_STALE": 223, "AGREES_WITH_KALSHI": 136, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 223, "MODEL_LONE_OUTLIER": 136, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3696, "share_external_supports_model": 0.0245}, "pregame_clean_ge_25pp": {"n": 3624, "with_external": 345, "coverage": 0.0952, "external_status": {"EXTERNAL_STALE": 207, "AGREES_WITH_KALSHI": 129, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 207, "MODEL_LONE_OUTLIER": 129, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3739, "share_external_supports_model": 0.0261}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 490.0, "median_sample_ratio": 2.43, "median_min_matches": 21.0, "median_max_days_since_last": 225.0, "share_severe_asymmetry": 0.2147, "data_status": {"POOR": 6394, "LIMITED": 2994, "ADEQUATE": 2066}, "comparison_lt_10pp": {"median_thinner_serve_points": 1670.0, "median_sample_ratio": 1.71, "median_min_matches": 94.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 848, "model_minus_observed": 0.0489, "kalshi_minus_observed": -0.0896, "brier_diff_model_minus_kalshi": -0.0031}, "4-10x": {"n": 581, "model_minus_observed": 0.0923, "kalshi_minus_observed": -0.0538, "brier_diff_model_minus_kalshi": 0.0126}, "<2x": {"n": 2089, "model_minus_observed": 0.0921, "kalshi_minus_observed": -0.0314, "brier_diff_model_minus_kalshi": 0.0127}, ">=10x": {"n": 778, "model_minus_observed": 0.1054, "kalshi_minus_observed": -0.0698, "brier_diff_model_minus_kalshi": 0.0061}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4296, "model": {"intercept": -0.541, "slope": 0.84, "slope_se": 0.04}, "kalshi_mid_same_rows": {"intercept": 0.214, "slope": 1.093, "slope_se": 0.044}, "mean_extremity_model": 0.1689, "mean_extremity_kalshi": 0.1654, "model_brier": 0.2335, "kalshi_brier": 0.2052, "brier_diff_model_minus_kalshi": 0.0282, "brier_diff_se": 0.0029, "model_logloss": 0.6634, "kalshi_logloss": 0.5931}, "fair_v1": {"n": 4296, "model": {"intercept": -0.412, "slope": 1.034, "slope_se": 0.043}, "kalshi_mid_same_rows": {"intercept": 0.302, "slope": 1.131, "slope_se": 0.045}, "mean_extremity_model": 0.169, "mean_extremity_kalshi": 0.1648, "model_brier": 0.214, "kalshi_brier": 0.2056, "brier_diff_model_minus_kalshi": 0.0084, "brier_diff_se": 0.0024, "model_logloss": 0.6166, "kalshi_logloss": 0.5937}, "gen1_elo": {"n": 4296, "model": {"intercept": -0.398, "slope": 1.011, "slope_se": 0.041}, "kalshi_mid_same_rows": {"intercept": 0.311, "slope": 1.12, "slope_se": 0.044}, "mean_extremity_model": 0.1759, "mean_extremity_kalshi": 0.1649, "model_brier": 0.2129, "kalshi_brier": 0.2058, "brier_diff_model_minus_kalshi": 0.0071, "brier_diff_se": 0.0024, "model_logloss": 0.6153, "kalshi_logloss": 0.5943}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.251, "share_ge_15": 0.4479, "median_abs_gap": 13.24, "n": 29750}, "gen1_elo": {"share_ge_25": 0.2481, "share_ge_15": 0.4471, "median_abs_gap": 13.06, "n": 29750}, "gen1_sr": {"share_ge_25": 0.3192, "share_ge_15": 0.5277, "median_abs_gap": 16.12, "n": 29750}, "gen2": {"share_ge_25": 0.322, "share_ge_15": 0.5165, "median_abs_gap": 15.71, "n": 29750}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1574, "share_ge_15": 0.3634, "median_abs_gap": 10.98, "n": 23014}, "gen1_elo": {"share_ge_25": 0.1584, "share_ge_15": 0.3611, "median_abs_gap": 10.79, "n": 23011}, "gen1_sr": {"share_ge_25": 0.2248, "share_ge_15": 0.4494, "median_abs_gap": 13.24, "n": 23015}, "gen2": {"share_ge_25": 0.2406, "share_ge_15": 0.448, "median_abs_gap": 13.14, "n": 23016}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.86, "share_ge_25_all": 0.0471, "share_ge_25_pregame_clean": 0.0423}, "WTA": {"median_abs_gap_pregame_clean": 7.7, "share_ge_25_all": 0.0531, "share_ge_25_pregame_clean": 0.0481}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2333, "share_within_10pp_all": 0.4303, "share_within_10pp_pregame_clean": 0.4839, "corr_model_vs_mid_pregame_clean": 0.8434}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 625, "model_brier": 0.2008, "kalshi_brier": 0.2019, "brier_diff_model_minus_kalshi": -0.0011}, "10-15": {"n_settled": 738, "model_brier": 0.2136, "kalshi_brier": 0.2035, "brier_diff_model_minus_kalshi": 0.0102}, "15-25": {"n_settled": 977, "model_brier": 0.225, "kalshi_brier": 0.2135, "brier_diff_model_minus_kalshi": 0.0116}, "25-40": {"n_settled": 556, "model_brier": 0.2237, "kalshi_brier": 0.2087, "brier_diff_model_minus_kalshi": 0.015}, "3-5": {"n_settled": 399, "model_brier": 0.2027, "kalshi_brier": 0.2024, "brier_diff_model_minus_kalshi": 0.0003}, "40+": {"n_settled": 112, "model_brier": 0.2783, "kalshi_brier": 0.1982, "brier_diff_model_minus_kalshi": 0.08}, "5-10": {"n_settled": 889, "model_brier": 0.2022, "kalshi_brier": 0.2017, "brier_diff_model_minus_kalshi": 0.0006}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.541, "slope": 0.84, "slope_se": 0.04}, "kalshi_slope": {"intercept": 0.214, "slope": 1.093, "slope_se": 0.044}, "n": 4296}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.509, "slope": 0.861, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.155, "slope": 1.073, "slope_se": 0.035}, "n": 6357}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 422, "model_brier": 0.3098, "kalshi_brier": 0.2355, "brier_diff_model_minus_kalshi": 0.0743, "brier_diff_se": 0.0148, "corr_model_outcome": 0.046, "corr_kalshi_outcome": 0.2571}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
