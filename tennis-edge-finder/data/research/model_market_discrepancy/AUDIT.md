# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-18T10:02Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 38,478): 0-3 14.5%, 3-5 9.5%, 5-10 19.9%, 10-15 15.4%, 15-25 18.9%, 25-40 13.7%, 40+ 8.2%; median gap 11.88 pp.
* **Where the extremes live**: 97.7% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.0%, Challenger 12.2%, doubles 7.3%). Main tour: ATP 3.1% and WTA 5.2% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 8,418): MARKET_ALREADY_SETTLED_WHEN_PRICED 35.3%, BOOK_QUALITY 19.1%, STALE_QUOTE 17.9%, POOR_DATA 8.5%, POSSIBLY_IN_PLAY_QUOTE 5.2%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 3.9%, IN_PLAY_QUOTE 3.2%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.5%. By class: coverage 35.3%, execution 19.1%, market_freshness 17.9%, data 12.4%, market_freshness/coverage 8.5%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.5%.
* **Stale / settled / in-play**: 52.3% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 8,418 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 23.2% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 545.0 points vs 1841.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.048, Gen-2 0.845, Gen-1 ledger 0.877 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 381 model 0.2251 vs Kalshi 0.2074; n 79 model 0.3062 vs Kalshi 0.1714.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 159,285 model-market comparisons (260,701 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 57,597 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-18T09:52:29.348618+00:00'], shadow board 42,445 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-18T09:52:32.932507+00:00'], Model 4 18,300 rows, 15,769 settled tickers, 5,424 tickers with an external scan.
* By model: {"gen1_ledger": 38793, "gen1_elo": 21345, "fair_v1": 21345, "gen2": 21345, "gen1_sr": 21345, "model4_fundamental": 17563, "model4_conditioned": 17549}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 38,478 | 14.5 | 9.5 | 19.9 | 15.4 | 18.9 | 13.7 | 8.2 | 11.88 | 40.7% | 21.9% |
| MW fair_v1 | 21,345 | 13.6 | 8.5 | 18.5 | 15.9 | 19.2 | 14.6 | 9.8 | 12.96 | 43.6% | 24.4% |
| MW gen1_elo | 21,345 | 13.1 | 9.1 | 19.4 | 15.2 | 19.4 | 14.3 | 9.5 | 12.52 | 43.1% | 23.8% |
| MW gen1_ledger | 17,133 | 15.6 | 10.8 | 21.6 | 14.8 | 18.4 | 12.6 | 6.2 | 10.48 | 37.2% | 18.8% |
| MW gen1_sr | 21,345 | 9.7 | 7.4 | 16.6 | 14.2 | 21.6 | 18.5 | 12.0 | 15.76 | 52.1% | 30.5% |
| MW gen2 | 21,345 | 11.4 | 7.1 | 16.5 | 14.2 | 19.9 | 17.6 | 13.2 | 15.38 | 50.8% | 30.8% |
| all families model4_conditioned | 17,549 | 21.6 | 19.1 | 34.5 | 17.4 | 4.7 | 1.5 | 1.2 | 5.95 | 7.4% | 2.7% |
| all families model4_fundamental | 17,563 | 16.2 | 13.0 | 34.7 | 20.2 | 11.1 | 3.4 | 1.5 | 7.87 | 15.9% | 4.9% |

