# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-04T07:53Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 76,692): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.4%, 15-25 19.1%, 25-40 13.6%, 40+ 8.0%; median gap 11.79 pp.
* **Where the extremes live**: 96.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.6%, Challenger 10.8%, doubles 6.7%). Main tour: ATP 3.9% and WTA 6.1% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 16,579): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.3%, STALE_QUOTE 19.6%, BOOK_QUALITY 18.1%, POOR_DATA 9.6%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 3.5%, IN_PLAY_QUOTE 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.3%, market_freshness 19.6%, execution 18.1%, data 13.1%, market_freshness/coverage 9.0%, mapping 4.3%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.5% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.3% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 16,579 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.7% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 476.0 points vs 1736.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.028, Gen-2 0.817, Gen-1 ledger 0.865 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 817 model 0.2207 vs Kalshi 0.2062; n 175 model 0.2937 vs Kalshi 0.1769.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 329,063 model-market comparisons (536,697 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 109,630 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-04T07:34:56.018302+00:00'], shadow board 88,121 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-04T07:34:59.880860+00:00'], Model 4 41,547 rows, 26,651 settled tickers, 10,117 tickers with an external scan.
* By model: {"gen1_ledger": 74130, "gen1_elo": 44282, "fair_v1": 44282, "gen2": 44282, "gen1_sr": 44282, "model4_fundamental": 38944, "model4_conditioned": 38861}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 76,692 | 14.1 | 9.6 | 20.2 | 15.4 | 19.1 | 13.6 | 8.0 | 11.79 | 40.7% | 21.6% |
| MW fair_v1 | 44,282 | 12.9 | 8.7 | 18.8 | 15.6 | 19.6 | 14.7 | 9.8 | 12.95 | 44.0% | 24.5% |
| MW gen1_elo | 44,282 | 12.6 | 8.8 | 19.4 | 15.4 | 19.5 | 14.6 | 9.7 | 12.73 | 43.8% | 24.2% |
| MW gen1_ledger | 32,410 | 15.8 | 10.9 | 22.1 | 15.1 | 18.4 | 12.2 | 5.5 | 10.28 | 36.1% | 17.7% |
| MW gen1_sr | 44,282 | 10.2 | 7.3 | 16.9 | 13.9 | 20.6 | 18.6 | 12.5 | 15.7 | 51.7% | 31.1% |
| MW gen2 | 44,282 | 11.1 | 7.6 | 16.7 | 13.8 | 19.5 | 17.7 | 13.6 | 15.35 | 50.7% | 31.3% |
| all families model4_conditioned | 38,861 | 22.2 | 18.0 | 34.2 | 17.1 | 5.0 | 2.2 | 1.2 | 6.06 | 8.4% | 3.4% |
| all families model4_fundamental | 38,944 | 17.4 | 13.5 | 33.9 | 19.9 | 10.0 | 3.8 | 1.5 | 7.63 | 15.3% | 5.3% |

