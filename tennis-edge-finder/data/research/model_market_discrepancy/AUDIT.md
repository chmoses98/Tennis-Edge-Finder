# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-19T11:09Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 40,492): 0-3 14.4%, 3-5 9.5%, 5-10 19.9%, 10-15 15.4%, 15-25 19.0%, 25-40 13.7%, 40+ 8.1%; median gap 11.87 pp.
* **Where the extremes live**: 97.4% of >=25 pp gaps are off the ATP/WTA main tour (ITF 75.4%, Challenger 12.5%, doubles 7.4%). Main tour: ATP 3.9% and WTA 4.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 8,786): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.9%, BOOK_QUALITY 19.4%, STALE_QUOTE 17.8%, POOR_DATA 8.8%, POSSIBLY_IN_PLAY_QUOTE 5.3%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 3.7%, IN_PLAY_QUOTE 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.5%. By class: coverage 34.9%, execution 19.4%, market_freshness 17.8%, data 12.5%, market_freshness/coverage 8.6%, mapping 4.3%, model_calibration_or_unknown 2.0%, model_calibration 0.5%.
* **Stale / settled / in-play**: 51.7% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 8,786 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.0% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 23.6% of the time and with the model 0.6%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 531.5 points vs 1822.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.052, Gen-2 0.836, Gen-1 ledger 0.878 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 416 model 0.2209 vs Kalshi 0.2106; n 85 model 0.3039 vs Kalshi 0.1748.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 171,523 model-market comparisons (278,735 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 60,836 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-19T10:57:38.869441+00:00'], shadow board 44,987 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-19T10:57:42.416359+00:00'], Model 4 20,843 rows, 16,470 settled tickers, 5,582 tickers with an external scan.
* By model: {"gen1_ledger": 41157, "gen1_elo": 22622, "fair_v1": 22622, "gen2": 22622, "gen1_sr": 22622, "model4_fundamental": 19948, "model4_conditioned": 19930}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 40,492 | 14.4 | 9.5 | 19.9 | 15.4 | 19.0 | 13.7 | 8.1 | 11.87 | 40.7% | 21.7% |
| MW fair_v1 | 22,622 | 13.5 | 8.6 | 18.4 | 16.0 | 19.4 | 14.5 | 9.6 | 12.94 | 43.5% | 24.0% |
| MW gen1_elo | 22,622 | 13.0 | 9.1 | 19.5 | 15.3 | 19.4 | 14.4 | 9.2 | 12.53 | 43.1% | 23.6% |
| MW gen1_ledger | 17,870 | 15.5 | 10.7 | 21.9 | 14.7 | 18.5 | 12.6 | 6.1 | 10.48 | 37.3% | 18.7% |
| MW gen1_sr | 22,622 | 9.9 | 7.4 | 16.9 | 14.3 | 21.4 | 18.3 | 11.9 | 15.54 | 51.6% | 30.2% |
| MW gen2 | 22,622 | 11.4 | 7.3 | 16.4 | 14.3 | 19.9 | 17.5 | 13.1 | 15.27 | 50.5% | 30.6% |
| all families model4_conditioned | 19,930 | 21.8 | 18.8 | 34.5 | 17.6 | 4.8 | 1.5 | 1.1 | 5.98 | 7.3% | 2.6% |
| all families model4_fundamental | 19,948 | 16.2 | 12.9 | 34.4 | 20.4 | 11.3 | 3.4 | 1.4 | 7.91 | 16.1% | 4.8% |

