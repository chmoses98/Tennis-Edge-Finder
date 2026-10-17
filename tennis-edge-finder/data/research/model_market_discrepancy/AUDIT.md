# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-17T01:21Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 35,523): 0-3 14.5%, 3-5 9.5%, 5-10 20.0%, 10-15 15.2%, 15-25 18.9%, 25-40 13.6%, 40+ 8.3%; median gap 11.86 pp.
* **Where the extremes live**: 98.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.0%, Challenger 12.2%, doubles 6.7%). Main tour: ATP 1.5% and WTA 5.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 7,787): MARKET_ALREADY_SETTLED_WHEN_PRICED 36.7%, STALE_QUOTE 18.3%, BOOK_QUALITY 17.3%, POOR_DATA 8.3%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 4.0%, IN_PLAY_QUOTE 3.2%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.5%. By class: coverage 36.7%, market_freshness 18.3%, execution 17.3%, data 12.3%, market_freshness/coverage 8.7%, mapping 4.3%, model_calibration_or_unknown 2.0%, model_calibration 0.5%.
* **Stale / settled / in-play**: 54.0% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 45.4% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 7,787 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.9% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 3.8%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 22.0% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 562.0 points vs 1794.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.064, Gen-2 0.868, Gen-1 ledger 0.876 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 362 model 0.2244 vs Kalshi 0.2087; n 74 model 0.2888 vs Kalshi 0.1769.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 141,768 model-market comparisons (235,881 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 49,587 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-17T01:16:02.462328+00:00'], shadow board 39,515 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-17T01:16:04.612136+00:00'], Model 4 14,977 rows, 14,967 settled tickers, 5,164 tickers with an external scan.
* By model: {"gen1_ledger": 32759, "gen1_elo": 19871, "fair_v1": 19871, "gen2": 19871, "gen1_sr": 19871, "model4_fundamental": 14767, "model4_conditioned": 14758}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 35,523 | 14.5 | 9.5 | 20.0 | 15.2 | 18.9 | 13.6 | 8.3 | 11.86 | 40.8% | 21.9% |
| MW fair_v1 | 19,871 | 13.6 | 8.4 | 18.5 | 15.7 | 19.2 | 14.6 | 10.0 | 13.0 | 43.8% | 24.6% |
| MW gen1_elo | 19,871 | 13.2 | 9.0 | 19.7 | 15.1 | 19.1 | 14.3 | 9.7 | 12.48 | 43.1% | 23.9% |
| MW gen1_ledger | 15,652 | 15.7 | 10.8 | 21.9 | 14.7 | 18.4 | 12.3 | 6.2 | 10.39 | 36.9% | 18.6% |
| MW gen1_sr | 19,871 | 9.7 | 7.5 | 16.3 | 14.2 | 21.6 | 18.8 | 12.0 | 15.9 | 52.4% | 30.8% |
| MW gen2 | 19,871 | 11.4 | 7.1 | 16.5 | 14.1 | 20.0 | 17.7 | 13.2 | 15.45 | 50.9% | 30.9% |
| all families model4_conditioned | 14,758 | 21.6 | 19.8 | 34.8 | 16.9 | 4.6 | 1.4 | 0.9 | 5.85 | 6.9% | 2.3% |
| all families model4_fundamental | 14,767 | 16.7 | 13.4 | 35.3 | 19.6 | 10.9 | 3.0 | 1.2 | 7.64 | 15.0% | 4.1% |

