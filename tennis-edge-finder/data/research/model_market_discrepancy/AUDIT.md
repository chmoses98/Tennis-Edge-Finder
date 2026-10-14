# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-14T03:24Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 31,635): 0-3 14.5%, 3-5 9.5%, 5-10 20.2%, 10-15 15.4%, 15-25 18.7%, 25-40 13.5%, 40+ 8.2%; median gap 11.73 pp.
* **Where the extremes live**: 98.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.1%, Challenger 12.6%, doubles 7.0%). Main tour: ATP 1.4% and WTA 6.3% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 6,856): MARKET_ALREADY_SETTLED_WHEN_PRICED 38.0%, BOOK_QUALITY 17.9%, STALE_QUOTE 16.2%, POOR_DATA 8.2%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IDENTITY_AMBIGUOUS 4.2%, LIMITED_DATA 4.2%, IN_PLAY_QUOTE 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.4%. By class: coverage 38.0%, execution 17.9%, market_freshness 16.2%, data 12.4%, market_freshness/coverage 8.8%, mapping 4.2%, model_calibration_or_unknown 2.0%, model_calibration 0.4%.
* **Stale / settled / in-play**: 53.2% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 46.9% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 6,856 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 18.9% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 3.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 21.1% of the time and with the model 0.6%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 586.5 points vs 1869.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.075, Gen-2 0.877, Gen-1 ledger 0.884 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 311 model 0.2235 vs Kalshi 0.2079; n 68 model 0.2909 vs Kalshi 0.1768.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 125,915 model-market comparisons (207,899 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 45,877 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-14T03:15:10.313791+00:00'], shadow board 33,936 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-14T03:15:13.734398+00:00'], Model 4 13,906 rows, 13,815 settled tickers, 4,272 tickers with an external scan.
* By model: {"gen1_ledger": 30190, "gen1_elo": 17056, "fair_v1": 17056, "gen2": 17056, "gen1_sr": 17056, "model4_fundamental": 13755, "model4_conditioned": 13746}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 31,635 | 14.5 | 9.5 | 20.2 | 15.4 | 18.7 | 13.5 | 8.2 | 11.73 | 40.3% | 21.7% |
| MW fair_v1 | 17,056 | 13.7 | 8.6 | 18.7 | 16.0 | 18.8 | 14.4 | 9.8 | 12.79 | 43.0% | 24.2% |
| MW gen1_elo | 17,056 | 13.3 | 9.1 | 20.1 | 15.1 | 18.7 | 14.4 | 9.3 | 12.26 | 42.4% | 23.6% |
| MW gen1_ledger | 14,579 | 15.4 | 10.7 | 22.0 | 14.7 | 18.5 | 12.4 | 6.3 | 10.46 | 37.2% | 18.7% |
| MW gen1_sr | 17,056 | 10.0 | 7.8 | 16.5 | 14.3 | 21.7 | 18.1 | 11.7 | 15.51 | 51.4% | 29.8% |
| MW gen2 | 17,056 | 11.8 | 7.3 | 16.4 | 14.2 | 20.2 | 17.1 | 13.1 | 15.19 | 50.3% | 30.1% |
| all families model4_conditioned | 13,746 | 21.7 | 20.1 | 35.5 | 16.4 | 4.3 | 1.1 | 0.9 | 5.81 | 6.3% | 2.0% |
| all families model4_fundamental | 13,755 | 16.7 | 13.4 | 35.8 | 19.8 | 10.6 | 2.6 | 1.1 | 7.61 | 14.4% | 3.7% |