Configurable thresholds (primary): >=5pp 76.1%, >=10pp 56.1%, >=15pp 40.7%, >=20pp 30.2%, >=25pp 21.7%, >=30pp 15.6%, >=40pp 8.1%, >=50pp 3.6%
Executable gap (model outside the book, before fees): median 8.18pp; >=10pp 44.5%, >=25pp 16.8%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,958 | 29.4 | 12.9 | 24.8 | 16.7 | 11.8 | 3.8 | 0.6 | 6.35 | 16.2% | 4.4% |
| CHALLENGER | 3,807 | 15.4 | 10.4 | 20.2 | 16.2 | 14.7 | 12.2 | 10.9 | 11.32 | 37.9% | 23.1% |
| ITF_MEN | 6,003 | 10.9 | 7.9 | 17.2 | 14.9 | 20.2 | 16.4 | 12.5 | 14.67 | 49.1% | 28.9% |
| ITF_WOMEN | 8,821 | 10.2 | 6.9 | 15.8 | 15.6 | 22.6 | 18.1 | 10.9 | 15.57 | 51.6% | 29.1% |
| WTA | 1,373 | 18.4 | 12.4 | 24.9 | 19.4 | 19.8 | 4.3 | 0.8 | 8.39 | 24.9% | 5.1% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,958 | 23.6 | 15.2 | 23.8 | 17.7 | 14.2 | 4.5 | 0.9 | 6.85 | 19.7% | 5.5% |
| CHALLENGER | 3,807 | 14.8 | 8.2 | 18.9 | 14.1 | 17.9 | 14.2 | 11.9 | 12.76 | 44.0% | 26.1% |
| ITF_MEN | 6,003 | 9.3 | 6.6 | 15.6 | 13.5 | 19.8 | 19.4 | 15.7 | 17.05 | 54.9% | 35.1% |
| ITF_WOMEN | 8,821 | 8.4 | 5.6 | 13.7 | 13.6 | 21.2 | 20.9 | 16.7 | 18.84 | 58.8% | 37.6% |
| WTA | 1,373 | 15.9 | 8.8 | 20.2 | 16.5 | 23.1 | 14.6 | 0.9 | 11.45 | 38.5% | 15.4% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,958 | 24.3 | 13.8 | 25.6 | 16.7 | 14.1 | 4.9 | 0.7 | 6.85 | 19.7% | 5.6% |
| CHALLENGER | 3,807 | 14.5 | 9.9 | 21.1 | 15.3 | 15.8 | 12.2 | 11.2 | 11.2 | 39.2% | 23.4% |
| ITF_MEN | 6,003 | 9.9 | 8.0 | 17.6 | 14.1 | 20.9 | 16.8 | 12.5 | 15.03 | 50.3% | 29.3% |
| ITF_WOMEN | 8,821 | 9.6 | 7.0 | 16.4 | 15.7 | 22.9 | 18.3 | 10.2 | 15.54 | 51.4% | 28.5% |
| WTA | 1,373 | 24.0 | 17.4 | 30.2 | 15.2 | 10.5 | 2.2 | 0.5 | 6.0 | 13.2% | 2.7% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,157 | 27.4 | 20.3 | 30.9 | 11.4 | 7.1 | 2.6 | 0.3 | 5.24 | 9.9% | 2.9% |
| CHALLENGER | 2,670 | 21.7 | 14.7 | 27.4 | 13.9 | 14.2 | 6.1 | 1.9 | 7.08 | 22.2% | 8.0% |
| DOUBLES | 1,340 | 4.5 | 4.2 | 10.6 | 10.7 | 21.2 | 26.0 | 22.8 | 24.16 | 70.0% | 48.8% |
| ITF_MEN | 5,004 | 14.4 | 8.6 | 20.7 | 15.8 | 20.9 | 12.5 | 7.0 | 11.87 | 40.4% | 19.5% |
| ITF_WOMEN | 5,860 | 11.6 | 9.0 | 19.5 | 14.9 | 22.1 | 16.8 | 6.2 | 13.17 | 45.0% | 23.0% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 958 | 22.6 | 15.7 | 29.5 | 17.3 | 10.7 | 3.9 | 0.3 | 6.86 | 14.8% | 4.2% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,919 | 29.6 | 13.0 | 25.1 | 16.6 | 11.6 | 3.5 | 0.6 | 6.24 | 15.7% | 4.2% |
| CHALLENGER | 2,730 | 19.9 | 12.9 | 25.1 | 18.6 | 15.1 | 6.3 | 2.0 | 8.31 | 23.4% | 8.4% |
| ITF_MEN | 4,349 | 13.5 | 9.8 | 20.6 | 16.8 | 20.5 | 13.2 | 5.6 | 11.66 | 39.3% | 18.8% |
| ITF_WOMEN | 6,626 | 11.9 | 8.2 | 17.8 | 17.7 | 24.1 | 15.4 | 4.9 | 13.34 | 44.4% | 20.3% |
| WTA | 1,337 | 18.6 | 12.1 | 24.8 | 19.4 | 20.0 | 4.3 | 0.8 | 8.42 | 25.1% | 5.1% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,919 | 23.8 | 15.4 | 23.9 | 17.7 | 14.1 | 4.4 | 0.8 | 6.73 | 19.2% | 5.2% |
| CHALLENGER | 2,730 | 18.7 | 10.4 | 23.4 | 17.0 | 18.4 | 9.6 | 2.5 | 9.46 | 30.4% | 12.0% |
| ITF_MEN | 4,350 | 11.1 | 7.9 | 18.1 | 15.3 | 21.9 | 17.1 | 8.6 | 14.14 | 47.5% | 25.7% |
| ITF_WOMEN | 6,626 | 9.2 | 6.4 | 15.0 | 14.9 | 23.4 | 20.4 | 10.6 | 16.71 | 54.4% | 31.1% |
| WTA | 1,337 | 15.9 | 8.8 | 20.1 | 16.4 | 23.2 | 14.7 | 0.9 | 11.5 | 38.8% | 15.6% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,124 | 27.6 | 20.5 | 31.1 | 11.6 | 6.6 | 2.4 | 0.3 | 5.19 | 9.2% | 2.7% |
| CHALLENGER | 2,321 | 23.3 | 15.9 | 29.3 | 13.7 | 13.5 | 3.8 | 0.6 | 6.52 | 17.9% | 4.3% |
| DOUBLES | 1,244 | 4.6 | 4.3 | 10.7 | 10.8 | 21.1 | 26.1 | 22.3 | 24.07 | 69.5% | 48.4% |
| ITF_MEN | 4,137 | 15.9 | 9.4 | 22.6 | 16.7 | 20.7 | 10.6 | 4.2 | 10.61 | 35.4% | 14.7% |
| ITF_WOMEN | 4,859 | 12.3 | 9.6 | 21.1 | 15.7 | 22.3 | 15.5 | 3.5 | 11.91 | 41.3% | 19.0% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 912 | 23.1 | 16.1 | 29.6 | 17.3 | 10.8 | 3.1 | 0.0 | 6.79 | 13.8% | 3.1% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,340 | 4.5 | 4.2 | 10.6 | 10.7 | 21.2 | 26.0 | 22.8 | 24.16 | 70.0% | 48.8% |
| singles | 16,530 | 16.4 | 11.2 | 22.8 | 15.1 | 18.3 | 11.5 | 4.8 | 9.91 | 34.6% | 16.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 5,145 | 13.6 | 9.0 | 19.3 | 16.0 | 18.2 | 14.3 | 9.6 | 12.6 | 42.1% | 23.9% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 14,570 | 13.9 | 8.6 | 18.4 | 15.6 | 19.7 | 14.3 | 9.5 | 12.95 | 43.5% | 23.8% |
| UNKNOWN | 2,670 | 11.5 | 7.8 | 16.9 | 18.3 | 19.8 | 15.8 | 9.8 | 13.38 | 45.4% | 25.6% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,664 | 19.9 | 11.0 | 21.4 | 17.3 | 15.8 | 8.6 | 6.0 | 9.32 | 30.4% | 14.6% |
| B | 2,938 | 13.0 | 9.3 | 19.8 | 17.1 | 18.5 | 11.8 | 10.5 | 12.04 | 40.8% | 22.3% |
| C | 3,250 | 12.7 | 9.3 | 19.3 | 14.8 | 19.3 | 14.7 | 9.8 | 12.77 | 43.8% | 24.5% |
| D | 3,789 | 12.4 | 8.1 | 17.1 | 15.6 | 21.9 | 15.5 | 9.4 | 13.9 | 46.8% | 24.9% |
| F | 5,981 | 7.8 | 5.6 | 14.9 | 14.7 | 22.4 | 21.5 | 13.1 | 17.85 | 57.0% | 34.6% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,257 | 23.4 | 15.9 | 28.8 | 15.1 | 11.4 | 4.0 | 1.5 | 6.6 | 16.9% | 5.5% |
| B | 2,530 | 15.2 | 10.0 | 24.2 | 16.4 | 19.2 | 10.9 | 4.0 | 10.09 | 34.2% | 14.9% |
| C | 3,611 | 11.2 | 7.5 | 18.1 | 14.1 | 21.7 | 16.4 | 11.1 | 14.59 | 49.2% | 27.5% |
| D | 2,599 | 13.8 | 9.8 | 20.6 | 13.7 | 20.9 | 14.5 | 6.5 | 12.04 | 42.0% | 21.1% |
| F | 3,873 | 10.1 | 7.7 | 15.2 | 14.4 | 23.1 | 20.6 | 9.0 | 16.19 | 52.6% | 29.5% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 7,575 | 18.0 | 10.0 | 20.7 | 17.2 | 16.3 | 9.4 | 8.4 | 10.37 | 34.1% | 17.8% |
| LIMITED | 5,078 | 14.4 | 10.4 | 20.2 | 15.6 | 18.9 | 13.2 | 7.3 | 11.49 | 39.4% | 20.5% |
| POOR | 9,969 | 9.6 | 6.7 | 15.8 | 15.2 | 22.1 | 19.0 | 11.6 | 15.96 | 52.7% | 30.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,462 | 26.9 | 21.6 | 34.8 | 11.3 | 4.0 | 1.2 | 0.2 | 5.11 | 5.4% | 1.4% |
| GAME_SPREAD | 3,988 | 23.6 | 15.4 | 33.9 | 17.3 | 7.4 | 2.1 | 0.3 | 6.42 | 9.8% | 2.3% |
| MATCH_WINNER | 17,870 | 15.5 | 10.7 | 21.9 | 14.7 | 18.5 | 12.6 | 6.1 | 10.48 | 37.3% | 18.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 8,375 | 30.4 | 17.4 | 30.4 | 12.3 | 7.9 | 1.2 | 0.4 | 5.26 | 9.5% | 1.6% |
| TOTAL_GAMES | 6,438 | 7.3 | 8.8 | 37.1 | 29.1 | 11.1 | 3.5 | 3.0 | 9.65 | 17.6% | 6.5% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,979 | 25.1 | 34.3 | 32.6 | 3.8 | 3.5 | 0.6 | 0.2 | 4.48 | 4.3% | 0.8% |
| GAME_SPREAD | 4,779 | 46.1 | 16.8 | 27.3 | 7.1 | 1.8 | 0.7 | 0.3 | 3.4 | 2.7% | 0.9% |
| TOTAL_GAMES | 8,172 | 4.7 | 6.8 | 40.4 | 35.5 | 7.7 | 2.6 | 2.4 | 9.82 | 12.7% | 5.0% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,982 | 24.3 | 17.6 | 36.0 | 12.1 | 7.2 | 2.5 | 0.3 | 5.86 | 10.1% | 2.9% |
| GAME_SPREAD | 4,782 | 19.3 | 13.4 | 28.5 | 20.0 | 13.9 | 3.8 | 1.0 | 7.91 | 18.7% | 4.8% |
| TOTAL_GAMES | 8,184 | 7.4 | 8.5 | 36.6 | 27.9 | 13.2 | 3.9 | 2.5 | 9.72 | 19.7% | 6.4% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 22,622 | 43.5% | 24.0% | 12.94 | 34.9% | 14.9% | 10.71 |
| gen1_elo | 22,622 | 43.1% | 23.6% | 12.53 | 34.2% | 14.9% | 10.27 |
| gen1_sr | 22,622 | 51.6% | 30.2% | 15.54 | 43.9% | 21.0% | 13.01 |
| gen2 | 22,622 | 50.5% | 30.6% | 15.27 | 43.9% | 22.7% | 12.99 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 12,087 | 16.3 | 10.4 | 21.4 | 17.5 | 19.8 | 11.4 | 3.2 | 10.52 | 34.4% | 14.6% |
| STALE | 10,535 | 10.3 | 6.5 | 15.1 | 14.2 | 19.0 | 18.0 | 16.8 | 17.01 | 53.8% | 34.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 11,338 | 16.8 | 11.4 | 23.1 | 14.7 | 17.4 | 11.7 | 4.9 | 9.68 | 34.0% | 16.6% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 40,492 | 11338 | 15559 | 13595 | 23.7 | 135.7 | 1400.4 |
| ge_15pp | 16,489 | 3859 | 5451 | 7179 | 25.7 | 439.3 | 1380.4 |
| ge_25pp | 8,786 | 1886 | 2358 | 4542 | 32.3 | 576.9 | 1380.4 |
| lt_10pp | 17,763 | 5813 | 7445 | 4505 | 21.7 | 47.8 | 1341.5 |