Configurable thresholds (primary): >=5pp 76.2%, >=10pp 56.1%, >=15pp 40.7%, >=20pp 30.0%, >=25pp 21.6%, >=30pp 15.6%, >=40pp 8.0%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.31pp; >=10pp 44.8%, >=25pp 16.9%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,868 | 28.2 | 15.5 | 27.8 | 13.4 | 10.8 | 3.7 | 0.6 | 5.84 | 15.1% | 4.3% |
| CHALLENGER | 6,691 | 16.1 | 9.8 | 20.8 | 15.3 | 15.9 | 11.4 | 10.6 | 10.83 | 37.9% | 22.0% |
| ITF_MEN | 12,297 | 9.9 | 7.3 | 16.9 | 15.2 | 21.4 | 17.4 | 12.0 | 15.26 | 50.8% | 29.4% |
| ITF_WOMEN | 17,195 | 9.5 | 7.1 | 16.1 | 15.1 | 22.1 | 18.2 | 12.0 | 15.74 | 52.3% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,934 | 17.0 | 13.0 | 24.7 | 21.2 | 16.3 | 6.8 | 1.1 | 8.68 | 24.1% | 7.9% |
| WTA125 | 1,291 | 16.0 | 7.0 | 22.6 | 20.1 | 20.4 | 12.2 | 1.8 | 10.67 | 34.3% | 13.9% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,868 | 26.8 | 15.7 | 26.1 | 15.5 | 11.5 | 3.7 | 0.8 | 6.06 | 16.0% | 4.5% |
| CHALLENGER | 6,691 | 15.0 | 9.0 | 18.6 | 14.1 | 18.5 | 13.5 | 11.3 | 12.41 | 43.2% | 24.8% |
| ITF_MEN | 12,297 | 8.1 | 6.2 | 15.1 | 13.7 | 19.8 | 20.7 | 16.3 | 17.94 | 56.9% | 37.0% |
| ITF_WOMEN | 17,195 | 7.8 | 5.8 | 14.1 | 12.8 | 20.6 | 21.2 | 17.6 | 19.06 | 59.4% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,934 | 14.3 | 10.3 | 21.9 | 16.1 | 22.1 | 12.8 | 2.6 | 11.03 | 37.5% | 15.5% |
| WTA125 | 1,291 | 10.3 | 7.3 | 16.3 | 15.7 | 24.2 | 17.4 | 8.8 | 15.14 | 50.4% | 26.3% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,868 | 22.8 | 13.9 | 25.1 | 15.6 | 15.2 | 6.2 | 1.2 | 7.3 | 22.6% | 7.4% |
| CHALLENGER | 6,691 | 15.2 | 9.6 | 21.0 | 15.6 | 15.9 | 11.9 | 10.8 | 11.15 | 38.6% | 22.7% |
| ITF_MEN | 12,297 | 9.3 | 7.2 | 17.3 | 14.3 | 22.0 | 17.5 | 12.4 | 15.71 | 51.9% | 29.9% |
| ITF_WOMEN | 17,195 | 9.3 | 6.9 | 16.4 | 15.9 | 22.2 | 18.1 | 11.3 | 15.51 | 51.5% | 29.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,934 | 23.0 | 16.7 | 32.0 | 15.0 | 9.0 | 3.3 | 1.1 | 6.12 | 13.4% | 4.4% |
| WTA125 | 1,291 | 21.4 | 13.2 | 25.8 | 18.3 | 15.2 | 5.8 | 0.3 | 8.01 | 21.3% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,283 | 26.2 | 19.7 | 30.2 | 12.4 | 8.4 | 2.6 | 0.4 | 5.4 | 11.4% | 3.1% |
| CHALLENGER | 4,324 | 22.4 | 14.5 | 27.3 | 14.6 | 13.7 | 5.9 | 1.6 | 7.09 | 21.1% | 7.4% |
| DOUBLES | 2,370 | 5.1 | 4.4 | 12.4 | 10.6 | 20.5 | 24.9 | 22.1 | 23.62 | 67.5% | 47.0% |
| ITF_MEN | 9,197 | 12.9 | 9.5 | 21.1 | 15.8 | 21.6 | 13.2 | 5.9 | 11.9 | 40.7% | 19.1% |
| ITF_WOMEN | 11,170 | 13.4 | 9.2 | 19.9 | 15.7 | 21.3 | 15.1 | 5.5 | 12.27 | 41.9% | 20.6% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,699 | 24.1 | 16.2 | 30.8 | 16.8 | 9.1 | 2.7 | 0.2 | 6.57 | 12.1% | 2.9% |
| WTA125 | 1,218 | 25.4 | 13.1 | 21.2 | 19.0 | 13.2 | 6.7 | 1.5 | 7.69 | 21.4% | 8.2% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,755 | 28.7 | 15.7 | 28.2 | 13.3 | 10.5 | 3.3 | 0.3 | 5.71 | 14.1% | 3.6% |
| CHALLENGER | 4,755 | 20.7 | 12.2 | 25.7 | 17.8 | 16.0 | 6.0 | 1.7 | 8.21 | 23.6% | 7.7% |
| ITF_MEN | 9,101 | 12.0 | 8.6 | 20.3 | 17.2 | 22.2 | 14.2 | 5.5 | 12.51 | 41.9% | 19.7% |
| ITF_WOMEN | 12,833 | 11.3 | 8.5 | 18.7 | 17.3 | 24.0 | 15.2 | 5.1 | 13.28 | 44.3% | 20.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,829 | 17.2 | 13.0 | 25.0 | 21.5 | 16.3 | 6.3 | 0.6 | 8.52 | 23.2% | 6.9% |
| WTA125 | 1,247 | 16.2 | 7.0 | 22.3 | 20.3 | 20.9 | 11.8 | 1.6 | 10.67 | 34.2% | 13.4% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,755 | 27.1 | 16.1 | 26.3 | 15.4 | 11.4 | 3.3 | 0.4 | 5.98 | 15.1% | 3.7% |
| CHALLENGER | 4,755 | 18.9 | 11.2 | 23.3 | 16.6 | 18.8 | 9.3 | 1.9 | 9.07 | 30.1% | 11.2% |
| ITF_MEN | 9,102 | 9.5 | 7.3 | 17.5 | 15.8 | 21.5 | 18.8 | 9.6 | 14.98 | 49.9% | 28.4% |
| ITF_WOMEN | 12,834 | 8.8 | 6.8 | 16.0 | 14.4 | 22.7 | 20.5 | 10.9 | 16.58 | 54.1% | 31.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,829 | 14.5 | 10.4 | 22.1 | 16.2 | 22.2 | 12.6 | 2.0 | 10.93 | 36.8% | 14.6% |
| WTA125 | 1,247 | 10.3 | 7.4 | 16.5 | 15.7 | 24.1 | 17.6 | 8.3 | 15.0 | 50.0% | 25.9% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,226 | 26.4 | 19.9 | 30.2 | 12.5 | 8.1 | 2.5 | 0.4 | 5.37 | 11.0% | 2.9% |
| CHALLENGER | 3,816 | 23.8 | 15.5 | 28.4 | 14.8 | 13.1 | 4.1 | 0.4 | 6.61 | 17.6% | 4.5% |
| DOUBLES | 2,230 | 5.0 | 4.5 | 12.6 | 10.7 | 20.3 | 24.8 | 22.1 | 23.58 | 67.2% | 46.9% |
| ITF_MEN | 7,908 | 13.7 | 10.1 | 22.7 | 16.3 | 21.5 | 11.7 | 4.0 | 11.02 | 37.2% | 15.7% |
| ITF_WOMEN | 9,582 | 14.1 | 9.7 | 21.0 | 16.3 | 21.4 | 14.1 | 3.5 | 11.46 | 39.0% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,638 | 24.5 | 16.6 | 30.8 | 16.9 | 9.1 | 2.1 | 0.1 | 6.44 | 11.3% | 2.2% |
| WTA125 | 1,083 | 26.5 | 13.8 | 22.2 | 19.9 | 12.3 | 4.8 | 0.5 | 7.2 | 17.5% | 5.3% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,370 | 5.1 | 4.4 | 12.4 | 10.6 | 20.5 | 24.9 | 22.1 | 23.62 | 67.5% | 47.0% |
| singles | 30,040 | 16.6 | 11.4 | 22.9 | 15.5 | 18.2 | 11.2 | 4.2 | 9.76 | 33.6% | 15.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 83 | 8.4 | 8.4 | 18.1 | 10.8 | 19.3 | 22.9 | 12.1 | 16.37 | 54.2% | 34.9% |
| Clay | 8,870 | 12.9 | 9.3 | 19.9 | 15.9 | 19.6 | 13.7 | 8.7 | 12.4 | 42.0% | 22.4% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 29,089 | 13.4 | 8.7 | 18.8 | 15.3 | 19.1 | 14.8 | 9.8 | 12.83 | 43.7% | 24.6% |
| UNKNOWN | 6,003 | 10.4 | 7.6 | 17.0 | 16.4 | 21.5 | 15.9 | 11.1 | 14.3 | 48.5% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 12,589 | 19.8 | 11.9 | 22.7 | 16.0 | 14.8 | 8.9 | 5.9 | 8.71 | 29.6% | 14.8% |
| B | 5,472 | 12.9 | 8.8 | 19.5 | 15.9 | 19.6 | 12.6 | 10.8 | 12.57 | 42.9% | 23.3% |
| C | 6,252 | 11.9 | 8.9 | 19.6 | 16.1 | 18.5 | 14.6 | 10.5 | 12.86 | 43.6% | 25.1% |
| D | 7,053 | 11.7 | 8.4 | 17.9 | 15.5 | 21.8 | 15.7 | 9.2 | 13.73 | 46.6% | 24.8% |
| F | 12,916 | 7.4 | 5.5 | 14.9 | 14.7 | 23.5 | 20.9 | 13.1 | 17.71 | 57.5% | 34.0% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,671 | 24.6 | 16.1 | 29.0 | 14.9 | 10.7 | 3.5 | 1.2 | 6.36 | 15.4% | 4.7% |
| B | 4,573 | 16.7 | 10.8 | 24.1 | 16.9 | 18.8 | 9.6 | 3.1 | 9.68 | 31.5% | 12.7% |
| C | 6,371 | 11.3 | 7.7 | 19.4 | 14.6 | 21.1 | 15.7 | 10.3 | 13.6 | 47.0% | 26.0% |
| D | 4,799 | 14.4 | 9.8 | 21.4 | 15.6 | 20.5 | 13.0 | 5.4 | 11.29 | 38.8% | 18.4% |
| F | 7,996 | 10.1 | 8.4 | 16.1 | 14.6 | 23.2 | 19.7 | 7.8 | 15.39 | 50.7% | 27.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 14,255 | 18.1 | 10.9 | 21.7 | 15.8 | 15.2 | 9.8 | 8.5 | 9.78 | 33.4% | 18.3% |
| LIMITED | 9,668 | 13.6 | 9.9 | 20.3 | 16.2 | 19.2 | 13.3 | 7.5 | 11.77 | 40.0% | 20.8% |
| POOR | 20,359 | 9.0 | 6.5 | 16.0 | 15.0 | 22.8 | 18.9 | 11.7 | 16.14 | 53.4% | 30.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,585 | 23.9 | 17.8 | 33.1 | 15.7 | 6.3 | 2.8 | 0.4 | 5.9 | 9.5% | 3.1% |
| GAME_SPREAD | 6,484 | 22.5 | 15.1 | 32.3 | 17.1 | 9.0 | 3.4 | 0.6 | 6.73 | 13.0% | 4.0% |
| MATCH_WINNER | 32,410 | 15.8 | 10.9 | 22.1 | 15.1 | 18.4 | 12.2 | 5.5 | 10.28 | 36.1% | 17.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 15,812 | 27.9 | 16.7 | 30.5 | 12.7 | 9.4 | 2.5 | 0.3 | 5.64 | 12.2% | 2.8% |
| TOTAL_GAMES | 10,815 | 9.9 | 10.9 | 35.4 | 26.1 | 10.5 | 4.2 | 3.0 | 9.2 | 17.7% | 7.2% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,804 | 24.5 | 28.9 | 33.3 | 8.2 | 4.0 | 1.0 | 0.3 | 4.79 | 5.2% | 1.2% |
| GAME_SPREAD | 8,988 | 46.7 | 16.2 | 24.8 | 7.5 | 2.3 | 1.9 | 0.6 | 3.31 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,069 | 6.6 | 9.8 | 40.2 | 30.2 | 7.4 | 3.4 | 2.4 | 9.22 | 13.2% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,839 | 23.9 | 16.6 | 34.8 | 14.7 | 6.9 | 2.5 | 0.5 | 6.05 | 10.0% | 3.0% |
| GAME_SPREAD | 8,997 | 20.5 | 13.5 | 28.3 | 20.1 | 12.0 | 4.5 | 1.2 | 7.64 | 17.7% | 5.7% |
| TOTAL_GAMES | 16,108 | 10.0 | 10.7 | 36.2 | 24.4 | 11.6 | 4.4 | 2.6 | 9.08 | 18.6% | 7.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 44,282 | 44.0% | 24.5% | 12.95 | 35.4% | 15.2% | 10.71 |
| gen1_elo | 44,282 | 43.8% | 24.2% | 12.73 | 35.0% | 15.1% | 10.51 |
| gen1_sr | 44,282 | 51.7% | 31.1% | 15.7 | 44.0% | 21.8% | 12.99 |
| gen2 | 44,282 | 50.7% | 31.3% | 15.35 | 43.9% | 23.3% | 12.85 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 19,722 | 15.5 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.3% | 15.3% |
| STALE | 24,560 | 10.8 | 7.3 | 16.8 | 14.1 | 19.1 | 17.0 | 14.9 | 15.41 | 51.1% | 31.9% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 25,878 | 16.5 | 11.2 | 22.7 | 15.2 | 17.9 | 11.7 | 4.8 | 9.89 | 34.4% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 76,692 | 25878 | 23194 | 27620 | 24.6 | 114.1 | 1451.1 |
| ge_15pp | 31,199 | 8892 | 8257 | 14050 | 27.6 | 419.8 | 1451.1 |
| ge_25pp | 16,579 | 4265 | 3603 | 8711 | 32.2 | 577.9 | 1431.1 |
| lt_10pp | 33,699 | 13042 | 10970 | 9687 | 22.6 | 47.3 | 1421.1 |

