# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-10T12:42Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 85,383): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.2%, 15-25 19.1%, 25-40 13.6%, 40+ 8.2%; median gap 11.83 pp.
* **Where the extremes live**: 97.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.8%, Challenger 11.1%, doubles 6.6%). Main tour: ATP 3.8% and WTA 6.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 18,630): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.3%, STALE_QUOTE 20.1%, BOOK_QUALITY 17.0%, POOR_DATA 9.2%, POSSIBLY_IN_PLAY_QUOTE 5.7%, IDENTITY_AMBIGUOUS 4.3%, IN_PLAY_QUOTE 3.4%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.8%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.3%, market_freshness 20.1%, execution 17.0%, data 12.6%, market_freshness/coverage 9.2%, mapping 4.3%, model_calibration_or_unknown 1.8%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 54.4% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.4% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 18,630 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.0% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.1%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 27.0% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 484.0 points vs 1732.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.025, Gen-2 0.816, Gen-1 ledger 0.866 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 948 model 0.2257 vs Kalshi 0.2051; n 194 model 0.2983 vs Kalshi 0.1732.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 359,639 model-market comparisons (591,140 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 119,346 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-10T12:28:04.055289+00:00'], shadow board 98,347 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-10T12:28:07.386283+00:00'], Model 4 43,559 rows, 29,715 settled tickers, 11,223 tickers with an external scan.
* By model: {"gen1_ledger": 80249, "gen1_elo": 49426, "fair_v1": 49426, "gen2": 49426, "gen1_sr": 49426, "model4_fundamental": 40885, "model4_conditioned": 40801}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 85,383 | 14.1 | 9.6 | 20.2 | 15.2 | 19.1 | 13.6 | 8.2 | 11.83 | 40.9% | 21.8% |
| MW fair_v1 | 49,426 | 12.8 | 8.6 | 18.8 | 15.3 | 19.6 | 14.9 | 10.1 | 13.06 | 44.5% | 25.0% |
| MW gen1_elo | 49,426 | 12.5 | 8.8 | 19.2 | 15.3 | 19.4 | 14.8 | 9.9 | 12.85 | 44.1% | 24.7% |
| MW gen1_ledger | 35,957 | 15.8 | 10.9 | 22.2 | 15.1 | 18.5 | 11.9 | 5.6 | 10.26 | 36.0% | 17.5% |
| MW gen1_sr | 49,426 | 10.0 | 7.2 | 16.7 | 13.9 | 20.8 | 18.7 | 12.7 | 15.85 | 52.1% | 31.4% |
| MW gen2 | 49,426 | 10.9 | 7.6 | 16.7 | 13.7 | 19.6 | 17.7 | 13.7 | 15.46 | 51.1% | 31.5% |
| all families model4_conditioned | 40,801 | 22.2 | 17.9 | 34.4 | 17.0 | 5.0 | 2.2 | 1.2 | 6.07 | 8.4% | 3.4% |
| all families model4_fundamental | 40,885 | 17.3 | 13.5 | 34.0 | 20.0 | 9.9 | 3.8 | 1.5 | 7.61 | 15.2% | 5.3% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.1%, >=15pp 40.9%, >=20pp 30.2%, >=25pp 21.8%, >=30pp 15.8%, >=40pp 8.2%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.42pp; >=10pp 45.1%, >=25pp 17.2%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,064 | 28.1 | 15.7 | 28.0 | 13.3 | 10.7 | 3.6 | 0.6 | 5.84 | 14.9% | 4.2% |
| CHALLENGER | 7,811 | 16.3 | 9.7 | 20.7 | 15.2 | 16.0 | 11.2 | 10.9 | 10.86 | 38.1% | 22.1% |
| ITF_MEN | 14,011 | 9.7 | 7.3 | 17.0 | 15.0 | 21.1 | 17.3 | 12.6 | 15.41 | 51.0% | 29.9% |
| ITF_WOMEN | 19,131 | 9.6 | 7.0 | 16.0 | 14.8 | 22.2 | 18.5 | 12.0 | 15.92 | 52.6% | 30.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,076 | 16.7 | 13.1 | 25.1 | 20.7 | 16.5 | 6.8 | 1.1 | 8.63 | 24.3% | 7.8% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,064 | 26.6 | 15.6 | 26.2 | 15.8 | 11.3 | 3.9 | 0.8 | 6.08 | 15.9% | 4.7% |
| CHALLENGER | 7,811 | 14.4 | 9.2 | 19.1 | 13.8 | 18.6 | 13.4 | 11.4 | 12.48 | 43.5% | 24.9% |
| ITF_MEN | 14,011 | 8.1 | 6.2 | 15.0 | 13.7 | 20.1 | 20.5 | 16.5 | 17.99 | 57.0% | 37.0% |
| ITF_WOMEN | 19,131 | 7.9 | 5.9 | 14.1 | 12.7 | 20.7 | 21.2 | 17.5 | 19.07 | 59.4% | 38.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,076 | 14.0 | 10.3 | 21.7 | 16.2 | 22.4 | 12.8 | 2.5 | 11.21 | 37.7% | 15.3% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,064 | 23.1 | 14.1 | 25.7 | 15.5 | 14.5 | 6.0 | 1.1 | 7.1 | 21.6% | 7.1% |
| CHALLENGER | 7,811 | 15.2 | 9.8 | 20.6 | 15.7 | 16.1 | 11.9 | 10.8 | 11.2 | 38.7% | 22.6% |
| ITF_MEN | 14,011 | 9.4 | 7.3 | 17.1 | 14.2 | 21.7 | 17.3 | 12.9 | 15.75 | 51.9% | 30.2% |
| ITF_WOMEN | 19,131 | 9.3 | 6.9 | 16.3 | 15.7 | 22.1 | 18.4 | 11.3 | 15.59 | 51.8% | 29.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,076 | 22.6 | 17.0 | 31.9 | 15.3 | 8.8 | 3.2 | 1.0 | 6.12 | 13.1% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,444 | 27.9 | 19.5 | 29.3 | 12.3 | 8.0 | 2.6 | 0.5 | 5.27 | 11.0% | 3.0% |
| CHALLENGER | 4,875 | 22.7 | 14.5 | 27.8 | 14.7 | 13.2 | 5.5 | 1.5 | 7.03 | 20.3% | 7.1% |
| DOUBLES | 2,637 | 4.8 | 4.5 | 12.9 | 10.9 | 20.6 | 24.5 | 21.8 | 23.23 | 66.9% | 46.4% |
| ITF_MEN | 10,371 | 12.8 | 9.6 | 21.3 | 15.6 | 21.7 | 13.0 | 6.0 | 11.83 | 40.8% | 19.0% |
| ITF_WOMEN | 12,418 | 13.4 | 9.3 | 19.9 | 15.7 | 21.5 | 14.7 | 5.5 | 12.22 | 41.7% | 20.2% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,807 | 23.8 | 16.1 | 31.5 | 16.9 | 8.9 | 2.5 | 0.2 | 6.56 | 11.7% | 2.8% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,939 | 28.6 | 15.9 | 28.4 | 13.2 | 10.4 | 3.1 | 0.3 | 5.67 | 13.8% | 3.4% |
| CHALLENGER | 5,549 | 20.9 | 12.0 | 25.6 | 17.9 | 16.0 | 5.8 | 1.6 | 8.23 | 23.4% | 7.4% |
| ITF_MEN | 10,259 | 11.9 | 8.6 | 20.5 | 17.2 | 22.1 | 14.3 | 5.5 | 12.5 | 41.8% | 19.8% |
| ITF_WOMEN | 14,063 | 11.4 | 8.5 | 18.9 | 17.0 | 24.0 | 15.3 | 4.8 | 13.16 | 44.1% | 20.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,962 | 17.0 | 13.2 | 25.4 | 21.1 | 16.5 | 6.2 | 0.6 | 8.45 | 23.3% | 6.8% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,939 | 26.9 | 15.9 | 26.5 | 15.7 | 11.2 | 3.4 | 0.4 | 5.99 | 15.0% | 3.8% |
| CHALLENGER | 5,549 | 18.2 | 11.7 | 23.9 | 16.2 | 19.0 | 9.3 | 1.8 | 8.97 | 30.1% | 11.1% |
| ITF_MEN | 10,260 | 9.5 | 7.3 | 17.5 | 15.8 | 22.0 | 18.6 | 9.3 | 14.95 | 49.8% | 27.9% |
| ITF_WOMEN | 14,064 | 8.9 | 6.9 | 15.9 | 14.3 | 22.6 | 20.6 | 10.7 | 16.52 | 53.9% | 31.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,962 | 14.3 | 10.4 | 21.9 | 16.4 | 22.6 | 12.5 | 1.9 | 11.03 | 36.9% | 14.3% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,378 | 28.1 | 19.7 | 29.4 | 12.4 | 7.7 | 2.4 | 0.3 | 5.23 | 10.4% | 2.7% |
| CHALLENGER | 4,320 | 24.0 | 15.4 | 29.0 | 14.8 | 12.6 | 3.8 | 0.4 | 6.58 | 16.9% | 4.3% |
| DOUBLES | 2,471 | 4.7 | 4.5 | 13.1 | 11.0 | 20.4 | 24.4 | 21.9 | 23.2 | 66.7% | 46.3% |
| ITF_MEN | 8,954 | 13.5 | 10.2 | 22.7 | 16.1 | 21.8 | 11.6 | 4.1 | 10.97 | 37.5% | 15.7% |
| ITF_WOMEN | 10,677 | 14.1 | 9.8 | 20.9 | 16.2 | 21.6 | 13.7 | 3.7 | 11.44 | 39.0% | 17.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,744 | 24.1 | 16.5 | 31.5 | 16.9 | 8.9 | 2.0 | 0.1 | 6.43 | 10.9% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,637 | 4.8 | 4.5 | 12.9 | 10.9 | 20.6 | 24.5 | 21.8 | 23.23 | 66.9% | 46.4% |
| singles | 33,320 | 16.7 | 11.4 | 22.9 | 15.4 | 18.3 | 10.9 | 4.3 | 9.73 | 33.6% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 10,293 | 12.8 | 9.0 | 19.7 | 15.4 | 19.7 | 14.0 | 9.4 | 12.65 | 43.1% | 23.4% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 32,272 | 13.3 | 8.7 | 18.9 | 15.1 | 19.1 | 14.8 | 10.1 | 12.9 | 44.0% | 24.9% |
| UNKNOWN | 6,448 | 10.5 | 7.5 | 17.0 | 16.4 | 21.5 | 16.0 | 11.2 | 14.36 | 48.6% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 14,060 | 19.4 | 11.8 | 22.5 | 15.9 | 14.9 | 9.2 | 6.3 | 8.91 | 30.4% | 15.5% |
| B | 6,025 | 12.8 | 8.5 | 19.6 | 15.4 | 19.7 | 12.7 | 11.3 | 12.83 | 43.7% | 23.9% |
| C | 6,986 | 12.1 | 8.8 | 19.6 | 15.6 | 18.7 | 14.6 | 10.7 | 12.89 | 44.0% | 25.3% |
| D | 7,922 | 11.7 | 8.4 | 17.8 | 15.2 | 21.7 | 15.8 | 9.4 | 13.89 | 46.9% | 25.2% |
| F | 14,433 | 7.4 | 5.6 | 14.9 | 14.6 | 23.2 | 21.0 | 13.3 | 17.92 | 57.5% | 34.3% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,645 | 24.8 | 16.1 | 29.0 | 15.0 | 10.5 | 3.4 | 1.2 | 6.34 | 15.2% | 4.6% |
| B | 4,976 | 16.6 | 10.9 | 24.4 | 16.8 | 18.8 | 9.5 | 3.0 | 9.59 | 31.3% | 12.5% |
| C | 7,028 | 10.9 | 7.7 | 19.6 | 14.7 | 21.1 | 15.6 | 10.3 | 13.6 | 47.0% | 25.9% |
| D | 5,350 | 14.4 | 10.1 | 21.2 | 15.3 | 20.9 | 12.7 | 5.4 | 11.26 | 39.0% | 18.1% |
| F | 8,958 | 10.3 | 8.4 | 16.2 | 14.5 | 23.4 | 19.2 | 8.0 | 15.34 | 50.7% | 27.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 15,905 | 17.7 | 10.8 | 21.6 | 15.6 | 15.2 | 10.0 | 9.0 | 9.98 | 34.3% | 19.0% |
| LIMITED | 10,773 | 13.6 | 9.6 | 20.5 | 15.8 | 19.5 | 13.3 | 7.7 | 11.86 | 40.5% | 21.0% |
| POOR | 22,748 | 9.0 | 6.6 | 16.0 | 14.8 | 22.6 | 19.0 | 11.9 | 16.24 | 53.6% | 31.0% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,135 | 23.7 | 18.0 | 33.0 | 15.5 | 6.4 | 3.0 | 0.4 | 5.9 | 9.8% | 3.4% |
| GAME_SPREAD | 6,838 | 22.9 | 15.3 | 32.1 | 16.7 | 9.0 | 3.3 | 0.6 | 6.68 | 12.9% | 4.0% |
| MATCH_WINNER | 35,957 | 15.8 | 10.9 | 22.2 | 15.1 | 18.5 | 11.9 | 5.6 | 10.26 | 36.0% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 16,838 | 28.2 | 16.9 | 30.8 | 12.6 | 8.9 | 2.4 | 0.3 | 5.58 | 11.6% | 2.7% |
| TOTAL_GAMES | 11,457 | 9.8 | 10.8 | 36.0 | 25.8 | 10.5 | 4.2 | 2.9 | 9.15 | 17.5% | 7.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,509 | 24.4 | 28.7 | 33.3 | 8.1 | 4.0 | 1.2 | 0.3 | 4.8 | 5.4% | 1.4% |
| GAME_SPREAD | 9,428 | 46.9 | 15.9 | 25.0 | 7.4 | 2.3 | 1.9 | 0.6 | 3.3 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,864 | 6.6 | 9.8 | 40.6 | 30.0 | 7.3 | 3.3 | 2.4 | 9.17 | 13.0% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,545 | 23.8 | 16.6 | 34.7 | 14.8 | 6.9 | 2.7 | 0.5 | 6.06 | 10.1% | 3.2% |
| GAME_SPREAD | 9,437 | 20.4 | 13.5 | 28.4 | 20.1 | 12.0 | 4.4 | 1.1 | 7.64 | 17.5% | 5.5% |
| TOTAL_GAMES | 16,903 | 10.0 | 10.8 | 36.5 | 24.3 | 11.3 | 4.4 | 2.6 | 9.02 | 18.4% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 49,426 | 44.5% | 25.0% | 13.06 | 35.4% | 15.2% | 10.68 |
| gen1_elo | 49,426 | 44.1% | 24.7% | 12.85 | 34.9% | 14.9% | 10.49 |
| gen1_sr | 49,426 | 52.1% | 31.4% | 15.85 | 43.9% | 21.6% | 12.97 |
| gen2 | 49,426 | 51.1% | 31.5% | 15.46 | 43.9% | 23.1% | 12.84 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,098 | 15.5 | 10.4 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 29,328 | 10.9 | 7.4 | 17.0 | 13.9 | 19.2 | 16.9 | 14.7 | 15.31 | 50.8% | 31.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 29,425 | 16.4 | 11.2 | 22.7 | 15.2 | 18.1 | 11.5 | 5.0 | 9.91 | 34.5% | 16.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 85,383 | 29425 | 23570 | 32388 | 24.9 | 129.7 | 1451.1 |
| ge_15pp | 34,948 | 10149 | 8394 | 16405 | 28.7 | 437.4 | 1451.1 |
| ge_25pp | 18,630 | 4833 | 3666 | 10131 | 34.3 | 582.4 | 1431.1 |
| lt_10pp | 37,442 | 14805 | 11149 | 11488 | 22.7 | 48.7 | 1421.7 |

