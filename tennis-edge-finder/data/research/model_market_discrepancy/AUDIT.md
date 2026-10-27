# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-27T06:10Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 57,978): 0-3 14.0%, 3-5 9.6%, 5-10 19.9%, 10-15 15.4%, 15-25 19.2%, 25-40 13.9%, 40+ 8.0%; median gap 11.97 pp.
* **Where the extremes live**: 96.7% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.4%, Challenger 11.7%, doubles 6.8%). Main tour: ATP 4.4% and WTA 5.6% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 12,718): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.3%, STALE_QUOTE 19.1%, BOOK_QUALITY 19.1%, POOR_DATA 8.7%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.4%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.3%, market_freshness 19.1%, execution 19.1%, data 12.2%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 51.6% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.2% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 12,718 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.0% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 467.0 points vs 1787.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.034, Gen-2 0.827, Gen-1 ledger 0.866 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 613 model 0.2205 vs Kalshi 0.209; n 121 model 0.2699 vs Kalshi 0.2006.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 254,882 model-market comparisons (411,821 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 85,325 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-27T05:55:23.328987+00:00'], shadow board 66,685 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-27T05:55:27.056659+00:00'], Model 4 33,170 rows, 21,286 settled tickers, 7,611 tickers with an external scan.
* By model: {"gen1_ledger": 58320, "gen1_elo": 33531, "fair_v1": 33531, "gen2": 33531, "gen1_sr": 33531, "model4_fundamental": 31241, "model4_conditioned": 31197}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 57,978 | 14.0 | 9.6 | 19.9 | 15.4 | 19.2 | 13.9 | 8.0 | 11.97 | 41.1% | 21.9% |
| MW fair_v1 | 33,531 | 12.9 | 8.7 | 18.6 | 15.6 | 19.7 | 14.8 | 9.7 | 13.05 | 44.2% | 24.5% |
| MW gen1_elo | 33,531 | 12.8 | 8.5 | 19.2 | 15.4 | 19.9 | 14.8 | 9.5 | 12.92 | 44.1% | 24.2% |
| MW gen1_ledger | 24,447 | 15.5 | 10.7 | 21.7 | 15.2 | 18.5 | 12.7 | 5.8 | 10.5 | 36.9% | 18.4% |
| MW gen1_sr | 33,531 | 10.2 | 7.2 | 16.9 | 13.7 | 20.7 | 18.6 | 12.7 | 15.87 | 52.0% | 31.3% |
| MW gen2 | 33,531 | 11.1 | 7.4 | 16.3 | 13.9 | 19.5 | 17.9 | 13.8 | 15.5 | 51.2% | 31.7% |
| all families model4_conditioned | 31,197 | 21.9 | 18.3 | 34.5 | 17.5 | 4.9 | 1.8 | 1.1 | 6.06 | 7.8% | 2.9% |
| all families model4_fundamental | 31,241 | 16.8 | 13.2 | 34.1 | 20.6 | 10.3 | 3.7 | 1.3 | 7.81 | 15.4% | 5.0% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.5%, >=15pp 41.1%, >=20pp 30.5%, >=25pp 21.9%, >=30pp 15.8%, >=40pp 8.0%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.32pp; >=10pp 44.8%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,118 | 27.2 | 15.2 | 26.8 | 14.4 | 11.6 | 4.3 | 0.6 | 6.0 | 16.5% | 4.9% |
| CHALLENGER | 5,315 | 15.9 | 9.9 | 20.3 | 15.8 | 15.6 | 12.1 | 10.4 | 11.06 | 38.1% | 22.5% |
| ITF_MEN | 8,930 | 10.0 | 7.2 | 16.6 | 14.6 | 21.8 | 17.6 | 12.3 | 15.55 | 51.7% | 29.9% |
| ITF_WOMEN | 13,072 | 9.6 | 7.0 | 15.9 | 15.2 | 22.5 | 18.2 | 11.7 | 15.74 | 52.4% | 30.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,223 | 16.8 | 13.9 | 25.2 | 20.6 | 16.6 | 6.3 | 0.6 | 8.39 | 23.5% | 6.9% |
| WTA125 | 867 | 14.7 | 7.4 | 22.1 | 21.2 | 20.3 | 12.3 | 2.0 | 11.13 | 34.6% | 14.3% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,118 | 24.9 | 15.3 | 25.5 | 17.2 | 12.0 | 4.3 | 0.8 | 6.48 | 17.1% | 5.1% |
| CHALLENGER | 5,315 | 15.0 | 8.8 | 18.1 | 14.7 | 18.2 | 13.9 | 11.3 | 12.69 | 43.4% | 25.2% |
| ITF_MEN | 8,930 | 8.0 | 5.9 | 14.2 | 12.9 | 19.8 | 21.2 | 17.9 | 18.85 | 59.0% | 39.2% |
| ITF_WOMEN | 13,072 | 8.1 | 5.6 | 13.8 | 12.9 | 20.7 | 21.2 | 17.6 | 19.21 | 59.6% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,223 | 14.3 | 10.5 | 22.7 | 16.0 | 22.4 | 13.0 | 1.2 | 10.71 | 36.5% | 14.1% |
| WTA125 | 867 | 8.2 | 6.6 | 15.9 | 18.2 | 24.2 | 18.0 | 8.9 | 15.49 | 51.1% | 26.9% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,118 | 22.9 | 12.4 | 24.7 | 16.2 | 16.1 | 6.5 | 1.4 | 7.58 | 23.9% | 7.9% |
| CHALLENGER | 5,315 | 14.4 | 9.3 | 21.2 | 15.9 | 16.1 | 12.5 | 10.7 | 11.35 | 39.2% | 23.1% |
| ITF_MEN | 8,930 | 9.7 | 7.2 | 16.6 | 13.9 | 22.2 | 17.9 | 12.5 | 16.01 | 52.6% | 30.4% |
| ITF_WOMEN | 13,072 | 9.4 | 6.6 | 16.3 | 15.9 | 22.7 | 18.1 | 10.9 | 15.56 | 51.8% | 29.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,223 | 23.8 | 16.6 | 31.2 | 15.2 | 9.5 | 2.6 | 1.1 | 6.07 | 13.2% | 3.6% |
| WTA125 | 867 | 22.7 | 11.5 | 26.3 | 16.7 | 16.3 | 6.1 | 0.3 | 8.01 | 22.7% | 6.5% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,841 | 24.8 | 19.2 | 30.4 | 12.8 | 9.2 | 3.1 | 0.4 | 5.73 | 12.8% | 3.6% |
| CHALLENGER | 3,697 | 21.7 | 14.3 | 26.9 | 14.8 | 14.4 | 6.3 | 1.6 | 7.32 | 22.3% | 8.0% |
| DOUBLES | 1,828 | 5.2 | 4.5 | 12.1 | 10.3 | 20.5 | 25.6 | 21.8 | 23.91 | 67.8% | 47.4% |
| ITF_MEN | 6,675 | 13.2 | 9.1 | 20.0 | 16.1 | 21.5 | 13.5 | 6.6 | 12.27 | 41.6% | 20.1% |
| ITF_WOMEN | 8,066 | 12.7 | 8.9 | 19.4 | 15.4 | 21.5 | 16.2 | 5.9 | 12.77 | 43.6% | 22.2% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,299 | 23.4 | 15.6 | 30.2 | 17.9 | 9.6 | 3.1 | 0.3 | 6.79 | 12.9% | 3.4% |
| WTA125 | 892 | 22.1 | 13.0 | 21.6 | 18.6 | 14.3 | 8.3 | 2.0 | 8.35 | 24.7% | 10.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,038 | 27.5 | 15.4 | 27.2 | 14.2 | 11.4 | 3.9 | 0.4 | 5.92 | 15.7% | 4.3% |
| CHALLENGER | 3,783 | 20.5 | 12.3 | 25.0 | 18.4 | 15.6 | 6.6 | 1.7 | 8.41 | 23.8% | 8.3% |
| ITF_MEN | 6,568 | 12.0 | 8.7 | 19.8 | 16.6 | 23.0 | 14.4 | 5.6 | 12.84 | 42.9% | 20.0% |
| ITF_WOMEN | 9,851 | 11.3 | 8.2 | 18.1 | 17.2 | 24.3 | 15.4 | 5.4 | 13.56 | 45.2% | 20.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,162 | 17.0 | 13.7 | 25.2 | 20.9 | 16.6 | 6.0 | 0.6 | 8.39 | 23.2% | 6.6% |
| WTA125 | 837 | 14.9 | 7.3 | 21.7 | 21.5 | 20.9 | 11.9 | 1.7 | 11.13 | 34.5% | 13.6% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,038 | 25.1 | 15.6 | 25.7 | 17.1 | 11.9 | 4.0 | 0.5 | 6.31 | 16.4% | 4.5% |
| CHALLENGER | 3,783 | 19.1 | 11.0 | 22.4 | 17.4 | 18.6 | 9.6 | 2.0 | 9.4 | 30.2% | 11.6% |
| ITF_MEN | 6,569 | 9.5 | 7.0 | 16.5 | 14.9 | 21.7 | 19.4 | 11.0 | 15.65 | 52.1% | 30.3% |
| ITF_WOMEN | 9,852 | 9.1 | 6.4 | 15.3 | 14.4 | 22.7 | 20.8 | 11.3 | 16.89 | 54.8% | 32.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,162 | 14.3 | 10.5 | 22.8 | 16.1 | 22.4 | 12.8 | 1.2 | 10.74 | 36.4% | 14.0% |
| WTA125 | 837 | 8.1 | 6.6 | 16.0 | 18.6 | 24.1 | 18.4 | 8.1 | 15.19 | 50.7% | 26.5% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,788 | 24.9 | 19.5 | 30.4 | 13.0 | 8.9 | 3.0 | 0.3 | 5.66 | 12.2% | 3.4% |
| CHALLENGER | 3,254 | 23.1 | 15.2 | 28.1 | 14.9 | 13.8 | 4.4 | 0.5 | 6.81 | 18.6% | 4.9% |
| DOUBLES | 1,708 | 5.2 | 4.6 | 12.4 | 10.4 | 20.3 | 25.5 | 21.6 | 23.85 | 67.4% | 47.1% |
| ITF_MEN | 5,633 | 14.2 | 9.6 | 21.6 | 16.9 | 21.5 | 11.9 | 4.2 | 11.4 | 37.6% | 16.2% |
| ITF_WOMEN | 6,776 | 13.4 | 9.4 | 20.6 | 16.2 | 21.7 | 15.1 | 3.5 | 11.82 | 40.3% | 18.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,245 | 23.8 | 16.0 | 30.2 | 18.0 | 9.6 | 2.4 | 0.1 | 6.68 | 12.0% | 2.5% |
| WTA125 | 777 | 23.8 | 14.2 | 22.9 | 19.8 | 13.0 | 5.7 | 0.6 | 7.74 | 19.3% | 6.3% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,828 | 5.2 | 4.5 | 12.1 | 10.3 | 20.5 | 25.6 | 21.8 | 23.91 | 67.8% | 47.4% |
| singles | 22,619 | 16.3 | 11.2 | 22.5 | 15.6 | 18.3 | 11.6 | 4.5 | 9.99 | 34.4% | 16.1% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,253 | 12.7 | 9.2 | 19.8 | 15.9 | 18.9 | 14.0 | 9.5 | 12.6 | 42.4% | 23.5% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 21,257 | 13.5 | 8.8 | 18.5 | 15.2 | 19.8 | 14.8 | 9.4 | 12.99 | 44.0% | 24.2% |
| UNKNOWN | 4,772 | 10.9 | 7.4 | 17.0 | 16.6 | 20.7 | 16.1 | 11.3 | 14.12 | 48.0% | 27.4% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,712 | 19.7 | 12.3 | 22.1 | 16.3 | 14.6 | 9.1 | 5.9 | 8.77 | 29.6% | 15.0% |
| B | 4,124 | 12.5 | 8.7 | 19.4 | 16.4 | 19.6 | 12.8 | 10.6 | 12.64 | 43.0% | 23.4% |
| C | 4,617 | 11.7 | 9.0 | 19.4 | 15.8 | 19.5 | 14.4 | 10.2 | 13.02 | 44.1% | 24.6% |
| D | 5,092 | 12.2 | 7.9 | 17.5 | 15.3 | 21.8 | 15.6 | 9.8 | 13.96 | 47.2% | 25.4% |
| F | 9,986 | 7.5 | 5.5 | 14.9 | 14.5 | 23.9 | 21.0 | 12.7 | 17.79 | 57.6% | 33.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,957 | 23.6 | 16.0 | 28.9 | 15.1 | 11.2 | 3.9 | 1.3 | 6.55 | 16.4% | 5.2% |
| B | 3,297 | 16.3 | 10.3 | 23.5 | 16.3 | 19.6 | 10.5 | 3.5 | 9.99 | 33.6% | 14.0% |
| C | 4,725 | 10.9 | 7.3 | 18.9 | 14.5 | 21.2 | 16.3 | 10.9 | 14.24 | 48.4% | 27.2% |
| D | 3,353 | 14.1 | 9.7 | 20.5 | 15.2 | 21.0 | 13.7 | 5.8 | 11.83 | 40.5% | 19.5% |
| F | 6,115 | 10.0 | 8.3 | 15.5 | 15.1 | 22.6 | 20.4 | 8.1 | 15.54 | 51.1% | 28.4% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 11,020 | 17.9 | 11.1 | 21.3 | 16.1 | 15.2 | 10.0 | 8.4 | 9.92 | 33.5% | 18.3% |
| LIMITED | 7,087 | 13.6 | 10.1 | 20.0 | 16.3 | 19.6 | 13.2 | 7.3 | 11.87 | 40.1% | 20.5% |
| POOR | 15,424 | 9.1 | 6.4 | 15.9 | 14.8 | 23.1 | 19.1 | 11.7 | 16.26 | 53.8% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,962 | 24.6 | 18.5 | 33.1 | 14.6 | 6.3 | 2.5 | 0.3 | 5.73 | 9.2% | 2.8% |
| GAME_SPREAD | 5,497 | 22.4 | 15.4 | 33.3 | 16.7 | 9.1 | 2.8 | 0.4 | 6.7 | 12.3% | 3.2% |
| MATCH_WINNER | 24,447 | 15.5 | 10.7 | 21.7 | 15.2 | 18.5 | 12.7 | 5.8 | 10.5 | 36.9% | 18.4% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 12,471 | 28.0 | 16.4 | 30.9 | 12.5 | 9.4 | 2.4 | 0.3 | 5.66 | 12.1% | 2.7% |
| TOTAL_GAMES | 8,919 | 9.2 | 10.2 | 36.4 | 27.1 | 10.5 | 4.0 | 2.7 | 9.32 | 17.2% | 6.7% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,133 | 24.5 | 30.9 | 32.7 | 6.9 | 4.0 | 0.8 | 0.2 | 4.67 | 5.1% | 1.0% |
| GAME_SPREAD | 7,308 | 46.5 | 16.5 | 25.9 | 7.6 | 1.9 | 1.1 | 0.5 | 3.35 | 3.5% | 1.6% |
| TOTAL_GAMES | 12,756 | 5.6 | 8.3 | 40.9 | 32.5 | 7.4 | 3.0 | 2.2 | 9.47 | 12.6% | 5.2% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,144 | 23.6 | 16.8 | 35.0 | 14.3 | 7.3 | 2.6 | 0.4 | 6.05 | 10.2% | 2.9% |
| GAME_SPREAD | 7,311 | 19.6 | 13.3 | 28.3 | 21.0 | 12.4 | 4.3 | 1.0 | 7.89 | 17.8% | 5.4% |
| TOTAL_GAMES | 12,786 | 9.2 | 9.8 | 36.5 | 26.0 | 11.8 | 4.2 | 2.4 | 9.34 | 18.4% | 6.6% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 33,531 | 44.2% | 24.5% | 13.05 | 36.0% | 15.5% | 10.88 |
| gen1_elo | 33,531 | 44.1% | 24.2% | 12.92 | 35.8% | 15.5% | 10.71 |
| gen1_sr | 33,531 | 52.0% | 31.3% | 15.87 | 44.4% | 22.2% | 13.01 |
| gen2 | 33,531 | 51.2% | 31.7% | 15.5 | 44.5% | 23.8% | 13.04 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 16,665 | 15.6 | 10.5 | 21.3 | 17.3 | 20.2 | 11.9 | 3.3 | 10.71 | 35.3% | 15.2% |
| STALE | 16,866 | 10.3 | 6.9 | 15.8 | 13.9 | 19.3 | 17.8 | 16.0 | 16.37 | 53.1% | 33.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 17,915 | 16.3 | 11.2 | 22.4 | 15.3 | 17.8 | 12.1 | 4.9 | 10.01 | 34.7% | 17.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 57,978 | 17915 | 20137 | 19926 | 24.1 | 125.1 | 1400.4 |
| ge_15pp | 23,855 | 6222 | 7174 | 10459 | 26.2 | 423.9 | 1399.2 |
| ge_25pp | 12,718 | 3042 | 3116 | 6560 | 31.5 | 572.1 | 1380.4 |
| lt_10pp | 25,195 | 8947 | 9532 | 6716 | 22.4 | 47.5 | 1341.5 |

