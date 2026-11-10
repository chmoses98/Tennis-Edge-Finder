# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-10T21:23Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 87,686): 0-3 14.0%, 3-5 9.5%, 5-10 20.2%, 10-15 15.2%, 15-25 19.1%, 25-40 13.7%, 40+ 8.2%; median gap 11.88 pp.
* **Where the extremes live**: 97.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 78.0%, Challenger 11.2%, doubles 6.5%). Main tour: ATP 3.7% and WTA 5.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 19,266): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.7%, STALE_QUOTE 20.2%, BOOK_QUALITY 16.7%, POOR_DATA 9.2%, POSSIBLY_IN_PLAY_QUOTE 5.7%, IDENTITY_AMBIGUOUS 4.3%, IN_PLAY_QUOTE 3.4%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.8%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.7%, market_freshness 20.2%, execution 16.7%, data 12.5%, market_freshness/coverage 9.1%, mapping 4.3%, model_calibration_or_unknown 1.8%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 55.0% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 19,266 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.9% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.9%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 27.3% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 479.0 points vs 1713.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.016, Gen-2 0.813, Gen-1 ledger 0.863 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 965 model 0.2266 vs Kalshi 0.2046; n 197 model 0.3023 vs Kalshi 0.1717.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 366,870 model-market comparisons (604,765 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 121,545 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-10T21:07:49.315485+00:00'], shadow board 101,091 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-10T21:07:53.280970+00:00'], Model 4 43,814 rows, 30,065 settled tickers, 11,289 tickers with an external scan.
* By model: {"gen1_ledger": 81486, "gen1_elo": 50803, "fair_v1": 50803, "gen2": 50803, "gen1_sr": 50803, "model4_fundamental": 41128, "model4_conditioned": 41044}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 87,686 | 14.0 | 9.5 | 20.2 | 15.2 | 19.1 | 13.7 | 8.2 | 11.88 | 41.1% | 22.0% |
| MW fair_v1 | 50,803 | 12.7 | 8.6 | 18.7 | 15.2 | 19.6 | 15.0 | 10.2 | 13.13 | 44.8% | 25.2% |
| MW gen1_elo | 50,803 | 12.4 | 8.8 | 19.2 | 15.3 | 19.4 | 14.9 | 10.0 | 12.96 | 44.3% | 24.9% |
| MW gen1_ledger | 36,883 | 15.8 | 10.8 | 22.1 | 15.1 | 18.6 | 11.9 | 5.6 | 10.28 | 36.1% | 17.5% |
| MW gen1_sr | 50,803 | 10.0 | 7.2 | 16.6 | 13.9 | 20.8 | 18.8 | 12.8 | 15.92 | 52.3% | 31.5% |
| MW gen2 | 50,803 | 10.9 | 7.6 | 16.7 | 13.7 | 19.6 | 17.7 | 13.8 | 15.48 | 51.2% | 31.5% |
| all families model4_conditioned | 41,044 | 22.2 | 17.9 | 34.5 | 16.9 | 5.0 | 2.2 | 1.2 | 6.07 | 8.4% | 3.5% |
| all families model4_fundamental | 41,128 | 17.3 | 13.5 | 34.0 | 19.9 | 9.9 | 3.8 | 1.5 | 7.61 | 15.3% | 5.3% |