Configurable thresholds (primary): >=5pp 76.0%, >=10pp 56.0%, >=15pp 40.8%, >=20pp 30.3%, >=25pp 21.9%, >=30pp 15.9%, >=40pp 8.3%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.5pp; >=10pp 45.4%, >=25pp 17.5%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,390 | 30.9 | 14.3 | 25.0 | 17.1 | 10.7 | 1.2 | 0.8 | 5.82 | 12.7% | 2.0% |
| CHALLENGER | 3,298 | 16.0 | 9.8 | 20.0 | 15.8 | 14.4 | 12.3 | 11.6 | 11.51 | 38.4% | 23.9% |
| ITF_MEN | 5,686 | 10.9 | 8.2 | 17.6 | 14.8 | 19.8 | 16.4 | 12.4 | 14.45 | 48.6% | 28.8% |
| ITF_WOMEN | 7,805 | 10.5 | 6.5 | 16.1 | 15.7 | 22.2 | 18.0 | 11.0 | 15.48 | 51.2% | 28.9% |
| WTA | 1,057 | 20.6 | 11.9 | 25.4 | 15.5 | 20.0 | 5.5 | 1.0 | 7.82 | 26.5% | 6.5% |
| WTA125 | 635 | 13.1 | 7.7 | 23.1 | 20.5 | 20.0 | 13.5 | 2.0 | 11.31 | 35.6% | 15.6% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,390 | 24.6 | 14.4 | 24.8 | 18.8 | 14.3 | 2.0 | 1.1 | 6.71 | 17.4% | 3.1% |
| CHALLENGER | 3,298 | 14.7 | 8.0 | 19.4 | 13.5 | 17.9 | 14.3 | 12.2 | 12.77 | 44.5% | 26.5% |
| ITF_MEN | 5,686 | 9.5 | 6.8 | 15.8 | 13.6 | 19.9 | 19.4 | 15.0 | 16.84 | 54.3% | 34.5% |
| ITF_WOMEN | 7,805 | 8.6 | 5.7 | 13.8 | 13.4 | 21.4 | 20.8 | 16.4 | 18.68 | 58.6% | 37.2% |
| WTA | 1,057 | 17.2 | 8.1 | 20.6 | 15.4 | 22.2 | 15.2 | 1.1 | 11.5 | 38.6% | 16.4% |
| WTA125 | 635 | 6.5 | 4.7 | 17.5 | 17.9 | 24.9 | 19.4 | 9.1 | 16.84 | 53.4% | 28.5% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,390 | 28.2 | 14.0 | 28.4 | 15.4 | 10.9 | 2.4 | 0.9 | 6.1 | 14.1% | 3.2% |
| CHALLENGER | 3,298 | 14.8 | 10.3 | 20.7 | 15.0 | 15.4 | 12.0 | 11.8 | 11.03 | 39.2% | 23.8% |
| ITF_MEN | 5,686 | 10.0 | 8.1 | 18.0 | 14.1 | 20.5 | 16.6 | 12.6 | 14.97 | 49.8% | 29.3% |
| ITF_WOMEN | 7,805 | 9.9 | 7.0 | 16.5 | 15.7 | 22.8 | 17.9 | 10.2 | 15.38 | 50.9% | 28.1% |
| WTA | 1,057 | 23.4 | 15.8 | 31.9 | 15.3 | 10.7 | 2.3 | 0.7 | 6.08 | 13.6% | 2.9% |
| WTA125 | 635 | 22.4 | 12.4 | 29.1 | 15.4 | 14.3 | 6.0 | 0.3 | 7.73 | 20.6% | 6.3% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 777 | 31.3 | 22.5 | 34.4 | 9.7 | 1.5 | 0.6 | 0.0 | 4.68 | 2.2% | 0.6% |
| CHALLENGER | 2,247 | 22.6 | 15.1 | 27.6 | 14.7 | 12.8 | 5.2 | 2.0 | 6.94 | 20.0% | 7.2% |
| DOUBLES | 1,066 | 5.2 | 3.8 | 11.3 | 10.7 | 20.2 | 24.5 | 24.4 | 24.13 | 69.0% | 48.9% |
| ITF_MEN | 4,793 | 14.7 | 8.7 | 20.7 | 15.4 | 20.8 | 12.5 | 7.1 | 11.86 | 40.5% | 19.7% |
| ITF_WOMEN | 5,162 | 11.8 | 9.3 | 19.5 | 14.8 | 22.3 | 16.5 | 5.8 | 13.02 | 44.6% | 22.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 752 | 21.9 | 16.1 | 28.1 | 16.6 | 12.4 | 4.5 | 0.4 | 7.01 | 17.3% | 4.9% |
| WTA125 | 706 | 20.7 | 13.9 | 22.7 | 18.4 | 14.2 | 8.1 | 2.1 | 8.21 | 24.4% | 10.2% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,376 | 30.8 | 14.2 | 25.2 | 17.1 | 10.6 | 1.2 | 0.8 | 5.84 | 12.6% | 2.0% |
| CHALLENGER | 2,338 | 20.9 | 12.4 | 25.3 | 18.4 | 14.9 | 5.9 | 2.3 | 8.24 | 23.1% | 8.2% |
| ITF_MEN | 4,133 | 13.3 | 10.1 | 20.9 | 16.6 | 20.2 | 13.2 | 5.7 | 11.53 | 39.1% | 18.9% |
| ITF_WOMEN | 5,830 | 12.4 | 7.9 | 18.3 | 17.8 | 23.6 | 14.9 | 5.0 | 13.07 | 43.5% | 20.0% |
| WTA | 1,037 | 20.8 | 11.4 | 25.8 | 15.5 | 20.1 | 5.4 | 1.1 | 7.83 | 26.5% | 6.5% |
| WTA125 | 609 | 13.5 | 7.5 | 22.7 | 20.9 | 20.7 | 13.1 | 1.6 | 11.31 | 35.5% | 14.8% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,376 | 24.5 | 14.5 | 24.9 | 18.8 | 14.3 | 2.0 | 1.1 | 6.74 | 17.4% | 3.0% |
| CHALLENGER | 2,338 | 18.9 | 10.3 | 24.4 | 16.2 | 18.3 | 9.4 | 2.5 | 9.02 | 30.2% | 11.9% |
| ITF_MEN | 4,134 | 11.2 | 8.1 | 18.2 | 15.3 | 21.9 | 16.9 | 8.5 | 14.09 | 47.3% | 25.4% |
| ITF_WOMEN | 5,830 | 9.7 | 6.5 | 15.3 | 14.6 | 23.3 | 19.9 | 10.5 | 16.41 | 53.8% | 30.4% |
| WTA | 1,037 | 17.2 | 8.0 | 20.6 | 15.4 | 22.3 | 15.3 | 1.2 | 11.62 | 38.8% | 16.5% |
| WTA125 | 609 | 6.2 | 4.9 | 17.6 | 18.4 | 24.8 | 19.9 | 8.2 | 16.74 | 52.9% | 28.1% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 757 | 31.3 | 22.7 | 34.6 | 9.8 | 0.9 | 0.7 | 0.0 | 4.62 | 1.6% | 0.7% |
| CHALLENGER | 1,931 | 24.4 | 16.5 | 29.7 | 14.5 | 11.9 | 2.4 | 0.5 | 6.31 | 14.8% | 2.9% |
| DOUBLES | 980 | 5.4 | 3.9 | 11.5 | 10.8 | 20.0 | 24.6 | 23.8 | 24.07 | 68.4% | 48.4% |
| ITF_MEN | 3,954 | 16.1 | 9.5 | 22.6 | 16.3 | 20.7 | 10.6 | 4.3 | 10.54 | 35.5% | 14.8% |
| ITF_WOMEN | 4,221 | 12.9 | 10.1 | 21.3 | 15.7 | 22.5 | 14.8 | 2.8 | 11.61 | 40.1% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 718 | 22.4 | 16.7 | 28.3 | 16.6 | 12.5 | 3.5 | 0.0 | 6.81 | 16.0% | 3.5% |
| WTA125 | 598 | 22.6 | 15.4 | 24.2 | 20.1 | 12.5 | 4.8 | 0.3 | 7.32 | 17.7% | 5.2% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,066 | 5.2 | 3.8 | 11.3 | 10.7 | 20.2 | 24.5 | 24.4 | 24.13 | 69.0% | 48.9% |
| singles | 14,586 | 16.4 | 11.3 | 22.7 | 15.0 | 18.2 | 11.5 | 4.9 | 9.88 | 34.6% | 16.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 4,677 | 13.4 | 8.8 | 19.2 | 15.7 | 18.0 | 14.7 | 10.2 | 12.76 | 42.9% | 24.9% |
| Grass | 225 | 10.7 | 11.6 | 17.8 | 13.8 | 22.7 | 15.6 | 8.0 | 14.16 | 46.2% | 23.6% |
| Hard | 12,855 | 13.9 | 8.4 | 18.6 | 15.2 | 19.6 | 14.4 | 9.9 | 12.98 | 43.9% | 24.2% |
| UNKNOWN | 2,114 | 12.1 | 7.2 | 16.9 | 18.8 | 19.1 | 15.8 | 10.2 | 13.38 | 45.0% | 25.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,782 | 19.8 | 10.7 | 21.1 | 16.9 | 15.7 | 8.9 | 6.8 | 9.46 | 31.5% | 15.8% |
| B | 2,601 | 14.0 | 9.0 | 19.6 | 16.3 | 18.5 | 12.3 | 10.2 | 12.01 | 41.1% | 22.5% |
| C | 2,880 | 12.6 | 9.4 | 20.1 | 14.2 | 19.2 | 14.4 | 10.0 | 12.69 | 43.7% | 24.4% |
| D | 3,412 | 11.8 | 7.8 | 17.4 | 15.9 | 21.9 | 15.4 | 9.8 | 13.94 | 47.1% | 25.1% |
| F | 5,196 | 8.1 | 5.3 | 14.9 | 14.8 | 21.7 | 21.6 | 13.4 | 17.98 | 56.8% | 35.1% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,594 | 23.2 | 15.8 | 28.9 | 15.1 | 11.0 | 4.3 | 1.6 | 6.66 | 17.0% | 6.0% |
| B | 2,333 | 14.8 | 10.2 | 24.1 | 16.5 | 19.3 | 11.0 | 4.2 | 10.18 | 34.5% | 15.3% |
| C | 3,085 | 12.1 | 7.8 | 18.1 | 14.2 | 20.9 | 15.7 | 11.2 | 13.85 | 47.8% | 26.9% |
| D | 2,323 | 14.1 | 9.8 | 20.6 | 13.7 | 21.3 | 13.8 | 6.6 | 11.86 | 41.8% | 20.4% |
| F | 3,317 | 10.4 | 7.7 | 15.3 | 13.9 | 23.5 | 20.3 | 8.9 | 16.19 | 52.7% | 29.2% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 6,542 | 18.0 | 9.7 | 20.4 | 16.6 | 16.3 | 9.9 | 9.1 | 10.52 | 35.4% | 19.1% |
| LIMITED | 4,601 | 14.6 | 10.3 | 20.8 | 15.3 | 18.6 | 12.9 | 7.5 | 11.3 | 38.9% | 20.3% |
| POOR | 8,728 | 9.7 | 6.5 | 16.0 | 15.2 | 21.8 | 19.0 | 11.9 | 15.99 | 52.7% | 30.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,239 | 30.6 | 24.0 | 35.5 | 6.7 | 2.2 | 0.9 | 0.1 | 4.58 | 3.2% | 1.0% |
| GAME_SPREAD | 2,997 | 25.7 | 16.3 | 36.3 | 16.9 | 4.2 | 0.4 | 0.2 | 5.95 | 4.8% | 0.6% |
| MATCH_WINNER | 15,652 | 15.7 | 10.8 | 21.9 | 14.7 | 18.4 | 12.3 | 6.2 | 10.39 | 36.9% | 18.6% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 6,109 | 32.9 | 19.1 | 30.6 | 10.3 | 5.6 | 1.2 | 0.2 | 4.81 | 7.1% | 1.5% |
| TOTAL_GAMES | 4,738 | 6.6 | 8.9 | 38.6 | 29.0 | 11.3 | 3.3 | 2.3 | 9.54 | 16.9% | 5.6% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,132 | 25.6 | 37.7 | 31.0 | 1.0 | 3.9 | 0.6 | 0.2 | 4.32 | 4.7% | 0.8% |
| GAME_SPREAD | 3,618 | 45.6 | 16.6 | 28.3 | 7.3 | 1.2 | 0.7 | 0.4 | 3.49 | 2.2% | 1.1% |
| TOTAL_GAMES | 6,008 | 3.7 | 6.5 | 41.8 | 36.3 | 7.2 | 2.5 | 1.9 | 9.82 | 11.6% | 4.4% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,132 | 26.4 | 18.4 | 36.8 | 9.3 | 6.5 | 2.3 | 0.4 | 5.52 | 9.2% | 2.6% |
| GAME_SPREAD | 3,618 | 19.6 | 13.6 | 30.1 | 20.7 | 12.9 | 2.4 | 0.7 | 7.68 | 16.0% | 3.1% |
| TOTAL_GAMES | 6,017 | 6.8 | 9.0 | 37.2 | 27.6 | 13.4 | 3.9 | 2.1 | 9.69 | 19.4% | 6.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 19,871 | 43.8% | 24.6% | 13.0 | 35.0% | 15.2% | 10.65 |
| gen1_elo | 19,871 | 43.1% | 23.9% | 12.48 | 33.9% | 14.9% | 10.11 |
| gen1_sr | 19,871 | 52.4% | 30.8% | 15.9 | 44.5% | 21.4% | 13.27 |
| gen2 | 19,871 | 50.9% | 30.9% | 15.45 | 44.1% | 22.8% | 13.02 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 10,582 | 16.5 | 10.4 | 21.6 | 17.2 | 19.6 | 11.3 | 3.4 | 10.41 | 34.3% | 14.6% |
| STALE | 9,289 | 10.2 | 6.2 | 15.0 | 14.0 | 18.8 | 18.4 | 17.5 | 17.35 | 54.7% | 35.9% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 9,120 | 17.5 | 11.7 | 23.5 | 14.6 | 16.9 | 11.1 | 4.8 | 9.34 | 32.7% | 15.8% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 35,523 | 9120 | 14054 | 12349 | 24.1 | 160.6 | 1400.4 |
| ge_15pp | 14,483 | 2981 | 4914 | 6588 | 26.9 | 465.8 | 1380.4 |
| ge_25pp | 7,787 | 1443 | 2139 | 4205 | 34.5 | 599.9 | 1380.4 |
| lt_10pp | 15,624 | 4805 | 6770 | 4049 | 22.2 | 48.5 | 1341.5 |