Configurable thresholds (primary): >=5pp 75.9%, >=10pp 55.7%, >=15pp 40.3%, >=20pp 29.9%, >=25pp 21.7%, >=30pp 15.8%, >=40pp 8.2%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.35pp; >=10pp 45.0%, >=25pp 17.3%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,311 | 30.1 | 14.7 | 24.9 | 17.8 | 10.4 | 1.1 | 0.8 | 5.84 | 12.4% | 2.0% |
| CHALLENGER | 3,016 | 15.5 | 10.1 | 20.2 | 15.8 | 14.7 | 12.0 | 11.8 | 11.52 | 38.5% | 23.8% |
| ITF_MEN | 4,745 | 11.3 | 8.4 | 18.1 | 14.9 | 19.4 | 15.5 | 12.3 | 13.98 | 47.2% | 27.8% |
| ITF_WOMEN | 6,542 | 10.3 | 6.5 | 16.1 | 16.1 | 21.9 | 18.7 | 10.6 | 15.46 | 51.1% | 29.2% |
| WTA | 891 | 21.9 | 10.9 | 24.9 | 15.7 | 19.6 | 5.7 | 1.2 | 8.0 | 26.6% | 7.0% |
| WTA125 | 551 | 13.2 | 7.8 | 22.9 | 20.5 | 19.6 | 14.0 | 2.0 | 11.2 | 35.6% | 16.0% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,311 | 23.9 | 14.6 | 24.8 | 19.1 | 14.7 | 1.9 | 1.0 | 6.81 | 17.5% | 2.9% |
| CHALLENGER | 3,016 | 15.1 | 7.6 | 19.3 | 13.3 | 18.2 | 14.0 | 12.5 | 12.75 | 44.6% | 26.4% |
| ITF_MEN | 4,745 | 9.9 | 7.2 | 16.3 | 14.2 | 20.0 | 18.2 | 14.2 | 15.87 | 52.4% | 32.4% |
| ITF_WOMEN | 6,542 | 8.7 | 5.8 | 13.0 | 13.0 | 21.8 | 20.8 | 16.8 | 18.97 | 59.4% | 37.6% |
| WTA | 891 | 18.4 | 8.2 | 19.0 | 15.9 | 22.6 | 14.7 | 1.2 | 11.64 | 38.5% | 15.9% |
| WTA125 | 551 | 6.0 | 4.2 | 18.3 | 18.0 | 24.9 | 19.1 | 9.6 | 16.84 | 53.5% | 28.7% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,311 | 27.5 | 14.4 | 29.0 | 15.3 | 10.4 | 2.5 | 0.9 | 6.1 | 13.8% | 3.4% |
| CHALLENGER | 3,016 | 14.9 | 10.2 | 20.6 | 15.2 | 15.3 | 11.9 | 11.8 | 11.01 | 39.0% | 23.7% |
| ITF_MEN | 4,745 | 10.3 | 8.4 | 18.9 | 14.0 | 20.0 | 16.0 | 12.4 | 14.2 | 48.4% | 28.4% |
| ITF_WOMEN | 6,542 | 9.8 | 6.8 | 16.5 | 15.7 | 22.6 | 19.1 | 9.4 | 15.48 | 51.1% | 28.5% |
| WTA | 891 | 22.3 | 15.4 | 33.2 | 15.7 | 10.3 | 2.2 | 0.8 | 6.12 | 13.4% | 3.0% |
| WTA125 | 551 | 22.9 | 11.6 | 29.0 | 15.2 | 14.3 | 6.5 | 0.4 | 7.55 | 21.2% | 6.9% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 713 | 30.9 | 22.9 | 35.6 | 9.0 | 1.3 | 0.4 | 0.0 | 4.7 | 1.7% | 0.4% |
| CHALLENGER | 2,059 | 22.0 | 15.5 | 27.5 | 15.1 | 12.9 | 5.0 | 2.0 | 6.94 | 19.9% | 7.0% |
| DOUBLES | 955 | 4.4 | 3.5 | 11.6 | 11.1 | 18.9 | 24.6 | 25.9 | 25.42 | 69.4% | 50.5% |
| ITF_MEN | 4,435 | 14.8 | 8.4 | 21.0 | 15.4 | 20.7 | 12.4 | 7.3 | 11.81 | 40.5% | 19.8% |
| ITF_WOMEN | 4,960 | 11.7 | 9.3 | 19.5 | 14.7 | 22.5 | 16.6 | 5.8 | 13.07 | 44.9% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 648 | 21.4 | 15.1 | 27.3 | 17.1 | 13.6 | 4.9 | 0.5 | 7.61 | 19.0% | 5.4% |
| WTA125 | 660 | 20.3 | 13.8 | 22.4 | 18.5 | 14.4 | 8.3 | 2.3 | 8.29 | 25.0% | 10.6% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,297 | 30.1 | 14.7 | 25.1 | 17.8 | 10.4 | 1.1 | 0.8 | 5.84 | 12.3% | 1.9% |
| CHALLENGER | 2,165 | 20.1 | 12.5 | 25.4 | 18.5 | 15.1 | 6.0 | 2.5 | 8.33 | 23.6% | 8.5% |
| ITF_MEN | 3,409 | 14.1 | 10.5 | 21.6 | 16.7 | 19.5 | 12.3 | 5.3 | 11.08 | 37.2% | 17.7% |
| ITF_WOMEN | 4,742 | 12.6 | 8.1 | 18.5 | 18.6 | 23.4 | 15.1 | 3.7 | 12.79 | 42.2% | 18.8% |
| WTA | 878 | 22.0 | 10.4 | 25.3 | 15.8 | 19.7 | 5.6 | 1.2 | 8.06 | 26.5% | 6.8% |
| WTA125 | 528 | 13.6 | 7.6 | 22.4 | 20.8 | 20.3 | 13.8 | 1.5 | 11.31 | 35.6% | 15.3% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,297 | 23.8 | 14.7 | 24.9 | 19.1 | 14.7 | 1.9 | 1.0 | 6.9 | 17.5% | 2.9% |
| CHALLENGER | 2,165 | 19.4 | 9.6 | 24.2 | 16.1 | 18.5 | 9.7 | 2.6 | 9.08 | 30.8% | 12.3% |
| ITF_MEN | 3,410 | 11.8 | 8.7 | 18.8 | 15.9 | 21.8 | 15.8 | 7.4 | 13.21 | 44.9% | 23.1% |
| ITF_WOMEN | 4,742 | 10.1 | 6.9 | 14.7 | 14.2 | 24.4 | 19.6 | 10.2 | 16.51 | 54.1% | 29.8% |
| WTA | 878 | 18.2 | 8.0 | 19.1 | 16.2 | 22.6 | 14.7 | 1.2 | 11.68 | 38.5% | 16.0% |
| WTA125 | 528 | 5.9 | 4.4 | 18.4 | 18.4 | 24.6 | 19.7 | 8.7 | 16.74 | 53.0% | 28.4% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 693 | 30.9 | 23.1 | 35.9 | 9.1 | 0.6 | 0.4 | 0.0 | 4.69 | 1.0% | 0.4% |
| CHALLENGER | 1,778 | 23.9 | 16.9 | 29.6 | 14.9 | 12.0 | 2.2 | 0.6 | 6.34 | 14.7% | 2.8% |
| DOUBLES | 885 | 4.4 | 3.5 | 12.0 | 11.1 | 19.1 | 24.3 | 25.6 | 24.89 | 69.0% | 49.9% |
| ITF_MEN | 3,627 | 16.4 | 9.2 | 23.0 | 16.2 | 20.6 | 10.3 | 4.2 | 10.4 | 35.2% | 14.6% |
| ITF_WOMEN | 4,054 | 12.8 | 10.0 | 21.3 | 15.5 | 22.8 | 14.9 | 2.6 | 11.65 | 40.4% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 614 | 22.0 | 15.8 | 27.5 | 17.1 | 13.8 | 3.8 | 0.0 | 7.21 | 17.6% | 3.8% |
| WTA125 | 557 | 22.3 | 15.3 | 23.9 | 20.3 | 12.8 | 5.2 | 0.4 | 7.37 | 18.3% | 5.6% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 955 | 4.4 | 3.5 | 11.6 | 11.1 | 18.9 | 24.6 | 25.9 | 25.42 | 69.4% | 50.5% |
| singles | 13,624 | 16.2 | 11.2 | 22.7 | 14.9 | 18.4 | 11.6 | 5.0 | 9.96 | 34.9% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 3,969 | 13.3 | 9.1 | 20.1 | 15.9 | 17.5 | 14.1 | 9.9 | 12.42 | 41.5% | 24.1% |
| Grass | 143 | 11.9 | 14.0 | 16.8 | 13.3 | 21.7 | 16.8 | 5.6 | 13.07 | 44.1% | 22.4% |
| Hard | 11,227 | 14.2 | 8.5 | 18.7 | 15.7 | 19.2 | 14.2 | 9.6 | 12.71 | 43.0% | 23.8% |
| UNKNOWN | 1,717 | 11.7 | 7.6 | 16.1 | 17.9 | 19.5 | 16.4 | 10.7 | 13.85 | 46.6% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,189 | 19.9 | 10.7 | 21.1 | 16.9 | 15.5 | 8.7 | 7.2 | 9.48 | 31.4% | 15.8% |
| B | 2,269 | 14.5 | 9.2 | 20.1 | 16.9 | 17.6 | 12.1 | 9.7 | 11.42 | 39.4% | 21.8% |
| C | 2,469 | 13.1 | 9.5 | 19.6 | 14.8 | 19.1 | 14.5 | 9.3 | 12.65 | 42.9% | 23.8% |
| D | 2,993 | 10.8 | 8.2 | 18.0 | 16.1 | 22.2 | 15.0 | 9.7 | 13.9 | 46.9% | 24.7% |
| F | 4,136 | 8.0 | 5.2 | 15.1 | 14.8 | 21.1 | 22.4 | 13.4 | 18.11 | 56.9% | 35.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,264 | 22.6 | 15.9 | 28.8 | 15.2 | 11.4 | 4.4 | 1.6 | 6.72 | 17.5% | 6.1% |
| B | 2,230 | 15.0 | 10.0 | 24.0 | 16.4 | 19.1 | 11.2 | 4.3 | 10.18 | 34.6% | 15.4% |
| C | 2,878 | 12.1 | 7.6 | 18.2 | 14.4 | 20.4 | 15.7 | 11.6 | 13.75 | 47.7% | 27.3% |
| D | 2,222 | 14.0 | 9.8 | 20.8 | 13.5 | 21.6 | 13.8 | 6.4 | 11.85 | 41.8% | 20.2% |
| F | 2,985 | 9.8 | 7.4 | 15.2 | 13.8 | 23.9 | 20.6 | 9.3 | 16.55 | 53.8% | 29.9% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 5,760 | 18.3 | 9.8 | 20.3 | 16.8 | 15.8 | 9.7 | 9.4 | 10.45 | 34.8% | 19.1% |
| LIMITED | 4,099 | 15.2 | 10.3 | 20.8 | 15.8 | 18.4 | 12.7 | 6.7 | 11.07 | 37.9% | 19.4% |
| POOR | 7,197 | 9.2 | 6.6 | 16.3 | 15.4 | 21.5 | 19.2 | 11.8 | 15.98 | 52.5% | 31.0% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,970 | 31.4 | 24.2 | 36.4 | 5.5 | 1.8 | 0.7 | 0.1 | 4.5 | 2.5% | 0.7% |
| GAME_SPREAD | 2,850 | 25.8 | 15.9 | 36.8 | 16.7 | 4.2 | 0.4 | 0.2 | 6.0 | 4.8% | 0.6% |
| MATCH_WINNER | 14,579 | 15.4 | 10.7 | 22.0 | 14.7 | 18.5 | 12.4 | 6.3 | 10.46 | 37.2% | 18.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 5,433 | 33.4 | 19.4 | 31.0 | 9.7 | 5.2 | 1.2 | 0.2 | 4.73 | 6.5% | 1.4% |
| TOTAL_GAMES | 4,334 | 6.7 | 9.1 | 39.1 | 29.6 | 10.4 | 2.7 | 2.4 | 9.46 | 15.5% | 5.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,841 | 25.6 | 38.0 | 31.6 | 0.3 | 3.9 | 0.4 | 0.1 | 4.32 | 4.5% | 0.6% |
| GAME_SPREAD | 3,455 | 45.1 | 16.5 | 28.9 | 7.3 | 1.1 | 0.7 | 0.4 | 3.58 | 2.2% | 1.1% |
| TOTAL_GAMES | 5,450 | 3.4 | 6.5 | 43.1 | 36.5 | 6.6 | 1.9 | 1.9 | 9.75 | 10.5% | 3.9% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,841 | 26.2 | 18.5 | 37.3 | 9.2 | 6.3 | 2.1 | 0.3 | 5.52 | 8.7% | 2.4% |
| GAME_SPREAD | 3,455 | 19.1 | 13.3 | 30.4 | 21.2 | 13.0 | 2.3 | 0.7 | 7.83 | 16.1% | 3.0% |
| TOTAL_GAMES | 5,459 | 6.6 | 8.8 | 38.0 | 28.3 | 12.9 | 3.2 | 2.1 | 9.67 | 18.3% | 5.3% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 17,056 | 43.0% | 24.2% | 12.79 | 33.5% | 14.2% | 10.36 |
| gen1_elo | 17,056 | 42.4% | 23.6% | 12.26 | 32.5% | 14.0% | 9.8 |
| gen1_sr | 17,056 | 51.4% | 29.8% | 15.51 | 42.9% | 19.8% | 12.74 |
| gen2 | 17,056 | 50.3% | 30.1% | 15.19 | 43.1% | 21.5% | 12.7 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 9,266 | 16.6 | 10.6 | 21.7 | 17.4 | 19.2 | 11.2 | 3.3 | 10.31 | 33.7% | 14.5% |
| STALE | 7,790 | 10.3 | 6.2 | 15.2 | 14.2 | 18.4 | 18.2 | 17.4 | 17.17 | 54.1% | 35.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 8,047 | 17.3 | 11.6 | 23.8 | 14.7 | 16.8 | 11.0 | 4.8 | 9.33 | 32.6% | 15.8% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 31,635 | 8047 | 12738 | 10850 | 24.2 | 145.6 | 1400.4 |
| ge_15pp | 12,761 | 2625 | 4410 | 5726 | 26.6 | 450.0 | 1380.4 |
| ge_25pp | 6,856 | 1270 | 1935 | 3651 | 34.4 | 577.2 | 1380.4 |
| lt_10pp | 14,009 | 4243 | 6160 | 3606 | 22.6 | 48.5 | 1341.5 |