Current slate `SL-20261019T110910Z-f7f4e310`: 610 priced rows, quote age at build {'median': 12.0, 'max': 12.0}, freshness {'AGING': 610}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 11 | 0.0 | 0.0 | 36.4 | 0.0 | 45.5 | 18.2 | 0.0 | 20.19 | 63.6% | 18.2% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,109 | 20.9 | 10.7 | 23.7 | 19.2 | 18.5 | 6.6 | 0.5 | 8.76 | 25.6% | 7.1% |
| KALSHI_LONE_OUTLIER | 11 | 9.1 | 0.0 | 72.7 | 0.0 | 9.1 | 9.1 | 0.0 | 5.2 | 18.2% | 9.1% |
| MARKETS_AGREE | 370 | 69.5 | 30.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.09 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 776 | 0.0 | 2.8 | 35.6 | 28.7 | 23.1 | 9.2 | 0.6 | 11.99 | 32.9% | 9.8% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 22,622 | 3289 (14.5%) | 23.6% | 0.6% | {"EXTERNAL_STALE": 2109, "AGREES_WITH_KALSHI": 776, "ALL_AGREE": 370, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 11, "SUPPORTS_MODEL_DIRECTION": 10, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 9,831 | 803 (8.2%) | 31.8% | 1.1% | {"EXTERNAL_STALE": 539, "AGREES_WITH_KALSHI": 255, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 5,438 | 228 (4.2%) | 33.3% | 1.3% | {"EXTERNAL_STALE": 149, "AGREES_WITH_KALSHI": 76, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,631 | 216 (8.2%) | 34.3% | 1.4% | {"EXTERNAL_STALE": 139, "AGREES_WITH_KALSHI": 74, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 9,181 | 1859 (20.2%) | 16.0% | 0.7% | {"EXTERNAL_STALE": 1166, "ALL_AGREE": 370, "AGREES_WITH_KALSHI": 298, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 9, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 4,347 | 11.1 | 7.9 | 19.4 | 15.1 | 21.6 | 15.1 | 9.8 | 13.76 | 46.6% | 24.9% |
| 4-10x | 2,949 | 12.1 | 8.9 | 19.0 | 15.9 | 19.4 | 15.2 | 9.5 | 13.02 | 44.1% | 24.7% |
| <2x | 11,754 | 15.6 | 9.5 | 19.0 | 17.0 | 17.9 | 12.5 | 8.6 | 11.68 | 39.0% | 21.1% |
| >=10x | 3,572 | 10.8 | 6.4 | 15.2 | 13.8 | 21.8 | 19.6 | 12.5 | 16.44 | 53.8% | 32.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 5,821 | 12.9 | 8.6 | 19.5 | 16.2 | 19.6 | 13.0 | 10.1 | 12.71 | 42.7% | 23.1% |
| 300-1000 | 5,010 | 12.2 | 8.8 | 17.0 | 15.9 | 20.7 | 16.0 | 9.4 | 13.72 | 46.2% | 25.4% |
| <300 | 6,811 | 9.0 | 6.0 | 15.4 | 14.8 | 22.0 | 20.2 | 12.6 | 16.85 | 54.8% | 32.8% |
| >=3000 | 4,980 | 21.7 | 12.1 | 22.8 | 17.3 | 14.3 | 6.8 | 5.0 | 8.15 | 26.1% | 11.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 680 | 0.5418 | 0.4074 | 0.4912 | +0.051 | -0.084 | -0.0009 ± 0.0057 |
| ratio 4-10x | 462 | 0.5915 | 0.4498 | 0.5173 | +0.074 | -0.068 | 0.0078 ± 0.0074 |
| ratio <2x | 1689 | 0.5387 | 0.4177 | 0.4512 | +0.087 | -0.034 | 0.0122 ± 0.0034 |
| ratio >=10x | 573 | 0.5625 | 0.3898 | 0.4468 | +0.116 | -0.057 | 0.0119 ± 0.0076 |
| thinner_sample 1000-3000 | 941 | 0.5437 | 0.4177 | 0.4633 | +0.080 | -0.046 | 0.0077 ± 0.0047 |
| thinner_sample 300-1000 | 811 | 0.566 | 0.4254 | 0.4969 | +0.069 | -0.072 | 0.0003 ± 0.0055 |
| thinner_sample <300 | 1065 | 0.5548 | 0.3924 | 0.4526 | +0.102 | -0.060 | 0.0137 ± 0.0053 |
| thinner_sample >=3000 | 587 | 0.5322 | 0.4391 | 0.46 | +0.072 | -0.021 | 0.0143 ± 0.0047 |
| data_status ADEQUATE | 992 | 0.5347 | 0.4303 | 0.4556 | +0.079 | -0.025 | 0.0113 ± 0.0039 |
| data_status LIMITED | 840 | 0.5545 | 0.4242 | 0.4905 | +0.064 | -0.066 | 0.0029 ± 0.0051 |
| data_status POOR | 1572 | 0.5583 | 0.401 | 0.4625 | +0.096 | -0.061 | 0.0107 ± 0.0043 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 518 | 0.1963 | 0.1975 | -0.0013 ± 0.0007 | 0.5712 | 0.5739 | 0.4963 | 0.4814 | 0.5309 | -0.051 ± 0.0204 | -0.01 (5) |
| 3-5 | 325 | 0.1975 | 0.1968 | +0.0007 ± 0.002 | 0.5768 | 0.5738 | 0.5061 | 0.4662 | 0.4769 | -0.085 ± 0.0252 | 0.02 (1) |
| 5-10 | 711 | 0.1999 | 0.1997 | +0.0002 ± 0.0025 | 0.5853 | 0.5831 | 0.513 | 0.4386 | 0.4698 | -0.085 ± 0.0175 | -0.0167 (6) |
| 10-15 | 607 | 0.2152 | 0.2061 | +0.0090 ± 0.0046 | 0.6201 | 0.5945 | 0.526 | 0.4018 | 0.4267 | -0.095 ± 0.0185 | -0.048 (5) |
| 15-25 | 742 | 0.2265 | 0.2129 | +0.0136 ± 0.0066 | 0.6468 | 0.6109 | 0.581 | 0.3859 | 0.4488 | -0.088 ± 0.0168 | -0.0033 (9) |
| 25-40 | 416 | 0.2209 | 0.2106 | +0.0102 ± 0.0133 | 0.63 | 0.6043 | 0.6563 | 0.3477 | 0.4856 | -0.067 ± 0.0203 | -0.01 (1) |
| 40+ | 85 | 0.3039 | 0.1748 | +0.1291 ± 0.0409 | 0.8278 | 0.523 | 0.7553 | 0.3058 | 0.3882 | -0.129 ± 0.0396 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2461 | 0.1821 | 0.1834 | -0.0013 ± 0.0003 | 0.5393 | 0.5407 | 0.4802 | 0.4652 | 0.5047 | -0.018 ± 0.0087 | -0.0129 (17) |
| 3-5 | 1552 | 0.1945 | 0.1924 | +0.0021 ± 0.0009 | 0.5697 | 0.5607 | 0.478 | 0.4382 | 0.4298 | -0.066 ± 0.0113 | 0.0 (2) |
| 5-10 | 3361 | 0.1942 | 0.1914 | +0.0028 ± 0.0011 | 0.5705 | 0.5611 | 0.485 | 0.4113 | 0.427 | -0.049 ± 0.0077 | -0.0119 (21) |
| 10-15 | 2976 | 0.2031 | 0.185 | +0.0181 ± 0.002 | 0.5937 | 0.543 | 0.4863 | 0.3616 | 0.3518 | -0.075 ± 0.0079 | -0.0281 (16) |
| 15-25 | 3596 | 0.2086 | 0.1733 | +0.0353 ± 0.0027 | 0.6086 | 0.5112 | 0.5038 | 0.3076 | 0.317 | -0.065 ± 0.0069 | -0.0025 (44) |
| 25-40 | 2785 | 0.222 | 0.1275 | +0.0945 ± 0.0042 | 0.6383 | 0.392 | 0.5333 | 0.2201 | 0.2298 | -0.066 ± 0.0065 | -0.01 (1) |
| 40+ | 1859 | 0.3791 | 0.0426 | +0.3365 ± 0.0054 | 0.9874 | 0.1694 | 0.6288 | 0.1067 | 0.0559 | -0.088 ± 0.0045 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 388 | 0.2011 | 0.2017 | -0.0006 ± 0.0008 | 0.5844 | 0.5858 | 0.5041 | 0.489 | 0.5129 | -0.084 ± 0.0243 | -0.01 (3) |
| 3-5 | 281 | 0.2152 | 0.2149 | +0.0003 ± 0.0022 | 0.6135 | 0.6138 | 0.5162 | 0.4763 | 0.4875 | -0.087 ± 0.0294 | 0.02 (1) |
| 5-10 | 609 | 0.1988 | 0.1985 | +0.0004 ± 0.0027 | 0.5812 | 0.5801 | 0.5456 | 0.4707 | 0.5057 | -0.074 ± 0.0186 | -0.01 (4) |
| 10-15 | 563 | 0.2176 | 0.2124 | +0.0052 ± 0.0049 | 0.6254 | 0.6113 | 0.5699 | 0.4455 | 0.4902 | -0.090 ± 0.0202 | -0.04 (5) |
| 15-25 | 819 | 0.2303 | 0.21 | +0.0202 ± 0.0063 | 0.6524 | 0.6028 | 0.5912 | 0.395 | 0.4457 | -0.095 ± 0.0163 | -0.0133 (9) |
| 25-40 | 544 | 0.2658 | 0.1977 | +0.0681 ± 0.012 | 0.7412 | 0.5764 | 0.6659 | 0.3507 | 0.4007 | -0.124 ± 0.0188 | -0.0075 (4) |
| 40+ | 200 | 0.3687 | 0.1766 | +0.1921 ± 0.0295 | 1.0263 | 0.5244 | 0.7457 | 0.2628 | 0.32 | -0.082 ± 0.0287 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2092 | 0.1856 | 0.1862 | -0.0006 ± 0.0003 | 0.5474 | 0.5485 | 0.5031 | 0.4884 | 0.512 | -0.034 ± 0.0098 | -0.0133 (15) |
| 3-5 | 1318 | 0.1958 | 0.195 | +0.0008 ± 0.001 | 0.5675 | 0.5655 | 0.5167 | 0.4768 | 0.4863 | -0.045 ± 0.0124 | 0.02 (1) |
| 5-10 | 2985 | 0.1913 | 0.1894 | +0.0019 ± 0.0012 | 0.5649 | 0.5571 | 0.5078 | 0.4338 | 0.4593 | -0.037 ± 0.0081 | -0.0117 (6) |
| 10-15 | 2617 | 0.1999 | 0.1899 | +0.0100 ± 0.0021 | 0.5882 | 0.5526 | 0.5214 | 0.3968 | 0.4215 | -0.047 ± 0.0086 | -0.0189 (18) |
| 15-25 | 3737 | 0.218 | 0.1809 | +0.0371 ± 0.0027 | 0.6308 | 0.5307 | 0.532 | 0.3359 | 0.3431 | -0.069 ± 0.007 | -0.0086 (42) |
| 25-40 | 3277 | 0.2509 | 0.137 | +0.1139 ± 0.0041 | 0.7082 | 0.4201 | 0.5636 | 0.2476 | 0.2267 | -0.091 ± 0.0064 | -0.0044 (18) |
| 40+ | 2564 | 0.4021 | 0.066 | +0.3361 ± 0.0058 | 1.0615 | 0.2305 | 0.6632 | 0.1261 | 0.0952 | -0.071 ± 0.005 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 502 | 0.1983 | 0.2009 | -0.0026 ± 0.0007 | 0.5776 | 0.5837 | 0.499 | 0.4837 | 0.5578 | -0.012 ± 0.0203 | -0.0137 (8) |
| 3-5 | 367 | 0.1931 | 0.1908 | +0.0023 ± 0.0018 | 0.5636 | 0.5583 | 0.4995 | 0.4599 | 0.4523 | -0.119 ± 0.0239 | 0.0067 (3) |
| 5-10 | 737 | 0.202 | 0.1986 | +0.0033 ± 0.0025 | 0.5909 | 0.5796 | 0.5075 | 0.4336 | 0.445 | -0.096 ± 0.0169 | -0.0071 (7) |
| 10-15 | 591 | 0.2094 | 0.2067 | +0.0027 ± 0.0046 | 0.6066 | 0.5965 | 0.5417 | 0.4186 | 0.4721 | -0.077 ± 0.0185 | -0.0317 (6) |
| 15-25 | 694 | 0.2344 | 0.21 | +0.0244 ± 0.0068 | 0.6677 | 0.604 | 0.5895 | 0.3963 | 0.4294 | -0.117 ± 0.0174 | -0.03 (1) |
| 25-40 | 428 | 0.2045 | 0.216 | -0.0115 ± 0.0129 | 0.5938 | 0.6163 | 0.662 | 0.3523 | 0.5234 | -0.040 ± 0.0197 | 0.015 (2) |
| 40+ | 85 | 0.3246 | 0.1885 | +0.1362 ± 0.0425 | 0.8809 | 0.5541 | 0.7597 | 0.3066 | 0.3882 | -0.123 ± 0.0444 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2364 | 0.1889 | 0.1899 | -0.0010 ± 0.0003 | 0.5549 | 0.5568 | 0.4882 | 0.4729 | 0.5 | -0.028 ± 0.009 | -0.0163 (35) |
| 3-5 | 1635 | 0.1896 | 0.1864 | +0.0032 ± 0.0009 | 0.5572 | 0.5495 | 0.4769 | 0.4374 | 0.4177 | -0.082 ± 0.011 | -0.0094 (18) |
| 5-10 | 3576 | 0.1959 | 0.1895 | +0.0063 ± 0.0011 | 0.5762 | 0.5555 | 0.4835 | 0.4096 | 0.4016 | -0.069 ± 0.0073 | -0.01 (31) |
| 10-15 | 2773 | 0.1974 | 0.1809 | +0.0165 ± 0.002 | 0.5799 | 0.5315 | 0.5006 | 0.3772 | 0.3725 | -0.072 ± 0.008 | -0.015 (12) |
| 15-25 | 3713 | 0.2089 | 0.1716 | +0.0373 ± 0.0027 | 0.6111 | 0.5075 | 0.5083 | 0.3135 | 0.3156 | -0.070 ± 0.0068 | -0.03 (2) |
| 25-40 | 2738 | 0.216 | 0.1261 | +0.0898 ± 0.0043 | 0.6247 | 0.3873 | 0.5308 | 0.215 | 0.2345 | -0.059 ± 0.0064 | 0.01 (3) |
| 40+ | 1791 | 0.3943 | 0.0473 | +0.3469 ± 0.0058 | 1.0292 | 0.1818 | 0.6401 | 0.112 | 0.0592 | -0.090 ± 0.0049 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 846 | 0.197 | 0.1972 | -0.0002 ± 0.0005 | 0.5747 | 0.5748 | 0.507 | 0.4919 | 0.4965 | -0.054 ± 0.0154 | -0.0224 (49) |
| 3-5 | 597 | 0.1943 | 0.1937 | +0.0006 ± 0.0015 | 0.5668 | 0.5643 | 0.4823 | 0.4425 | 0.4523 | -0.053 ± 0.0182 | -0.0194 (34) |
| 5-10 | 1243 | 0.1991 | 0.1929 | +0.0062 ± 0.0019 | 0.5856 | 0.5678 | 0.4894 | 0.416 | 0.4111 | -0.069 ± 0.0127 | -0.005 (78) |
| 10-15 | 800 | 0.208 | 0.1966 | +0.0115 ± 0.0039 | 0.6039 | 0.5749 | 0.5122 | 0.389 | 0.4025 | -0.063 ± 0.0159 | 0.0014 (64) |
| 15-25 | 1071 | 0.2335 | 0.2125 | +0.0210 ± 0.0055 | 0.6651 | 0.6113 | 0.5704 | 0.3753 | 0.4202 | -0.063 ± 0.0141 | -0.0214 (59) |
| 25-40 | 638 | 0.2448 | 0.2012 | +0.0436 ± 0.0109 | 0.6946 | 0.5813 | 0.6588 | 0.3464 | 0.431 | -0.081 ± 0.0164 | -0.0219 (26) |
| 40+ | 221 | 0.355 | 0.1936 | +0.1614 ± 0.0297 | 1.0268 | 0.5683 | 0.8034 | 0.3163 | 0.4163 | -0.084 ± 0.0262 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2632 | 0.1882 | 0.1883 | -0.0001 ± 0.0003 | 0.5515 | 0.5508 | 0.5051 | 0.4898 | 0.4985 | -0.038 ± 0.0085 | -0.0157 (88) |
| 3-5 | 1820 | 0.1915 | 0.1888 | +0.0026 ± 0.0008 | 0.5594 | 0.5532 | 0.4889 | 0.4493 | 0.4363 | -0.061 ± 0.0103 | -0.0209 (69) |
| 5-10 | 3623 | 0.1958 | 0.1872 | +0.0087 ± 0.0011 | 0.5765 | 0.5526 | 0.4874 | 0.414 | 0.3941 | -0.072 ± 0.0073 | -0.0082 (132) |
| 10-15 | 2489 | 0.2037 | 0.1893 | +0.0144 ± 0.0022 | 0.5943 | 0.5569 | 0.5184 | 0.3954 | 0.3973 | -0.059 ± 0.0087 | -0.0053 (105) |
| 15-25 | 3101 | 0.2289 | 0.1984 | +0.0305 ± 0.0031 | 0.6594 | 0.5769 | 0.5633 | 0.3679 | 0.3889 | -0.063 ± 0.0081 | -0.0253 (107) |
| 25-40 | 2120 | 0.2499 | 0.1746 | +0.0753 ± 0.0057 | 0.7102 | 0.5132 | 0.6177 | 0.3041 | 0.3443 | -0.071 ± 0.0088 | -0.0229 (51) |
| 40+ | 993 | 0.3813 | 0.134 | +0.2473 ± 0.0123 | 1.083 | 0.4084 | 0.7187 | 0.2146 | 0.2356 | -0.077 ± 0.0109 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3404 | 1.052 ± 0.048 | 1.177 | 0.168 | 0.1651 | 0.2128 | 0.2038 |
| gen2 | 3404 | 0.836 ± 0.044 | 1.136 | 0.174 | 0.1651 | 0.2318 | 0.2039 |
| gen1_elo | 3404 | 1.033 ± 0.047 | 1.161 | 0.1737 | 0.1655 | 0.2118 | 0.2038 |
| gen1_sr | 3404 | 1.039 ± 0.057 | 1.206 | 0.134 | 0.1669 | 0.2277 | 0.2036 |
| gen1_ledger | 5416 | 0.878 ± 0.033 | 1.083 | 0.1785 | 0.1807 | 0.2181 | 0.1991 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 16,489)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,879 | 23.5% |
| STALE_QUOTE | market_freshness | 3,378 | 20.5% |
| BOOK_QUALITY | execution | 3,246 | 19.7% |
| POOR_DATA | data | 1,818 | 11.0% |
| LIMITED_DATA | data | 1,118 | 6.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 875 | 5.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 816 | 5.0% |
| IDENTITY_AMBIGUOUS | mapping | 664 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 466 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 229 | 1.4% |

Cause class: coverage 23.5%, market_freshness 20.5%, execution 19.7%, data 17.8%, market_freshness/coverage 8.1%, model_calibration_or_unknown 5.0%, mapping 4.0%, model_calibration 1.4%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.5%, START_UNVERIFIABLE 94.4%, LOW_DATA_QUALITY 69.8%, THIN_PLAYER_HISTORY 58.1%, STALE_PLAYER_DATA 51.8%, STALE_KALSHI_QUOTE 43.5%, MODEL_INTERNAL_DISAGREEMENT 40.4%, ASYMMETRIC_SAMPLE_SIZE 32.4%, WIDE_SPREAD 25.7%, MODEL_HIGH_UNCERTAINTY 17.9%, PLAYER_IDENTITY_RISK 15.1%, LEVEL_TRANSFER_RISK 9.2%, EVENT_MAPPING_RISK 8.6%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 2.4%, UNKNOWN 1.0%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.9%, POST_SETTLEMENT_OBSERVATION 23.5%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 8,786)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,067 | 34.9% |
| BOOK_QUALITY | execution | 1,702 | 19.4% |
| STALE_QUOTE | market_freshness | 1,566 | 17.8% |
| POOR_DATA | data | 771 | 8.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 464 | 5.3% |
| IDENTITY_AMBIGUOUS | mapping | 376 | 4.3% |
| LIMITED_DATA | data | 328 | 3.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 287 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 177 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 48 | 0.5% |

Cause class: coverage 34.9%, execution 19.4%, market_freshness 17.8%, data 12.5%, market_freshness/coverage 8.6%, mapping 4.3%, model_calibration_or_unknown 2.0%, model_calibration 0.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.7%, START_UNVERIFIABLE 97.4%, LOW_DATA_QUALITY 73.9%, THIN_PLAYER_HISTORY 60.7%, STALE_KALSHI_QUOTE 51.7%, STALE_PLAYER_DATA 47.3%, MODEL_INTERNAL_DISAGREEMENT 41.2%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 25.5%, PLAYER_IDENTITY_RISK 18.4%, MODEL_HIGH_UNCERTAINTY 18.1%, EVENT_MAPPING_RISK 10.4%, LEVEL_TRANSFER_RISK 8.2%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 5.2%, EXTERNAL_MARKET_REJECTION 1.3%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.7%, POST_SETTLEMENT_OBSERVATION 34.9%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 6940, "IDENTITY_AMBIGUOUS": 1846}; ticker orientation: {"VERIFIED": 8786}.

Checks: discipline:AMBIGUOUS 654, discipline:PASS 8132, identity_confidence:AMBIGUOUS 1616, identity_confidence:PASS 7170, level_mapping:NA 666, level_mapping:PASS 8120, market_pair:AMBIGUOUS 320, market_pair:NA 215, market_pair:PASS 8251, model_complement:NA 182, model_complement:PASS 8604, namesake:PASS 8786, physical_match_id:NA 3348, physical_match_id:PASS 5438, player_ids:PASS 8786, same_pair_other_event:PASS 8786, ticker_orientation:PASS 8786

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,115 | 3.9% | 3.6% | 1.4% | {"market_freshness": 40, "data": 29, "model_calibration_or_unknown": 18, "execution": 15, "market_freshness/coverage": 8, "model_calibration": 8, "coverage": 2} | 5.82 | 0.2157 / 0.2106 (333) | 17.9% | 3.4% | 4.0% | 2.3% |
| CHALLENGER | 6,477 | 16.9% | 6.5% | 12.5% | {"coverage": 628, "market_freshness/coverage": 137, "market_freshness": 133, "data": 99, "model_calibration_or_unknown": 50, "execution": 26, "mapping": 12, "model_calibration": 10} | 7.31 | 0.2168 / 0.207 (1598) | 35.5% | 15.4% | 3.5% | 22.0% |
| DOUBLES | 1,340 | 48.8% | 48.4% | 7.4% | {"execution": 325, "mapping": 171, "market_freshness": 106, "market_freshness/coverage": 45, "coverage": 7} | 24.07 | 0.3224 / 0.2341 (343) | 17.5% | 0.0% | 100.0% | 7.2% |
| ITF_MEN | 11,007 | 24.6% | 16.8% | 30.9% | {"coverage": 1063, "execution": 554, "market_freshness": 417, "data": 358, "market_freshness/coverage": 222, "mapping": 96, "model_calibration_or_unknown": 2} | 11.21 | 0.2149 / 0.1951 (2674) | 36.3% | 62.2% | 13.8% | 22.9% |
| ITF_WOMEN | 14,681 | 26.6% | 19.8% | 44.5% | {"coverage": 1350, "market_freshness": 794, "execution": 752, "data": 579, "market_freshness/coverage": 290, "mapping": 91, "model_calibration_or_unknown": 43, "model_calibration": 10} | 12.83 | 0.2019 / 0.1936 (2961) | 38.2% | 57.9% | 10.3% | 21.8% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,331 | 4.7% | 4.3% | 1.2% | {"market_freshness": 36, "model_calibration_or_unknown": 23, "execution": 16, "data": 11, "market_freshness/coverage": 10, "model_calibration": 9, "coverage": 4, "mapping": 1} | 7.7 | 0.2399 / 0.2328 (381) | 23.5% | 1.5% | 1.5% | 3.5% |
| WTA125 | 1,392 | 12.5% | 9.9% | 2.0% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 5 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 6 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 7 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | POOR_DATA | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 9 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 10 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 11 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 12 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 13 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 14 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 15 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 16 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 17 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 18 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 19 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 20 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 22 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 463 min (STALE); no external reference |
| 23 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 24 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 25 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 26 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 27 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 28 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 29 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 9.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 553 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 30 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 31 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 32 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 33 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 34 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 468 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 35 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 36 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 37 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 38 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 39 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.2h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 196 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |
| 40 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 33 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 41 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 42 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 43 | `KXITFWMATCH-26OCT16ESTLAB-LAB` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 68 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1475.0, ratio 2.28); no external reference |
| 44 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 46 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 47 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 48 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 49 | `KXATPDOUBLES-26OCT18COLGOFPOLZIE-COLGOF` | DOUBLES | gen1_ledger | 90% / 15% | +75 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9738, "by_level_share_of_ge_25pp": {"ATP": 0.0137, "CHALLENGER": 0.1246, "DOUBLES": 0.0744, "ITF_MEN": 0.3087, "ITF_WOMEN": 0.4449, "OTHER": 0.0014, "WTA": 0.0125, "WTA125": 0.0198}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.517, "share_primary_cause_market_settled_or_in_play": 0.4346, "share_primary_cause_stale_quote_only": 0.1782}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 8786, "identity_ambiguous_share": 0.2101, "ticker_orientation": {"VERIFIED": 8786}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 5438, "with_external": 228, "coverage": 0.0419, "external_status": {"EXTERNAL_STALE": 149, "AGREES_WITH_KALSHI": 76, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 149, "MODEL_LONE_OUTLIER": 76, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3333, "share_external_supports_model": 0.0132}, "pregame_clean_ge_25pp": {"n": 2631, "with_external": 216, "coverage": 0.0821, "external_status": {"EXTERNAL_STALE": 139, "AGREES_WITH_KALSHI": 74, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 139, "MODEL_LONE_OUTLIER": 74, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3426, "share_external_supports_model": 0.0139}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 531.5, "median_sample_ratio": 2.46, "median_min_matches": 21.0, "median_max_days_since_last": 218.0, "share_severe_asymmetry": 0.2074, "data_status": {"POOR": 4757, "LIMITED": 2489, "ADEQUATE": 1540}, "comparison_lt_10pp": {"median_thinner_serve_points": 1822.0, "median_sample_ratio": 1.67, "median_min_matches": 95.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 680, "model_minus_observed": 0.0506, "kalshi_minus_observed": -0.0837, "brier_diff_model_minus_kalshi": -0.0009}, "4-10x": {"n": 462, "model_minus_observed": 0.0742, "kalshi_minus_observed": -0.0675, "brier_diff_model_minus_kalshi": 0.0078}, "<2x": {"n": 1689, "model_minus_observed": 0.0875, "kalshi_minus_observed": -0.0335, "brier_diff_model_minus_kalshi": 0.0122}, ">=10x": {"n": 573, "model_minus_observed": 0.1157, "kalshi_minus_observed": -0.057, "brier_diff_model_minus_kalshi": 0.0119}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3404, "model": {"intercept": -0.522, "slope": 0.836, "slope_se": 0.044}, "kalshi_mid_same_rows": {"intercept": 0.239, "slope": 1.136, "slope_se": 0.051}, "mean_extremity_model": 0.174, "mean_extremity_kalshi": 0.1651, "model_brier": 0.2318, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0279, "brier_diff_se": 0.0032, "model_logloss": 0.6604, "kalshi_logloss": 0.5903}, "fair_v1": {"n": 3404, "model": {"intercept": -0.4, "slope": 1.052, "slope_se": 0.048}, "kalshi_mid_same_rows": {"intercept": 0.315, "slope": 1.177, "slope_se": 0.051}, "mean_extremity_model": 0.168, "mean_extremity_kalshi": 0.1651, "model_brier": 0.2128, "kalshi_brier": 0.2038, "brier_diff_model_minus_kalshi": 0.009, "brier_diff_se": 0.0026, "model_logloss": 0.6135, "kalshi_logloss": 0.59}, "gen1_elo": {"n": 3404, "model": {"intercept": -0.39, "slope": 1.033, "slope_se": 0.047}, "kalshi_mid_same_rows": {"intercept": 0.309, "slope": 1.161, "slope_se": 0.051}, "mean_extremity_model": 0.1737, "mean_extremity_kalshi": 0.1655, "model_brier": 0.2118, "kalshi_brier": 0.2038, "brier_diff_model_minus_kalshi": 0.008, "brier_diff_se": 0.0026, "model_logloss": 0.612, "kalshi_logloss": 0.5898}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2404, "share_ge_15": 0.4346, "median_abs_gap": 12.94, "n": 22622}, "gen1_elo": {"share_ge_25": 0.2364, "share_ge_15": 0.4306, "median_abs_gap": 12.53, "n": 22622}, "gen1_sr": {"share_ge_25": 0.3019, "share_ge_15": 0.516, "median_abs_gap": 15.54, "n": 22622}, "gen2": {"share_ge_25": 0.3059, "share_ge_15": 0.5051, "median_abs_gap": 15.27, "n": 22622}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1495, "share_ge_15": 0.3495, "median_abs_gap": 10.71, "n": 17595}, "gen1_elo": {"share_ge_25": 0.1492, "share_ge_15": 0.3421, "median_abs_gap": 10.27, "n": 17594}, "gen1_sr": {"share_ge_25": 0.2103, "share_ge_15": 0.4393, "median_abs_gap": 13.01, "n": 17595}, "gen2": {"share_ge_25": 0.2266, "share_ge_15": 0.4394, "median_abs_gap": 12.99, "n": 17596}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.82, "share_ge_25_all": 0.0385, "share_ge_25_pregame_clean": 0.0361}, "WTA": {"median_abs_gap_pregame_clean": 7.7, "share_ge_25_all": 0.0472, "share_ge_25_pregame_clean": 0.0427}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2392, "share_within_10pp_all": 0.4387, "share_within_10pp_pregame_clean": 0.4924, "corr_model_vs_mid_pregame_clean": 0.8417}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 518, "model_brier": 0.1963, "kalshi_brier": 0.1975, "brier_diff_model_minus_kalshi": -0.0013}, "10-15": {"n_settled": 607, "model_brier": 0.2152, "kalshi_brier": 0.2061, "brier_diff_model_minus_kalshi": 0.009}, "15-25": {"n_settled": 742, "model_brier": 0.2265, "kalshi_brier": 0.2129, "brier_diff_model_minus_kalshi": 0.0136}, "25-40": {"n_settled": 416, "model_brier": 0.2209, "kalshi_brier": 0.2106, "brier_diff_model_minus_kalshi": 0.0102}, "3-5": {"n_settled": 325, "model_brier": 0.1975, "kalshi_brier": 0.1968, "brier_diff_model_minus_kalshi": 0.0007}, "40+": {"n_settled": 85, "model_brier": 0.3039, "kalshi_brier": 0.1748, "brier_diff_model_minus_kalshi": 0.1291}, "5-10": {"n_settled": 711, "model_brier": 0.1999, "kalshi_brier": 0.1997, "brier_diff_model_minus_kalshi": 0.0002}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.522, "slope": 0.836, "slope_se": 0.044}, "kalshi_slope": {"intercept": 0.239, "slope": 1.136, "slope_se": 0.051}, "n": 3404}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.513, "slope": 0.878, "slope_se": 0.033}, "kalshi_slope": {"intercept": 0.154, "slope": 1.083, "slope_se": 0.038}, "n": 5416}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 343, "model_brier": 0.3224, "kalshi_brier": 0.2341, "brier_diff_model_minus_kalshi": 0.0883, "brier_diff_se": 0.0169, "corr_model_outcome": 0.0105, "corr_kalshi_outcome": 0.2599}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
