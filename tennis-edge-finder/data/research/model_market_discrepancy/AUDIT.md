# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-08T23:45Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 25,561): 0-3 14.0%, 3-5 9.6%, 5-10 19.8%, 10-15 15.4%, 15-25 18.6%, 25-40 14.1%, 40+ 8.5%; median gap 12.04 pp.
* **Where the extremes live**: 98.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.2%, Challenger 12.3%, doubles 6.4%). Main tour: ATP 1.7% and WTA 8.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 5,774): MARKET_ALREADY_SETTLED_WHEN_PRICED 39.8%, STALE_QUOTE 17.2%, BOOK_QUALITY 16.9%, POOR_DATA 7.9%, POSSIBLY_IN_PLAY_QUOTE 5.5%, LIMITED_DATA 4.2%, IN_PLAY_QUOTE 3.5%, IDENTITY_AMBIGUOUS 3.0%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.2%. By class: coverage 39.8%, market_freshness 17.2%, execution 16.9%, data 12.1%, market_freshness/coverage 9.0%, mapping 3.0%, model_calibration_or_unknown 1.9%, model_calibration 0.2%.
* **Stale / settled / in-play**: 56.0% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 48.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 5,774 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 16.8% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 1.9%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 14.1% of the time and with the model 0.3%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 620.0 points vs 1754.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.106, Gen-2 0.884, Gen-1 ledger 0.927 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 241 model 0.2178 vs Kalshi 0.2014; n 52 model 0.282 vs Kalshi 0.1791.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 96,897 model-market comparisons (162,156 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 36,501 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-08T23:39:50.203799+00:00'], shadow board 26,764 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-08T23:39:53.466461+00:00'], Model 4 10,030 rows, 11,176 settled tickers, 3,001 tickers with an external scan.
* By model: {"gen1_ledger": 23332, "gen1_elo": 13449, "fair_v1": 13449, "gen2": 13449, "gen1_sr": 13449, "model4_fundamental": 9889, "model4_conditioned": 9880}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 25,561 | 14.0 | 9.6 | 19.8 | 15.4 | 18.6 | 14.1 | 8.5 | 12.04 | 41.2% | 22.6% |
| MW fair_v1 | 13,449 | 13.3 | 8.7 | 18.2 | 16.2 | 18.4 | 14.9 | 10.2 | 12.99 | 43.6% | 25.2% |
| MW gen1_elo | 13,449 | 12.8 | 8.8 | 19.9 | 15.0 | 19.2 | 14.6 | 9.7 | 12.56 | 43.5% | 24.3% |
| MW gen1_ledger | 12,112 | 14.8 | 10.5 | 21.5 | 14.6 | 18.8 | 13.1 | 6.6 | 10.89 | 38.5% | 19.7% |
| MW gen1_sr | 13,449 | 10.2 | 7.8 | 16.1 | 14.0 | 21.4 | 18.5 | 11.9 | 15.64 | 51.9% | 30.5% |
| MW gen2 | 13,449 | 12.0 | 7.1 | 16.1 | 14.3 | 19.6 | 17.4 | 13.4 | 15.25 | 50.4% | 30.8% |
| all families model4_conditioned | 9,880 | 22.1 | 20.4 | 35.6 | 16.0 | 4.2 | 0.9 | 0.8 | 5.7 | 5.9% | 1.7% |
| all families model4_fundamental | 9,889 | 16.5 | 13.2 | 35.1 | 20.4 | 10.8 | 2.8 | 1.1 | 7.72 | 14.8% | 3.9% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.6%, >=15pp 41.2%, >=20pp 30.9%, >=25pp 22.6%, >=30pp 16.6%, >=40pp 8.5%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.53pp; >=10pp 45.8%, >=25pp 18.2%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 994 | 27.8 | 15.2 | 24.4 | 17.8 | 12.5 | 1.3 | 1.1 | 5.98 | 14.9% | 2.4% |
| CHALLENGER | 2,278 | 15.4 | 10.8 | 18.5 | 16.1 | 13.0 | 13.1 | 13.1 | 11.95 | 39.2% | 26.2% |
| ITF_MEN | 3,891 | 11.0 | 8.6 | 18.5 | 14.9 | 19.3 | 15.1 | 12.6 | 13.84 | 47.0% | 27.7% |
| ITF_WOMEN | 5,417 | 10.3 | 6.7 | 15.9 | 16.3 | 21.6 | 18.8 | 10.4 | 15.33 | 50.8% | 29.2% |
| WTA | 544 | 24.3 | 9.4 | 25.4 | 16.0 | 16.9 | 6.1 | 2.0 | 7.92 | 25.0% | 8.1% |
| WTA125 | 325 | 12.0 | 6.5 | 21.9 | 26.1 | 14.8 | 16.3 | 2.5 | 11.33 | 33.5% | 18.8% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 994 | 22.6 | 13.9 | 24.6 | 18.5 | 16.9 | 2.2 | 1.3 | 6.9 | 20.4% | 3.5% |
| CHALLENGER | 2,278 | 15.2 | 7.5 | 17.9 | 13.5 | 18.0 | 14.5 | 13.4 | 13.15 | 45.9% | 27.9% |
| ITF_MEN | 3,891 | 10.6 | 7.3 | 16.8 | 14.7 | 19.8 | 17.4 | 13.2 | 15.3 | 50.5% | 30.6% |
| ITF_WOMEN | 5,417 | 9.1 | 5.9 | 13.0 | 13.1 | 20.4 | 21.3 | 17.1 | 18.91 | 58.8% | 38.4% |
| WTA | 544 | 22.4 | 5.3 | 18.6 | 14.9 | 20.8 | 16.0 | 2.0 | 11.93 | 38.8% | 18.0% |
| WTA125 | 325 | 4.6 | 2.8 | 17.2 | 21.5 | 21.2 | 20.9 | 11.7 | 17.19 | 53.8% | 32.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 994 | 25.9 | 13.2 | 29.6 | 15.8 | 11.3 | 3.1 | 1.2 | 6.53 | 15.6% | 4.3% |
| CHALLENGER | 2,278 | 15.9 | 10.6 | 19.8 | 14.2 | 14.1 | 12.3 | 13.0 | 11.01 | 39.4% | 25.3% |
| ITF_MEN | 3,891 | 10.1 | 8.8 | 18.5 | 14.1 | 20.3 | 15.6 | 12.6 | 14.19 | 48.5% | 28.2% |
| ITF_WOMEN | 5,417 | 9.5 | 6.7 | 16.9 | 15.8 | 23.2 | 18.7 | 9.2 | 15.51 | 51.1% | 27.9% |
| WTA | 544 | 23.2 | 12.9 | 35.7 | 14.3 | 9.2 | 3.5 | 1.3 | 6.92 | 14.0% | 4.8% |
| WTA125 | 325 | 20.9 | 11.7 | 30.1 | 17.2 | 14.5 | 4.9 | 0.6 | 7.99 | 20.0% | 5.5% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 522 | 28.7 | 22.6 | 37.0 | 10.2 | 1.3 | 0.2 | 0.0 | 4.85 | 1.5% | 0.2% |
| CHALLENGER | 1,471 | 23.2 | 17.3 | 25.7 | 14.0 | 12.3 | 5.5 | 2.0 | 6.61 | 19.9% | 7.5% |
| DOUBLES | 740 | 3.9 | 3.4 | 10.9 | 11.1 | 20.4 | 25.0 | 25.3 | 25.33 | 70.7% | 50.3% |
| ITF_MEN | 3,810 | 14.6 | 8.6 | 20.8 | 15.1 | 20.3 | 12.7 | 7.9 | 11.86 | 40.9% | 20.6% |
| ITF_WOMEN | 4,482 | 11.6 | 9.4 | 19.8 | 14.4 | 22.2 | 16.9 | 5.8 | 13.06 | 44.9% | 22.7% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 443 | 21.0 | 11.5 | 25.5 | 18.7 | 15.3 | 7.2 | 0.7 | 8.44 | 23.2% | 7.9% |
| WTA125 | 495 | 16.6 | 12.5 | 22.4 | 20.0 | 16.8 | 8.9 | 2.8 | 9.54 | 28.5% | 11.7% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 989 | 27.8 | 15.1 | 24.4 | 17.9 | 12.4 | 1.3 | 1.1 | 6.01 | 14.9% | 2.4% |
| CHALLENGER | 1,597 | 20.4 | 13.8 | 23.9 | 19.1 | 13.3 | 6.6 | 2.8 | 8.03 | 22.8% | 9.5% |
| ITF_MEN | 2,756 | 13.6 | 10.9 | 22.0 | 16.7 | 19.3 | 12.2 | 5.3 | 10.98 | 36.8% | 17.4% |
| ITF_WOMEN | 3,840 | 12.9 | 8.4 | 18.8 | 18.7 | 23.1 | 15.0 | 3.1 | 12.61 | 41.2% | 18.1% |
| WTA | 541 | 24.2 | 9.4 | 25.5 | 15.9 | 17.0 | 5.9 | 2.0 | 7.89 | 24.9% | 8.0% |
| WTA125 | 312 | 12.5 | 6.7 | 21.1 | 26.6 | 15.1 | 16.4 | 1.6 | 11.33 | 33.0% | 17.9% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 989 | 22.6 | 13.8 | 24.7 | 18.5 | 16.9 | 2.2 | 1.3 | 6.9 | 20.4% | 3.5% |
| CHALLENGER | 1,597 | 20.2 | 9.9 | 22.7 | 16.5 | 18.4 | 9.6 | 2.7 | 9.08 | 30.8% | 12.3% |
| ITF_MEN | 2,757 | 12.7 | 8.9 | 19.5 | 16.6 | 21.2 | 15.1 | 6.1 | 12.49 | 42.3% | 21.1% |
| ITF_WOMEN | 3,840 | 10.7 | 7.1 | 14.7 | 14.3 | 22.8 | 20.3 | 10.1 | 16.2 | 53.2% | 30.4% |
| WTA | 541 | 22.4 | 5.4 | 18.7 | 15.0 | 20.7 | 15.9 | 2.0 | 11.75 | 38.6% | 17.9% |
| WTA125 | 312 | 4.8 | 2.9 | 17.3 | 22.4 | 20.5 | 21.5 | 10.6 | 16.74 | 52.6% | 32.0% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 507 | 29.0 | 22.9 | 37.1 | 10.3 | 0.6 | 0.2 | 0.0 | 4.83 | 0.8% | 0.2% |
| CHALLENGER | 1,241 | 25.3 | 19.6 | 27.9 | 13.7 | 11.4 | 2.1 | 0.1 | 5.83 | 13.5% | 2.2% |
| DOUBLES | 680 | 3.8 | 3.4 | 11.2 | 11.0 | 20.7 | 24.7 | 25.1 | 24.7 | 70.6% | 49.9% |
| ITF_MEN | 3,053 | 16.3 | 9.6 | 23.2 | 16.1 | 20.1 | 10.2 | 4.5 | 10.21 | 34.8% | 14.8% |
| ITF_WOMEN | 3,630 | 12.9 | 10.2 | 21.7 | 15.3 | 22.4 | 15.0 | 2.5 | 11.42 | 39.9% | 17.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 413 | 21.6 | 12.1 | 26.1 | 18.9 | 15.7 | 5.6 | 0.0 | 8.33 | 21.3% | 5.6% |
| WTA125 | 410 | 18.5 | 13.9 | 24.9 | 22.9 | 14.9 | 4.6 | 0.2 | 8.29 | 19.8% | 4.9% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 740 | 3.9 | 3.4 | 10.9 | 11.1 | 20.4 | 25.0 | 25.3 | 25.33 | 70.7% | 50.3% |
| singles | 11,372 | 15.6 | 11.0 | 22.2 | 14.8 | 18.7 | 12.3 | 5.4 | 10.29 | 36.4% | 17.8% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 3,119 | 13.3 | 9.5 | 20.3 | 15.6 | 16.0 | 14.6 | 10.6 | 12.22 | 41.3% | 25.2% |
| Hard | 9,004 | 13.5 | 8.5 | 18.1 | 16.2 | 19.0 | 14.7 | 10.1 | 13.02 | 43.8% | 24.8% |
| UNKNOWN | 1,326 | 11.7 | 8.0 | 14.6 | 17.9 | 20.4 | 17.0 | 10.3 | 14.16 | 47.7% | 27.4% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,874 | 19.3 | 10.7 | 20.2 | 17.1 | 14.7 | 9.7 | 8.3 | 9.98 | 32.7% | 18.0% |
| B | 1,776 | 15.0 | 9.3 | 19.6 | 17.6 | 16.6 | 11.9 | 10.0 | 11.31 | 38.5% | 21.9% |
| C | 2,085 | 12.3 | 10.1 | 19.6 | 15.4 | 18.5 | 14.6 | 9.6 | 12.69 | 42.6% | 24.2% |
| D | 2,568 | 11.0 | 8.3 | 17.2 | 16.3 | 22.0 | 15.2 | 10.0 | 14.07 | 47.2% | 25.1% |
| F | 3,146 | 7.4 | 5.1 | 15.0 | 14.8 | 21.1 | 23.1 | 13.5 | 18.43 | 57.7% | 36.5% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,323 | 21.7 | 15.6 | 27.5 | 15.7 | 12.3 | 5.2 | 2.0 | 7.03 | 19.5% | 7.2% |
| B | 1,906 | 14.4 | 9.8 | 24.7 | 16.3 | 18.4 | 11.7 | 4.8 | 10.34 | 34.8% | 16.4% |
| C | 2,471 | 12.0 | 8.1 | 18.3 | 14.0 | 20.8 | 15.9 | 10.9 | 13.75 | 47.6% | 26.8% |
| D | 2,027 | 14.0 | 9.1 | 21.2 | 13.0 | 22.0 | 14.3 | 6.4 | 12.09 | 42.7% | 20.7% |
| F | 2,385 | 9.3 | 7.9 | 14.3 | 13.6 | 23.4 | 21.4 | 10.2 | 16.88 | 55.0% | 31.7% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 4,401 | 17.9 | 9.9 | 19.4 | 17.3 | 15.1 | 10.1 | 10.3 | 10.73 | 35.5% | 20.4% |
| LIMITED | 3,293 | 14.4 | 10.5 | 20.7 | 16.0 | 17.5 | 13.4 | 7.3 | 11.32 | 38.3% | 20.8% |
| POOR | 5,755 | 9.1 | 6.6 | 15.9 | 15.5 | 21.6 | 19.4 | 11.9 | 16.13 | 52.8% | 31.3% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,172 | 30.0 | 25.2 | 37.3 | 5.6 | 1.6 | 0.3 | 0.0 | 4.56 | 1.9% | 0.3% |
| GAME_SPREAD | 2,100 | 24.9 | 15.4 | 36.8 | 18.0 | 4.6 | 0.2 | 0.1 | 6.18 | 5.0% | 0.4% |
| MATCH_WINNER | 12,112 | 14.8 | 10.5 | 21.5 | 14.6 | 18.8 | 13.1 | 6.6 | 10.89 | 38.5% | 19.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 3,854 | 30.8 | 19.9 | 30.6 | 10.5 | 6.6 | 1.3 | 0.3 | 4.9 | 8.2% | 1.6% |
| TOTAL_GAMES | 3,070 | 7.2 | 9.0 | 38.6 | 30.6 | 9.4 | 3.1 | 2.1 | 9.45 | 14.7% | 5.2% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,672 | 24.4 | 38.7 | 30.9 | 0.3 | 5.1 | 0.6 | 0.2 | 4.34 | 5.8% | 0.7% |
| GAME_SPREAD | 2,544 | 46.1 | 14.2 | 29.1 | 8.2 | 1.2 | 0.8 | 0.3 | 3.54 | 2.3% | 1.1% |
| TOTAL_GAMES | 3,664 | 3.3 | 6.4 | 44.8 | 37.1 | 5.4 | 1.3 | 1.8 | 9.59 | 8.5% | 3.1% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,672 | 25.5 | 18.2 | 36.1 | 9.8 | 7.2 | 2.8 | 0.4 | 5.63 | 10.3% | 3.2% |
| GAME_SPREAD | 2,544 | 18.8 | 13.0 | 27.3 | 22.7 | 14.7 | 2.8 | 0.7 | 8.34 | 18.2% | 3.5% |
| TOTAL_GAMES | 3,673 | 6.0 | 8.3 | 39.6 | 29.2 | 11.9 | 2.9 | 2.1 | 9.59 | 16.9% | 5.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 13,449 | 43.6% | 25.2% | 12.99 | 33.3% | 14.5% | 10.39 |
| gen1_elo | 13,449 | 43.5% | 24.3% | 12.56 | 32.9% | 14.0% | 9.95 |
| gen1_sr | 13,449 | 51.9% | 30.5% | 15.64 | 42.7% | 19.9% | 12.72 |
| gen2 | 13,449 | 50.4% | 30.8% | 15.25 | 42.6% | 21.7% | 12.61 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 6,693 | 16.1 | 11.0 | 21.4 | 17.6 | 18.5 | 11.8 | 3.5 | 10.38 | 33.8% | 15.3% |
| STALE | 6,756 | 10.4 | 6.3 | 15.2 | 14.8 | 18.3 | 18.0 | 16.9 | 16.86 | 53.3% | 34.9% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 5,580 | 16.9 | 11.7 | 23.6 | 14.3 | 16.9 | 11.9 | 4.7 | 9.39 | 33.5% | 16.6% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 25,561 | 5580 | 10165 | 9816 | 25.2 | 170.1 | 1400.4 |
| ge_15pp | 10,531 | 1868 | 3554 | 5109 | 29.1 | 459.5 | 1380.4 |
| ge_25pp | 5,774 | 928 | 1615 | 3231 | 37.9 | 574.8 | 1380.4 |
| lt_10pp | 11,085 | 2912 | 4882 | 3291 | 23.9 | 50.6 | 1230.8 |