Current slate `SL-20261014T032410Z-88b0441c`: 701 priced rows, quote age at build {'median': 9.3, 'max': 9.4}, freshness {'FRESH': 701}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 8 | 0.0 | 0.0 | 37.5 | 0.0 | 37.5 | 25.0 | 0.0 | 20.45 | 62.5% | 25.0% |
| EXTERNAL_LONE_OUTLIER | 9 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.3 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,322 | 21.8 | 10.7 | 23.0 | 19.0 | 18.2 | 6.7 | 0.6 | 8.72 | 25.6% | 7.3% |
| KALSHI_LONE_OUTLIER | 5 | 20.0 | 0.0 | 60.0 | 0.0 | 20.0 | 0.0 | 0.0 | 5.14 | 20.0% | 0.0% |
| MARKETS_AGREE | 230 | 71.3 | 28.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.03 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 421 | 0.0 | 4.0 | 35.1 | 30.2 | 21.9 | 8.1 | 0.7 | 11.41 | 30.6% | 8.8% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 17,056 | 1995 (11.7%) | 21.1% | 0.6% | {"EXTERNAL_STALE": 1322, "AGREES_WITH_KALSHI": 421, "ALL_AGREE": 230, "EXTERNAL_OUTLIER": 9, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 5, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 7,337 | 473 (6.5%) | 27.3% | 1.3% | {"EXTERNAL_STALE": 338, "AGREES_WITH_KALSHI": 129, "SUPPORTS_MODEL_DIRECTION": 5, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp | 4,124 | 136 (3.3%) | 27.2% | 1.5% | {"EXTERNAL_STALE": 97, "AGREES_WITH_KALSHI": 37, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_ge_25pp_pregame_clean | 1,843 | 128 (7.0%) | 27.3% | 1.6% | {"EXTERNAL_STALE": 91, "AGREES_WITH_KALSHI": 35, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_lt_10pp | 6,997 | 1144 (16.4%) | 14.4% | 0.5% | {"EXTERNAL_STALE": 733, "ALL_AGREE": 230, "AGREES_WITH_KALSHI": 165, "EXTERNAL_OUTLIER": 9, "AGREES_WITH_MODEL": 4, "SUPPORTS_MODEL_DIRECTION": 2, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,365 | 11.7 | 8.1 | 19.9 | 14.9 | 21.3 | 14.2 | 9.9 | 13.28 | 45.5% | 24.2% |
| 4-10x | 2,265 | 11.9 | 8.7 | 19.4 | 15.4 | 19.7 | 15.7 | 9.1 | 13.09 | 44.6% | 24.9% |
| <2x | 9,062 | 15.7 | 9.2 | 18.9 | 17.0 | 17.4 | 12.7 | 9.2 | 11.75 | 39.2% | 21.8% |
| >=10x | 2,364 | 10.7 | 6.7 | 15.9 | 14.0 | 20.1 | 20.2 | 12.4 | 16.21 | 52.8% | 32.6% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 4,463 | 14.1 | 8.2 | 19.5 | 16.0 | 19.0 | 12.7 | 10.5 | 12.5 | 42.2% | 23.2% |
| 300-1000 | 3,946 | 11.9 | 8.6 | 17.5 | 16.1 | 21.2 | 15.7 | 8.9 | 13.66 | 45.8% | 24.7% |
| <300 | 4,706 | 8.7 | 6.1 | 15.9 | 14.7 | 20.9 | 20.9 | 12.9 | 16.98 | 54.6% | 33.7% |
| >=3000 | 3,941 | 21.1 | 11.8 | 22.6 | 17.3 | 13.8 | 7.5 | 5.9 | 8.5 | 27.2% | 13.4% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 561 | 0.5359 | 0.4048 | 0.4795 | +0.056 | -0.075 | 0.0021 ± 0.0062 |
| ratio 4-10x | 374 | 0.5862 | 0.4457 | 0.5241 | +0.062 | -0.078 | 0.0037 ± 0.0082 |
| ratio <2x | 1326 | 0.5381 | 0.4163 | 0.4555 | +0.083 | -0.039 | 0.0105 ± 0.0039 |
| ratio >=10x | 407 | 0.5472 | 0.3797 | 0.4324 | +0.115 | -0.053 | 0.0124 ± 0.0088 |
| thinner_sample 1000-3000 | 753 | 0.5442 | 0.4189 | 0.4728 | +0.071 | -0.054 | 0.0042 ± 0.0053 |
| thinner_sample 300-1000 | 670 | 0.5608 | 0.4229 | 0.4821 | +0.079 | -0.059 | 0.0045 ± 0.0059 |
| thinner_sample <300 | 781 | 0.5453 | 0.385 | 0.4558 | +0.089 | -0.071 | 0.0103 ± 0.0062 |
| thinner_sample >=3000 | 464 | 0.5276 | 0.4329 | 0.4526 | +0.075 | -0.020 | 0.0158 ± 0.0053 |
| data_status ADEQUATE | 762 | 0.5318 | 0.4278 | 0.4528 | +0.079 | -0.025 | 0.0095 ± 0.0045 |
| data_status LIMITED | 711 | 0.5521 | 0.4231 | 0.488 | +0.064 | -0.065 | 0.003 ± 0.0055 |
| data_status POOR | 1195 | 0.5509 | 0.3962 | 0.4628 | +0.088 | -0.067 | 0.0102 ± 0.0049 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 410 | 0.1925 | 0.1939 | -0.0014 ± 0.0008 | 0.5624 | 0.5654 | 0.492 | 0.477 | 0.5195 | -0.053 ± 0.0228 | -0.01 (3) |
| 3-5 | 271 | 0.1898 | 0.1905 | -0.0006 ± 0.0021 | 0.5596 | 0.5597 | 0.5069 | 0.4671 | 0.4908 | -0.070 ± 0.027 | 0.02 (1) |
| 5-10 | 556 | 0.1979 | 0.1991 | -0.0012 ± 0.0029 | 0.5803 | 0.5823 | 0.5118 | 0.4377 | 0.4748 | -0.082 ± 0.0197 | -0.0125 (4) |
| 10-15 | 478 | 0.2096 | 0.2025 | +0.0071 ± 0.0051 | 0.6058 | 0.5856 | 0.5222 | 0.3986 | 0.4289 | -0.087 ± 0.0204 | -0.0633 (3) |
| 15-25 | 574 | 0.2267 | 0.2146 | +0.0121 ± 0.0075 | 0.6478 | 0.6157 | 0.5742 | 0.3795 | 0.4477 | -0.076 ± 0.0193 | -0.0133 (6) |
| 25-40 | 311 | 0.2235 | 0.2079 | +0.0156 ± 0.0155 | 0.6384 | 0.5962 | 0.6503 | 0.3404 | 0.4695 | -0.066 ± 0.0233 | -0.01 (1) |
| 40+ | 68 | 0.2909 | 0.1768 | +0.1141 ± 0.0454 | 0.7906 | 0.5286 | 0.7508 | 0.3033 | 0.3971 | -0.121 ± 0.0447 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1942 | 0.1768 | 0.1779 | -0.0011 ± 0.0003 | 0.5274 | 0.5284 | 0.4783 | 0.4633 | 0.4974 | -0.023 ± 0.0097 | -0.0188 (8) |
| 3-5 | 1225 | 0.1949 | 0.1933 | +0.0016 ± 0.001 | 0.5711 | 0.5629 | 0.4798 | 0.4402 | 0.4359 | -0.064 ± 0.0128 | 0.02 (1) |
| 5-10 | 2659 | 0.1929 | 0.1912 | +0.0017 ± 0.0013 | 0.5674 | 0.5614 | 0.4856 | 0.4118 | 0.4336 | -0.045 ± 0.0086 | -0.0082 (17) |
| 10-15 | 2303 | 0.2006 | 0.1828 | +0.0177 ± 0.0022 | 0.5867 | 0.5373 | 0.4796 | 0.3552 | 0.3461 | -0.075 ± 0.0089 | -0.0475 (4) |
| 15-25 | 2732 | 0.2055 | 0.1699 | +0.0355 ± 0.0031 | 0.6027 | 0.5026 | 0.4985 | 0.3026 | 0.3122 | -0.065 ± 0.0079 | -0.0048 (29) |
| 25-40 | 2182 | 0.2195 | 0.1243 | +0.0952 ± 0.0047 | 0.6322 | 0.384 | 0.529 | 0.2151 | 0.2236 | -0.063 ± 0.0073 | -0.01 (1) |
| 40+ | 1494 | 0.3718 | 0.0438 | +0.3280 ± 0.006 | 0.9693 | 0.173 | 0.6241 | 0.1061 | 0.0589 | -0.084 ± 0.005 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 314 | 0.1959 | 0.1962 | -0.0003 ± 0.0009 | 0.5732 | 0.5739 | 0.5 | 0.4849 | 0.5 | -0.089 ± 0.0264 | -0.01 (1) |
| 3-5 | 214 | 0.212 | 0.2109 | +0.0011 ± 0.0026 | 0.6062 | 0.6053 | 0.5187 | 0.4787 | 0.4813 | -0.084 ± 0.0331 | 0.02 (1) |
| 5-10 | 487 | 0.1969 | 0.1968 | +0.0002 ± 0.003 | 0.5755 | 0.5757 | 0.5557 | 0.4805 | 0.5154 | -0.070 ± 0.0209 | -0.01 (4) |
| 10-15 | 438 | 0.2172 | 0.2059 | +0.0112 ± 0.0055 | 0.621 | 0.5972 | 0.5756 | 0.4512 | 0.4726 | -0.104 ± 0.0226 | -0.05 (4) |
| 15-25 | 643 | 0.2243 | 0.2076 | +0.0166 ± 0.0071 | 0.6386 | 0.5978 | 0.5913 | 0.3939 | 0.4541 | -0.083 ± 0.0183 | -0.01 (5) |
| 25-40 | 417 | 0.27 | 0.197 | +0.0730 ± 0.0137 | 0.7558 | 0.5731 | 0.6668 | 0.3529 | 0.3957 | -0.131 ± 0.0215 | -0.025 (2) |
| 40+ | 155 | 0.3451 | 0.19 | +0.1551 ± 0.0338 | 0.9621 | 0.5558 | 0.7492 | 0.272 | 0.3613 | -0.056 ± 0.0333 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1675 | 0.182 | 0.1824 | -0.0004 ± 0.0004 | 0.5393 | 0.54 | 0.4954 | 0.4808 | 0.5045 | -0.033 ± 0.0108 | -0.0217 (6) |
| 3-5 | 1072 | 0.1954 | 0.1947 | +0.0008 ± 0.0011 | 0.5662 | 0.5645 | 0.5166 | 0.4767 | 0.486 | -0.042 ± 0.0137 | 0.02 (1) |
| 5-10 | 2324 | 0.1893 | 0.1871 | +0.0023 ± 0.0013 | 0.5602 | 0.5517 | 0.5146 | 0.4408 | 0.4639 | -0.040 ± 0.0091 | -0.01 (5) |
| 10-15 | 2027 | 0.1971 | 0.1817 | +0.0155 ± 0.0024 | 0.5798 | 0.5329 | 0.5239 | 0.3995 | 0.4026 | -0.067 ± 0.0096 | -0.02 (14) |
| 15-25 | 2928 | 0.2148 | 0.1753 | +0.0395 ± 0.0031 | 0.625 | 0.5182 | 0.5344 | 0.3381 | 0.3388 | -0.076 ± 0.0078 | -0.0026 (27) |
| 25-40 | 2526 | 0.2485 | 0.1368 | +0.1117 ± 0.0047 | 0.7059 | 0.4174 | 0.5617 | 0.2459 | 0.2288 | -0.088 ± 0.0074 | -0.015 (6) |
| 40+ | 1985 | 0.3997 | 0.0681 | +0.3316 ± 0.0067 | 1.047 | 0.2371 | 0.666 | 0.129 | 0.1023 | -0.068 ± 0.0057 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 404 | 0.1923 | 0.1951 | -0.0028 ± 0.0008 | 0.5632 | 0.5705 | 0.4921 | 0.477 | 0.5569 | +0.001 ± 0.0222 | -0.0133 (6) |
| 3-5 | 290 | 0.1866 | 0.1849 | +0.0018 ± 0.002 | 0.5489 | 0.5446 | 0.4929 | 0.4535 | 0.4517 | -0.117 ± 0.0265 | -0.01 (1) |
| 5-10 | 600 | 0.1997 | 0.1976 | +0.0021 ± 0.0027 | 0.5857 | 0.5779 | 0.5057 | 0.432 | 0.4517 | -0.088 ± 0.0187 | -0.01 (4) |
| 10-15 | 453 | 0.209 | 0.2108 | -0.0018 ± 0.0053 | 0.6055 | 0.6045 | 0.5397 | 0.4171 | 0.4879 | -0.060 ± 0.0213 | -0.044 (5) |
| 15-25 | 538 | 0.2303 | 0.2085 | +0.0217 ± 0.0077 | 0.6595 | 0.6011 | 0.5787 | 0.3854 | 0.4275 | -0.102 ± 0.0196 | -0.03 (1) |
| 25-40 | 322 | 0.2093 | 0.2147 | -0.0054 ± 0.0152 | 0.6067 | 0.6128 | 0.6568 | 0.3443 | 0.5062 | -0.039 ± 0.0226 | 0.0 (1) |
| 40+ | 61 | 0.3195 | 0.1777 | +0.1418 ± 0.0492 | 0.8584 | 0.5313 | 0.7574 | 0.3028 | 0.377 | -0.134 ± 0.0497 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1845 | 0.1852 | 0.1865 | -0.0013 ± 0.0004 | 0.5463 | 0.5489 | 0.4841 | 0.4689 | 0.5062 | -0.017 ± 0.0101 | -0.0183 (23) |
| 3-5 | 1288 | 0.1865 | 0.1844 | +0.0021 ± 0.001 | 0.5497 | 0.5447 | 0.4763 | 0.437 | 0.4301 | -0.072 ± 0.0124 | -0.0243 (7) |
| 5-10 | 2855 | 0.1925 | 0.1872 | +0.0052 ± 0.0012 | 0.5683 | 0.5511 | 0.4817 | 0.408 | 0.4081 | -0.062 ± 0.0082 | -0.01 (18) |
| 10-15 | 2160 | 0.1944 | 0.1806 | +0.0138 ± 0.0023 | 0.5729 | 0.53 | 0.4943 | 0.3711 | 0.3764 | -0.064 ± 0.0091 | -0.03 (9) |
| 15-25 | 2805 | 0.2079 | 0.1701 | +0.0379 ± 0.003 | 0.6104 | 0.504 | 0.502 | 0.3067 | 0.3098 | -0.069 ± 0.0078 | -0.03 (2) |
| 25-40 | 2161 | 0.2138 | 0.122 | +0.0918 ± 0.0047 | 0.6194 | 0.3768 | 0.5242 | 0.2076 | 0.2244 | -0.058 ± 0.0071 | 0.0 (1) |
| 40+ | 1423 | 0.386 | 0.0456 | +0.3404 ± 0.0064 | 1.009 | 0.1783 | 0.6323 | 0.1081 | 0.0569 | -0.087 ± 0.0053 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 717 | 0.1993 | 0.2001 | -0.0008 ± 0.0006 | 0.5795 | 0.5813 | 0.5053 | 0.4903 | 0.5105 | -0.034 ± 0.0167 | -0.0226 (46) |
| 3-5 | 522 | 0.1964 | 0.1958 | +0.0006 ± 0.0016 | 0.5721 | 0.569 | 0.48 | 0.4402 | 0.4502 | -0.047 ± 0.0195 | -0.0058 (33) |
| 5-10 | 1079 | 0.1916 | 0.1859 | +0.0056 ± 0.002 | 0.5669 | 0.5524 | 0.4813 | 0.4079 | 0.4069 | -0.064 ± 0.0134 | -0.0049 (73) |
| 10-15 | 691 | 0.2046 | 0.1952 | +0.0093 ± 0.0042 | 0.5973 | 0.5719 | 0.4973 | 0.3743 | 0.3965 | -0.046 ± 0.0168 | 0.0014 (64) |
| 15-25 | 919 | 0.2325 | 0.2121 | +0.0203 ± 0.0059 | 0.6632 | 0.6106 | 0.5585 | 0.3643 | 0.4102 | -0.051 ± 0.0152 | -0.0216 (58) |
| 25-40 | 525 | 0.2534 | 0.1923 | +0.0611 ± 0.0119 | 0.7143 | 0.5602 | 0.6446 | 0.3313 | 0.3886 | -0.087 ± 0.0178 | -0.0216 (25) |
| 40+ | 178 | 0.3628 | 0.1934 | +0.1693 ± 0.0336 | 1.0535 | 0.568 | 0.7956 | 0.3023 | 0.3989 | -0.070 ± 0.0301 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2177 | 0.1902 | 0.1905 | -0.0003 ± 0.0003 | 0.5559 | 0.5556 | 0.5042 | 0.4889 | 0.503 | -0.031 ± 0.0093 | -0.0155 (82) |
| 3-5 | 1509 | 0.1891 | 0.1866 | +0.0025 ± 0.0009 | 0.5531 | 0.5469 | 0.4867 | 0.4471 | 0.4361 | -0.058 ± 0.0112 | -0.0148 (63) |
| 5-10 | 3076 | 0.1905 | 0.1826 | +0.0078 ± 0.0012 | 0.5645 | 0.5426 | 0.4765 | 0.4029 | 0.3898 | -0.066 ± 0.0078 | -0.0087 (125) |
| 10-15 | 2071 | 0.1997 | 0.187 | +0.0127 ± 0.0024 | 0.5859 | 0.5518 | 0.5056 | 0.3825 | 0.3921 | -0.049 ± 0.0095 | -0.0053 (105) |
| 15-25 | 2601 | 0.2297 | 0.1987 | +0.0310 ± 0.0034 | 0.6632 | 0.5772 | 0.5527 | 0.3578 | 0.3772 | -0.059 ± 0.0088 | -0.0255 (106) |
| 25-40 | 1762 | 0.2536 | 0.1674 | +0.0862 ± 0.0062 | 0.7201 | 0.495 | 0.6053 | 0.2904 | 0.3133 | -0.077 ± 0.0095 | -0.0206 (47) |
| 40+ | 861 | 0.3855 | 0.1269 | +0.2587 ± 0.0131 | 1.0958 | 0.3898 | 0.7094 | 0.2002 | 0.2137 | -0.072 ± 0.0115 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2668 | 1.075 ± 0.055 | 1.189 | 0.1691 | 0.1699 | 0.2099 | 0.2018 |
| gen2 | 2668 | 0.877 ± 0.049 | 1.129 | 0.1807 | 0.1698 | 0.228 | 0.2016 |
| gen1_elo | 2668 | 1.054 ± 0.053 | 1.183 | 0.1733 | 0.1703 | 0.2088 | 0.2019 |
| gen1_sr | 2668 | 1.078 ± 0.063 | 1.206 | 0.1395 | 0.1717 | 0.224 | 0.2014 |
| gen1_ledger | 4631 | 0.884 ± 0.037 | 1.094 | 0.1757 | 0.1865 | 0.217 | 0.1968 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 12,761)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,307 | 25.9% |
| STALE_QUOTE | market_freshness | 2,472 | 19.4% |
| BOOK_QUALITY | execution | 2,355 | 18.4% |
| POOR_DATA | data | 1,388 | 10.9% |
| LIMITED_DATA | data | 968 | 7.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 698 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 627 | 4.9% |
| IDENTITY_AMBIGUOUS | mapping | 464 | 3.6% |
| IN_PLAY_QUOTE | market_freshness/coverage | 365 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 117 | 0.9% |

Cause class: coverage 25.9%, market_freshness 19.4%, data 18.5%, execution 18.4%, market_freshness/coverage 8.3%, model_calibration_or_unknown 4.9%, mapping 3.6%, model_calibration 0.9%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.4%, START_UNVERIFIABLE 95.8%, LOW_DATA_QUALITY 68.3%, THIN_PLAYER_HISTORY 57.0%, STALE_PLAYER_DATA 55.4%, STALE_KALSHI_QUOTE 44.9%, MODEL_INTERNAL_DISAGREEMENT 38.5%, ASYMMETRIC_SAMPLE_SIZE 31.0%, WIDE_SPREAD 24.1%, MODEL_HIGH_UNCERTAINTY 16.5%, PLAYER_IDENTITY_RISK 12.8%, LEVEL_TRANSFER_RISK 8.8%, EVENT_MAPPING_RISK 7.8%, LOW_DISPLAYED_LIQUIDITY 7.4%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 1.5%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 28.3%, POST_SETTLEMENT_OBSERVATION 25.9%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### >= ge_25 pp (N = 6,856)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,609 | 38.0% |
| BOOK_QUALITY | execution | 1,225 | 17.9% |
| STALE_QUOTE | market_freshness | 1,114 | 16.2% |
| POOR_DATA | data | 564 | 8.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 379 | 5.5% |
| IDENTITY_AMBIGUOUS | mapping | 289 | 4.2% |
| LIMITED_DATA | data | 285 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 226 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 139 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 26 | 0.4% |

Cause class: coverage 38.0%, execution 17.9%, market_freshness 16.2%, data 12.4%, market_freshness/coverage 8.8%, mapping 4.2%, model_calibration_or_unknown 2.0%, model_calibration 0.4%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.2%, START_UNVERIFIABLE 98.2%, LOW_DATA_QUALITY 72.0%, THIN_PLAYER_HISTORY 59.2%, STALE_KALSHI_QUOTE 53.2%, STALE_PLAYER_DATA 50.2%, MODEL_INTERNAL_DISAGREEMENT 39.6%, ASYMMETRIC_SAMPLE_SIZE 33.0%, WIDE_SPREAD 23.8%, MODEL_HIGH_UNCERTAINTY 17.4%, PLAYER_IDENTITY_RISK 16.4%, EVENT_MAPPING_RISK 9.7%, LEVEL_TRANSFER_RISK 7.7%, LOW_DISPLAYED_LIQUIDITY 7.6%, MODEL_CALIBRATION_OUTLIER 4.6%, EXTERNAL_MARKET_REJECTION 0.8%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 40.8%, POST_SETTLEMENT_OBSERVATION 38.0%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 5561, "IDENTITY_AMBIGUOUS": 1295}; ticker orientation: {"VERIFIED": 6856}.

Checks: discipline:AMBIGUOUS 482, discipline:PASS 6374, identity_confidence:AMBIGUOUS 1124, identity_confidence:PASS 5732, level_mapping:NA 494, level_mapping:PASS 6362, market_pair:AMBIGUOUS 236, market_pair:NA 170, market_pair:PASS 6450, model_complement:NA 137, model_complement:PASS 6719, namesake:PASS 6856, physical_match_id:NA 2732, physical_match_id:PASS 4124, player_ids:PASS 6856, same_pair_other_event:PASS 6856, ticker_orientation:PASS 6856

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,024 | 1.4% | 1.4% | 0.4% | {"market_freshness": 20, "execution": 8, "market_freshness/coverage": 1} | 5.27 | 0.2124 / 0.2138 (243) | 16.4% | 0.5% | 5.5% | 1.7% |
| CHALLENGER | 5,075 | 17.0% | 5.9% | 12.6% | {"coverage": 523, "market_freshness": 109, "market_freshness/coverage": 105, "data": 57, "model_calibration_or_unknown": 45, "execution": 12, "mapping": 6, "model_calibration": 4} | 7.24 | 0.2166 / 0.2025 (1300) | 37.9% | 8.7% | 2.4% | 22.3% |
| DOUBLES | 955 | 50.5% | 49.9% | 7.0% | {"execution": 189, "mapping": 147, "market_freshness": 106, "market_freshness/coverage": 33, "coverage": 7} | 24.89 | 0.3357 / 0.2324 (268) | 24.5% | 0.0% | 100.0% | 7.3% |
| ITF_MEN | 9,180 | 23.9% | 16.1% | 32.0% | {"coverage": 877, "execution": 474, "market_freshness": 300, "data": 298, "market_freshness/coverage": 187, "mapping": 57, "model_calibration_or_unknown": 2} | 10.73 | 0.2099 / 0.194 (2272) | 35.8% | 56.9% | 9.2% | 23.4% |
| ITF_WOMEN | 11,502 | 26.3% | 18.2% | 44.1% | {"coverage": 1185, "execution": 521, "market_freshness": 508, "data": 460, "market_freshness/coverage": 234, "mapping": 73, "model_calibration_or_unknown": 31, "model_calibration": 10} | 12.34 | 0.2032 / 0.1921 (2509) | 37.8% | 58.1% | 9.8% | 23.5% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,539 | 6.3% | 5.6% | 1.4% | {"market_freshness": 36, "model_calibration_or_unknown": 22, "data": 11, "market_freshness/coverage": 10, "execution": 7, "model_calibration": 6, "coverage": 4, "mapping": 1} | 7.75 | 0.2329 / 0.2248 (251) | 26.2% | 1.4% | 1.8% | 3.0% |
| WTA125 | 1,211 | 13.1% | 10.3% | 2.3% | {"model_calibration_or_unknown": 37, "market_freshness/coverage": 34, "market_freshness": 33, "data": 23, "coverage": 12, "execution": 9, "model_calibration": 6, "mapping": 4} | 9.33 | 0.2188 / 0.2098 (414) | 22.8% | 8.4% | 4.2% | 10.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 5 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 6 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 7 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 151 min (STALE); no external reference |
| 8 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 9 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 10 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 11 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 12 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 13 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 14 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 15 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 16 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 17 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 18 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 19 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 20 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 21 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 22 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 23 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 24 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 25 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 26 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 27 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 765 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 28 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 29 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 30 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 33 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 31 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 32 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 33 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 34 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 35 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 36 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 37 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 38 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 39 | `KXATPCHALLENGERMATCH-26OCT13GIUSEA-SEA` | CHALLENGER | fair_v1 | 76% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 757 min (STALE); no external reference |
| 40 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 189 min (STALE); no external reference |
| 41 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 42 | `KXITFWMATCH-26OCT13MAMSTR-MAM` | ITF_WOMEN | fair_v1 | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 406 min (STALE); data LIMITED (grade C, thinner serve sample 879.0, ratio 2.64); no external reference |
| 43 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 44 | `KXITFMATCH-26OCT13VISMUE-MUE` | ITF_MEN | fair_v1 | 25% / 98% | -74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 617 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 0.0); no external reference |
| 45 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 46 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 47 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 48 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 253 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 49 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 50 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 22 min (AGING); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9817, "by_level_share_of_ge_25pp": {"ATP": 0.0042, "CHALLENGER": 0.1256, "DOUBLES": 0.0703, "ITF_MEN": 0.3202, "ITF_WOMEN": 0.4408, "OTHER": 0.0018, "WTA": 0.0141, "WTA125": 0.023}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5325, "share_primary_cause_market_settled_or_in_play": 0.4688, "share_primary_cause_stale_quote_only": 0.1625}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 6856, "identity_ambiguous_share": 0.1889, "ticker_orientation": {"VERIFIED": 6856}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 4124, "with_external": 136, "coverage": 0.033, "external_status": {"EXTERNAL_STALE": 97, "AGREES_WITH_KALSHI": 37, "SUPPORTS_MODEL_DIRECTION": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 97, "MODEL_LONE_OUTLIER": 37, "ALL_THREE_DISAGREE": 2}, "share_external_agrees_with_kalshi": 0.2721, "share_external_supports_model": 0.0147}, "pregame_clean_ge_25pp": {"n": 1843, "with_external": 128, "coverage": 0.0695, "external_status": {"EXTERNAL_STALE": 91, "AGREES_WITH_KALSHI": 35, "SUPPORTS_MODEL_DIRECTION": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 91, "MODEL_LONE_OUTLIER": 35, "ALL_THREE_DISAGREE": 2}, "share_external_agrees_with_kalshi": 0.2734, "share_external_supports_model": 0.0156}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 586.5, "median_sample_ratio": 2.34, "median_min_matches": 20.0, "median_max_days_since_last": 203.0, "share_severe_asymmetry": 0.1908, "data_status": {"POOR": 3587, "LIMITED": 2008, "ADEQUATE": 1261}, "comparison_lt_10pp": {"median_thinner_serve_points": 1869.0, "median_sample_ratio": 1.67, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 561, "model_minus_observed": 0.0564, "kalshi_minus_observed": -0.0747, "brier_diff_model_minus_kalshi": 0.0021}, "4-10x": {"n": 374, "model_minus_observed": 0.0622, "kalshi_minus_observed": -0.0783, "brier_diff_model_minus_kalshi": 0.0037}, "<2x": {"n": 1326, "model_minus_observed": 0.0826, "kalshi_minus_observed": -0.0392, "brier_diff_model_minus_kalshi": 0.0105}, ">=10x": {"n": 407, "model_minus_observed": 0.1148, "kalshi_minus_observed": -0.0528, "brier_diff_model_minus_kalshi": 0.0124}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2668, "model": {"intercept": -0.553, "slope": 0.877, "slope_se": 0.049}, "kalshi_mid_same_rows": {"intercept": 0.223, "slope": 1.129, "slope_se": 0.056}, "mean_extremity_model": 0.1807, "mean_extremity_kalshi": 0.1698, "model_brier": 0.228, "kalshi_brier": 0.2016, "brier_diff_model_minus_kalshi": 0.0264, "brier_diff_se": 0.0036, "model_logloss": 0.651, "kalshi_logloss": 0.5852}, "fair_v1": {"n": 2668, "model": {"intercept": -0.391, "slope": 1.075, "slope_se": 0.055}, "kalshi_mid_same_rows": {"intercept": 0.333, "slope": 1.189, "slope_se": 0.058}, "mean_extremity_model": 0.1691, "mean_extremity_kalshi": 0.1699, "model_brier": 0.2099, "kalshi_brier": 0.2018, "brier_diff_model_minus_kalshi": 0.0081, "brier_diff_se": 0.0029, "model_logloss": 0.6067, "kalshi_logloss": 0.5854}, "gen1_elo": {"n": 2668, "model": {"intercept": -0.358, "slope": 1.054, "slope_se": 0.053}, "kalshi_mid_same_rows": {"intercept": 0.349, "slope": 1.183, "slope_se": 0.057}, "mean_extremity_model": 0.1733, "mean_extremity_kalshi": 0.1703, "model_brier": 0.2088, "kalshi_brier": 0.2019, "brier_diff_model_minus_kalshi": 0.0069, "brier_diff_se": 0.0029, "model_logloss": 0.6053, "kalshi_logloss": 0.5855}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2418, "share_ge_15": 0.4302, "median_abs_gap": 12.79, "n": 17056}, "gen1_elo": {"share_ge_25": 0.2365, "share_ge_15": 0.424, "median_abs_gap": 12.26, "n": 17056}, "gen1_sr": {"share_ge_25": 0.2977, "share_ge_15": 0.5145, "median_abs_gap": 15.51, "n": 17056}, "gen2": {"share_ge_25": 0.3011, "share_ge_15": 0.5035, "median_abs_gap": 15.19, "n": 17056}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1416, "share_ge_15": 0.335, "median_abs_gap": 10.36, "n": 13019}, "gen1_elo": {"share_ge_25": 0.1397, "share_ge_15": 0.3251, "median_abs_gap": 9.8, "n": 13018}, "gen1_sr": {"share_ge_25": 0.1976, "share_ge_15": 0.4287, "median_abs_gap": 12.74, "n": 13019}, "gen2": {"share_ge_25": 0.2146, "share_ge_15": 0.4308, "median_abs_gap": 12.7, "n": 13020}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.27, "share_ge_25_all": 0.0143, "share_ge_25_pregame_clean": 0.0141}, "WTA": {"median_abs_gap_pregame_clean": 7.75, "share_ge_25_all": 0.063, "share_ge_25_pregame_clean": 0.0556}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2405, "share_within_10pp_all": 0.4428, "share_within_10pp_pregame_clean": 0.5031, "corr_model_vs_mid_pregame_clean": 0.8493}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 410, "model_brier": 0.1925, "kalshi_brier": 0.1939, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 478, "model_brier": 0.2096, "kalshi_brier": 0.2025, "brier_diff_model_minus_kalshi": 0.0071}, "15-25": {"n_settled": 574, "model_brier": 0.2267, "kalshi_brier": 0.2146, "brier_diff_model_minus_kalshi": 0.0121}, "25-40": {"n_settled": 311, "model_brier": 0.2235, "kalshi_brier": 0.2079, "brier_diff_model_minus_kalshi": 0.0156}, "3-5": {"n_settled": 271, "model_brier": 0.1898, "kalshi_brier": 0.1905, "brier_diff_model_minus_kalshi": -0.0006}, "40+": {"n_settled": 68, "model_brier": 0.2909, "kalshi_brier": 0.1768, "brier_diff_model_minus_kalshi": 0.1141}, "5-10": {"n_settled": 556, "model_brier": 0.1979, "kalshi_brier": 0.1991, "brier_diff_model_minus_kalshi": -0.0012}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.553, "slope": 0.877, "slope_se": 0.049}, "kalshi_slope": {"intercept": 0.223, "slope": 1.129, "slope_se": 0.056}, "n": 2668}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.503, "slope": 0.884, "slope_se": 0.037}, "kalshi_slope": {"intercept": 0.167, "slope": 1.094, "slope_se": 0.041}, "n": 4631}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 268, "model_brier": 0.3357, "kalshi_brier": 0.2324, "brier_diff_model_minus_kalshi": 0.1033, "brier_diff_se": 0.0199, "corr_model_outcome": -0.0413, "corr_kalshi_outcome": 0.2681}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
