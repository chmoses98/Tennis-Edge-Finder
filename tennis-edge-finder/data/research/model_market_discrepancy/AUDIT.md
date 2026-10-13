# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-13T23:23Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 31,227): 0-3 14.5%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 18.6%, 25-40 13.5%, 40+ 8.2%; median gap 11.73 pp.
* **Where the extremes live**: 98.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.0%, Challenger 12.7%, doubles 7.0%). Main tour: ATP 1.4% and WTA 6.2% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 6,784): MARKET_ALREADY_SETTLED_WHEN_PRICED 38.4%, BOOK_QUALITY 17.8%, STALE_QUOTE 16.4%, POOR_DATA 8.1%, POSSIBLY_IN_PLAY_QUOTE 5.6%, LIMITED_DATA 4.2%, IDENTITY_AMBIGUOUS 3.9%, IN_PLAY_QUOTE 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.4%. By class: coverage 38.4%, execution 17.8%, market_freshness 16.4%, data 12.2%, market_freshness/coverage 8.9%, mapping 3.9%, model_calibration_or_unknown 2.0%, model_calibration 0.4%.
* **Stale / settled / in-play**: 53.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 47.3% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 6,784 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 18.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 3.1%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 22.0% of the time and with the model 0.6%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 600.0 points vs 1886.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.071, Gen-2 0.873, Gen-1 ledger 0.881 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 311 model 0.2235 vs Kalshi 0.2079; n 68 model 0.2909 vs Kalshi 0.1768.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 124,434 model-market comparisons (205,164 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 45,562 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-13T23:13:56.731397+00:00'], shadow board 33,369 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-13T23:14:01.964194+00:00'], Model 4 13,830 rows, 13,795 settled tickers, 4,134 tickers with an external scan.
* By model: {"gen1_ledger": 29997, "gen1_elo": 16772, "fair_v1": 16772, "gen2": 16772, "gen1_sr": 16772, "model4_fundamental": 13679, "model4_conditioned": 13670}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 31,227 | 14.5 | 9.6 | 20.2 | 15.3 | 18.6 | 13.5 | 8.2 | 11.73 | 40.4% | 21.7% |
| MW fair_v1 | 16,772 | 13.7 | 8.6 | 18.7 | 15.9 | 18.8 | 14.4 | 9.8 | 12.79 | 43.1% | 24.3% |
| MW gen1_elo | 16,772 | 13.3 | 9.0 | 20.2 | 15.0 | 18.7 | 14.4 | 9.4 | 12.26 | 42.5% | 23.8% |
| MW gen1_ledger | 14,455 | 15.4 | 10.7 | 22.0 | 14.7 | 18.5 | 12.4 | 6.3 | 10.46 | 37.2% | 18.7% |
| MW gen1_sr | 16,772 | 10.0 | 7.8 | 16.5 | 14.3 | 21.6 | 18.1 | 11.7 | 15.51 | 51.4% | 29.8% |
| MW gen2 | 16,772 | 11.8 | 7.3 | 16.4 | 14.2 | 20.2 | 17.0 | 13.1 | 15.18 | 50.3% | 30.2% |
| all families model4_conditioned | 13,670 | 21.7 | 20.1 | 35.5 | 16.3 | 4.3 | 1.1 | 0.9 | 5.8 | 6.3% | 2.0% |
| all families model4_fundamental | 13,679 | 16.6 | 13.3 | 35.8 | 19.8 | 10.6 | 2.6 | 1.1 | 7.62 | 14.4% | 3.8% |

