# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-08T02:53Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 23,612): 0-3 13.7%, 3-5 9.6%, 5-10 19.9%, 10-15 15.4%, 15-25 18.8%, 25-40 14.2%, 40+ 8.4%; median gap 12.08 pp.
* **Where the extremes live**: 98.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.7%, Challenger 12.8%, doubles 5.2%). Main tour: ATP 1.8% and WTA 8.2% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 5,353): MARKET_ALREADY_SETTLED_WHEN_PRICED 40.1%, STALE_QUOTE 18.1%, BOOK_QUALITY 16.7%, POOR_DATA 8.1%, POSSIBLY_IN_PLAY_QUOTE 5.2%, LIMITED_DATA 3.9%, IN_PLAY_QUOTE 3.2%, IDENTITY_AMBIGUOUS 2.6%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.2%. By class: coverage 40.1%, market_freshness 18.1%, execution 16.7%, data 12.0%, market_freshness/coverage 8.4%, mapping 2.6%, model_calibration_or_unknown 2.0%, model_calibration 0.2%.
* **Stale / settled / in-play**: 57.5% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 48.4% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 5,353 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 16.0% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 1.5%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 11.3% of the time and with the model 0.2%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 605.0 points vs 1701.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.134, Gen-2 0.912, Gen-1 ledger 0.941 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 218 model 0.2161 vs Kalshi 0.2039; n 49 model 0.2835 vs Kalshi 0.1763.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 87,900 model-market comparisons (147,999 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 33,278 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-08T02:47:16.398873+00:00'], shadow board 24,601 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-08T02:47:19.684101+00:00'], Model 4 8,847 rows, 10,406 settled tickers, 2,785 tickers with an external scan.
* By model: {"gen1_ledger": 21015, "gen1_elo": 12361, "fair_v1": 12361, "gen2": 12361, "gen1_sr": 12361, "model4_fundamental": 8725, "model4_conditioned": 8716}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 23,612 | 13.7 | 9.6 | 19.9 | 15.4 | 18.8 | 14.2 | 8.4 | 12.08 | 41.4% | 22.7% |
| MW fair_v1 | 12,361 | 12.9 | 8.8 | 18.4 | 16.0 | 18.5 | 15.2 | 10.2 | 13.05 | 43.9% | 25.4% |
| MW gen1_elo | 12,361 | 12.8 | 8.8 | 19.7 | 15.0 | 19.4 | 14.8 | 9.6 | 12.65 | 43.7% | 24.3% |
| MW gen1_ledger | 11,251 | 14.6 | 10.4 | 21.6 | 14.6 | 19.0 | 13.2 | 6.5 | 10.95 | 38.7% | 19.7% |
| MW gen1_sr | 12,361 | 10.1 | 7.8 | 15.9 | 14.2 | 21.6 | 18.7 | 11.9 | 15.76 | 52.1% | 30.6% |
| MW gen2 | 12,361 | 11.9 | 7.1 | 15.9 | 14.3 | 19.9 | 17.5 | 13.4 | 15.4 | 50.8% | 30.9% |
| all families model4_conditioned | 8,716 | 21.9 | 20.5 | 35.3 | 16.1 | 4.5 | 0.9 | 0.8 | 5.72 | 6.2% | 1.6% |
| all families model4_fundamental | 8,725 | 16.3 | 13.4 | 34.6 | 20.4 | 11.1 | 3.1 | 1.1 | 7.81 | 15.3% | 4.2% |

