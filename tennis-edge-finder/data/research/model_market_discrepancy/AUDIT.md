# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-31T09:10Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 71,087): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 19.0%, 25-40 13.7%, 40+ 8.0%; median gap 11.82 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.9%, Challenger 10.8%, doubles 6.6%). Main tour: ATP 4.0% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 15,470): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.1%, STALE_QUOTE 18.8%, BOOK_QUALITY 18.2%, POOR_DATA 9.4%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IDENTITY_AMBIGUOUS 4.2%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.1%, market_freshness 18.8%, execution 18.2%, data 12.8%, market_freshness/coverage 9.1%, mapping 4.2%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.4% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.2% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 15,470 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.4% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.3% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 479.0 points vs 1723.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.023, Gen-2 0.812, Gen-1 ledger 0.86 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 748 model 0.2233 vs Kalshi 0.2052; n 157 model 0.2855 vs Kalshi 0.1866.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 302,461 model-market comparisons (494,137 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 101,989 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-31T08:58:57.325443+00:00'], shadow board 81,180 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-31T08:59:00.698491+00:00'], Model 4 37,592 rows, 24,539 settled tickers, 9,028 tickers with an external scan.
* By model: {"gen1_ledger": 68775, "gen1_elo": 40800, "fair_v1": 40800, "gen2": 40800, "gen1_sr": 40800, "model4_fundamental": 35265, "model4_conditioned": 35221}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 71,087 | 14.1 | 9.6 | 20.2 | 15.3 | 19.0 | 13.7 | 8.0 | 11.82 | 40.8% | 21.8% |
| MW fair_v1 | 40,800 | 13.0 | 8.7 | 18.8 | 15.3 | 19.4 | 14.8 | 9.9 | 13.0 | 44.2% | 24.8% |
| MW gen1_elo | 40,800 | 12.5 | 8.7 | 19.3 | 15.4 | 19.5 | 14.8 | 9.8 | 12.92 | 44.1% | 24.6% |
| MW gen1_ledger | 30,287 | 15.7 | 10.8 | 22.2 | 15.2 | 18.4 | 12.3 | 5.5 | 10.31 | 36.1% | 17.7% |
| MW gen1_sr | 40,800 | 10.2 | 7.2 | 16.9 | 13.8 | 20.6 | 18.5 | 12.7 | 15.78 | 51.9% | 31.2% |
| MW gen2 | 40,800 | 11.1 | 7.6 | 16.6 | 13.8 | 19.3 | 17.7 | 13.8 | 15.4 | 50.8% | 31.5% |
| all families model4_conditioned | 35,221 | 22.5 | 18.3 | 34.1 | 17.1 | 4.9 | 1.9 | 1.1 | 5.97 | 7.9% | 3.0% |
| all families model4_fundamental | 35,265 | 17.5 | 13.4 | 33.9 | 20.2 | 10.1 | 3.6 | 1.4 | 7.63 | 15.1% | 5.0% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.0%, >=15pp 40.8%, >=20pp 30.1%, >=25pp 21.8%, >=30pp 15.7%, >=40pp 8.0%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.28pp; >=10pp 44.7%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,523 | 27.4 | 15.3 | 28.0 | 13.3 | 11.4 | 3.9 | 0.6 | 5.93 | 15.9% | 4.5% |
| CHALLENGER | 6,022 | 16.3 | 9.7 | 20.8 | 15.1 | 15.3 | 11.7 | 10.9 | 10.91 | 37.9% | 22.6% |
| ITF_MEN | 11,472 | 9.8 | 7.5 | 17.0 | 15.0 | 21.2 | 17.5 | 12.0 | 15.21 | 50.7% | 29.5% |
| ITF_WOMEN | 16,052 | 9.7 | 7.1 | 15.9 | 15.1 | 22.0 | 18.1 | 12.2 | 15.68 | 52.2% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,580 | 18.3 | 13.4 | 25.3 | 20.0 | 15.7 | 6.1 | 1.2 | 8.18 | 23.0% | 7.3% |
| WTA125 | 1,145 | 16.5 | 7.2 | 22.4 | 19.1 | 20.8 | 12.1 | 1.8 | 10.7 | 34.7% | 13.9% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,523 | 26.0 | 15.3 | 26.3 | 15.9 | 11.8 | 4.0 | 0.8 | 6.22 | 16.5% | 4.7% |
| CHALLENGER | 6,022 | 15.2 | 9.1 | 18.2 | 14.2 | 18.1 | 13.4 | 11.8 | 12.49 | 43.3% | 25.2% |
| ITF_MEN | 11,472 | 8.1 | 6.2 | 15.2 | 13.9 | 19.5 | 20.7 | 16.5 | 17.91 | 56.7% | 37.2% |
| ITF_WOMEN | 16,052 | 8.0 | 5.8 | 14.0 | 12.8 | 20.6 | 21.1 | 17.7 | 19.09 | 59.4% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,580 | 15.3 | 11.0 | 22.4 | 15.0 | 21.8 | 12.4 | 2.0 | 10.4 | 36.2% | 14.4% |
| WTA125 | 1,145 | 9.8 | 6.7 | 17.0 | 15.8 | 24.1 | 17.8 | 8.7 | 15.19 | 50.7% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,523 | 22.1 | 13.6 | 24.6 | 15.9 | 16.0 | 6.6 | 1.3 | 7.54 | 23.8% | 7.9% |
| CHALLENGER | 6,022 | 15.0 | 9.3 | 20.9 | 16.1 | 15.6 | 12.1 | 11.1 | 11.34 | 38.7% | 23.2% |
| ITF_MEN | 11,472 | 9.3 | 7.2 | 17.4 | 14.2 | 21.8 | 17.7 | 12.4 | 15.73 | 51.9% | 30.1% |
| ITF_WOMEN | 16,052 | 9.4 | 6.9 | 16.4 | 15.8 | 22.1 | 18.0 | 11.5 | 15.49 | 51.5% | 29.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,580 | 23.3 | 16.4 | 32.2 | 14.5 | 9.4 | 3.1 | 1.2 | 6.12 | 13.7% | 4.3% |
| WTA125 | 1,145 | 21.4 | 13.0 | 27.0 | 17.6 | 14.8 | 5.8 | 0.3 | 7.99 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,099 | 24.9 | 19.3 | 30.8 | 12.9 | 8.9 | 2.8 | 0.5 | 5.66 | 12.2% | 3.3% |
| CHALLENGER | 4,077 | 22.7 | 14.6 | 27.3 | 14.5 | 13.5 | 5.9 | 1.6 | 7.07 | 20.9% | 7.5% |
| DOUBLES | 2,188 | 5.1 | 4.3 | 12.1 | 10.6 | 20.9 | 25.2 | 21.7 | 23.62 | 67.8% | 46.9% |
| ITF_MEN | 8,673 | 13.0 | 9.5 | 21.3 | 15.8 | 21.4 | 13.2 | 5.8 | 11.88 | 40.5% | 19.1% |
| ITF_WOMEN | 10,367 | 13.1 | 9.1 | 20.0 | 15.8 | 21.2 | 15.3 | 5.5 | 12.31 | 42.0% | 20.8% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,574 | 24.3 | 16.1 | 30.4 | 17.1 | 9.0 | 2.9 | 0.2 | 6.55 | 12.1% | 3.2% |
| WTA125 | 1,160 | 25.0 | 12.8 | 21.1 | 19.5 | 13.3 | 6.8 | 1.6 | 7.88 | 21.6% | 8.4% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,424 | 27.7 | 15.5 | 28.4 | 13.3 | 11.2 | 3.6 | 0.3 | 5.9 | 15.1% | 3.9% |
| CHALLENGER | 4,215 | 21.3 | 12.3 | 25.9 | 17.7 | 15.2 | 6.0 | 1.6 | 8.01 | 22.8% | 7.6% |
| ITF_MEN | 8,381 | 12.1 | 8.8 | 20.6 | 17.1 | 22.0 | 14.2 | 5.2 | 12.35 | 41.4% | 19.4% |
| ITF_WOMEN | 11,904 | 11.6 | 8.5 | 18.5 | 17.3 | 24.0 | 15.1 | 5.1 | 13.25 | 44.1% | 20.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,494 | 18.6 | 13.4 | 25.5 | 20.3 | 15.8 | 5.7 | 0.7 | 8.13 | 22.2% | 6.4% |
| WTA125 | 1,106 | 16.7 | 7.1 | 22.0 | 19.4 | 21.2 | 11.8 | 1.6 | 10.79 | 34.7% | 13.5% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,424 | 26.2 | 15.6 | 26.5 | 15.9 | 11.7 | 3.6 | 0.4 | 6.19 | 15.8% | 4.1% |
| CHALLENGER | 4,215 | 19.3 | 11.6 | 22.9 | 16.7 | 18.5 | 9.0 | 1.9 | 8.99 | 29.4% | 10.9% |
| ITF_MEN | 8,382 | 9.5 | 7.4 | 17.6 | 16.1 | 21.3 | 18.7 | 9.4 | 14.86 | 49.5% | 28.2% |
| ITF_WOMEN | 11,905 | 8.9 | 6.8 | 15.9 | 14.3 | 22.8 | 20.6 | 10.8 | 16.54 | 54.1% | 31.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,494 | 15.6 | 11.1 | 22.6 | 15.1 | 22.0 | 12.3 | 1.3 | 10.2 | 35.6% | 13.7% |
| WTA125 | 1,106 | 9.8 | 6.8 | 17.2 | 15.9 | 24.1 | 18.1 | 8.2 | 15.12 | 50.4% | 26.3% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,042 | 25.0 | 19.5 | 30.8 | 13.0 | 8.6 | 2.7 | 0.4 | 5.62 | 11.7% | 3.1% |
| CHALLENGER | 3,595 | 24.2 | 15.5 | 28.5 | 14.6 | 12.8 | 4.0 | 0.5 | 6.58 | 17.2% | 4.4% |
| DOUBLES | 2,051 | 5.0 | 4.4 | 12.3 | 10.8 | 20.7 | 25.1 | 21.6 | 23.56 | 67.4% | 46.7% |
| ITF_MEN | 7,406 | 13.8 | 10.1 | 22.9 | 16.4 | 21.4 | 11.7 | 3.8 | 10.89 | 36.8% | 15.5% |
| ITF_WOMEN | 8,834 | 13.7 | 9.6 | 21.2 | 16.4 | 21.3 | 14.3 | 3.5 | 11.5 | 39.0% | 17.7% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,518 | 24.6 | 16.5 | 30.4 | 17.2 | 9.0 | 2.4 | 0.1 | 6.39 | 11.4% | 2.4% |
| WTA125 | 1,031 | 26.2 | 13.6 | 22.2 | 20.6 | 12.2 | 4.8 | 0.5 | 7.37 | 17.5% | 5.2% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,188 | 5.1 | 4.3 | 12.1 | 10.6 | 20.9 | 25.2 | 21.7 | 23.62 | 67.8% | 46.9% |
| singles | 28,099 | 16.5 | 11.3 | 23.0 | 15.6 | 18.2 | 11.3 | 4.2 | 9.79 | 33.6% | 15.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 8,033 | 13.1 | 9.4 | 20.2 | 15.8 | 18.9 | 13.7 | 8.9 | 12.27 | 41.5% | 22.6% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 26,839 | 13.5 | 8.7 | 18.7 | 15.1 | 19.2 | 14.9 | 10.0 | 12.95 | 44.1% | 24.9% |
| UNKNOWN | 5,679 | 10.4 | 7.8 | 17.1 | 16.3 | 21.3 | 16.1 | 11.1 | 14.27 | 48.5% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 11,397 | 20.1 | 12.0 | 22.6 | 15.6 | 14.7 | 9.0 | 6.1 | 8.51 | 29.8% | 15.1% |
| B | 5,092 | 12.9 | 8.9 | 19.3 | 15.8 | 19.5 | 12.6 | 10.9 | 12.57 | 43.0% | 23.5% |
| C | 5,847 | 11.8 | 8.9 | 19.9 | 15.7 | 18.5 | 14.4 | 10.7 | 12.87 | 43.6% | 25.2% |
| D | 6,446 | 11.8 | 8.4 | 17.6 | 15.3 | 21.6 | 15.9 | 9.4 | 13.84 | 47.0% | 25.4% |
| F | 12,018 | 7.4 | 5.6 | 15.0 | 14.8 | 23.3 | 20.9 | 13.0 | 17.64 | 57.2% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,131 | 24.3 | 15.9 | 29.1 | 15.0 | 10.8 | 3.6 | 1.3 | 6.44 | 15.7% | 4.9% |
| B | 4,333 | 16.8 | 10.7 | 24.1 | 16.9 | 18.7 | 9.7 | 3.1 | 9.67 | 31.5% | 12.8% |
| C | 5,927 | 11.3 | 7.8 | 19.4 | 14.6 | 21.0 | 15.8 | 10.1 | 13.54 | 46.9% | 25.9% |
| D | 4,426 | 14.2 | 9.9 | 21.7 | 15.4 | 20.1 | 13.3 | 5.4 | 11.26 | 38.8% | 18.7% |
| F | 7,470 | 9.9 | 8.3 | 16.0 | 14.9 | 23.2 | 19.8 | 7.7 | 15.41 | 50.8% | 27.5% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 12,893 | 18.3 | 10.9 | 21.7 | 15.4 | 15.1 | 9.8 | 8.9 | 9.71 | 33.7% | 18.7% |
| LIMITED | 9,066 | 13.7 | 10.0 | 20.4 | 16.0 | 19.2 | 13.2 | 7.6 | 11.75 | 39.9% | 20.8% |
| POOR | 18,841 | 9.0 | 6.6 | 16.0 | 15.0 | 22.6 | 19.0 | 11.8 | 16.13 | 53.4% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,907 | 24.3 | 18.2 | 33.2 | 14.9 | 6.4 | 2.6 | 0.4 | 5.82 | 9.4% | 3.0% |
| GAME_SPREAD | 6,052 | 22.4 | 15.2 | 32.8 | 17.1 | 9.1 | 2.9 | 0.6 | 6.73 | 12.6% | 3.5% |
| MATCH_WINNER | 30,287 | 15.7 | 10.8 | 22.2 | 15.2 | 18.4 | 12.3 | 5.5 | 10.31 | 36.1% | 17.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 14,434 | 27.7 | 16.7 | 30.9 | 12.4 | 9.4 | 2.5 | 0.3 | 5.65 | 12.2% | 2.9% |
| TOTAL_GAMES | 10,071 | 10.0 | 10.7 | 35.7 | 26.5 | 10.4 | 4.0 | 2.8 | 9.22 | 17.2% | 6.8% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,551 | 24.5 | 29.9 | 33.0 | 7.4 | 4.0 | 0.9 | 0.2 | 4.71 | 5.1% | 1.1% |
| GAME_SPREAD | 8,206 | 47.5 | 16.1 | 25.1 | 7.2 | 2.2 | 1.3 | 0.6 | 3.25 | 4.1% | 1.9% |
| TOTAL_GAMES | 14,464 | 6.6 | 9.5 | 40.2 | 31.1 | 7.2 | 3.2 | 2.2 | 9.27 | 12.5% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,562 | 24.1 | 16.8 | 34.9 | 14.4 | 7.0 | 2.6 | 0.4 | 6.0 | 10.0% | 3.0% |
| GAME_SPREAD | 8,209 | 20.3 | 13.6 | 28.1 | 20.3 | 12.3 | 4.2 | 1.1 | 7.72 | 17.7% | 5.3% |
| TOTAL_GAMES | 14,494 | 10.2 | 10.3 | 36.3 | 25.1 | 11.5 | 4.2 | 2.4 | 9.15 | 18.1% | 6.6% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 40,800 | 44.2% | 24.8% | 13.0 | 35.3% | 15.2% | 10.66 |
| gen1_elo | 40,800 | 44.1% | 24.6% | 12.92 | 35.1% | 15.2% | 10.53 |
| gen1_sr | 40,800 | 51.9% | 31.2% | 15.78 | 43.9% | 21.6% | 12.96 |
| gen2 | 40,800 | 50.8% | 31.5% | 15.4 | 43.8% | 23.2% | 12.82 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 18,801 | 15.7 | 10.5 | 21.4 | 17.2 | 20.0 | 11.9 | 3.3 | 10.68 | 35.3% | 15.2% |
| STALE | 21,999 | 10.7 | 7.2 | 16.6 | 13.8 | 18.9 | 17.3 | 15.6 | 15.7 | 51.8% | 32.9% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 23,755 | 16.4 | 11.2 | 22.9 | 15.4 | 17.8 | 11.8 | 4.7 | 9.89 | 34.2% | 16.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 71,087 | 23755 | 22273 | 25059 | 24.4 | 124.4 | 1451.1 |
| ge_15pp | 28,966 | 8130 | 7921 | 12915 | 26.9 | 435.3 | 1451.1 |
| ge_25pp | 15,470 | 3905 | 3457 | 8108 | 32.1 | 586.4 | 1431.1 |
| lt_10pp | 31,240 | 11971 | 10573 | 8696 | 22.4 | 46.9 | 1421.1 |