Configurable thresholds (primary): >=5pp 76.5%, >=10pp 56.3%, >=15pp 41.1%, >=20pp 30.3%, >=25pp 22.0%, >=30pp 15.9%, >=40pp 8.2%, >=50pp 3.9%
Executable gap (model outside the book, before fees): median 8.5pp; >=10pp 45.4%, >=25pp 17.4%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,089 | 28.1 | 15.7 | 28.1 | 13.3 | 10.7 | 3.6 | 0.6 | 5.82 | 14.9% | 4.2% |
| CHALLENGER | 8,080 | 16.3 | 9.5 | 20.6 | 15.2 | 15.9 | 11.5 | 10.9 | 10.93 | 38.4% | 22.4% |
| ITF_MEN | 14,559 | 9.6 | 7.3 | 16.9 | 14.9 | 21.2 | 17.3 | 12.8 | 15.48 | 51.2% | 30.1% |
| ITF_WOMEN | 19,658 | 9.5 | 7.0 | 16.1 | 14.7 | 22.1 | 18.6 | 12.0 | 15.96 | 52.7% | 30.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,084 | 16.7 | 13.2 | 25.1 | 20.7 | 16.5 | 6.7 | 1.1 | 8.56 | 24.3% | 7.8% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,089 | 26.4 | 15.7 | 26.2 | 15.8 | 11.2 | 3.9 | 0.8 | 6.09 | 16.0% | 4.7% |
| CHALLENGER | 8,080 | 14.4 | 9.1 | 19.1 | 13.8 | 18.5 | 13.7 | 11.5 | 12.5 | 43.7% | 25.2% |
| ITF_MEN | 14,559 | 8.0 | 6.2 | 15.0 | 13.8 | 20.3 | 20.2 | 16.5 | 17.94 | 57.0% | 36.7% |
| ITF_WOMEN | 19,658 | 7.9 | 5.9 | 14.2 | 12.7 | 20.6 | 21.2 | 17.6 | 19.06 | 59.4% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,084 | 14.1 | 10.4 | 21.7 | 16.2 | 22.3 | 12.7 | 2.5 | 11.18 | 37.6% | 15.2% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,089 | 23.3 | 14.1 | 25.6 | 15.5 | 14.4 | 6.0 | 1.1 | 7.08 | 21.6% | 7.1% |
| CHALLENGER | 8,080 | 15.0 | 9.6 | 20.8 | 15.5 | 16.2 | 12.0 | 10.9 | 11.31 | 39.1% | 22.9% |
| ITF_MEN | 14,559 | 9.4 | 7.2 | 17.1 | 14.2 | 21.6 | 17.4 | 13.1 | 15.85 | 52.1% | 30.5% |
| ITF_WOMEN | 19,658 | 9.3 | 6.9 | 16.3 | 15.6 | 22.0 | 18.5 | 11.3 | 15.62 | 51.9% | 29.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,084 | 22.6 | 17.1 | 31.9 | 15.3 | 8.8 | 3.2 | 1.0 | 6.12 | 13.1% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,464 | 28.0 | 19.5 | 29.2 | 12.2 | 8.1 | 2.6 | 0.5 | 5.26 | 11.1% | 3.0% |
| CHALLENGER | 4,957 | 22.7 | 14.5 | 28.0 | 14.7 | 13.1 | 5.5 | 1.5 | 7.03 | 20.1% | 7.0% |
| DOUBLES | 2,691 | 4.8 | 4.5 | 12.9 | 11.0 | 20.5 | 24.6 | 21.6 | 23.13 | 66.7% | 46.2% |
| ITF_MEN | 10,770 | 12.7 | 9.4 | 21.3 | 15.6 | 21.8 | 13.0 | 6.2 | 11.9 | 41.0% | 19.2% |
| ITF_WOMEN | 12,781 | 13.5 | 9.3 | 19.8 | 15.7 | 21.6 | 14.6 | 5.4 | 12.19 | 41.7% | 20.1% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,815 | 24.1 | 16.0 | 31.5 | 16.9 | 8.9 | 2.5 | 0.2 | 6.44 | 11.6% | 2.8% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,962 | 28.5 | 15.9 | 28.5 | 13.2 | 10.5 | 3.1 | 0.3 | 5.67 | 13.9% | 3.4% |
| CHALLENGER | 5,681 | 21.0 | 12.0 | 25.7 | 17.9 | 15.9 | 5.8 | 1.6 | 8.21 | 23.3% | 7.4% |
| ITF_MEN | 10,639 | 11.9 | 8.6 | 20.4 | 17.2 | 22.2 | 14.2 | 5.5 | 12.54 | 42.0% | 19.8% |
| ITF_WOMEN | 14,404 | 11.4 | 8.5 | 19.0 | 17.0 | 24.0 | 15.4 | 4.7 | 13.15 | 44.1% | 20.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,970 | 17.0 | 13.3 | 25.4 | 21.0 | 16.5 | 6.2 | 0.6 | 8.42 | 23.3% | 6.8% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,962 | 26.7 | 16.0 | 26.5 | 15.7 | 11.2 | 3.5 | 0.4 | 6.0 | 15.0% | 3.9% |
| CHALLENGER | 5,681 | 18.2 | 11.6 | 23.9 | 16.2 | 19.0 | 9.1 | 1.9 | 8.97 | 30.0% | 11.0% |
| ITF_MEN | 10,640 | 9.5 | 7.3 | 17.5 | 16.0 | 22.1 | 18.4 | 9.2 | 14.93 | 49.7% | 27.6% |
| ITF_WOMEN | 14,405 | 8.9 | 7.0 | 16.0 | 14.3 | 22.5 | 20.6 | 10.8 | 16.51 | 53.8% | 31.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,970 | 14.3 | 10.5 | 21.9 | 16.4 | 22.5 | 12.4 | 1.9 | 11.03 | 36.8% | 14.3% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,395 | 28.3 | 19.7 | 29.2 | 12.4 | 7.8 | 2.3 | 0.3 | 5.22 | 10.4% | 2.7% |
| CHALLENGER | 4,389 | 24.0 | 15.4 | 29.2 | 14.8 | 12.4 | 3.8 | 0.4 | 6.58 | 16.6% | 4.2% |
| DOUBLES | 2,524 | 4.7 | 4.5 | 13.2 | 11.1 | 20.4 | 24.5 | 21.7 | 23.04 | 66.6% | 46.2% |
| ITF_MEN | 9,320 | 13.4 | 10.0 | 22.8 | 16.1 | 21.9 | 11.6 | 4.3 | 11.11 | 37.7% | 15.9% |
| ITF_WOMEN | 11,020 | 14.2 | 9.8 | 20.8 | 16.2 | 21.7 | 13.6 | 3.6 | 11.42 | 39.0% | 17.2% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,752 | 24.4 | 16.4 | 31.4 | 16.8 | 8.8 | 2.0 | 0.1 | 6.42 | 10.9% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,691 | 4.8 | 4.5 | 12.9 | 11.0 | 20.5 | 24.6 | 21.6 | 23.13 | 66.7% | 46.2% |
| singles | 34,192 | 16.7 | 11.3 | 22.9 | 15.4 | 18.4 | 11.0 | 4.3 | 9.76 | 33.7% | 15.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 10,699 | 12.7 | 8.9 | 19.5 | 15.2 | 19.6 | 14.3 | 9.7 | 12.81 | 43.6% | 24.0% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 33,166 | 13.2 | 8.7 | 18.9 | 15.1 | 19.1 | 15.0 | 10.2 | 12.95 | 44.2% | 25.1% |
| UNKNOWN | 6,525 | 10.4 | 7.5 | 16.9 | 16.4 | 21.6 | 15.9 | 11.3 | 14.49 | 48.8% | 27.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 14,326 | 19.3 | 11.8 | 22.5 | 15.8 | 14.8 | 9.5 | 6.4 | 8.99 | 30.7% | 15.8% |
| B | 6,160 | 12.9 | 8.4 | 19.7 | 15.3 | 19.7 | 12.5 | 11.6 | 12.83 | 43.7% | 24.0% |
| C | 7,167 | 12.0 | 8.6 | 19.5 | 15.9 | 18.8 | 14.6 | 10.5 | 12.91 | 43.9% | 25.1% |
| D | 8,233 | 11.6 | 8.4 | 17.8 | 15.0 | 22.1 | 15.7 | 9.5 | 13.98 | 47.2% | 25.2% |
| F | 14,917 | 7.3 | 5.6 | 14.9 | 14.4 | 23.0 | 21.2 | 13.6 | 18.02 | 57.8% | 34.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,784 | 24.9 | 15.9 | 29.0 | 14.9 | 10.6 | 3.4 | 1.2 | 6.35 | 15.3% | 4.7% |
| B | 5,058 | 16.6 | 10.9 | 24.3 | 16.8 | 18.9 | 9.4 | 3.0 | 9.6 | 31.3% | 12.4% |
| C | 7,230 | 11.0 | 7.8 | 19.6 | 14.9 | 21.1 | 15.6 | 10.1 | 13.52 | 46.8% | 25.7% |
| D | 5,576 | 14.5 | 10.1 | 21.0 | 15.3 | 21.0 | 12.6 | 5.5 | 11.32 | 39.0% | 18.1% |
| F | 9,235 | 10.2 | 8.3 | 16.4 | 14.5 | 23.4 | 19.1 | 8.1 | 15.33 | 50.6% | 27.2% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 16,223 | 17.7 | 10.8 | 21.5 | 15.5 | 15.1 | 10.2 | 9.1 | 10.0 | 34.5% | 19.3% |
| LIMITED | 11,033 | 13.5 | 9.5 | 20.5 | 16.0 | 19.6 | 13.4 | 7.6 | 11.92 | 40.6% | 21.0% |
| POOR | 23,547 | 8.9 | 6.6 | 16.0 | 14.7 | 22.6 | 19.1 | 12.1 | 16.34 | 53.8% | 31.2% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,210 | 23.6 | 18.1 | 33.0 | 15.5 | 6.4 | 3.0 | 0.4 | 5.9 | 9.8% | 3.4% |
| GAME_SPREAD | 6,889 | 22.8 | 15.3 | 32.0 | 16.8 | 9.1 | 3.3 | 0.7 | 6.69 | 13.1% | 4.0% |
| MATCH_WINNER | 36,883 | 15.8 | 10.8 | 22.1 | 15.1 | 18.6 | 11.9 | 5.6 | 10.28 | 36.1% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 16,948 | 28.3 | 16.8 | 30.7 | 12.6 | 8.9 | 2.4 | 0.3 | 5.58 | 11.6% | 2.7% |
| TOTAL_GAMES | 11,532 | 9.7 | 10.8 | 36.1 | 25.8 | 10.4 | 4.2 | 2.9 | 9.15 | 17.6% | 7.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,597 | 24.4 | 28.8 | 33.3 | 8.1 | 4.0 | 1.2 | 0.3 | 4.8 | 5.4% | 1.5% |
| GAME_SPREAD | 9,493 | 46.7 | 15.9 | 25.1 | 7.4 | 2.4 | 1.9 | 0.6 | 3.32 | 4.9% | 2.5% |
| TOTAL_GAMES | 16,954 | 6.6 | 9.8 | 40.7 | 29.9 | 7.3 | 3.3 | 2.4 | 9.17 | 13.0% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,633 | 23.8 | 16.6 | 34.6 | 14.8 | 6.9 | 2.7 | 0.5 | 6.06 | 10.1% | 3.2% |
| GAME_SPREAD | 9,502 | 20.4 | 13.4 | 28.4 | 20.1 | 12.1 | 4.4 | 1.2 | 7.67 | 17.6% | 5.5% |
| TOTAL_GAMES | 16,993 | 10.0 | 10.8 | 36.5 | 24.3 | 11.3 | 4.4 | 2.6 | 9.02 | 18.4% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 50,803 | 44.8% | 25.2% | 13.13 | 35.5% | 15.2% | 10.71 |
| gen1_elo | 50,803 | 44.3% | 24.9% | 12.96 | 35.0% | 15.0% | 10.5 |
| gen1_sr | 50,803 | 52.3% | 31.5% | 15.92 | 44.0% | 21.6% | 12.98 |
| gen2 | 50,803 | 51.2% | 31.5% | 15.48 | 43.9% | 23.1% | 12.83 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,098 | 15.5 | 10.4 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 30,705 | 10.9 | 7.3 | 17.0 | 13.9 | 19.2 | 17.1 | 14.7 | 15.38 | 50.9% | 31.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 30,351 | 16.4 | 11.1 | 22.7 | 15.2 | 18.2 | 11.5 | 5.0 | 9.95 | 34.6% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 87,686 | 30351 | 23570 | 33765 | 25.0 | 136.6 | 1451.1 |
| ge_15pp | 36,054 | 10516 | 8394 | 17144 | 28.8 | 443.6 | 1451.1 |
| ge_25pp | 19,266 | 4998 | 3666 | 10602 | 34.5 | 593.2 | 1431.1 |
| lt_10pp | 38,327 | 15225 | 11149 | 11953 | 22.8 | 49.5 | 1421.7 |