Configurable thresholds (primary): >=5pp 76.0%, >=10pp 56.1%, >=15pp 40.7%, >=20pp 30.3%, >=25pp 21.9%, >=30pp 15.8%, >=40pp 8.2%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.2pp; >=10pp 44.6%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,729 | 29.4 | 13.6 | 24.5 | 17.4 | 11.6 | 2.9 | 0.7 | 6.17 | 15.2% | 3.6% |
| CHALLENGER | 3,516 | 16.0 | 10.1 | 20.1 | 15.8 | 14.3 | 12.4 | 11.2 | 11.22 | 37.9% | 23.7% |
| ITF_MEN | 5,892 | 11.0 | 8.0 | 17.5 | 14.9 | 19.9 | 16.2 | 12.4 | 14.45 | 48.5% | 28.6% |
| ITF_WOMEN | 8,340 | 10.3 | 6.7 | 15.9 | 15.5 | 22.3 | 18.2 | 11.2 | 15.65 | 51.7% | 29.4% |
| WTA | 1,209 | 19.3 | 12.2 | 24.9 | 18.4 | 19.4 | 4.9 | 0.9 | 8.17 | 25.1% | 5.8% |
| WTA125 | 659 | 13.3 | 7.4 | 23.5 | 20.3 | 19.9 | 13.5 | 2.0 | 11.31 | 35.4% | 15.5% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,729 | 23.4 | 14.5 | 24.6 | 18.2 | 14.3 | 4.0 | 1.0 | 6.9 | 19.3% | 5.0% |
| CHALLENGER | 3,516 | 14.7 | 8.1 | 19.2 | 13.7 | 18.1 | 14.3 | 11.9 | 12.72 | 44.3% | 26.2% |
| ITF_MEN | 5,892 | 9.3 | 6.7 | 15.7 | 13.7 | 19.8 | 19.3 | 15.5 | 16.94 | 54.6% | 34.8% |
| ITF_WOMEN | 8,340 | 8.5 | 5.6 | 13.7 | 13.5 | 21.1 | 20.8 | 16.9 | 18.85 | 58.8% | 37.7% |
| WTA | 1,209 | 17.4 | 7.8 | 20.3 | 15.9 | 22.8 | 14.9 | 1.0 | 11.62 | 38.6% | 15.9% |
| WTA125 | 659 | 6.8 | 4.7 | 17.0 | 17.4 | 25.9 | 19.3 | 8.8 | 16.84 | 54.0% | 28.1% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,729 | 25.8 | 13.8 | 25.8 | 16.8 | 13.5 | 3.5 | 0.8 | 6.58 | 17.8% | 4.3% |
| CHALLENGER | 3,516 | 15.0 | 10.3 | 20.6 | 15.0 | 15.5 | 12.1 | 11.5 | 11.05 | 39.1% | 23.6% |
| ITF_MEN | 5,892 | 10.0 | 8.1 | 17.9 | 14.2 | 20.7 | 16.6 | 12.4 | 14.97 | 49.8% | 29.1% |
| ITF_WOMEN | 8,340 | 9.6 | 6.9 | 16.3 | 15.6 | 22.9 | 18.3 | 10.3 | 15.58 | 51.5% | 28.6% |
| WTA | 1,209 | 23.3 | 16.9 | 30.9 | 15.2 | 11.1 | 2.0 | 0.6 | 6.04 | 13.7% | 2.6% |
| WTA125 | 659 | 22.9 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.73 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,096 | 27.9 | 20.4 | 31.9 | 11.5 | 6.0 | 2.2 | 0.1 | 5.11 | 8.3% | 2.3% |
| CHALLENGER | 2,455 | 22.2 | 15.2 | 26.9 | 14.1 | 13.8 | 5.8 | 2.0 | 7.01 | 21.6% | 7.8% |
| DOUBLES | 1,253 | 4.8 | 4.2 | 10.1 | 10.8 | 21.0 | 25.9 | 23.1 | 24.22 | 70.0% | 49.0% |
| ITF_MEN | 4,949 | 14.6 | 8.6 | 20.7 | 15.8 | 20.9 | 12.5 | 7.0 | 11.86 | 40.4% | 19.4% |
| ITF_WOMEN | 5,605 | 11.8 | 9.1 | 19.1 | 14.8 | 22.1 | 16.9 | 6.2 | 13.2 | 45.2% | 23.2% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 895 | 22.1 | 15.8 | 29.5 | 17.6 | 10.6 | 4.0 | 0.3 | 6.86 | 15.0% | 4.4% |
| WTA125 | 731 | 21.5 | 14.1 | 22.0 | 18.2 | 14.4 | 7.8 | 2.0 | 8.14 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,697 | 29.6 | 13.7 | 24.8 | 17.2 | 11.5 | 2.5 | 0.7 | 6.04 | 14.7% | 3.2% |
| CHALLENGER | 2,530 | 20.6 | 12.7 | 25.2 | 18.2 | 14.7 | 6.4 | 2.2 | 8.23 | 23.4% | 8.7% |
| ITF_MEN | 4,280 | 13.6 | 9.9 | 20.8 | 16.9 | 20.2 | 13.1 | 5.5 | 11.54 | 38.8% | 18.6% |
| ITF_WOMEN | 6,247 | 12.1 | 8.0 | 18.1 | 17.6 | 23.7 | 15.4 | 5.1 | 13.3 | 44.2% | 20.4% |
| WTA | 1,184 | 19.4 | 11.7 | 25.1 | 18.5 | 19.5 | 4.8 | 0.9 | 8.18 | 25.2% | 5.7% |
| WTA125 | 633 | 13.7 | 7.3 | 23.1 | 20.7 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,697 | 23.5 | 14.7 | 24.6 | 18.3 | 14.2 | 3.8 | 0.9 | 6.86 | 18.9% | 4.7% |
| CHALLENGER | 2,530 | 18.7 | 10.4 | 23.9 | 16.4 | 18.5 | 9.6 | 2.6 | 9.18 | 30.7% | 12.2% |
| ITF_MEN | 4,281 | 11.0 | 8.0 | 18.1 | 15.4 | 21.9 | 17.0 | 8.5 | 14.12 | 47.4% | 25.5% |
| ITF_WOMEN | 6,247 | 9.5 | 6.3 | 15.2 | 14.9 | 23.1 | 20.3 | 10.7 | 16.57 | 54.1% | 31.0% |
| WTA | 1,184 | 17.4 | 7.7 | 20.3 | 15.9 | 22.7 | 15.0 | 1.0 | 11.68 | 38.8% | 16.1% |
| WTA125 | 633 | 6.6 | 4.9 | 17.1 | 17.9 | 25.9 | 19.8 | 7.9 | 16.74 | 53.5% | 27.7% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,066 | 28.1 | 20.5 | 32.3 | 11.6 | 5.4 | 2.0 | 0.1 | 5.07 | 7.5% | 2.1% |
| CHALLENGER | 2,125 | 23.9 | 16.5 | 28.7 | 13.9 | 13.1 | 3.2 | 0.6 | 6.37 | 17.0% | 3.9% |
| DOUBLES | 1,161 | 4.8 | 4.4 | 10.3 | 11.0 | 20.8 | 26.0 | 22.6 | 24.07 | 69.4% | 48.6% |
| ITF_MEN | 4,097 | 15.9 | 9.4 | 22.6 | 16.7 | 20.7 | 10.6 | 4.1 | 10.61 | 35.4% | 14.7% |
| ITF_WOMEN | 4,639 | 12.7 | 9.7 | 20.7 | 15.6 | 22.3 | 15.6 | 3.5 | 11.9 | 41.3% | 19.1% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 857 | 22.5 | 16.2 | 29.8 | 17.6 | 10.7 | 3.1 | 0.0 | 6.8 | 13.9% | 3.1% |
| WTA125 | 621 | 23.5 | 15.6 | 23.5 | 19.6 | 12.7 | 4.7 | 0.3 | 7.2 | 17.7% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,253 | 4.8 | 4.2 | 10.1 | 10.8 | 21.0 | 25.9 | 23.1 | 24.22 | 70.0% | 49.0% |
| singles | 15,880 | 16.5 | 11.3 | 22.6 | 15.1 | 18.2 | 11.5 | 4.8 | 9.91 | 34.6% | 16.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 4,936 | 13.4 | 8.9 | 19.2 | 15.9 | 18.1 | 14.5 | 10.0 | 12.71 | 42.6% | 24.5% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 13,796 | 13.9 | 8.5 | 18.4 | 15.5 | 19.6 | 14.4 | 9.7 | 12.96 | 43.7% | 24.1% |
| UNKNOWN | 2,376 | 12.2 | 7.4 | 17.2 | 18.2 | 19.1 | 15.7 | 10.3 | 13.3 | 45.0% | 26.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,285 | 19.8 | 10.8 | 21.2 | 17.3 | 15.8 | 8.7 | 6.3 | 9.45 | 30.9% | 15.1% |
| B | 2,769 | 13.4 | 9.2 | 19.9 | 16.5 | 18.4 | 12.0 | 10.7 | 12.04 | 41.1% | 22.7% |
| C | 3,100 | 12.9 | 9.3 | 19.5 | 14.3 | 19.0 | 15.0 | 10.0 | 12.77 | 44.0% | 24.9% |
| D | 3,585 | 12.2 | 7.9 | 17.2 | 15.6 | 21.9 | 15.6 | 9.7 | 13.96 | 47.2% | 25.3% |
| F | 5,606 | 8.0 | 5.5 | 14.9 | 15.0 | 21.8 | 21.5 | 13.3 | 17.71 | 56.6% | 34.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,071 | 23.2 | 15.9 | 28.9 | 15.2 | 11.2 | 4.1 | 1.5 | 6.62 | 16.7% | 5.6% |
| B | 2,458 | 15.3 | 10.1 | 23.9 | 16.4 | 19.2 | 11.0 | 4.1 | 10.15 | 34.3% | 15.1% |
| C | 3,437 | 11.4 | 7.7 | 17.6 | 14.3 | 21.5 | 16.5 | 11.1 | 14.54 | 49.1% | 27.6% |
| D | 2,492 | 14.2 | 9.8 | 20.1 | 13.8 | 20.8 | 14.5 | 6.7 | 12.05 | 42.0% | 21.2% |
| F | 3,675 | 10.2 | 7.7 | 14.9 | 14.2 | 23.5 | 20.4 | 9.0 | 16.3 | 52.9% | 29.4% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 7,119 | 17.9 | 9.8 | 20.5 | 17.0 | 16.3 | 9.7 | 8.8 | 10.5 | 34.8% | 18.5% |
| LIMITED | 4,868 | 14.6 | 10.4 | 20.5 | 15.3 | 18.5 | 13.2 | 7.5 | 11.32 | 39.1% | 20.6% |
| POOR | 9,358 | 9.7 | 6.5 | 15.9 | 15.3 | 21.8 | 19.0 | 11.8 | 15.96 | 52.6% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,228 | 27.3 | 22.1 | 35.1 | 10.8 | 3.4 | 1.1 | 0.2 | 5.04 | 4.7% | 1.3% |
| GAME_SPREAD | 3,619 | 24.3 | 15.2 | 34.8 | 17.5 | 6.6 | 1.3 | 0.2 | 6.28 | 8.1% | 1.5% |
| MATCH_WINNER | 17,133 | 15.6 | 10.8 | 21.6 | 14.8 | 18.4 | 12.6 | 6.2 | 10.48 | 37.2% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 7,909 | 30.6 | 17.9 | 30.6 | 12.1 | 7.2 | 1.2 | 0.4 | 5.16 | 8.9% | 1.7% |
| TOTAL_GAMES | 5,880 | 6.8 | 8.9 | 37.2 | 28.7 | 11.5 | 3.7 | 3.1 | 9.67 | 18.3% | 6.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,157 | 24.9 | 35.2 | 31.8 | 3.5 | 3.7 | 0.7 | 0.2 | 4.45 | 4.6% | 0.9% |
| GAME_SPREAD | 4,243 | 46.0 | 16.6 | 27.5 | 7.2 | 1.7 | 0.7 | 0.3 | 3.44 | 2.6% | 1.0% |
| TOTAL_GAMES | 7,149 | 4.2 | 6.6 | 41.0 | 35.5 | 7.4 | 2.8 | 2.5 | 9.83 | 12.7% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,158 | 24.7 | 17.6 | 36.1 | 11.7 | 7.0 | 2.5 | 0.4 | 5.79 | 9.9% | 2.9% |
| GAME_SPREAD | 4,245 | 19.4 | 13.6 | 28.7 | 20.2 | 13.7 | 3.4 | 0.9 | 7.85 | 18.1% | 4.4% |
| TOTAL_GAMES | 7,160 | 7.0 | 8.7 | 37.1 | 27.5 | 13.0 | 4.1 | 2.7 | 9.7 | 19.8% | 6.8% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 21,345 | 43.6% | 24.4% | 12.96 | 34.9% | 15.1% | 10.7 |
| gen1_elo | 21,345 | 43.1% | 23.8% | 12.52 | 34.1% | 14.9% | 10.18 |
| gen1_sr | 21,345 | 52.1% | 30.5% | 15.76 | 44.3% | 21.3% | 13.15 |
| gen2 | 21,345 | 50.8% | 30.8% | 15.38 | 44.1% | 22.8% | 13.02 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 11,375 | 16.4 | 10.4 | 21.4 | 17.4 | 19.6 | 11.4 | 3.3 | 10.5 | 34.3% | 14.7% |
| STALE | 9,970 | 10.3 | 6.3 | 15.1 | 14.1 | 18.8 | 18.2 | 17.2 | 17.16 | 54.2% | 35.4% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 10,601 | 17.1 | 11.5 | 22.8 | 14.8 | 17.2 | 11.6 | 4.9 | 9.64 | 33.7% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 38,478 | 10601 | 14847 | 13030 | 23.7 | 140.8 | 1400.4 |
| ge_15pp | 15,677 | 3575 | 5191 | 6911 | 25.8 | 445.7 | 1380.4 |
| ge_25pp | 8,418 | 1752 | 2263 | 4403 | 32.9 | 584.0 | 1380.4 |
| lt_10pp | 16,883 | 5458 | 7123 | 4302 | 21.8 | 47.9 | 1341.5 |