Current slate `SL-20261008T234509Z-b3a325a0`: 634 priced rows, quote age at build {'median': 5.7, 'max': 5.7}, freshness {'FRESH': 634}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 4 | 0.0 | 0.0 | 25.0 | 0.0 | 75.0 | 0.0 | 0.0 | 20.45 | 75.0% | 0.0% |
| EXTERNAL_LONE_OUTLIER | 3 | 33.3 | 66.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 3.05 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 690 | 24.4 | 11.4 | 20.9 | 20.6 | 15.1 | 7.2 | 0.4 | 8.02 | 22.8% | 7.7% |
| MARKETS_AGREE | 74 | 78.4 | 21.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.99 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 127 | 0.0 | 3.1 | 32.3 | 34.6 | 20.5 | 9.4 | 0.0 | 11.81 | 29.9% | 9.4% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 13,449 | 898 (6.7%) | 14.1% | 0.3% | {"EXTERNAL_STALE": 690, "AGREES_WITH_KALSHI": 127, "ALL_AGREE": 74, "SUPPORTS_MODEL_DIRECTION": 3, "EXTERNAL_OUTLIER": 3, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 5,864 | 198 (3.4%) | 19.2% | 1.5% | {"EXTERNAL_STALE": 157, "AGREES_WITH_KALSHI": 38, "SUPPORTS_MODEL_DIRECTION": 3} |
| fair_v1_ge_25pp | 3,384 | 65 (1.9%) | 18.5% | 0.0% | {"EXTERNAL_STALE": 53, "AGREES_WITH_KALSHI": 12} |
| fair_v1_ge_25pp_pregame_clean | 1,451 | 63 (4.3%) | 19.1% | 0.0% | {"EXTERNAL_STALE": 51, "AGREES_WITH_KALSHI": 12} |
| fair_v1_lt_10pp | 5,404 | 514 (9.5%) | 8.8% | 0.0% | {"EXTERNAL_STALE": 391, "ALL_AGREE": 74, "AGREES_WITH_KALSHI": 45, "EXTERNAL_OUTLIER": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 2,760 | 11.5 | 8.4 | 19.6 | 15.5 | 21.1 | 14.0 | 9.9 | 13.12 | 45.0% | 23.9% |
| 4-10x | 1,918 | 11.3 | 9.2 | 18.4 | 15.1 | 20.1 | 16.8 | 9.2 | 13.67 | 46.1% | 26.1% |
| <2x | 7,042 | 15.2 | 9.2 | 18.3 | 17.2 | 16.6 | 13.3 | 10.1 | 12.11 | 40.1% | 23.4% |
| >=10x | 1,729 | 10.3 | 6.4 | 15.7 | 14.5 | 19.8 | 20.6 | 12.6 | 16.48 | 53.0% | 33.3% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 3,486 | 14.1 | 8.6 | 19.5 | 16.0 | 17.8 | 12.9 | 11.1 | 12.2 | 41.8% | 24.1% |
| 300-1000 | 3,331 | 11.8 | 9.1 | 16.5 | 16.4 | 20.9 | 16.1 | 9.2 | 13.81 | 46.2% | 25.3% |
| <300 | 3,633 | 8.0 | 6.0 | 15.8 | 14.9 | 21.1 | 21.1 | 13.1 | 17.2 | 55.3% | 34.2% |
| >=3000 | 2,999 | 20.4 | 11.5 | 21.6 | 17.9 | 13.3 | 8.3 | 7.0 | 9.03 | 28.6% | 15.3% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 430 | 0.5406 | 0.4098 | 0.4884 | +0.052 | -0.079 | 0.0006 ± 0.007 |
| ratio 4-10x | 303 | 0.5828 | 0.4409 | 0.5215 | +0.061 | -0.081 | -0.0016 ± 0.009 |
| ratio <2x | 915 | 0.5436 | 0.4185 | 0.459 | +0.085 | -0.041 | 0.0112 ± 0.0048 |
| ratio >=10x | 292 | 0.5481 | 0.3781 | 0.4384 | +0.110 | -0.060 | 0.0135 ± 0.0103 |
| thinner_sample 1000-3000 | 524 | 0.5474 | 0.4229 | 0.4695 | +0.078 | -0.047 | 0.0052 ± 0.0062 |
| thinner_sample 300-1000 | 533 | 0.5696 | 0.4298 | 0.4991 | +0.070 | -0.069 | 0.001 ± 0.0068 |
| thinner_sample <300 | 594 | 0.5429 | 0.3821 | 0.463 | +0.080 | -0.081 | 0.0089 ± 0.0069 |
| thinner_sample >=3000 | 289 | 0.5316 | 0.4342 | 0.4464 | +0.085 | -0.012 | 0.0192 ± 0.0068 |
| data_status ADEQUATE | 505 | 0.5302 | 0.4254 | 0.4436 | +0.087 | -0.018 | 0.0128 ± 0.0055 |
| data_status LIMITED | 499 | 0.5646 | 0.4321 | 0.499 | +0.066 | -0.067 | 0.0001 ± 0.0068 |
| data_status POOR | 936 | 0.5524 | 0.3982 | 0.4733 | +0.079 | -0.075 | 0.008 ± 0.0054 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 292 | 0.1862 | 0.1875 | -0.0013 ± 0.0009 | 0.5482 | 0.5515 | 0.4917 | 0.4771 | 0.5171 | -0.069 ± 0.0266 | -0.01 (3) |
| 3-5 | 197 | 0.1865 | 0.1874 | -0.0009 ± 0.0025 | 0.5522 | 0.5522 | 0.5145 | 0.4745 | 0.5025 | -0.070 ± 0.0313 | 0.02 (1) |
| 5-10 | 398 | 0.2012 | 0.2034 | -0.0022 ± 0.0034 | 0.5891 | 0.5941 | 0.5217 | 0.4477 | 0.4899 | -0.087 ± 0.0236 | -0.0125 (4) |
| 10-15 | 344 | 0.2117 | 0.2059 | +0.0058 ± 0.0061 | 0.6099 | 0.5919 | 0.5233 | 0.3993 | 0.436 | -0.096 ± 0.0245 | -0.0633 (3) |
| 15-25 | 416 | 0.2227 | 0.2127 | +0.0100 ± 0.0088 | 0.637 | 0.6132 | 0.5736 | 0.378 | 0.4495 | -0.082 ± 0.0226 | -0.0133 (6) |
| 25-40 | 241 | 0.2178 | 0.2014 | +0.0165 ± 0.0171 | 0.6251 | 0.5779 | 0.6465 | 0.3375 | 0.4647 | -0.071 ± 0.0257 | -0.01 (1) |
| 40+ | 52 | 0.282 | 0.1791 | +0.1028 ± 0.0518 | 0.7673 | 0.5347 | 0.7592 | 0.3118 | 0.4231 | -0.120 ± 0.0507 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1436 | 0.1674 | 0.1682 | -0.0008 ± 0.0004 | 0.5034 | 0.5042 | 0.4725 | 0.4577 | 0.4937 | -0.027 ± 0.011 | -0.0188 (8) |
| 3-5 | 956 | 0.191 | 0.1872 | +0.0039 ± 0.0011 | 0.563 | 0.548 | 0.479 | 0.4394 | 0.4069 | -0.093 ± 0.0142 | 0.02 (1) |
| 5-10 | 2035 | 0.1931 | 0.191 | +0.0021 ± 0.0014 | 0.569 | 0.5619 | 0.4921 | 0.4183 | 0.4359 | -0.054 ± 0.0098 | -0.0082 (17) |
| 10-15 | 1846 | 0.1969 | 0.1798 | +0.0171 ± 0.0025 | 0.5776 | 0.529 | 0.4719 | 0.3474 | 0.3413 | -0.077 ± 0.0098 | -0.0475 (4) |
| 15-25 | 2171 | 0.2 | 0.1638 | +0.0362 ± 0.0034 | 0.5893 | 0.4883 | 0.489 | 0.293 | 0.2994 | -0.070 ± 0.0087 | -0.0048 (29) |
| 25-40 | 1834 | 0.2164 | 0.1236 | +0.0928 ± 0.0051 | 0.6249 | 0.3826 | 0.5268 | 0.2133 | 0.2246 | -0.059 ± 0.0079 | -0.01 (1) |
| 40+ | 1264 | 0.3698 | 0.0454 | +0.3244 ± 0.0066 | 0.9646 | 0.1779 | 0.6221 | 0.1061 | 0.0601 | -0.082 ± 0.0056 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 228 | 0.1954 | 0.1956 | -0.0003 ± 0.001 | 0.5743 | 0.5752 | 0.4903 | 0.4751 | 0.4781 | -0.103 ± 0.031 | -0.01 (1) |
| 3-5 | 149 | 0.2036 | 0.2049 | -0.0014 ± 0.003 | 0.586 | 0.5915 | 0.52 | 0.48 | 0.5101 | -0.060 ± 0.039 | 0.02 (1) |
| 5-10 | 334 | 0.1928 | 0.1898 | +0.0030 ± 0.0036 | 0.5674 | 0.5607 | 0.5674 | 0.4924 | 0.506 | -0.100 ± 0.0247 | -0.01 (4) |
| 10-15 | 331 | 0.2158 | 0.2092 | +0.0066 ± 0.0063 | 0.6175 | 0.6043 | 0.5821 | 0.4574 | 0.4985 | -0.098 ± 0.0261 | -0.05 (4) |
| 15-25 | 464 | 0.2248 | 0.207 | +0.0179 ± 0.0084 | 0.6385 | 0.5957 | 0.5995 | 0.4021 | 0.4612 | -0.098 ± 0.0217 | -0.01 (5) |
| 25-40 | 316 | 0.2704 | 0.2016 | +0.0688 ± 0.0159 | 0.7556 | 0.5836 | 0.6707 | 0.3571 | 0.4051 | -0.138 ± 0.0253 | -0.025 (2) |
| 40+ | 118 | 0.338 | 0.1877 | +0.1503 ± 0.0387 | 0.9519 | 0.5497 | 0.7622 | 0.2834 | 0.3814 | -0.064 ± 0.0369 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1304 | 0.1741 | 0.1748 | -0.0007 ± 0.0004 | 0.5207 | 0.5223 | 0.4919 | 0.4775 | 0.5023 | -0.034 ± 0.0121 | -0.0217 (6) |
| 3-5 | 802 | 0.1887 | 0.1859 | +0.0028 ± 0.0012 | 0.5492 | 0.5429 | 0.5211 | 0.4813 | 0.4663 | -0.069 ± 0.0154 | 0.02 (1) |
| 5-10 | 1789 | 0.1842 | 0.1801 | +0.0041 ± 0.0015 | 0.5497 | 0.5356 | 0.5192 | 0.4457 | 0.4561 | -0.057 ± 0.0102 | -0.01 (5) |
| 10-15 | 1622 | 0.1932 | 0.1794 | +0.0138 ± 0.0026 | 0.5716 | 0.5256 | 0.5162 | 0.3918 | 0.4014 | -0.066 ± 0.0107 | -0.02 (14) |
| 15-25 | 2264 | 0.2142 | 0.1726 | +0.0416 ± 0.0034 | 0.624 | 0.5109 | 0.529 | 0.3333 | 0.3277 | -0.085 ± 0.0088 | -0.0026 (27) |
| 25-40 | 2093 | 0.2471 | 0.1371 | +0.1100 ± 0.0052 | 0.7004 | 0.4183 | 0.561 | 0.2444 | 0.2303 | -0.087 ± 0.0081 | -0.015 (6) |
| 40+ | 1668 | 0.4023 | 0.0678 | +0.3345 ± 0.0073 | 1.0539 | 0.238 | 0.6688 | 0.1311 | 0.1025 | -0.070 ± 0.0062 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 297 | 0.1915 | 0.194 | -0.0026 ± 0.0009 | 0.5616 | 0.5687 | 0.4966 | 0.4813 | 0.5455 | -0.025 ± 0.0258 | -0.0133 (6) |
| 3-5 | 204 | 0.184 | 0.1826 | +0.0014 ± 0.0024 | 0.5429 | 0.5389 | 0.4991 | 0.4599 | 0.4657 | -0.119 ± 0.0317 | -0.01 (1) |
| 5-10 | 420 | 0.1977 | 0.1976 | +0.0000 ± 0.0033 | 0.5813 | 0.5795 | 0.5111 | 0.4373 | 0.469 | -0.089 ± 0.0227 | -0.01 (4) |
| 10-15 | 325 | 0.215 | 0.2138 | +0.0013 ± 0.0064 | 0.62 | 0.6115 | 0.5357 | 0.4126 | 0.4708 | -0.083 ± 0.0253 | -0.044 (5) |
| 15-25 | 406 | 0.2237 | 0.2067 | +0.0170 ± 0.0088 | 0.6436 | 0.5973 | 0.5802 | 0.3866 | 0.4384 | -0.102 ± 0.0223 | -0.03 (1) |
| 25-40 | 242 | 0.2011 | 0.2072 | -0.0062 ± 0.017 | 0.5854 | 0.5936 | 0.6542 | 0.3425 | 0.5041 | -0.046 ± 0.025 | 0.0 (1) |
| 40+ | 46 | 0.3062 | 0.1787 | +0.1275 ± 0.0561 | 0.8241 | 0.5334 | 0.752 | 0.2995 | 0.3913 | -0.131 ± 0.0563 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1362 | 0.1796 | 0.1805 | -0.0009 ± 0.0004 | 0.5326 | 0.5346 | 0.483 | 0.4678 | 0.4963 | -0.032 ± 0.0116 | -0.0183 (23) |
| 3-5 | 955 | 0.183 | 0.1804 | +0.0026 ± 0.0011 | 0.5407 | 0.5341 | 0.4689 | 0.4297 | 0.4157 | -0.084 ± 0.0143 | -0.0243 (7) |
| 5-10 | 2182 | 0.185 | 0.1803 | +0.0047 ± 0.0014 | 0.5513 | 0.5354 | 0.4808 | 0.4065 | 0.4129 | -0.060 ± 0.0092 | -0.01 (18) |
| 10-15 | 1729 | 0.1957 | 0.1795 | +0.0161 ± 0.0025 | 0.5756 | 0.5268 | 0.4885 | 0.365 | 0.3597 | -0.078 ± 0.0101 | -0.03 (9) |
| 15-25 | 2329 | 0.2025 | 0.1666 | +0.0360 ± 0.0033 | 0.597 | 0.4955 | 0.4929 | 0.2972 | 0.304 | -0.067 ± 0.0085 | -0.03 (2) |
| 25-40 | 1785 | 0.2119 | 0.1195 | +0.0924 ± 0.0052 | 0.6145 | 0.3708 | 0.5229 | 0.2054 | 0.2218 | -0.057 ± 0.0077 | 0.0 (1) |
| 40+ | 1200 | 0.3843 | 0.0469 | +0.3375 ± 0.007 | 1.0043 | 0.1825 | 0.6301 | 0.1072 | 0.0575 | -0.085 ± 0.006 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 582 | 0.2013 | 0.2014 | -0.0001 ± 0.0006 | 0.5853 | 0.5851 | 0.4997 | 0.4848 | 0.4863 | -0.048 ± 0.0185 | -0.0226 (46) |
| 3-5 | 435 | 0.195 | 0.1937 | +0.0013 ± 0.0017 | 0.5708 | 0.5661 | 0.4795 | 0.44 | 0.446 | -0.050 ± 0.0211 | -0.0058 (33) |
| 5-10 | 887 | 0.1914 | 0.1861 | +0.0053 ± 0.0022 | 0.567 | 0.5529 | 0.48 | 0.4065 | 0.4081 | -0.059 ± 0.0148 | -0.0049 (73) |
| 10-15 | 580 | 0.2041 | 0.1947 | +0.0095 ± 0.0046 | 0.5974 | 0.5709 | 0.4825 | 0.3596 | 0.381 | -0.043 ± 0.0182 | 0.0014 (64) |
| 15-25 | 781 | 0.2332 | 0.2079 | +0.0253 ± 0.0064 | 0.6605 | 0.6009 | 0.5476 | 0.3534 | 0.3867 | -0.056 ± 0.0164 | -0.0216 (58) |
| 25-40 | 442 | 0.2438 | 0.185 | +0.0588 ± 0.0127 | 0.6866 | 0.5434 | 0.626 | 0.3126 | 0.3733 | -0.072 ± 0.0191 | -0.0216 (25) |
| 40+ | 148 | 0.3468 | 0.1863 | +0.1605 ± 0.0359 | 0.987 | 0.5507 | 0.7778 | 0.2865 | 0.3919 | -0.057 ± 0.0323 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1721 | 0.1862 | 0.1862 | +0.0000 ± 0.0004 | 0.5474 | 0.5463 | 0.5006 | 0.4855 | 0.4863 | -0.043 ± 0.0103 | -0.0155 (82) |
| 3-5 | 1212 | 0.1862 | 0.1836 | +0.0026 ± 0.001 | 0.5465 | 0.5406 | 0.4904 | 0.4509 | 0.4414 | -0.057 ± 0.0123 | -0.0148 (63) |
| 5-10 | 2486 | 0.1901 | 0.1821 | +0.0080 ± 0.0013 | 0.5641 | 0.5413 | 0.4774 | 0.4036 | 0.3902 | -0.067 ± 0.0087 | -0.0087 (125) |
| 10-15 | 1701 | 0.1999 | 0.186 | +0.0140 ± 0.0026 | 0.5874 | 0.5499 | 0.4965 | 0.3734 | 0.3774 | -0.056 ± 0.0103 | -0.0053 (105) |
| 15-25 | 2199 | 0.2258 | 0.1952 | +0.0306 ± 0.0037 | 0.6504 | 0.5692 | 0.5416 | 0.3466 | 0.3661 | -0.057 ± 0.0095 | -0.0255 (106) |
| 25-40 | 1543 | 0.2386 | 0.16 | +0.0786 ± 0.0064 | 0.6762 | 0.4774 | 0.5885 | 0.2739 | 0.3085 | -0.059 ± 0.0099 | -0.0206 (47) |
| 40+ | 732 | 0.3629 | 0.1095 | +0.2534 ± 0.013 | 0.9965 | 0.3444 | 0.6812 | 0.1765 | 0.1899 | -0.065 ± 0.0113 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 1940 | 1.106 ± 0.065 | 1.201 | 0.1708 | 0.1695 | 0.2081 | 0.2009 |
| gen2 | 1940 | 0.884 ± 0.057 | 1.132 | 0.187 | 0.1689 | 0.227 | 0.2009 |
| gen1_elo | 1940 | 1.095 ± 0.064 | 1.192 | 0.1746 | 0.1701 | 0.2066 | 0.2009 |
| gen1_sr | 1940 | 1.093 ± 0.073 | 1.211 | 0.1446 | 0.1715 | 0.222 | 0.2006 |
| gen1_ledger | 3855 | 0.927 ± 0.042 | 1.082 | 0.1727 | 0.1912 | 0.2157 | 0.1949 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 10,531)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,926 | 27.8% |
| STALE_QUOTE | market_freshness | 2,216 | 21.0% |
| BOOK_QUALITY | execution | 1,843 | 17.5% |
| POOR_DATA | data | 1,105 | 10.5% |
| LIMITED_DATA | data | 749 | 7.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 579 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 458 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 322 | 3.1% |
| IDENTITY_AMBIGUOUS | mapping | 293 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 40 | 0.4% |

Cause class: coverage 27.8%, market_freshness 21.0%, data 17.6%, execution 17.5%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.3%, mapping 2.8%, model_calibration 0.4%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.4%, START_UNVERIFIABLE 96.2%, LOW_DATA_QUALITY 69.0%, THIN_PLAYER_HISTORY 57.5%, STALE_PLAYER_DATA 57.5%, STALE_KALSHI_QUOTE 48.5%, MODEL_INTERNAL_DISAGREEMENT 37.3%, ASYMMETRIC_SAMPLE_SIZE 30.8%, WIDE_SPREAD 23.6%, MODEL_HIGH_UNCERTAINTY 16.2%, PLAYER_IDENTITY_RISK 11.1%, LEVEL_TRANSFER_RISK 8.9%, EVENT_MAPPING_RISK 7.7%, LOW_DISPLAYED_LIQUIDITY 7.4%, MODEL_CALIBRATION_OUTLIER 3.2%, EXTERNAL_MARKET_REJECTION 0.6%, UNKNOWN 0.5%, EXTERNAL_MARKET_CONFIRMATION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 30.4%, POST_SETTLEMENT_OBSERVATION 27.8%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### >= ge_25 pp (N = 5,774)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,296 | 39.8% |
| STALE_QUOTE | market_freshness | 990 | 17.2% |
| BOOK_QUALITY | execution | 975 | 16.9% |
| POOR_DATA | data | 457 | 7.9% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 317 | 5.5% |
| LIMITED_DATA | data | 241 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 203 | 3.5% |
| IDENTITY_AMBIGUOUS | mapping | 176 | 3.0% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 108 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 11 | 0.2% |

Cause class: coverage 39.8%, market_freshness 17.2%, execution 16.9%, data 12.1%, market_freshness/coverage 9.0%, mapping 3.0%, model_calibration_or_unknown 1.9%, model_calibration 0.2%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.7%, START_UNVERIFIABLE 98.2%, LOW_DATA_QUALITY 71.7%, THIN_PLAYER_HISTORY 59.1%, STALE_KALSHI_QUOTE 56.0%, STALE_PLAYER_DATA 52.5%, MODEL_INTERNAL_DISAGREEMENT 38.7%, ASYMMETRIC_SAMPLE_SIZE 32.5%, WIDE_SPREAD 23.1%, MODEL_HIGH_UNCERTAINTY 17.6%, PLAYER_IDENTITY_RISK 13.9%, EVENT_MAPPING_RISK 9.3%, LOW_DISPLAYED_LIQUIDITY 7.7%, LEVEL_TRANSFER_RISK 7.5%, MODEL_CALIBRATION_OUTLIER 4.0%, EXTERNAL_MARKET_REJECTION 0.3%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 42.7%, POST_SETTLEMENT_OBSERVATION 39.8%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 4807, "IDENTITY_AMBIGUOUS": 967}; ticker orientation: {"VERIFIED": 5774}.