Configurable thresholds (primary): >=5pp 76.7%, >=10pp 56.8%, >=15pp 41.4%, >=20pp 31.0%, >=25pp 22.7%, >=30pp 16.6%, >=40pp 8.5%, >=50pp 3.6%
Executable gap (model outside the book, before fees): median 8.52pp; >=10pp 45.7%, >=25pp 18.3%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 870 | 25.8 | 16.4 | 24.2 | 17.5 | 13.4 | 1.4 | 1.3 | 6.01 | 16.1% | 2.6% |
| CHALLENGER | 2,158 | 14.4 | 11.1 | 18.5 | 16.1 | 13.1 | 13.6 | 13.2 | 12.04 | 39.9% | 26.8% |
| ITF_MEN | 3,555 | 10.9 | 8.6 | 18.9 | 14.5 | 19.5 | 15.1 | 12.7 | 13.98 | 47.2% | 27.7% |
| ITF_WOMEN | 4,940 | 10.4 | 6.8 | 16.0 | 16.1 | 21.5 | 19.2 | 10.0 | 15.3 | 50.7% | 29.2% |
| WTA | 530 | 23.4 | 9.6 | 24.9 | 16.4 | 17.4 | 6.2 | 2.1 | 8.16 | 25.7% | 8.3% |
| WTA125 | 308 | 12.3 | 6.8 | 20.8 | 25.6 | 14.9 | 16.9 | 2.6 | 11.33 | 34.4% | 19.5% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 870 | 21.6 | 14.6 | 23.8 | 18.6 | 17.5 | 2.4 | 1.5 | 6.9 | 21.4% | 3.9% |
| CHALLENGER | 2,158 | 14.9 | 7.3 | 17.7 | 13.4 | 18.5 | 14.6 | 13.6 | 13.43 | 46.7% | 28.2% |
| ITF_MEN | 3,555 | 10.6 | 7.3 | 16.6 | 14.6 | 19.8 | 17.6 | 13.4 | 15.41 | 50.8% | 31.0% |
| ITF_WOMEN | 4,940 | 9.1 | 6.0 | 12.9 | 13.1 | 20.9 | 21.4 | 16.6 | 18.89 | 58.9% | 38.0% |
| WTA | 530 | 21.9 | 5.1 | 17.9 | 15.3 | 21.3 | 16.4 | 2.1 | 12.59 | 39.8% | 18.5% |
| WTA125 | 308 | 4.9 | 2.9 | 16.9 | 22.7 | 20.1 | 20.1 | 12.3 | 16.74 | 52.6% | 32.5% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 870 | 26.4 | 11.2 | 29.8 | 16.7 | 11.2 | 3.5 | 1.4 | 6.85 | 16.0% | 4.8% |
| CHALLENGER | 2,158 | 15.5 | 11.0 | 19.5 | 14.1 | 14.1 | 12.6 | 13.2 | 11.03 | 39.9% | 25.8% |
| ITF_MEN | 3,555 | 9.9 | 8.8 | 18.4 | 14.1 | 20.7 | 15.4 | 12.7 | 14.47 | 48.8% | 28.2% |
| ITF_WOMEN | 4,940 | 9.6 | 6.7 | 16.8 | 15.6 | 23.5 | 19.0 | 8.6 | 15.5 | 51.2% | 27.7% |
| WTA | 530 | 22.8 | 13.2 | 35.1 | 14.5 | 9.4 | 3.6 | 1.3 | 6.99 | 14.3% | 4.9% |
| WTA125 | 308 | 21.1 | 12.0 | 28.2 | 17.5 | 15.3 | 5.2 | 0.7 | 7.73 | 21.1% | 5.8% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 415 | 28.4 | 21.0 | 37.8 | 11.6 | 1.2 | 0.0 | 0.0 | 5.11 | 1.2% | 0.0% |
| CHALLENGER | 1,384 | 22.8 | 16.5 | 26.4 | 14.2 | 12.5 | 5.5 | 2.2 | 6.73 | 20.2% | 7.7% |
| DOUBLES | 611 | 4.1 | 3.4 | 12.8 | 12.1 | 22.3 | 22.6 | 22.8 | 23.2 | 67.6% | 45.3% |
| ITF_MEN | 3,582 | 14.0 | 8.8 | 20.4 | 15.2 | 20.4 | 13.0 | 8.2 | 12.05 | 41.7% | 21.2% |
| ITF_WOMEN | 4,194 | 11.7 | 9.4 | 19.7 | 14.0 | 22.0 | 17.2 | 5.9 | 13.06 | 45.1% | 23.1% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 438 | 20.1 | 11.6 | 25.8 | 18.9 | 15.5 | 7.3 | 0.7 | 8.48 | 23.5% | 8.0% |
| WTA125 | 478 | 15.9 | 12.8 | 22.2 | 19.7 | 17.4 | 9.2 | 2.9 | 9.77 | 29.5% | 12.1% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 866 | 25.8 | 16.3 | 24.2 | 17.6 | 13.5 | 1.4 | 1.3 | 6.03 | 16.2% | 2.7% |
| CHALLENGER | 1,521 | 19.0 | 14.3 | 24.1 | 18.9 | 13.9 | 7.0 | 3.0 | 8.32 | 23.8% | 9.9% |
| ITF_MEN | 2,575 | 13.3 | 10.9 | 22.2 | 16.2 | 19.6 | 12.1 | 5.6 | 11.01 | 37.3% | 17.8% |
| ITF_WOMEN | 3,576 | 12.8 | 8.4 | 18.9 | 18.6 | 23.0 | 15.2 | 3.0 | 12.64 | 41.2% | 18.2% |
| WTA | 527 | 23.3 | 9.7 | 25.1 | 16.3 | 17.5 | 6.1 | 2.1 | 8.16 | 25.6% | 8.2% |
| WTA125 | 297 | 12.8 | 7.1 | 20.5 | 25.9 | 15.2 | 16.8 | 1.7 | 11.31 | 33.7% | 18.5% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 866 | 21.5 | 14.6 | 23.9 | 18.6 | 17.6 | 2.4 | 1.5 | 6.91 | 21.5% | 3.9% |
| CHALLENGER | 1,521 | 19.7 | 9.7 | 22.4 | 16.4 | 18.9 | 10.1 | 2.8 | 9.56 | 31.8% | 12.9% |
| ITF_MEN | 2,576 | 12.7 | 8.7 | 19.4 | 16.7 | 21.0 | 15.1 | 6.4 | 12.58 | 42.5% | 21.5% |
| ITF_WOMEN | 3,576 | 10.5 | 7.2 | 15.0 | 14.3 | 23.0 | 19.9 | 10.2 | 16.11 | 53.0% | 30.1% |
| WTA | 527 | 21.8 | 5.1 | 18.0 | 15.4 | 21.2 | 16.3 | 2.1 | 12.47 | 39.7% | 18.4% |
| WTA125 | 297 | 5.0 | 3.0 | 17.2 | 23.6 | 19.2 | 20.9 | 11.1 | 15.85 | 51.2% | 32.0% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 400 | 28.8 | 21.2 | 38.0 | 11.8 | 0.2 | 0.0 | 0.0 | 5.0 | 0.2% | 0.0% |
| CHALLENGER | 1,166 | 24.8 | 18.7 | 28.7 | 13.8 | 11.8 | 2.1 | 0.1 | 6.04 | 14.0% | 2.1% |
| DOUBLES | 557 | 4.1 | 3.4 | 13.1 | 12.0 | 22.6 | 22.3 | 22.4 | 22.7 | 67.3% | 44.7% |
| ITF_MEN | 2,880 | 15.8 | 9.8 | 22.8 | 16.2 | 20.1 | 10.6 | 4.8 | 10.5 | 35.5% | 15.3% |
| ITF_WOMEN | 3,401 | 13.2 | 10.2 | 21.6 | 14.9 | 22.1 | 15.5 | 2.5 | 11.36 | 40.1% | 18.0% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 408 | 20.6 | 12.2 | 26.5 | 19.1 | 15.9 | 5.6 | 0.0 | 8.4 | 21.6% | 5.6% |
| WTA125 | 395 | 18.0 | 14.2 | 24.8 | 22.5 | 15.4 | 4.8 | 0.2 | 8.55 | 20.5% | 5.1% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 611 | 4.1 | 3.4 | 12.8 | 12.1 | 22.3 | 22.6 | 22.8 | 23.2 | 67.6% | 45.3% |
| singles | 10,640 | 15.2 | 10.9 | 22.1 | 14.8 | 18.8 | 12.7 | 5.6 | 10.48 | 37.1% | 18.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 2,885 | 13.0 | 9.7 | 20.3 | 15.5 | 16.0 | 14.8 | 10.8 | 12.29 | 41.6% | 25.7% |
| Hard | 8,313 | 13.0 | 8.6 | 18.3 | 15.9 | 19.2 | 15.0 | 10.0 | 13.23 | 44.2% | 25.0% |
| UNKNOWN | 1,163 | 12.0 | 8.5 | 14.2 | 18.2 | 20.0 | 17.3 | 9.7 | 14.1 | 47.0% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,540 | 17.9 | 11.3 | 20.3 | 16.9 | 15.1 | 10.1 | 8.3 | 10.09 | 33.6% | 18.5% |
| B | 1,562 | 15.2 | 9.9 | 19.8 | 17.2 | 16.1 | 11.8 | 10.1 | 11.14 | 38.0% | 21.9% |
| C | 1,932 | 12.6 | 9.8 | 20.5 | 15.1 | 18.4 | 14.2 | 9.3 | 12.55 | 42.0% | 23.5% |
| D | 2,366 | 11.2 | 8.7 | 16.9 | 16.1 | 22.6 | 15.2 | 9.3 | 14.04 | 47.0% | 24.5% |
| F | 2,961 | 7.3 | 4.9 | 15.0 | 14.8 | 20.8 | 23.5 | 13.8 | 18.53 | 58.1% | 37.3% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,048 | 21.2 | 15.0 | 27.3 | 15.9 | 13.0 | 5.3 | 2.2 | 7.24 | 20.5% | 7.5% |
| B | 1,749 | 14.6 | 10.0 | 24.7 | 15.8 | 18.1 | 11.7 | 5.1 | 10.16 | 34.9% | 16.8% |
| C | 2,242 | 12.2 | 8.4 | 19.4 | 14.4 | 20.9 | 14.9 | 9.8 | 13.1 | 45.6% | 24.7% |
| D | 1,920 | 13.4 | 9.1 | 21.1 | 13.2 | 22.1 | 14.7 | 6.3 | 12.23 | 43.1% | 21.0% |
| F | 2,292 | 9.2 | 7.9 | 14.0 | 13.4 | 23.2 | 21.8 | 10.5 | 17.0 | 55.5% | 32.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 4,014 | 16.9 | 10.5 | 19.5 | 17.1 | 15.3 | 10.4 | 10.3 | 10.87 | 36.0% | 20.7% |
| LIMITED | 2,982 | 14.4 | 10.6 | 21.3 | 15.6 | 17.4 | 13.3 | 7.3 | 11.05 | 38.0% | 20.6% |
| POOR | 5,365 | 9.1 | 6.7 | 15.8 | 15.4 | 21.6 | 19.7 | 11.8 | 16.19 | 53.1% | 31.5% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,737 | 29.8 | 26.2 | 36.8 | 5.4 | 1.7 | 0.2 | 0.0 | 4.47 | 1.8% | 0.2% |
| GAME_SPREAD | 1,835 | 24.1 | 15.4 | 36.9 | 18.6 | 4.6 | 0.3 | 0.2 | 6.18 | 5.0% | 0.4% |
| MATCH_WINNER | 11,251 | 14.6 | 10.4 | 21.6 | 14.6 | 19.0 | 13.2 | 6.5 | 10.95 | 38.7% | 19.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 3,398 | 29.2 | 19.0 | 31.2 | 11.4 | 7.3 | 1.4 | 0.3 | 5.21 | 9.0% | 1.7% |
| TOTAL_GAMES | 2,770 | 7.5 | 9.3 | 38.2 | 29.6 | 9.9 | 3.3 | 2.3 | 9.45 | 15.4% | 5.6% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,200 | 24.2 | 39.5 | 29.7 | 0.3 | 5.6 | 0.5 | 0.2 | 4.34 | 6.3% | 0.7% |
| GAME_SPREAD | 2,223 | 46.1 | 14.1 | 29.6 | 8.4 | 1.1 | 0.5 | 0.2 | 3.54 | 1.8% | 0.7% |
| TOTAL_GAMES | 3,293 | 3.4 | 6.3 | 44.7 | 36.6 | 5.8 | 1.4 | 1.7 | 9.6 | 9.0% | 3.1% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,200 | 25.2 | 18.4 | 35.5 | 10.2 | 7.2 | 3.0 | 0.5 | 5.63 | 10.7% | 3.5% |
| GAME_SPREAD | 2,223 | 19.2 | 13.2 | 26.3 | 23.0 | 14.7 | 3.0 | 0.7 | 8.38 | 18.3% | 3.6% |
| TOTAL_GAMES | 3,302 | 5.8 | 8.6 | 39.3 | 28.7 | 12.3 | 3.2 | 2.1 | 9.6 | 17.6% | 5.3% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 12,361 | 43.9% | 25.4% | 13.05 | 33.9% | 14.7% | 10.46 |
| gen1_elo | 12,361 | 43.7% | 24.3% | 12.65 | 33.5% | 14.2% | 10.03 |
| gen1_sr | 12,361 | 52.1% | 30.6% | 15.76 | 43.1% | 20.1% | 12.89 |
| gen2 | 12,361 | 50.8% | 30.9% | 15.4 | 43.0% | 21.9% | 12.71 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 6,031 | 15.6 | 11.4 | 21.5 | 17.4 | 18.7 | 11.9 | 3.5 | 10.39 | 34.1% | 15.4% |
| STALE | 6,330 | 10.4 | 6.5 | 15.3 | 14.7 | 18.4 | 18.2 | 16.6 | 16.72 | 53.2% | 34.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 4,719 | 16.7 | 11.7 | 24.1 | 14.5 | 17.0 | 11.9 | 4.2 | 9.33 | 33.0% | 16.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 23,612 | 4719 | 9503 | 9390 | 25.5 | 170.0 | 1400.4 |
| ge_15pp | 9,782 | 1558 | 3347 | 4877 | 29.8 | 455.5 | 1380.4 |
| ge_25pp | 5,353 | 757 | 1520 | 3076 | 39.8 | 574.7 | 1380.4 |
| lt_10pp | 10,204 | 2478 | 4554 | 3172 | 24.3 | 52.4 | 1230.8 |