Current slate `SL-20261018T100251Z-c241aab1`: 988 priced rows, quote age at build {'median': 11.0, 'max': 11.0}, freshness {'AGING': 988}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 11 | 0.0 | 0.0 | 36.4 | 0.0 | 45.5 | 18.2 | 0.0 | 20.19 | 63.6% | 18.2% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,953 | 21.4 | 10.8 | 23.0 | 18.9 | 18.6 | 6.7 | 0.5 | 8.65 | 25.8% | 7.2% |
| KALSHI_LONE_OUTLIER | 11 | 9.1 | 0.0 | 72.7 | 0.0 | 9.1 | 9.1 | 0.0 | 5.2 | 18.2% | 9.1% |
| MARKETS_AGREE | 344 | 70.1 | 29.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.09 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 704 | 0.0 | 3.0 | 35.5 | 28.8 | 23.3 | 8.7 | 0.7 | 11.87 | 32.7% | 9.4% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 21,345 | 3035 (14.2%) | 23.2% | 0.7% | {"EXTERNAL_STALE": 1953, "AGREES_WITH_KALSHI": 704, "ALL_AGREE": 344, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 11, "SUPPORTS_MODEL_DIRECTION": 10, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 9,303 | 743 (8.0%) | 31.0% | 1.2% | {"EXTERNAL_STALE": 504, "AGREES_WITH_KALSHI": 230, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 5,204 | 210 (4.0%) | 31.4% | 1.4% | {"EXTERNAL_STALE": 141, "AGREES_WITH_KALSHI": 66, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,508 | 198 (7.9%) | 32.3% | 1.5% | {"EXTERNAL_STALE": 131, "AGREES_WITH_KALSHI": 64, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 8,656 | 1719 (19.9%) | 15.8% | 0.7% | {"EXTERNAL_STALE": 1079, "ALL_AGREE": 344, "AGREES_WITH_KALSHI": 271, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 9, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 4,112 | 11.3 | 7.8 | 19.3 | 15.0 | 21.5 | 14.9 | 10.2 | 13.79 | 46.6% | 25.1% |
| 4-10x | 2,748 | 12.6 | 8.8 | 19.2 | 15.5 | 19.3 | 15.2 | 9.4 | 12.97 | 43.9% | 24.6% |
| <2x | 11,131 | 15.5 | 9.3 | 19.0 | 16.9 | 17.7 | 12.8 | 8.9 | 11.81 | 39.4% | 21.6% |
| >=10x | 3,354 | 10.8 | 6.4 | 15.3 | 13.9 | 21.3 | 19.5 | 12.8 | 16.38 | 53.6% | 32.3% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 5,597 | 13.2 | 8.4 | 19.4 | 15.9 | 19.6 | 13.2 | 10.3 | 12.81 | 43.1% | 23.5% |
| 300-1000 | 4,727 | 12.3 | 8.7 | 17.1 | 15.7 | 20.6 | 16.2 | 9.5 | 13.72 | 46.2% | 25.7% |
| <300 | 6,374 | 9.1 | 5.9 | 15.5 | 14.8 | 21.7 | 20.1 | 12.9 | 16.84 | 54.7% | 33.0% |
| >=3000 | 4,647 | 21.5 | 12.0 | 22.9 | 17.3 | 14.0 | 7.0 | 5.3 | 8.23 | 26.3% | 12.3% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 647 | 0.5387 | 0.4054 | 0.4838 | +0.055 | -0.078 | 0.0015 ± 0.0059 |
| ratio 4-10x | 433 | 0.5845 | 0.4465 | 0.5035 | +0.081 | -0.057 | 0.0094 ± 0.0075 |
| ratio <2x | 1613 | 0.5372 | 0.4155 | 0.4495 | +0.088 | -0.034 | 0.0129 ± 0.0035 |
| ratio >=10x | 527 | 0.548 | 0.3801 | 0.4231 | +0.125 | -0.043 | 0.0163 ± 0.0077 |
| thinner_sample 1000-3000 | 915 | 0.5436 | 0.4178 | 0.4634 | +0.080 | -0.046 | 0.0077 ± 0.0047 |
| thinner_sample 300-1000 | 756 | 0.5615 | 0.4227 | 0.4841 | +0.077 | -0.061 | 0.0031 ± 0.0057 |
| thinner_sample <300 | 989 | 0.5442 | 0.3839 | 0.4328 | +0.111 | -0.049 | 0.0175 ± 0.0055 |
| thinner_sample >=3000 | 560 | 0.5299 | 0.4368 | 0.4661 | +0.064 | -0.029 | 0.014 ± 0.0049 |
| data_status ADEQUATE | 956 | 0.5334 | 0.4292 | 0.4592 | +0.074 | -0.030 | 0.0105 ± 0.004 |
| data_status LIMITED | 799 | 0.5525 | 0.4232 | 0.4856 | +0.067 | -0.062 | 0.0045 ± 0.0052 |
| data_status POOR | 1465 | 0.5498 | 0.3943 | 0.4451 | +0.105 | -0.051 | 0.0142 ± 0.0044 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 497 | 0.1929 | 0.1943 | -0.0013 ± 0.0007 | 0.564 | 0.5668 | 0.4944 | 0.4796 | 0.5292 | -0.043 ± 0.0207 | -0.01 (5) |
| 3-5 | 313 | 0.195 | 0.1945 | +0.0005 ± 0.002 | 0.5712 | 0.5688 | 0.506 | 0.466 | 0.4792 | -0.080 ± 0.0257 | 0.02 (1) |
| 5-10 | 678 | 0.1989 | 0.1982 | +0.0008 ± 0.0026 | 0.5836 | 0.5799 | 0.5108 | 0.4364 | 0.4631 | -0.085 ± 0.0177 | -0.0167 (6) |
| 10-15 | 570 | 0.2148 | 0.2055 | +0.0093 ± 0.0048 | 0.6199 | 0.5931 | 0.52 | 0.3959 | 0.4193 | -0.089 ± 0.019 | -0.048 (5) |
| 15-25 | 702 | 0.2296 | 0.2129 | +0.0168 ± 0.0068 | 0.6538 | 0.611 | 0.5766 | 0.3817 | 0.4373 | -0.087 ± 0.0174 | -0.0033 (9) |
| 25-40 | 381 | 0.2251 | 0.2074 | +0.0177 ± 0.0139 | 0.6394 | 0.5971 | 0.6473 | 0.3388 | 0.4646 | -0.064 ± 0.0212 | -0.01 (1) |
| 40+ | 79 | 0.3062 | 0.1714 | +0.1348 ± 0.0418 | 0.8247 | 0.5154 | 0.7425 | 0.2952 | 0.3671 | -0.124 ± 0.041 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2325 | 0.1805 | 0.1817 | -0.0012 ± 0.0003 | 0.536 | 0.5373 | 0.4787 | 0.4637 | 0.4994 | -0.019 ± 0.009 | -0.0129 (17) |
| 3-5 | 1463 | 0.1928 | 0.1908 | +0.0020 ± 0.0009 | 0.5659 | 0.557 | 0.4801 | 0.4403 | 0.434 | -0.063 ± 0.0117 | 0.0 (2) |
| 5-10 | 3145 | 0.1943 | 0.1917 | +0.0026 ± 0.0012 | 0.5713 | 0.5625 | 0.4824 | 0.4085 | 0.4264 | -0.045 ± 0.0079 | -0.0119 (21) |
| 10-15 | 2760 | 0.2027 | 0.183 | +0.0197 ± 0.002 | 0.5937 | 0.5387 | 0.4811 | 0.3564 | 0.3402 | -0.078 ± 0.0081 | -0.0281 (16) |
| 15-25 | 3342 | 0.2091 | 0.1709 | +0.0382 ± 0.0028 | 0.61 | 0.5055 | 0.5024 | 0.3062 | 0.3085 | -0.069 ± 0.0071 | -0.0025 (44) |
| 25-40 | 2617 | 0.2228 | 0.1252 | +0.0976 ± 0.0043 | 0.6394 | 0.3868 | 0.5288 | 0.2156 | 0.2205 | -0.064 ± 0.0067 | -0.01 (1) |
| 40+ | 1785 | 0.3784 | 0.0421 | +0.3363 ± 0.0054 | 0.9847 | 0.1682 | 0.6267 | 0.1053 | 0.0538 | -0.087 ± 0.0045 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 367 | 0.1974 | 0.1978 | -0.0004 ± 0.0008 | 0.576 | 0.577 | 0.501 | 0.4859 | 0.5041 | -0.082 ± 0.0245 | -0.01 (3) |
| 3-5 | 259 | 0.2134 | 0.2122 | +0.0012 ± 0.0023 | 0.6097 | 0.608 | 0.5162 | 0.4763 | 0.4749 | -0.088 ± 0.0304 | 0.02 (1) |
| 5-10 | 589 | 0.1992 | 0.1988 | +0.0004 ± 0.0028 | 0.582 | 0.5811 | 0.5476 | 0.4728 | 0.5076 | -0.072 ± 0.0189 | -0.01 (4) |
| 10-15 | 532 | 0.2197 | 0.2108 | +0.0088 ± 0.005 | 0.6298 | 0.6078 | 0.5678 | 0.4434 | 0.4737 | -0.096 ± 0.0209 | -0.04 (5) |
| 15-25 | 770 | 0.2291 | 0.2077 | +0.0214 ± 0.0065 | 0.6498 | 0.5977 | 0.5882 | 0.3917 | 0.439 | -0.089 ± 0.0167 | -0.0133 (9) |
| 25-40 | 512 | 0.269 | 0.1955 | +0.0735 ± 0.0124 | 0.7493 | 0.5713 | 0.6592 | 0.3444 | 0.3867 | -0.120 ± 0.0195 | -0.0075 (4) |
| 40+ | 191 | 0.3649 | 0.1779 | +0.1870 ± 0.0301 | 1.0145 | 0.527 | 0.741 | 0.2585 | 0.3194 | -0.071 ± 0.0295 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1956 | 0.1831 | 0.1836 | -0.0004 ± 0.0003 | 0.5417 | 0.5425 | 0.5017 | 0.487 | 0.5082 | -0.034 ± 0.01 | -0.0133 (15) |
| 3-5 | 1239 | 0.1949 | 0.1937 | +0.0012 ± 0.001 | 0.5652 | 0.5623 | 0.5151 | 0.4751 | 0.4794 | -0.046 ± 0.0128 | 0.02 (1) |
| 5-10 | 2818 | 0.1922 | 0.1896 | +0.0026 ± 0.0012 | 0.5671 | 0.558 | 0.5093 | 0.4353 | 0.4564 | -0.040 ± 0.0083 | -0.0117 (6) |
| 10-15 | 2423 | 0.1999 | 0.1882 | +0.0117 ± 0.0022 | 0.5888 | 0.5491 | 0.5203 | 0.3958 | 0.4135 | -0.051 ± 0.009 | -0.0189 (18) |
| 15-25 | 3496 | 0.217 | 0.1768 | +0.0403 ± 0.0028 | 0.6293 | 0.5216 | 0.5321 | 0.3359 | 0.3341 | -0.074 ± 0.0072 | -0.0086 (42) |
| 25-40 | 3083 | 0.2511 | 0.1352 | +0.1159 ± 0.0042 | 0.7091 | 0.4158 | 0.5595 | 0.2437 | 0.2199 | -0.090 ± 0.0066 | -0.0044 (18) |
| 40+ | 2422 | 0.4019 | 0.0657 | +0.3362 ± 0.006 | 1.0603 | 0.2303 | 0.6626 | 0.1253 | 0.0941 | -0.070 ± 0.0051 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 477 | 0.1954 | 0.1976 | -0.0022 ± 0.0007 | 0.5712 | 0.5765 | 0.4981 | 0.4828 | 0.5472 | -0.016 ± 0.0208 | -0.0137 (8) |
| 3-5 | 356 | 0.1908 | 0.1888 | +0.0020 ± 0.0019 | 0.5585 | 0.5538 | 0.4983 | 0.4586 | 0.4551 | -0.112 ± 0.0242 | 0.0067 (3) |
| 5-10 | 708 | 0.2016 | 0.1975 | +0.0041 ± 0.0025 | 0.5904 | 0.5772 | 0.5034 | 0.4296 | 0.435 | -0.096 ± 0.0172 | -0.0071 (7) |
| 10-15 | 558 | 0.2077 | 0.2059 | +0.0018 ± 0.0047 | 0.6028 | 0.5949 | 0.537 | 0.4142 | 0.4713 | -0.067 ± 0.019 | -0.0317 (6) |
| 15-25 | 650 | 0.2348 | 0.2095 | +0.0253 ± 0.007 | 0.6694 | 0.603 | 0.5851 | 0.3918 | 0.4215 | -0.111 ± 0.0178 | -0.03 (1) |
| 25-40 | 395 | 0.212 | 0.2128 | -0.0008 ± 0.0136 | 0.6108 | 0.6093 | 0.6524 | 0.343 | 0.4962 | -0.044 ± 0.0207 | 0.015 (2) |
| 40+ | 76 | 0.3254 | 0.1849 | +0.1405 ± 0.0445 | 0.8712 | 0.5464 | 0.7463 | 0.2938 | 0.3684 | -0.109 ± 0.0466 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2219 | 0.1875 | 0.1882 | -0.0008 ± 0.0003 | 0.5521 | 0.5534 | 0.4858 | 0.4705 | 0.4935 | -0.029 ± 0.0093 | -0.0163 (35) |
| 3-5 | 1540 | 0.1877 | 0.1844 | +0.0034 ± 0.0009 | 0.5533 | 0.5451 | 0.4778 | 0.4383 | 0.4162 | -0.083 ± 0.0112 | -0.0094 (18) |
| 5-10 | 3363 | 0.1949 | 0.1883 | +0.0066 ± 0.0011 | 0.575 | 0.5533 | 0.4814 | 0.4075 | 0.3976 | -0.069 ± 0.0075 | -0.01 (31) |
| 10-15 | 2590 | 0.1962 | 0.1806 | +0.0156 ± 0.0021 | 0.577 | 0.5306 | 0.4967 | 0.3733 | 0.3722 | -0.066 ± 0.0083 | -0.015 (12) |
| 15-25 | 3454 | 0.2081 | 0.1692 | +0.0389 ± 0.0027 | 0.6098 | 0.5019 | 0.5046 | 0.3096 | 0.308 | -0.070 ± 0.007 | -0.03 (2) |
| 25-40 | 2563 | 0.2178 | 0.1234 | +0.0944 ± 0.0044 | 0.6281 | 0.3811 | 0.5255 | 0.2095 | 0.2224 | -0.060 ± 0.0066 | 0.01 (3) |
| 40+ | 1708 | 0.394 | 0.0462 | +0.3479 ± 0.0058 | 1.0273 | 0.1792 | 0.6382 | 0.1098 | 0.0562 | -0.089 ± 0.0049 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 827 | 0.1952 | 0.1953 | -0.0001 ± 0.0005 | 0.5709 | 0.5708 | 0.5079 | 0.4929 | 0.4958 | -0.053 ± 0.0155 | -0.0224 (49) |
| 3-5 | 580 | 0.1949 | 0.1941 | +0.0007 ± 0.0015 | 0.5681 | 0.5651 | 0.4799 | 0.4401 | 0.4483 | -0.050 ± 0.0184 | -0.0194 (34) |
| 5-10 | 1219 | 0.198 | 0.1919 | +0.0060 ± 0.0019 | 0.5832 | 0.5658 | 0.4885 | 0.415 | 0.4118 | -0.065 ± 0.0128 | -0.005 (78) |
| 10-15 | 775 | 0.2076 | 0.1959 | +0.0116 ± 0.004 | 0.6036 | 0.5735 | 0.507 | 0.3839 | 0.3974 | -0.057 ± 0.016 | 0.0014 (64) |
| 15-25 | 1028 | 0.2337 | 0.2122 | +0.0215 ± 0.0056 | 0.6658 | 0.6106 | 0.5659 | 0.371 | 0.4144 | -0.056 ± 0.0144 | -0.0214 (59) |
| 25-40 | 601 | 0.2482 | 0.1962 | +0.0520 ± 0.0111 | 0.7008 | 0.5704 | 0.6502 | 0.3382 | 0.4093 | -0.082 ± 0.0168 | -0.0219 (26) |
| 40+ | 198 | 0.3755 | 0.1901 | +0.1854 ± 0.0316 | 1.081 | 0.5609 | 0.7922 | 0.3012 | 0.3788 | -0.081 ± 0.0284 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2506 | 0.1872 | 0.1873 | -0.0000 ± 0.0003 | 0.5503 | 0.5494 | 0.5042 | 0.489 | 0.4988 | -0.035 ± 0.0086 | -0.0157 (88) |
| 3-5 | 1721 | 0.1907 | 0.1883 | +0.0024 ± 0.0008 | 0.5573 | 0.5516 | 0.486 | 0.4463 | 0.4364 | -0.056 ± 0.0105 | -0.0209 (69) |
| 5-10 | 3464 | 0.1947 | 0.1867 | +0.0080 ± 0.0011 | 0.5748 | 0.552 | 0.4838 | 0.4102 | 0.3952 | -0.066 ± 0.0074 | -0.0082 (132) |
| 10-15 | 2344 | 0.2042 | 0.1895 | +0.0147 ± 0.0022 | 0.5963 | 0.5574 | 0.5102 | 0.3873 | 0.3891 | -0.056 ± 0.009 | -0.0053 (105) |
| 15-25 | 2910 | 0.2295 | 0.1979 | +0.0315 ± 0.0032 | 0.6616 | 0.5756 | 0.5576 | 0.3623 | 0.3808 | -0.060 ± 0.0083 | -0.0253 (107) |
| 25-40 | 1983 | 0.253 | 0.1696 | +0.0834 ± 0.0058 | 0.7166 | 0.5019 | 0.6103 | 0.2964 | 0.3232 | -0.076 ± 0.0089 | -0.0229 (51) |
| 40+ | 937 | 0.3871 | 0.1293 | +0.2578 ± 0.0125 | 1.0953 | 0.3965 | 0.7085 | 0.2023 | 0.2134 | -0.072 ± 0.0112 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3220 | 1.048 ± 0.05 | 1.165 | 0.1678 | 0.1701 | 0.2129 | 0.2022 |
| gen2 | 3220 | 0.845 ± 0.045 | 1.122 | 0.1746 | 0.1701 | 0.2316 | 0.2021 |
| gen1_elo | 3220 | 1.039 ± 0.048 | 1.151 | 0.1732 | 0.1705 | 0.2115 | 0.202 |
| gen1_sr | 3220 | 1.039 ± 0.058 | 1.182 | 0.1345 | 0.1718 | 0.2275 | 0.2019 |
| gen1_ledger | 5228 | 0.877 ± 0.034 | 1.078 | 0.1772 | 0.1846 | 0.2181 | 0.1977 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 15,677)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,756 | 24.0% |
| STALE_QUOTE | market_freshness | 3,218 | 20.5% |
| BOOK_QUALITY | execution | 3,033 | 19.4% |
| POOR_DATA | data | 1,717 | 10.9% |
| LIMITED_DATA | data | 1,089 | 7.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 827 | 5.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 761 | 4.9% |
| IDENTITY_AMBIGUOUS | mapping | 633 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 441 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 202 | 1.3% |

Cause class: coverage 24.0%, market_freshness 20.5%, execution 19.4%, data 17.9%, market_freshness/coverage 8.1%, model_calibration_or_unknown 4.9%, mapping 4.0%, model_calibration 1.3%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.7%, START_UNVERIFIABLE 95.0%, LOW_DATA_QUALITY 69.6%, THIN_PLAYER_HISTORY 57.8%, STALE_PLAYER_DATA 52.2%, STALE_KALSHI_QUOTE 44.1%, MODEL_INTERNAL_DISAGREEMENT 40.0%, ASYMMETRIC_SAMPLE_SIZE 32.1%, WIDE_SPREAD 25.3%, MODEL_HIGH_UNCERTAINTY 17.7%, PLAYER_IDENTITY_RISK 14.8%, LEVEL_TRANSFER_RISK 8.8%, EVENT_MAPPING_RISK 8.4%, LOW_DISPLAYED_LIQUIDITY 7.6%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 2.2%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 26.4%, POST_SETTLEMENT_OBSERVATION 24.0%, POSSIBLE_IN_PLAY_QUOTE 5.6%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 8,418)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,973 | 35.3% |
| BOOK_QUALITY | execution | 1,605 | 19.1% |
| STALE_QUOTE | market_freshness | 1,511 | 17.9% |
| POOR_DATA | data | 719 | 8.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 442 | 5.2% |
| IDENTITY_AMBIGUOUS | mapping | 364 | 4.3% |
| LIMITED_DATA | data | 327 | 3.9% |
| IN_PLAY_QUOTE | market_freshness/coverage | 273 | 3.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 161 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 43 | 0.5% |

Cause class: coverage 35.3%, execution 19.1%, market_freshness 17.9%, data 12.4%, market_freshness/coverage 8.5%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.8%, START_UNVERIFIABLE 97.7%, LOW_DATA_QUALITY 73.5%, THIN_PLAYER_HISTORY 60.3%, STALE_KALSHI_QUOTE 52.3%, STALE_PLAYER_DATA 47.6%, MODEL_INTERNAL_DISAGREEMENT 41.0%, ASYMMETRIC_SAMPLE_SIZE 33.9%, WIDE_SPREAD 25.2%, PLAYER_IDENTITY_RISK 18.0%, MODEL_HIGH_UNCERTAINTY 18.0%, EVENT_MAPPING_RISK 10.1%, LEVEL_TRANSFER_RISK 7.8%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 5.0%, EXTERNAL_MARKET_REJECTION 1.1%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 38.1%, POST_SETTLEMENT_OBSERVATION 35.3%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 6687, "IDENTITY_AMBIGUOUS": 1731}; ticker orientation: {"VERIFIED": 8418}.

Checks: discipline:AMBIGUOUS 614, discipline:PASS 7804, identity_confidence:AMBIGUOUS 1518, identity_confidence:PASS 6900, level_mapping:NA 626, level_mapping:PASS 7792, market_pair:AMBIGUOUS 298, market_pair:NA 208, market_pair:PASS 7912, model_complement:NA 175, model_complement:PASS 8243, namesake:PASS 8418, physical_match_id:NA 3214, physical_match_id:PASS 5204, player_ids:PASS 8418, same_pair_other_event:PASS 8418, ticker_orientation:PASS 8418

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,825 | 3.1% | 2.8% | 1.0% | {"market_freshness": 33, "data": 21, "execution": 13, "market_freshness/coverage": 8, "model_calibration_or_unknown": 6, "model_calibration": 4, "coverage": 2} | 5.62 | 0.2094 / 0.2065 (297) | 17.0% | 2.8% | 4.4% | 2.2% |
| CHALLENGER | 5,971 | 17.1% | 6.5% | 12.2% | {"coverage": 593, "market_freshness/coverage": 129, "market_freshness": 128, "data": 86, "model_calibration_or_unknown": 46, "execution": 24, "model_calibration": 9, "mapping": 8} | 7.19 | 0.218 / 0.2053 (1498) | 36.2% | 12.4% | 2.6% | 22.0% |
| DOUBLES | 1,253 | 49.0% | 48.6% | 7.3% | {"execution": 290, "mapping": 168, "market_freshness": 106, "market_freshness/coverage": 43, "coverage": 7} | 24.07 | 0.3221 / 0.2339 (335) | 18.7% | 0.0% | 100.0% | 7.3% |
| ITF_MEN | 10,841 | 24.4% | 16.7% | 31.5% | {"coverage": 1041, "execution": 537, "market_freshness": 407, "data": 357, "market_freshness/coverage": 210, "mapping": 95, "model_calibration_or_unknown": 2} | 11.13 | 0.2133 / 0.1942 (2630) | 36.3% | 61.7% | 13.1% | 22.7% |
| ITF_WOMEN | 13,945 | 26.9% | 19.9% | 44.5% | {"coverage": 1313, "market_freshness": 761, "execution": 712, "data": 548, "market_freshness/coverage": 276, "mapping": 87, "model_calibration_or_unknown": 43, "model_calibration": 10} | 12.78 | 0.2038 / 0.1915 (2805) | 38.6% | 57.4% | 10.2% | 21.9% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,104 | 5.2% | 4.7% | 1.3% | {"market_freshness": 36, "model_calibration_or_unknown": 23, "execution": 15, "data": 11, "market_freshness/coverage": 10, "model_calibration": 9, "coverage": 4, "mapping": 1} | 7.58 | 0.2378 / 0.2317 (359) | 23.1% | 1.6% | 1.7% | 3.0% |
| WTA125 | 1,390 | 12.5% | 9.9% | 2.1% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.2185 / 0.2069 (482) | 22.9% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 5 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 6 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 7 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 207 min (STALE); no external reference |
| 9 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 10 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 11 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 12 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 13 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 14 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 15 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 16 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 17 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 18 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 19 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 20 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 463 min (STALE); no external reference |
| 22 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 23 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 24 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 25 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 26 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 27 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 28 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 29 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 30 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 31 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 32 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 33 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 752 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 34 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 35 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 36 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 37 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 38 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 39 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 547 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 40 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 41 | `KXITFWMATCH-26OCT16ESTLAB-LAB` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 68 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1475.0, ratio 2.28); no external reference |
| 42 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 43 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 44 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 45 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 46 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 47 | `KXATPDOUBLES-26OCT18COLGOFPOLZIE-COLGOF` | DOUBLES | gen1_ledger | 90% / 15% | +75 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 49 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 50 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9767, "by_level_share_of_ge_25pp": {"ATP": 0.0103, "CHALLENGER": 0.1215, "DOUBLES": 0.0729, "ITF_MEN": 0.3147, "ITF_WOMEN": 0.4455, "OTHER": 0.0014, "WTA": 0.0129, "WTA125": 0.0207}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.523, "share_primary_cause_market_settled_or_in_play": 0.4381, "share_primary_cause_stale_quote_only": 0.1795}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 8418, "identity_ambiguous_share": 0.2056, "ticker_orientation": {"VERIFIED": 8418}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 5204, "with_external": 210, "coverage": 0.0404, "external_status": {"EXTERNAL_STALE": 141, "AGREES_WITH_KALSHI": 66, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 141, "MODEL_LONE_OUTLIER": 66, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3143, "share_external_supports_model": 0.0143}, "pregame_clean_ge_25pp": {"n": 2508, "with_external": 198, "coverage": 0.0789, "external_status": {"EXTERNAL_STALE": 131, "AGREES_WITH_KALSHI": 64, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 131, "MODEL_LONE_OUTLIER": 64, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3232, "share_external_supports_model": 0.0152}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 545.0, "median_sample_ratio": 2.43, "median_min_matches": 21.0, "median_max_days_since_last": 211.0, "share_severe_asymmetry": 0.2056, "data_status": {"POOR": 4511, "LIMITED": 2407, "ADEQUATE": 1500}, "comparison_lt_10pp": {"median_thinner_serve_points": 1841.0, "median_sample_ratio": 1.67, "median_min_matches": 94.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 647, "model_minus_observed": 0.0549, "kalshi_minus_observed": -0.0784, "brier_diff_model_minus_kalshi": 0.0015}, "4-10x": {"n": 433, "model_minus_observed": 0.081, "kalshi_minus_observed": -0.057, "brier_diff_model_minus_kalshi": 0.0094}, "<2x": {"n": 1613, "model_minus_observed": 0.0877, "kalshi_minus_observed": -0.034, "brier_diff_model_minus_kalshi": 0.0129}, ">=10x": {"n": 527, "model_minus_observed": 0.1249, "kalshi_minus_observed": -0.0431, "brier_diff_model_minus_kalshi": 0.0163}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3220, "model": {"intercept": -0.556, "slope": 0.845, "slope_se": 0.045}, "kalshi_mid_same_rows": {"intercept": 0.208, "slope": 1.122, "slope_se": 0.051}, "mean_extremity_model": 0.1746, "mean_extremity_kalshi": 0.1701, "model_brier": 0.2316, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": 0.0295, "brier_diff_se": 0.0033, "model_logloss": 0.6599, "kalshi_logloss": 0.5864}, "fair_v1": {"n": 3220, "model": {"intercept": -0.417, "slope": 1.048, "slope_se": 0.05}, "kalshi_mid_same_rows": {"intercept": 0.29, "slope": 1.165, "slope_se": 0.052}, "mean_extremity_model": 0.1678, "mean_extremity_kalshi": 0.1701, "model_brier": 0.2129, "kalshi_brier": 0.2022, "brier_diff_model_minus_kalshi": 0.0107, "brier_diff_se": 0.0027, "model_logloss": 0.6136, "kalshi_logloss": 0.5864}, "gen1_elo": {"n": 3220, "model": {"intercept": -0.411, "slope": 1.039, "slope_se": 0.048}, "kalshi_mid_same_rows": {"intercept": 0.282, "slope": 1.151, "slope_se": 0.051}, "mean_extremity_model": 0.1732, "mean_extremity_kalshi": 0.1705, "model_brier": 0.2115, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0095, "brier_diff_se": 0.0027, "model_logloss": 0.6113, "kalshi_logloss": 0.586}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2438, "share_ge_15": 0.4358, "median_abs_gap": 12.96, "n": 21345}, "gen1_elo": {"share_ge_25": 0.2376, "share_ge_15": 0.4314, "median_abs_gap": 12.52, "n": 21345}, "gen1_sr": {"share_ge_25": 0.3051, "share_ge_15": 0.5207, "median_abs_gap": 15.76, "n": 21345}, "gen2": {"share_ge_25": 0.3082, "share_ge_15": 0.5077, "median_abs_gap": 15.38, "n": 21345}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1513, "share_ge_15": 0.349, "median_abs_gap": 10.7, "n": 16571}, "gen1_elo": {"share_ge_25": 0.1489, "share_ge_15": 0.3411, "median_abs_gap": 10.18, "n": 16570}, "gen1_sr": {"share_ge_25": 0.2127, "share_ge_15": 0.4434, "median_abs_gap": 13.15, "n": 16571}, "gen2": {"share_ge_25": 0.2281, "share_ge_15": 0.4407, "median_abs_gap": 13.02, "n": 16572}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.62, "share_ge_25_all": 0.0308, "share_ge_25_pregame_clean": 0.0279}, "WTA": {"median_abs_gap_pregame_clean": 7.58, "share_ge_25_all": 0.0518, "share_ge_25_pregame_clean": 0.0465}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2399, "share_within_10pp_all": 0.4388, "share_within_10pp_pregame_clean": 0.4939, "corr_model_vs_mid_pregame_clean": 0.8419}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 497, "model_brier": 0.1929, "kalshi_brier": 0.1943, "brier_diff_model_minus_kalshi": -0.0013}, "10-15": {"n_settled": 570, "model_brier": 0.2148, "kalshi_brier": 0.2055, "brier_diff_model_minus_kalshi": 0.0093}, "15-25": {"n_settled": 702, "model_brier": 0.2296, "kalshi_brier": 0.2129, "brier_diff_model_minus_kalshi": 0.0168}, "25-40": {"n_settled": 381, "model_brier": 0.2251, "kalshi_brier": 0.2074, "brier_diff_model_minus_kalshi": 0.0177}, "3-5": {"n_settled": 313, "model_brier": 0.195, "kalshi_brier": 0.1945, "brier_diff_model_minus_kalshi": 0.0005}, "40+": {"n_settled": 79, "model_brier": 0.3062, "kalshi_brier": 0.1714, "brier_diff_model_minus_kalshi": 0.1348}, "5-10": {"n_settled": 678, "model_brier": 0.1989, "kalshi_brier": 0.1982, "brier_diff_model_minus_kalshi": 0.0008}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.556, "slope": 0.845, "slope_se": 0.045}, "kalshi_slope": {"intercept": 0.208, "slope": 1.122, "slope_se": 0.051}, "n": 3220}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.519, "slope": 0.877, "slope_se": 0.034}, "kalshi_slope": {"intercept": 0.138, "slope": 1.078, "slope_se": 0.038}, "n": 5228}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 335, "model_brier": 0.3221, "kalshi_brier": 0.2339, "brier_diff_model_minus_kalshi": 0.0882, "brier_diff_se": 0.0171, "corr_model_outcome": 0.0175, "corr_kalshi_outcome": 0.2597}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