Configurable thresholds (primary): >=5pp 75.9%, >=10pp 55.7%, >=15pp 40.4%, >=20pp 30.0%, >=25pp 21.7%, >=30pp 15.9%, >=40pp 8.2%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.34pp; >=10pp 44.9%, >=25pp 17.4%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,307 | 30.1 | 14.7 | 24.9 | 17.8 | 10.5 | 1.1 | 0.8 | 5.84 | 12.5% | 2.0% |
| CHALLENGER | 2,989 | 15.4 | 10.1 | 20.0 | 15.8 | 14.7 | 12.0 | 11.9 | 11.62 | 38.6% | 23.9% |
| ITF_MEN | 4,644 | 11.3 | 8.5 | 18.1 | 14.8 | 19.4 | 15.5 | 12.4 | 13.99 | 47.3% | 27.9% |
| ITF_WOMEN | 6,415 | 10.2 | 6.5 | 16.0 | 16.1 | 21.8 | 18.7 | 10.7 | 15.49 | 51.2% | 29.5% |
| WTA | 877 | 21.7 | 10.9 | 25.1 | 15.8 | 19.6 | 5.6 | 1.2 | 8.03 | 26.5% | 6.8% |
| WTA125 | 540 | 13.3 | 8.0 | 23.1 | 20.0 | 19.4 | 14.1 | 2.0 | 11.08 | 35.6% | 16.1% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,307 | 23.9 | 14.6 | 24.6 | 19.2 | 14.7 | 1.9 | 1.0 | 6.9 | 17.6% | 2.9% |
| CHALLENGER | 2,989 | 15.1 | 7.5 | 19.3 | 13.3 | 18.2 | 14.0 | 12.6 | 12.84 | 44.8% | 26.5% |
| ITF_MEN | 4,644 | 10.0 | 7.3 | 16.4 | 14.2 | 19.8 | 18.2 | 14.1 | 15.75 | 52.1% | 32.3% |
| ITF_WOMEN | 6,415 | 8.7 | 5.8 | 12.9 | 12.9 | 21.7 | 20.9 | 17.1 | 19.11 | 59.7% | 38.0% |
| WTA | 877 | 18.5 | 8.2 | 18.8 | 16.0 | 22.7 | 14.6 | 1.2 | 11.64 | 38.5% | 15.8% |
| WTA125 | 540 | 5.9 | 4.3 | 18.7 | 18.1 | 24.3 | 18.9 | 9.8 | 16.84 | 53.0% | 28.7% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,307 | 27.5 | 14.4 | 29.1 | 15.2 | 10.4 | 2.5 | 0.9 | 6.1 | 13.9% | 3.4% |
| CHALLENGER | 2,989 | 14.9 | 10.1 | 20.7 | 15.3 | 15.2 | 11.9 | 11.8 | 11.01 | 38.9% | 23.8% |
| ITF_MEN | 4,644 | 10.3 | 8.5 | 18.8 | 13.8 | 20.0 | 16.0 | 12.5 | 14.31 | 48.5% | 28.5% |
| ITF_WOMEN | 6,415 | 9.8 | 6.7 | 16.6 | 15.7 | 22.6 | 19.1 | 9.6 | 15.51 | 51.3% | 28.7% |
| WTA | 877 | 22.5 | 15.3 | 33.4 | 15.5 | 10.3 | 2.3 | 0.8 | 6.12 | 13.3% | 3.1% |
| WTA125 | 540 | 22.6 | 11.5 | 29.3 | 15.2 | 14.4 | 6.7 | 0.4 | 7.59 | 21.5% | 7.0% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 713 | 30.9 | 22.9 | 35.6 | 9.0 | 1.3 | 0.4 | 0.0 | 4.7 | 1.7% | 0.4% |
| CHALLENGER | 2,034 | 22.0 | 15.6 | 27.4 | 14.9 | 13.0 | 5.0 | 2.1 | 6.94 | 20.0% | 7.0% |
| DOUBLES | 949 | 4.3 | 3.5 | 11.7 | 11.2 | 19.1 | 24.6 | 25.7 | 25.37 | 69.3% | 50.3% |
| ITF_MEN | 4,354 | 14.7 | 8.5 | 21.1 | 15.4 | 20.6 | 12.4 | 7.3 | 11.8 | 40.4% | 19.7% |
| ITF_WOMEN | 4,960 | 11.7 | 9.3 | 19.5 | 14.7 | 22.5 | 16.6 | 5.8 | 13.07 | 44.9% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 648 | 21.4 | 15.1 | 27.3 | 17.1 | 13.6 | 4.9 | 0.5 | 7.61 | 19.0% | 5.4% |
| WTA125 | 648 | 19.9 | 14.0 | 22.1 | 18.5 | 14.7 | 8.5 | 2.3 | 8.32 | 25.5% | 10.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,293 | 30.1 | 14.6 | 25.1 | 17.9 | 10.4 | 1.1 | 0.8 | 5.84 | 12.4% | 1.9% |
| CHALLENGER | 2,143 | 19.9 | 12.6 | 25.1 | 18.8 | 15.1 | 6.0 | 2.5 | 8.36 | 23.6% | 8.5% |
| ITF_MEN | 3,309 | 14.2 | 10.7 | 21.6 | 16.5 | 19.5 | 12.3 | 5.3 | 11.01 | 37.1% | 17.6% |
| ITF_WOMEN | 4,618 | 12.5 | 8.1 | 18.6 | 18.6 | 23.3 | 15.1 | 3.8 | 12.78 | 42.2% | 18.9% |
| WTA | 864 | 21.8 | 10.4 | 25.5 | 16.0 | 19.7 | 5.4 | 1.3 | 8.09 | 26.4% | 6.7% |
| WTA125 | 517 | 13.7 | 7.7 | 22.6 | 20.3 | 20.1 | 13.9 | 1.6 | 11.2 | 35.6% | 15.5% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,293 | 23.8 | 14.7 | 24.8 | 19.2 | 14.7 | 1.9 | 1.0 | 6.9 | 17.6% | 2.9% |
| CHALLENGER | 2,143 | 19.4 | 9.5 | 24.2 | 16.1 | 18.5 | 9.7 | 2.6 | 9.13 | 30.8% | 12.3% |
| ITF_MEN | 3,310 | 12.0 | 8.8 | 18.9 | 16.0 | 21.6 | 15.6 | 7.1 | 12.97 | 44.3% | 22.7% |
| ITF_WOMEN | 4,618 | 10.1 | 6.8 | 14.6 | 14.1 | 24.3 | 19.7 | 10.3 | 16.61 | 54.4% | 30.0% |
| WTA | 864 | 18.3 | 8.0 | 19.0 | 16.2 | 22.7 | 14.6 | 1.3 | 11.72 | 38.5% | 15.9% |
| WTA125 | 517 | 5.8 | 4.5 | 18.8 | 18.6 | 24.0 | 19.5 | 8.9 | 16.74 | 52.4% | 28.4% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 693 | 30.9 | 23.1 | 35.9 | 9.1 | 0.6 | 0.4 | 0.0 | 4.69 | 1.0% | 0.4% |
| CHALLENGER | 1,755 | 23.9 | 17.1 | 29.5 | 14.6 | 12.1 | 2.2 | 0.6 | 6.33 | 14.9% | 2.8% |
| DOUBLES | 879 | 4.3 | 3.5 | 12.1 | 11.2 | 19.2 | 24.2 | 25.5 | 24.5 | 68.9% | 49.7% |
| ITF_MEN | 3,546 | 16.4 | 9.3 | 23.1 | 16.2 | 20.5 | 10.3 | 4.2 | 10.27 | 34.9% | 14.4% |
| ITF_WOMEN | 4,054 | 12.8 | 10.0 | 21.3 | 15.5 | 22.8 | 14.9 | 2.6 | 11.65 | 40.4% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 614 | 22.0 | 15.8 | 27.5 | 17.1 | 13.8 | 3.8 | 0.0 | 7.21 | 17.6% | 3.8% |
| WTA125 | 545 | 21.8 | 15.6 | 23.5 | 20.4 | 13.0 | 5.3 | 0.4 | 7.42 | 18.7% | 5.7% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 949 | 4.3 | 3.5 | 11.7 | 11.2 | 19.1 | 24.6 | 25.7 | 25.37 | 69.3% | 50.3% |
| singles | 13,506 | 16.2 | 11.2 | 22.7 | 14.9 | 18.4 | 11.6 | 4.9 | 9.95 | 35.0% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 3,898 | 13.3 | 9.1 | 20.2 | 15.8 | 17.3 | 14.1 | 10.1 | 12.4 | 41.5% | 24.2% |
| Grass | 130 | 11.5 | 15.4 | 16.9 | 11.5 | 22.3 | 16.1 | 6.2 | 13.04 | 44.6% | 22.3% |
| Hard | 11,064 | 14.2 | 8.4 | 18.7 | 15.7 | 19.1 | 14.2 | 9.7 | 12.71 | 43.0% | 23.9% |
| UNKNOWN | 1,680 | 11.6 | 7.8 | 15.7 | 17.7 | 19.7 | 16.6 | 10.8 | 14.09 | 47.1% | 27.4% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,134 | 19.9 | 10.8 | 21.1 | 16.9 | 15.5 | 8.7 | 7.2 | 9.47 | 31.3% | 15.9% |
| B | 2,248 | 14.4 | 9.2 | 20.0 | 17.0 | 17.5 | 12.2 | 9.7 | 11.47 | 39.5% | 21.9% |
| C | 2,438 | 13.1 | 9.6 | 19.5 | 14.7 | 19.2 | 14.6 | 9.3 | 12.69 | 43.1% | 23.9% |
| D | 2,942 | 10.8 | 8.3 | 18.0 | 15.9 | 22.3 | 15.0 | 9.8 | 13.94 | 47.0% | 24.8% |
| F | 4,010 | 7.9 | 5.1 | 15.0 | 14.7 | 20.9 | 22.7 | 13.6 | 18.3 | 57.2% | 36.3% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,238 | 22.5 | 16.0 | 28.8 | 15.2 | 11.5 | 4.4 | 1.6 | 6.73 | 17.6% | 6.1% |
| B | 2,225 | 15.1 | 10.0 | 24.0 | 16.3 | 19.2 | 11.2 | 4.3 | 10.18 | 34.6% | 15.5% |
| C | 2,863 | 12.1 | 7.7 | 18.2 | 14.4 | 20.4 | 15.7 | 11.6 | 13.71 | 47.6% | 27.3% |
| D | 2,215 | 14.1 | 9.8 | 20.9 | 13.4 | 21.6 | 13.9 | 6.4 | 11.85 | 41.8% | 20.2% |
| F | 2,914 | 9.6 | 7.5 | 15.2 | 13.8 | 23.9 | 20.7 | 9.4 | 16.61 | 54.0% | 30.1% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 5,693 | 18.2 | 9.8 | 20.3 | 16.9 | 15.7 | 9.7 | 9.5 | 10.46 | 34.8% | 19.1% |
| LIMITED | 4,062 | 15.3 | 10.4 | 20.7 | 15.7 | 18.4 | 12.8 | 6.8 | 11.08 | 37.9% | 19.5% |
| POOR | 7,017 | 9.1 | 6.6 | 16.3 | 15.3 | 21.5 | 19.3 | 11.9 | 16.04 | 52.7% | 31.2% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,954 | 31.4 | 24.2 | 36.4 | 5.5 | 1.8 | 0.7 | 0.1 | 4.51 | 2.5% | 0.7% |
| GAME_SPREAD | 2,850 | 25.8 | 15.9 | 36.8 | 16.7 | 4.2 | 0.4 | 0.2 | 6.0 | 4.8% | 0.6% |
| MATCH_WINNER | 14,455 | 15.4 | 10.7 | 22.0 | 14.7 | 18.5 | 12.4 | 6.3 | 10.46 | 37.2% | 18.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 5,417 | 33.2 | 19.4 | 31.1 | 9.7 | 5.2 | 1.2 | 0.2 | 4.76 | 6.6% | 1.4% |
| TOTAL_GAMES | 4,297 | 6.7 | 9.1 | 39.2 | 29.6 | 10.4 | 2.7 | 2.4 | 9.45 | 15.5% | 5.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,829 | 25.6 | 38.0 | 31.6 | 0.3 | 3.9 | 0.4 | 0.1 | 4.31 | 4.5% | 0.6% |
| GAME_SPREAD | 3,443 | 45.0 | 16.4 | 29.0 | 7.3 | 1.1 | 0.7 | 0.4 | 3.59 | 2.2% | 1.1% |
| TOTAL_GAMES | 5,398 | 3.4 | 6.5 | 43.3 | 36.4 | 6.6 | 1.9 | 2.0 | 9.73 | 10.5% | 3.9% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,829 | 26.2 | 18.5 | 37.2 | 9.3 | 6.3 | 2.1 | 0.3 | 5.52 | 8.8% | 2.4% |
| GAME_SPREAD | 3,443 | 19.1 | 13.3 | 30.3 | 21.2 | 13.1 | 2.4 | 0.7 | 7.84 | 16.1% | 3.0% |
| TOTAL_GAMES | 5,407 | 6.6 | 8.8 | 38.1 | 28.3 | 12.9 | 3.3 | 2.1 | 9.67 | 18.3% | 5.4% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 16,772 | 43.1% | 24.3% | 12.79 | 33.4% | 14.1% | 10.31 |
| gen1_elo | 16,772 | 42.5% | 23.8% | 12.26 | 32.4% | 13.9% | 9.71 |
| gen1_sr | 16,772 | 51.4% | 29.8% | 15.51 | 42.7% | 19.6% | 12.7 |
| gen2 | 16,772 | 50.3% | 30.2% | 15.18 | 42.9% | 21.3% | 12.64 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 8,986 | 16.6 | 10.7 | 21.7 | 17.4 | 19.1 | 11.2 | 3.3 | 10.27 | 33.5% | 14.4% |
| STALE | 7,786 | 10.3 | 6.2 | 15.2 | 14.2 | 18.4 | 18.2 | 17.4 | 17.16 | 54.1% | 35.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 7,923 | 17.3 | 11.7 | 23.9 | 14.6 | 16.8 | 11.0 | 4.7 | 9.32 | 32.6% | 15.7% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 31,227 | 7923 | 12458 | 10846 | 24.1 | 151.4 | 1400.4 |
| ge_15pp | 12,604 | 2581 | 4300 | 5723 | 26.9 | 454.4 | 1380.4 |
| ge_25pp | 6,784 | 1247 | 1889 | 3648 | 34.5 | 582.0 | 1380.4 |
| lt_10pp | 13,833 | 4186 | 6042 | 3605 | 22.6 | 48.8 | 1341.5 |