Current slate `SL-20261017T012157Z-0e07119f`: 602 priced rows, quote age at build {'median': 6.2, 'max': 6.3}, freshness {'FRESH': 602}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 10 | 0.0 | 0.0 | 40.0 | 0.0 | 40.0 | 20.0 | 0.0 | 20.33 | 60.0% | 20.0% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,739 | 21.6 | 10.9 | 23.2 | 17.9 | 19.0 | 6.8 | 0.6 | 8.52 | 26.4% | 7.4% |
| KALSHI_LONE_OUTLIER | 9 | 11.1 | 0.0 | 66.7 | 0.0 | 11.1 | 11.1 | 0.0 | 5.14 | 22.2% | 11.1% |
| MARKETS_AGREE | 293 | 69.3 | 30.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.11 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 582 | 0.0 | 3.6 | 35.2 | 27.5 | 24.2 | 8.6 | 0.9 | 11.66 | 33.7% | 9.4% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 19,871 | 2645 (13.3%) | 22.0% | 0.7% | {"EXTERNAL_STALE": 1739, "AGREES_WITH_KALSHI": 582, "ALL_AGREE": 293, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 9, "AGREES_WITH_MODEL": 9, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 8,703 | 663 (7.6%) | 29.6% | 1.2% | {"EXTERNAL_STALE": 459, "AGREES_WITH_KALSHI": 196, "SUPPORTS_MODEL_DIRECTION": 6, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 4,882 | 187 (3.8%) | 29.4% | 1.6% | {"EXTERNAL_STALE": 129, "AGREES_WITH_KALSHI": 55, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,322 | 176 (7.6%) | 30.1% | 1.7% | {"EXTERNAL_STALE": 120, "AGREES_WITH_KALSHI": 53, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 8,050 | 1510 (18.8%) | 15.0% | 0.7% | {"EXTERNAL_STALE": 968, "ALL_AGREE": 293, "AGREES_WITH_KALSHI": 226, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 7, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,843 | 11.2 | 7.7 | 19.4 | 14.9 | 22.1 | 14.3 | 10.4 | 13.8 | 46.8% | 24.7% |
| 4-10x | 2,565 | 12.8 | 8.9 | 20.0 | 15.4 | 18.7 | 15.1 | 9.1 | 12.6 | 43.0% | 24.2% |
| <2x | 10,381 | 15.4 | 9.1 | 18.9 | 16.6 | 17.7 | 13.1 | 9.1 | 11.93 | 40.0% | 22.2% |
| >=10x | 3,082 | 11.0 | 6.5 | 15.1 | 13.7 | 21.2 | 19.5 | 13.0 | 16.49 | 53.7% | 32.5% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 5,280 | 13.5 | 8.2 | 19.3 | 15.8 | 19.9 | 12.9 | 10.4 | 12.81 | 43.1% | 23.3% |
| 300-1000 | 4,460 | 12.0 | 8.7 | 17.3 | 15.9 | 20.8 | 15.8 | 9.5 | 13.71 | 46.2% | 25.3% |
| <300 | 5,893 | 9.1 | 6.0 | 15.6 | 14.6 | 21.4 | 20.3 | 12.9 | 16.88 | 54.7% | 33.2% |
| >=3000 | 4,238 | 21.4 | 11.7 | 22.9 | 16.9 | 13.7 | 7.5 | 5.8 | 8.36 | 27.0% | 13.3% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 622 | 0.5375 | 0.4046 | 0.4839 | +0.053 | -0.079 | 0.0003 ± 0.0059 |
| ratio 4-10x | 414 | 0.585 | 0.4473 | 0.5121 | +0.073 | -0.065 | 0.0073 ± 0.0077 |
| ratio <2x | 1525 | 0.5365 | 0.4147 | 0.4538 | +0.083 | -0.039 | 0.0113 ± 0.0037 |
| ratio >=10x | 504 | 0.5439 | 0.3773 | 0.4187 | +0.125 | -0.041 | 0.0153 ± 0.0078 |
| thinner_sample 1000-3000 | 862 | 0.5435 | 0.4184 | 0.4722 | +0.071 | -0.054 | 0.0053 ± 0.0049 |
| thinner_sample 300-1000 | 737 | 0.5595 | 0.4214 | 0.4844 | +0.075 | -0.063 | 0.0021 ± 0.0057 |
| thinner_sample <300 | 945 | 0.5424 | 0.3825 | 0.436 | +0.106 | -0.053 | 0.0156 ± 0.0056 |
| thinner_sample >=3000 | 521 | 0.5286 | 0.4352 | 0.4607 | +0.068 | -0.025 | 0.0142 ± 0.0051 |
| data_status ADEQUATE | 893 | 0.5335 | 0.4291 | 0.4602 | +0.073 | -0.031 | 0.0093 ± 0.0042 |
| data_status LIMITED | 763 | 0.551 | 0.4222 | 0.4889 | +0.062 | -0.067 | 0.003 ± 0.0053 |
| data_status POOR | 1409 | 0.5479 | 0.3933 | 0.4485 | +0.099 | -0.055 | 0.0125 ± 0.0045 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 478 | 0.1924 | 0.1939 | -0.0014 ± 0.0007 | 0.5629 | 0.5658 | 0.4938 | 0.479 | 0.5293 | -0.041 ± 0.0211 | -0.01 (5) |
| 3-5 | 295 | 0.1905 | 0.1909 | -0.0004 ± 0.002 | 0.5609 | 0.5605 | 0.509 | 0.4692 | 0.4915 | -0.071 ± 0.026 | 0.02 (1) |
| 5-10 | 643 | 0.1979 | 0.1973 | +0.0006 ± 0.0027 | 0.5814 | 0.5776 | 0.51 | 0.4355 | 0.4619 | -0.085 ± 0.0182 | -0.0167 (6) |
| 10-15 | 542 | 0.2118 | 0.2033 | +0.0084 ± 0.0048 | 0.6112 | 0.5881 | 0.5174 | 0.3937 | 0.4207 | -0.085 ± 0.0193 | -0.048 (5) |
| 15-25 | 671 | 0.2306 | 0.2156 | +0.0150 ± 0.007 | 0.6564 | 0.6171 | 0.5755 | 0.3804 | 0.4411 | -0.080 ± 0.0178 | -0.0033 (9) |
| 25-40 | 362 | 0.2244 | 0.2087 | +0.0158 ± 0.0143 | 0.639 | 0.5994 | 0.6443 | 0.3357 | 0.4641 | -0.061 ± 0.0219 | -0.01 (1) |
| 40+ | 74 | 0.2888 | 0.1769 | +0.1119 ± 0.0433 | 0.7848 | 0.5268 | 0.7422 | 0.2957 | 0.3919 | -0.107 ± 0.043 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2225 | 0.1781 | 0.1794 | -0.0013 ± 0.0003 | 0.5299 | 0.5314 | 0.4781 | 0.4631 | 0.5011 | -0.017 ± 0.0091 | -0.0129 (17) |
| 3-5 | 1355 | 0.1917 | 0.1899 | +0.0017 ± 0.001 | 0.5632 | 0.5548 | 0.4783 | 0.4387 | 0.4339 | -0.062 ± 0.0121 | 0.0 (2) |
| 5-10 | 2993 | 0.1923 | 0.1897 | +0.0026 ± 0.0012 | 0.5668 | 0.5572 | 0.4831 | 0.4092 | 0.426 | -0.047 ± 0.0081 | -0.0119 (21) |
| 10-15 | 2605 | 0.2012 | 0.1819 | +0.0193 ± 0.0021 | 0.5884 | 0.5354 | 0.4779 | 0.3533 | 0.339 | -0.077 ± 0.0083 | -0.0281 (16) |
| 15-25 | 3172 | 0.2088 | 0.1712 | +0.0376 ± 0.0029 | 0.6099 | 0.5054 | 0.501 | 0.3049 | 0.3086 | -0.068 ± 0.0073 | -0.0025 (44) |
| 25-40 | 2485 | 0.2199 | 0.1263 | +0.0936 ± 0.0045 | 0.6329 | 0.3892 | 0.5273 | 0.2144 | 0.2249 | -0.059 ± 0.0069 | -0.01 (1) |
| 40+ | 1680 | 0.3758 | 0.0429 | +0.3329 ± 0.0057 | 0.9783 | 0.1703 | 0.626 | 0.1051 | 0.0565 | -0.085 ± 0.0047 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 355 | 0.1979 | 0.1983 | -0.0004 ± 0.0008 | 0.5772 | 0.578 | 0.5004 | 0.4852 | 0.507 | -0.078 ± 0.0248 | -0.01 (3) |
| 3-5 | 246 | 0.2088 | 0.2082 | +0.0006 ± 0.0024 | 0.5997 | 0.5996 | 0.5162 | 0.4761 | 0.4837 | -0.077 ± 0.0307 | 0.02 (1) |
| 5-10 | 560 | 0.1972 | 0.1963 | +0.0010 ± 0.0028 | 0.5774 | 0.5751 | 0.5489 | 0.4739 | 0.5054 | -0.073 ± 0.0194 | -0.01 (4) |
| 10-15 | 500 | 0.2165 | 0.2083 | +0.0082 ± 0.0051 | 0.6208 | 0.6018 | 0.5677 | 0.4432 | 0.476 | -0.089 ± 0.0213 | -0.04 (5) |
| 15-25 | 740 | 0.2287 | 0.2091 | +0.0197 ± 0.0066 | 0.6492 | 0.6006 | 0.5866 | 0.39 | 0.4419 | -0.086 ± 0.0171 | -0.0133 (9) |
| 25-40 | 482 | 0.2649 | 0.2 | +0.0649 ± 0.0128 | 0.741 | 0.5812 | 0.659 | 0.3441 | 0.4004 | -0.107 ± 0.0202 | -0.0075 (4) |
| 40+ | 182 | 0.3579 | 0.1786 | +0.1793 ± 0.0306 | 0.988 | 0.5282 | 0.738 | 0.2578 | 0.3242 | -0.067 ± 0.0303 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1868 | 0.182 | 0.1823 | -0.0004 ± 0.0003 | 0.5389 | 0.5396 | 0.4991 | 0.4844 | 0.5075 | -0.033 ± 0.0102 | -0.0133 (15) |
| 3-5 | 1183 | 0.1921 | 0.1914 | +0.0007 ± 0.001 | 0.559 | 0.5573 | 0.5164 | 0.4764 | 0.4869 | -0.040 ± 0.013 | 0.02 (1) |
| 5-10 | 2658 | 0.19 | 0.1867 | +0.0033 ± 0.0013 | 0.5621 | 0.5505 | 0.5104 | 0.4363 | 0.4533 | -0.044 ± 0.0085 | -0.0117 (6) |
| 10-15 | 2305 | 0.1973 | 0.1847 | +0.0126 ± 0.0022 | 0.5803 | 0.5396 | 0.5171 | 0.3926 | 0.4069 | -0.053 ± 0.0091 | -0.0189 (18) |
| 15-25 | 3321 | 0.2159 | 0.1763 | +0.0397 ± 0.0029 | 0.6274 | 0.52 | 0.5303 | 0.3339 | 0.3345 | -0.073 ± 0.0074 | -0.0086 (42) |
| 25-40 | 2935 | 0.2476 | 0.137 | +0.1105 ± 0.0043 | 0.7017 | 0.4188 | 0.5579 | 0.2418 | 0.2269 | -0.082 ± 0.0068 | -0.0044 (18) |
| 40+ | 2245 | 0.398 | 0.067 | +0.3310 ± 0.0062 | 1.0438 | 0.2338 | 0.6615 | 0.1257 | 0.098 | -0.067 ± 0.0053 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 458 | 0.1926 | 0.1952 | -0.0026 ± 0.0007 | 0.564 | 0.5705 | 0.4942 | 0.4789 | 0.5524 | -0.003 ± 0.021 | -0.0137 (8) |
| 3-5 | 333 | 0.1898 | 0.1877 | +0.0021 ± 0.0019 | 0.5561 | 0.5512 | 0.5004 | 0.4609 | 0.4565 | -0.116 ± 0.0249 | 0.0067 (3) |
| 5-10 | 675 | 0.2026 | 0.1984 | +0.0042 ± 0.0026 | 0.5925 | 0.5791 | 0.5042 | 0.4305 | 0.4356 | -0.096 ± 0.0176 | -0.0071 (7) |
| 10-15 | 529 | 0.2067 | 0.2061 | +0.0007 ± 0.0049 | 0.6008 | 0.5953 | 0.5357 | 0.4127 | 0.4745 | -0.062 ± 0.0196 | -0.0317 (6) |
| 15-25 | 620 | 0.2358 | 0.2094 | +0.0264 ± 0.0072 | 0.6711 | 0.6027 | 0.583 | 0.3896 | 0.4177 | -0.110 ± 0.0182 | -0.03 (1) |
| 25-40 | 380 | 0.2109 | 0.2126 | -0.0017 ± 0.0138 | 0.6092 | 0.6084 | 0.6495 | 0.34 | 0.4947 | -0.041 ± 0.0211 | 0.015 (2) |
| 40+ | 70 | 0.3064 | 0.1929 | +0.1135 ± 0.0469 | 0.8277 | 0.5631 | 0.7471 | 0.294 | 0.4 | -0.086 ± 0.0496 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2101 | 0.1841 | 0.185 | -0.0009 ± 0.0003 | 0.5428 | 0.5443 | 0.4829 | 0.4676 | 0.4955 | -0.024 ± 0.0094 | -0.0163 (35) |
| 3-5 | 1447 | 0.1874 | 0.1842 | +0.0032 ± 0.0009 | 0.5518 | 0.544 | 0.4795 | 0.4401 | 0.4195 | -0.083 ± 0.0116 | -0.0094 (18) |
| 5-10 | 3185 | 0.1943 | 0.1877 | +0.0066 ± 0.0012 | 0.5727 | 0.5515 | 0.4801 | 0.4062 | 0.3965 | -0.069 ± 0.0077 | -0.01 (31) |
| 10-15 | 2463 | 0.1943 | 0.1797 | +0.0146 ± 0.0021 | 0.5728 | 0.5287 | 0.4951 | 0.3719 | 0.3747 | -0.063 ± 0.0085 | -0.015 (12) |
| 15-25 | 3257 | 0.2099 | 0.1689 | +0.0410 ± 0.0028 | 0.6143 | 0.501 | 0.5043 | 0.3091 | 0.303 | -0.075 ± 0.0072 | -0.03 (2) |
| 25-40 | 2437 | 0.2152 | 0.125 | +0.0902 ± 0.0045 | 0.6222 | 0.3847 | 0.5248 | 0.2093 | 0.2277 | -0.055 ± 0.0068 | 0.01 (3) |
| 40+ | 1625 | 0.3892 | 0.0464 | +0.3428 ± 0.006 | 1.0154 | 0.1793 | 0.6354 | 0.1083 | 0.0585 | -0.085 ± 0.0051 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 794 | 0.1951 | 0.1954 | -0.0002 ± 0.0005 | 0.5707 | 0.5709 | 0.5073 | 0.4922 | 0.5 | -0.047 ± 0.0157 | -0.0224 (49) |
| 3-5 | 566 | 0.1945 | 0.1939 | +0.0006 ± 0.0015 | 0.5672 | 0.5643 | 0.4808 | 0.441 | 0.4505 | -0.048 ± 0.0186 | -0.0194 (34) |
| 5-10 | 1187 | 0.1964 | 0.1906 | +0.0058 ± 0.0019 | 0.5791 | 0.5625 | 0.4883 | 0.4147 | 0.4128 | -0.064 ± 0.0129 | -0.005 (78) |
| 10-15 | 746 | 0.2081 | 0.1966 | +0.0114 ± 0.0041 | 0.605 | 0.5751 | 0.5057 | 0.3827 | 0.3968 | -0.055 ± 0.0163 | 0.0014 (64) |
| 15-25 | 999 | 0.2336 | 0.2116 | +0.0220 ± 0.0057 | 0.6657 | 0.609 | 0.5633 | 0.3686 | 0.4104 | -0.056 ± 0.0146 | -0.0214 (59) |
| 25-40 | 579 | 0.2506 | 0.1962 | +0.0544 ± 0.0114 | 0.7067 | 0.5702 | 0.646 | 0.3337 | 0.4007 | -0.080 ± 0.0171 | -0.0219 (26) |
| 40+ | 193 | 0.3701 | 0.1933 | +0.1769 ± 0.0321 | 1.0713 | 0.5679 | 0.793 | 0.3026 | 0.3886 | -0.075 ± 0.029 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2365 | 0.1872 | 0.1872 | -0.0001 ± 0.0003 | 0.5498 | 0.549 | 0.502 | 0.4866 | 0.4973 | -0.034 ± 0.0089 | -0.0157 (88) |
| 3-5 | 1614 | 0.1878 | 0.1854 | +0.0024 ± 0.0009 | 0.5501 | 0.5443 | 0.4886 | 0.449 | 0.4387 | -0.056 ± 0.0108 | -0.0209 (69) |
| 5-10 | 3297 | 0.1931 | 0.1855 | +0.0076 ± 0.0011 | 0.5708 | 0.5488 | 0.4822 | 0.4085 | 0.3964 | -0.064 ± 0.0076 | -0.0082 (132) |
| 10-15 | 2210 | 0.2042 | 0.1896 | +0.0146 ± 0.0023 | 0.5963 | 0.5575 | 0.5107 | 0.3877 | 0.39 | -0.056 ± 0.0093 | -0.0053 (105) |
| 15-25 | 2792 | 0.2302 | 0.1981 | +0.0321 ± 0.0033 | 0.6637 | 0.5757 | 0.5551 | 0.36 | 0.3768 | -0.062 ± 0.0085 | -0.0253 (107) |
| 25-40 | 1900 | 0.2539 | 0.1699 | +0.0840 ± 0.006 | 0.7195 | 0.5019 | 0.6071 | 0.2931 | 0.3184 | -0.075 ± 0.0092 | -0.0229 (51) |
| 40+ | 913 | 0.385 | 0.1309 | +0.2541 ± 0.0128 | 1.0918 | 0.3995 | 0.7089 | 0.2019 | 0.218 | -0.068 ± 0.0114 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3065 | 1.064 ± 0.051 | 1.168 | 0.1681 | 0.1714 | 0.2113 | 0.2021 |
| gen2 | 3065 | 0.868 ± 0.046 | 1.126 | 0.1753 | 0.1714 | 0.2291 | 0.202 |
| gen1_elo | 3065 | 1.046 ± 0.05 | 1.152 | 0.1733 | 0.1718 | 0.2105 | 0.2019 |
| gen1_sr | 3065 | 1.079 ± 0.06 | 1.192 | 0.1349 | 0.1732 | 0.2253 | 0.2018 |
| gen1_ledger | 5064 | 0.876 ± 0.035 | 1.077 | 0.1772 | 0.1858 | 0.2179 | 0.1975 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 14,483)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,614 | 24.9% |
| STALE_QUOTE | market_freshness | 3,032 | 20.9% |
| BOOK_QUALITY | execution | 2,585 | 17.8% |
| POOR_DATA | data | 1,589 | 11.0% |
| LIMITED_DATA | data | 1,035 | 7.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 788 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 687 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 573 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 410 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 170 | 1.2% |

Cause class: coverage 24.9%, market_freshness 20.9%, data 18.1%, execution 17.8%, market_freshness/coverage 8.3%, model_calibration_or_unknown 4.7%, mapping 4.0%, model_calibration 1.2%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 95.8%, LOW_DATA_QUALITY 69.1%, THIN_PLAYER_HISTORY 57.8%, STALE_PLAYER_DATA 52.0%, STALE_KALSHI_QUOTE 45.5%, MODEL_INTERNAL_DISAGREEMENT 39.5%, ASYMMETRIC_SAMPLE_SIZE 31.7%, WIDE_SPREAD 23.6%, MODEL_HIGH_UNCERTAINTY 17.6%, PLAYER_IDENTITY_RISK 14.1%, LEVEL_TRANSFER_RISK 8.3%, EVENT_MAPPING_RISK 8.0%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.5%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 27.3%, POST_SETTLEMENT_OBSERVATION 24.9%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 7,787)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,856 | 36.7% |
| STALE_QUOTE | market_freshness | 1,426 | 18.3% |
| BOOK_QUALITY | execution | 1,346 | 17.3% |
| POOR_DATA | data | 647 | 8.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 425 | 5.5% |
| IDENTITY_AMBIGUOUS | mapping | 333 | 4.3% |
| LIMITED_DATA | data | 309 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 253 | 3.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 153 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 39 | 0.5% |

Cause class: coverage 36.7%, market_freshness 18.3%, execution 17.3%, data 12.3%, market_freshness/coverage 8.7%, mapping 4.3%, model_calibration_or_unknown 2.0%, model_calibration 0.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.9%, START_UNVERIFIABLE 98.2%, LOW_DATA_QUALITY 72.7%, THIN_PLAYER_HISTORY 60.2%, STALE_KALSHI_QUOTE 54.0%, STALE_PLAYER_DATA 47.0%, MODEL_INTERNAL_DISAGREEMENT 40.5%, ASYMMETRIC_SAMPLE_SIZE 33.5%, WIDE_SPREAD 23.2%, MODEL_HIGH_UNCERTAINTY 18.1%, PLAYER_IDENTITY_RISK 17.4%, EVENT_MAPPING_RISK 9.6%, LOW_DISPLAYED_LIQUIDITY 8.0%, LEVEL_TRANSFER_RISK 7.3%, MODEL_CALIBRATION_OUTLIER 4.4%, EXTERNAL_MARKET_REJECTION 1.0%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 39.4%, POST_SETTLEMENT_OBSERVATION 36.7%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 6234, "IDENTITY_AMBIGUOUS": 1553}; ticker orientation: {"VERIFIED": 7787}.

Checks: discipline:AMBIGUOUS 521, discipline:PASS 7266, identity_confidence:AMBIGUOUS 1354, identity_confidence:PASS 6433, level_mapping:NA 533, level_mapping:PASS 7254, market_pair:AMBIGUOUS 283, market_pair:NA 195, market_pair:PASS 7309, model_complement:NA 162, model_complement:PASS 7625, namesake:PASS 7787, physical_match_id:NA 2905, physical_match_id:PASS 4882, player_ids:PASS 7787, same_pair_other_event:PASS 7787, ticker_orientation:PASS 7787

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,167 | 1.5% | 1.5% | 0.4% | {"market_freshness": 21, "execution": 8, "data": 3, "market_freshness/coverage": 1} | 5.24 | 0.2088 / 0.2109 (259) | 16.0% | 1.1% | 5.3% | 1.6% |
| CHALLENGER | 5,545 | 17.2% | 5.8% | 12.2% | {"coverage": 581, "market_freshness/coverage": 121, "market_freshness": 112, "data": 63, "model_calibration_or_unknown": 46, "execution": 13, "model_calibration": 9, "mapping": 6} | 7.14 | 0.2173 / 0.2045 (1461) | 37.3% | 9.4% | 2.4% | 23.0% |
| DOUBLES | 1,066 | 48.9% | 48.4% | 6.7% | {"execution": 213, "mapping": 155, "market_freshness": 106, "market_freshness/coverage": 40, "coverage": 7} | 24.07 | 0.3273 / 0.2332 (325) | 21.9% | 0.0% | 100.0% | 8.1% |
| ITF_MEN | 10,479 | 24.6% | 16.9% | 33.1% | {"coverage": 1008, "execution": 524, "market_freshness": 407, "data": 347, "market_freshness/coverage": 205, "mapping": 88, "model_calibration_or_unknown": 2} | 11.12 | 0.2133 / 0.1944 (2572) | 36.5% | 61.0% | 12.3% | 22.8% |
| ITF_WOMEN | 12,967 | 26.3% | 19.0% | 43.8% | {"coverage": 1243, "market_freshness": 705, "execution": 562, "data": 509, "market_freshness/coverage": 262, "mapping": 78, "model_calibration_or_unknown": 43, "model_calibration": 10} | 12.53 | 0.2018 / 0.1918 (2711) | 39.2% | 57.0% | 10.0% | 22.5% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,809 | 5.9% | 5.2% | 1.4% | {"market_freshness": 36, "model_calibration_or_unknown": 23, "execution": 12, "data": 11, "market_freshness/coverage": 10, "model_calibration": 9, "coverage": 4, "mapping": 1} | 7.44 | 0.2398 / 0.2312 (289) | 24.5% | 1.8% | 1.9% | 3.0% |
| WTA125 | 1,341 | 12.8% | 10.0% | 2.2% | {"market_freshness/coverage": 38, "model_calibration_or_unknown": 37, "market_freshness": 37, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.22 | 0.2167 / 0.2061 (470) | 22.9% | 7.6% | 4.6% | 10.0% |

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
| 8 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 9 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 10 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 11 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 12 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 13 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 14 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 15 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 16 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 17 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 18 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 19 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 20 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 22 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 23 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 24 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 25 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 26 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 27 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 92 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 28 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 29 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 30 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 31 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 32 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 468 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 33 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 34 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 874 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 35 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 36 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 37 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 38 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 33 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 39 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFWMATCH-26OCT16ESTLAB-LAB` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 68 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1475.0, ratio 2.28); no external reference |
| 41 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 42 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 43 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 44 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.8h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 359 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 45 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 46 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 47 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 48 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 49 | `KXATPCHALLENGERMATCH-26OCT13GIUSEA-SEA` | CHALLENGER | fair_v1 | 76% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 243 min (STALE); no external reference |
| 50 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 189 min (STALE); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9821, "by_level_share_of_ge_25pp": {"ATP": 0.0042, "CHALLENGER": 0.1221, "DOUBLES": 0.0669, "ITF_MEN": 0.3314, "ITF_WOMEN": 0.4382, "OTHER": 0.0015, "WTA": 0.0136, "WTA125": 0.022}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.54, "share_primary_cause_market_settled_or_in_play": 0.4539, "share_primary_cause_stale_quote_only": 0.1831}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 7787, "identity_ambiguous_share": 0.1994, "ticker_orientation": {"VERIFIED": 7787}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 4882, "with_external": 187, "coverage": 0.0383, "external_status": {"EXTERNAL_STALE": 129, "AGREES_WITH_KALSHI": 55, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 129, "MODEL_LONE_OUTLIER": 55, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2941, "share_external_supports_model": 0.016}, "pregame_clean_ge_25pp": {"n": 2322, "with_external": 176, "coverage": 0.0758, "external_status": {"EXTERNAL_STALE": 120, "AGREES_WITH_KALSHI": 53, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 120, "MODEL_LONE_OUTLIER": 53, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3011, "share_external_supports_model": 0.017}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 562.0, "median_sample_ratio": 2.36, "median_min_matches": 20.0, "median_max_days_since_last": 204.0, "share_severe_asymmetry": 0.2028, "data_status": {"POOR": 4156, "LIMITED": 2208, "ADEQUATE": 1423}, "comparison_lt_10pp": {"median_thinner_serve_points": 1794.0, "median_sample_ratio": 1.69, "median_min_matches": 90.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 622, "model_minus_observed": 0.0535, "kalshi_minus_observed": -0.0794, "brier_diff_model_minus_kalshi": 0.0003}, "4-10x": {"n": 414, "model_minus_observed": 0.073, "kalshi_minus_observed": -0.0648, "brier_diff_model_minus_kalshi": 0.0073}, "<2x": {"n": 1525, "model_minus_observed": 0.0828, "kalshi_minus_observed": -0.0391, "brier_diff_model_minus_kalshi": 0.0113}, ">=10x": {"n": 504, "model_minus_observed": 0.1252, "kalshi_minus_observed": -0.0413, "brier_diff_model_minus_kalshi": 0.0153}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3065, "model": {"intercept": -0.544, "slope": 0.868, "slope_se": 0.046}, "kalshi_mid_same_rows": {"intercept": 0.233, "slope": 1.126, "slope_se": 0.052}, "mean_extremity_model": 0.1753, "mean_extremity_kalshi": 0.1714, "model_brier": 0.2291, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0271, "brier_diff_se": 0.0034, "model_logloss": 0.6537, "kalshi_logloss": 0.5861}, "fair_v1": {"n": 3065, "model": {"intercept": -0.402, "slope": 1.064, "slope_se": 0.051}, "kalshi_mid_same_rows": {"intercept": 0.311, "slope": 1.168, "slope_se": 0.053}, "mean_extremity_model": 0.1681, "mean_extremity_kalshi": 0.1714, "model_brier": 0.2113, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": 0.0092, "brier_diff_se": 0.0027, "model_logloss": 0.6099, "kalshi_logloss": 0.586}, "gen1_elo": {"n": 3065, "model": {"intercept": -0.398, "slope": 1.046, "slope_se": 0.05}, "kalshi_mid_same_rows": {"intercept": 0.299, "slope": 1.152, "slope_se": 0.052}, "mean_extremity_model": 0.1733, "mean_extremity_kalshi": 0.1718, "model_brier": 0.2105, "kalshi_brier": 0.2019, "brier_diff_model_minus_kalshi": 0.0086, "brier_diff_se": 0.0027, "model_logloss": 0.6091, "kalshi_logloss": 0.5856}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2457, "share_ge_15": 0.438, "median_abs_gap": 13.0, "n": 19871}, "gen1_elo": {"share_ge_25": 0.2395, "share_ge_15": 0.4311, "median_abs_gap": 12.48, "n": 19871}, "gen1_sr": {"share_ge_25": 0.3078, "share_ge_15": 0.5236, "median_abs_gap": 15.9, "n": 19871}, "gen2": {"share_ge_25": 0.3088, "share_ge_15": 0.5091, "median_abs_gap": 15.45, "n": 19871}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1515, "share_ge_15": 0.3497, "median_abs_gap": 10.65, "n": 15323}, "gen1_elo": {"share_ge_25": 0.1489, "share_ge_15": 0.3389, "median_abs_gap": 10.11, "n": 15322}, "gen1_sr": {"share_ge_25": 0.2145, "share_ge_15": 0.4449, "median_abs_gap": 13.27, "n": 15323}, "gen2": {"share_ge_25": 0.2276, "share_ge_15": 0.4411, "median_abs_gap": 13.02, "n": 15324}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.24, "share_ge_25_all": 0.0152, "share_ge_25_pregame_clean": 0.015}, "WTA": {"median_abs_gap_pregame_clean": 7.44, "share_ge_25_all": 0.0586, "share_ge_25_pregame_clean": 0.0524}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2396, "share_within_10pp_all": 0.4398, "share_within_10pp_pregame_clean": 0.4979, "corr_model_vs_mid_pregame_clean": 0.8435}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 478, "model_brier": 0.1924, "kalshi_brier": 0.1939, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 542, "model_brier": 0.2118, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.0084}, "15-25": {"n_settled": 671, "model_brier": 0.2306, "kalshi_brier": 0.2156, "brier_diff_model_minus_kalshi": 0.015}, "25-40": {"n_settled": 362, "model_brier": 0.2244, "kalshi_brier": 0.2087, "brier_diff_model_minus_kalshi": 0.0158}, "3-5": {"n_settled": 295, "model_brier": 0.1905, "kalshi_brier": 0.1909, "brier_diff_model_minus_kalshi": -0.0004}, "40+": {"n_settled": 74, "model_brier": 0.2888, "kalshi_brier": 0.1769, "brier_diff_model_minus_kalshi": 0.1119}, "5-10": {"n_settled": 643, "model_brier": 0.1979, "kalshi_brier": 0.1973, "brier_diff_model_minus_kalshi": 0.0006}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.544, "slope": 0.868, "slope_se": 0.046}, "kalshi_slope": {"intercept": 0.233, "slope": 1.126, "slope_se": 0.052}, "n": 3065}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.515, "slope": 0.876, "slope_se": 0.035}, "kalshi_slope": {"intercept": 0.142, "slope": 1.077, "slope_se": 0.039}, "n": 5064}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 325, "model_brier": 0.3273, "kalshi_brier": 0.2332, "brier_diff_model_minus_kalshi": 0.0942, "brier_diff_se": 0.0175, "corr_model_outcome": 0.011, "corr_kalshi_outcome": 0.258}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