Current slate `SL-20261008T025339Z-90255c92`: 525 priced rows, quote age at build {'median': 6.8, 'max': 6.9}, freshness {'FRESH': 525}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 1 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 20.71 | 100.0% | 0.0% |
| EXTERNAL_LONE_OUTLIER | 2 | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.98 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 509 | 21.2 | 12.0 | 21.0 | 20.2 | 17.9 | 7.3 | 0.4 | 8.64 | 25.5% | 7.7% |
| MARKETS_AGREE | 36 | 72.2 | 27.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.18 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 70 | 0.0 | 2.9 | 28.6 | 34.3 | 21.4 | 12.9 | 0.0 | 11.66 | 34.3% | 12.9% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 12,361 | 618 (5.0%) | 11.3% | 0.2% | {"EXTERNAL_STALE": 509, "AGREES_WITH_KALSHI": 70, "ALL_AGREE": 36, "EXTERNAL_OUTLIER": 2, "SUPPORTS_MODEL_DIRECTION": 1} |
| fair_v1_ge_15pp | 5,425 | 155 (2.9%) | 15.5% | 0.7% | {"EXTERNAL_STALE": 130, "AGREES_WITH_KALSHI": 24, "SUPPORTS_MODEL_DIRECTION": 1} |
| fair_v1_ge_25pp | 3,134 | 48 (1.5%) | 18.8% | 0.0% | {"EXTERNAL_STALE": 39, "AGREES_WITH_KALSHI": 9} |
| fair_v1_ge_25pp_pregame_clean | 1,380 | 47 (3.4%) | 19.1% | 0.0% | {"EXTERNAL_STALE": 38, "AGREES_WITH_KALSHI": 9} |
| fair_v1_lt_10pp | 4,957 | 336 (6.8%) | 6.6% | 0.0% | {"EXTERNAL_STALE": 276, "ALL_AGREE": 36, "AGREES_WITH_KALSHI": 22, "EXTERNAL_OUTLIER": 2} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 2,505 | 11.3 | 8.6 | 20.3 | 15.7 | 20.9 | 14.1 | 9.2 | 12.82 | 44.1% | 23.2% |
| 4-10x | 1,812 | 11.3 | 9.3 | 17.9 | 14.4 | 20.6 | 17.2 | 9.2 | 14.09 | 47.1% | 26.4% |
| <2x | 6,439 | 14.7 | 9.5 | 18.3 | 16.9 | 17.0 | 13.5 | 10.2 | 12.26 | 40.7% | 23.7% |
| >=10x | 1,605 | 10.2 | 6.2 | 15.9 | 14.8 | 18.8 | 21.1 | 13.0 | 16.24 | 52.9% | 34.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 3,145 | 13.9 | 8.7 | 20.2 | 15.8 | 17.4 | 12.9 | 11.0 | 12.14 | 41.4% | 24.0% |
| 300-1000 | 3,044 | 12.2 | 9.3 | 16.7 | 15.9 | 21.3 | 16.0 | 8.6 | 13.69 | 45.9% | 24.6% |
| <300 | 3,442 | 8.0 | 6.0 | 15.6 | 15.0 | 20.7 | 21.4 | 13.3 | 17.29 | 55.5% | 34.8% |
| >=3000 | 2,730 | 18.8 | 12.1 | 21.5 | 17.7 | 14.0 | 8.8 | 7.1 | 9.44 | 29.8% | 15.9% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 377 | 0.5399 | 0.4078 | 0.4695 | +0.070 | -0.062 | 0.0025 ± 0.0074 |
| ratio 4-10x | 278 | 0.588 | 0.4465 | 0.536 | +0.052 | -0.089 | -0.006 ± 0.0093 |
| ratio <2x | 793 | 0.5432 | 0.4157 | 0.4578 | +0.086 | -0.042 | 0.0107 ± 0.0052 |
| ratio >=10x | 258 | 0.5624 | 0.3872 | 0.4612 | +0.101 | -0.074 | 0.013 ± 0.0115 |
| thinner_sample 1000-3000 | 448 | 0.5457 | 0.4198 | 0.4598 | +0.086 | -0.040 | 0.0058 ± 0.0068 |
| thinner_sample 300-1000 | 471 | 0.5731 | 0.4333 | 0.4989 | +0.074 | -0.066 | 0.0001 ± 0.0071 |
| thinner_sample <300 | 545 | 0.5527 | 0.3893 | 0.4789 | +0.074 | -0.090 | 0.0076 ± 0.0075 |
| thinner_sample >=3000 | 242 | 0.5256 | 0.4259 | 0.438 | +0.088 | -0.012 | 0.0182 ± 0.0076 |
| data_status ADEQUATE | 448 | 0.5294 | 0.4226 | 0.4375 | +0.092 | -0.015 | 0.0121 ± 0.0059 |
| data_status LIMITED | 411 | 0.565 | 0.4309 | 0.4964 | +0.069 | -0.065 | -0.0003 ± 0.0075 |
| data_status POOR | 847 | 0.559 | 0.4026 | 0.4817 | +0.077 | -0.079 | 0.0069 ± 0.0058 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 247 | 0.1792 | 0.1803 | -0.0011 ± 0.0009 | 0.532 | 0.5348 | 0.4937 | 0.4793 | 0.5101 | -0.086 ± 0.0286 | -0.01 (3) |
| 3-5 | 170 | 0.1848 | 0.1851 | -0.0003 ± 0.0027 | 0.5484 | 0.5464 | 0.5113 | 0.4714 | 0.4882 | -0.087 ± 0.0336 | 0.02 (1) |
| 5-10 | 353 | 0.2004 | 0.2019 | -0.0016 ± 0.0036 | 0.587 | 0.5918 | 0.5196 | 0.4459 | 0.4844 | -0.096 ± 0.025 | -0.0167 (3) |
| 10-15 | 298 | 0.22 | 0.2177 | +0.0023 ± 0.0068 | 0.6286 | 0.6194 | 0.5331 | 0.4088 | 0.4597 | -0.093 ± 0.0271 | -0.0633 (3) |
| 15-25 | 371 | 0.2203 | 0.211 | +0.0093 ± 0.0093 | 0.6316 | 0.6098 | 0.5735 | 0.3776 | 0.4501 | -0.083 ± 0.0238 | -0.02 (4) |
| 25-40 | 218 | 0.2161 | 0.2039 | +0.0122 ± 0.0181 | 0.6204 | 0.5841 | 0.6522 | 0.3424 | 0.4771 | -0.071 ± 0.0271 | -0.01 (1) |
| 40+ | 49 | 0.2835 | 0.1763 | +0.1072 ± 0.0527 | 0.7693 | 0.5281 | 0.75 | 0.3043 | 0.4082 | -0.120 ± 0.0527 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1142 | 0.1629 | 0.1633 | -0.0004 ± 0.0004 | 0.4917 | 0.4918 | 0.4782 | 0.4633 | 0.4956 | -0.037 ± 0.0122 | -0.0188 (8) |
| 3-5 | 817 | 0.1914 | 0.1863 | +0.0052 ± 0.0012 | 0.5654 | 0.5474 | 0.4791 | 0.4396 | 0.3905 | -0.113 ± 0.0153 | 0.02 (1) |
| 5-10 | 1743 | 0.1909 | 0.1889 | +0.0020 ± 0.0016 | 0.5644 | 0.5589 | 0.4911 | 0.4175 | 0.4383 | -0.054 ± 0.0105 | -0.0129 (7) |
| 10-15 | 1515 | 0.205 | 0.1907 | +0.0144 ± 0.0028 | 0.5962 | 0.5558 | 0.4786 | 0.3539 | 0.3591 | -0.071 ± 0.0112 | -0.0633 (3) |
| 15-25 | 1875 | 0.198 | 0.1634 | +0.0346 ± 0.0037 | 0.5849 | 0.4877 | 0.4901 | 0.2935 | 0.3045 | -0.069 ± 0.0093 | -0.017 (10) |
| 25-40 | 1665 | 0.2153 | 0.126 | +0.0893 ± 0.0054 | 0.6224 | 0.3884 | 0.5288 | 0.2155 | 0.2318 | -0.056 ± 0.0084 | -0.01 (1) |
| 40+ | 1152 | 0.366 | 0.0462 | +0.3197 ± 0.007 | 0.9549 | 0.1801 | 0.6202 | 0.1057 | 0.0625 | -0.078 ± 0.0059 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 194 | 0.1952 | 0.1954 | -0.0003 ± 0.0011 | 0.5738 | 0.5741 | 0.4941 | 0.4791 | 0.4742 | -0.119 ± 0.0333 | -0.01 (1) |
| 3-5 | 124 | 0.2044 | 0.2038 | +0.0006 ± 0.0033 | 0.5872 | 0.5894 | 0.5078 | 0.4679 | 0.4758 | -0.085 ± 0.0434 | 0.02 (1) |
| 5-10 | 297 | 0.1915 | 0.1901 | +0.0014 ± 0.0038 | 0.5658 | 0.5621 | 0.5636 | 0.4882 | 0.5118 | -0.092 ± 0.0261 | -0.01 (4) |
| 10-15 | 292 | 0.2189 | 0.2087 | +0.0102 ± 0.0067 | 0.6248 | 0.6045 | 0.5866 | 0.4622 | 0.4897 | -0.117 ± 0.0279 | -0.0667 (3) |
| 15-25 | 412 | 0.2223 | 0.206 | +0.0163 ± 0.0089 | 0.6318 | 0.5931 | 0.5999 | 0.4024 | 0.466 | -0.102 ± 0.0231 | -0.0167 (3) |
| 25-40 | 282 | 0.266 | 0.2061 | +0.0600 ± 0.0169 | 0.7441 | 0.5943 | 0.6739 | 0.3613 | 0.422 | -0.135 ± 0.0272 | -0.025 (2) |
| 40+ | 105 | 0.3393 | 0.1907 | +0.1486 ± 0.0416 | 0.9415 | 0.5571 | 0.7604 | 0.2777 | 0.381 | -0.054 ± 0.0393 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1077 | 0.1746 | 0.1755 | -0.0008 ± 0.0004 | 0.5217 | 0.524 | 0.4967 | 0.4825 | 0.5097 | -0.037 ± 0.0134 | -0.0217 (6) |
| 3-5 | 668 | 0.1886 | 0.1849 | +0.0038 ± 0.0013 | 0.5482 | 0.5405 | 0.5171 | 0.4772 | 0.4521 | -0.080 ± 0.0169 | 0.02 (1) |
| 5-10 | 1502 | 0.1816 | 0.1795 | +0.0022 ± 0.0016 | 0.5447 | 0.5357 | 0.5133 | 0.4391 | 0.4601 | -0.048 ± 0.0111 | -0.01 (5) |
| 10-15 | 1357 | 0.1958 | 0.1812 | +0.0146 ± 0.0029 | 0.5799 | 0.5323 | 0.5237 | 0.3995 | 0.406 | -0.074 ± 0.0118 | -0.0575 (4) |
| 15-25 | 1956 | 0.2092 | 0.1707 | +0.0385 ± 0.0037 | 0.6097 | 0.5061 | 0.5283 | 0.3331 | 0.3354 | -0.082 ± 0.0095 | -0.0143 (7) |
| 25-40 | 1862 | 0.2465 | 0.1388 | +0.1077 ± 0.0055 | 0.6982 | 0.4222 | 0.5626 | 0.2458 | 0.2352 | -0.087 ± 0.0087 | -0.015 (6) |
| 40+ | 1487 | 0.3995 | 0.072 | +0.3275 ± 0.008 | 1.0454 | 0.2482 | 0.6702 | 0.1317 | 0.111 | -0.062 ± 0.0067 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 255 | 0.1876 | 0.1899 | -0.0023 ± 0.001 | 0.5521 | 0.5587 | 0.5046 | 0.4894 | 0.549 | -0.036 ± 0.0276 | -0.01 (5) |
| 3-5 | 184 | 0.1842 | 0.182 | +0.0022 ± 0.0025 | 0.5436 | 0.5384 | 0.4913 | 0.452 | 0.4457 | -0.136 ± 0.0335 | -- (0) |
| 5-10 | 358 | 0.1958 | 0.1972 | -0.0014 ± 0.0035 | 0.577 | 0.5792 | 0.5174 | 0.4437 | 0.4832 | -0.087 ± 0.0243 | -0.01 (3) |
| 10-15 | 282 | 0.2165 | 0.2161 | +0.0004 ± 0.0069 | 0.6238 | 0.6177 | 0.5434 | 0.4202 | 0.4823 | -0.090 ± 0.0273 | -0.044 (5) |
| 15-25 | 366 | 0.2255 | 0.2103 | +0.0151 ± 0.0093 | 0.6478 | 0.6058 | 0.5821 | 0.3886 | 0.4454 | -0.099 ± 0.0238 | -0.03 (1) |
| 25-40 | 218 | 0.2023 | 0.2095 | -0.0072 ± 0.0179 | 0.5884 | 0.5993 | 0.6571 | 0.3459 | 0.5092 | -0.052 ± 0.0262 | 0.0 (1) |
| 40+ | 43 | 0.3101 | 0.1754 | +0.1346 ± 0.0575 | 0.8319 | 0.5258 | 0.7415 | 0.29 | 0.3721 | -0.132 ± 0.059 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1111 | 0.1767 | 0.1779 | -0.0012 ± 0.0004 | 0.5246 | 0.5273 | 0.4842 | 0.469 | 0.5104 | -0.024 ± 0.0127 | -0.0162 (13) |
| 3-5 | 843 | 0.1855 | 0.1822 | +0.0034 ± 0.0012 | 0.5474 | 0.5402 | 0.4711 | 0.4318 | 0.4093 | -0.095 ± 0.0153 | -0.01 (2) |
| 5-10 | 1783 | 0.1823 | 0.1795 | +0.0028 ± 0.0015 | 0.5458 | 0.5347 | 0.4856 | 0.4116 | 0.4262 | -0.057 ± 0.0101 | -0.01 (3) |
| 10-15 | 1432 | 0.1998 | 0.1833 | +0.0165 ± 0.0028 | 0.5851 | 0.5364 | 0.4927 | 0.3694 | 0.3638 | -0.084 ± 0.0112 | -0.03 (9) |
| 15-25 | 2052 | 0.2065 | 0.1684 | +0.0381 ± 0.0036 | 0.6061 | 0.5008 | 0.4954 | 0.2987 | 0.3012 | -0.072 ± 0.0091 | -0.03 (2) |
| 25-40 | 1606 | 0.2135 | 0.1215 | +0.0920 ± 0.0055 | 0.6179 | 0.3759 | 0.5233 | 0.206 | 0.2235 | -0.059 ± 0.0082 | 0.0 (1) |
| 40+ | 1082 | 0.3791 | 0.0471 | +0.3321 ± 0.0075 | 0.9922 | 0.1829 | 0.6265 | 0.105 | 0.0591 | -0.080 ± 0.0062 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 538 | 0.2016 | 0.2016 | -0.0000 ± 0.0007 | 0.5867 | 0.5863 | 0.5001 | 0.4853 | 0.487 | -0.048 ± 0.0193 | -0.0226 (46) |
| 3-5 | 401 | 0.1957 | 0.1947 | +0.0010 ± 0.0018 | 0.5732 | 0.5692 | 0.48 | 0.4404 | 0.4514 | -0.046 ± 0.022 | -0.0059 (32) |
| 5-10 | 824 | 0.1906 | 0.1853 | +0.0053 ± 0.0023 | 0.5645 | 0.5514 | 0.4707 | 0.3971 | 0.3993 | -0.059 ± 0.0153 | -0.005 (72) |
| 10-15 | 541 | 0.2022 | 0.1917 | +0.0105 ± 0.0047 | 0.5923 | 0.5641 | 0.4761 | 0.3531 | 0.3715 | -0.046 ± 0.0188 | 0.0016 (63) |
| 15-25 | 745 | 0.2347 | 0.2101 | +0.0246 ± 0.0066 | 0.6644 | 0.6059 | 0.5439 | 0.3495 | 0.3852 | -0.054 ± 0.0169 | -0.0216 (58) |
| 25-40 | 415 | 0.2435 | 0.1825 | +0.0610 ± 0.013 | 0.6843 | 0.5377 | 0.6178 | 0.3043 | 0.3614 | -0.070 ± 0.0196 | -0.0216 (25) |
| 40+ | 139 | 0.3461 | 0.1831 | +0.1630 ± 0.0371 | 0.9827 | 0.5433 | 0.768 | 0.2747 | 0.3813 | -0.043 ± 0.0329 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1495 | 0.1881 | 0.1879 | +0.0002 ± 0.0004 | 0.5538 | 0.5523 | 0.4994 | 0.4841 | 0.4836 | -0.047 ± 0.0111 | -0.0155 (82) |
| 3-5 | 1052 | 0.1857 | 0.1837 | +0.0020 ± 0.0011 | 0.5468 | 0.5421 | 0.4878 | 0.4482 | 0.4468 | -0.052 ± 0.0132 | -0.018 (54) |
| 5-10 | 2192 | 0.1872 | 0.1797 | +0.0075 ± 0.0014 | 0.5569 | 0.5364 | 0.472 | 0.398 | 0.3869 | -0.067 ± 0.0092 | -0.0089 (122) |
| 10-15 | 1522 | 0.198 | 0.1835 | +0.0145 ± 0.0027 | 0.5824 | 0.5442 | 0.4873 | 0.3644 | 0.3666 | -0.059 ± 0.0109 | -0.0053 (99) |
| 15-25 | 2038 | 0.2276 | 0.1983 | +0.0293 ± 0.0039 | 0.6543 | 0.5767 | 0.5373 | 0.342 | 0.3651 | -0.054 ± 0.01 | -0.0255 (106) |
| 25-40 | 1420 | 0.2363 | 0.1564 | +0.0799 ± 0.0066 | 0.6694 | 0.4687 | 0.58 | 0.2648 | 0.2972 | -0.061 ± 0.0101 | -0.0206 (47) |
| 40+ | 692 | 0.3541 | 0.1062 | +0.2479 ± 0.0132 | 0.9682 | 0.3358 | 0.673 | 0.1676 | 0.1879 | -0.054 ± 0.0115 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 1706 | 1.134 ± 0.071 | 1.217 | 0.1693 | 0.1664 | 0.2079 | 0.2014 |
| gen2 | 1706 | 0.912 ± 0.062 | 1.144 | 0.1864 | 0.1659 | 0.2264 | 0.2014 |
| gen1_elo | 1706 | 1.111 ± 0.069 | 1.202 | 0.1731 | 0.1669 | 0.2068 | 0.2014 |
| gen1_sr | 1706 | 1.137 ± 0.08 | 1.228 | 0.143 | 0.1683 | 0.2218 | 0.2013 |
| gen1_ledger | 3603 | 0.941 ± 0.044 | 1.09 | 0.1693 | 0.1917 | 0.2157 | 0.1945 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 9,782)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,713 | 27.7% |
| STALE_QUOTE | market_freshness | 2,176 | 22.2% |
| BOOK_QUALITY | execution | 1,713 | 17.5% |
| POOR_DATA | data | 1,028 | 10.5% |
| LIMITED_DATA | data | 670 | 6.9% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 504 | 5.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 448 | 4.6% |
| IN_PLAY_QUOTE | market_freshness/coverage | 271 | 2.8% |
| IDENTITY_AMBIGUOUS | mapping | 239 | 2.4% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 20 | 0.2% |

