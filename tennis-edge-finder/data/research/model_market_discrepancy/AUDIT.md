# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-29T23:42Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 68,978): 0-3 14.0%, 3-5 9.6%, 5-10 20.1%, 10-15 15.3%, 15-25 19.0%, 25-40 13.9%, 40+ 8.0%; median gap 11.89 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.9%, Challenger 10.9%, doubles 6.5%). Main tour: ATP 4.2% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 15,121): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.1%, STALE_QUOTE 18.6%, BOOK_QUALITY 18.5%, POOR_DATA 9.3%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IDENTITY_AMBIGUOUS 4.0%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.1%, market_freshness 18.6%, execution 18.5%, data 12.8%, market_freshness/coverage 9.1%, mapping 4.0%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.2% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.2% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 15,121 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.2% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 471.0 points vs 1667.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.017, Gen-2 0.81, Gen-1 ledger 0.855 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 730 model 0.2226 vs Kalshi 0.2059; n 153 model 0.2836 vs Kalshi 0.1908.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 293,803 model-market comparisons (479,972 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 98,341 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-29T23:23:57.518326+00:00'], shadow board 78,906 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-29T23:24:02.231232+00:00'], Model 4 36,733 rows, 23,911 settled tickers, 8,707 tickers with an external scan.
* By model: {"gen1_ledger": 66263, "gen1_elo": 39661, "fair_v1": 39661, "gen2": 39661, "gen1_sr": 39661, "model4_fundamental": 34470, "model4_conditioned": 34426}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 68,978 | 14.0 | 9.6 | 20.1 | 15.3 | 19.0 | 13.9 | 8.0 | 11.89 | 41.0% | 21.9% |
| MW fair_v1 | 39,661 | 12.9 | 8.7 | 18.7 | 15.4 | 19.5 | 15.0 | 9.9 | 13.05 | 44.4% | 24.9% |
| MW gen1_elo | 39,661 | 12.5 | 8.6 | 19.3 | 15.4 | 19.5 | 14.9 | 9.8 | 12.97 | 44.2% | 24.7% |
| MW gen1_ledger | 29,317 | 15.6 | 10.8 | 22.1 | 15.3 | 18.4 | 12.4 | 5.5 | 10.38 | 36.3% | 17.9% |
| MW gen1_sr | 39,661 | 10.1 | 7.2 | 16.8 | 13.8 | 20.7 | 18.6 | 12.8 | 15.91 | 52.1% | 31.4% |
| MW gen2 | 39,661 | 11.1 | 7.5 | 16.5 | 13.8 | 19.4 | 17.9 | 13.8 | 15.48 | 51.1% | 31.7% |
| all families model4_conditioned | 34,426 | 22.4 | 18.2 | 34.2 | 17.3 | 5.0 | 1.9 | 1.1 | 6.01 | 8.0% | 3.1% |
| all families model4_fundamental | 34,470 | 17.3 | 13.3 | 33.8 | 20.3 | 10.2 | 3.7 | 1.4 | 7.71 | 15.3% | 5.1% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.3%, >=15pp 41.0%, >=20pp 30.3%, >=25pp 21.9%, >=30pp 15.8%, >=40pp 8.0%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.31pp; >=10pp 44.8%, >=25pp 17.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,414 | 27.4 | 15.4 | 27.6 | 13.4 | 11.6 | 4.0 | 0.6 | 5.92 | 16.2% | 4.6% |
| CHALLENGER | 5,922 | 16.3 | 9.8 | 20.8 | 15.1 | 15.4 | 11.8 | 10.8 | 10.91 | 38.0% | 22.6% |
| ITF_MEN | 11,114 | 9.7 | 7.3 | 17.1 | 15.1 | 21.2 | 17.6 | 12.0 | 15.26 | 50.8% | 29.6% |
| ITF_WOMEN | 15,661 | 9.6 | 7.1 | 15.8 | 15.1 | 22.0 | 18.2 | 12.1 | 15.74 | 52.4% | 30.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,459 | 18.2 | 13.7 | 24.8 | 19.9 | 16.1 | 6.3 | 1.0 | 8.23 | 23.5% | 7.4% |
| WTA125 | 1,085 | 16.1 | 7.7 | 22.4 | 19.1 | 20.4 | 12.4 | 1.9 | 10.97 | 34.8% | 14.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,414 | 26.1 | 15.4 | 25.5 | 16.2 | 11.9 | 4.1 | 0.8 | 6.23 | 16.8% | 4.9% |
| CHALLENGER | 5,922 | 15.1 | 8.9 | 18.3 | 14.3 | 18.1 | 13.7 | 11.6 | 12.63 | 43.4% | 25.3% |
| ITF_MEN | 11,114 | 8.0 | 6.1 | 15.1 | 13.8 | 19.5 | 20.7 | 16.8 | 18.0 | 57.0% | 37.5% |
| ITF_WOMEN | 15,661 | 8.0 | 5.8 | 14.0 | 12.6 | 20.6 | 21.3 | 17.6 | 19.21 | 59.5% | 38.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,459 | 15.1 | 10.9 | 22.2 | 15.3 | 22.0 | 12.6 | 1.9 | 10.59 | 36.4% | 14.5% |
| WTA125 | 1,085 | 9.5 | 6.3 | 16.7 | 16.4 | 24.5 | 17.4 | 9.2 | 15.35 | 51.1% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,414 | 22.3 | 13.1 | 24.4 | 16.0 | 16.2 | 6.7 | 1.3 | 7.58 | 24.2% | 8.0% |
| CHALLENGER | 5,922 | 14.9 | 9.2 | 21.1 | 16.1 | 15.6 | 12.1 | 11.0 | 11.31 | 38.7% | 23.1% |
| ITF_MEN | 11,114 | 9.2 | 7.1 | 17.4 | 14.4 | 21.7 | 17.8 | 12.4 | 15.73 | 51.9% | 30.2% |
| ITF_WOMEN | 15,661 | 9.4 | 6.8 | 16.3 | 15.8 | 22.0 | 18.1 | 11.5 | 15.51 | 51.6% | 29.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,459 | 23.7 | 16.7 | 31.8 | 14.4 | 9.2 | 2.9 | 1.3 | 6.05 | 13.4% | 4.2% |
| WTA125 | 1,085 | 21.9 | 12.8 | 26.9 | 16.8 | 15.1 | 6.1 | 0.4 | 8.01 | 21.6% | 6.5% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,989 | 24.5 | 18.9 | 31.3 | 12.8 | 9.0 | 3.0 | 0.5 | 5.74 | 12.5% | 3.5% |
| CHALLENGER | 4,007 | 22.6 | 14.6 | 27.1 | 14.6 | 13.6 | 6.0 | 1.6 | 7.08 | 21.1% | 7.5% |
| DOUBLES | 2,108 | 5.1 | 4.5 | 12.2 | 10.8 | 21.0 | 24.9 | 21.4 | 23.54 | 67.4% | 46.4% |
| ITF_MEN | 8,435 | 13.0 | 9.4 | 21.2 | 15.8 | 21.3 | 13.3 | 5.9 | 11.9 | 40.5% | 19.2% |
| ITF_WOMEN | 10,067 | 13.1 | 9.2 | 19.7 | 15.7 | 21.2 | 15.5 | 5.6 | 12.37 | 42.3% | 21.1% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,463 | 24.5 | 15.3 | 30.4 | 17.6 | 9.1 | 2.7 | 0.3 | 6.69 | 12.1% | 3.0% |
| WTA125 | 1,099 | 24.8 | 12.7 | 21.1 | 18.7 | 13.7 | 7.2 | 1.6 | 7.9 | 22.6% | 8.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,315 | 27.7 | 15.6 | 27.9 | 13.4 | 11.4 | 3.7 | 0.4 | 5.88 | 15.4% | 4.0% |
| CHALLENGER | 4,144 | 21.2 | 12.3 | 25.9 | 17.6 | 15.3 | 6.1 | 1.5 | 8.03 | 22.9% | 7.6% |
| ITF_MEN | 8,123 | 11.9 | 8.8 | 20.6 | 17.2 | 22.0 | 14.3 | 5.2 | 12.4 | 41.5% | 19.5% |
| ITF_WOMEN | 11,614 | 11.5 | 8.5 | 18.4 | 17.3 | 24.0 | 15.2 | 5.2 | 13.32 | 44.3% | 20.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,377 | 18.5 | 13.6 | 25.0 | 20.1 | 16.2 | 5.9 | 0.6 | 8.18 | 22.7% | 6.4% |
| WTA125 | 1,049 | 16.4 | 7.5 | 21.9 | 19.4 | 20.9 | 12.2 | 1.7 | 11.03 | 34.8% | 13.9% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,315 | 26.4 | 15.7 | 25.7 | 16.1 | 11.9 | 3.7 | 0.5 | 6.2 | 16.1% | 4.2% |
| CHALLENGER | 4,144 | 19.2 | 11.5 | 23.0 | 16.8 | 18.6 | 9.1 | 1.9 | 9.02 | 29.6% | 11.0% |
| ITF_MEN | 8,124 | 9.5 | 7.2 | 17.4 | 16.0 | 21.3 | 18.9 | 9.7 | 14.95 | 49.9% | 28.5% |
| ITF_WOMEN | 11,615 | 8.9 | 6.7 | 15.9 | 14.1 | 22.8 | 20.8 | 10.8 | 16.62 | 54.3% | 31.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,377 | 15.3 | 11.0 | 22.4 | 15.4 | 22.2 | 12.5 | 1.2 | 10.43 | 35.9% | 13.7% |
| WTA125 | 1,049 | 9.5 | 6.3 | 16.8 | 16.6 | 24.4 | 17.7 | 8.7 | 15.22 | 50.8% | 26.4% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,935 | 24.6 | 19.1 | 31.3 | 13.0 | 8.7 | 2.8 | 0.4 | 5.67 | 11.9% | 3.3% |
| CHALLENGER | 3,532 | 24.1 | 15.5 | 28.3 | 14.8 | 12.8 | 4.0 | 0.5 | 6.58 | 17.4% | 4.5% |
| DOUBLES | 1,977 | 5.1 | 4.5 | 12.4 | 11.0 | 20.8 | 24.8 | 21.3 | 23.31 | 67.0% | 46.1% |
| ITF_MEN | 7,201 | 13.8 | 10.0 | 22.9 | 16.4 | 21.2 | 11.8 | 3.9 | 10.94 | 36.9% | 15.7% |
| ITF_WOMEN | 8,560 | 13.7 | 9.7 | 20.9 | 16.4 | 21.3 | 14.4 | 3.5 | 11.57 | 39.3% | 17.9% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,409 | 24.9 | 15.7 | 30.4 | 17.7 | 9.1 | 2.1 | 0.1 | 6.57 | 11.3% | 2.2% |
| WTA125 | 974 | 26.2 | 13.6 | 22.2 | 19.8 | 12.7 | 5.0 | 0.5 | 7.36 | 18.3% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,108 | 5.1 | 4.5 | 12.2 | 10.8 | 21.0 | 24.9 | 21.4 | 23.54 | 67.4% | 46.4% |
| singles | 27,209 | 16.4 | 11.3 | 22.8 | 15.6 | 18.2 | 11.4 | 4.3 | 9.85 | 33.9% | 15.7% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,892 | 13.1 | 9.3 | 20.1 | 15.6 | 19.1 | 13.9 | 9.0 | 12.39 | 41.9% | 22.8% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 26,015 | 13.4 | 8.7 | 18.5 | 15.1 | 19.3 | 15.1 | 10.0 | 13.01 | 44.4% | 25.1% |
| UNKNOWN | 5,505 | 10.3 | 7.7 | 17.1 | 16.6 | 21.1 | 16.0 | 11.1 | 14.18 | 48.2% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 10,957 | 20.0 | 12.1 | 22.4 | 15.6 | 14.7 | 9.3 | 6.0 | 8.59 | 30.0% | 15.3% |
| B | 4,890 | 12.7 | 9.1 | 19.2 | 15.9 | 19.2 | 12.7 | 11.2 | 12.61 | 43.1% | 23.9% |
| C | 5,685 | 11.9 | 8.9 | 19.9 | 15.8 | 18.6 | 14.3 | 10.6 | 12.8 | 43.5% | 24.9% |
| D | 6,276 | 12.0 | 8.2 | 17.6 | 15.4 | 21.6 | 15.9 | 9.3 | 13.78 | 46.8% | 25.2% |
| F | 11,853 | 7.4 | 5.5 | 15.0 | 14.7 | 23.3 | 21.0 | 13.0 | 17.71 | 57.4% | 34.0% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,775 | 24.1 | 15.7 | 28.9 | 15.2 | 11.0 | 3.7 | 1.3 | 6.53 | 16.1% | 5.0% |
| B | 4,137 | 17.0 | 10.7 | 24.0 | 16.5 | 18.8 | 9.8 | 3.1 | 9.61 | 31.7% | 12.9% |
| C | 5,723 | 11.2 | 7.9 | 19.5 | 14.7 | 20.9 | 15.7 | 10.1 | 13.45 | 46.7% | 25.7% |
| D | 4,307 | 14.4 | 9.9 | 21.6 | 15.4 | 20.0 | 13.2 | 5.4 | 11.26 | 38.7% | 18.6% |
| F | 7,375 | 9.9 | 8.3 | 16.0 | 15.0 | 23.1 | 20.0 | 7.7 | 15.44 | 50.8% | 27.7% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 12,434 | 18.2 | 11.0 | 21.4 | 15.3 | 15.2 | 10.1 | 8.8 | 9.78 | 34.1% | 18.9% |
| LIMITED | 8,730 | 13.5 | 10.0 | 20.4 | 16.2 | 18.9 | 13.2 | 7.6 | 11.74 | 39.8% | 20.9% |
| POOR | 18,497 | 9.0 | 6.5 | 16.0 | 15.0 | 22.7 | 19.1 | 11.7 | 16.18 | 53.5% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,527 | 24.1 | 18.1 | 33.0 | 15.0 | 6.6 | 2.8 | 0.4 | 5.86 | 9.8% | 3.2% |
| GAME_SPREAD | 5,895 | 22.1 | 15.2 | 33.0 | 17.2 | 9.0 | 3.0 | 0.6 | 6.74 | 12.6% | 3.6% |
| MATCH_WINNER | 29,317 | 15.6 | 10.8 | 22.1 | 15.3 | 18.4 | 12.4 | 5.5 | 10.38 | 36.3% | 17.9% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 13,666 | 27.5 | 16.7 | 31.0 | 12.5 | 9.5 | 2.5 | 0.3 | 5.68 | 12.3% | 2.8% |
| TOTAL_GAMES | 9,834 | 9.6 | 10.3 | 35.8 | 26.8 | 10.5 | 4.1 | 2.8 | 9.3 | 17.4% | 6.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,171 | 24.4 | 30.1 | 32.9 | 7.3 | 4.1 | 0.9 | 0.3 | 4.71 | 5.3% | 1.2% |
| GAME_SPREAD | 8,049 | 47.3 | 16.0 | 25.3 | 7.3 | 2.2 | 1.3 | 0.6 | 3.27 | 4.1% | 1.9% |
| TOTAL_GAMES | 14,206 | 6.5 | 9.2 | 40.3 | 31.4 | 7.2 | 3.2 | 2.2 | 9.31 | 12.6% | 5.4% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,182 | 23.9 | 16.9 | 34.7 | 14.4 | 7.1 | 2.6 | 0.4 | 6.02 | 10.2% | 3.0% |
| GAME_SPREAD | 8,052 | 20.2 | 13.5 | 27.9 | 20.4 | 12.5 | 4.3 | 1.1 | 7.82 | 17.9% | 5.4% |
| TOTAL_GAMES | 14,236 | 10.0 | 10.2 | 36.3 | 25.3 | 11.5 | 4.2 | 2.4 | 9.19 | 18.2% | 6.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 39,661 | 44.4% | 24.9% | 13.05 | 35.5% | 15.3% | 10.73 |
| gen1_elo | 39,661 | 44.2% | 24.7% | 12.97 | 35.2% | 15.3% | 10.54 |
| gen1_sr | 39,661 | 52.1% | 31.4% | 15.91 | 44.2% | 21.8% | 13.03 |
| gen2 | 39,661 | 51.1% | 31.7% | 15.48 | 44.1% | 23.4% | 12.92 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 18,643 | 15.6 | 10.6 | 21.3 | 17.2 | 20.1 | 12.0 | 3.3 | 10.71 | 35.4% | 15.3% |
| STALE | 21,018 | 10.5 | 7.0 | 16.3 | 13.8 | 19.0 | 17.6 | 15.8 | 16.02 | 52.4% | 33.4% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 22,785 | 16.3 | 11.1 | 22.7 | 15.4 | 17.8 | 11.9 | 4.7 | 9.95 | 34.4% | 16.6% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 68,978 | 22785 | 22115 | 24078 | 24.4 | 127.9 | 1451.1 |
| ge_15pp | 28,255 | 7846 | 7884 | 12525 | 26.9 | 439.8 | 1451.1 |
| ge_25pp | 15,121 | 3782 | 3443 | 7896 | 32.3 | 588.2 | 1431.1 |
| lt_10pp | 30,158 | 11428 | 10480 | 8250 | 22.4 | 47.1 | 1421.1 |