Current slate `SL-20261110T124201Z-91bc073f`: 598 priced rows, quote age at build {'median': 14.3, 'max': 14.4}, freshness {'AGING': 598}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 51 | 0.0 | 0.0 | 35.3 | 9.8 | 31.4 | 19.6 | 3.9 | 18.34 | 54.9% | 23.5% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,856 | 19.4 | 11.1 | 25.5 | 18.0 | 17.9 | 7.3 | 0.9 | 8.76 | 26.1% | 8.2% |
| KALSHI_LONE_OUTLIER | 32 | 6.2 | 6.2 | 75.0 | 6.2 | 3.1 | 3.1 | 0.0 | 6.16 | 6.2% | 3.1% |
| MARKETS_AGREE | 1,039 | 66.5 | 33.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.16 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,225 | 0.0 | 2.2 | 38.3 | 26.1 | 23.7 | 8.9 | 0.9 | 11.66 | 33.5% | 9.8% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 49,426 | 8232 (16.7%) | 27.0% | 1.0% | {"EXTERNAL_STALE": 4856, "AGREES_WITH_KALSHI": 2225, "ALL_AGREE": 1039, "SUPPORTS_MODEL_DIRECTION": 49, "AGREES_WITH_MODEL": 32, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 22,000 | 2040 (9.3%) | 36.5% | 1.5% | {"EXTERNAL_STALE": 1265, "AGREES_WITH_KALSHI": 745, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 12,335 | 629 (5.1%) | 34.7% | 2.1% | {"EXTERNAL_STALE": 398, "AGREES_WITH_KALSHI": 218, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,774 | 598 (10.4%) | 35.3% | 2.2% | {"EXTERNAL_STALE": 374, "AGREES_WITH_KALSHI": 211, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 19,868 | 4730 (23.8%) | 19.0% | 0.9% | {"EXTERNAL_STALE": 2716, "ALL_AGREE": 1039, "AGREES_WITH_KALSHI": 900, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 28, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 9,665 | 10.7 | 7.7 | 19.2 | 14.4 | 21.5 | 16.3 | 10.1 | 14.14 | 48.0% | 26.5% |
| 4-10x | 6,571 | 11.2 | 8.5 | 18.1 | 15.1 | 21.9 | 14.8 | 10.5 | 13.98 | 47.2% | 25.2% |
| <2x | 25,332 | 14.8 | 9.7 | 19.9 | 16.0 | 17.5 | 13.1 | 9.0 | 11.55 | 39.6% | 22.1% |
| >=10x | 7,858 | 10.3 | 6.4 | 15.0 | 14.4 | 21.7 | 19.0 | 13.2 | 16.47 | 53.9% | 32.2% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 13,011 | 12.5 | 8.6 | 19.8 | 16.1 | 19.1 | 13.5 | 10.4 | 12.71 | 43.0% | 23.9% |
| 300-1000 | 10,574 | 11.8 | 8.8 | 17.7 | 15.0 | 20.8 | 16.4 | 9.6 | 13.76 | 46.7% | 26.0% |
| <300 | 15,560 | 8.2 | 5.8 | 15.1 | 14.7 | 22.9 | 20.0 | 13.3 | 17.24 | 56.2% | 33.3% |
| >=3000 | 10,281 | 21.1 | 12.8 | 24.1 | 15.5 | 13.9 | 7.3 | 5.2 | 7.82 | 26.5% | 12.5% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1510 | 0.55 | 0.4109 | 0.4828 | +0.067 | -0.072 | 0.0033 ± 0.004 |
| ratio 4-10x | 1020 | 0.5775 | 0.4322 | 0.4833 | +0.094 | -0.051 | 0.0109 ± 0.005 |
| ratio <2x | 3702 | 0.5362 | 0.4137 | 0.4368 | +0.099 | -0.023 | 0.0143 ± 0.0023 |
| ratio >=10x | 1253 | 0.5659 | 0.3928 | 0.4429 | +0.123 | -0.050 | 0.0161 ± 0.0051 |
| thinner_sample 1000-3000 | 2077 | 0.5398 | 0.4126 | 0.4468 | +0.093 | -0.034 | 0.0116 ± 0.0032 |
| thinner_sample 300-1000 | 1681 | 0.5662 | 0.4259 | 0.4759 | +0.090 | -0.050 | 0.005 ± 0.0038 |
| thinner_sample <300 | 2422 | 0.558 | 0.3902 | 0.4488 | +0.109 | -0.059 | 0.0151 ± 0.0036 |
| thinner_sample >=3000 | 1305 | 0.5281 | 0.4345 | 0.4437 | +0.084 | -0.009 | 0.0153 ± 0.0032 |
| data_status ADEQUATE | 2089 | 0.5316 | 0.4288 | 0.4385 | +0.093 | -0.010 | 0.0157 ± 0.0027 |
| data_status LIMITED | 1825 | 0.5488 | 0.4158 | 0.4668 | +0.082 | -0.051 | 0.0074 ± 0.0035 |
| data_status POOR | 3571 | 0.5605 | 0.4006 | 0.4553 | +0.105 | -0.055 | 0.012 ± 0.0029 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1081 | 0.1974 | 0.1977 | -0.0003 ± 0.0005 | 0.5747 | 0.5755 | 0.5041 | 0.489 | 0.5023 | -0.093 ± 0.0143 | -0.0087 (8) |
| 3-5 | 685 | 0.2063 | 0.2056 | +0.0006 ± 0.0014 | 0.5974 | 0.5943 | 0.5037 | 0.4639 | 0.4759 | -0.102 ± 0.0179 | 0.01 (3) |
| 5-10 | 1615 | 0.2039 | 0.2023 | +0.0016 ± 0.0017 | 0.5947 | 0.5885 | 0.5121 | 0.4383 | 0.4625 | -0.095 ± 0.0116 | -0.0143 (7) |
| 10-15 | 1303 | 0.2184 | 0.2091 | +0.0093 ± 0.0031 | 0.6286 | 0.6019 | 0.5245 | 0.4011 | 0.4244 | -0.107 ± 0.0129 | -0.055 (6) |
| 15-25 | 1659 | 0.2259 | 0.2075 | +0.0184 ± 0.0044 | 0.6467 | 0.5983 | 0.5754 | 0.3807 | 0.431 | -0.106 ± 0.0112 | -0.0045 (11) |
| 25-40 | 948 | 0.2257 | 0.2051 | +0.0206 ± 0.0088 | 0.642 | 0.591 | 0.6507 | 0.3411 | 0.462 | -0.072 ± 0.0137 | -0.06 (2) |
| 40+ | 194 | 0.2983 | 0.1732 | +0.1251 ± 0.0269 | 0.8017 | 0.5181 | 0.7293 | 0.2739 | 0.3711 | -0.085 ± 0.0259 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5597 | 0.1859 | 0.1868 | -0.0009 ± 0.0002 | 0.5481 | 0.5492 | 0.4915 | 0.4763 | 0.5081 | -0.020 ± 0.0059 | -0.01 (28) |
| 3-5 | 3703 | 0.1988 | 0.1969 | +0.0019 ± 0.0006 | 0.5784 | 0.5718 | 0.4828 | 0.443 | 0.4391 | -0.059 ± 0.0074 | 0.005 (6) |
| 5-10 | 8160 | 0.2013 | 0.1974 | +0.0039 ± 0.0007 | 0.5885 | 0.5758 | 0.4843 | 0.4106 | 0.4213 | -0.048 ± 0.005 | -0.0114 (22) |
| 10-15 | 6679 | 0.2022 | 0.1859 | +0.0162 ± 0.0013 | 0.5911 | 0.5457 | 0.4856 | 0.3617 | 0.3586 | -0.065 ± 0.0053 | -0.0379 (19) |
| 15-25 | 8477 | 0.2066 | 0.1668 | +0.0398 ± 0.0017 | 0.6051 | 0.4958 | 0.4998 | 0.3042 | 0.301 | -0.071 ± 0.0044 | -0.0043 (51) |
| 25-40 | 6606 | 0.224 | 0.1251 | +0.0990 ± 0.0027 | 0.6424 | 0.3852 | 0.5268 | 0.2131 | 0.216 | -0.062 ± 0.0042 | -0.0733 (3) |
| 40+ | 4469 | 0.3813 | 0.0435 | +0.3378 ± 0.0036 | 0.9928 | 0.1693 | 0.6295 | 0.1009 | 0.0573 | -0.075 ± 0.003 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 872 | 0.2056 | 0.2059 | -0.0003 ± 0.0005 | 0.5923 | 0.5933 | 0.507 | 0.4922 | 0.5161 | -0.100 ± 0.0164 | -0.0117 (6) |
| 3-5 | 614 | 0.2119 | 0.2089 | +0.0030 ± 0.0015 | 0.6069 | 0.6004 | 0.5143 | 0.4748 | 0.4528 | -0.133 ± 0.0199 | 0.01 (3) |
| 5-10 | 1383 | 0.2078 | 0.2057 | +0.0021 ± 0.0018 | 0.602 | 0.5964 | 0.5399 | 0.4653 | 0.491 | -0.090 ± 0.0126 | -0.01 (4) |
| 10-15 | 1206 | 0.2138 | 0.2064 | +0.0074 ± 0.0033 | 0.6202 | 0.5984 | 0.5613 | 0.4369 | 0.4718 | -0.105 ± 0.0137 | -0.04 (5) |
| 15-25 | 1748 | 0.2323 | 0.2118 | +0.0205 ± 0.0043 | 0.6607 | 0.6079 | 0.5858 | 0.3902 | 0.4371 | -0.103 ± 0.0113 | -0.0183 (12) |
| 25-40 | 1226 | 0.2689 | 0.1987 | +0.0702 ± 0.008 | 0.749 | 0.5775 | 0.6608 | 0.3468 | 0.394 | -0.120 ± 0.0128 | -0.008 (5) |
| 40+ | 436 | 0.3717 | 0.1624 | +0.2093 ± 0.0193 | 1.0132 | 0.4907 | 0.7362 | 0.2481 | 0.2913 | -0.089 ± 0.0186 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4790 | 0.1917 | 0.1918 | -0.0001 ± 0.0002 | 0.559 | 0.559 | 0.5068 | 0.4917 | 0.5056 | -0.041 ± 0.0065 | -0.0154 (26) |
| 3-5 | 3270 | 0.1933 | 0.1921 | +0.0012 ± 0.0006 | 0.5635 | 0.5598 | 0.5119 | 0.4723 | 0.4765 | -0.048 ± 0.0079 | 0.01 (5) |
| 5-10 | 7245 | 0.1969 | 0.1934 | +0.0034 ± 0.0008 | 0.5787 | 0.5661 | 0.5087 | 0.4345 | 0.4509 | -0.040 ± 0.0052 | -0.0117 (6) |
| 10-15 | 6014 | 0.2031 | 0.1911 | +0.0120 ± 0.0014 | 0.5957 | 0.5591 | 0.5092 | 0.3853 | 0.3997 | -0.050 ± 0.0057 | -0.0189 (18) |
| 15-25 | 8560 | 0.2171 | 0.1804 | +0.0367 ± 0.0018 | 0.6314 | 0.5297 | 0.5252 | 0.3297 | 0.336 | -0.062 ± 0.0046 | -0.014 (52) |
| 25-40 | 7732 | 0.252 | 0.1374 | +0.1146 ± 0.0027 | 0.711 | 0.4197 | 0.5614 | 0.2441 | 0.2257 | -0.081 ± 0.0042 | -0.0095 (20) |
| 40+ | 6080 | 0.4022 | 0.0585 | +0.3438 ± 0.0036 | 1.0592 | 0.211 | 0.6546 | 0.1183 | 0.0794 | -0.074 ± 0.003 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1058 | 0.1953 | 0.1965 | -0.0013 ± 0.0005 | 0.5699 | 0.573 | 0.5025 | 0.4871 | 0.5293 | -0.055 ± 0.0142 | -0.0191 (11) |
| 3-5 | 750 | 0.2073 | 0.2056 | +0.0018 ± 0.0013 | 0.6013 | 0.5953 | 0.4988 | 0.4592 | 0.4587 | -0.115 ± 0.0173 | 0.002 (5) |
| 5-10 | 1633 | 0.2043 | 0.2004 | +0.0039 ± 0.0017 | 0.5944 | 0.5835 | 0.5128 | 0.4391 | 0.4489 | -0.107 ± 0.0114 | -0.01 (10) |
| 10-15 | 1325 | 0.2123 | 0.203 | +0.0093 ± 0.0031 | 0.6148 | 0.5886 | 0.5386 | 0.4154 | 0.4415 | -0.108 ± 0.0125 | -0.0286 (7) |
| 15-25 | 1586 | 0.2312 | 0.2121 | +0.0191 ± 0.0045 | 0.6596 | 0.6084 | 0.5858 | 0.3915 | 0.4395 | -0.108 ± 0.0116 | -0.03 (1) |
| 25-40 | 928 | 0.2155 | 0.2099 | +0.0056 ± 0.0089 | 0.6206 | 0.602 | 0.659 | 0.3483 | 0.4925 | -0.060 ± 0.0138 | -0.0267 (3) |
| 40+ | 205 | 0.3095 | 0.1803 | +0.1292 ± 0.0267 | 0.8367 | 0.5333 | 0.7403 | 0.2852 | 0.3805 | -0.085 ± 0.0273 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5405 | 0.1848 | 0.1853 | -0.0006 ± 0.0002 | 0.5448 | 0.5454 | 0.4851 | 0.4697 | 0.4866 | -0.035 ± 0.0059 | -0.0189 (44) |
| 3-5 | 3850 | 0.204 | 0.2021 | +0.0019 ± 0.0006 | 0.5931 | 0.5867 | 0.4808 | 0.4413 | 0.4379 | -0.058 ± 0.0074 | -0.0073 (22) |
| 5-10 | 8266 | 0.1968 | 0.1913 | +0.0055 ± 0.0007 | 0.5773 | 0.5602 | 0.4877 | 0.4137 | 0.4133 | -0.058 ± 0.0048 | -0.0117 (42) |
| 10-15 | 6659 | 0.1946 | 0.1795 | +0.0151 ± 0.0013 | 0.574 | 0.5307 | 0.496 | 0.3727 | 0.373 | -0.062 ± 0.0052 | -0.0136 (14) |
| 15-25 | 8555 | 0.2122 | 0.1723 | +0.0399 ± 0.0018 | 0.6182 | 0.5084 | 0.5122 | 0.3177 | 0.3133 | -0.072 ± 0.0045 | -0.0533 (3) |
| 25-40 | 6558 | 0.2174 | 0.1251 | +0.0923 ± 0.0027 | 0.6282 | 0.3847 | 0.5279 | 0.2124 | 0.2257 | -0.052 ± 0.0042 | -0.02 (4) |
| 40+ | 4398 | 0.3896 | 0.0482 | +0.3413 ± 0.0038 | 1.0153 | 0.1811 | 0.6383 | 0.1068 | 0.0641 | -0.075 ± 0.0032 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1504 | 0.1971 | 0.197 | +0.0001 ± 0.0004 | 0.5726 | 0.5723 | 0.5094 | 0.4944 | 0.4973 | -0.070 ± 0.0117 | -0.0221 (56) |
| 3-5 | 1072 | 0.1891 | 0.1892 | -0.0001 ± 0.0011 | 0.5564 | 0.555 | 0.4981 | 0.4582 | 0.4776 | -0.055 ± 0.0136 | -0.0194 (34) |
| 5-10 | 2165 | 0.1995 | 0.1945 | +0.0050 ± 0.0014 | 0.5887 | 0.5722 | 0.5079 | 0.4344 | 0.4374 | -0.078 ± 0.0097 | -0.005 (78) |
| 10-15 | 1480 | 0.2151 | 0.2027 | +0.0124 ± 0.0029 | 0.6245 | 0.589 | 0.5418 | 0.419 | 0.4284 | -0.089 ± 0.012 | 0.0012 (66) |
| 15-25 | 1947 | 0.2315 | 0.2077 | +0.0237 ± 0.0041 | 0.6602 | 0.5994 | 0.5918 | 0.397 | 0.435 | -0.091 ± 0.0104 | -0.0214 (59) |
| 25-40 | 1158 | 0.2418 | 0.2109 | +0.0310 ± 0.0082 | 0.6901 | 0.6047 | 0.6892 | 0.377 | 0.4836 | -0.088 ± 0.0127 | -0.0252 (27) |
| 40+ | 420 | 0.3262 | 0.1989 | +0.1273 ± 0.0208 | 0.9377 | 0.5802 | 0.8154 | 0.3394 | 0.4595 | -0.098 ± 0.0194 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5481 | 0.1777 | 0.1778 | -0.0001 ± 0.0002 | 0.5258 | 0.5256 | 0.5122 | 0.497 | 0.5065 | -0.039 ± 0.0057 | -0.0154 (103) |
| 3-5 | 3781 | 0.1952 | 0.1944 | +0.0008 ± 0.0006 | 0.5695 | 0.5671 | 0.5019 | 0.4621 | 0.4724 | -0.040 ± 0.0073 | -0.0212 (73) |
| 5-10 | 7692 | 0.197 | 0.1904 | +0.0066 ± 0.0007 | 0.5813 | 0.5611 | 0.5017 | 0.4282 | 0.4212 | -0.063 ± 0.005 | -0.0084 (134) |
| 10-15 | 5252 | 0.2098 | 0.1932 | +0.0166 ± 0.0015 | 0.6113 | 0.567 | 0.5363 | 0.4134 | 0.4059 | -0.073 ± 0.0061 | -0.0057 (111) |
| 15-25 | 6436 | 0.232 | 0.1999 | +0.0321 ± 0.0022 | 0.6662 | 0.5791 | 0.5766 | 0.3813 | 0.3973 | -0.069 ± 0.0056 | -0.026 (108) |
| 25-40 | 4173 | 0.2583 | 0.1905 | +0.0678 ± 0.0042 | 0.7301 | 0.5545 | 0.6407 | 0.3281 | 0.3789 | -0.066 ± 0.0066 | -0.0277 (53) |
| 40+ | 1875 | 0.3706 | 0.158 | +0.2126 ± 0.0095 | 1.046 | 0.4714 | 0.7446 | 0.2442 | 0.2923 | -0.065 ± 0.0087 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7485 | 1.025 ± 0.032 | 1.099 | 0.168 | 0.1677 | 0.2158 | 0.2039 |
| gen2 | 7485 | 0.816 ± 0.029 | 1.071 | 0.1733 | 0.168 | 0.2341 | 0.2038 |
| gen1_elo | 7485 | 1.009 ± 0.031 | 1.09 | 0.1743 | 0.1678 | 0.2147 | 0.2039 |
| gen1_sr | 7485 | 0.998 ± 0.038 | 1.123 | 0.1332 | 0.1696 | 0.2302 | 0.2035 |
| gen1_ledger | 9746 | 0.866 ± 0.024 | 1.077 | 0.1893 | 0.1751 | 0.2172 | 0.2003 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 34,948)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 8,339 | 23.9% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,937 | 22.7% |
| BOOK_QUALITY | execution | 6,126 | 17.5% |
| POOR_DATA | data | 4,026 | 11.5% |
| LIMITED_DATA | data | 2,141 | 6.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 2,002 | 5.7% |
| IDENTITY_AMBIGUOUS | mapping | 1,451 | 4.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,389 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 972 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 564 | 1.6% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 23.9%, coverage 22.7%, data 17.6%, execution 17.5%, market_freshness/coverage 8.5%, mapping 4.2%, model_calibration_or_unknown 4.0%, model_calibration 1.6%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.8%, LOW_DATA_QUALITY 71.6%, THIN_PLAYER_HISTORY 59.8%, STALE_PLAYER_DATA 52.3%, STALE_KALSHI_QUOTE 46.9%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 23.9%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 15.2%, LEVEL_TRANSFER_RISK 9.8%, LOW_DISPLAYED_LIQUIDITY 8.4%, EVENT_MAPPING_RISK 7.1%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.1%, POST_SETTLEMENT_OBSERVATION 22.7%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 18,630)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,385 | 34.3% |
| STALE_QUOTE | market_freshness | 3,736 | 20.1% |
| BOOK_QUALITY | execution | 3,170 | 17.0% |
| POOR_DATA | data | 1,712 | 9.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,070 | 5.7% |
| IDENTITY_AMBIGUOUS | mapping | 810 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 636 | 3.4% |
| LIMITED_DATA | data | 631 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 341 | 1.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 138 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.3%, market_freshness 20.1%, execution 17.0%, data 12.6%, market_freshness/coverage 9.2%, mapping 4.3%, model_calibration_or_unknown 1.8%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.1%, LOW_DATA_QUALITY 74.8%, THIN_PLAYER_HISTORY 61.9%, STALE_KALSHI_QUOTE 54.4%, STALE_PLAYER_DATA 46.0%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 23.2%, MODEL_HIGH_UNCERTAINTY 19.2%, PLAYER_IDENTITY_RISK 18.2%, EVENT_MAPPING_RISK 8.7%, LEVEL_TRANSFER_RISK 8.6%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 1.8%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.2%, POST_SETTLEMENT_OBSERVATION 34.3%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 14898, "IDENTITY_AMBIGUOUS": 3732}; ticker orientation: {"VERIFIED": 18630}.

Checks: discipline:AMBIGUOUS 1223, discipline:PASS 17407, identity_confidence:AMBIGUOUS 3394, identity_confidence:PASS 15236, level_mapping:NA 1235, level_mapping:PASS 17395, market_pair:AMBIGUOUS 500, market_pair:NA 412, market_pair:PASS 17718, model_complement:NA 374, model_complement:PASS 18256, namesake:AMBIGUOUS 6, namesake:PASS 18624, physical_match_id:NA 6295, physical_match_id:PASS 12335, player_ids:PASS 18630, same_pair_other_event:PASS 18630, ticker_orientation:PASS 18630

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,508 | 3.8% | 3.2% | 1.3% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 24, "market_freshness/coverage": 21, "mapping": 1} | 5.51 | 0.2217 / 0.2172 (841) | 25.4% | 2.4% | 3.1% | 2.9% |
| CHALLENGER | 12,686 | 16.3% | 6.0% | 11.1% | {"coverage": 1239, "market_freshness": 253, "market_freshness/coverage": 232, "data": 164, "model_calibration_or_unknown": 80, "execution": 41, "model_calibration": 39, "mapping": 17, "possible_market_error": 1} | 7.36 | 0.2205 / 0.2096 (2929) | 40.2% | 14.3% | 4.0% | 22.2% |
| DOUBLES | 2,637 | 46.4% | 46.3% | 6.6% | {"execution": 676, "mapping": 363, "market_freshness": 106, "market_freshness/coverage": 71, "coverage": 7} | 23.2 | 0.2993 / 0.2323 (654) | 8.9% | 0.0% | 100.0% | 6.3% |
| ITF_MEN | 24,382 | 25.3% | 17.9% | 33.1% | {"coverage": 2125, "market_freshness": 1270, "execution": 1012, "data": 924, "market_freshness/coverage": 603, "mapping": 218, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.76 | 0.2185 / 0.1996 (5095) | 40.7% | 69.5% | 15.2% | 21.2% |
| ITF_WOMEN | 31,549 | 26.4% | 18.9% | 44.8% | {"coverage": 2935, "market_freshness": 1846, "execution": 1358, "data": 1154, "market_freshness/coverage": 722, "mapping": 205, "model_calibration_or_unknown": 94, "model_calibration": 23} | 12.49 | 0.2035 / 0.1942 (6096) | 41.8% | 57.2% | 9.9% | 21.6% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,883 | 6.0% | 5.1% | 1.6% | {"market_freshness": 111, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.65 | 0.2307 / 0.2205 (804) | 30.2% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.6% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 523 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 17.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 1025 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 628 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 12 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 21.3h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 1282 min (STALE); no external reference |
| 15 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 18 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 17.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1037 min (STALE); no external reference |
| 19 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 20 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 21 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 22 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 23 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 24 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 25 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 454 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 26 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 27 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 28 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 29 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 30 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 31 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 32 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 33 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 34 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 365 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 35 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 36 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 37 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 38 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 39 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 40 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 41 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 43 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 44 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 45 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 46 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 379 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 49 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 50 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 252 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9711, "by_level_share_of_ge_25pp": {"ATP": 0.0132, "CHALLENGER": 0.1109, "DOUBLES": 0.0656, "ITF_MEN": 0.3308, "ITF_WOMEN": 0.4475, "OTHER": 0.0006, "WTA": 0.0156, "WTA125": 0.0157}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5438, "share_primary_cause_market_settled_or_in_play": 0.4342, "share_primary_cause_stale_quote_only": 0.2005}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 18630, "identity_ambiguous_share": 0.2003, "ticker_orientation": {"VERIFIED": 18630}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 12335, "with_external": 629, "coverage": 0.051, "external_status": {"EXTERNAL_STALE": 398, "AGREES_WITH_KALSHI": 218, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 398, "MODEL_LONE_OUTLIER": 218, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3466, "share_external_supports_model": 0.0207}, "pregame_clean_ge_25pp": {"n": 5774, "with_external": 598, "coverage": 0.1036, "external_status": {"EXTERNAL_STALE": 374, "AGREES_WITH_KALSHI": 211, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 374, "MODEL_LONE_OUTLIER": 211, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3528, "share_external_supports_model": 0.0217}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 484.0, "median_sample_ratio": 2.44, "median_min_matches": 18.0, "median_max_days_since_last": 243.0, "share_severe_asymmetry": 0.2083, "data_status": {"POOR": 10492, "LIMITED": 4770, "ADEQUATE": 3368}, "comparison_lt_10pp": {"median_thinner_serve_points": 1732.0, "median_sample_ratio": 1.69, "median_min_matches": 90.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1510, "model_minus_observed": 0.0672, "kalshi_minus_observed": -0.0719, "brier_diff_model_minus_kalshi": 0.0033}, "4-10x": {"n": 1020, "model_minus_observed": 0.0941, "kalshi_minus_observed": -0.0511, "brier_diff_model_minus_kalshi": 0.0109}, "<2x": {"n": 3702, "model_minus_observed": 0.0994, "kalshi_minus_observed": -0.0231, "brier_diff_model_minus_kalshi": 0.0143}, ">=10x": {"n": 1253, "model_minus_observed": 0.123, "kalshi_minus_observed": -0.0501, "brier_diff_model_minus_kalshi": 0.0161}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 7485, "model": {"intercept": -0.561, "slope": 0.816, "slope_se": 0.029}, "kalshi_mid_same_rows": {"intercept": 0.169, "slope": 1.071, "slope_se": 0.033}, "mean_extremity_model": 0.1733, "mean_extremity_kalshi": 0.168, "model_brier": 0.2341, "kalshi_brier": 0.2038, "brier_diff_model_minus_kalshi": 0.0303, "brier_diff_se": 0.0022, "model_logloss": 0.6659, "kalshi_logloss": 0.5901}, "fair_v1": {"n": 7485, "model": {"intercept": -0.458, "slope": 1.025, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.232, "slope": 1.099, "slope_se": 0.033}, "mean_extremity_model": 0.168, "mean_extremity_kalshi": 0.1677, "model_brier": 0.2158, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0119, "brier_diff_se": 0.0018, "model_logloss": 0.6209, "kalshi_logloss": 0.5901}, "gen1_elo": {"n": 7485, "model": {"intercept": -0.446, "slope": 1.009, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.234, "slope": 1.09, "slope_se": 0.033}, "mean_extremity_model": 0.1743, "mean_extremity_kalshi": 0.1678, "model_brier": 0.2147, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0108, "brier_diff_se": 0.0018, "model_logloss": 0.6189, "kalshi_logloss": 0.5903}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2496, "share_ge_15": 0.4451, "median_abs_gap": 13.06, "n": 49426}, "gen1_elo": {"share_ge_25": 0.2467, "share_ge_15": 0.4408, "median_abs_gap": 12.85, "n": 49426}, "gen1_sr": {"share_ge_25": 0.3135, "share_ge_15": 0.521, "median_abs_gap": 15.85, "n": 49426}, "gen2": {"share_ge_25": 0.3146, "share_ge_15": 0.5106, "median_abs_gap": 15.46, "n": 49426}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1517, "share_ge_15": 0.3541, "median_abs_gap": 10.68, "n": 38056}, "gen1_elo": {"share_ge_25": 0.1495, "share_ge_15": 0.3487, "median_abs_gap": 10.49, "n": 38056}, "gen1_sr": {"share_ge_25": 0.2159, "share_ge_15": 0.4392, "median_abs_gap": 12.97, "n": 38058}, "gen2": {"share_ge_25": 0.2312, "share_ge_15": 0.4387, "median_abs_gap": 12.84, "n": 38058}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.51, "share_ge_25_all": 0.0376, "share_ge_25_pregame_clean": 0.0317}, "WTA": {"median_abs_gap_pregame_clean": 7.65, "share_ge_25_all": 0.0596, "share_ge_25_pregame_clean": 0.0506}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2365, "share_within_10pp_all": 0.4385, "share_within_10pp_pregame_clean": 0.4916, "corr_model_vs_mid_pregame_clean": 0.8488}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1081, "model_brier": 0.1974, "kalshi_brier": 0.1977, "brier_diff_model_minus_kalshi": -0.0003}, "10-15": {"n_settled": 1303, "model_brier": 0.2184, "kalshi_brier": 0.2091, "brier_diff_model_minus_kalshi": 0.0093}, "15-25": {"n_settled": 1659, "model_brier": 0.2259, "kalshi_brier": 0.2075, "brier_diff_model_minus_kalshi": 0.0184}, "25-40": {"n_settled": 948, "model_brier": 0.2257, "kalshi_brier": 0.2051, "brier_diff_model_minus_kalshi": 0.0206}, "3-5": {"n_settled": 685, "model_brier": 0.2063, "kalshi_brier": 0.2056, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 194, "model_brier": 0.2983, "kalshi_brier": 0.1732, "brier_diff_model_minus_kalshi": 0.1251}, "5-10": {"n_settled": 1615, "model_brier": 0.2039, "kalshi_brier": 0.2023, "brier_diff_model_minus_kalshi": 0.0016}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.561, "slope": 0.816, "slope_se": 0.029}, "kalshi_slope": {"intercept": 0.169, "slope": 1.071, "slope_se": 0.033}, "n": 7485}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.491, "slope": 0.866, "slope_se": 0.024}, "kalshi_slope": {"intercept": 0.166, "slope": 1.077, "slope_se": 0.028}, "n": 9746}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 654, "model_brier": 0.2993, "kalshi_brier": 0.2323, "brier_diff_model_minus_kalshi": 0.0669, "brier_diff_se": 0.0115, "corr_model_outcome": 0.0995, "corr_kalshi_outcome": 0.2797}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