Cause class: coverage 27.7%, market_freshness 22.2%, execution 17.5%, data 17.4%, market_freshness/coverage 7.9%, model_calibration_or_unknown 4.6%, mapping 2.4%, model_calibration 0.2%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.6%, START_UNVERIFIABLE 96.1%, LOW_DATA_QUALITY 69.2%, THIN_PLAYER_HISTORY 58.5%, STALE_PLAYER_DATA 58.3%, STALE_KALSHI_QUOTE 49.9%, MODEL_INTERNAL_DISAGREEMENT 37.5%, ASYMMETRIC_SAMPLE_SIZE 31.6%, WIDE_SPREAD 23.9%, MODEL_HIGH_UNCERTAINTY 15.8%, PLAYER_IDENTITY_RISK 10.6%, LEVEL_TRANSFER_RISK 8.7%, LOW_DISPLAYED_LIQUIDITY 7.3%, EVENT_MAPPING_RISK 7.1%, MODEL_CALIBRATION_OUTLIER 2.9%, UNKNOWN 0.5%, EXTERNAL_MARKET_REJECTION 0.4%, EXTERNAL_MARKET_CONFIRMATION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 30.0%, POST_SETTLEMENT_OBSERVATION 27.7%, POSSIBLE_IN_PLAY_QUOTE 5.6%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### >= ge_25 pp (N = 5,353)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,144 | 40.1% |
| STALE_QUOTE | market_freshness | 971 | 18.1% |
| BOOK_QUALITY | execution | 892 | 16.7% |
| POOR_DATA | data | 433 | 8.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 278 | 5.2% |
| LIMITED_DATA | data | 211 | 3.9% |
| IN_PLAY_QUOTE | market_freshness/coverage | 171 | 3.2% |
| IDENTITY_AMBIGUOUS | mapping | 137 | 2.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 107 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 9 | 0.2% |

