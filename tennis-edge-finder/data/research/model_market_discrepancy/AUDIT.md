# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-09T19:32Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 83,778): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.2%, 15-25 19.1%, 25-40 13.6%, 40+ 8.2%; median gap 11.83 pp.
* **Where the extremes live**: 97.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.7%, Challenger 11.1%, doubles 6.6%). Main tour: ATP 3.8% and WTA 6.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 18,245): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.4%, STALE_QUOTE 19.7%, BOOK_QUALITY 17.2%, POOR_DATA 9.1%, POSSIBLY_IN_PLAY_QUOTE 5.8%, IDENTITY_AMBIGUOUS 4.3%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.4%, market_freshness 19.7%, execution 17.2%, data 12.5%, market_freshness/coverage 9.2%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 54.1% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.7% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 18,245 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.1% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.9% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 490.0 points vs 1736.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.025, Gen-2 0.815, Gen-1 ledger 0.867 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 929 model 0.2236 vs Kalshi 0.2059; n 191 model 0.296 vs Kalshi 0.1751.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 354,672 model-market comparisons (581,926 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 117,650 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-09T19:11:00.658901+00:00'], shadow board 96,579 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-09T19:11:04.784523+00:00'], Model 4 43,327 rows, 29,369 settled tickers, 11,065 tickers with an external scan.
* By model: {"gen1_ledger": 79276, "gen1_elo": 48540, "fair_v1": 48540, "gen2": 48540, "gen1_sr": 48540, "model4_fundamental": 40660, "model4_conditioned": 40576}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 83,778 | 14.1 | 9.6 | 20.2 | 15.2 | 19.1 | 13.6 | 8.2 | 11.83 | 40.9% | 21.8% |
| MW fair_v1 | 48,540 | 12.8 | 8.6 | 18.8 | 15.3 | 19.6 | 14.8 | 10.1 | 13.05 | 44.5% | 24.9% |
| MW gen1_elo | 48,540 | 12.6 | 8.8 | 19.2 | 15.4 | 19.4 | 14.7 | 9.9 | 12.84 | 44.0% | 24.6% |
| MW gen1_ledger | 35,238 | 15.8 | 10.9 | 22.2 | 15.1 | 18.5 | 12.0 | 5.5 | 10.26 | 36.0% | 17.5% |
| MW gen1_sr | 48,540 | 10.0 | 7.3 | 16.7 | 13.9 | 20.7 | 18.7 | 12.7 | 15.82 | 52.0% | 31.3% |
| MW gen2 | 48,540 | 11.0 | 7.5 | 16.7 | 13.7 | 19.6 | 17.7 | 13.7 | 15.46 | 51.0% | 31.4% |
| all families model4_conditioned | 40,576 | 22.3 | 17.9 | 34.4 | 17.0 | 5.0 | 2.2 | 1.2 | 6.07 | 8.4% | 3.4% |
| all families model4_fundamental | 40,660 | 17.3 | 13.5 | 33.9 | 20.0 | 9.9 | 3.8 | 1.5 | 7.62 | 15.3% | 5.3% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.1%, >=15pp 40.9%, >=20pp 30.1%, >=25pp 21.8%, >=30pp 15.7%, >=40pp 8.2%, >=50pp 3.9%
Executable gap (model outside the book, before fees): median 8.4pp; >=10pp 45.1%, >=25pp 17.2%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,042 | 28.2 | 15.7 | 27.8 | 13.4 | 10.6 | 3.6 | 0.6 | 5.84 | 14.9% | 4.2% |
| CHALLENGER | 7,582 | 16.1 | 9.6 | 20.6 | 15.4 | 16.1 | 11.3 | 10.8 | 10.93 | 38.2% | 22.1% |
| ITF_MEN | 13,685 | 9.8 | 7.3 | 17.1 | 14.9 | 21.1 | 17.3 | 12.5 | 15.38 | 50.9% | 29.8% |
| ITF_WOMEN | 18,826 | 9.5 | 7.0 | 16.0 | 14.8 | 22.2 | 18.4 | 12.0 | 15.89 | 52.6% | 30.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,072 | 16.7 | 13.1 | 25.1 | 20.8 | 16.5 | 6.8 | 1.1 | 8.65 | 24.4% | 7.8% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,042 | 26.7 | 15.6 | 26.1 | 15.7 | 11.3 | 3.9 | 0.8 | 6.08 | 16.0% | 4.7% |
| CHALLENGER | 7,582 | 14.4 | 9.2 | 19.1 | 13.8 | 18.7 | 13.5 | 11.4 | 12.51 | 43.6% | 24.9% |
| ITF_MEN | 13,685 | 8.2 | 6.1 | 15.0 | 13.7 | 20.0 | 20.5 | 16.5 | 18.0 | 57.0% | 37.0% |
| ITF_WOMEN | 18,826 | 7.9 | 5.8 | 14.2 | 12.8 | 20.7 | 21.2 | 17.5 | 19.09 | 59.4% | 38.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,072 | 14.0 | 10.3 | 21.7 | 16.3 | 22.4 | 12.8 | 2.5 | 11.23 | 37.7% | 15.3% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,042 | 23.1 | 14.1 | 25.5 | 15.6 | 14.6 | 6.0 | 1.1 | 7.11 | 21.8% | 7.2% |
| CHALLENGER | 7,582 | 15.1 | 9.7 | 20.5 | 15.9 | 16.0 | 11.9 | 10.8 | 11.3 | 38.8% | 22.8% |
| ITF_MEN | 13,685 | 9.4 | 7.3 | 17.2 | 14.1 | 21.7 | 17.3 | 12.9 | 15.74 | 51.9% | 30.2% |
| ITF_WOMEN | 18,826 | 9.3 | 6.9 | 16.3 | 15.7 | 22.2 | 18.3 | 11.3 | 15.58 | 51.8% | 29.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,072 | 22.6 | 17.0 | 31.9 | 15.4 | 8.8 | 3.3 | 1.0 | 6.12 | 13.1% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,427 | 27.8 | 19.5 | 29.3 | 12.4 | 8.0 | 2.5 | 0.5 | 5.29 | 11.0% | 3.0% |
| CHALLENGER | 4,743 | 22.7 | 14.5 | 27.5 | 14.7 | 13.4 | 5.7 | 1.6 | 7.04 | 20.6% | 7.2% |
| DOUBLES | 2,610 | 4.8 | 4.5 | 12.9 | 10.9 | 20.5 | 24.3 | 22.0 | 23.23 | 66.8% | 46.3% |
| ITF_MEN | 10,084 | 12.8 | 9.6 | 21.3 | 15.6 | 21.7 | 13.0 | 5.9 | 11.81 | 40.6% | 18.9% |
| ITF_WOMEN | 12,166 | 13.4 | 9.2 | 19.9 | 15.7 | 21.4 | 14.8 | 5.5 | 12.23 | 41.7% | 20.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,803 | 23.6 | 16.1 | 31.6 | 17.0 | 8.9 | 2.5 | 0.2 | 6.57 | 11.7% | 2.8% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,917 | 28.7 | 15.9 | 28.3 | 13.3 | 10.4 | 3.1 | 0.3 | 5.67 | 13.8% | 3.5% |
| CHALLENGER | 5,387 | 20.8 | 11.9 | 25.6 | 18.1 | 16.1 | 5.9 | 1.6 | 8.28 | 23.6% | 7.5% |
| ITF_MEN | 9,976 | 12.0 | 8.6 | 20.6 | 17.2 | 22.0 | 14.2 | 5.4 | 12.45 | 41.6% | 19.6% |
| ITF_WOMEN | 13,814 | 11.4 | 8.5 | 18.9 | 17.1 | 24.1 | 15.1 | 4.8 | 13.15 | 44.0% | 19.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,958 | 17.0 | 13.2 | 25.4 | 21.1 | 16.5 | 6.2 | 0.6 | 8.45 | 23.4% | 6.8% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,917 | 27.0 | 15.9 | 26.4 | 15.7 | 11.2 | 3.4 | 0.4 | 5.99 | 15.0% | 3.8% |
| CHALLENGER | 5,387 | 18.1 | 11.6 | 23.9 | 16.2 | 19.1 | 9.4 | 1.8 | 8.99 | 30.3% | 11.2% |
| ITF_MEN | 9,977 | 9.6 | 7.2 | 17.6 | 15.9 | 21.9 | 18.6 | 9.2 | 14.91 | 49.7% | 27.8% |
| ITF_WOMEN | 13,815 | 8.9 | 6.8 | 16.0 | 14.4 | 22.6 | 20.6 | 10.7 | 16.52 | 53.8% | 31.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,958 | 14.3 | 10.4 | 21.9 | 16.5 | 22.6 | 12.5 | 1.9 | 11.03 | 37.0% | 14.4% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,361 | 28.0 | 19.6 | 29.3 | 12.5 | 7.8 | 2.4 | 0.3 | 5.24 | 10.5% | 2.7% |
| CHALLENGER | 4,195 | 24.0 | 15.4 | 28.6 | 14.9 | 12.7 | 4.0 | 0.4 | 6.58 | 17.1% | 4.4% |
| DOUBLES | 2,445 | 4.7 | 4.5 | 13.1 | 11.0 | 20.3 | 24.2 | 22.0 | 23.2 | 66.6% | 46.3% |
| ITF_MEN | 8,678 | 13.6 | 10.2 | 22.9 | 16.1 | 21.7 | 11.5 | 4.0 | 10.89 | 37.2% | 15.5% |
| ITF_WOMEN | 10,444 | 14.1 | 9.7 | 21.0 | 16.2 | 21.5 | 13.8 | 3.6 | 11.42 | 39.0% | 17.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,740 | 24.0 | 16.5 | 31.6 | 16.9 | 8.9 | 2.0 | 0.1 | 6.43 | 11.0% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,610 | 4.8 | 4.5 | 12.9 | 10.9 | 20.5 | 24.3 | 22.0 | 23.23 | 66.8% | 46.3% |
| singles | 32,628 | 16.7 | 11.4 | 22.9 | 15.4 | 18.3 | 11.0 | 4.2 | 9.72 | 33.5% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 10,009 | 12.7 | 9.1 | 19.9 | 15.5 | 19.6 | 13.9 | 9.4 | 12.62 | 42.9% | 23.3% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 31,726 | 13.3 | 8.7 | 18.8 | 15.2 | 19.2 | 14.8 | 10.0 | 12.89 | 44.0% | 24.8% |
| UNKNOWN | 6,392 | 10.5 | 7.5 | 17.0 | 16.3 | 21.4 | 16.0 | 11.1 | 14.41 | 48.6% | 27.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 13,858 | 19.3 | 11.8 | 22.5 | 15.9 | 15.0 | 9.1 | 6.3 | 8.93 | 30.4% | 15.4% |
| B | 5,938 | 12.8 | 8.5 | 19.6 | 15.5 | 19.7 | 12.8 | 11.2 | 12.79 | 43.6% | 23.9% |
| C | 6,880 | 11.9 | 8.8 | 19.6 | 15.6 | 18.7 | 14.6 | 10.8 | 12.93 | 44.1% | 25.4% |
| D | 7,788 | 11.8 | 8.4 | 17.8 | 15.2 | 21.7 | 15.8 | 9.4 | 13.87 | 46.9% | 25.2% |
| F | 14,076 | 7.4 | 5.5 | 14.9 | 14.6 | 23.3 | 20.9 | 13.3 | 17.84 | 57.5% | 34.2% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,507 | 24.8 | 16.0 | 28.9 | 15.0 | 10.6 | 3.4 | 1.3 | 6.34 | 15.2% | 4.7% |
| B | 4,902 | 16.6 | 10.8 | 24.4 | 16.8 | 18.9 | 9.6 | 3.0 | 9.59 | 31.4% | 12.6% |
| C | 6,910 | 10.9 | 7.7 | 19.6 | 14.7 | 21.1 | 15.6 | 10.4 | 13.66 | 47.1% | 26.0% |
| D | 5,244 | 14.5 | 10.1 | 21.3 | 15.3 | 20.9 | 12.6 | 5.3 | 11.25 | 38.8% | 17.9% |
| F | 8,675 | 10.2 | 8.4 | 16.1 | 14.5 | 23.3 | 19.4 | 7.9 | 15.35 | 50.7% | 27.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 15,680 | 17.7 | 10.8 | 21.5 | 15.7 | 15.3 | 10.0 | 9.0 | 9.99 | 34.2% | 19.0% |
| LIMITED | 10,606 | 13.6 | 9.6 | 20.5 | 15.8 | 19.5 | 13.3 | 7.7 | 11.89 | 40.5% | 21.1% |
| POOR | 22,254 | 9.0 | 6.6 | 16.0 | 14.8 | 22.7 | 19.0 | 11.9 | 16.2 | 53.5% | 30.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,067 | 23.7 | 18.0 | 33.0 | 15.6 | 6.4 | 2.9 | 0.4 | 5.9 | 9.8% | 3.3% |
| GAME_SPREAD | 6,793 | 22.9 | 15.3 | 32.1 | 16.7 | 9.0 | 3.3 | 0.7 | 6.68 | 12.9% | 4.0% |
| MATCH_WINNER | 35,238 | 15.8 | 10.9 | 22.2 | 15.1 | 18.5 | 12.0 | 5.5 | 10.26 | 36.0% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 16,754 | 28.2 | 16.8 | 30.8 | 12.6 | 8.9 | 2.4 | 0.3 | 5.59 | 11.6% | 2.7% |
| TOTAL_GAMES | 11,400 | 9.8 | 10.8 | 36.0 | 25.9 | 10.5 | 4.2 | 2.9 | 9.17 | 17.6% | 7.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,424 | 24.5 | 28.6 | 33.3 | 8.1 | 4.0 | 1.1 | 0.3 | 4.8 | 5.4% | 1.4% |
| GAME_SPREAD | 9,366 | 46.9 | 15.9 | 24.9 | 7.4 | 2.3 | 1.9 | 0.6 | 3.3 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,786 | 6.6 | 9.9 | 40.5 | 30.0 | 7.4 | 3.3 | 2.4 | 9.18 | 13.0% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,460 | 23.7 | 16.7 | 34.6 | 14.8 | 6.9 | 2.7 | 0.5 | 6.06 | 10.1% | 3.2% |
| GAME_SPREAD | 9,375 | 20.5 | 13.5 | 28.3 | 20.2 | 12.0 | 4.3 | 1.1 | 7.64 | 17.5% | 5.5% |
| TOTAL_GAMES | 16,825 | 10.0 | 10.8 | 36.4 | 24.4 | 11.4 | 4.4 | 2.6 | 9.04 | 18.4% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 48,540 | 44.5% | 24.9% | 13.05 | 35.3% | 15.1% | 10.66 |
| gen1_elo | 48,540 | 44.0% | 24.6% | 12.84 | 34.8% | 14.9% | 10.48 |
| gen1_sr | 48,540 | 52.0% | 31.3% | 15.82 | 43.8% | 21.5% | 12.95 |
| gen2 | 48,540 | 51.0% | 31.4% | 15.46 | 43.8% | 23.1% | 12.83 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,098 | 15.5 | 10.4 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 28,442 | 10.9 | 7.3 | 16.9 | 13.9 | 19.2 | 16.9 | 14.7 | 15.36 | 50.9% | 31.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 28,706 | 16.4 | 11.2 | 22.7 | 15.2 | 18.0 | 11.5 | 4.9 | 9.89 | 34.4% | 16.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 83,778 | 28706 | 23570 | 31502 | 24.9 | 130.4 | 1451.1 |
| ge_15pp | 34,257 | 9877 | 8394 | 15986 | 28.5 | 439.7 | 1451.1 |
| ge_25pp | 18,245 | 4707 | 3666 | 9872 | 34.2 | 584.7 | 1431.1 |
| lt_10pp | 36,753 | 14467 | 11149 | 11137 | 22.7 | 48.2 | 1421.1 |