Current slate `SL-20261027T061055Z-680e988b`: 656 priced rows, quote age at build {'median': 16.1, 'max': 16.1}, freshness {'AGING': 656}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 29 | 0.0 | 0.0 | 20.7 | 10.3 | 41.4 | 27.6 | 0.0 | 20.47 | 69.0% | 27.6% |
| EXTERNAL_LONE_OUTLIER | 18 | 77.8 | 22.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,289 | 19.5 | 11.1 | 25.2 | 18.9 | 17.7 | 6.9 | 0.7 | 8.8 | 25.3% | 7.6% |
| KALSHI_LONE_OUTLIER | 22 | 4.5 | 4.5 | 77.3 | 4.5 | 4.5 | 4.5 | 0.0 | 6.16 | 9.1% | 4.5% |
| MARKETS_AGREE | 655 | 65.5 | 34.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.2 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,412 | 0.0 | 2.6 | 34.9 | 26.8 | 24.9 | 10.1 | 0.6 | 12.14 | 35.6% | 10.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 33,531 | 5425 (16.2%) | 26.0% | 0.9% | {"EXTERNAL_STALE": 3289, "AGREES_WITH_KALSHI": 1412, "ALL_AGREE": 655, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 22, "EXTERNAL_OUTLIER": 18, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 14,834 | 1357 (9.2%) | 37.1% | 1.6% | {"EXTERNAL_STALE": 832, "AGREES_WITH_KALSHI": 503, "SUPPORTS_MODEL_DIRECTION": 20, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 8,214 | 411 (5.0%) | 36.7% | 2.2% | {"EXTERNAL_STALE": 251, "AGREES_WITH_KALSHI": 151, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,068 | 388 (9.5%) | 37.1% | 2.3% | {"EXTERNAL_STALE": 235, "AGREES_WITH_KALSHI": 144, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 13,479 | 3062 (22.7%) | 17.3% | 0.8% | {"EXTERNAL_STALE": 1834, "ALL_AGREE": 655, "AGREES_WITH_KALSHI": 530, "AGREES_WITH_MODEL": 19, "EXTERNAL_OUTLIER": 18, "SUPPORTS_MODEL_DIRECTION": 5, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 6,428 | 10.3 | 7.6 | 19.3 | 14.7 | 22.5 | 15.9 | 9.7 | 14.09 | 48.1% | 25.6% |
| 4-10x | 4,347 | 11.0 | 8.4 | 18.6 | 15.2 | 22.3 | 14.7 | 9.7 | 13.92 | 46.8% | 24.4% |
| <2x | 17,150 | 15.1 | 10.1 | 19.4 | 16.4 | 17.3 | 12.9 | 8.7 | 11.56 | 39.0% | 21.6% |
| >=10x | 5,606 | 10.6 | 6.1 | 15.1 | 14.2 | 22.0 | 19.6 | 12.4 | 16.52 | 54.0% | 32.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 8,513 | 12.8 | 8.6 | 19.3 | 16.2 | 19.1 | 13.6 | 10.4 | 12.8 | 43.1% | 24.0% |
| 300-1000 | 6,999 | 11.8 | 8.8 | 17.3 | 15.3 | 20.9 | 16.2 | 9.8 | 13.83 | 46.9% | 25.9% |
| <300 | 10,925 | 8.4 | 5.7 | 15.3 | 14.7 | 23.4 | 20.1 | 12.5 | 17.04 | 55.9% | 32.5% |
| >=3000 | 7,094 | 21.2 | 13.5 | 23.9 | 16.4 | 13.7 | 6.9 | 4.4 | 7.69 | 25.0% | 11.3% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 950 | 0.5525 | 0.4147 | 0.5053 | +0.047 | -0.091 | -0.0038 ± 0.005 |
| ratio 4-10x | 638 | 0.5875 | 0.4412 | 0.5016 | +0.086 | -0.060 | 0.0091 ± 0.0063 |
| ratio <2x | 2323 | 0.5396 | 0.4167 | 0.4494 | +0.090 | -0.033 | 0.011 ± 0.003 |
| ratio >=10x | 850 | 0.5723 | 0.397 | 0.4612 | +0.111 | -0.064 | 0.0087 ± 0.0063 |
| thinner_sample 1000-3000 | 1286 | 0.5414 | 0.4149 | 0.4518 | +0.090 | -0.037 | 0.0088 ± 0.004 |
| thinner_sample 300-1000 | 1069 | 0.5698 | 0.4272 | 0.4939 | +0.076 | -0.067 | 0.0011 ± 0.0049 |
| thinner_sample <300 | 1608 | 0.5635 | 0.3967 | 0.4683 | +0.095 | -0.072 | 0.0084 ± 0.0044 |
| thinner_sample >=3000 | 798 | 0.5364 | 0.4418 | 0.4687 | +0.068 | -0.027 | 0.0117 ± 0.0041 |
| data_status ADEQUATE | 1367 | 0.5377 | 0.4336 | 0.4521 | +0.086 | -0.018 | 0.0119 ± 0.0033 |
| data_status LIMITED | 1099 | 0.5517 | 0.4187 | 0.4895 | +0.062 | -0.071 | 0.0019 ± 0.0045 |
| data_status POOR | 2295 | 0.5657 | 0.4043 | 0.4706 | +0.095 | -0.066 | 0.0074 ± 0.0036 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 699 | 0.2021 | 0.2028 | -0.0007 ± 0.0006 | 0.5853 | 0.5868 | 0.5027 | 0.4877 | 0.5179 | -0.080 ± 0.0181 | -0.01 (5) |
| 3-5 | 434 | 0.2043 | 0.2039 | +0.0004 ± 0.0018 | 0.5915 | 0.5891 | 0.5047 | 0.4647 | 0.4793 | -0.103 ± 0.0223 | 0.02 (1) |
| 5-10 | 985 | 0.2019 | 0.2023 | -0.0004 ± 0.0022 | 0.5902 | 0.5885 | 0.515 | 0.441 | 0.4761 | -0.090 ± 0.0148 | -0.0167 (6) |
| 10-15 | 830 | 0.2185 | 0.2098 | +0.0088 ± 0.004 | 0.6288 | 0.6023 | 0.5327 | 0.4087 | 0.4337 | -0.107 ± 0.0159 | -0.048 (5) |
| 15-25 | 1079 | 0.2261 | 0.2137 | +0.0123 ± 0.0055 | 0.648 | 0.6111 | 0.5783 | 0.3825 | 0.4495 | -0.097 ± 0.0141 | -0.0033 (9) |
| 25-40 | 613 | 0.2205 | 0.209 | +0.0115 ± 0.011 | 0.6299 | 0.6005 | 0.6586 | 0.3487 | 0.4829 | -0.072 ± 0.0168 | -0.01 (1) |
| 40+ | 121 | 0.2699 | 0.2006 | +0.0693 ± 0.035 | 0.7406 | 0.5869 | 0.761 | 0.3143 | 0.4628 | -0.072 ± 0.0342 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3624 | 0.1847 | 0.1855 | -0.0008 ± 0.0002 | 0.5449 | 0.5457 | 0.4895 | 0.4744 | 0.503 | -0.027 ± 0.0073 | -0.0129 (17) |
| 3-5 | 2394 | 0.1993 | 0.1977 | +0.0016 ± 0.0007 | 0.5791 | 0.5728 | 0.486 | 0.4461 | 0.4453 | -0.057 ± 0.0092 | 0.0 (2) |
| 5-10 | 5130 | 0.2 | 0.1966 | +0.0034 ± 0.0009 | 0.5854 | 0.5732 | 0.4852 | 0.4113 | 0.4248 | -0.049 ± 0.0063 | -0.0119 (21) |
| 10-15 | 4372 | 0.199 | 0.1812 | +0.0178 ± 0.0016 | 0.5843 | 0.5337 | 0.4892 | 0.3649 | 0.3552 | -0.074 ± 0.0064 | -0.0281 (16) |
| 15-25 | 5528 | 0.2083 | 0.1697 | +0.0386 ± 0.0022 | 0.61 | 0.5011 | 0.5033 | 0.307 | 0.3081 | -0.072 ± 0.0055 | -0.0025 (44) |
| 25-40 | 4284 | 0.2223 | 0.1279 | +0.0944 ± 0.0034 | 0.6387 | 0.3918 | 0.531 | 0.2177 | 0.2274 | -0.061 ± 0.0053 | -0.01 (1) |
| 40+ | 2757 | 0.3785 | 0.0475 | +0.3310 ± 0.0047 | 0.9853 | 0.1808 | 0.6318 | 0.1071 | 0.0667 | -0.076 ± 0.0039 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 546 | 0.2081 | 0.2088 | -0.0008 ± 0.0007 | 0.5985 | 0.6004 | 0.5075 | 0.4924 | 0.5183 | -0.105 ± 0.0212 | -0.01 (3) |
| 3-5 | 394 | 0.2256 | 0.2225 | +0.0031 ± 0.0019 | 0.6369 | 0.6304 | 0.5102 | 0.4705 | 0.4467 | -0.138 ± 0.0254 | 0.02 (1) |
| 5-10 | 856 | 0.2073 | 0.2068 | +0.0005 ± 0.0023 | 0.6009 | 0.5993 | 0.5487 | 0.4738 | 0.5117 | -0.087 ± 0.0161 | -0.01 (4) |
| 10-15 | 784 | 0.2173 | 0.2106 | +0.0068 ± 0.0041 | 0.6244 | 0.6069 | 0.5666 | 0.4422 | 0.4796 | -0.107 ± 0.0171 | -0.04 (5) |
| 15-25 | 1112 | 0.2317 | 0.2134 | +0.0183 ± 0.0054 | 0.6577 | 0.6098 | 0.5894 | 0.3939 | 0.4487 | -0.102 ± 0.0142 | -0.0133 (9) |
| 25-40 | 778 | 0.2635 | 0.1978 | +0.0656 ± 0.01 | 0.7376 | 0.5764 | 0.6549 | 0.3405 | 0.3959 | -0.120 ± 0.0157 | -0.0075 (4) |
| 40+ | 291 | 0.3541 | 0.1742 | +0.1799 ± 0.0241 | 0.9723 | 0.5196 | 0.7363 | 0.2533 | 0.323 | -0.071 ± 0.0235 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3048 | 0.1946 | 0.1949 | -0.0003 ± 0.0003 | 0.566 | 0.5664 | 0.5119 | 0.4969 | 0.5112 | -0.045 ± 0.0083 | -0.0133 (15) |
| 3-5 | 2058 | 0.2013 | 0.2002 | +0.0011 ± 0.0008 | 0.5813 | 0.5779 | 0.5123 | 0.4724 | 0.4776 | -0.050 ± 0.0101 | 0.02 (1) |
| 5-10 | 4560 | 0.1979 | 0.195 | +0.0029 ± 0.001 | 0.5818 | 0.5696 | 0.5132 | 0.4392 | 0.4596 | -0.041 ± 0.0066 | -0.0117 (6) |
| 10-15 | 3939 | 0.2025 | 0.1903 | +0.0122 ± 0.0017 | 0.5938 | 0.5541 | 0.5158 | 0.3919 | 0.4052 | -0.056 ± 0.0071 | -0.0189 (18) |
| 15-25 | 5488 | 0.2165 | 0.1792 | +0.0373 ± 0.0023 | 0.629 | 0.5258 | 0.5259 | 0.3303 | 0.3367 | -0.067 ± 0.0058 | -0.0086 (42) |
| 25-40 | 5025 | 0.2506 | 0.1369 | +0.1136 ± 0.0033 | 0.7057 | 0.4202 | 0.558 | 0.2413 | 0.2227 | -0.085 ± 0.0052 | -0.0044 (18) |
| 40+ | 3971 | 0.3936 | 0.0617 | +0.3319 ± 0.0045 | 1.0351 | 0.2199 | 0.6516 | 0.12 | 0.0871 | -0.071 ± 0.0039 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 672 | 0.1998 | 0.2019 | -0.0021 ± 0.0006 | 0.5805 | 0.5856 | 0.5023 | 0.4871 | 0.5491 | -0.036 ± 0.018 | -0.0137 (8) |
| 3-5 | 472 | 0.2036 | 0.2024 | +0.0012 ± 0.0017 | 0.5908 | 0.5862 | 0.5077 | 0.468 | 0.4746 | -0.116 ± 0.0216 | 0.0067 (3) |
| 5-10 | 1008 | 0.2032 | 0.2008 | +0.0024 ± 0.0021 | 0.5927 | 0.5838 | 0.5131 | 0.439 | 0.4583 | -0.100 ± 0.0145 | -0.0071 (7) |
| 10-15 | 823 | 0.2093 | 0.2055 | +0.0038 ± 0.0039 | 0.6076 | 0.5932 | 0.5414 | 0.4178 | 0.4654 | -0.092 ± 0.0158 | -0.0317 (6) |
| 15-25 | 1023 | 0.2324 | 0.215 | +0.0174 ± 0.0057 | 0.6635 | 0.6134 | 0.5893 | 0.3946 | 0.4467 | -0.110 ± 0.0145 | -0.03 (1) |
| 25-40 | 633 | 0.2132 | 0.2166 | -0.0034 ± 0.0108 | 0.6156 | 0.6182 | 0.6679 | 0.3574 | 0.515 | -0.057 ± 0.0166 | 0.015 (2) |
| 40+ | 130 | 0.2842 | 0.2106 | +0.0736 ± 0.0348 | 0.7847 | 0.6082 | 0.7681 | 0.3201 | 0.4692 | -0.070 ± 0.0366 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3529 | 0.186 | 0.1866 | -0.0006 ± 0.0003 | 0.5468 | 0.5478 | 0.4885 | 0.4734 | 0.4928 | -0.034 ± 0.0074 | -0.0163 (35) |
| 3-5 | 2398 | 0.1994 | 0.1973 | +0.0020 ± 0.0007 | 0.5824 | 0.5756 | 0.4883 | 0.4487 | 0.4441 | -0.064 ± 0.0093 | -0.0094 (18) |
| 5-10 | 5227 | 0.1954 | 0.1904 | +0.0050 ± 0.0009 | 0.5747 | 0.5574 | 0.487 | 0.413 | 0.4167 | -0.056 ± 0.0061 | -0.01 (31) |
| 10-15 | 4267 | 0.1919 | 0.1769 | +0.0150 ± 0.0016 | 0.5677 | 0.5225 | 0.4994 | 0.3759 | 0.3766 | -0.064 ± 0.0064 | -0.015 (12) |
| 15-25 | 5679 | 0.2111 | 0.1714 | +0.0397 ± 0.0022 | 0.6165 | 0.5055 | 0.5138 | 0.3187 | 0.3155 | -0.075 ± 0.0055 | -0.03 (2) |
| 25-40 | 4298 | 0.2195 | 0.1318 | +0.0877 ± 0.0035 | 0.6332 | 0.4004 | 0.5351 | 0.2194 | 0.2401 | -0.052 ± 0.0053 | 0.01 (3) |
| 40+ | 2691 | 0.3924 | 0.0526 | +0.3398 ± 0.005 | 1.0248 | 0.1942 | 0.6442 | 0.114 | 0.0728 | -0.078 ± 0.0042 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1059 | 0.1966 | 0.1967 | -0.0000 ± 0.0005 | 0.5728 | 0.5726 | 0.5022 | 0.4871 | 0.4891 | -0.068 ± 0.0139 | -0.0224 (49) |
| 3-5 | 729 | 0.1937 | 0.1929 | +0.0008 ± 0.0013 | 0.565 | 0.5619 | 0.4928 | 0.453 | 0.4609 | -0.063 ± 0.0167 | -0.0194 (34) |
| 5-10 | 1535 | 0.2024 | 0.1966 | +0.0058 ± 0.0017 | 0.5939 | 0.5755 | 0.498 | 0.4245 | 0.4228 | -0.077 ± 0.0115 | -0.005 (78) |
| 10-15 | 1038 | 0.2114 | 0.2 | +0.0114 ± 0.0034 | 0.614 | 0.5824 | 0.5275 | 0.4047 | 0.4181 | -0.072 ± 0.0142 | 0.0014 (64) |
| 15-25 | 1369 | 0.2318 | 0.2109 | +0.0208 ± 0.0049 | 0.6611 | 0.6069 | 0.5802 | 0.3854 | 0.431 | -0.077 ± 0.0125 | -0.0214 (59) |
| 25-40 | 839 | 0.2413 | 0.2097 | +0.0316 ± 0.0096 | 0.6897 | 0.6013 | 0.6792 | 0.3669 | 0.472 | -0.082 ± 0.0146 | -0.0219 (26) |
| 40+ | 276 | 0.3427 | 0.2018 | +0.1409 ± 0.0264 | 0.9895 | 0.5906 | 0.8107 | 0.33 | 0.442 | -0.092 ± 0.0243 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3548 | 0.1824 | 0.1825 | -0.0001 ± 0.0003 | 0.5372 | 0.5367 | 0.5039 | 0.4887 | 0.4952 | -0.044 ± 0.0072 | -0.0157 (88) |
| 3-5 | 2484 | 0.1965 | 0.1945 | +0.0020 ± 0.0007 | 0.5714 | 0.567 | 0.5031 | 0.4634 | 0.4581 | -0.056 ± 0.009 | -0.0209 (69) |
| 5-10 | 4967 | 0.1977 | 0.1895 | +0.0082 ± 0.0009 | 0.5813 | 0.5566 | 0.4936 | 0.42 | 0.4037 | -0.073 ± 0.0062 | -0.0082 (132) |
| 10-15 | 3475 | 0.2071 | 0.1914 | +0.0157 ± 0.0018 | 0.6046 | 0.561 | 0.5304 | 0.4076 | 0.4043 | -0.066 ± 0.0075 | -0.0053 (105) |
| 15-25 | 4268 | 0.2301 | 0.2001 | +0.0300 ± 0.0027 | 0.6632 | 0.5795 | 0.5693 | 0.3736 | 0.396 | -0.066 ± 0.0069 | -0.0253 (107) |
| 25-40 | 2927 | 0.2569 | 0.1864 | +0.0705 ± 0.005 | 0.7288 | 0.5434 | 0.6342 | 0.3208 | 0.3676 | -0.074 ± 0.0078 | -0.0229 (51) |
| 40+ | 1265 | 0.373 | 0.1472 | +0.2258 ± 0.0113 | 1.0549 | 0.4435 | 0.7315 | 0.2286 | 0.2688 | -0.069 ± 0.0101 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4761 | 1.034 ± 0.041 | 1.109 | 0.1681 | 0.1625 | 0.2146 | 0.2072 |
| gen2 | 4761 | 0.827 ± 0.038 | 1.071 | 0.1686 | 0.1631 | 0.2344 | 0.207 |
| gen1_elo | 4761 | 1.008 ± 0.039 | 1.107 | 0.1747 | 0.1626 | 0.2136 | 0.2073 |
| gen1_sr | 4761 | 1.01 ± 0.049 | 1.133 | 0.1293 | 0.165 | 0.2307 | 0.2066 |
| gen1_ledger | 6845 | 0.866 ± 0.029 | 1.064 | 0.1841 | 0.1763 | 0.2183 | 0.2014 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 23,855)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,276 | 22.1% |
| STALE_QUOTE | market_freshness | 5,265 | 22.1% |
| BOOK_QUALITY | execution | 4,632 | 19.4% |
| POOR_DATA | data | 2,684 | 11.2% |
| LIMITED_DATA | data | 1,469 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,285 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,117 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 1,013 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 692 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 421 | 1.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.1%, market_freshness 22.1%, execution 19.4%, data 17.4%, market_freshness/coverage 8.3%, model_calibration_or_unknown 4.7%, mapping 4.2%, model_calibration 1.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.0%, LOW_DATA_QUALITY 71.1%, THIN_PLAYER_HISTORY 60.1%, STALE_PLAYER_DATA 50.9%, STALE_KALSHI_QUOTE 43.8%, MODEL_INTERNAL_DISAGREEMENT 42.6%, ASYMMETRIC_SAMPLE_SIZE 33.6%, WIDE_SPREAD 25.6%, MODEL_HIGH_UNCERTAINTY 17.7%, PLAYER_IDENTITY_RISK 16.5%, LEVEL_TRANSFER_RISK 10.6%, LOW_DISPLAYED_LIQUIDITY 8.0%, EVENT_MAPPING_RISK 7.9%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.6%, POST_SETTLEMENT_OBSERVATION 22.1%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 12,718)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,234 | 33.3% |
| STALE_QUOTE | market_freshness | 2,429 | 19.1% |
| BOOK_QUALITY | execution | 2,428 | 19.1% |
| POOR_DATA | data | 1,109 | 8.7% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 690 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 561 | 4.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 442 | 3.5% |
| LIMITED_DATA | data | 437 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 286 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 101 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.3%, market_freshness 19.1%, execution 19.1%, data 12.2%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.7%, LOW_DATA_QUALITY 74.5%, THIN_PLAYER_HISTORY 62.3%, STALE_KALSHI_QUOTE 51.6%, STALE_PLAYER_DATA 45.5%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 34.8%, WIDE_SPREAD 25.1%, PLAYER_IDENTITY_RISK 19.8%, MODEL_HIGH_UNCERTAINTY 18.1%, EVENT_MAPPING_RISK 9.6%, LEVEL_TRANSFER_RISK 9.4%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 5.1%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.4%, POST_SETTLEMENT_OBSERVATION 33.3%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 9889, "IDENTITY_AMBIGUOUS": 2829}; ticker orientation: {"VERIFIED": 12718}.

Checks: discipline:AMBIGUOUS 866, discipline:PASS 11852, identity_confidence:AMBIGUOUS 2521, identity_confidence:PASS 10197, level_mapping:NA 878, level_mapping:PASS 11840, market_pair:AMBIGUOUS 466, market_pair:NA 305, market_pair:PASS 11947, model_complement:NA 272, model_complement:PASS 12446, namesake:AMBIGUOUS 6, namesake:PASS 12712, physical_match_id:NA 4504, physical_match_id:PASS 8214, player_ids:PASS 12718, same_pair_other_event:PASS 12718, ticker_orientation:PASS 12718

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,959 | 4.4% | 4.0% | 1.7% | {"market_freshness": 56, "model_calibration_or_unknown": 51, "data": 36, "execution": 24, "model_calibration": 24, "market_freshness/coverage": 15, "coverage": 13} | 5.86 | 0.2217 / 0.2194 (561) | 20.7% | 3.2% | 3.3% | 2.7% |
| CHALLENGER | 9,012 | 16.5% | 6.7% | 11.7% | {"coverage": 837, "market_freshness/coverage": 183, "market_freshness": 166, "data": 144, "model_calibration_or_unknown": 72, "execution": 36, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.56 | 0.2192 / 0.21 (2101) | 34.4% | 16.8% | 4.2% | 21.9% |
| DOUBLES | 1,828 | 47.4% | 47.1% | 6.8% | {"execution": 481, "mapping": 217, "market_freshness": 106, "market_freshness/coverage": 55, "coverage": 7} | 23.85 | 0.3091 / 0.2364 (442) | 12.8% | 0.0% | 100.0% | 6.6% |
| ITF_MEN | 15,605 | 25.7% | 18.2% | 31.6% | {"coverage": 1444, "execution": 776, "market_freshness": 713, "data": 545, "market_freshness/coverage": 348, "mapping": 182, "model_calibration_or_unknown": 2, "model_calibration": 2} | 12.08 | 0.2164 / 0.1988 (3391) | 37.4% | 70.5% | 19.3% | 21.8% |
| ITF_WOMEN | 21,138 | 27.0% | 20.0% | 44.9% | {"coverage": 1908, "market_freshness": 1264, "execution": 1058, "data": 775, "market_freshness/coverage": 478, "mapping": 139, "model_calibration_or_unknown": 72, "model_calibration": 11} | 12.89 | 0.2034 / 0.1965 (3982) | 39.5% | 57.7% | 10.4% | 21.3% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,522 | 5.6% | 5.1% | 1.6% | {"market_freshness": 72, "model_calibration_or_unknown": 40, "execution": 27, "data": 18, "model_calibration": 16, "coverage": 12, "market_freshness/coverage": 11, "mapping": 1} | 7.69 | 0.2331 / 0.2269 (545) | 25.5% | 1.2% | 1.5% | 3.3% |
| WTA125 | 1,759 | 12.3% | 10.1% | 1.7% | {"market_freshness": 50, "model_calibration_or_unknown": 47, "market_freshness/coverage": 41, "data": 28, "execution": 21, "model_calibration": 13, "coverage": 12, "mapping": 4} | 9.52 | 0.2165 / 0.2028 (542) | 24.8% | 11.4% | 6.1% | 8.2% |

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
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 15 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 16 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 17 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 18 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 19 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 20 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 21 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 22 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 23 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 24 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 25 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 26 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 27 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 28 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 29 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 30 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 31 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 32 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 33 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 34 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 35 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 36 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 37 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 39 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 41 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 42 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 43 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 44 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 46 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 752 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 47 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 48 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 49 | `KXWTADOUBLES-26OCT25DABSTEBUCFER-BUCFER` | DOUBLES | gen1_ledger | 93% / 16% | +77 | BOOK_QUALITY | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9673, "by_level_share_of_ge_25pp": {"ATP": 0.0172, "CHALLENGER": 0.1172, "DOUBLES": 0.0681, "ITF_MEN": 0.3155, "ITF_WOMEN": 0.4486, "OTHER": 0.0009, "WTA": 0.0155, "WTA125": 0.017}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5158, "share_primary_cause_market_settled_or_in_play": 0.422, "share_primary_cause_stale_quote_only": 0.191}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 12718, "identity_ambiguous_share": 0.2224, "ticker_orientation": {"VERIFIED": 12718}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 8214, "with_external": 411, "coverage": 0.05, "external_status": {"EXTERNAL_STALE": 251, "AGREES_WITH_KALSHI": 151, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 251, "MODEL_LONE_OUTLIER": 151, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3674, "share_external_supports_model": 0.0219}, "pregame_clean_ge_25pp": {"n": 4068, "with_external": 388, "coverage": 0.0954, "external_status": {"EXTERNAL_STALE": 235, "AGREES_WITH_KALSHI": 144, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 235, "MODEL_LONE_OUTLIER": 144, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3711, "share_external_supports_model": 0.0232}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 467.0, "median_sample_ratio": 2.47, "median_min_matches": 19.0, "median_max_days_since_last": 233.0, "share_severe_asymmetry": 0.2173, "data_status": {"POOR": 7154, "LIMITED": 3269, "ADEQUATE": 2295}, "comparison_lt_10pp": {"median_thinner_serve_points": 1787.0, "median_sample_ratio": 1.67, "median_min_matches": 96.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 950, "model_minus_observed": 0.0472, "kalshi_minus_observed": -0.0906, "brier_diff_model_minus_kalshi": -0.0038}, "4-10x": {"n": 638, "model_minus_observed": 0.086, "kalshi_minus_observed": -0.0603, "brier_diff_model_minus_kalshi": 0.0091}, "<2x": {"n": 2323, "model_minus_observed": 0.0901, "kalshi_minus_observed": -0.0328, "brier_diff_model_minus_kalshi": 0.011}, ">=10x": {"n": 850, "model_minus_observed": 0.1112, "kalshi_minus_observed": -0.0642, "brier_diff_model_minus_kalshi": 0.0087}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4761, "model": {"intercept": -0.535, "slope": 0.827, "slope_se": 0.038}, "kalshi_mid_same_rows": {"intercept": 0.199, "slope": 1.071, "slope_se": 0.042}, "mean_extremity_model": 0.1686, "mean_extremity_kalshi": 0.1631, "model_brier": 0.2344, "kalshi_brier": 0.207, "brier_diff_model_minus_kalshi": 0.0274, "brier_diff_se": 0.0027, "model_logloss": 0.6658, "kalshi_logloss": 0.5971}, "fair_v1": {"n": 4761, "model": {"intercept": -0.413, "slope": 1.034, "slope_se": 0.041}, "kalshi_mid_same_rows": {"intercept": 0.287, "slope": 1.109, "slope_se": 0.042}, "mean_extremity_model": 0.1681, "mean_extremity_kalshi": 0.1625, "model_brier": 0.2146, "kalshi_brier": 0.2072, "brier_diff_model_minus_kalshi": 0.0074, "brier_diff_se": 0.0023, "model_logloss": 0.6184, "kalshi_logloss": 0.5973}, "gen1_elo": {"n": 4761, "model": {"intercept": -0.389, "slope": 1.008, "slope_se": 0.039}, "kalshi_mid_same_rows": {"intercept": 0.308, "slope": 1.107, "slope_se": 0.042}, "mean_extremity_model": 0.1747, "mean_extremity_kalshi": 0.1626, "model_brier": 0.2136, "kalshi_brier": 0.2073, "brier_diff_model_minus_kalshi": 0.0063, "brier_diff_se": 0.0023, "model_logloss": 0.6169, "kalshi_logloss": 0.5975}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.245, "share_ge_15": 0.4424, "median_abs_gap": 13.05, "n": 33531}, "gen1_elo": {"share_ge_25": 0.2424, "share_ge_15": 0.4412, "median_abs_gap": 12.92, "n": 33531}, "gen1_sr": {"share_ge_25": 0.3128, "share_ge_15": 0.5201, "median_abs_gap": 15.87, "n": 33531}, "gen2": {"share_ge_25": 0.3168, "share_ge_15": 0.5117, "median_abs_gap": 15.5, "n": 33531}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.155, "share_ge_15": 0.36, "median_abs_gap": 10.88, "n": 26245}, "gen1_elo": {"share_ge_25": 0.1552, "share_ge_15": 0.3577, "median_abs_gap": 10.71, "n": 26242}, "gen1_sr": {"share_ge_25": 0.2218, "share_ge_15": 0.4437, "median_abs_gap": 13.01, "n": 26246}, "gen2": {"share_ge_25": 0.2384, "share_ge_15": 0.4448, "median_abs_gap": 13.04, "n": 26247}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.86, "share_ge_25_all": 0.0442, "share_ge_25_pregame_clean": 0.0396}, "WTA": {"median_abs_gap_pregame_clean": 7.69, "share_ge_25_all": 0.0559, "share_ge_25_pregame_clean": 0.0511}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2357, "share_within_10pp_all": 0.4346, "share_within_10pp_pregame_clean": 0.4853, "corr_model_vs_mid_pregame_clean": 0.8434}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 699, "model_brier": 0.2021, "kalshi_brier": 0.2028, "brier_diff_model_minus_kalshi": -0.0007}, "10-15": {"n_settled": 830, "model_brier": 0.2185, "kalshi_brier": 0.2098, "brier_diff_model_minus_kalshi": 0.0088}, "15-25": {"n_settled": 1079, "model_brier": 0.2261, "kalshi_brier": 0.2137, "brier_diff_model_minus_kalshi": 0.0123}, "25-40": {"n_settled": 613, "model_brier": 0.2205, "kalshi_brier": 0.209, "brier_diff_model_minus_kalshi": 0.0115}, "3-5": {"n_settled": 434, "model_brier": 0.2043, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0004}, "40+": {"n_settled": 121, "model_brier": 0.2699, "kalshi_brier": 0.2006, "brier_diff_model_minus_kalshi": 0.0693}, "5-10": {"n_settled": 985, "model_brier": 0.2019, "kalshi_brier": 0.2023, "brier_diff_model_minus_kalshi": -0.0004}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.535, "slope": 0.827, "slope_se": 0.038}, "kalshi_slope": {"intercept": 0.199, "slope": 1.071, "slope_se": 0.042}, "n": 4761}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.496, "slope": 0.866, "slope_se": 0.029}, "kalshi_slope": {"intercept": 0.16, "slope": 1.064, "slope_se": 0.033}, "n": 6845}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 442, "model_brier": 0.3091, "kalshi_brier": 0.2364, "brier_diff_model_minus_kalshi": 0.0727, "brier_diff_se": 0.0143, "corr_model_outcome": 0.0392, "corr_kalshi_outcome": 0.2496}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