Current slate `SL-20261110T212314Z-6366ef1f`: 530 priced rows, quote age at build {'median': 15.8, 'max': 15.8}, freshness {'AGING': 530}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 51 | 0.0 | 0.0 | 35.3 | 9.8 | 31.4 | 19.6 | 3.9 | 18.34 | 54.9% | 23.5% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,879 | 19.2 | 11.1 | 25.5 | 18.1 | 17.9 | 7.3 | 0.9 | 8.8 | 26.1% | 8.2% |
| KALSHI_LONE_OUTLIER | 32 | 6.2 | 6.2 | 75.0 | 6.2 | 3.1 | 3.1 | 0.0 | 6.16 | 6.2% | 3.1% |
| MARKETS_AGREE | 1,067 | 66.5 | 33.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,269 | 0.0 | 2.2 | 38.6 | 25.9 | 23.8 | 8.7 | 0.9 | 11.65 | 33.4% | 9.6% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 50,803 | 8327 (16.4%) | 27.3% | 1.0% | {"EXTERNAL_STALE": 4879, "AGREES_WITH_KALSHI": 2269, "ALL_AGREE": 1067, "SUPPORTS_MODEL_DIRECTION": 49, "AGREES_WITH_MODEL": 32, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 22,739 | 2062 (9.1%) | 36.7% | 1.5% | {"EXTERNAL_STALE": 1275, "AGREES_WITH_KALSHI": 757, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 12,806 | 633 (4.9%) | 34.4% | 2.1% | {"EXTERNAL_STALE": 402, "AGREES_WITH_KALSHI": 218, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,930 | 602 (10.2%) | 35.0% | 2.2% | {"EXTERNAL_STALE": 378, "AGREES_WITH_KALSHI": 211, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 20,333 | 4787 (23.5%) | 19.3% | 0.9% | {"EXTERNAL_STALE": 2720, "ALL_AGREE": 1067, "AGREES_WITH_KALSHI": 925, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 28, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 9,939 | 10.7 | 7.6 | 19.1 | 14.3 | 21.7 | 16.4 | 10.2 | 14.28 | 48.3% | 26.6% |
| 4-10x | 6,773 | 11.1 | 8.6 | 18.0 | 14.9 | 21.9 | 14.7 | 10.8 | 14.05 | 47.4% | 25.5% |
| <2x | 26,002 | 14.7 | 9.6 | 19.9 | 15.9 | 17.5 | 13.3 | 9.1 | 11.61 | 39.8% | 22.3% |
| >=10x | 8,089 | 10.2 | 6.4 | 15.1 | 14.2 | 21.6 | 19.1 | 13.3 | 16.52 | 54.0% | 32.4% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 13,374 | 12.5 | 8.4 | 19.8 | 16.1 | 19.0 | 13.6 | 10.5 | 12.8 | 43.2% | 24.1% |
| 300-1000 | 10,916 | 11.7 | 8.7 | 17.8 | 15.0 | 20.9 | 16.3 | 9.6 | 13.79 | 46.8% | 25.9% |
| <300 | 16,056 | 8.1 | 5.8 | 15.0 | 14.5 | 22.8 | 20.2 | 13.5 | 17.46 | 56.5% | 33.8% |
| >=3000 | 10,457 | 21.1 | 12.8 | 24.0 | 15.4 | 13.9 | 7.4 | 5.3 | 7.84 | 26.7% | 12.7% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1533 | 0.55 | 0.4111 | 0.4801 | +0.070 | -0.069 | 0.0041 ± 0.0039 |
| ratio 4-10x | 1039 | 0.5771 | 0.432 | 0.486 | +0.091 | -0.054 | 0.0101 ± 0.005 |
| ratio <2x | 3769 | 0.5367 | 0.4143 | 0.437 | +0.100 | -0.023 | 0.0146 ± 0.0023 |
| ratio >=10x | 1281 | 0.5649 | 0.3924 | 0.4403 | +0.125 | -0.048 | 0.0175 ± 0.005 |
| thinner_sample 1000-3000 | 2111 | 0.5412 | 0.414 | 0.4467 | +0.095 | -0.033 | 0.0124 ± 0.0032 |
| thinner_sample 300-1000 | 1700 | 0.5661 | 0.426 | 0.4741 | +0.092 | -0.048 | 0.0058 ± 0.0038 |
| thinner_sample <300 | 2484 | 0.5571 | 0.3898 | 0.4485 | +0.109 | -0.059 | 0.0153 ± 0.0035 |
| thinner_sample >=3000 | 1327 | 0.528 | 0.4348 | 0.4439 | +0.084 | -0.009 | 0.0151 ± 0.0031 |
| data_status ADEQUATE | 2115 | 0.5316 | 0.4293 | 0.4388 | +0.093 | -0.009 | 0.0156 ± 0.0026 |
| data_status LIMITED | 1859 | 0.5503 | 0.4173 | 0.4664 | +0.084 | -0.049 | 0.0083 ± 0.0035 |
| data_status POOR | 3648 | 0.5597 | 0.4001 | 0.4542 | +0.105 | -0.054 | 0.0125 ± 0.0028 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1109 | 0.1977 | 0.198 | -0.0003 ± 0.0005 | 0.5753 | 0.5761 | 0.5049 | 0.4897 | 0.5041 | -0.092 ± 0.0142 | -0.0087 (8) |
| 3-5 | 700 | 0.2065 | 0.2059 | +0.0006 ± 0.0014 | 0.5983 | 0.5951 | 0.5047 | 0.465 | 0.4771 | -0.103 ± 0.0176 | 0.01 (3) |
| 5-10 | 1642 | 0.204 | 0.2024 | +0.0016 ± 0.0017 | 0.595 | 0.5885 | 0.512 | 0.4381 | 0.4622 | -0.095 ± 0.0115 | -0.0143 (7) |
| 10-15 | 1323 | 0.2192 | 0.2094 | +0.0098 ± 0.0031 | 0.6302 | 0.6025 | 0.5254 | 0.4021 | 0.4233 | -0.109 ± 0.0128 | -0.055 (6) |
| 15-25 | 1686 | 0.2267 | 0.2079 | +0.0187 ± 0.0043 | 0.6486 | 0.5991 | 0.575 | 0.3804 | 0.43 | -0.106 ± 0.0112 | -0.0045 (11) |
| 25-40 | 965 | 0.2266 | 0.2046 | +0.0219 ± 0.0087 | 0.6439 | 0.5899 | 0.6496 | 0.34 | 0.4591 | -0.072 ± 0.0135 | -0.06 (2) |
| 40+ | 197 | 0.3023 | 0.1717 | +0.1306 ± 0.0266 | 0.811 | 0.515 | 0.7295 | 0.2738 | 0.3655 | -0.089 ± 0.0256 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5685 | 0.1867 | 0.1876 | -0.0010 ± 0.0002 | 0.5498 | 0.551 | 0.4917 | 0.4765 | 0.5106 | -0.018 ± 0.0058 | -0.01 (28) |
| 3-5 | 3776 | 0.1991 | 0.1971 | +0.0020 ± 0.0006 | 0.5792 | 0.5723 | 0.4829 | 0.4431 | 0.4372 | -0.060 ± 0.0073 | 0.005 (6) |
| 5-10 | 8308 | 0.2016 | 0.1976 | +0.0041 ± 0.0007 | 0.5892 | 0.5759 | 0.4836 | 0.4098 | 0.4192 | -0.049 ± 0.0049 | -0.0114 (22) |
| 10-15 | 6759 | 0.2025 | 0.1863 | +0.0161 ± 0.0013 | 0.5917 | 0.5467 | 0.4857 | 0.3618 | 0.3589 | -0.065 ± 0.0053 | -0.0379 (19) |
| 15-25 | 8635 | 0.2067 | 0.1668 | +0.0399 ± 0.0017 | 0.6053 | 0.4957 | 0.4991 | 0.3034 | 0.3002 | -0.070 ± 0.0044 | -0.0043 (51) |
| 25-40 | 6822 | 0.2241 | 0.1242 | +0.0999 ± 0.0027 | 0.6428 | 0.383 | 0.5257 | 0.2119 | 0.2134 | -0.062 ± 0.0041 | -0.0733 (3) |
| 40+ | 4650 | 0.3816 | 0.0429 | +0.3387 ± 0.0035 | 0.9936 | 0.1679 | 0.629 | 0.1008 | 0.0557 | -0.077 ± 0.0029 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 887 | 0.2052 | 0.2055 | -0.0004 ± 0.0005 | 0.5912 | 0.5924 | 0.5083 | 0.4934 | 0.5186 | -0.098 ± 0.0163 | -0.0117 (6) |
| 3-5 | 629 | 0.2114 | 0.2086 | +0.0028 ± 0.0015 | 0.6054 | 0.5997 | 0.5172 | 0.4776 | 0.4595 | -0.129 ± 0.0197 | 0.01 (3) |
| 5-10 | 1409 | 0.2075 | 0.2055 | +0.0020 ± 0.0018 | 0.6016 | 0.596 | 0.5402 | 0.4656 | 0.4918 | -0.089 ± 0.0125 | -0.01 (4) |
| 10-15 | 1230 | 0.215 | 0.2074 | +0.0076 ± 0.0033 | 0.623 | 0.6007 | 0.5607 | 0.4363 | 0.4707 | -0.106 ± 0.0135 | -0.04 (5) |
| 15-25 | 1777 | 0.2324 | 0.2117 | +0.0207 ± 0.0043 | 0.661 | 0.6075 | 0.5863 | 0.3906 | 0.4367 | -0.104 ± 0.0112 | -0.0183 (12) |
| 25-40 | 1246 | 0.2689 | 0.1993 | +0.0696 ± 0.0079 | 0.7491 | 0.5788 | 0.6604 | 0.3466 | 0.3949 | -0.118 ± 0.0127 | -0.008 (5) |
| 40+ | 444 | 0.3732 | 0.1615 | +0.2117 ± 0.0191 | 1.0173 | 0.4888 | 0.7354 | 0.2473 | 0.2883 | -0.090 ± 0.0184 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4866 | 0.1909 | 0.1911 | -0.0002 ± 0.0002 | 0.5573 | 0.5574 | 0.5082 | 0.4931 | 0.5072 | -0.041 ± 0.0064 | -0.0154 (26) |
| 3-5 | 3321 | 0.1931 | 0.1921 | +0.0010 ± 0.0006 | 0.5628 | 0.5596 | 0.5119 | 0.4723 | 0.4794 | -0.045 ± 0.0078 | 0.01 (5) |
| 5-10 | 7386 | 0.1967 | 0.1935 | +0.0033 ± 0.0008 | 0.5782 | 0.5659 | 0.5072 | 0.433 | 0.4507 | -0.039 ± 0.0052 | -0.0117 (6) |
| 10-15 | 6121 | 0.204 | 0.1916 | +0.0124 ± 0.0014 | 0.5982 | 0.5603 | 0.5092 | 0.3853 | 0.3981 | -0.052 ± 0.0057 | -0.0189 (18) |
| 15-25 | 8732 | 0.2165 | 0.1795 | +0.0370 ± 0.0018 | 0.6302 | 0.5275 | 0.524 | 0.3286 | 0.3338 | -0.063 ± 0.0046 | -0.014 (52) |
| 25-40 | 7936 | 0.2515 | 0.1373 | +0.1142 ± 0.0027 | 0.7099 | 0.4193 | 0.5603 | 0.2429 | 0.2256 | -0.079 ± 0.0042 | -0.0095 (20) |
| 40+ | 6273 | 0.4029 | 0.0588 | +0.3442 ± 0.0035 | 1.0618 | 0.2117 | 0.6547 | 0.1184 | 0.0792 | -0.074 ± 0.003 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1084 | 0.1961 | 0.1973 | -0.0012 ± 0.0005 | 0.5717 | 0.5745 | 0.5028 | 0.4874 | 0.5277 | -0.059 ± 0.0141 | -0.0191 (11) |
| 3-5 | 765 | 0.2084 | 0.2067 | +0.0017 ± 0.0013 | 0.6039 | 0.5981 | 0.4988 | 0.4593 | 0.4588 | -0.115 ± 0.0172 | 0.002 (5) |
| 5-10 | 1659 | 0.2042 | 0.2003 | +0.0039 ± 0.0017 | 0.5942 | 0.583 | 0.5127 | 0.439 | 0.4485 | -0.107 ± 0.0113 | -0.01 (10) |
| 10-15 | 1351 | 0.2125 | 0.2034 | +0.0091 ± 0.003 | 0.6153 | 0.5895 | 0.5392 | 0.416 | 0.4426 | -0.107 ± 0.0124 | -0.0286 (7) |
| 15-25 | 1611 | 0.232 | 0.212 | +0.0199 ± 0.0045 | 0.6615 | 0.608 | 0.585 | 0.3909 | 0.4364 | -0.111 ± 0.0115 | -0.03 (1) |
| 25-40 | 946 | 0.2175 | 0.2095 | +0.0080 ± 0.0088 | 0.6249 | 0.6011 | 0.6582 | 0.3474 | 0.4884 | -0.061 ± 0.0137 | -0.0267 (3) |
| 40+ | 206 | 0.3107 | 0.1798 | +0.1309 ± 0.0266 | 0.8393 | 0.5322 | 0.7403 | 0.2852 | 0.3786 | -0.087 ± 0.0272 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5490 | 0.1858 | 0.1863 | -0.0005 ± 0.0002 | 0.5474 | 0.5478 | 0.486 | 0.4707 | 0.486 | -0.036 ± 0.0059 | -0.0189 (44) |
| 3-5 | 3910 | 0.2045 | 0.2026 | +0.0019 ± 0.0006 | 0.5943 | 0.5879 | 0.481 | 0.4415 | 0.4379 | -0.058 ± 0.0073 | -0.0073 (22) |
| 5-10 | 8422 | 0.1968 | 0.1916 | +0.0052 ± 0.0007 | 0.5773 | 0.5608 | 0.4866 | 0.4126 | 0.4139 | -0.056 ± 0.0048 | -0.0117 (42) |
| 10-15 | 6758 | 0.1952 | 0.1802 | +0.0151 ± 0.0013 | 0.5755 | 0.5322 | 0.4963 | 0.373 | 0.3735 | -0.062 ± 0.0052 | -0.0136 (14) |
| 15-25 | 8710 | 0.2119 | 0.1716 | +0.0403 ± 0.0017 | 0.6175 | 0.5066 | 0.5111 | 0.3166 | 0.311 | -0.072 ± 0.0044 | -0.0533 (3) |
| 25-40 | 6765 | 0.2182 | 0.1245 | +0.0938 ± 0.0027 | 0.6301 | 0.383 | 0.5272 | 0.2115 | 0.2226 | -0.054 ± 0.0042 | -0.02 (4) |
| 40+ | 4580 | 0.3891 | 0.0473 | +0.3419 ± 0.0036 | 1.0142 | 0.1787 | 0.6371 | 0.1061 | 0.0622 | -0.076 ± 0.0031 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1530 | 0.1978 | 0.1977 | +0.0002 ± 0.0004 | 0.5744 | 0.5738 | 0.5101 | 0.4951 | 0.4954 | -0.072 ± 0.0116 | -0.0221 (56) |
| 3-5 | 1087 | 0.1889 | 0.189 | -0.0001 ± 0.0011 | 0.5557 | 0.5544 | 0.4984 | 0.4584 | 0.4784 | -0.054 ± 0.0135 | -0.0194 (34) |
| 5-10 | 2190 | 0.2 | 0.1949 | +0.0050 ± 0.0014 | 0.5897 | 0.573 | 0.5085 | 0.435 | 0.4374 | -0.079 ± 0.0097 | -0.005 (78) |
| 10-15 | 1512 | 0.2155 | 0.2028 | +0.0126 ± 0.0029 | 0.6251 | 0.5892 | 0.5427 | 0.42 | 0.4286 | -0.092 ± 0.0119 | 0.0012 (66) |
| 15-25 | 1972 | 0.2317 | 0.208 | +0.0237 ± 0.004 | 0.661 | 0.5998 | 0.5921 | 0.3973 | 0.4351 | -0.091 ± 0.0104 | -0.0214 (59) |
| 25-40 | 1169 | 0.2421 | 0.2109 | +0.0312 ± 0.0082 | 0.6907 | 0.6048 | 0.6892 | 0.3773 | 0.4833 | -0.088 ± 0.0127 | -0.0252 (27) |
| 40+ | 426 | 0.328 | 0.1976 | +0.1304 ± 0.0206 | 0.9406 | 0.5773 | 0.8145 | 0.3386 | 0.4554 | -0.100 ± 0.0192 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5555 | 0.1782 | 0.1783 | -0.0001 ± 0.0002 | 0.5272 | 0.5268 | 0.5121 | 0.4969 | 0.5051 | -0.040 ± 0.0057 | -0.0154 (103) |
| 3-5 | 3848 | 0.1947 | 0.1939 | +0.0008 ± 0.0006 | 0.5682 | 0.5657 | 0.5023 | 0.4625 | 0.4725 | -0.040 ± 0.0072 | -0.0212 (73) |
| 5-10 | 7774 | 0.1977 | 0.191 | +0.0067 ± 0.0007 | 0.583 | 0.5625 | 0.5023 | 0.4289 | 0.4214 | -0.063 ± 0.005 | -0.0084 (134) |
| 10-15 | 5341 | 0.2101 | 0.1939 | +0.0163 ± 0.0015 | 0.612 | 0.5686 | 0.5362 | 0.4134 | 0.407 | -0.072 ± 0.0061 | -0.0057 (111) |
| 15-25 | 6523 | 0.2321 | 0.1995 | +0.0326 ± 0.0022 | 0.6664 | 0.5781 | 0.5765 | 0.3812 | 0.396 | -0.070 ± 0.0056 | -0.026 (108) |
| 25-40 | 4233 | 0.2587 | 0.1906 | +0.0681 ± 0.0042 | 0.731 | 0.5548 | 0.6405 | 0.328 | 0.3782 | -0.066 ± 0.0066 | -0.0277 (53) |
| 40+ | 1911 | 0.3711 | 0.1576 | +0.2136 ± 0.0094 | 1.0454 | 0.4705 | 0.7438 | 0.2439 | 0.2904 | -0.065 ± 0.0086 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7622 | 1.016 ± 0.032 | 1.095 | 0.1678 | 0.1678 | 0.2164 | 0.204 |
| gen2 | 7622 | 0.813 ± 0.029 | 1.069 | 0.1733 | 0.1681 | 0.2342 | 0.2039 |
| gen1_elo | 7622 | 1.002 ± 0.031 | 1.084 | 0.1741 | 0.1679 | 0.2153 | 0.2041 |
| gen1_sr | 7622 | 0.996 ± 0.038 | 1.118 | 0.1332 | 0.1696 | 0.2303 | 0.2036 |
| gen1_ledger | 9886 | 0.863 ± 0.024 | 1.071 | 0.1894 | 0.1751 | 0.2176 | 0.2005 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 36,054)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 8,691 | 24.1% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 8,293 | 23.0% |
| BOOK_QUALITY | execution | 6,227 | 17.3% |
| POOR_DATA | data | 4,151 | 11.5% |
| LIMITED_DATA | data | 2,195 | 6.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 2,048 | 5.7% |
| IDENTITY_AMBIGUOUS | mapping | 1,477 | 4.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,406 | 3.9% |
| IN_PLAY_QUOTE | market_freshness/coverage | 996 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 569 | 1.6% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 24.1%, coverage 23.0%, data 17.6%, execution 17.3%, market_freshness/coverage 8.4%, mapping 4.1%, model_calibration_or_unknown 3.9%, model_calibration 1.6%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.6%, START_UNVERIFIABLE 94.9%, LOW_DATA_QUALITY 71.8%, THIN_PLAYER_HISTORY 60.0%, STALE_PLAYER_DATA 52.4%, STALE_KALSHI_QUOTE 47.5%, MODEL_INTERNAL_DISAGREEMENT 41.8%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 23.8%, MODEL_HIGH_UNCERTAINTY 18.5%, PLAYER_IDENTITY_RISK 15.1%, LEVEL_TRANSFER_RISK 9.7%, LOW_DISPLAYED_LIQUIDITY 8.5%, EVENT_MAPPING_RISK 7.0%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.2%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.4%, POST_SETTLEMENT_OBSERVATION 23.0%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 19,266)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,684 | 34.7% |
| STALE_QUOTE | market_freshness | 3,892 | 20.2% |
| BOOK_QUALITY | execution | 3,217 | 16.7% |
| POOR_DATA | data | 1,768 | 9.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,101 | 5.7% |
| IDENTITY_AMBIGUOUS | mapping | 825 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 650 | 3.4% |
| LIMITED_DATA | data | 646 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 344 | 1.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 138 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.7%, market_freshness 20.2%, execution 16.7%, data 12.5%, market_freshness/coverage 9.1%, mapping 4.3%, model_calibration_or_unknown 1.8%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.1%, START_UNVERIFIABLE 97.2%, LOW_DATA_QUALITY 74.9%, THIN_PLAYER_HISTORY 62.1%, STALE_KALSHI_QUOTE 55.0%, STALE_PLAYER_DATA 45.9%, MODEL_INTERNAL_DISAGREEMENT 42.0%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 22.9%, MODEL_HIGH_UNCERTAINTY 19.1%, PLAYER_IDENTITY_RISK 18.1%, EVENT_MAPPING_RISK 8.5%, LEVEL_TRANSFER_RISK 8.5%, LOW_DISPLAYED_LIQUIDITY 8.3%, MODEL_CALIBRATION_OUTLIER 4.7%, EXTERNAL_MARKET_REJECTION 1.8%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.6%, POST_SETTLEMENT_OBSERVATION 34.7%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 15439, "IDENTITY_AMBIGUOUS": 3827}; ticker orientation: {"VERIFIED": 19266}.

Checks: discipline:AMBIGUOUS 1244, discipline:PASS 18022, identity_confidence:AMBIGUOUS 3487, identity_confidence:PASS 15779, level_mapping:NA 1256, level_mapping:PASS 18010, market_pair:AMBIGUOUS 504, market_pair:NA 416, market_pair:PASS 18346, model_complement:NA 378, model_complement:PASS 18888, namesake:AMBIGUOUS 6, namesake:PASS 19260, physical_match_id:NA 6460, physical_match_id:PASS 12806, player_ids:PASS 19266, same_pair_other_event:PASS 19266, ticker_orientation:PASS 19266

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,553 | 3.7% | 3.1% | 1.3% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 24, "market_freshness/coverage": 22} | 5.48 | 0.222 / 0.2176 (851) | 25.6% | 2.4% | 3.1% | 3.0% |
| CHALLENGER | 13,037 | 16.6% | 6.0% | 11.2% | {"coverage": 1319, "market_freshness": 263, "market_freshness/coverage": 235, "data": 164, "model_calibration_or_unknown": 80, "execution": 41, "model_calibration": 39, "mapping": 17, "possible_market_error": 1} | 7.35 | 0.2206 / 0.2097 (2997) | 41.2% | 14.0% | 4.0% | 22.8% |
| DOUBLES | 2,691 | 46.2% | 46.2% | 6.5% | {"execution": 690, "mapping": 370, "market_freshness": 106, "market_freshness/coverage": 71, "coverage": 7} | 23.04 | 0.299 / 0.2321 (657) | 8.7% | 0.0% | 100.0% | 6.2% |
| ITF_MEN | 25,329 | 25.4% | 17.9% | 33.4% | {"coverage": 2232, "market_freshness": 1344, "execution": 1031, "data": 970, "market_freshness/coverage": 630, "mapping": 225, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.85 | 0.2195 / 0.2002 (5209) | 41.4% | 69.8% | 14.9% | 21.2% |
| ITF_WOMEN | 32,439 | 26.5% | 18.9% | 44.5% | {"coverage": 3047, "market_freshness": 1918, "execution": 1372, "data": 1179, "market_freshness/coverage": 736, "mapping": 207, "model_calibration_or_unknown": 97, "model_calibration": 23} | 12.48 | 0.2039 / 0.1941 (6178) | 42.3% | 57.3% | 9.9% | 21.6% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,899 | 5.9% | 5.0% | 1.5% | {"market_freshness": 111, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.64 | 0.2307 / 0.2205 (804) | 30.2% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.5% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 519 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 725 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFMATCH-26NOV10KOUPOR-POR` | ITF_MEN | fair_v1 | 87% / 2% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 403 min (STALE); data POOR (grade D, thinner serve sample 1554.0, ratio 1.02); no external reference |
| 12 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 13 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 15 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); no external reference |
| 16 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 17 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 18 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 19 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 20 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 21 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 22 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 23 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 24 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 25 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 26 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 573 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 27 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 28 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 29 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 30 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 31 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 32 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 33 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 34 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 35 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 36 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 37 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 38 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 39 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 40 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 41 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 43 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 44 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 45 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 46 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 47 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 48 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 49 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.1h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 446 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 50 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9722, "by_level_share_of_ge_25pp": {"ATP": 0.0127, "CHALLENGER": 0.1121, "DOUBLES": 0.0646, "ITF_MEN": 0.3344, "ITF_WOMEN": 0.4453, "OTHER": 0.0006, "WTA": 0.0151, "WTA125": 0.0152}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5503, "share_primary_cause_market_settled_or_in_play": 0.4377, "share_primary_cause_stale_quote_only": 0.202}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 19266, "identity_ambiguous_share": 0.1986, "ticker_orientation": {"VERIFIED": 19266}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 12806, "with_external": 633, "coverage": 0.0494, "external_status": {"EXTERNAL_STALE": 402, "AGREES_WITH_KALSHI": 218, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 402, "MODEL_LONE_OUTLIER": 218, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3444, "share_external_supports_model": 0.0205}, "pregame_clean_ge_25pp": {"n": 5930, "with_external": 602, "coverage": 0.1015, "external_status": {"EXTERNAL_STALE": 378, "AGREES_WITH_KALSHI": 211, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 378, "MODEL_LONE_OUTLIER": 211, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3505, "share_external_supports_model": 0.0216}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 479.0, "median_sample_ratio": 2.44, "median_min_matches": 18.0, "median_max_days_since_last": 246.0, "share_severe_asymmetry": 0.2079, "data_status": {"POOR": 10911, "LIMITED": 4872, "ADEQUATE": 3483}, "comparison_lt_10pp": {"median_thinner_serve_points": 1713.0, "median_sample_ratio": 1.7, "median_min_matches": 88.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1533, "model_minus_observed": 0.0699, "kalshi_minus_observed": -0.069, "brier_diff_model_minus_kalshi": 0.0041}, "4-10x": {"n": 1039, "model_minus_observed": 0.091, "kalshi_minus_observed": -0.054, "brier_diff_model_minus_kalshi": 0.0101}, "<2x": {"n": 3769, "model_minus_observed": 0.0997, "kalshi_minus_observed": -0.0227, "brier_diff_model_minus_kalshi": 0.0146}, ">=10x": {"n": 1281, "model_minus_observed": 0.1246, "kalshi_minus_observed": -0.0479, "brier_diff_model_minus_kalshi": 0.0175}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 7622, "model": {"intercept": -0.557, "slope": 0.813, "slope_se": 0.029}, "kalshi_mid_same_rows": {"intercept": 0.169, "slope": 1.069, "slope_se": 0.033}, "mean_extremity_model": 0.1733, "mean_extremity_kalshi": 0.1681, "model_brier": 0.2342, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0303, "brier_diff_se": 0.0022, "model_logloss": 0.6663, "kalshi_logloss": 0.5903}, "fair_v1": {"n": 7622, "model": {"intercept": -0.457, "slope": 1.016, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.228, "slope": 1.095, "slope_se": 0.033}, "mean_extremity_model": 0.1678, "mean_extremity_kalshi": 0.1678, "model_brier": 0.2164, "kalshi_brier": 0.204, "brier_diff_model_minus_kalshi": 0.0124, "brier_diff_se": 0.0018, "model_logloss": 0.6222, "kalshi_logloss": 0.5904}, "gen1_elo": {"n": 7622, "model": {"intercept": -0.448, "slope": 1.002, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.227, "slope": 1.084, "slope_se": 0.032}, "mean_extremity_model": 0.1741, "mean_extremity_kalshi": 0.1679, "model_brier": 0.2153, "kalshi_brier": 0.2041, "brier_diff_model_minus_kalshi": 0.0112, "brier_diff_se": 0.0018, "model_logloss": 0.6204, "kalshi_logloss": 0.5906}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2521, "share_ge_15": 0.4476, "median_abs_gap": 13.13, "n": 50803}, "gen1_elo": {"share_ge_25": 0.2494, "share_ge_15": 0.4433, "median_abs_gap": 12.96, "n": 50803}, "gen1_sr": {"share_ge_25": 0.3151, "share_ge_15": 0.5228, "median_abs_gap": 15.92, "n": 50803}, "gen2": {"share_ge_25": 0.3154, "share_ge_15": 0.5116, "median_abs_gap": 15.48, "n": 50803}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1523, "share_ge_15": 0.3551, "median_abs_gap": 10.71, "n": 38940}, "gen1_elo": {"share_ge_25": 0.1505, "share_ge_15": 0.3497, "median_abs_gap": 10.5, "n": 38940}, "gen1_sr": {"share_ge_25": 0.2162, "share_ge_15": 0.4396, "median_abs_gap": 12.98, "n": 38942}, "gen2": {"share_ge_25": 0.2309, "share_ge_15": 0.4387, "median_abs_gap": 12.83, "n": 38942}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.48, "share_ge_25_all": 0.0374, "share_ge_25_pregame_clean": 0.0313}, "WTA": {"median_abs_gap_pregame_clean": 7.64, "share_ge_25_all": 0.0594, "share_ge_25_pregame_clean": 0.0504}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2354, "share_within_10pp_all": 0.4371, "share_within_10pp_pregame_clean": 0.4906, "corr_model_vs_mid_pregame_clean": 0.8493}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1109, "model_brier": 0.1977, "kalshi_brier": 0.198, "brier_diff_model_minus_kalshi": -0.0003}, "10-15": {"n_settled": 1323, "model_brier": 0.2192, "kalshi_brier": 0.2094, "brier_diff_model_minus_kalshi": 0.0098}, "15-25": {"n_settled": 1686, "model_brier": 0.2267, "kalshi_brier": 0.2079, "brier_diff_model_minus_kalshi": 0.0187}, "25-40": {"n_settled": 965, "model_brier": 0.2266, "kalshi_brier": 0.2046, "brier_diff_model_minus_kalshi": 0.0219}, "3-5": {"n_settled": 700, "model_brier": 0.2065, "kalshi_brier": 0.2059, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 197, "model_brier": 0.3023, "kalshi_brier": 0.1717, "brier_diff_model_minus_kalshi": 0.1306}, "5-10": {"n_settled": 1642, "model_brier": 0.204, "kalshi_brier": 0.2024, "brier_diff_model_minus_kalshi": 0.0016}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.557, "slope": 0.813, "slope_se": 0.029}, "kalshi_slope": {"intercept": 0.169, "slope": 1.069, "slope_se": 0.033}, "n": 7622}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.494, "slope": 0.863, "slope_se": 0.024}, "kalshi_slope": {"intercept": 0.158, "slope": 1.071, "slope_se": 0.028}, "n": 9886}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 657, "model_brier": 0.299, "kalshi_brier": 0.2321, "brier_diff_model_minus_kalshi": 0.0669, "brier_diff_se": 0.0114, "corr_model_outcome": 0.1003, "corr_kalshi_outcome": 0.2815}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