Current slate `SL-20261029T234158Z-d930eea7`: 388 priced rows, quote age at build {'median': 18.4, 'max': 18.5}, freshness {'AGING': 388}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 45 | 0.0 | 0.0 | 31.1 | 6.7 | 35.6 | 22.2 | 4.4 | 20.19 | 62.2% | 26.7% |
| EXTERNAL_LONE_OUTLIER | 24 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.37 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,889 | 19.6 | 11.1 | 25.2 | 18.0 | 17.9 | 7.3 | 0.9 | 8.67 | 26.1% | 8.2% |
| KALSHI_LONE_OUTLIER | 26 | 3.9 | 3.9 | 76.9 | 7.7 | 3.9 | 3.9 | 0.0 | 6.31 | 7.7% | 3.9% |
| MARKETS_AGREE | 775 | 65.4 | 34.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.21 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,688 | 0.0 | 2.4 | 36.3 | 25.4 | 24.9 | 10.1 | 0.9 | 12.12 | 36.0% | 11.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 39,661 | 6447 (16.3%) | 26.2% | 1.1% | {"EXTERNAL_STALE": 3889, "AGREES_WITH_KALSHI": 1688, "ALL_AGREE": 775, "SUPPORTS_MODEL_DIRECTION": 44, "AGREES_WITH_MODEL": 26, "EXTERNAL_OUTLIER": 24, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 17,610 | 1652 (9.4%) | 36.7% | 1.8% | {"EXTERNAL_STALE": 1015, "AGREES_WITH_KALSHI": 607, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 9,877 | 518 (5.2%) | 35.9% | 2.5% | {"EXTERNAL_STALE": 319, "AGREES_WITH_KALSHI": 186, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,694 | 491 (10.5%) | 36.5% | 2.6% | {"EXTERNAL_STALE": 299, "AGREES_WITH_KALSHI": 179, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 15,961 | 3662 (22.9%) | 17.8% | 1.0% | {"EXTERNAL_STALE": 2175, "ALL_AGREE": 775, "AGREES_WITH_KALSHI": 652, "EXTERNAL_OUTLIER": 24, "AGREES_WITH_MODEL": 22, "SUPPORTS_MODEL_DIRECTION": 13, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 7,777 | 10.4 | 7.5 | 19.7 | 14.3 | 21.6 | 16.6 | 10.0 | 14.12 | 48.1% | 26.6% |
| 4-10x | 5,362 | 11.1 | 8.5 | 18.6 | 15.6 | 21.9 | 14.4 | 10.0 | 13.67 | 46.3% | 24.4% |
| <2x | 20,030 | 15.1 | 10.0 | 19.4 | 16.0 | 17.4 | 13.1 | 9.0 | 11.6 | 39.5% | 22.1% |
| >=10x | 6,492 | 10.5 | 6.4 | 15.1 | 14.4 | 21.6 | 19.3 | 12.6 | 16.3 | 53.5% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 10,169 | 12.6 | 8.8 | 19.6 | 16.0 | 18.9 | 13.5 | 10.5 | 12.7 | 43.0% | 24.0% |
| 300-1000 | 8,595 | 12.0 | 8.6 | 17.8 | 15.2 | 20.3 | 16.4 | 9.6 | 13.63 | 46.3% | 26.0% |
| <300 | 12,813 | 8.2 | 5.8 | 15.1 | 14.8 | 23.0 | 20.1 | 12.9 | 17.09 | 56.0% | 33.0% |
| >=3000 | 8,084 | 21.6 | 13.2 | 24.0 | 15.5 | 13.8 | 7.2 | 4.9 | 7.56 | 25.8% | 12.1% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1139 | 0.5493 | 0.4103 | 0.496 | +0.053 | -0.086 | -0.0019 ± 0.0046 |
| ratio 4-10x | 790 | 0.5794 | 0.4331 | 0.4937 | +0.086 | -0.060 | 0.008 ± 0.0057 |
| ratio <2x | 2734 | 0.5379 | 0.4146 | 0.4484 | +0.089 | -0.034 | 0.0118 ± 0.0028 |
| ratio >=10x | 987 | 0.5681 | 0.3937 | 0.4529 | +0.115 | -0.059 | 0.0131 ± 0.0058 |
| thinner_sample 1000-3000 | 1527 | 0.5397 | 0.4126 | 0.4538 | +0.086 | -0.041 | 0.0088 ± 0.0037 |
| thinner_sample 300-1000 | 1289 | 0.5672 | 0.4253 | 0.4856 | +0.082 | -0.060 | 0.0029 ± 0.0044 |
| thinner_sample <300 | 1901 | 0.5592 | 0.3916 | 0.4613 | +0.098 | -0.070 | 0.0106 ± 0.0041 |
| thinner_sample >=3000 | 933 | 0.5321 | 0.4381 | 0.463 | +0.069 | -0.025 | 0.013 ± 0.0037 |
| data_status ADEQUATE | 1532 | 0.5344 | 0.4317 | 0.451 | +0.083 | -0.019 | 0.0125 ± 0.0031 |
| data_status LIMITED | 1370 | 0.549 | 0.4154 | 0.4745 | +0.074 | -0.059 | 0.0062 ± 0.0041 |
| data_status POOR | 2748 | 0.5618 | 0.4007 | 0.4683 | +0.093 | -0.068 | 0.0079 ± 0.0033 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 821 | 0.1984 | 0.1989 | -0.0005 ± 0.0005 | 0.5761 | 0.5775 | 0.5032 | 0.488 | 0.5104 | -0.086 ± 0.0165 | -0.01 (5) |
| 3-5 | 515 | 0.2056 | 0.2059 | -0.0004 ± 0.0016 | 0.5937 | 0.5932 | 0.5042 | 0.4643 | 0.4874 | -0.096 ± 0.0205 | 0.02 (1) |
| 5-10 | 1186 | 0.2008 | 0.2014 | -0.0005 ± 0.0019 | 0.5873 | 0.586 | 0.5109 | 0.4372 | 0.4755 | -0.085 ± 0.0134 | -0.0167 (6) |
| 10-15 | 993 | 0.2206 | 0.2119 | +0.0087 ± 0.0036 | 0.6339 | 0.6091 | 0.5264 | 0.4028 | 0.428 | -0.109 ± 0.0147 | -0.048 (5) |
| 15-25 | 1252 | 0.2252 | 0.2127 | +0.0124 ± 0.0051 | 0.6461 | 0.6098 | 0.5766 | 0.3811 | 0.4473 | -0.099 ± 0.0131 | -0.0033 (9) |
| 25-40 | 730 | 0.2226 | 0.2059 | +0.0168 ± 0.01 | 0.6348 | 0.5932 | 0.6549 | 0.3445 | 0.4726 | -0.075 ± 0.0154 | -0.01 (1) |
| 40+ | 153 | 0.2836 | 0.1908 | +0.0928 ± 0.0308 | 0.7727 | 0.5616 | 0.7405 | 0.2924 | 0.4183 | -0.075 ± 0.0306 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4493 | 0.1829 | 0.1837 | -0.0008 ± 0.0002 | 0.5399 | 0.5409 | 0.4874 | 0.4722 | 0.501 | -0.025 ± 0.0065 | -0.0129 (17) |
| 3-5 | 3027 | 0.1957 | 0.1938 | +0.0018 ± 0.0006 | 0.5704 | 0.5637 | 0.4825 | 0.4427 | 0.4387 | -0.059 ± 0.0081 | 0.0 (2) |
| 5-10 | 6420 | 0.2024 | 0.1991 | +0.0034 ± 0.0008 | 0.5907 | 0.5791 | 0.4844 | 0.4108 | 0.4257 | -0.045 ± 0.0056 | -0.0119 (21) |
| 10-15 | 5367 | 0.2015 | 0.1856 | +0.0158 ± 0.0015 | 0.5891 | 0.5457 | 0.484 | 0.36 | 0.3576 | -0.066 ± 0.0059 | -0.0281 (16) |
| 15-25 | 6708 | 0.2061 | 0.1679 | +0.0382 ± 0.002 | 0.6047 | 0.4982 | 0.4993 | 0.3032 | 0.3047 | -0.069 ± 0.005 | -0.0025 (44) |
| 25-40 | 5308 | 0.2215 | 0.125 | +0.0965 ± 0.003 | 0.6372 | 0.3843 | 0.5255 | 0.2113 | 0.2189 | -0.059 ± 0.0047 | -0.01 (1) |
| 40+ | 3477 | 0.3848 | 0.045 | +0.3398 ± 0.0041 | 1.0026 | 0.1737 | 0.6332 | 0.104 | 0.0598 | -0.078 ± 0.0034 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 650 | 0.2049 | 0.2054 | -0.0006 ± 0.0006 | 0.5911 | 0.5926 | 0.508 | 0.4931 | 0.52 | -0.103 ± 0.0193 | -0.01 (3) |
| 3-5 | 462 | 0.2212 | 0.2186 | +0.0026 ± 0.0017 | 0.6269 | 0.6216 | 0.5118 | 0.4722 | 0.4545 | -0.128 ± 0.0231 | 0.02 (1) |
| 5-10 | 1035 | 0.2074 | 0.2069 | +0.0005 ± 0.0021 | 0.6006 | 0.5985 | 0.5445 | 0.4698 | 0.5053 | -0.086 ± 0.0146 | -0.01 (4) |
| 10-15 | 918 | 0.2165 | 0.2102 | +0.0063 ± 0.0038 | 0.6241 | 0.6076 | 0.5646 | 0.4402 | 0.4793 | -0.108 ± 0.0158 | -0.04 (5) |
| 15-25 | 1310 | 0.2295 | 0.2145 | +0.0151 ± 0.005 | 0.6537 | 0.6131 | 0.5833 | 0.388 | 0.4496 | -0.094 ± 0.013 | -0.0133 (9) |
| 25-40 | 931 | 0.2681 | 0.1967 | +0.0714 ± 0.0091 | 0.7483 | 0.574 | 0.6579 | 0.3438 | 0.3899 | -0.133 ± 0.0145 | -0.0075 (4) |
| 40+ | 344 | 0.3601 | 0.1678 | +0.1923 ± 0.0219 | 0.9887 | 0.5035 | 0.7319 | 0.2472 | 0.3052 | -0.078 ± 0.0214 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3885 | 0.1894 | 0.1896 | -0.0002 ± 0.0002 | 0.5536 | 0.5538 | 0.5098 | 0.4948 | 0.5097 | -0.042 ± 0.0072 | -0.0133 (15) |
| 3-5 | 2629 | 0.1965 | 0.1954 | +0.0011 ± 0.0007 | 0.5699 | 0.5663 | 0.5112 | 0.4715 | 0.4755 | -0.048 ± 0.0088 | 0.02 (1) |
| 5-10 | 5696 | 0.1981 | 0.1948 | +0.0033 ± 0.0009 | 0.5813 | 0.5687 | 0.5109 | 0.4368 | 0.4542 | -0.042 ± 0.0059 | -0.0117 (6) |
| 10-15 | 4801 | 0.2044 | 0.1925 | +0.0120 ± 0.0016 | 0.5983 | 0.5623 | 0.5125 | 0.3887 | 0.4032 | -0.053 ± 0.0064 | -0.0189 (18) |
| 15-25 | 6725 | 0.2169 | 0.1812 | +0.0357 ± 0.002 | 0.6311 | 0.5313 | 0.523 | 0.3276 | 0.3374 | -0.061 ± 0.0052 | -0.0086 (42) |
| 25-40 | 6193 | 0.251 | 0.1359 | +0.1152 ± 0.003 | 0.7083 | 0.4167 | 0.5572 | 0.2404 | 0.2206 | -0.085 ± 0.0047 | -0.0044 (18) |
| 40+ | 4871 | 0.3982 | 0.0587 | +0.3395 ± 0.004 | 1.0513 | 0.2115 | 0.6517 | 0.1168 | 0.0805 | -0.073 ± 0.0034 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 788 | 0.1955 | 0.1977 | -0.0022 ± 0.0006 | 0.5696 | 0.5752 | 0.5007 | 0.4853 | 0.5457 | -0.038 ± 0.0165 | -0.0137 (8) |
| 3-5 | 549 | 0.205 | 0.2032 | +0.0018 ± 0.0016 | 0.5929 | 0.5867 | 0.4952 | 0.4555 | 0.4536 | -0.121 ± 0.0199 | 0.0067 (3) |
| 5-10 | 1224 | 0.203 | 0.2014 | +0.0016 ± 0.0019 | 0.5916 | 0.5857 | 0.5093 | 0.4356 | 0.4608 | -0.094 ± 0.0132 | -0.0071 (7) |
| 10-15 | 993 | 0.2087 | 0.2043 | +0.0045 ± 0.0036 | 0.607 | 0.5921 | 0.5388 | 0.4154 | 0.4602 | -0.096 ± 0.0144 | -0.0317 (6) |
| 15-25 | 1186 | 0.234 | 0.2172 | +0.0168 ± 0.0053 | 0.667 | 0.6197 | 0.5879 | 0.3936 | 0.4477 | -0.111 ± 0.0136 | -0.03 (1) |
| 25-40 | 747 | 0.2135 | 0.2128 | +0.0007 ± 0.0099 | 0.6158 | 0.6093 | 0.6629 | 0.3524 | 0.5047 | -0.059 ± 0.0152 | 0.015 (2) |
| 40+ | 163 | 0.2995 | 0.196 | +0.1035 ± 0.0306 | 0.8153 | 0.5732 | 0.7492 | 0.2987 | 0.4172 | -0.077 ± 0.0316 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4325 | 0.1834 | 0.184 | -0.0006 ± 0.0002 | 0.5401 | 0.5412 | 0.4835 | 0.4682 | 0.4853 | -0.035 ± 0.0066 | -0.0163 (35) |
| 3-5 | 2979 | 0.2018 | 0.1996 | +0.0023 ± 0.0007 | 0.5867 | 0.5788 | 0.4811 | 0.4416 | 0.4334 | -0.065 ± 0.0083 | -0.0094 (18) |
| 5-10 | 6575 | 0.1945 | 0.1908 | +0.0037 ± 0.0008 | 0.5722 | 0.5592 | 0.4842 | 0.4102 | 0.4228 | -0.046 ± 0.0054 | -0.01 (31) |
| 10-15 | 5329 | 0.1915 | 0.1786 | +0.0129 ± 0.0014 | 0.5664 | 0.529 | 0.4933 | 0.3699 | 0.3787 | -0.055 ± 0.0058 | -0.015 (12) |
| 15-25 | 6832 | 0.2129 | 0.173 | +0.0399 ± 0.002 | 0.6201 | 0.5098 | 0.5124 | 0.3179 | 0.3143 | -0.073 ± 0.005 | -0.03 (2) |
| 25-40 | 5294 | 0.2163 | 0.1285 | +0.0878 ± 0.0031 | 0.6259 | 0.3924 | 0.5292 | 0.2138 | 0.2346 | -0.048 ± 0.0048 | 0.01 (3) |
| 40+ | 3466 | 0.3946 | 0.0504 | +0.3442 ± 0.0043 | 1.0291 | 0.188 | 0.6427 | 0.1108 | 0.0664 | -0.079 ± 0.0036 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1184 | 0.1955 | 0.1957 | -0.0002 ± 0.0005 | 0.5696 | 0.5697 | 0.5045 | 0.4894 | 0.4941 | -0.068 ± 0.0131 | -0.0224 (49) |
| 3-5 | 843 | 0.1867 | 0.1858 | +0.0009 ± 0.0012 | 0.5475 | 0.5447 | 0.4968 | 0.4569 | 0.4638 | -0.069 ± 0.0152 | -0.0194 (34) |
| 5-10 | 1748 | 0.2017 | 0.1969 | +0.0048 ± 0.0016 | 0.5924 | 0.5774 | 0.5016 | 0.428 | 0.4331 | -0.075 ± 0.0108 | -0.005 (78) |
| 10-15 | 1199 | 0.2158 | 0.2039 | +0.0119 ± 0.0032 | 0.624 | 0.5918 | 0.5371 | 0.4143 | 0.4254 | -0.085 ± 0.0134 | 0.0014 (64) |
| 15-25 | 1539 | 0.2318 | 0.2111 | +0.0207 ± 0.0046 | 0.6605 | 0.6072 | 0.5825 | 0.3878 | 0.4347 | -0.083 ± 0.0118 | -0.0214 (59) |
| 25-40 | 965 | 0.2453 | 0.2101 | +0.0352 ± 0.009 | 0.7005 | 0.6024 | 0.6842 | 0.3722 | 0.4725 | -0.096 ± 0.0139 | -0.0219 (26) |
| 40+ | 325 | 0.3354 | 0.2036 | +0.1318 ± 0.0241 | 0.9718 | 0.5927 | 0.8163 | 0.3393 | 0.4554 | -0.099 ± 0.0226 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4428 | 0.1755 | 0.1758 | -0.0002 ± 0.0002 | 0.5199 | 0.5201 | 0.5084 | 0.4931 | 0.5054 | -0.037 ± 0.0063 | -0.0157 (88) |
| 3-5 | 3041 | 0.1929 | 0.1913 | +0.0015 ± 0.0006 | 0.5617 | 0.5587 | 0.5025 | 0.4627 | 0.463 | -0.051 ± 0.008 | -0.0209 (69) |
| 5-10 | 6195 | 0.1989 | 0.1919 | +0.0070 ± 0.0008 | 0.5846 | 0.5644 | 0.4968 | 0.4231 | 0.4147 | -0.066 ± 0.0056 | -0.0082 (132) |
| 10-15 | 4337 | 0.2113 | 0.1957 | +0.0156 ± 0.0017 | 0.6137 | 0.5726 | 0.5347 | 0.4117 | 0.4088 | -0.069 ± 0.0068 | -0.0053 (105) |
| 15-25 | 5262 | 0.2297 | 0.2011 | +0.0286 ± 0.0024 | 0.6605 | 0.5817 | 0.5695 | 0.3742 | 0.3997 | -0.062 ± 0.0062 | -0.0253 (107) |
| 25-40 | 3538 | 0.2608 | 0.1868 | +0.0740 ± 0.0046 | 0.7377 | 0.5451 | 0.6364 | 0.3236 | 0.3646 | -0.080 ± 0.0071 | -0.0229 (51) |
| 40+ | 1528 | 0.3783 | 0.154 | +0.2243 ± 0.0104 | 1.0715 | 0.4606 | 0.741 | 0.2393 | 0.2775 | -0.074 ± 0.0096 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5650 | 1.017 ± 0.037 | 1.092 | 0.1694 | 0.1665 | 0.2148 | 0.2061 |
| gen2 | 5650 | 0.81 ± 0.034 | 1.054 | 0.1715 | 0.1669 | 0.2341 | 0.2059 |
| gen1_elo | 5650 | 0.993 ± 0.036 | 1.088 | 0.1758 | 0.1667 | 0.2138 | 0.2062 |
| gen1_sr | 5650 | 0.994 ± 0.044 | 1.113 | 0.1317 | 0.1688 | 0.2302 | 0.2056 |
| gen1_ledger | 7803 | 0.855 ± 0.027 | 1.059 | 0.1878 | 0.1761 | 0.2182 | 0.2013 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 28,255)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,389 | 22.6% |
| STALE_QUOTE | market_freshness | 6,164 | 21.8% |
| BOOK_QUALITY | execution | 5,358 | 19.0% |
| POOR_DATA | data | 3,306 | 11.7% |
| LIMITED_DATA | data | 1,748 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,615 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,220 | 4.3% |
| IDENTITY_AMBIGUOUS | mapping | 1,148 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 818 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 488 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.6%, market_freshness 21.8%, execution 19.0%, data 17.9%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.3%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.5%, LOW_DATA_QUALITY 71.8%, THIN_PLAYER_HISTORY 60.6%, STALE_PLAYER_DATA 52.3%, STALE_KALSHI_QUOTE 44.3%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 33.5%, WIDE_SPREAD 25.0%, MODEL_HIGH_UNCERTAINTY 18.1%, PLAYER_IDENTITY_RISK 15.6%, LEVEL_TRANSFER_RISK 10.4%, LOW_DISPLAYED_LIQUIDITY 8.0%, EVENT_MAPPING_RISK 7.4%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.4%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.1%, POST_SETTLEMENT_OBSERVATION 22.6%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 15,121)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,160 | 34.1% |
| STALE_QUOTE | market_freshness | 2,819 | 18.6% |
| BOOK_QUALITY | execution | 2,794 | 18.5% |
| POOR_DATA | data | 1,414 | 9.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 846 | 5.6% |
| IDENTITY_AMBIGUOUS | mapping | 613 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 529 | 3.5% |
| LIMITED_DATA | data | 516 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 306 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 123 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.1%, market_freshness 18.6%, execution 18.5%, data 12.8%, market_freshness/coverage 9.1%, mapping 4.0%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 75.1%, THIN_PLAYER_HISTORY 62.7%, STALE_KALSHI_QUOTE 52.2%, STALE_PLAYER_DATA 46.4%, MODEL_INTERNAL_DISAGREEMENT 42.8%, ASYMMETRIC_SAMPLE_SIZE 34.5%, WIDE_SPREAD 24.5%, MODEL_HIGH_UNCERTAINTY 18.8%, PLAYER_IDENTITY_RISK 18.4%, LEVEL_TRANSFER_RISK 9.2%, EVENT_MAPPING_RISK 8.9%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.1%, POST_SETTLEMENT_OBSERVATION 34.1%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 12026, "IDENTITY_AMBIGUOUS": 3095}; ticker orientation: {"VERIFIED": 15121}.

Checks: discipline:AMBIGUOUS 978, discipline:PASS 14143, identity_confidence:AMBIGUOUS 2775, identity_confidence:PASS 12346, level_mapping:NA 990, level_mapping:PASS 14131, market_pair:AMBIGUOUS 479, market_pair:NA 347, market_pair:PASS 14295, model_complement:NA 311, model_complement:PASS 14810, namesake:AMBIGUOUS 6, namesake:PASS 15115, physical_match_id:NA 5244, physical_match_id:PASS 9877, player_ids:PASS 15121, same_pair_other_event:PASS 15121, ticker_orientation:PASS 15121

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,403 | 4.2% | 3.8% | 1.5% | {"market_freshness": 56, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 17, "coverage": 13} | 5.84 | 0.2207 / 0.2165 (633) | 21.6% | 2.9% | 3.2% | 2.8% |
| CHALLENGER | 9,929 | 16.5% | 6.2% | 10.9% | {"coverage": 971, "market_freshness/coverage": 196, "market_freshness": 167, "data": 144, "model_calibration_or_unknown": 74, "execution": 37, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.25 | 0.2207 / 0.2115 (2267) | 35.4% | 15.7% | 4.2% | 22.7% |
| DOUBLES | 2,108 | 46.4% | 46.1% | 6.5% | {"execution": 555, "mapping": 251, "market_freshness": 106, "market_freshness/coverage": 59, "coverage": 7} | 23.31 | 0.3092 / 0.2385 (512) | 11.1% | 0.0% | 100.0% | 6.2% |
| ITF_MEN | 19,549 | 25.1% | 17.7% | 32.5% | {"coverage": 1732, "execution": 912, "market_freshness": 889, "data": 720, "market_freshness/coverage": 466, "mapping": 183, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.72 | 0.2167 / 0.1997 (4024) | 37.6% | 69.9% | 16.7% | 21.6% |
| ITF_WOMEN | 25,728 | 26.7% | 19.3% | 45.5% | {"coverage": 2394, "market_freshness": 1452, "execution": 1213, "data": 973, "market_freshness/coverage": 584, "mapping": 156, "model_calibration_or_unknown": 81, "model_calibration": 21} | 12.59 | 0.2036 / 0.1956 (4718) | 39.5% | 57.4% | 10.0% | 21.6% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,922 | 5.7% | 4.9% | 1.5% | {"market_freshness": 76, "model_calibration_or_unknown": 43, "coverage": 30, "execution": 27, "data": 19, "model_calibration": 18, "market_freshness/coverage": 11, "mapping": 1} | 7.48 | 0.2371 / 0.2301 (607) | 26.4% | 1.1% | 1.4% | 3.5% |
| WTA125 | 2,184 | 11.6% | 9.9% | 1.7% | {"market_freshness": 71, "model_calibration_or_unknown": 51, "market_freshness/coverage": 41, "data": 38, "execution": 21, "model_calibration": 15, "coverage": 12, "mapping": 4} | 9.2 | 0.2084 / 0.191 (650) | 25.6% | 11.2% | 4.9% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 16.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 969 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 773 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.5h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 517 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 9 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 10 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.9h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 658 min (STALE); no external reference |
| 13 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 14 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 151 min (STALE); no external reference |
| 17 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 18 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 19 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 20 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 21 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 22 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 23 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 24 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 25 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 26 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 27 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 28 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 29 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 30 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 31 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 32 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 33 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 34 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 35 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 36 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 37 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 38 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 39 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 463 min (STALE); no external reference |
| 40 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 41 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 42 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 43 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 720 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 44 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 45 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 46 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 12.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 768 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 49 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 50 | `KXATPDOUBLES-26OCT29MICVANARROLI-MICVAN` | DOUBLES | gen1_ledger | 98% / 20% | +77 | BOOK_QUALITY | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9701, "by_level_share_of_ge_25pp": {"ATP": 0.015, "CHALLENGER": 0.1086, "DOUBLES": 0.0647, "ITF_MEN": 0.3247, "ITF_WOMEN": 0.4546, "OTHER": 0.0008, "WTA": 0.0149, "WTA125": 0.0167}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5222, "share_primary_cause_market_settled_or_in_play": 0.4321, "share_primary_cause_stale_quote_only": 0.1864}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 15121, "identity_ambiguous_share": 0.2047, "ticker_orientation": {"VERIFIED": 15121}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 9877, "with_external": 518, "coverage": 0.0524, "external_status": {"EXTERNAL_STALE": 319, "AGREES_WITH_KALSHI": 186, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 319, "MODEL_LONE_OUTLIER": 186, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3591, "share_external_supports_model": 0.0251}, "pregame_clean_ge_25pp": {"n": 4694, "with_external": 491, "coverage": 0.1046, "external_status": {"EXTERNAL_STALE": 299, "AGREES_WITH_KALSHI": 179, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 299, "MODEL_LONE_OUTLIER": 179, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3646, "share_external_supports_model": 0.0265}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 471.0, "median_sample_ratio": 2.5, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2105, "data_status": {"POOR": 8582, "LIMITED": 3889, "ADEQUATE": 2650}, "comparison_lt_10pp": {"median_thinner_serve_points": 1667.0, "median_sample_ratio": 1.73, "median_min_matches": 89.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1139, "model_minus_observed": 0.0533, "kalshi_minus_observed": -0.0857, "brier_diff_model_minus_kalshi": -0.0019}, "4-10x": {"n": 790, "model_minus_observed": 0.0857, "kalshi_minus_observed": -0.0605, "brier_diff_model_minus_kalshi": 0.008}, "<2x": {"n": 2734, "model_minus_observed": 0.0895, "kalshi_minus_observed": -0.0338, "brier_diff_model_minus_kalshi": 0.0118}, ">=10x": {"n": 987, "model_minus_observed": 0.1152, "kalshi_minus_observed": -0.0592, "brier_diff_model_minus_kalshi": 0.0131}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 5650, "model": {"intercept": -0.534, "slope": 0.81, "slope_se": 0.034}, "kalshi_mid_same_rows": {"intercept": 0.195, "slope": 1.054, "slope_se": 0.038}, "mean_extremity_model": 0.1715, "mean_extremity_kalshi": 0.1669, "model_brier": 0.2341, "kalshi_brier": 0.2059, "brier_diff_model_minus_kalshi": 0.0282, "brier_diff_se": 0.0025, "model_logloss": 0.6658, "kalshi_logloss": 0.5948}, "fair_v1": {"n": 5650, "model": {"intercept": -0.413, "slope": 1.017, "slope_se": 0.037}, "kalshi_mid_same_rows": {"intercept": 0.283, "slope": 1.092, "slope_se": 0.038}, "mean_extremity_model": 0.1694, "mean_extremity_kalshi": 0.1665, "model_brier": 0.2148, "kalshi_brier": 0.2061, "brier_diff_model_minus_kalshi": 0.0088, "brier_diff_se": 0.0021, "model_logloss": 0.6186, "kalshi_logloss": 0.595}, "gen1_elo": {"n": 5650, "model": {"intercept": -0.391, "slope": 0.993, "slope_se": 0.036}, "kalshi_mid_same_rows": {"intercept": 0.301, "slope": 1.088, "slope_se": 0.038}, "mean_extremity_model": 0.1758, "mean_extremity_kalshi": 0.1667, "model_brier": 0.2138, "kalshi_brier": 0.2062, "brier_diff_model_minus_kalshi": 0.0076, "brier_diff_se": 0.0021, "model_logloss": 0.6169, "kalshi_logloss": 0.5953}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.249, "share_ge_15": 0.444, "median_abs_gap": 13.05, "n": 39661}, "gen1_elo": {"share_ge_25": 0.2471, "share_ge_15": 0.4419, "median_abs_gap": 12.97, "n": 39661}, "gen1_sr": {"share_ge_25": 0.3142, "share_ge_15": 0.5214, "median_abs_gap": 15.91, "n": 39661}, "gen2": {"share_ge_25": 0.317, "share_ge_15": 0.5109, "median_abs_gap": 15.48, "n": 39661}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1532, "share_ge_15": 0.3554, "median_abs_gap": 10.73, "n": 30628}, "gen1_elo": {"share_ge_25": 0.1532, "share_ge_15": 0.3521, "median_abs_gap": 10.54, "n": 30627}, "gen1_sr": {"share_ge_25": 0.218, "share_ge_15": 0.4416, "median_abs_gap": 13.03, "n": 30630}, "gen2": {"share_ge_25": 0.2344, "share_ge_15": 0.4409, "median_abs_gap": 12.92, "n": 30630}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.84, "share_ge_25_all": 0.042, "share_ge_25_pregame_clean": 0.0375}, "WTA": {"median_abs_gap_pregame_clean": 7.48, "share_ge_25_all": 0.0574, "share_ge_25_pregame_clean": 0.0486}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2362, "share_within_10pp_all": 0.4372, "share_within_10pp_pregame_clean": 0.4902, "corr_model_vs_mid_pregame_clean": 0.8506}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 821, "model_brier": 0.1984, "kalshi_brier": 0.1989, "brier_diff_model_minus_kalshi": -0.0005}, "10-15": {"n_settled": 993, "model_brier": 0.2206, "kalshi_brier": 0.2119, "brier_diff_model_minus_kalshi": 0.0087}, "15-25": {"n_settled": 1252, "model_brier": 0.2252, "kalshi_brier": 0.2127, "brier_diff_model_minus_kalshi": 0.0124}, "25-40": {"n_settled": 730, "model_brier": 0.2226, "kalshi_brier": 0.2059, "brier_diff_model_minus_kalshi": 0.0168}, "3-5": {"n_settled": 515, "model_brier": 0.2056, "kalshi_brier": 0.2059, "brier_diff_model_minus_kalshi": -0.0004}, "40+": {"n_settled": 153, "model_brier": 0.2836, "kalshi_brier": 0.1908, "brier_diff_model_minus_kalshi": 0.0928}, "5-10": {"n_settled": 1186, "model_brier": 0.2008, "kalshi_brier": 0.2014, "brier_diff_model_minus_kalshi": -0.0005}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.534, "slope": 0.81, "slope_se": 0.034}, "kalshi_slope": {"intercept": 0.195, "slope": 1.054, "slope_se": 0.038}, "n": 5650}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.489, "slope": 0.855, "slope_se": 0.027}, "kalshi_slope": {"intercept": 0.166, "slope": 1.059, "slope_se": 0.031}, "n": 7803}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 512, "model_brier": 0.3092, "kalshi_brier": 0.2385, "brier_diff_model_minus_kalshi": 0.0707, "brier_diff_se": 0.0132, "corr_model_outcome": 0.0561, "corr_kalshi_outcome": 0.2273}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