Current slate `SL-20261109T193224Z-219b0fa4`: 491 priced rows, quote age at build {'median': 66.7, 'max': 106.7}, freshness {'STALE': 491}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 51 | 0.0 | 0.0 | 35.3 | 9.8 | 31.4 | 19.6 | 3.9 | 18.34 | 54.9% | 23.5% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,796 | 19.3 | 10.9 | 25.6 | 18.1 | 17.9 | 7.3 | 0.9 | 8.77 | 26.2% | 8.3% |
| KALSHI_LONE_OUTLIER | 31 | 6.5 | 6.5 | 74.2 | 6.5 | 3.2 | 3.2 | 0.0 | 6.21 | 6.5% | 3.2% |
| MARKETS_AGREE | 1,013 | 66.8 | 33.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.16 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,179 | 0.0 | 2.2 | 37.7 | 26.2 | 23.9 | 9.0 | 0.9 | 11.77 | 33.8% | 10.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 48,540 | 8099 (16.7%) | 26.9% | 1.0% | {"EXTERNAL_STALE": 4796, "AGREES_WITH_KALSHI": 2179, "ALL_AGREE": 1013, "SUPPORTS_MODEL_DIRECTION": 49, "AGREES_WITH_MODEL": 31, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 21,581 | 2021 (9.4%) | 36.5% | 1.5% | {"EXTERNAL_STALE": 1254, "AGREES_WITH_KALSHI": 737, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 12,076 | 627 (5.2%) | 34.6% | 2.1% | {"EXTERNAL_STALE": 397, "AGREES_WITH_KALSHI": 217, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,625 | 596 (10.6%) | 35.2% | 2.2% | {"EXTERNAL_STALE": 373, "AGREES_WITH_KALSHI": 210, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 19,517 | 4633 (23.7%) | 18.8% | 0.9% | {"EXTERNAL_STALE": 2676, "ALL_AGREE": 1013, "AGREES_WITH_KALSHI": 870, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 27, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 9,490 | 10.6 | 7.6 | 19.3 | 14.5 | 21.5 | 16.3 | 10.1 | 14.12 | 48.0% | 26.4% |
| 4-10x | 6,458 | 11.2 | 8.5 | 18.3 | 15.1 | 21.9 | 14.7 | 10.4 | 13.92 | 46.9% | 25.0% |
| <2x | 24,884 | 14.8 | 9.7 | 19.9 | 16.0 | 17.6 | 13.0 | 9.0 | 11.55 | 39.6% | 22.0% |
| >=10x | 7,708 | 10.5 | 6.4 | 15.1 | 14.3 | 21.7 | 18.9 | 13.2 | 16.44 | 53.8% | 32.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 12,784 | 12.4 | 8.5 | 19.8 | 16.2 | 19.1 | 13.5 | 10.4 | 12.73 | 43.0% | 23.9% |
| 300-1000 | 10,423 | 11.8 | 8.8 | 17.7 | 15.0 | 20.8 | 16.3 | 9.7 | 13.79 | 46.8% | 26.0% |
| <300 | 15,193 | 8.3 | 5.8 | 15.2 | 14.7 | 22.9 | 20.0 | 13.2 | 17.19 | 56.1% | 33.2% |
| >=3000 | 10,140 | 21.1 | 12.8 | 24.0 | 15.6 | 14.0 | 7.3 | 5.2 | 7.83 | 26.5% | 12.5% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1477 | 0.5494 | 0.4103 | 0.4848 | +0.065 | -0.074 | 0.0021 ± 0.004 |
| ratio 4-10x | 1000 | 0.5774 | 0.4329 | 0.487 | +0.090 | -0.054 | 0.0087 ± 0.005 |
| ratio <2x | 3628 | 0.5366 | 0.414 | 0.4377 | +0.099 | -0.024 | 0.0142 ± 0.0024 |
| ratio >=10x | 1233 | 0.5669 | 0.3934 | 0.4477 | +0.119 | -0.054 | 0.0148 ± 0.0051 |
| thinner_sample 1000-3000 | 2037 | 0.5402 | 0.4127 | 0.4482 | +0.092 | -0.035 | 0.0113 ± 0.0032 |
| thinner_sample 300-1000 | 1654 | 0.5649 | 0.4246 | 0.4746 | +0.090 | -0.050 | 0.0049 ± 0.0038 |
| thinner_sample <300 | 2364 | 0.5588 | 0.3909 | 0.4543 | +0.104 | -0.063 | 0.0132 ± 0.0036 |
| thinner_sample >=3000 | 1283 | 0.529 | 0.4354 | 0.4451 | +0.084 | -0.010 | 0.015 ± 0.0032 |
| data_status ADEQUATE | 2045 | 0.5317 | 0.4289 | 0.4391 | +0.093 | -0.010 | 0.0153 ± 0.0027 |
| data_status LIMITED | 1800 | 0.5489 | 0.4157 | 0.4667 | +0.082 | -0.051 | 0.0074 ± 0.0036 |
| data_status POOR | 3493 | 0.5609 | 0.4009 | 0.4595 | +0.101 | -0.059 | 0.0106 ± 0.0029 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1060 | 0.1983 | 0.1986 | -0.0003 ± 0.0005 | 0.5768 | 0.5775 | 0.5032 | 0.4881 | 0.5009 | -0.093 ± 0.0145 | -0.0087 (8) |
| 3-5 | 676 | 0.2062 | 0.2059 | +0.0003 ± 0.0014 | 0.5972 | 0.5949 | 0.5047 | 0.4649 | 0.4808 | -0.098 ± 0.018 | 0.01 (3) |
| 5-10 | 1578 | 0.2034 | 0.202 | +0.0014 ± 0.0017 | 0.5934 | 0.5877 | 0.5121 | 0.4383 | 0.4632 | -0.094 ± 0.0117 | -0.0143 (7) |
| 10-15 | 1274 | 0.2182 | 0.2095 | +0.0087 ± 0.0032 | 0.6281 | 0.6027 | 0.5241 | 0.4006 | 0.4262 | -0.104 ± 0.013 | -0.055 (6) |
| 15-25 | 1630 | 0.2261 | 0.2085 | +0.0177 ± 0.0044 | 0.6474 | 0.6006 | 0.576 | 0.3813 | 0.4331 | -0.104 ± 0.0114 | -0.0045 (11) |
| 25-40 | 929 | 0.2236 | 0.2059 | +0.0176 ± 0.0089 | 0.637 | 0.593 | 0.6521 | 0.3423 | 0.4682 | -0.068 ± 0.0137 | -0.06 (2) |
| 40+ | 191 | 0.296 | 0.1751 | +0.1210 ± 0.0272 | 0.7965 | 0.5226 | 0.7305 | 0.2751 | 0.377 | -0.082 ± 0.0262 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5511 | 0.186 | 0.1869 | -0.0009 ± 0.0002 | 0.5483 | 0.5494 | 0.491 | 0.4758 | 0.5088 | -0.019 ± 0.0059 | -0.01 (28) |
| 3-5 | 3665 | 0.1981 | 0.1963 | +0.0018 ± 0.0006 | 0.5769 | 0.5704 | 0.4828 | 0.443 | 0.4401 | -0.057 ± 0.0074 | 0.005 (6) |
| 5-10 | 7982 | 0.2016 | 0.1978 | +0.0038 ± 0.0007 | 0.589 | 0.5764 | 0.4842 | 0.4105 | 0.4216 | -0.047 ± 0.005 | -0.0114 (22) |
| 10-15 | 6584 | 0.2022 | 0.1862 | +0.0159 ± 0.0013 | 0.591 | 0.5464 | 0.4854 | 0.3615 | 0.3597 | -0.064 ± 0.0053 | -0.0379 (19) |
| 15-25 | 8373 | 0.2065 | 0.1671 | +0.0394 ± 0.0017 | 0.605 | 0.4965 | 0.4998 | 0.3043 | 0.3019 | -0.070 ± 0.0045 | -0.0043 (51) |
| 25-40 | 6468 | 0.2232 | 0.1257 | +0.0975 ± 0.0028 | 0.6406 | 0.3864 | 0.527 | 0.2131 | 0.2188 | -0.059 ± 0.0043 | -0.0733 (3) |
| 40+ | 4377 | 0.3819 | 0.0433 | +0.3386 ± 0.0036 | 0.9944 | 0.1689 | 0.6302 | 0.1009 | 0.0573 | -0.076 ± 0.003 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 852 | 0.2064 | 0.2068 | -0.0004 ± 0.0005 | 0.5939 | 0.5952 | 0.5053 | 0.4905 | 0.5153 | -0.100 ± 0.0167 | -0.0117 (6) |
| 3-5 | 603 | 0.2118 | 0.2089 | +0.0029 ± 0.0015 | 0.6068 | 0.6005 | 0.5143 | 0.4748 | 0.4544 | -0.131 ± 0.02 | 0.01 (3) |
| 5-10 | 1357 | 0.2075 | 0.2057 | +0.0018 ± 0.0019 | 0.6014 | 0.5964 | 0.5405 | 0.466 | 0.4937 | -0.088 ± 0.0127 | -0.01 (4) |
| 10-15 | 1181 | 0.2136 | 0.2067 | +0.0069 ± 0.0033 | 0.62 | 0.5993 | 0.5622 | 0.4378 | 0.475 | -0.102 ± 0.0138 | -0.04 (5) |
| 15-25 | 1716 | 0.2323 | 0.2125 | +0.0198 ± 0.0044 | 0.6604 | 0.6096 | 0.5857 | 0.3902 | 0.4388 | -0.101 ± 0.0114 | -0.0183 (12) |
| 25-40 | 1203 | 0.2676 | 0.1993 | +0.0683 ± 0.0081 | 0.7461 | 0.5791 | 0.6611 | 0.3471 | 0.3973 | -0.118 ± 0.0129 | -0.008 (5) |
| 40+ | 426 | 0.3719 | 0.1618 | +0.2101 ± 0.0195 | 1.0133 | 0.4896 | 0.7366 | 0.2477 | 0.2911 | -0.089 ± 0.0187 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4717 | 0.1926 | 0.1928 | -0.0002 ± 0.0002 | 0.5611 | 0.5613 | 0.5071 | 0.492 | 0.5075 | -0.040 ± 0.0066 | -0.0154 (26) |
| 3-5 | 3214 | 0.1931 | 0.192 | +0.0010 ± 0.0006 | 0.563 | 0.5596 | 0.5119 | 0.4722 | 0.4779 | -0.046 ± 0.0079 | 0.01 (5) |
| 5-10 | 7134 | 0.1969 | 0.1936 | +0.0033 ± 0.0008 | 0.5787 | 0.5663 | 0.5085 | 0.4343 | 0.4514 | -0.040 ± 0.0053 | -0.0117 (6) |
| 10-15 | 5920 | 0.203 | 0.191 | +0.0119 ± 0.0014 | 0.5953 | 0.559 | 0.51 | 0.3861 | 0.4007 | -0.050 ± 0.0058 | -0.0189 (18) |
| 15-25 | 8410 | 0.2174 | 0.181 | +0.0364 ± 0.0018 | 0.6317 | 0.531 | 0.5255 | 0.3299 | 0.3372 | -0.061 ± 0.0047 | -0.014 (52) |
| 25-40 | 7601 | 0.2514 | 0.1376 | +0.1137 ± 0.0027 | 0.7098 | 0.4202 | 0.5609 | 0.2438 | 0.2267 | -0.080 ± 0.0043 | -0.0095 (20) |
| 40+ | 5964 | 0.4022 | 0.0581 | +0.3441 ± 0.0036 | 1.0593 | 0.2101 | 0.6544 | 0.1179 | 0.0791 | -0.074 ± 0.003 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1037 | 0.1962 | 0.1975 | -0.0013 ± 0.0005 | 0.5722 | 0.5754 | 0.5029 | 0.4875 | 0.5304 | -0.054 ± 0.0144 | -0.0191 (11) |
| 3-5 | 736 | 0.2082 | 0.2066 | +0.0016 ± 0.0013 | 0.6031 | 0.5975 | 0.4996 | 0.46 | 0.462 | -0.111 ± 0.0175 | 0.002 (5) |
| 5-10 | 1602 | 0.2034 | 0.1996 | +0.0037 ± 0.0017 | 0.5921 | 0.5816 | 0.5126 | 0.4389 | 0.4494 | -0.106 ± 0.0115 | -0.01 (10) |
| 10-15 | 1293 | 0.2123 | 0.2036 | +0.0086 ± 0.0031 | 0.615 | 0.59 | 0.5378 | 0.4145 | 0.4432 | -0.106 ± 0.0126 | -0.0286 (7) |
| 15-25 | 1554 | 0.2311 | 0.213 | +0.0180 ± 0.0046 | 0.6596 | 0.6105 | 0.5866 | 0.3925 | 0.4427 | -0.106 ± 0.0117 | -0.03 (1) |
| 25-40 | 915 | 0.2131 | 0.2103 | +0.0027 ± 0.0089 | 0.6148 | 0.603 | 0.6595 | 0.3486 | 0.4973 | -0.055 ± 0.0138 | -0.0267 (3) |
| 40+ | 201 | 0.3076 | 0.1831 | +0.1245 ± 0.0271 | 0.8325 | 0.54 | 0.7426 | 0.2875 | 0.3881 | -0.083 ± 0.0277 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5320 | 0.1856 | 0.1862 | -0.0006 ± 0.0002 | 0.5469 | 0.5476 | 0.4853 | 0.47 | 0.488 | -0.033 ± 0.006 | -0.0189 (44) |
| 3-5 | 3805 | 0.2044 | 0.2025 | +0.0019 ± 0.0006 | 0.5939 | 0.5876 | 0.4805 | 0.441 | 0.4378 | -0.058 ± 0.0074 | -0.0073 (22) |
| 5-10 | 8105 | 0.1959 | 0.1904 | +0.0055 ± 0.0007 | 0.5751 | 0.5582 | 0.487 | 0.413 | 0.4131 | -0.057 ± 0.0049 | -0.0117 (42) |
| 10-15 | 6555 | 0.1945 | 0.1798 | +0.0147 ± 0.0013 | 0.5738 | 0.5311 | 0.4952 | 0.3719 | 0.3738 | -0.060 ± 0.0053 | -0.0136 (14) |
| 15-25 | 8427 | 0.2119 | 0.1726 | +0.0393 ± 0.0018 | 0.6177 | 0.509 | 0.5125 | 0.318 | 0.3151 | -0.070 ± 0.0045 | -0.0533 (3) |
| 25-40 | 6437 | 0.2167 | 0.1259 | +0.0907 ± 0.0028 | 0.6266 | 0.3865 | 0.5283 | 0.2127 | 0.2287 | -0.050 ± 0.0043 | -0.02 (4) |
| 40+ | 4311 | 0.3903 | 0.0484 | +0.3419 ± 0.0038 | 1.0171 | 0.1814 | 0.6391 | 0.1069 | 0.0647 | -0.075 ± 0.0032 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1473 | 0.1984 | 0.1984 | +0.0000 ± 0.0004 | 0.5756 | 0.5754 | 0.5085 | 0.4935 | 0.4976 | -0.069 ± 0.0119 | -0.0221 (56) |
| 3-5 | 1055 | 0.1886 | 0.1884 | +0.0002 ± 0.0011 | 0.5553 | 0.5532 | 0.4981 | 0.4582 | 0.4749 | -0.057 ± 0.0137 | -0.0194 (34) |
| 5-10 | 2129 | 0.2002 | 0.1953 | +0.0049 ± 0.0014 | 0.5902 | 0.574 | 0.5079 | 0.4343 | 0.4382 | -0.077 ± 0.0098 | -0.005 (78) |
| 10-15 | 1458 | 0.2145 | 0.2024 | +0.0121 ± 0.0029 | 0.6224 | 0.5884 | 0.5419 | 0.419 | 0.43 | -0.087 ± 0.0121 | 0.0012 (66) |
| 15-25 | 1920 | 0.2306 | 0.2078 | +0.0228 ± 0.0041 | 0.6582 | 0.5996 | 0.5919 | 0.3969 | 0.4375 | -0.089 ± 0.0105 | -0.0214 (59) |
| 25-40 | 1145 | 0.2399 | 0.2109 | +0.0290 ± 0.0083 | 0.6852 | 0.6047 | 0.689 | 0.377 | 0.4865 | -0.085 ± 0.0128 | -0.0252 (27) |
| 40+ | 414 | 0.3241 | 0.2011 | +0.1230 ± 0.021 | 0.9319 | 0.5854 | 0.8175 | 0.3416 | 0.4662 | -0.097 ± 0.0196 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5414 | 0.1782 | 0.1783 | -0.0001 ± 0.0002 | 0.5269 | 0.5267 | 0.5116 | 0.4964 | 0.5055 | -0.040 ± 0.0058 | -0.0154 (103) |
| 3-5 | 3739 | 0.1952 | 0.1943 | +0.0009 ± 0.0006 | 0.5696 | 0.567 | 0.502 | 0.4622 | 0.4715 | -0.041 ± 0.0073 | -0.0212 (73) |
| 5-10 | 7598 | 0.1969 | 0.1904 | +0.0065 ± 0.0008 | 0.5812 | 0.5611 | 0.5017 | 0.4282 | 0.4217 | -0.062 ± 0.0051 | -0.0084 (134) |
| 10-15 | 5190 | 0.2095 | 0.1933 | +0.0162 ± 0.0015 | 0.6103 | 0.5672 | 0.5366 | 0.4137 | 0.4077 | -0.071 ± 0.0062 | -0.0057 (111) |
| 15-25 | 6339 | 0.2314 | 0.2 | +0.0314 ± 0.0022 | 0.6648 | 0.5795 | 0.5768 | 0.3814 | 0.3994 | -0.068 ± 0.0057 | -0.026 (108) |
| 25-40 | 4128 | 0.2569 | 0.1904 | +0.0665 ± 0.0043 | 0.7269 | 0.5542 | 0.6404 | 0.328 | 0.3806 | -0.065 ± 0.0067 | -0.0277 (53) |
| 40+ | 1840 | 0.3681 | 0.1597 | +0.2084 ± 0.0096 | 1.0384 | 0.4753 | 0.7454 | 0.2448 | 0.2973 | -0.062 ± 0.0089 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7338 | 1.025 ± 0.033 | 1.097 | 0.1683 | 0.1676 | 0.2155 | 0.2044 |
| gen2 | 7338 | 0.815 ± 0.029 | 1.069 | 0.1733 | 0.1679 | 0.2339 | 0.2043 |
| gen1_elo | 7338 | 1.011 ± 0.032 | 1.088 | 0.1746 | 0.1677 | 0.2143 | 0.2044 |
| gen1_sr | 7338 | 1.001 ± 0.039 | 1.124 | 0.1333 | 0.1696 | 0.2299 | 0.204 |
| gen1_ledger | 9594 | 0.867 ± 0.024 | 1.076 | 0.1893 | 0.1748 | 0.217 | 0.2007 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 34,257)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 8,044 | 23.5% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,827 | 22.9% |
| BOOK_QUALITY | execution | 6,061 | 17.7% |
| POOR_DATA | data | 3,923 | 11.5% |
| LIMITED_DATA | data | 2,101 | 6.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,972 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 1,420 | 4.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,384 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 966 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 558 | 1.6% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 23.5%, coverage 22.9%, execution 17.7%, data 17.6%, market_freshness/coverage 8.6%, mapping 4.2%, model_calibration_or_unknown 4.0%, model_calibration 1.6%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.7%, LOW_DATA_QUALITY 71.4%, THIN_PLAYER_HISTORY 59.6%, STALE_PLAYER_DATA 51.9%, STALE_KALSHI_QUOTE 46.7%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 33.0%, WIDE_SPREAD 24.0%, MODEL_HIGH_UNCERTAINTY 18.7%, PLAYER_IDENTITY_RISK 15.2%, LEVEL_TRANSFER_RISK 9.8%, LOW_DISPLAYED_LIQUIDITY 8.3%, EVENT_MAPPING_RISK 7.2%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.3%, POST_SETTLEMENT_OBSERVATION 22.9%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 18,245)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,286 | 34.4% |
| STALE_QUOTE | market_freshness | 3,587 | 19.7% |
| BOOK_QUALITY | execution | 3,140 | 17.2% |
| POOR_DATA | data | 1,659 | 9.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,050 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 791 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 633 | 3.5% |
| LIMITED_DATA | data | 619 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 341 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 138 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.4%, market_freshness 19.7%, execution 17.2%, data 12.5%, market_freshness/coverage 9.2%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.1%, LOW_DATA_QUALITY 74.7%, THIN_PLAYER_HISTORY 61.7%, STALE_KALSHI_QUOTE 54.1%, STALE_PLAYER_DATA 45.6%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 34.2%, WIDE_SPREAD 23.4%, MODEL_HIGH_UNCERTAINTY 19.3%, PLAYER_IDENTITY_RISK 18.2%, EVENT_MAPPING_RISK 8.8%, LEVEL_TRANSFER_RISK 8.7%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.5%, POST_SETTLEMENT_OBSERVATION 34.4%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 14582, "IDENTITY_AMBIGUOUS": 3663}; ticker orientation: {"VERIFIED": 18245}.

Checks: discipline:AMBIGUOUS 1209, discipline:PASS 17036, identity_confidence:AMBIGUOUS 3326, identity_confidence:PASS 14919, level_mapping:NA 1221, level_mapping:PASS 17024, market_pair:AMBIGUOUS 499, market_pair:NA 411, market_pair:PASS 17335, model_complement:NA 373, model_complement:PASS 17872, namesake:AMBIGUOUS 6, namesake:PASS 18239, physical_match_id:NA 6169, physical_match_id:PASS 12076, player_ids:PASS 18245, same_pair_other_event:PASS 18245, ticker_orientation:PASS 18245

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,469 | 3.8% | 3.2% | 1.3% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 24, "market_freshness/coverage": 21} | 5.51 | 0.2226 / 0.2181 (837) | 25.2% | 2.4% | 3.0% | 2.9% |
| CHALLENGER | 12,325 | 16.4% | 6.2% | 11.1% | {"coverage": 1200, "market_freshness": 247, "market_freshness/coverage": 231, "data": 164, "model_calibration_or_unknown": 80, "execution": 41, "model_calibration": 39, "mapping": 17, "possible_market_error": 1} | 7.39 | 0.2217 / 0.2114 (2833) | 39.6% | 14.6% | 4.0% | 22.3% |
| DOUBLES | 2,610 | 46.3% | 46.3% | 6.6% | {"execution": 668, "mapping": 358, "market_freshness": 106, "market_freshness/coverage": 70, "coverage": 7} | 23.2 | 0.2975 / 0.2322 (649) | 9.0% | 0.0% | 100.0% | 6.3% |
| ITF_MEN | 23,769 | 25.2% | 17.7% | 32.8% | {"coverage": 2094, "market_freshness": 1199, "execution": 1003, "data": 879, "market_freshness/coverage": 594, "mapping": 210, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.72 | 0.2179 / 0.1998 (5015) | 40.4% | 69.2% | 15.2% | 21.5% |
| ITF_WOMEN | 30,992 | 26.4% | 18.8% | 44.9% | {"coverage": 2906, "market_freshness": 1774, "execution": 1345, "data": 1134, "market_freshness/coverage": 710, "mapping": 200, "model_calibration_or_unknown": 94, "model_calibration": 23} | 12.49 | 0.2026 / 0.1942 (5986) | 41.6% | 57.0% | 9.9% | 21.7% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,875 | 6.0% | 5.1% | 1.6% | {"market_freshness": 111, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.68 | 0.2312 / 0.2209 (800) | 30.1% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.6% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 725 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 311 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 12 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 899 min (STALE); no external reference |
| 15 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 18 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 17.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1037 min (STALE); no external reference |
| 19 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 20 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 21 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 22 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 23 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 24 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 25 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 163 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 26 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 27 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 28 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 29 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 30 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 31 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 32 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 33 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 34 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 365 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 35 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 36 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 37 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 38 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 39 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 40 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 41 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 463 min (STALE); no external reference |
| 43 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 44 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 45 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 46 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 124 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 49 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 50 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 82 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9708, "by_level_share_of_ge_25pp": {"ATP": 0.0134, "CHALLENGER": 0.1107, "DOUBLES": 0.0663, "ITF_MEN": 0.3283, "ITF_WOMEN": 0.4487, "OTHER": 0.0007, "WTA": 0.0159, "WTA125": 0.0161}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5411, "share_primary_cause_market_settled_or_in_play": 0.4368, "share_primary_cause_stale_quote_only": 0.1966}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 18245, "identity_ambiguous_share": 0.2008, "ticker_orientation": {"VERIFIED": 18245}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 12076, "with_external": 627, "coverage": 0.0519, "external_status": {"EXTERNAL_STALE": 397, "AGREES_WITH_KALSHI": 217, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 397, "MODEL_LONE_OUTLIER": 217, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3461, "share_external_supports_model": 0.0207}, "pregame_clean_ge_25pp": {"n": 5625, "with_external": 596, "coverage": 0.106, "external_status": {"EXTERNAL_STALE": 373, "AGREES_WITH_KALSHI": 210, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 373, "MODEL_LONE_OUTLIER": 210, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3523, "share_external_supports_model": 0.0218}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 490.0, "median_sample_ratio": 2.44, "median_min_matches": 18.0, "median_max_days_since_last": 240.0, "share_severe_asymmetry": 0.2079, "data_status": {"POOR": 10218, "LIMITED": 4711, "ADEQUATE": 3316}, "comparison_lt_10pp": {"median_thinner_serve_points": 1736.0, "median_sample_ratio": 1.69, "median_min_matches": 90.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1477, "model_minus_observed": 0.0647, "kalshi_minus_observed": -0.0744, "brier_diff_model_minus_kalshi": 0.0021}, "4-10x": {"n": 1000, "model_minus_observed": 0.0904, "kalshi_minus_observed": -0.0541, "brier_diff_model_minus_kalshi": 0.0087}, "<2x": {"n": 3628, "model_minus_observed": 0.0988, "kalshi_minus_observed": -0.0237, "brier_diff_model_minus_kalshi": 0.0142}, ">=10x": {"n": 1233, "model_minus_observed": 0.1192, "kalshi_minus_observed": -0.0543, "brier_diff_model_minus_kalshi": 0.0148}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 7338, "model": {"intercept": -0.551, "slope": 0.815, "slope_se": 0.029}, "kalshi_mid_same_rows": {"intercept": 0.179, "slope": 1.069, "slope_se": 0.033}, "mean_extremity_model": 0.1733, "mean_extremity_kalshi": 0.1679, "model_brier": 0.2339, "kalshi_brier": 0.2043, "brier_diff_model_minus_kalshi": 0.0296, "brier_diff_se": 0.0022, "model_logloss": 0.6654, "kalshi_logloss": 0.5911}, "fair_v1": {"n": 7338, "model": {"intercept": -0.45, "slope": 1.025, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.243, "slope": 1.097, "slope_se": 0.033}, "mean_extremity_model": 0.1683, "mean_extremity_kalshi": 0.1676, "model_brier": 0.2155, "kalshi_brier": 0.2044, "brier_diff_model_minus_kalshi": 0.0111, "brier_diff_se": 0.0018, "model_logloss": 0.6202, "kalshi_logloss": 0.5913}, "gen1_elo": {"n": 7338, "model": {"intercept": -0.438, "slope": 1.011, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.246, "slope": 1.088, "slope_se": 0.033}, "mean_extremity_model": 0.1746, "mean_extremity_kalshi": 0.1677, "model_brier": 0.2143, "kalshi_brier": 0.2044, "brier_diff_model_minus_kalshi": 0.0099, "brier_diff_se": 0.0018, "model_logloss": 0.6181, "kalshi_logloss": 0.5914}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2488, "share_ge_15": 0.4446, "median_abs_gap": 13.05, "n": 48540}, "gen1_elo": {"share_ge_25": 0.246, "share_ge_15": 0.4402, "median_abs_gap": 12.84, "n": 48540}, "gen1_sr": {"share_ge_25": 0.3133, "share_ge_15": 0.5204, "median_abs_gap": 15.82, "n": 48540}, "gen2": {"share_ge_25": 0.3144, "share_ge_15": 0.5104, "median_abs_gap": 15.46, "n": 48540}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1506, "share_ge_15": 0.353, "median_abs_gap": 10.66, "n": 37336}, "gen1_elo": {"share_ge_25": 0.1486, "share_ge_15": 0.3476, "median_abs_gap": 10.48, "n": 37336}, "gen1_sr": {"share_ge_25": 0.2152, "share_ge_15": 0.4382, "median_abs_gap": 12.95, "n": 37338}, "gen2": {"share_ge_25": 0.2305, "share_ge_15": 0.4381, "median_abs_gap": 12.83, "n": 37338}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.51, "share_ge_25_all": 0.0377, "share_ge_25_pregame_clean": 0.0317}, "WTA": {"median_abs_gap_pregame_clean": 7.68, "share_ge_25_all": 0.0597, "share_ge_25_pregame_clean": 0.0507}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2366, "share_within_10pp_all": 0.4387, "share_within_10pp_pregame_clean": 0.4923, "corr_model_vs_mid_pregame_clean": 0.8495}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1060, "model_brier": 0.1983, "kalshi_brier": 0.1986, "brier_diff_model_minus_kalshi": -0.0003}, "10-15": {"n_settled": 1274, "model_brier": 0.2182, "kalshi_brier": 0.2095, "brier_diff_model_minus_kalshi": 0.0087}, "15-25": {"n_settled": 1630, "model_brier": 0.2261, "kalshi_brier": 0.2085, "brier_diff_model_minus_kalshi": 0.0177}, "25-40": {"n_settled": 929, "model_brier": 0.2236, "kalshi_brier": 0.2059, "brier_diff_model_minus_kalshi": 0.0176}, "3-5": {"n_settled": 676, "model_brier": 0.2062, "kalshi_brier": 0.2059, "brier_diff_model_minus_kalshi": 0.0003}, "40+": {"n_settled": 191, "model_brier": 0.296, "kalshi_brier": 0.1751, "brier_diff_model_minus_kalshi": 0.121}, "5-10": {"n_settled": 1578, "model_brier": 0.2034, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0014}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.551, "slope": 0.815, "slope_se": 0.029}, "kalshi_slope": {"intercept": 0.179, "slope": 1.069, "slope_se": 0.033}, "n": 7338}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.484, "slope": 0.867, "slope_se": 0.024}, "kalshi_slope": {"intercept": 0.176, "slope": 1.076, "slope_se": 0.028}, "n": 9594}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 649, "model_brier": 0.2975, "kalshi_brier": 0.2322, "brier_diff_model_minus_kalshi": 0.0653, "brier_diff_se": 0.0115, "corr_model_outcome": 0.1063, "corr_kalshi_outcome": 0.2816}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