Current slate `SL-20261013T232350Z-0117cb6f`: 610 priced rows, quote age at build {'median': 10.2, 'max': 10.3}, freshness {'AGING': 610}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 8 | 0.0 | 0.0 | 37.5 | 0.0 | 37.5 | 25.0 | 0.0 | 20.45 | 62.5% | 25.0% |
| EXTERNAL_LONE_OUTLIER | 9 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.3 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,232 | 22.1 | 11.0 | 22.8 | 18.7 | 18.4 | 6.6 | 0.5 | 8.59 | 25.5% | 7.1% |
| KALSHI_LONE_OUTLIER | 5 | 20.0 | 0.0 | 60.0 | 0.0 | 20.0 | 0.0 | 0.0 | 5.14 | 20.0% | 0.0% |
| MARKETS_AGREE | 227 | 70.9 | 29.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.03 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 418 | 0.0 | 4.1 | 35.4 | 29.9 | 22.0 | 7.9 | 0.7 | 11.41 | 30.6% | 8.6% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 16,772 | 1899 (11.3%) | 22.0% | 0.6% | {"EXTERNAL_STALE": 1232, "AGREES_WITH_KALSHI": 418, "ALL_AGREE": 227, "EXTERNAL_OUTLIER": 9, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 5, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 7,224 | 448 (6.2%) | 28.6% | 1.3% | {"EXTERNAL_STALE": 314, "AGREES_WITH_KALSHI": 128, "SUPPORTS_MODEL_DIRECTION": 5, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp | 4,075 | 125 (3.1%) | 28.8% | 1.6% | {"EXTERNAL_STALE": 87, "AGREES_WITH_KALSHI": 36, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_ge_25pp_pregame_clean | 1,798 | 117 (6.5%) | 29.1% | 1.7% | {"EXTERNAL_STALE": 81, "AGREES_WITH_KALSHI": 34, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_lt_10pp | 6,878 | 1096 (15.9%) | 15.0% | 0.5% | {"EXTERNAL_STALE": 688, "ALL_AGREE": 227, "AGREES_WITH_KALSHI": 165, "EXTERNAL_OUTLIER": 9, "AGREES_WITH_MODEL": 4, "SUPPORTS_MODEL_DIRECTION": 2, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,318 | 11.6 | 8.2 | 19.7 | 14.9 | 21.3 | 14.2 | 10.0 | 13.28 | 45.6% | 24.3% |
| 4-10x | 2,231 | 11.9 | 8.7 | 19.3 | 15.4 | 19.6 | 15.8 | 9.2 | 13.12 | 44.7% | 25.1% |
| <2x | 8,944 | 15.7 | 9.2 | 18.9 | 17.0 | 17.3 | 12.6 | 9.2 | 11.79 | 39.2% | 21.9% |
| >=10x | 2,279 | 10.6 | 6.6 | 16.1 | 13.6 | 20.0 | 20.5 | 12.6 | 16.46 | 53.1% | 33.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 4,400 | 14.1 | 8.2 | 19.4 | 16.0 | 19.0 | 12.7 | 10.7 | 12.52 | 42.3% | 23.4% |
| 300-1000 | 3,893 | 11.9 | 8.7 | 17.4 | 16.1 | 21.2 | 15.7 | 9.0 | 13.67 | 46.0% | 24.8% |
| <300 | 4,564 | 8.6 | 6.1 | 15.9 | 14.5 | 20.8 | 21.1 | 13.1 | 17.12 | 54.9% | 34.1% |
| >=3000 | 3,915 | 21.1 | 11.8 | 22.6 | 17.4 | 13.8 | 7.5 | 6.0 | 8.5 | 27.2% | 13.4% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 557 | 0.5371 | 0.4054 | 0.4811 | +0.056 | -0.076 | 0.002 ± 0.0062 |
| ratio 4-10x | 371 | 0.5852 | 0.4447 | 0.5229 | +0.062 | -0.078 | 0.0039 ± 0.0082 |
| ratio <2x | 1323 | 0.538 | 0.4162 | 0.455 | +0.083 | -0.039 | 0.0107 ± 0.0039 |
| ratio >=10x | 407 | 0.5472 | 0.3797 | 0.4324 | +0.115 | -0.053 | 0.0124 ± 0.0088 |
| thinner_sample 1000-3000 | 750 | 0.5446 | 0.4191 | 0.4733 | +0.071 | -0.054 | 0.0041 ± 0.0053 |
| thinner_sample 300-1000 | 664 | 0.5608 | 0.4227 | 0.4819 | +0.079 | -0.059 | 0.0046 ± 0.006 |
| thinner_sample <300 | 781 | 0.5453 | 0.385 | 0.4558 | +0.089 | -0.071 | 0.0103 ± 0.0062 |
| thinner_sample >=3000 | 463 | 0.5272 | 0.4328 | 0.4514 | +0.076 | -0.019 | 0.0162 ± 0.0053 |
| data_status ADEQUATE | 759 | 0.5314 | 0.4275 | 0.4519 | +0.080 | -0.025 | 0.0096 ± 0.0045 |
| data_status LIMITED | 706 | 0.5531 | 0.4238 | 0.4887 | +0.065 | -0.065 | 0.0032 ± 0.0055 |
| data_status POOR | 1193 | 0.5507 | 0.3959 | 0.4627 | +0.088 | -0.067 | 0.0102 ± 0.0049 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 408 | 0.1934 | 0.1948 | -0.0014 ± 0.0008 | 0.5646 | 0.5676 | 0.4921 | 0.4771 | 0.5196 | -0.053 ± 0.0229 | -0.01 (3) |
| 3-5 | 271 | 0.1898 | 0.1905 | -0.0006 ± 0.0021 | 0.5596 | 0.5597 | 0.5069 | 0.4671 | 0.4908 | -0.070 ± 0.027 | 0.02 (1) |
| 5-10 | 554 | 0.1983 | 0.1997 | -0.0014 ± 0.0029 | 0.5813 | 0.5836 | 0.5128 | 0.4386 | 0.4765 | -0.081 ± 0.0198 | -0.0125 (4) |
| 10-15 | 474 | 0.2099 | 0.203 | +0.0069 ± 0.0052 | 0.6066 | 0.5866 | 0.5211 | 0.3975 | 0.4283 | -0.087 ± 0.0206 | -0.0633 (3) |
| 15-25 | 572 | 0.227 | 0.2143 | +0.0127 ± 0.0075 | 0.6484 | 0.6151 | 0.574 | 0.3792 | 0.4458 | -0.078 ± 0.0193 | -0.0133 (6) |
| 25-40 | 311 | 0.2235 | 0.2079 | +0.0156 ± 0.0155 | 0.6384 | 0.5962 | 0.6503 | 0.3404 | 0.4695 | -0.066 ± 0.0233 | -0.01 (1) |
| 40+ | 68 | 0.2909 | 0.1768 | +0.1141 ± 0.0454 | 0.7906 | 0.5286 | 0.7508 | 0.3033 | 0.3971 | -0.121 ± 0.0447 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1938 | 0.1771 | 0.1782 | -0.0011 ± 0.0003 | 0.5282 | 0.5293 | 0.4779 | 0.4629 | 0.4969 | -0.023 ± 0.0097 | -0.0188 (8) |
| 3-5 | 1225 | 0.1949 | 0.1933 | +0.0016 ± 0.001 | 0.5711 | 0.5629 | 0.4798 | 0.4402 | 0.4359 | -0.064 ± 0.0128 | 0.02 (1) |
| 5-10 | 2655 | 0.1931 | 0.1914 | +0.0017 ± 0.0013 | 0.5679 | 0.5619 | 0.4858 | 0.412 | 0.4339 | -0.045 ± 0.0086 | -0.0082 (17) |
| 10-15 | 2294 | 0.2009 | 0.1832 | +0.0177 ± 0.0022 | 0.5874 | 0.5382 | 0.4794 | 0.355 | 0.3461 | -0.074 ± 0.0089 | -0.0475 (4) |
| 15-25 | 2730 | 0.2055 | 0.1698 | +0.0357 ± 0.0031 | 0.6028 | 0.5024 | 0.4984 | 0.3025 | 0.3117 | -0.065 ± 0.0079 | -0.0048 (29) |
| 25-40 | 2180 | 0.2196 | 0.1244 | +0.0952 ± 0.0047 | 0.6324 | 0.3843 | 0.5292 | 0.2153 | 0.2239 | -0.063 ± 0.0073 | -0.01 (1) |
| 40+ | 1492 | 0.3719 | 0.0439 | +0.3280 ± 0.006 | 0.9695 | 0.1732 | 0.6242 | 0.1062 | 0.059 | -0.084 ± 0.005 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 313 | 0.1965 | 0.1968 | -0.0003 ± 0.0009 | 0.5746 | 0.5754 | 0.4988 | 0.4836 | 0.4984 | -0.090 ± 0.0265 | -0.01 (1) |
| 3-5 | 212 | 0.2136 | 0.2126 | +0.0010 ± 0.0026 | 0.6099 | 0.6091 | 0.5177 | 0.4777 | 0.4811 | -0.084 ± 0.0334 | 0.02 (1) |
| 5-10 | 485 | 0.1977 | 0.1974 | +0.0003 ± 0.0031 | 0.5774 | 0.5772 | 0.5543 | 0.4792 | 0.5134 | -0.071 ± 0.021 | -0.01 (4) |
| 10-15 | 437 | 0.2171 | 0.2056 | +0.0115 ± 0.0055 | 0.6209 | 0.5965 | 0.5757 | 0.4513 | 0.4714 | -0.106 ± 0.0226 | -0.05 (4) |
| 15-25 | 639 | 0.2244 | 0.2077 | +0.0167 ± 0.0071 | 0.6389 | 0.5979 | 0.5909 | 0.3935 | 0.4538 | -0.083 ± 0.0184 | -0.01 (5) |
| 25-40 | 417 | 0.27 | 0.197 | +0.0730 ± 0.0137 | 0.7558 | 0.5731 | 0.6668 | 0.3529 | 0.3957 | -0.131 ± 0.0215 | -0.025 (2) |
| 40+ | 155 | 0.3451 | 0.19 | +0.1551 ± 0.0338 | 0.9621 | 0.5558 | 0.7492 | 0.272 | 0.3613 | -0.056 ± 0.0333 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1672 | 0.1823 | 0.1827 | -0.0004 ± 0.0004 | 0.5402 | 0.5409 | 0.4952 | 0.4806 | 0.5042 | -0.033 ± 0.0108 | -0.0217 (6) |
| 3-5 | 1070 | 0.1957 | 0.195 | +0.0007 ± 0.0011 | 0.5669 | 0.5651 | 0.5164 | 0.4765 | 0.486 | -0.042 ± 0.0138 | 0.02 (1) |
| 5-10 | 2318 | 0.1897 | 0.1875 | +0.0023 ± 0.0013 | 0.5611 | 0.5527 | 0.5145 | 0.4407 | 0.4638 | -0.040 ± 0.0092 | -0.01 (5) |
| 10-15 | 2025 | 0.1972 | 0.1816 | +0.0156 ± 0.0024 | 0.5799 | 0.5328 | 0.5237 | 0.3993 | 0.402 | -0.068 ± 0.0096 | -0.02 (14) |
| 15-25 | 2921 | 0.215 | 0.1754 | +0.0396 ± 0.0031 | 0.6254 | 0.5184 | 0.5343 | 0.3379 | 0.3386 | -0.076 ± 0.0078 | -0.0026 (27) |
| 25-40 | 2525 | 0.2486 | 0.1368 | +0.1117 ± 0.0047 | 0.706 | 0.4175 | 0.5617 | 0.246 | 0.2289 | -0.088 ± 0.0074 | -0.015 (6) |
| 40+ | 1983 | 0.3998 | 0.0682 | +0.3316 ± 0.0067 | 1.0471 | 0.2374 | 0.666 | 0.1291 | 0.1024 | -0.068 ± 0.0057 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 404 | 0.1923 | 0.1951 | -0.0028 ± 0.0008 | 0.5632 | 0.5705 | 0.4921 | 0.477 | 0.5569 | +0.001 ± 0.0222 | -0.0133 (6) |
| 3-5 | 288 | 0.1878 | 0.186 | +0.0017 ± 0.002 | 0.5516 | 0.5476 | 0.4952 | 0.4559 | 0.4549 | -0.117 ± 0.0267 | -0.01 (1) |
| 5-10 | 596 | 0.2003 | 0.1983 | +0.0020 ± 0.0027 | 0.5871 | 0.5797 | 0.5065 | 0.4329 | 0.453 | -0.088 ± 0.0188 | -0.01 (4) |
| 10-15 | 450 | 0.2091 | 0.2108 | -0.0018 ± 0.0053 | 0.6059 | 0.6047 | 0.5385 | 0.4158 | 0.4867 | -0.061 ± 0.0214 | -0.044 (5) |
| 15-25 | 537 | 0.2304 | 0.2083 | +0.0221 ± 0.0077 | 0.6597 | 0.6006 | 0.5787 | 0.3853 | 0.4264 | -0.103 ± 0.0196 | -0.03 (1) |
| 25-40 | 322 | 0.2093 | 0.2147 | -0.0054 ± 0.0152 | 0.6067 | 0.6128 | 0.6568 | 0.3443 | 0.5062 | -0.039 ± 0.0226 | 0.0 (1) |
| 40+ | 61 | 0.3195 | 0.1777 | +0.1418 ± 0.0492 | 0.8584 | 0.5313 | 0.7574 | 0.3028 | 0.377 | -0.134 ± 0.0497 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1843 | 0.1853 | 0.1866 | -0.0013 ± 0.0004 | 0.5466 | 0.5492 | 0.4842 | 0.469 | 0.5062 | -0.017 ± 0.0101 | -0.0183 (23) |
| 3-5 | 1284 | 0.1869 | 0.1848 | +0.0021 ± 0.001 | 0.5507 | 0.5458 | 0.4772 | 0.4378 | 0.4315 | -0.071 ± 0.0124 | -0.0243 (7) |
| 5-10 | 2850 | 0.1927 | 0.1874 | +0.0052 ± 0.0012 | 0.5687 | 0.5516 | 0.482 | 0.4083 | 0.4084 | -0.062 ± 0.0082 | -0.01 (18) |
| 10-15 | 2155 | 0.1945 | 0.1806 | +0.0139 ± 0.0023 | 0.5732 | 0.5302 | 0.4938 | 0.3707 | 0.3759 | -0.064 ± 0.0091 | -0.03 (9) |
| 15-25 | 2802 | 0.208 | 0.1701 | +0.0379 ± 0.003 | 0.6106 | 0.5041 | 0.5021 | 0.3068 | 0.3098 | -0.069 ± 0.0078 | -0.03 (2) |
| 25-40 | 2158 | 0.214 | 0.1222 | +0.0918 ± 0.0047 | 0.6197 | 0.3773 | 0.5244 | 0.2078 | 0.2247 | -0.058 ± 0.0071 | 0.0 (1) |
| 40+ | 1422 | 0.386 | 0.0457 | +0.3403 ± 0.0064 | 1.009 | 0.1784 | 0.6323 | 0.1082 | 0.057 | -0.087 ± 0.0053 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 716 | 0.1996 | 0.2004 | -0.0008 ± 0.0006 | 0.5801 | 0.5819 | 0.5058 | 0.4908 | 0.5112 | -0.034 ± 0.0167 | -0.0226 (46) |
| 3-5 | 520 | 0.1971 | 0.1965 | +0.0006 ± 0.0016 | 0.5739 | 0.5707 | 0.4797 | 0.4399 | 0.45 | -0.047 ± 0.0196 | -0.0058 (33) |
| 5-10 | 1076 | 0.1918 | 0.1861 | +0.0057 ± 0.002 | 0.5675 | 0.5528 | 0.481 | 0.4076 | 0.4061 | -0.064 ± 0.0134 | -0.0049 (73) |
| 10-15 | 688 | 0.2045 | 0.195 | +0.0095 ± 0.0042 | 0.5971 | 0.5715 | 0.4965 | 0.3736 | 0.3953 | -0.046 ± 0.0168 | 0.0014 (64) |
| 15-25 | 918 | 0.2326 | 0.2121 | +0.0205 ± 0.0059 | 0.6636 | 0.6106 | 0.5584 | 0.3641 | 0.4096 | -0.051 ± 0.0152 | -0.0216 (58) |
| 25-40 | 525 | 0.2534 | 0.1923 | +0.0611 ± 0.0119 | 0.7143 | 0.5602 | 0.6446 | 0.3313 | 0.3886 | -0.087 ± 0.0178 | -0.0216 (25) |
| 40+ | 178 | 0.3628 | 0.1934 | +0.1693 ± 0.0336 | 1.0535 | 0.568 | 0.7956 | 0.3023 | 0.3989 | -0.070 ± 0.0301 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2175 | 0.1904 | 0.1907 | -0.0003 ± 0.0003 | 0.5562 | 0.5559 | 0.5045 | 0.4892 | 0.5034 | -0.031 ± 0.0093 | -0.0155 (82) |
| 3-5 | 1506 | 0.1894 | 0.1869 | +0.0025 ± 0.0009 | 0.5538 | 0.5477 | 0.4868 | 0.4472 | 0.4363 | -0.057 ± 0.0112 | -0.0148 (63) |
| 5-10 | 3073 | 0.1906 | 0.1827 | +0.0079 ± 0.0012 | 0.5647 | 0.5428 | 0.4764 | 0.4028 | 0.3895 | -0.066 ± 0.0078 | -0.0087 (125) |
| 10-15 | 2068 | 0.1997 | 0.1869 | +0.0128 ± 0.0024 | 0.5858 | 0.5516 | 0.5053 | 0.3823 | 0.3917 | -0.049 ± 0.0095 | -0.0053 (105) |
| 15-25 | 2600 | 0.2298 | 0.1987 | +0.0311 ± 0.0034 | 0.6633 | 0.5772 | 0.5526 | 0.3577 | 0.3769 | -0.059 ± 0.0088 | -0.0255 (106) |
| 25-40 | 1761 | 0.2537 | 0.1674 | +0.0864 ± 0.0062 | 0.7204 | 0.495 | 0.6052 | 0.2903 | 0.3129 | -0.077 ± 0.0095 | -0.0206 (47) |
| 40+ | 861 | 0.3855 | 0.1269 | +0.2587 ± 0.0131 | 1.0958 | 0.3898 | 0.7094 | 0.2002 | 0.2137 | -0.072 ± 0.0115 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2658 | 1.071 ± 0.055 | 1.185 | 0.1689 | 0.1697 | 0.2103 | 0.2021 |
| gen2 | 2658 | 0.873 ± 0.049 | 1.126 | 0.1804 | 0.1696 | 0.2284 | 0.2019 |
| gen1_elo | 2658 | 1.049 ± 0.053 | 1.179 | 0.1732 | 0.1701 | 0.2091 | 0.2021 |
| gen1_sr | 2658 | 1.073 ± 0.063 | 1.202 | 0.1393 | 0.1715 | 0.2243 | 0.2017 |
| gen1_ledger | 4621 | 0.881 ± 0.037 | 1.091 | 0.1755 | 0.1864 | 0.2172 | 0.197 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 12,604)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,303 | 26.2% |
| STALE_QUOTE | market_freshness | 2,471 | 19.6% |
| BOOK_QUALITY | execution | 2,312 | 18.3% |
| POOR_DATA | data | 1,339 | 10.6% |
| LIMITED_DATA | data | 960 | 7.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 697 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 611 | 4.9% |
| IDENTITY_AMBIGUOUS | mapping | 430 | 3.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 365 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 116 | 0.9% |

Cause class: coverage 26.2%, market_freshness 19.6%, execution 18.3%, data 18.2%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.9%, mapping 3.4%, model_calibration 0.9%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.4%, START_UNVERIFIABLE 95.8%, LOW_DATA_QUALITY 68.2%, THIN_PLAYER_HISTORY 56.8%, STALE_PLAYER_DATA 55.5%, STALE_KALSHI_QUOTE 45.4%, MODEL_INTERNAL_DISAGREEMENT 38.3%, ASYMMETRIC_SAMPLE_SIZE 30.8%, WIDE_SPREAD 24.1%, MODEL_HIGH_UNCERTAINTY 16.5%, PLAYER_IDENTITY_RISK 12.6%, LEVEL_TRANSFER_RISK 8.8%, EVENT_MAPPING_RISK 7.8%, LOW_DISPLAYED_LIQUIDITY 7.4%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 1.5%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 28.6%, POST_SETTLEMENT_OBSERVATION 26.2%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### >= ge_25 pp (N = 6,784)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,605 | 38.4% |
| BOOK_QUALITY | execution | 1,204 | 17.8% |
| STALE_QUOTE | market_freshness | 1,113 | 16.4% |
| POOR_DATA | data | 548 | 8.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 378 | 5.6% |
| LIMITED_DATA | data | 283 | 4.2% |
| IDENTITY_AMBIGUOUS | mapping | 267 | 3.9% |
| IN_PLAY_QUOTE | market_freshness/coverage | 226 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 135 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 25 | 0.4% |

Cause class: coverage 38.4%, execution 17.8%, market_freshness 16.4%, data 12.2%, market_freshness/coverage 8.9%, mapping 3.9%, model_calibration_or_unknown 2.0%, model_calibration 0.4%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.2%, START_UNVERIFIABLE 98.2%, LOW_DATA_QUALITY 71.9%, THIN_PLAYER_HISTORY 59.1%, STALE_KALSHI_QUOTE 53.8%, STALE_PLAYER_DATA 50.1%, MODEL_INTERNAL_DISAGREEMENT 39.5%, ASYMMETRIC_SAMPLE_SIZE 32.8%, WIDE_SPREAD 23.8%, MODEL_HIGH_UNCERTAINTY 17.4%, PLAYER_IDENTITY_RISK 16.1%, EVENT_MAPPING_RISK 9.6%, LEVEL_TRANSFER_RISK 7.7%, LOW_DISPLAYED_LIQUIDITY 7.6%, MODEL_CALIBRATION_OUTLIER 4.6%, EXTERNAL_MARKET_REJECTION 0.8%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 41.2%, POST_SETTLEMENT_OBSERVATION 38.4%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 5523, "IDENTITY_AMBIGUOUS": 1261}; ticker orientation: {"VERIFIED": 6784}.

Checks: discipline:AMBIGUOUS 477, discipline:PASS 6307, identity_confidence:AMBIGUOUS 1093, identity_confidence:PASS 5691, level_mapping:NA 489, level_mapping:PASS 6295, market_pair:AMBIGUOUS 233, market_pair:NA 169, market_pair:PASS 6382, model_complement:NA 136, model_complement:PASS 6648, namesake:PASS 6784, physical_match_id:NA 2709, physical_match_id:PASS 4075, player_ids:PASS 6784, same_pair_other_event:PASS 6784, ticker_orientation:PASS 6784

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,020 | 1.4% | 1.4% | 0.4% | {"market_freshness": 20, "execution": 8, "market_freshness/coverage": 1} | 5.27 | 0.2124 / 0.2138 (243) | 16.4% | 0.5% | 5.5% | 1.7% |
| CHALLENGER | 5,023 | 17.1% | 5.9% | 12.7% | {"coverage": 522, "market_freshness": 109, "market_freshness/coverage": 104, "data": 56, "model_calibration_or_unknown": 45, "execution": 12, "mapping": 6, "model_calibration": 4} | 7.24 | 0.2178 / 0.2034 (1290) | 38.3% | 8.6% | 2.5% | 22.4% |
| DOUBLES | 949 | 50.3% | 49.7% | 7.0% | {"execution": 187, "mapping": 144, "market_freshness": 106, "market_freshness/coverage": 33, "coverage": 7} | 24.5 | 0.3357 / 0.2324 (268) | 24.7% | 0.0% | 100.0% | 7.4% |
| ITF_MEN | 8,998 | 23.9% | 15.9% | 31.8% | {"coverage": 876, "execution": 462, "market_freshness": 300, "data": 289, "market_freshness/coverage": 187, "mapping": 39, "model_calibration_or_unknown": 2} | 10.63 | 0.2099 / 0.1939 (2270) | 36.5% | 56.2% | 8.6% | 23.8% |
| ITF_WOMEN | 11,375 | 26.4% | 18.3% | 44.2% | {"coverage": 1183, "execution": 515, "market_freshness": 507, "data": 452, "market_freshness/coverage": 234, "mapping": 72, "model_calibration_or_unknown": 28, "model_calibration": 10} | 12.33 | 0.2033 / 0.1923 (2501) | 38.2% | 58.0% | 9.8% | 23.8% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,525 | 6.2% | 5.5% | 1.4% | {"market_freshness": 36, "model_calibration_or_unknown": 22, "data": 11, "market_freshness/coverage": 10, "execution": 6, "model_calibration": 5, "coverage": 4, "mapping": 1} | 7.77 | 0.2329 / 0.2248 (251) | 26.4% | 1.4% | 1.8% | 3.1% |
| WTA125 | 1,188 | 13.2% | 10.4% | 2.3% | {"model_calibration_or_unknown": 36, "market_freshness/coverage": 34, "market_freshness": 33, "data": 23, "coverage": 12, "execution": 9, "model_calibration": 6, "mapping": 4} | 9.32 | 0.2188 / 0.2098 (414) | 23.2% | 8.6% | 4.1% | 10.6% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 5 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 6 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 7 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 8 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 9 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 10 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 11 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 12 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 13 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 14 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 15 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 16 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 17 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 18 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 19 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 20 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 21 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 22 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 23 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 24 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 25 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 26 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 27 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 874 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 28 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 29 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 30 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 31 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 547 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 32 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 33 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 34 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 35 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 36 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 37 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 38 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 39 | `KXATPCHALLENGERMATCH-26OCT13GIUSEA-SEA` | CHALLENGER | fair_v1 | 76% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 243 min (STALE); no external reference |
| 40 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 760 min (STALE); no external reference |
| 41 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 42 | `KXITFWMATCH-26OCT13MAMSTR-MAM` | ITF_WOMEN | fair_v1 | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 406 min (STALE); data LIMITED (grade C, thinner serve sample 879.0, ratio 2.64); no external reference |
| 43 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 44 | `KXITFMATCH-26OCT13VISMUE-MUE` | ITF_MEN | fair_v1 | 25% / 98% | -74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 103 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 0.0); no external reference |
| 45 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 46 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 47 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 48 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 799 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 49 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 50 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9818, "by_level_share_of_ge_25pp": {"ATP": 0.0043, "CHALLENGER": 0.1265, "DOUBLES": 0.0703, "ITF_MEN": 0.3177, "ITF_WOMEN": 0.4424, "OTHER": 0.0018, "WTA": 0.014, "WTA125": 0.0231}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5377, "share_primary_cause_market_settled_or_in_play": 0.473, "share_primary_cause_stale_quote_only": 0.1641}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 6784, "identity_ambiguous_share": 0.1859, "ticker_orientation": {"VERIFIED": 6784}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 4075, "with_external": 125, "coverage": 0.0307, "external_status": {"EXTERNAL_STALE": 87, "AGREES_WITH_KALSHI": 36, "SUPPORTS_MODEL_DIRECTION": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 87, "MODEL_LONE_OUTLIER": 36, "ALL_THREE_DISAGREE": 2}, "share_external_agrees_with_kalshi": 0.288, "share_external_supports_model": 0.016}, "pregame_clean_ge_25pp": {"n": 1798, "with_external": 117, "coverage": 0.0651, "external_status": {"EXTERNAL_STALE": 81, "AGREES_WITH_KALSHI": 34, "SUPPORTS_MODEL_DIRECTION": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 81, "MODEL_LONE_OUTLIER": 34, "ALL_THREE_DISAGREE": 2}, "share_external_agrees_with_kalshi": 0.2906, "share_external_supports_model": 0.0171}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 600.0, "median_sample_ratio": 2.34, "median_min_matches": 20.0, "median_max_days_since_last": 199.0, "share_severe_asymmetry": 0.1893, "data_status": {"POOR": 3533, "LIMITED": 1998, "ADEQUATE": 1253}, "comparison_lt_10pp": {"median_thinner_serve_points": 1886.0, "median_sample_ratio": 1.67, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 557, "model_minus_observed": 0.056, "kalshi_minus_observed": -0.0757, "brier_diff_model_minus_kalshi": 0.002}, "4-10x": {"n": 371, "model_minus_observed": 0.0623, "kalshi_minus_observed": -0.0782, "brier_diff_model_minus_kalshi": 0.0039}, "<2x": {"n": 1323, "model_minus_observed": 0.083, "kalshi_minus_observed": -0.0388, "brier_diff_model_minus_kalshi": 0.0107}, ">=10x": {"n": 407, "model_minus_observed": 0.1148, "kalshi_minus_observed": -0.0528, "brier_diff_model_minus_kalshi": 0.0124}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2658, "model": {"intercept": -0.553, "slope": 0.873, "slope_se": 0.049}, "kalshi_mid_same_rows": {"intercept": 0.221, "slope": 1.126, "slope_se": 0.056}, "mean_extremity_model": 0.1804, "mean_extremity_kalshi": 0.1696, "model_brier": 0.2284, "kalshi_brier": 0.2019, "brier_diff_model_minus_kalshi": 0.0265, "brier_diff_se": 0.0036, "model_logloss": 0.652, "kalshi_logloss": 0.5858}, "fair_v1": {"n": 2658, "model": {"intercept": -0.39, "slope": 1.071, "slope_se": 0.055}, "kalshi_mid_same_rows": {"intercept": 0.332, "slope": 1.185, "slope_se": 0.058}, "mean_extremity_model": 0.1689, "mean_extremity_kalshi": 0.1697, "model_brier": 0.2103, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": 0.0082, "brier_diff_se": 0.0029, "model_logloss": 0.6075, "kalshi_logloss": 0.5861}, "gen1_elo": {"n": 2658, "model": {"intercept": -0.357, "slope": 1.049, "slope_se": 0.053}, "kalshi_mid_same_rows": {"intercept": 0.348, "slope": 1.179, "slope_se": 0.057}, "mean_extremity_model": 0.1732, "mean_extremity_kalshi": 0.1701, "model_brier": 0.2091, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": 0.007, "brier_diff_se": 0.0029, "model_logloss": 0.6061, "kalshi_logloss": 0.5862}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.243, "share_ge_15": 0.4307, "median_abs_gap": 12.79, "n": 16772}, "gen1_elo": {"share_ge_25": 0.2377, "share_ge_15": 0.4246, "median_abs_gap": 12.26, "n": 16772}, "gen1_sr": {"share_ge_25": 0.2981, "share_ge_15": 0.5145, "median_abs_gap": 15.51, "n": 16772}, "gen2": {"share_ge_25": 0.3016, "share_ge_15": 0.5032, "median_abs_gap": 15.18, "n": 16772}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1411, "share_ge_15": 0.3337, "median_abs_gap": 10.31, "n": 12744}, "gen1_elo": {"share_ge_25": 0.1393, "share_ge_15": 0.324, "median_abs_gap": 9.71, "n": 12743}, "gen1_sr": {"share_ge_25": 0.1962, "share_ge_15": 0.427, "median_abs_gap": 12.7, "n": 12744}, "gen2": {"share_ge_25": 0.2135, "share_ge_15": 0.429, "median_abs_gap": 12.64, "n": 12745}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.27, "share_ge_25_all": 0.0144, "share_ge_25_pregame_clean": 0.0141}, "WTA": {"median_abs_gap_pregame_clean": 7.77, "share_ge_25_all": 0.0623, "share_ge_25_pregame_clean": 0.0548}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2407, "share_within_10pp_all": 0.443, "share_within_10pp_pregame_clean": 0.5041, "corr_model_vs_mid_pregame_clean": 0.8492}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 408, "model_brier": 0.1934, "kalshi_brier": 0.1948, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 474, "model_brier": 0.2099, "kalshi_brier": 0.203, "brier_diff_model_minus_kalshi": 0.0069}, "15-25": {"n_settled": 572, "model_brier": 0.227, "kalshi_brier": 0.2143, "brier_diff_model_minus_kalshi": 0.0127}, "25-40": {"n_settled": 311, "model_brier": 0.2235, "kalshi_brier": 0.2079, "brier_diff_model_minus_kalshi": 0.0156}, "3-5": {"n_settled": 271, "model_brier": 0.1898, "kalshi_brier": 0.1905, "brier_diff_model_minus_kalshi": -0.0006}, "40+": {"n_settled": 68, "model_brier": 0.2909, "kalshi_brier": 0.1768, "brier_diff_model_minus_kalshi": 0.1141}, "5-10": {"n_settled": 554, "model_brier": 0.1983, "kalshi_brier": 0.1997, "brier_diff_model_minus_kalshi": -0.0014}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.553, "slope": 0.873, "slope_se": 0.049}, "kalshi_slope": {"intercept": 0.221, "slope": 1.126, "slope_se": 0.056}, "n": 2658}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.503, "slope": 0.881, "slope_se": 0.037}, "kalshi_slope": {"intercept": 0.166, "slope": 1.091, "slope_se": 0.041}, "n": 4621}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 268, "model_brier": 0.3357, "kalshi_brier": 0.2324, "brier_diff_model_minus_kalshi": 0.1033, "brier_diff_se": 0.0199, "corr_model_outcome": -0.0413, "corr_kalshi_outcome": 0.2681}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