Current slate `SL-20261031T091011Z-15d163c6`: 416 priced rows, quote age at build {'median': 11.6, 'max': 11.6}, freshness {'AGING': 416}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 47 | 0.0 | 0.0 | 34.0 | 6.4 | 34.0 | 21.3 | 4.3 | 19.92 | 59.6% | 25.5% |
| EXTERNAL_LONE_OUTLIER | 25 | 64.0 | 36.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.43 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,061 | 19.8 | 11.0 | 25.6 | 17.9 | 17.8 | 7.1 | 0.9 | 8.56 | 25.9% | 8.1% |
| KALSHI_LONE_OUTLIER | 27 | 3.7 | 3.7 | 77.8 | 7.4 | 3.7 | 3.7 | 0.0 | 6.42 | 7.4% | 3.7% |
| MARKETS_AGREE | 826 | 65.9 | 34.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.2 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,783 | 0.0 | 2.4 | 37.0 | 25.6 | 24.4 | 9.7 | 0.9 | 11.91 | 35.0% | 10.6% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 40,800 | 6769 (16.6%) | 26.3% | 1.1% | {"EXTERNAL_STALE": 4061, "AGREES_WITH_KALSHI": 1783, "ALL_AGREE": 826, "SUPPORTS_MODEL_DIRECTION": 46, "AGREES_WITH_MODEL": 27, "EXTERNAL_OUTLIER": 25, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 18,037 | 1704 (9.4%) | 36.6% | 1.8% | {"EXTERNAL_STALE": 1050, "AGREES_WITH_KALSHI": 624, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 10,103 | 530 (5.2%) | 35.7% | 2.5% | {"EXTERNAL_STALE": 328, "AGREES_WITH_KALSHI": 189, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,788 | 503 (10.5%) | 36.2% | 2.6% | {"EXTERNAL_STALE": 308, "AGREES_WITH_KALSHI": 182, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 16,500 | 3878 (23.5%) | 18.1% | 1.0% | {"EXTERNAL_STALE": 2286, "ALL_AGREE": 826, "AGREES_WITH_KALSHI": 702, "EXTERNAL_OUTLIER": 25, "AGREES_WITH_MODEL": 23, "SUPPORTS_MODEL_DIRECTION": 15, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 7,938 | 10.5 | 7.6 | 19.5 | 14.5 | 21.5 | 16.5 | 9.9 | 14.09 | 47.9% | 26.5% |
| 4-10x | 5,482 | 11.0 | 8.5 | 18.8 | 15.5 | 21.9 | 14.3 | 10.0 | 13.63 | 46.2% | 24.3% |
| <2x | 20,786 | 15.2 | 9.9 | 19.7 | 15.9 | 17.3 | 13.0 | 9.0 | 11.52 | 39.3% | 21.9% |
| >=10x | 6,594 | 10.4 | 6.4 | 15.0 | 14.5 | 21.7 | 19.1 | 12.9 | 16.35 | 53.6% | 32.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 10,649 | 12.8 | 8.9 | 19.7 | 15.8 | 19.0 | 13.3 | 10.4 | 12.64 | 42.7% | 23.7% |
| 300-1000 | 8,780 | 11.9 | 8.7 | 17.8 | 15.3 | 20.3 | 16.4 | 9.6 | 13.59 | 46.2% | 26.0% |
| <300 | 13,002 | 8.2 | 5.8 | 15.1 | 14.8 | 23.0 | 20.0 | 13.0 | 17.07 | 56.0% | 33.0% |
| >=3000 | 8,369 | 21.6 | 12.9 | 24.2 | 15.6 | 13.7 | 7.1 | 5.0 | 7.57 | 25.7% | 12.1% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1174 | 0.5486 | 0.4101 | 0.494 | +0.055 | -0.084 | -0.0017 ± 0.0045 |
| ratio 4-10x | 812 | 0.5814 | 0.4352 | 0.4938 | +0.088 | -0.059 | 0.0083 ± 0.0056 |
| ratio <2x | 2849 | 0.5368 | 0.4143 | 0.4437 | +0.093 | -0.029 | 0.0128 ± 0.0027 |
| ratio >=10x | 1004 | 0.5676 | 0.3929 | 0.4492 | +0.118 | -0.056 | 0.0149 ± 0.0058 |
| thinner_sample 1000-3000 | 1610 | 0.5382 | 0.4118 | 0.4466 | +0.092 | -0.035 | 0.0104 ± 0.0036 |
| thinner_sample 300-1000 | 1325 | 0.5679 | 0.4261 | 0.486 | +0.082 | -0.060 | 0.0027 ± 0.0044 |
| thinner_sample <300 | 1930 | 0.5593 | 0.3917 | 0.458 | +0.101 | -0.066 | 0.012 ± 0.0041 |
| thinner_sample >=3000 | 974 | 0.5307 | 0.4374 | 0.461 | +0.070 | -0.024 | 0.0131 ± 0.0036 |
| data_status ADEQUATE | 1602 | 0.5325 | 0.4303 | 0.4463 | +0.086 | -0.016 | 0.0135 ± 0.003 |
| data_status LIMITED | 1430 | 0.5489 | 0.416 | 0.4699 | +0.079 | -0.054 | 0.0071 ± 0.004 |
| data_status POOR | 2807 | 0.562 | 0.4009 | 0.4663 | +0.096 | -0.065 | 0.0087 ± 0.0033 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 854 | 0.1984 | 0.1987 | -0.0003 ± 0.0005 | 0.5762 | 0.5772 | 0.5035 | 0.4884 | 0.507 | -0.089 ± 0.0162 | -0.01 (5) |
| 3-5 | 535 | 0.2047 | 0.205 | -0.0003 ± 0.0016 | 0.5915 | 0.5911 | 0.5051 | 0.4652 | 0.4879 | -0.097 ± 0.02 | 0.02 (1) |
| 5-10 | 1234 | 0.2014 | 0.2012 | +0.0002 ± 0.0019 | 0.589 | 0.5858 | 0.5097 | 0.4359 | 0.4692 | -0.089 ± 0.0132 | -0.0167 (6) |
| 10-15 | 1019 | 0.22 | 0.2112 | +0.0089 ± 0.0036 | 0.6324 | 0.6073 | 0.5272 | 0.4035 | 0.4279 | -0.109 ± 0.0145 | -0.048 (5) |
| 15-25 | 1292 | 0.2254 | 0.2112 | +0.0142 ± 0.005 | 0.6465 | 0.6062 | 0.5756 | 0.3804 | 0.442 | -0.102 ± 0.0128 | -0.0033 (9) |
| 25-40 | 748 | 0.2233 | 0.2052 | +0.0180 ± 0.0099 | 0.6365 | 0.5923 | 0.6545 | 0.3444 | 0.4706 | -0.077 ± 0.0152 | -0.01 (1) |
| 40+ | 157 | 0.2855 | 0.1866 | +0.0989 ± 0.0302 | 0.7765 | 0.5515 | 0.7369 | 0.2888 | 0.4076 | -0.078 ± 0.0298 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4660 | 0.184 | 0.1849 | -0.0009 ± 0.0002 | 0.5426 | 0.5438 | 0.4867 | 0.4715 | 0.5017 | -0.023 ± 0.0064 | -0.0129 (17) |
| 3-5 | 3142 | 0.1945 | 0.1927 | +0.0018 ± 0.0006 | 0.5677 | 0.5611 | 0.483 | 0.4432 | 0.4395 | -0.058 ± 0.0079 | 0.0 (2) |
| 5-10 | 6689 | 0.2019 | 0.198 | +0.0039 ± 0.0008 | 0.5897 | 0.5772 | 0.4852 | 0.4117 | 0.4234 | -0.048 ± 0.0055 | -0.0119 (21) |
| 10-15 | 5549 | 0.2015 | 0.1855 | +0.0160 ± 0.0014 | 0.5891 | 0.5453 | 0.4841 | 0.3601 | 0.3566 | -0.067 ± 0.0058 | -0.0281 (16) |
| 15-25 | 6954 | 0.2066 | 0.1675 | +0.0391 ± 0.0019 | 0.6059 | 0.4972 | 0.4989 | 0.3032 | 0.3021 | -0.071 ± 0.0049 | -0.0025 (44) |
| 25-40 | 5420 | 0.2217 | 0.1247 | +0.0969 ± 0.003 | 0.6375 | 0.3843 | 0.5254 | 0.2113 | 0.2181 | -0.060 ± 0.0047 | -0.01 (1) |
| 40+ | 3601 | 0.384 | 0.0443 | +0.3397 ± 0.004 | 1.0004 | 0.172 | 0.6326 | 0.1037 | 0.0592 | -0.078 ± 0.0033 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 676 | 0.2051 | 0.2057 | -0.0006 ± 0.0006 | 0.5914 | 0.5931 | 0.5094 | 0.4945 | 0.5237 | -0.101 ± 0.0189 | -0.01 (3) |
| 3-5 | 482 | 0.2177 | 0.2155 | +0.0022 ± 0.0017 | 0.619 | 0.6147 | 0.515 | 0.4754 | 0.4627 | -0.122 ± 0.0225 | 0.02 (1) |
| 5-10 | 1076 | 0.2074 | 0.206 | +0.0014 ± 0.0021 | 0.6012 | 0.5967 | 0.5409 | 0.4661 | 0.4963 | -0.091 ± 0.0143 | -0.01 (4) |
| 10-15 | 946 | 0.2159 | 0.21 | +0.0058 ± 0.0037 | 0.6226 | 0.607 | 0.5636 | 0.4392 | 0.481 | -0.104 ± 0.0155 | -0.04 (5) |
| 15-25 | 1356 | 0.2299 | 0.2128 | +0.0170 ± 0.0049 | 0.6544 | 0.6097 | 0.5825 | 0.3871 | 0.4432 | -0.098 ± 0.0128 | -0.0133 (9) |
| 25-40 | 949 | 0.2683 | 0.1974 | +0.0709 ± 0.009 | 0.7491 | 0.5752 | 0.6592 | 0.3451 | 0.392 | -0.132 ± 0.0144 | -0.0075 (4) |
| 40+ | 354 | 0.3652 | 0.1649 | +0.2002 ± 0.0214 | 0.999 | 0.4971 | 0.7319 | 0.2469 | 0.2966 | -0.084 ± 0.0209 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4004 | 0.1901 | 0.1904 | -0.0002 ± 0.0002 | 0.5554 | 0.5557 | 0.5084 | 0.4934 | 0.5095 | -0.040 ± 0.0071 | -0.0133 (15) |
| 3-5 | 2732 | 0.1941 | 0.1931 | +0.0011 ± 0.0007 | 0.5644 | 0.5611 | 0.5114 | 0.4718 | 0.4766 | -0.047 ± 0.0086 | 0.02 (1) |
| 5-10 | 5975 | 0.1983 | 0.1949 | +0.0034 ± 0.0009 | 0.582 | 0.5694 | 0.5096 | 0.4355 | 0.4526 | -0.042 ± 0.0058 | -0.0117 (6) |
| 10-15 | 4988 | 0.2039 | 0.1919 | +0.0120 ± 0.0016 | 0.5971 | 0.5612 | 0.511 | 0.3872 | 0.4016 | -0.052 ± 0.0063 | -0.0189 (18) |
| 15-25 | 6952 | 0.2171 | 0.1802 | +0.0369 ± 0.002 | 0.6314 | 0.5293 | 0.5222 | 0.327 | 0.3331 | -0.064 ± 0.0051 | -0.0086 (42) |
| 25-40 | 6355 | 0.2512 | 0.1355 | +0.1157 ± 0.0029 | 0.7089 | 0.4156 | 0.5576 | 0.2409 | 0.2201 | -0.086 ± 0.0046 | -0.0044 (18) |
| 40+ | 5009 | 0.399 | 0.0585 | +0.3404 ± 0.004 | 1.0528 | 0.2111 | 0.6529 | 0.1177 | 0.0811 | -0.073 ± 0.0034 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 808 | 0.1946 | 0.1968 | -0.0022 ± 0.0005 | 0.5677 | 0.5734 | 0.5013 | 0.486 | 0.5483 | -0.036 ± 0.0163 | -0.0137 (8) |
| 3-5 | 575 | 0.2039 | 0.2018 | +0.0020 ± 0.0015 | 0.5903 | 0.5838 | 0.4964 | 0.4568 | 0.4522 | -0.122 ± 0.0194 | 0.0067 (3) |
| 5-10 | 1284 | 0.2032 | 0.2007 | +0.0024 ± 0.0019 | 0.5919 | 0.5841 | 0.5106 | 0.437 | 0.4556 | -0.100 ± 0.0129 | -0.0071 (7) |
| 10-15 | 1019 | 0.2085 | 0.2034 | +0.0051 ± 0.0035 | 0.6068 | 0.5901 | 0.5391 | 0.4158 | 0.4583 | -0.097 ± 0.0141 | -0.0317 (6) |
| 15-25 | 1223 | 0.2351 | 0.2169 | +0.0182 ± 0.0052 | 0.6695 | 0.6188 | 0.5881 | 0.3939 | 0.444 | -0.113 ± 0.0133 | -0.03 (1) |
| 25-40 | 764 | 0.213 | 0.2118 | +0.0013 ± 0.0098 | 0.6146 | 0.6074 | 0.6619 | 0.3516 | 0.5026 | -0.060 ± 0.015 | 0.015 (2) |
| 40+ | 166 | 0.3035 | 0.1944 | +0.1091 ± 0.0302 | 0.8261 | 0.5695 | 0.7484 | 0.2986 | 0.4096 | -0.084 ± 0.0315 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4457 | 0.1832 | 0.1839 | -0.0007 ± 0.0002 | 0.5398 | 0.5411 | 0.4824 | 0.4671 | 0.4882 | -0.030 ± 0.0065 | -0.0163 (35) |
| 3-5 | 3116 | 0.2013 | 0.1991 | +0.0022 ± 0.0006 | 0.5856 | 0.5784 | 0.4809 | 0.4415 | 0.4336 | -0.064 ± 0.0081 | -0.0094 (18) |
| 5-10 | 6869 | 0.1939 | 0.1897 | +0.0043 ± 0.0008 | 0.5709 | 0.5567 | 0.4865 | 0.4125 | 0.4209 | -0.050 ± 0.0053 | -0.01 (31) |
| 10-15 | 5513 | 0.1921 | 0.1787 | +0.0134 ± 0.0014 | 0.5684 | 0.5294 | 0.4945 | 0.3712 | 0.378 | -0.057 ± 0.0057 | -0.015 (12) |
| 15-25 | 7070 | 0.2138 | 0.173 | +0.0408 ± 0.0019 | 0.6222 | 0.5095 | 0.5125 | 0.318 | 0.3119 | -0.075 ± 0.0049 | -0.03 (2) |
| 25-40 | 5420 | 0.2163 | 0.128 | +0.0883 ± 0.0031 | 0.6258 | 0.3919 | 0.5289 | 0.2134 | 0.2334 | -0.049 ± 0.0047 | 0.01 (3) |
| 40+ | 3570 | 0.3938 | 0.0498 | +0.3440 ± 0.0042 | 1.0269 | 0.1862 | 0.642 | 0.1104 | 0.0658 | -0.079 ± 0.0036 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1222 | 0.1946 | 0.1947 | -0.0001 ± 0.0004 | 0.5674 | 0.5674 | 0.5056 | 0.4905 | 0.4959 | -0.068 ± 0.0129 | -0.0224 (49) |
| 3-5 | 864 | 0.1866 | 0.1859 | +0.0007 ± 0.0012 | 0.5476 | 0.5452 | 0.4972 | 0.4574 | 0.4664 | -0.066 ± 0.015 | -0.0194 (34) |
| 5-10 | 1801 | 0.2014 | 0.1968 | +0.0047 ± 0.0016 | 0.5915 | 0.5768 | 0.5023 | 0.4285 | 0.4342 | -0.076 ± 0.0107 | -0.005 (78) |
| 10-15 | 1229 | 0.2164 | 0.2034 | +0.0130 ± 0.0032 | 0.6253 | 0.5908 | 0.5386 | 0.4158 | 0.4223 | -0.090 ± 0.0132 | 0.0014 (64) |
| 15-25 | 1576 | 0.2323 | 0.2103 | +0.0220 ± 0.0045 | 0.6617 | 0.6053 | 0.5835 | 0.3887 | 0.4327 | -0.086 ± 0.0117 | -0.0214 (59) |
| 25-40 | 985 | 0.2435 | 0.2105 | +0.0329 ± 0.009 | 0.696 | 0.6036 | 0.6843 | 0.3722 | 0.4761 | -0.094 ± 0.0137 | -0.0219 (26) |
| 40+ | 331 | 0.3371 | 0.2029 | +0.1342 ± 0.0239 | 0.9782 | 0.5911 | 0.8165 | 0.3401 | 0.4532 | -0.103 ± 0.0225 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4602 | 0.175 | 0.1752 | -0.0002 ± 0.0002 | 0.5192 | 0.5193 | 0.5104 | 0.4951 | 0.5078 | -0.037 ± 0.0062 | -0.0157 (88) |
| 3-5 | 3158 | 0.1926 | 0.1913 | +0.0013 ± 0.0006 | 0.5616 | 0.5589 | 0.5033 | 0.4636 | 0.4671 | -0.048 ± 0.0079 | -0.0209 (69) |
| 5-10 | 6506 | 0.1986 | 0.192 | +0.0066 ± 0.0008 | 0.5836 | 0.5644 | 0.4986 | 0.4249 | 0.4187 | -0.064 ± 0.0055 | -0.0082 (132) |
| 10-15 | 4498 | 0.2106 | 0.1942 | +0.0164 ± 0.0016 | 0.6118 | 0.5693 | 0.5365 | 0.4136 | 0.4071 | -0.072 ± 0.0066 | -0.0053 (105) |
| 15-25 | 5411 | 0.2309 | 0.2006 | +0.0303 ± 0.0024 | 0.6638 | 0.5806 | 0.5708 | 0.3755 | 0.397 | -0.066 ± 0.0061 | -0.0253 (107) |
| 25-40 | 3642 | 0.2599 | 0.1879 | +0.0719 ± 0.0045 | 0.7352 | 0.5485 | 0.6362 | 0.3237 | 0.3677 | -0.076 ± 0.007 | -0.0229 (51) |
| 40+ | 1561 | 0.3754 | 0.1564 | +0.2190 ± 0.0104 | 1.0635 | 0.4661 | 0.742 | 0.24 | 0.2832 | -0.070 ± 0.0095 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5839 | 1.023 ± 0.036 | 1.1 | 0.1689 | 0.1666 | 0.2149 | 0.2053 |
| gen2 | 5839 | 0.812 ± 0.033 | 1.068 | 0.1713 | 0.167 | 0.234 | 0.2051 |
| gen1_elo | 5839 | 1.0 ± 0.035 | 1.096 | 0.1756 | 0.1667 | 0.2138 | 0.2054 |
| gen1_sr | 5839 | 0.998 ± 0.044 | 1.126 | 0.1315 | 0.1689 | 0.2301 | 0.2048 |
| gen1_ledger | 8008 | 0.86 ± 0.026 | 1.066 | 0.1878 | 0.1758 | 0.2179 | 0.2009 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 28,966)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,532 | 22.6% |
| STALE_QUOTE | market_freshness | 6,391 | 22.1% |
| BOOK_QUALITY | execution | 5,414 | 18.7% |
| POOR_DATA | data | 3,384 | 11.7% |
| LIMITED_DATA | data | 1,816 | 6.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,659 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,240 | 4.3% |
| IDENTITY_AMBIGUOUS | mapping | 1,196 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 838 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 495 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.6%, market_freshness 22.1%, execution 18.7%, data 17.9%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.3%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.4%, START_UNVERIFIABLE 94.5%, LOW_DATA_QUALITY 71.6%, THIN_PLAYER_HISTORY 60.0%, STALE_PLAYER_DATA 52.2%, STALE_KALSHI_QUOTE 44.6%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 33.3%, WIDE_SPREAD 24.7%, MODEL_HIGH_UNCERTAINTY 18.3%, PLAYER_IDENTITY_RISK 15.6%, LEVEL_TRANSFER_RISK 10.5%, LOW_DISPLAYED_LIQUIDITY 8.1%, EVENT_MAPPING_RISK 7.5%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.4%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.0%, POST_SETTLEMENT_OBSERVATION 22.6%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 15,470)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,278 | 34.1% |
| STALE_QUOTE | market_freshness | 2,902 | 18.8% |
| BOOK_QUALITY | execution | 2,817 | 18.2% |
| POOR_DATA | data | 1,450 | 9.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 870 | 5.6% |
| IDENTITY_AMBIGUOUS | mapping | 644 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 543 | 3.5% |
| LIMITED_DATA | data | 534 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 307 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 124 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.1%, market_freshness 18.8%, execution 18.2%, data 12.8%, market_freshness/coverage 9.1%, mapping 4.2%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 75.0%, THIN_PLAYER_HISTORY 62.3%, STALE_KALSHI_QUOTE 52.4%, STALE_PLAYER_DATA 46.2%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 24.2%, MODEL_HIGH_UNCERTAINTY 19.0%, PLAYER_IDENTITY_RISK 18.4%, LEVEL_TRANSFER_RISK 9.3%, EVENT_MAPPING_RISK 9.0%, LOW_DISPLAYED_LIQUIDITY 8.0%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.2%, POST_SETTLEMENT_OBSERVATION 34.1%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 12306, "IDENTITY_AMBIGUOUS": 3164}; ticker orientation: {"VERIFIED": 15470}.

Checks: discipline:AMBIGUOUS 1026, discipline:PASS 14444, identity_confidence:AMBIGUOUS 2841, identity_confidence:PASS 12629, level_mapping:NA 1038, level_mapping:PASS 14432, market_pair:AMBIGUOUS 482, market_pair:NA 352, market_pair:PASS 14636, model_complement:NA 315, model_complement:PASS 15155, namesake:AMBIGUOUS 6, namesake:PASS 15464, physical_match_id:NA 5367, physical_match_id:PASS 10103, player_ids:PASS 15470, same_pair_other_event:PASS 15470, ticker_orientation:PASS 15470

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,622 | 4.0% | 3.6% | 1.5% | {"market_freshness": 56, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 17, "coverage": 13} | 5.81 | 0.22 / 0.2151 (651) | 22.1% | 2.8% | 3.1% | 2.8% |
| CHALLENGER | 10,099 | 16.5% | 6.2% | 10.8% | {"coverage": 986, "market_freshness/coverage": 199, "market_freshness": 173, "data": 144, "model_calibration_or_unknown": 74, "execution": 37, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.24 | 0.221 / 0.2116 (2313) | 35.7% | 15.5% | 4.1% | 22.7% |
| DOUBLES | 2,188 | 46.9% | 46.7% | 6.6% | {"execution": 572, "mapping": 280, "market_freshness": 106, "market_freshness/coverage": 61, "coverage": 7} | 23.56 | 0.3064 / 0.2392 (529) | 10.7% | 0.0% | 100.0% | 6.3% |
| ITF_MEN | 20,145 | 25.0% | 17.5% | 32.5% | {"coverage": 1782, "market_freshness": 923, "execution": 915, "data": 739, "market_freshness/coverage": 484, "mapping": 183, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.68 | 0.2164 / 0.1994 (4137) | 38.1% | 69.1% | 16.3% | 21.6% |
| ITF_WOMEN | 26,419 | 26.5% | 19.1% | 45.3% | {"coverage": 2447, "market_freshness": 1487, "execution": 1215, "data": 1002, "market_freshness/coverage": 599, "mapping": 158, "model_calibration_or_unknown": 82, "model_calibration": 21} | 12.53 | 0.2037 / 0.1946 (4852) | 39.8% | 57.0% | 9.9% | 21.5% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,154 | 5.7% | 4.9% | 1.5% | {"market_freshness": 82, "model_calibration_or_unknown": 43, "coverage": 30, "execution": 28, "data": 25, "model_calibration": 18, "market_freshness/coverage": 11, "mapping": 1} | 7.39 | 0.2323 / 0.2255 (641) | 27.1% | 1.7% | 1.4% | 3.4% |
| WTA125 | 2,305 | 11.1% | 9.5% | 1.7% | {"market_freshness": 73, "model_calibration_or_unknown": 51, "market_freshness/coverage": 41, "data": 38, "execution": 21, "model_calibration": 16, "coverage": 12, "mapping": 4} | 9.14 | 0.2123 / 0.1926 (682) | 26.6% | 10.6% | 4.6% | 7.3% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 17.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 1025 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 172 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 164 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 9 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 10 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 547 min (STALE); no external reference |
| 13 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
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
| 26 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 27 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 28 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 29 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 30 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 31 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 32 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 33 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 34 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 35 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 36 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 37 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 38 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 39 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 463 min (STALE); no external reference |
| 40 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 41 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 42 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 43 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 720 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 44 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 45 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.3h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 748 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |
| 46 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 47 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 48 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 49 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 50 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9699, "by_level_share_of_ge_25pp": {"ATP": 0.0147, "CHALLENGER": 0.1077, "DOUBLES": 0.0663, "ITF_MEN": 0.3254, "ITF_WOMEN": 0.4532, "OTHER": 0.0008, "WTA": 0.0154, "WTA125": 0.0165}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5241, "share_primary_cause_market_settled_or_in_play": 0.4325, "share_primary_cause_stale_quote_only": 0.1876}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 15470, "identity_ambiguous_share": 0.2045, "ticker_orientation": {"VERIFIED": 15470}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 10103, "with_external": 530, "coverage": 0.0525, "external_status": {"EXTERNAL_STALE": 328, "AGREES_WITH_KALSHI": 189, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 328, "MODEL_LONE_OUTLIER": 189, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3566, "share_external_supports_model": 0.0245}, "pregame_clean_ge_25pp": {"n": 4788, "with_external": 503, "coverage": 0.1051, "external_status": {"EXTERNAL_STALE": 308, "AGREES_WITH_KALSHI": 182, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 308, "MODEL_LONE_OUTLIER": 182, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3618, "share_external_supports_model": 0.0258}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 479.0, "median_sample_ratio": 2.48, "median_min_matches": 19.0, "median_max_days_since_last": 237.0, "share_severe_asymmetry": 0.2092, "data_status": {"POOR": 8730, "LIMITED": 4027, "ADEQUATE": 2713}, "comparison_lt_10pp": {"median_thinner_serve_points": 1723.0, "median_sample_ratio": 1.7, "median_min_matches": 91.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1174, "model_minus_observed": 0.0546, "kalshi_minus_observed": -0.084, "brier_diff_model_minus_kalshi": -0.0017}, "4-10x": {"n": 812, "model_minus_observed": 0.0876, "kalshi_minus_observed": -0.0586, "brier_diff_model_minus_kalshi": 0.0083}, "<2x": {"n": 2849, "model_minus_observed": 0.0931, "kalshi_minus_observed": -0.0294, "brier_diff_model_minus_kalshi": 0.0128}, ">=10x": {"n": 1004, "model_minus_observed": 0.1184, "kalshi_minus_observed": -0.0563, "brier_diff_model_minus_kalshi": 0.0149}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 5839, "model": {"intercept": -0.536, "slope": 0.812, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.195, "slope": 1.068, "slope_se": 0.037}, "mean_extremity_model": 0.1713, "mean_extremity_kalshi": 0.167, "model_brier": 0.234, "kalshi_brier": 0.2051, "brier_diff_model_minus_kalshi": 0.0289, "brier_diff_se": 0.0025, "model_logloss": 0.6655, "kalshi_logloss": 0.5929}, "fair_v1": {"n": 5839, "model": {"intercept": -0.427, "slope": 1.023, "slope_se": 0.036}, "kalshi_mid_same_rows": {"intercept": 0.27, "slope": 1.1, "slope_se": 0.038}, "mean_extremity_model": 0.1689, "mean_extremity_kalshi": 0.1666, "model_brier": 0.2149, "kalshi_brier": 0.2053, "brier_diff_model_minus_kalshi": 0.0096, "brier_diff_se": 0.002, "model_logloss": 0.6188, "kalshi_logloss": 0.5932}, "gen1_elo": {"n": 5839, "model": {"intercept": -0.404, "slope": 1.0, "slope_se": 0.035}, "kalshi_mid_same_rows": {"intercept": 0.288, "slope": 1.096, "slope_se": 0.037}, "mean_extremity_model": 0.1756, "mean_extremity_kalshi": 0.1667, "model_brier": 0.2138, "kalshi_brier": 0.2054, "brier_diff_model_minus_kalshi": 0.0084, "brier_diff_se": 0.002, "model_logloss": 0.6169, "kalshi_logloss": 0.5935}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2476, "share_ge_15": 0.4421, "median_abs_gap": 13.0, "n": 40800}, "gen1_elo": {"share_ge_25": 0.2458, "share_ge_15": 0.4409, "median_abs_gap": 12.92, "n": 40800}, "gen1_sr": {"share_ge_25": 0.3125, "share_ge_15": 0.5188, "median_abs_gap": 15.78, "n": 40800}, "gen2": {"share_ge_25": 0.3151, "share_ge_15": 0.5085, "median_abs_gap": 15.4, "n": 40800}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1518, "share_ge_15": 0.3534, "median_abs_gap": 10.66, "n": 31530}, "gen1_elo": {"share_ge_25": 0.1516, "share_ge_15": 0.3512, "median_abs_gap": 10.53, "n": 31529}, "gen1_sr": {"share_ge_25": 0.2162, "share_ge_15": 0.4385, "median_abs_gap": 12.96, "n": 31532}, "gen2": {"share_ge_25": 0.2322, "share_ge_15": 0.4381, "median_abs_gap": 12.82, "n": 31532}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.81, "share_ge_25_all": 0.0404, "share_ge_25_pregame_clean": 0.036}, "WTA": {"median_abs_gap_pregame_clean": 7.39, "share_ge_25_all": 0.0573, "share_ge_25_pregame_clean": 0.0491}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2372, "share_within_10pp_all": 0.4395, "share_within_10pp_pregame_clean": 0.4923, "corr_model_vs_mid_pregame_clean": 0.8506}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 854, "model_brier": 0.1984, "kalshi_brier": 0.1987, "brier_diff_model_minus_kalshi": -0.0003}, "10-15": {"n_settled": 1019, "model_brier": 0.22, "kalshi_brier": 0.2112, "brier_diff_model_minus_kalshi": 0.0089}, "15-25": {"n_settled": 1292, "model_brier": 0.2254, "kalshi_brier": 0.2112, "brier_diff_model_minus_kalshi": 0.0142}, "25-40": {"n_settled": 748, "model_brier": 0.2233, "kalshi_brier": 0.2052, "brier_diff_model_minus_kalshi": 0.018}, "3-5": {"n_settled": 535, "model_brier": 0.2047, "kalshi_brier": 0.205, "brier_diff_model_minus_kalshi": -0.0003}, "40+": {"n_settled": 157, "model_brier": 0.2855, "kalshi_brier": 0.1866, "brier_diff_model_minus_kalshi": 0.0989}, "5-10": {"n_settled": 1234, "model_brier": 0.2014, "kalshi_brier": 0.2012, "brier_diff_model_minus_kalshi": 0.0002}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.536, "slope": 0.812, "slope_se": 0.033}, "kalshi_slope": {"intercept": 0.195, "slope": 1.068, "slope_se": 0.037}, "n": 5839}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.491, "slope": 0.86, "slope_se": 0.026}, "kalshi_slope": {"intercept": 0.165, "slope": 1.066, "slope_se": 0.031}, "n": 8008}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 529, "model_brier": 0.3064, "kalshi_brier": 0.2392, "brier_diff_model_minus_kalshi": 0.0672, "brier_diff_se": 0.013, "corr_model_outcome": 0.0585, "corr_kalshi_outcome": 0.2248}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