Current slate `SL-20261104T075307Z-de108e25`: 878 priced rows, quote age at build {'median': 18.8, 'max': 18.8}, freshness {'AGING': 878}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 49 | 0.0 | 0.0 | 36.7 | 6.1 | 32.6 | 20.4 | 4.1 | 18.34 | 57.1% | 24.5% |
| EXTERNAL_LONE_OUTLIER | 28 | 67.9 | 32.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,374 | 19.5 | 10.9 | 25.5 | 17.9 | 17.8 | 7.4 | 1.0 | 8.71 | 26.1% | 8.3% |
| KALSHI_LONE_OUTLIER | 27 | 3.7 | 3.7 | 77.8 | 7.4 | 3.7 | 3.7 | 0.0 | 6.42 | 7.4% | 3.7% |
| MARKETS_AGREE | 896 | 66.0 | 34.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.2 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,955 | 0.0 | 2.4 | 37.1 | 26.2 | 24.2 | 9.3 | 0.8 | 11.81 | 34.3% | 10.1% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 44,282 | 7329 (16.6%) | 26.7% | 1.0% | {"EXTERNAL_STALE": 4374, "AGREES_WITH_KALSHI": 1955, "ALL_AGREE": 896, "SUPPORTS_MODEL_DIRECTION": 48, "EXTERNAL_OUTLIER": 28, "AGREES_WITH_MODEL": 27, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 19,508 | 1844 (9.4%) | 36.4% | 1.6% | {"EXTERNAL_STALE": 1143, "AGREES_WITH_KALSHI": 671, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 10,852 | 575 (5.3%) | 34.3% | 2.3% | {"EXTERNAL_STALE": 365, "AGREES_WITH_KALSHI": 197, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,255 | 546 (10.4%) | 34.8% | 2.4% | {"EXTERNAL_STALE": 343, "AGREES_WITH_KALSHI": 190, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 17,888 | 4183 (23.4%) | 18.5% | 1.0% | {"EXTERNAL_STALE": 2446, "ALL_AGREE": 896, "AGREES_WITH_KALSHI": 772, "EXTERNAL_OUTLIER": 28, "AGREES_WITH_MODEL": 23, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 8,605 | 10.4 | 7.7 | 19.4 | 14.8 | 21.7 | 16.1 | 9.8 | 14.0 | 47.6% | 25.9% |
| 4-10x | 5,908 | 11.1 | 8.5 | 18.7 | 15.4 | 22.1 | 14.2 | 10.0 | 13.7 | 46.3% | 24.2% |
| <2x | 22,722 | 15.1 | 9.8 | 19.8 | 16.2 | 17.4 | 13.0 | 8.7 | 11.48 | 39.1% | 21.7% |
| >=10x | 7,047 | 10.4 | 6.3 | 15.0 | 14.5 | 21.6 | 19.1 | 13.0 | 16.42 | 53.8% | 32.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 11,520 | 12.6 | 8.8 | 19.8 | 16.4 | 19.0 | 13.3 | 10.0 | 12.61 | 42.4% | 23.4% |
| 300-1000 | 9,528 | 11.8 | 8.8 | 17.8 | 15.5 | 20.6 | 16.1 | 9.4 | 13.57 | 46.1% | 25.5% |
| <300 | 13,974 | 8.2 | 5.8 | 15.1 | 14.8 | 23.1 | 20.0 | 13.0 | 17.12 | 56.1% | 33.0% |
| >=3000 | 9,260 | 21.4 | 12.9 | 24.1 | 15.7 | 13.7 | 7.1 | 4.9 | 7.65 | 25.7% | 12.0% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1294 | 0.5481 | 0.4084 | 0.4907 | +0.057 | -0.082 | -0.0007 ± 0.0043 |
| ratio 4-10x | 889 | 0.5821 | 0.4354 | 0.4904 | +0.092 | -0.055 | 0.0094 ± 0.0054 |
| ratio <2x | 3183 | 0.5367 | 0.4142 | 0.442 | +0.095 | -0.028 | 0.013 ± 0.0025 |
| ratio >=10x | 1083 | 0.5695 | 0.3955 | 0.4497 | +0.120 | -0.054 | 0.0159 ± 0.0055 |
| thinner_sample 1000-3000 | 1780 | 0.5385 | 0.4118 | 0.4522 | +0.086 | -0.041 | 0.0089 ± 0.0034 |
| thinner_sample 300-1000 | 1457 | 0.5675 | 0.4261 | 0.4839 | +0.084 | -0.058 | 0.0029 ± 0.0041 |
| thinner_sample <300 | 2110 | 0.5608 | 0.3923 | 0.4555 | +0.105 | -0.063 | 0.0137 ± 0.0039 |
| thinner_sample >=3000 | 1102 | 0.5291 | 0.4362 | 0.4483 | +0.081 | -0.012 | 0.0155 ± 0.0034 |
| data_status ADEQUATE | 1803 | 0.5312 | 0.4288 | 0.4426 | +0.089 | -0.014 | 0.0139 ± 0.0029 |
| data_status LIMITED | 1560 | 0.5486 | 0.4156 | 0.4705 | +0.078 | -0.055 | 0.0066 ± 0.0038 |
| data_status POOR | 3086 | 0.5632 | 0.4021 | 0.4644 | +0.099 | -0.062 | 0.01 ± 0.0031 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 942 | 0.1992 | 0.1997 | -0.0005 ± 0.0005 | 0.5787 | 0.5799 | 0.5017 | 0.4866 | 0.5053 | -0.091 ± 0.0154 | -0.0087 (8) |
| 3-5 | 590 | 0.2044 | 0.2039 | +0.0005 ± 0.0015 | 0.5917 | 0.5886 | 0.5026 | 0.4627 | 0.4763 | -0.105 ± 0.0191 | 0.01 (2) |
| 5-10 | 1371 | 0.2007 | 0.2006 | +0.0001 ± 0.0018 | 0.587 | 0.5846 | 0.5126 | 0.4389 | 0.4719 | -0.089 ± 0.0126 | -0.0143 (7) |
| 10-15 | 1123 | 0.2206 | 0.2107 | +0.0098 ± 0.0034 | 0.6341 | 0.6058 | 0.5262 | 0.4027 | 0.4239 | -0.111 ± 0.0139 | -0.048 (5) |
| 15-25 | 1431 | 0.2249 | 0.2089 | +0.0160 ± 0.0047 | 0.6445 | 0.6013 | 0.5762 | 0.3811 | 0.4382 | -0.106 ± 0.0121 | -0.004 (10) |
| 25-40 | 817 | 0.2207 | 0.2062 | +0.0145 ± 0.0095 | 0.6301 | 0.5941 | 0.6554 | 0.3453 | 0.4774 | -0.071 ± 0.0144 | -0.06 (2) |
| 40+ | 175 | 0.2937 | 0.1769 | +0.1168 ± 0.0284 | 0.7931 | 0.5276 | 0.7355 | 0.2823 | 0.3886 | -0.087 ± 0.0276 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5013 | 0.1852 | 0.1861 | -0.0009 ± 0.0002 | 0.5456 | 0.5466 | 0.4863 | 0.4711 | 0.5023 | -0.022 ± 0.0062 | -0.01 (28) |
| 3-5 | 3350 | 0.1965 | 0.1949 | +0.0016 ± 0.0006 | 0.5718 | 0.5656 | 0.4808 | 0.441 | 0.44 | -0.056 ± 0.0077 | 0.0 (3) |
| 5-10 | 7223 | 0.2007 | 0.1978 | +0.0030 ± 0.0008 | 0.5868 | 0.5764 | 0.4851 | 0.4115 | 0.4282 | -0.043 ± 0.0053 | -0.0114 (22) |
| 10-15 | 6011 | 0.2026 | 0.1865 | +0.0161 ± 0.0014 | 0.5921 | 0.5472 | 0.4859 | 0.362 | 0.3588 | -0.065 ± 0.0056 | -0.0281 (16) |
| 15-25 | 7500 | 0.2066 | 0.1675 | +0.0391 ± 0.0019 | 0.6054 | 0.4973 | 0.4998 | 0.3042 | 0.3028 | -0.071 ± 0.0047 | -0.0027 (45) |
| 25-40 | 5781 | 0.2221 | 0.1265 | +0.0956 ± 0.0029 | 0.6382 | 0.3886 | 0.5269 | 0.2131 | 0.2221 | -0.058 ± 0.0045 | -0.0733 (3) |
| 40+ | 3823 | 0.3834 | 0.0453 | +0.3381 ± 0.0039 | 0.9985 | 0.1747 | 0.6326 | 0.1042 | 0.0607 | -0.077 ± 0.0033 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 754 | 0.2064 | 0.2071 | -0.0006 ± 0.0006 | 0.5949 | 0.5967 | 0.5043 | 0.4896 | 0.5212 | -0.097 ± 0.0179 | -0.0117 (6) |
| 3-5 | 529 | 0.213 | 0.2104 | +0.0027 ± 0.0016 | 0.6079 | 0.6028 | 0.5114 | 0.4717 | 0.4537 | -0.131 ± 0.0214 | 0.01 (2) |
| 5-10 | 1183 | 0.2064 | 0.2038 | +0.0026 ± 0.002 | 0.5991 | 0.5913 | 0.5406 | 0.4659 | 0.4886 | -0.098 ± 0.0135 | -0.01 (4) |
| 10-15 | 1040 | 0.2137 | 0.2085 | +0.0052 ± 0.0035 | 0.6191 | 0.6035 | 0.5652 | 0.4409 | 0.4856 | -0.100 ± 0.0148 | -0.04 (5) |
| 15-25 | 1501 | 0.2315 | 0.2121 | +0.0194 ± 0.0047 | 0.6577 | 0.6083 | 0.5846 | 0.3893 | 0.4397 | -0.104 ± 0.0121 | -0.012 (10) |
| 25-40 | 1057 | 0.2689 | 0.1996 | +0.0693 ± 0.0086 | 0.7495 | 0.5802 | 0.6612 | 0.3476 | 0.3964 | -0.127 ± 0.0137 | -0.008 (5) |
| 40+ | 385 | 0.3677 | 0.163 | +0.2047 ± 0.0205 | 1.0021 | 0.4923 | 0.7345 | 0.2472 | 0.2961 | -0.086 ± 0.0197 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4324 | 0.1919 | 0.1923 | -0.0004 ± 0.0002 | 0.5595 | 0.5602 | 0.5073 | 0.4923 | 0.5134 | -0.035 ± 0.0069 | -0.0154 (26) |
| 3-5 | 2939 | 0.1927 | 0.1918 | +0.0009 ± 0.0006 | 0.5612 | 0.5582 | 0.51 | 0.4703 | 0.4781 | -0.044 ± 0.0083 | 0.01 (2) |
| 5-10 | 6441 | 0.1978 | 0.1941 | +0.0037 ± 0.0008 | 0.5802 | 0.5671 | 0.507 | 0.433 | 0.4478 | -0.043 ± 0.0056 | -0.0117 (6) |
| 10-15 | 5372 | 0.2029 | 0.192 | +0.0110 ± 0.0015 | 0.5955 | 0.5615 | 0.5127 | 0.3888 | 0.4073 | -0.048 ± 0.0061 | -0.0189 (18) |
| 15-25 | 7491 | 0.2177 | 0.1811 | +0.0366 ± 0.0019 | 0.6325 | 0.5312 | 0.5238 | 0.3286 | 0.3357 | -0.063 ± 0.005 | -0.0084 (43) |
| 25-40 | 6817 | 0.2516 | 0.138 | +0.1136 ± 0.0029 | 0.7093 | 0.4215 | 0.5601 | 0.2435 | 0.2258 | -0.083 ± 0.0045 | -0.0095 (20) |
| 40+ | 5317 | 0.4012 | 0.0598 | +0.3415 ± 0.0039 | 1.0576 | 0.2148 | 0.6548 | 0.1195 | 0.0822 | -0.074 ± 0.0033 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 908 | 0.1963 | 0.1979 | -0.0017 ± 0.0005 | 0.5719 | 0.5762 | 0.5014 | 0.486 | 0.5363 | -0.049 ± 0.0154 | -0.012 (10) |
| 3-5 | 637 | 0.208 | 0.2065 | +0.0015 ± 0.0015 | 0.6008 | 0.595 | 0.497 | 0.4574 | 0.46 | -0.115 ± 0.0188 | -0.0 (4) |
| 5-10 | 1413 | 0.2024 | 0.199 | +0.0033 ± 0.0018 | 0.5899 | 0.5801 | 0.512 | 0.4382 | 0.4508 | -0.107 ± 0.0123 | -0.01 (9) |
| 10-15 | 1127 | 0.2108 | 0.2041 | +0.0068 ± 0.0033 | 0.6121 | 0.5915 | 0.5394 | 0.4163 | 0.4516 | -0.103 ± 0.0135 | -0.0286 (7) |
| 15-25 | 1355 | 0.2316 | 0.2133 | +0.0183 ± 0.0049 | 0.6609 | 0.6106 | 0.589 | 0.3944 | 0.4443 | -0.114 ± 0.0125 | -0.03 (1) |
| 25-40 | 825 | 0.2116 | 0.2105 | +0.0011 ± 0.0094 | 0.6109 | 0.6044 | 0.6632 | 0.3521 | 0.5042 | -0.058 ± 0.0143 | -0.0267 (3) |
| 40+ | 184 | 0.3097 | 0.1845 | +0.1252 ± 0.0284 | 0.8397 | 0.5449 | 0.746 | 0.2915 | 0.3913 | -0.092 ± 0.0292 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4819 | 0.1837 | 0.1844 | -0.0007 ± 0.0002 | 0.5412 | 0.5423 | 0.482 | 0.4666 | 0.4877 | -0.030 ± 0.0063 | -0.0137 (41) |
| 3-5 | 3416 | 0.204 | 0.2023 | +0.0017 ± 0.0006 | 0.5916 | 0.5856 | 0.4808 | 0.4413 | 0.4406 | -0.056 ± 0.0078 | -0.01 (19) |
| 5-10 | 7420 | 0.1959 | 0.191 | +0.0048 ± 0.0008 | 0.5749 | 0.5595 | 0.4875 | 0.4136 | 0.4179 | -0.054 ± 0.0051 | -0.0105 (37) |
| 10-15 | 5902 | 0.1934 | 0.1793 | +0.0141 ± 0.0014 | 0.5714 | 0.5305 | 0.495 | 0.3717 | 0.3755 | -0.059 ± 0.0055 | -0.0146 (13) |
| 15-25 | 7595 | 0.2123 | 0.1726 | +0.0397 ± 0.0019 | 0.619 | 0.5089 | 0.5142 | 0.3195 | 0.316 | -0.072 ± 0.0048 | -0.0533 (3) |
| 25-40 | 5769 | 0.2169 | 0.1278 | +0.0891 ± 0.003 | 0.6269 | 0.3916 | 0.5301 | 0.2145 | 0.2333 | -0.050 ± 0.0045 | -0.02 (4) |
| 40+ | 3780 | 0.393 | 0.0508 | +0.3422 ± 0.0041 | 1.0245 | 0.1888 | 0.6421 | 0.1106 | 0.0677 | -0.077 ± 0.0035 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1331 | 0.196 | 0.196 | +0.0000 ± 0.0004 | 0.5699 | 0.5697 | 0.5059 | 0.491 | 0.4921 | -0.072 ± 0.0124 | -0.0213 (54) |
| 3-5 | 937 | 0.1894 | 0.1891 | +0.0003 ± 0.0011 | 0.5563 | 0.5543 | 0.4951 | 0.4552 | 0.4696 | -0.061 ± 0.0145 | -0.0194 (34) |
| 5-10 | 1922 | 0.2006 | 0.1958 | +0.0049 ± 0.0015 | 0.5896 | 0.5742 | 0.5057 | 0.4321 | 0.436 | -0.078 ± 0.0103 | -0.005 (78) |
| 10-15 | 1322 | 0.2162 | 0.2031 | +0.0132 ± 0.0031 | 0.6254 | 0.59 | 0.5395 | 0.4166 | 0.4228 | -0.093 ± 0.0128 | 0.0014 (65) |
| 15-25 | 1695 | 0.2304 | 0.2075 | +0.0229 ± 0.0044 | 0.6576 | 0.599 | 0.5883 | 0.3935 | 0.4354 | -0.089 ± 0.0112 | -0.0214 (59) |
| 25-40 | 1053 | 0.2416 | 0.2096 | +0.0319 ± 0.0086 | 0.6901 | 0.6019 | 0.6867 | 0.3745 | 0.4796 | -0.091 ± 0.0132 | -0.0252 (27) |
| 40+ | 367 | 0.3254 | 0.2026 | +0.1228 ± 0.0225 | 0.9414 | 0.5896 | 0.8171 | 0.34 | 0.4659 | -0.095 ± 0.0209 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4919 | 0.1759 | 0.1761 | -0.0002 ± 0.0002 | 0.5208 | 0.5208 | 0.5114 | 0.4962 | 0.5064 | -0.039 ± 0.006 | -0.0145 (98) |
| 3-5 | 3366 | 0.1945 | 0.1935 | +0.0010 ± 0.0006 | 0.567 | 0.5646 | 0.5011 | 0.4613 | 0.4685 | -0.044 ± 0.0077 | -0.0204 (72) |
| 5-10 | 6858 | 0.1976 | 0.1909 | +0.0067 ± 0.0008 | 0.5813 | 0.562 | 0.5004 | 0.4267 | 0.4198 | -0.064 ± 0.0053 | -0.0084 (134) |
| 10-15 | 4730 | 0.2104 | 0.1943 | +0.0161 ± 0.0016 | 0.6115 | 0.5698 | 0.5371 | 0.4141 | 0.4089 | -0.072 ± 0.0065 | -0.0053 (106) |
| 15-25 | 5689 | 0.2299 | 0.1996 | +0.0304 ± 0.0023 | 0.6613 | 0.5783 | 0.574 | 0.3786 | 0.4001 | -0.066 ± 0.006 | -0.026 (108) |
| 25-40 | 3822 | 0.2581 | 0.1891 | +0.0690 ± 0.0044 | 0.7303 | 0.5514 | 0.6383 | 0.3257 | 0.3741 | -0.071 ± 0.0069 | -0.0246 (52) |
| 40+ | 1662 | 0.3713 | 0.1572 | +0.2141 ± 0.0101 | 1.0495 | 0.4687 | 0.7435 | 0.2423 | 0.29 | -0.067 ± 0.0092 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 6449 | 1.028 ± 0.035 | 1.107 | 0.1691 | 0.167 | 0.2147 | 0.2045 |
| gen2 | 6449 | 0.817 ± 0.032 | 1.075 | 0.1729 | 0.1673 | 0.2338 | 0.2043 |
| gen1_elo | 6449 | 1.005 ± 0.034 | 1.098 | 0.1758 | 0.1671 | 0.2139 | 0.2045 |
| gen1_sr | 6449 | 1.003 ± 0.041 | 1.133 | 0.1329 | 0.1691 | 0.2298 | 0.204 |
| gen1_ledger | 8627 | 0.865 ± 0.025 | 1.073 | 0.189 | 0.1757 | 0.2172 | 0.2005 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 31,199)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 7,173 | 23.0% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,843 | 21.9% |
| BOOK_QUALITY | execution | 5,772 | 18.5% |
| POOR_DATA | data | 3,690 | 11.8% |
| LIMITED_DATA | data | 1,970 | 6.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,744 | 5.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,325 | 4.2% |
| IDENTITY_AMBIGUOUS | mapping | 1,286 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 875 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 520 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 23.0%, coverage 21.9%, execution 18.5%, data 18.1%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.2%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.4%, LOW_DATA_QUALITY 71.6%, THIN_PLAYER_HISTORY 60.1%, STALE_PLAYER_DATA 52.3%, STALE_KALSHI_QUOTE 45.0%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 24.7%, MODEL_HIGH_UNCERTAINTY 18.5%, PLAYER_IDENTITY_RISK 15.5%, LEVEL_TRANSFER_RISK 10.2%, LOW_DISPLAYED_LIQUIDITY 8.3%, EVENT_MAPPING_RISK 7.3%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.3%, POST_SETTLEMENT_OBSERVATION 21.9%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 16,579)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,515 | 33.3% |
| STALE_QUOTE | market_freshness | 3,241 | 19.6% |
| BOOK_QUALITY | execution | 3,001 | 18.1% |
| POOR_DATA | data | 1,588 | 9.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 921 | 5.6% |
| IDENTITY_AMBIGUOUS | mapping | 706 | 4.3% |
| LIMITED_DATA | data | 577 | 3.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 572 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 329 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 128 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.3%, market_freshness 19.6%, execution 18.1%, data 13.1%, market_freshness/coverage 9.0%, mapping 4.3%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 96.9%, LOW_DATA_QUALITY 75.1%, THIN_PLAYER_HISTORY 62.2%, STALE_KALSHI_QUOTE 52.5%, STALE_PLAYER_DATA 46.4%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 24.2%, MODEL_HIGH_UNCERTAINTY 19.1%, PLAYER_IDENTITY_RISK 18.5%, LEVEL_TRANSFER_RISK 9.1%, EVENT_MAPPING_RISK 9.0%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 5.0%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.3%, POST_SETTLEMENT_OBSERVATION 33.3%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 13184, "IDENTITY_AMBIGUOUS": 3395}; ticker orientation: {"VERIFIED": 16579}.

Checks: discipline:AMBIGUOUS 1115, discipline:PASS 15464, identity_confidence:AMBIGUOUS 3071, identity_confidence:PASS 13508, level_mapping:NA 1127, level_mapping:PASS 15452, market_pair:AMBIGUOUS 485, market_pair:NA 365, market_pair:PASS 15729, model_complement:NA 328, model_complement:PASS 16251, namesake:AMBIGUOUS 6, namesake:PASS 16573, physical_match_id:NA 5727, physical_match_id:PASS 10852, player_ids:PASS 16579, same_pair_other_event:PASS 16579, ticker_orientation:PASS 16579

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,151 | 3.9% | 3.3% | 1.4% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 21, "market_freshness/coverage": 17} | 5.56 | 0.2227 / 0.2169 (751) | 24.2% | 2.5% | 3.1% | 2.8% |
| CHALLENGER | 11,015 | 16.3% | 6.2% | 10.8% | {"coverage": 1045, "market_freshness/coverage": 213, "market_freshness": 209, "data": 157, "model_calibration_or_unknown": 76, "execution": 41, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.37 | 0.2208 / 0.2101 (2562) | 37.1% | 15.8% | 4.2% | 22.2% |
| DOUBLES | 2,370 | 47.0% | 46.9% | 6.7% | {"execution": 641, "mapping": 300, "market_freshness": 106, "market_freshness/coverage": 61, "coverage": 7} | 23.58 | 0.304 / 0.2381 (555) | 9.9% | 0.0% | 100.0% | 5.9% |
| ITF_MEN | 21,494 | 25.0% | 17.8% | 32.4% | {"coverage": 1826, "market_freshness": 1040, "execution": 956, "data": 821, "market_freshness/coverage": 514, "mapping": 202, "model_calibration": 6, "model_calibration_or_unknown": 4} | 11.81 | 0.2173 / 0.1993 (4411) | 38.7% | 69.2% | 15.9% | 20.9% |
| ITF_WOMEN | 28,365 | 26.4% | 19.2% | 45.2% | {"coverage": 2564, "market_freshness": 1637, "execution": 1280, "data": 1086, "market_freshness/coverage": 632, "mapping": 181, "model_calibration_or_unknown": 89, "model_calibration": 22} | 12.55 | 0.2026 / 0.194 (5294) | 40.1% | 57.4% | 9.8% | 21.0% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,633 | 6.1% | 5.2% | 1.7% | {"market_freshness": 105, "model_calibration_or_unknown": 52, "coverage": 37, "execution": 29, "data": 24, "model_calibration": 20, "market_freshness/coverage": 13, "mapping": 1} | 7.7 | 0.2298 / 0.2234 (735) | 29.2% | 2.1% | 1.3% | 3.6% |
| WTA125 | 2,509 | 11.2% | 9.6% | 1.7% | {"market_freshness": 85, "model_calibration_or_unknown": 53, "market_freshness/coverage": 42, "data": 41, "execution": 24, "model_calibration": 17, "coverage": 14, "mapping": 4} | 9.17 | 0.208 / 0.1906 (726) | 28.4% | 10.8% | 4.3% | 7.1% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 16.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 969 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 852 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.5h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 517 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 9 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 10 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 547 min (STALE); no external reference |
| 13 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 14 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 17 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 18 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 19 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 20 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 21 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 22 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 23 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 24 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 25 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 26 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 27 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 28 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 29 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 30 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 31 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 365 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 32 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 33 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 34 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 35 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 36 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 37 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 38 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 39 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 40 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 41 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 42 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 43 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 44 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 720 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 45 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 46 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.3h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 748 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |
| 47 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXATPCHALLENGERMATCH-26NOV02TOBSTO-TOB` | CHALLENGER | fair_v1 | 80% / 2% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 165 min (STALE); data POOR (grade F, thinner serve sample 159.0, ratio 20.58); no external reference |
| 49 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 50 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9687, "by_level_share_of_ge_25pp": {"ATP": 0.0143, "CHALLENGER": 0.1082, "DOUBLES": 0.0673, "ITF_MEN": 0.3238, "ITF_WOMEN": 0.4518, "OTHER": 0.0007, "WTA": 0.0169, "WTA125": 0.0169}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5254, "share_primary_cause_market_settled_or_in_play": 0.4227, "share_primary_cause_stale_quote_only": 0.1955}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 16579, "identity_ambiguous_share": 0.2048, "ticker_orientation": {"VERIFIED": 16579}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 10852, "with_external": 575, "coverage": 0.053, "external_status": {"EXTERNAL_STALE": 365, "AGREES_WITH_KALSHI": 197, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 365, "MODEL_LONE_OUTLIER": 197, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3426, "share_external_supports_model": 0.0226}, "pregame_clean_ge_25pp": {"n": 5255, "with_external": 546, "coverage": 0.1039, "external_status": {"EXTERNAL_STALE": 343, "AGREES_WITH_KALSHI": 190, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 343, "MODEL_LONE_OUTLIER": 190, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.348, "share_external_supports_model": 0.0238}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 476.0, "median_sample_ratio": 2.47, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2095, "data_status": {"POOR": 9361, "LIMITED": 4299, "ADEQUATE": 2919}, "comparison_lt_10pp": {"median_thinner_serve_points": 1736.0, "median_sample_ratio": 1.69, "median_min_matches": 90.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1294, "model_minus_observed": 0.0574, "kalshi_minus_observed": -0.0823, "brier_diff_model_minus_kalshi": -0.0007}, "4-10x": {"n": 889, "model_minus_observed": 0.0916, "kalshi_minus_observed": -0.0551, "brier_diff_model_minus_kalshi": 0.0094}, "<2x": {"n": 3183, "model_minus_observed": 0.0946, "kalshi_minus_observed": -0.0279, "brier_diff_model_minus_kalshi": 0.013}, ">=10x": {"n": 1083, "model_minus_observed": 0.1198, "kalshi_minus_observed": -0.0542, "brier_diff_model_minus_kalshi": 0.0159}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 6449, "model": {"intercept": -0.548, "slope": 0.817, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.187, "slope": 1.075, "slope_se": 0.036}, "mean_extremity_model": 0.1729, "mean_extremity_kalshi": 0.1673, "model_brier": 0.2338, "kalshi_brier": 0.2043, "brier_diff_model_minus_kalshi": 0.0296, "brier_diff_se": 0.0024, "model_logloss": 0.6649, "kalshi_logloss": 0.591}, "fair_v1": {"n": 6449, "model": {"intercept": -0.436, "slope": 1.028, "slope_se": 0.035}, "kalshi_mid_same_rows": {"intercept": 0.264, "slope": 1.107, "slope_se": 0.036}, "mean_extremity_model": 0.1691, "mean_extremity_kalshi": 0.167, "model_brier": 0.2147, "kalshi_brier": 0.2045, "brier_diff_model_minus_kalshi": 0.0103, "brier_diff_se": 0.0019, "model_logloss": 0.6183, "kalshi_logloss": 0.5913}, "gen1_elo": {"n": 6449, "model": {"intercept": -0.422, "slope": 1.005, "slope_se": 0.034}, "kalshi_mid_same_rows": {"intercept": 0.269, "slope": 1.098, "slope_se": 0.035}, "mean_extremity_model": 0.1758, "mean_extremity_kalshi": 0.1671, "model_brier": 0.2139, "kalshi_brier": 0.2045, "brier_diff_model_minus_kalshi": 0.0094, "brier_diff_se": 0.0019, "model_logloss": 0.6171, "kalshi_logloss": 0.5915}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2451, "share_ge_15": 0.4405, "median_abs_gap": 12.95, "n": 44282}, "gen1_elo": {"share_ge_25": 0.2425, "share_ge_15": 0.4376, "median_abs_gap": 12.73, "n": 44282}, "gen1_sr": {"share_ge_25": 0.3108, "share_ge_15": 0.5173, "median_abs_gap": 15.7, "n": 44282}, "gen2": {"share_ge_25": 0.3129, "share_ge_15": 0.5075, "median_abs_gap": 15.35, "n": 44282}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1522, "share_ge_15": 0.3543, "median_abs_gap": 10.71, "n": 34526}, "gen1_elo": {"share_ge_25": 0.1509, "share_ge_15": 0.3502, "median_abs_gap": 10.51, "n": 34526}, "gen1_sr": {"share_ge_25": 0.2175, "share_ge_15": 0.4395, "median_abs_gap": 12.99, "n": 34528}, "gen2": {"share_ge_25": 0.2327, "share_ge_15": 0.4391, "median_abs_gap": 12.85, "n": 34528}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.56, "share_ge_25_all": 0.0385, "share_ge_25_pregame_clean": 0.0333}, "WTA": {"median_abs_gap_pregame_clean": 7.7, "share_ge_25_all": 0.0607, "share_ge_25_pregame_clean": 0.0517}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2375, "share_within_10pp_all": 0.4394, "share_within_10pp_pregame_clean": 0.4905, "corr_model_vs_mid_pregame_clean": 0.8499}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 942, "model_brier": 0.1992, "kalshi_brier": 0.1997, "brier_diff_model_minus_kalshi": -0.0005}, "10-15": {"n_settled": 1123, "model_brier": 0.2206, "kalshi_brier": 0.2107, "brier_diff_model_minus_kalshi": 0.0098}, "15-25": {"n_settled": 1431, "model_brier": 0.2249, "kalshi_brier": 0.2089, "brier_diff_model_minus_kalshi": 0.016}, "25-40": {"n_settled": 817, "model_brier": 0.2207, "kalshi_brier": 0.2062, "brier_diff_model_minus_kalshi": 0.0145}, "3-5": {"n_settled": 590, "model_brier": 0.2044, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0005}, "40+": {"n_settled": 175, "model_brier": 0.2937, "kalshi_brier": 0.1769, "brier_diff_model_minus_kalshi": 0.1168}, "5-10": {"n_settled": 1371, "model_brier": 0.2007, "kalshi_brier": 0.2006, "brier_diff_model_minus_kalshi": 0.0001}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.548, "slope": 0.817, "slope_se": 0.032}, "kalshi_slope": {"intercept": 0.187, "slope": 1.075, "slope_se": 0.036}, "n": 6449}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.491, "slope": 0.865, "slope_se": 0.025}, "kalshi_slope": {"intercept": 0.169, "slope": 1.073, "slope_se": 0.03}, "n": 8627}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 555, "model_brier": 0.304, "kalshi_brier": 0.2381, "brier_diff_model_minus_kalshi": 0.0659, "brier_diff_se": 0.0127, "corr_model_outcome": 0.0736, "corr_kalshi_outcome": 0.2361}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