Checks: discipline:AMBIGUOUS 372, discipline:PASS 5402, identity_confidence:AMBIGUOUS 804, identity_confidence:PASS 4970, level_mapping:NA 384, level_mapping:PASS 5390, market_pair:AMBIGUOUS 220, market_pair:NA 130, market_pair:PASS 5424, model_complement:NA 97, model_complement:PASS 5677, namesake:PASS 5774, physical_match_id:NA 2390, physical_match_id:PASS 3384, player_ids:PASS 5774, same_pair_other_event:PASS 5774, ticker_orientation:PASS 5774

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,516 | 1.7% | 1.7% | 0.4% | {"market_freshness": 20, "execution": 5} | 5.43 | 0.2183 / 0.2094 (141) | 20.1% | 0.1% | 5.9% | 1.3% |
| CHALLENGER | 3,749 | 18.9% | 6.3% | 12.3% | {"coverage": 445, "market_freshness": 107, "market_freshness/coverage": 85, "model_calibration_or_unknown": 39, "data": 25, "execution": 4, "model_calibration": 3} | 6.78 | 0.2239 / 0.206 (894) | 46.2% | 4.8% | 1.7% | 24.3% |
| DOUBLES | 740 | 50.3% | 49.9% | 6.4% | {"execution": 142, "market_freshness": 106, "mapping": 91, "market_freshness/coverage": 26, "coverage": 7} | 24.7 | 0.3166 / 0.2266 (212) | 31.6% | 0.0% | 100.0% | 8.1% |
| ITF_MEN | 7,701 | 24.2% | 16.1% | 32.2% | {"coverage": 767, "execution": 383, "data": 266, "market_freshness": 264, "market_freshness/coverage": 162, "mapping": 19, "model_calibration_or_unknown": 1} | 10.61 | 0.2104 / 0.1924 (1927) | 38.8% | 54.7% | 6.2% | 24.6% |
| ITF_WOMEN | 9,899 | 26.2% | 17.8% | 45.0% | {"coverage": 1060, "market_freshness": 435, "execution": 424, "data": 383, "market_freshness/coverage": 206, "mapping": 60, "model_calibration_or_unknown": 22, "model_calibration": 7} | 12.11 | 0.2009 / 0.1922 (2145) | 40.0% | 58.1% | 9.8% | 24.5% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 987 | 8.0% | 6.9% | 1.4% | {"market_freshness": 34, "model_calibration_or_unknown": 16, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.09 | 0.2039 / 0.1997 (149) | 33.8% | 2.1% | 1.2% | 3.3% |
| WTA125 | 820 | 14.5% | 10.5% | 2.1% | {"market_freshness/coverage": 31, "model_calibration_or_unknown": 28, "market_freshness": 22, "data": 13, "coverage": 12, "execution": 8, "mapping": 4, "model_calibration": 1} | 9.98 | 0.2257 / 0.2107 (285) | 26.6% | 6.5% | 4.2% | 11.9% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 5 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 6 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 8 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 9 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 10 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 11 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 12 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 14 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 16 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 22.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1345 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 17 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 18 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 19 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 20 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 21 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 22 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 23 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 24 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 25 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 26 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 27 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 28 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 29 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 30 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 189 min (STALE); no external reference |
| 31 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 32 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 33 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 110 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 34 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 36 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 253 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 37 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 38 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 39 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 40 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 41 | `KXITFWMATCH-26OCT08ARISAV-SAV` | ITF_WOMEN | fair_v1 | 75% / 2% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 826 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 43 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 687 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 44 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 45 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 46 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 708 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 49 | `KXITFWMATCH-26OCT08YANZHE-YAN` | ITF_WOMEN | fair_v1 | 90% / 18% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 61 min before settlement (in-play print); quote age at model time 166 min (STALE); data LIMITED (grade C, thinner serve sample 1212.0, ratio 2.36); no external reference |
| 50 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.982, "by_level_share_of_ge_25pp": {"ATP": 0.0043, "CHALLENGER": 0.1226, "DOUBLES": 0.0644, "ITF_MEN": 0.3225, "ITF_WOMEN": 0.4498, "OTHER": 0.0021, "WTA": 0.0137, "WTA125": 0.0206}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5596, "share_primary_cause_market_settled_or_in_play": 0.4877, "share_primary_cause_stale_quote_only": 0.1715}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 5774, "identity_ambiguous_share": 0.1675, "ticker_orientation": {"VERIFIED": 5774}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 3384, "with_external": 65, "coverage": 0.0192, "external_status": {"EXTERNAL_STALE": 53, "AGREES_WITH_KALSHI": 12}, "triangulation": {"INSUFFICIENT_INPUTS": 53, "MODEL_LONE_OUTLIER": 12}, "share_external_agrees_with_kalshi": 0.1846, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 1451, "with_external": 63, "coverage": 0.0434, "external_status": {"EXTERNAL_STALE": 51, "AGREES_WITH_KALSHI": 12}, "triangulation": {"INSUFFICIENT_INPUTS": 51, "MODEL_LONE_OUTLIER": 12}, "share_external_agrees_with_kalshi": 0.1905, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 620.0, "median_sample_ratio": 2.32, "median_min_matches": 20.0, "median_max_days_since_last": 197.0, "share_severe_asymmetry": 0.1749, "data_status": {"POOR": 2987, "LIMITED": 1741, "ADEQUATE": 1046}, "comparison_lt_10pp": {"median_thinner_serve_points": 1754.0, "median_sample_ratio": 1.75, "median_min_matches": 74.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 430, "model_minus_observed": 0.0522, "kalshi_minus_observed": -0.0786, "brier_diff_model_minus_kalshi": 0.0006}, "4-10x": {"n": 303, "model_minus_observed": 0.0613, "kalshi_minus_observed": -0.0805, "brier_diff_model_minus_kalshi": -0.0016}, "<2x": {"n": 915, "model_minus_observed": 0.0846, "kalshi_minus_observed": -0.0405, "brier_diff_model_minus_kalshi": 0.0112}, ">=10x": {"n": 292, "model_minus_observed": 0.1097, "kalshi_minus_observed": -0.0603, "brier_diff_model_minus_kalshi": 0.0135}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 1940, "model": {"intercept": -0.569, "slope": 0.884, "slope_se": 0.057}, "kalshi_mid_same_rows": {"intercept": 0.226, "slope": 1.132, "slope_se": 0.065}, "mean_extremity_model": 0.187, "mean_extremity_kalshi": 0.1689, "model_brier": 0.227, "kalshi_brier": 0.2009, "brier_diff_model_minus_kalshi": 0.0261, "brier_diff_se": 0.0043, "model_logloss": 0.6492, "kalshi_logloss": 0.5836}, "fair_v1": {"n": 1940, "model": {"intercept": -0.4, "slope": 1.106, "slope_se": 0.065}, "kalshi_mid_same_rows": {"intercept": 0.35, "slope": 1.201, "slope_se": 0.068}, "mean_extremity_model": 0.1708, "mean_extremity_kalshi": 0.1695, "model_brier": 0.2081, "kalshi_brier": 0.2009, "brier_diff_model_minus_kalshi": 0.0072, "brier_diff_se": 0.0034, "model_logloss": 0.6024, "kalshi_logloss": 0.5835}, "gen1_elo": {"n": 1940, "model": {"intercept": -0.374, "slope": 1.095, "slope_se": 0.064}, "kalshi_mid_same_rows": {"intercept": 0.358, "slope": 1.192, "slope_se": 0.067}, "mean_extremity_model": 0.1746, "mean_extremity_kalshi": 0.1701, "model_brier": 0.2066, "kalshi_brier": 0.2009, "brier_diff_model_minus_kalshi": 0.0058, "brier_diff_se": 0.0034, "model_logloss": 0.6, "kalshi_logloss": 0.5833}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2516, "share_ge_15": 0.436, "median_abs_gap": 12.99, "n": 13449}, "gen1_elo": {"share_ge_25": 0.2434, "share_ge_15": 0.4351, "median_abs_gap": 12.56, "n": 13449}, "gen1_sr": {"share_ge_25": 0.3049, "share_ge_15": 0.5191, "median_abs_gap": 15.64, "n": 13449}, "gen2": {"share_ge_25": 0.3084, "share_ge_15": 0.5045, "median_abs_gap": 15.25, "n": 13449}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1446, "share_ge_15": 0.3331, "median_abs_gap": 10.39, "n": 10035}, "gen1_elo": {"share_ge_25": 0.1401, "share_ge_15": 0.3291, "median_abs_gap": 9.95, "n": 10034}, "gen1_sr": {"share_ge_25": 0.1993, "share_ge_15": 0.4271, "median_abs_gap": 12.72, "n": 10035}, "gen2": {"share_ge_25": 0.217, "share_ge_15": 0.4259, "median_abs_gap": 12.61, "n": 10036}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.43, "share_ge_25_all": 0.0165, "share_ge_25_pregame_clean": 0.0167}, "WTA": {"median_abs_gap_pregame_clean": 8.09, "share_ge_25_all": 0.08, "share_ge_25_pregame_clean": 0.0692}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2357, "share_within_10pp_all": 0.4337, "share_within_10pp_pregame_clean": 0.4992, "corr_model_vs_mid_pregame_clean": 0.8512}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 292, "model_brier": 0.1862, "kalshi_brier": 0.1875, "brier_diff_model_minus_kalshi": -0.0013}, "10-15": {"n_settled": 344, "model_brier": 0.2117, "kalshi_brier": 0.2059, "brier_diff_model_minus_kalshi": 0.0058}, "15-25": {"n_settled": 416, "model_brier": 0.2227, "kalshi_brier": 0.2127, "brier_diff_model_minus_kalshi": 0.01}, "25-40": {"n_settled": 241, "model_brier": 0.2178, "kalshi_brier": 0.2014, "brier_diff_model_minus_kalshi": 0.0165}, "3-5": {"n_settled": 197, "model_brier": 0.1865, "kalshi_brier": 0.1874, "brier_diff_model_minus_kalshi": -0.0009}, "40+": {"n_settled": 52, "model_brier": 0.282, "kalshi_brier": 0.1791, "brier_diff_model_minus_kalshi": 0.1028}, "5-10": {"n_settled": 398, "model_brier": 0.2012, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": -0.0022}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.569, "slope": 0.884, "slope_se": 0.057}, "kalshi_slope": {"intercept": 0.226, "slope": 1.132, "slope_se": 0.065}, "n": 1940}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 212, "model_brier": 0.3166, "kalshi_brier": 0.2266, "brier_diff_model_minus_kalshi": 0.0901, "brier_diff_se": 0.0216, "corr_model_outcome": 0.0031, "corr_kalshi_outcome": 0.3253}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