Cause class: coverage 40.1%, market_freshness 18.1%, execution 16.7%, data 12.0%, market_freshness/coverage 8.4%, mapping 2.6%, model_calibration_or_unknown 2.0%, model_calibration 0.2%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.8%, START_UNVERIFIABLE 98.1%, LOW_DATA_QUALITY 71.6%, THIN_PLAYER_HISTORY 60.4%, STALE_KALSHI_QUOTE 57.5%, STALE_PLAYER_DATA 53.7%, MODEL_INTERNAL_DISAGREEMENT 39.4%, ASYMMETRIC_SAMPLE_SIZE 33.8%, WIDE_SPREAD 23.0%, MODEL_HIGH_UNCERTAINTY 17.1%, PLAYER_IDENTITY_RISK 13.2%, EVENT_MAPPING_RISK 8.1%, LOW_DISPLAYED_LIQUIDITY 7.7%, LEVEL_TRANSFER_RISK 7.4%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 0.2%, UNKNOWN 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 42.7%, POST_SETTLEMENT_OBSERVATION 40.1%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 4496, "IDENTITY_AMBIGUOUS": 857}; ticker orientation: {"VERIFIED": 5353}.

Checks: discipline:AMBIGUOUS 277, discipline:PASS 5076, identity_confidence:AMBIGUOUS 704, identity_confidence:PASS 4649, level_mapping:NA 289, level_mapping:PASS 5064, market_pair:AMBIGUOUS 192, market_pair:NA 125, market_pair:PASS 5036, model_complement:NA 92, model_complement:PASS 5261, namesake:PASS 5353, physical_match_id:NA 2219, physical_match_id:PASS 3134, player_ids:PASS 5353, same_pair_other_event:PASS 5353, ticker_orientation:PASS 5353

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,285 | 1.8% | 1.8% | 0.4% | {"market_freshness": 20, "execution": 3} | 5.72 | 0.2039 / 0.2 (105) | 21.7% | 0.2% | 6.3% | 1.5% |
| CHALLENGER | 3,542 | 19.3% | 6.6% | 12.8% | {"coverage": 427, "market_freshness": 107, "market_freshness/coverage": 81, "model_calibration_or_unknown": 38, "data": 25, "execution": 4, "model_calibration": 2} | 6.92 | 0.223 / 0.2047 (844) | 47.7% | 5.1% | 1.6% | 24.1% |
| DOUBLES | 611 | 45.3% | 44.7% | 5.2% | {"market_freshness": 106, "execution": 89, "mapping": 54, "market_freshness/coverage": 21, "coverage": 7} | 22.7 | 0.3105 / 0.2241 (194) | 38.3% | 0.0% | 100.0% | 8.8% |
| ITF_MEN | 7,137 | 24.5% | 16.5% | 32.6% | {"coverage": 710, "execution": 378, "market_freshness": 261, "data": 240, "market_freshness/coverage": 138, "mapping": 19, "model_calibration_or_unknown": 1} | 10.71 | 0.2127 / 0.1926 (1769) | 39.9% | 55.6% | 6.4% | 23.6% |
| ITF_WOMEN | 9,134 | 26.4% | 18.1% | 45.1% | {"coverage": 983, "market_freshness": 420, "execution": 401, "data": 355, "market_freshness/coverage": 168, "mapping": 58, "model_calibration_or_unknown": 22, "model_calibration": 6} | 12.11 | 0.2012 / 0.193 (1941) | 41.0% | 59.3% | 10.2% | 23.6% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 968 | 8.2% | 7.1% | 1.5% | {"market_freshness": 34, "model_calibration_or_unknown": 16, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.28 | 0.2008 / 0.1978 (145) | 34.4% | 2.2% | 1.2% | 3.4% |
| WTA125 | 786 | 15.0% | 10.8% | 2.2% | {"market_freshness/coverage": 31, "model_calibration_or_unknown": 28, "market_freshness": 21, "data": 13, "coverage": 12, "execution": 8, "mapping": 4, "model_calibration": 1} | 10.01 | 0.2242 / 0.2098 (269) | 27.2% | 5.7% | 4.3% | 12.0% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 5 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 15.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 928 min (STALE); no external reference |
| 6 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 7 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 8 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 9 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 10 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 11 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 12 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 92 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 14 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 15 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 16 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 17 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 18 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 874 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 19 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 20 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 21 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 22 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 23 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 24 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 25 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 26 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 27 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 189 min (STALE); no external reference |
| 28 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 29 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 30 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 31 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 32 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 33 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 253 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 34 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 35 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 36 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 37 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 38 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 256 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 39 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 114 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 40 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 41 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 42 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 43 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 156 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 44 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 45 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 46 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 47 | `KXATPCHALLENGERMATCH-26OCT06BARSAM-SAM` | CHALLENGER | fair_v1 | 84% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 710 min (STALE); no external reference |
| 48 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 49 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 114 min (STALE); data LIMITED (grade B, thinner serve sample 2163.0, ratio 2.0); no external reference |
| 50 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 183 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9809, "by_level_share_of_ge_25pp": {"ATP": 0.0043, "CHALLENGER": 0.1278, "DOUBLES": 0.0517, "ITF_MEN": 0.3264, "ITF_WOMEN": 0.4508, "OTHER": 0.0022, "WTA": 0.0148, "WTA125": 0.022}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5746, "share_primary_cause_market_settled_or_in_play": 0.4843, "share_primary_cause_stale_quote_only": 0.1814}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 5353, "identity_ambiguous_share": 0.1601, "ticker_orientation": {"VERIFIED": 5353}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 3134, "with_external": 48, "coverage": 0.0153, "external_status": {"EXTERNAL_STALE": 39, "AGREES_WITH_KALSHI": 9}, "triangulation": {"INSUFFICIENT_INPUTS": 39, "MODEL_LONE_OUTLIER": 9}, "share_external_agrees_with_kalshi": 0.1875, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 1380, "with_external": 47, "coverage": 0.0341, "external_status": {"EXTERNAL_STALE": 38, "AGREES_WITH_KALSHI": 9}, "triangulation": {"INSUFFICIENT_INPUTS": 38, "MODEL_LONE_OUTLIER": 9}, "share_external_agrees_with_kalshi": 0.1915, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 605.0, "median_sample_ratio": 2.35, "median_min_matches": 19.0, "median_max_days_since_last": 197.0, "share_severe_asymmetry": 0.1814, "data_status": {"POOR": 2843, "LIMITED": 1542, "ADEQUATE": 968}, "comparison_lt_10pp": {"median_thinner_serve_points": 1701.0, "median_sample_ratio": 1.77, "median_min_matches": 70.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 377, "model_minus_observed": 0.0704, "kalshi_minus_observed": -0.0617, "brier_diff_model_minus_kalshi": 0.0025}, "4-10x": {"n": 278, "model_minus_observed": 0.052, "kalshi_minus_observed": -0.0895, "brier_diff_model_minus_kalshi": -0.006}, "<2x": {"n": 793, "model_minus_observed": 0.0855, "kalshi_minus_observed": -0.042, "brier_diff_model_minus_kalshi": 0.0107}, ">=10x": {"n": 258, "model_minus_observed": 0.1012, "kalshi_minus_observed": -0.0741, "brier_diff_model_minus_kalshi": 0.013}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 1706, "model": {"intercept": -0.579, "slope": 0.912, "slope_se": 0.062}, "kalshi_mid_same_rows": {"intercept": 0.236, "slope": 1.144, "slope_se": 0.071}, "mean_extremity_model": 0.1864, "mean_extremity_kalshi": 0.1659, "model_brier": 0.2264, "kalshi_brier": 0.2014, "brier_diff_model_minus_kalshi": 0.025, "brier_diff_se": 0.0046, "model_logloss": 0.6469, "kalshi_logloss": 0.5852}, "fair_v1": {"n": 1706, "model": {"intercept": -0.415, "slope": 1.134, "slope_se": 0.071}, "kalshi_mid_same_rows": {"intercept": 0.357, "slope": 1.217, "slope_se": 0.073}, "mean_extremity_model": 0.1693, "mean_extremity_kalshi": 0.1664, "model_brier": 0.2079, "kalshi_brier": 0.2014, "brier_diff_model_minus_kalshi": 0.0065, "brier_diff_se": 0.0037, "model_logloss": 0.6016, "kalshi_logloss": 0.5849}, "gen1_elo": {"n": 1706, "model": {"intercept": -0.382, "slope": 1.111, "slope_se": 0.069}, "kalshi_mid_same_rows": {"intercept": 0.364, "slope": 1.202, "slope_se": 0.072}, "mean_extremity_model": 0.1731, "mean_extremity_kalshi": 0.1669, "model_brier": 0.2068, "kalshi_brier": 0.2014, "brier_diff_model_minus_kalshi": 0.0054, "brier_diff_se": 0.0037, "model_logloss": 0.6005, "kalshi_logloss": 0.585}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2535, "share_ge_15": 0.4389, "median_abs_gap": 13.05, "n": 12361}, "gen1_elo": {"share_ge_25": 0.2435, "share_ge_15": 0.4373, "median_abs_gap": 12.65, "n": 12361}, "gen1_sr": {"share_ge_25": 0.3056, "share_ge_15": 0.5212, "median_abs_gap": 15.76, "n": 12361}, "gen2": {"share_ge_25": 0.3092, "share_ge_15": 0.5082, "median_abs_gap": 15.4, "n": 12361}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1474, "share_ge_15": 0.3389, "median_abs_gap": 10.46, "n": 9362}, "gen1_elo": {"share_ge_25": 0.1418, "share_ge_15": 0.3345, "median_abs_gap": 10.03, "n": 9361}, "gen1_sr": {"share_ge_25": 0.2012, "share_ge_15": 0.4315, "median_abs_gap": 12.89, "n": 9362}, "gen2": {"share_ge_25": 0.2192, "share_ge_15": 0.4296, "median_abs_gap": 12.71, "n": 9363}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.72, "share_ge_25_all": 0.0179, "share_ge_25_pregame_clean": 0.0182}, "WTA": {"median_abs_gap_pregame_clean": 8.28, "share_ge_25_all": 0.0816, "share_ge_25_pregame_clean": 0.0706}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2333, "share_within_10pp_all": 0.4322, "share_within_10pp_pregame_clean": 0.4968, "corr_model_vs_mid_pregame_clean": 0.8519}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 247, "model_brier": 0.1792, "kalshi_brier": 0.1803, "brier_diff_model_minus_kalshi": -0.0011}, "10-15": {"n_settled": 298, "model_brier": 0.22, "kalshi_brier": 0.2177, "brier_diff_model_minus_kalshi": 0.0023}, "15-25": {"n_settled": 371, "model_brier": 0.2203, "kalshi_brier": 0.211, "brier_diff_model_minus_kalshi": 0.0093}, "25-40": {"n_settled": 218, "model_brier": 0.2161, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0122}, "3-5": {"n_settled": 170, "model_brier": 0.1848, "kalshi_brier": 0.1851, "brier_diff_model_minus_kalshi": -0.0003}, "40+": {"n_settled": 49, "model_brier": 0.2835, "kalshi_brier": 0.1763, "brier_diff_model_minus_kalshi": 0.1072}, "5-10": {"n_settled": 353, "model_brier": 0.2004, "kalshi_brier": 0.2019, "brier_diff_model_minus_kalshi": -0.0016}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%)
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap).
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 194, "model_brier": 0.3105, "kalshi_brier": 0.2241, "brier_diff_model_minus_kalshi": 0.0864, "brier_diff_se": 0.0227, "corr_model_outcome": 0.0137, "corr_kalshi_outcome": 0.3509}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
