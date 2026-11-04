# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-04T17:06Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 77,595): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.4%, 15-25 19.1%, 25-40 13.7%, 40+ 8.0%; median gap 11.82 pp.
* **Where the extremes live**: 96.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.7%, Challenger 10.8%, doubles 6.7%). Main tour: ATP 3.8% and WTA 6.1% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 16,818): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.4%, STALE_QUOTE 19.7%, BOOK_QUALITY 17.9%, POOR_DATA 9.5%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IDENTITY_AMBIGUOUS 4.3%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.4%, market_freshness 19.7%, execution 17.9%, data 13.0%, market_freshness/coverage 9.0%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 16,818 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.4% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.6% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 476.0 points vs 1732.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.041, Gen-2 0.833, Gen-1 ledger 0.871 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 842 model 0.2209 vs Kalshi 0.2045; n 180 model 0.2928 vs Kalshi 0.1795.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 332,129 model-market comparisons (542,215 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 110,566 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-04T16:50:25.328165+00:00'], shadow board 89,170 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-04T16:50:29.335566+00:00'], Model 4 41,760 rows, 27,210 settled tickers, 10,240 tickers with an external scan.
* By model: {"gen1_ledger": 74680, "gen1_elo": 44811, "fair_v1": 44811, "gen2": 44811, "gen1_sr": 44811, "model4_fundamental": 39144, "model4_conditioned": 39061}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 77,595 | 14.1 | 9.6 | 20.2 | 15.4 | 19.1 | 13.7 | 8.0 | 11.82 | 40.8% | 21.7% |
| MW fair_v1 | 44,811 | 12.9 | 8.7 | 18.8 | 15.5 | 19.6 | 14.8 | 9.8 | 13.0 | 44.2% | 24.6% |
| MW gen1_elo | 44,811 | 12.6 | 8.8 | 19.3 | 15.4 | 19.5 | 14.7 | 9.7 | 12.76 | 43.8% | 24.3% |
| MW gen1_ledger | 32,784 | 15.8 | 10.9 | 22.1 | 15.2 | 18.4 | 12.1 | 5.5 | 10.29 | 36.1% | 17.7% |
| MW gen1_sr | 44,811 | 10.2 | 7.3 | 16.8 | 13.9 | 20.6 | 18.7 | 12.5 | 15.74 | 51.9% | 31.2% |
| MW gen2 | 44,811 | 11.1 | 7.6 | 16.7 | 13.8 | 19.5 | 17.7 | 13.6 | 15.38 | 50.8% | 31.4% |
| all families model4_conditioned | 39,061 | 22.2 | 18.1 | 34.1 | 17.1 | 5.0 | 2.2 | 1.2 | 6.06 | 8.5% | 3.4% |
| all families model4_fundamental | 39,144 | 17.4 | 13.5 | 33.8 | 19.9 | 10.0 | 3.8 | 1.5 | 7.63 | 15.4% | 5.3% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.1%, >=15pp 40.8%, >=20pp 30.0%, >=25pp 21.7%, >=30pp 15.6%, >=40pp 8.0%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.33pp; >=10pp 44.9%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,885 | 28.3 | 15.5 | 27.7 | 13.5 | 10.7 | 3.7 | 0.6 | 5.84 | 15.0% | 4.3% |
| CHALLENGER | 6,759 | 16.0 | 9.9 | 20.8 | 15.3 | 16.0 | 11.3 | 10.7 | 10.86 | 38.0% | 22.0% |
| ITF_MEN | 12,486 | 9.9 | 7.3 | 16.9 | 15.1 | 21.3 | 17.3 | 12.1 | 15.29 | 50.8% | 29.4% |
| ITF_WOMEN | 17,412 | 9.5 | 7.1 | 16.0 | 15.0 | 22.1 | 18.3 | 12.0 | 15.78 | 52.4% | 30.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,955 | 16.9 | 13.1 | 24.7 | 21.1 | 16.3 | 6.8 | 1.1 | 8.68 | 24.3% | 8.0% |
| WTA125 | 1,308 | 15.8 | 7.0 | 22.7 | 19.9 | 20.6 | 12.3 | 1.8 | 10.7 | 34.6% | 14.1% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,885 | 26.8 | 15.7 | 26.0 | 15.4 | 11.5 | 3.7 | 0.8 | 6.06 | 16.0% | 4.5% |
| CHALLENGER | 6,759 | 15.0 | 9.0 | 18.6 | 14.1 | 18.6 | 13.4 | 11.3 | 12.43 | 43.3% | 24.8% |
| ITF_MEN | 12,486 | 8.1 | 6.2 | 15.2 | 13.7 | 19.8 | 20.7 | 16.4 | 17.94 | 56.8% | 37.1% |
| ITF_WOMEN | 17,412 | 7.8 | 5.8 | 14.1 | 12.8 | 20.5 | 21.2 | 17.6 | 19.1 | 59.4% | 38.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,955 | 14.2 | 10.2 | 21.9 | 15.9 | 22.1 | 13.0 | 2.6 | 11.09 | 37.7% | 15.6% |
| WTA125 | 1,308 | 10.2 | 7.2 | 16.5 | 15.4 | 24.2 | 17.4 | 9.0 | 15.21 | 50.7% | 26.5% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,885 | 22.9 | 13.9 | 25.1 | 15.6 | 15.1 | 6.2 | 1.2 | 7.26 | 22.5% | 7.4% |
| CHALLENGER | 6,759 | 15.2 | 9.5 | 20.9 | 15.7 | 16.0 | 11.9 | 10.8 | 11.2 | 38.7% | 22.7% |
| ITF_MEN | 12,486 | 9.4 | 7.1 | 17.2 | 14.3 | 22.0 | 17.4 | 12.5 | 15.73 | 52.0% | 30.0% |
| ITF_WOMEN | 17,412 | 9.3 | 6.9 | 16.3 | 15.9 | 22.2 | 18.2 | 11.3 | 15.55 | 51.6% | 29.5% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,955 | 22.9 | 16.9 | 31.8 | 15.0 | 8.9 | 3.4 | 1.1 | 6.12 | 13.4% | 4.4% |
| WTA125 | 1,308 | 21.2 | 13.2 | 25.8 | 18.7 | 15.0 | 5.7 | 0.3 | 8.01 | 21.0% | 6.0% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,291 | 26.3 | 19.7 | 30.2 | 12.4 | 8.3 | 2.6 | 0.4 | 5.4 | 11.4% | 3.1% |
| CHALLENGER | 4,361 | 22.3 | 14.6 | 27.4 | 14.6 | 13.6 | 5.8 | 1.6 | 7.1 | 21.1% | 7.4% |
| DOUBLES | 2,399 | 5.1 | 4.4 | 12.5 | 10.6 | 20.5 | 24.9 | 22.1 | 23.61 | 67.4% | 46.9% |
| ITF_MEN | 9,321 | 12.9 | 9.5 | 21.1 | 15.8 | 21.5 | 13.2 | 6.0 | 11.91 | 40.7% | 19.2% |
| ITF_WOMEN | 11,317 | 13.4 | 9.2 | 19.9 | 15.7 | 21.4 | 15.1 | 5.5 | 12.3 | 41.9% | 20.6% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,711 | 24.2 | 16.1 | 30.9 | 16.7 | 9.2 | 2.7 | 0.2 | 6.57 | 12.1% | 2.9% |
| WTA125 | 1,235 | 25.3 | 13.0 | 21.5 | 19.0 | 13.1 | 6.6 | 1.5 | 7.71 | 21.2% | 8.1% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,772 | 28.8 | 15.7 | 28.1 | 13.4 | 10.5 | 3.3 | 0.3 | 5.69 | 14.1% | 3.6% |
| CHALLENGER | 4,796 | 20.6 | 12.3 | 25.6 | 17.9 | 16.0 | 6.0 | 1.6 | 8.22 | 23.6% | 7.6% |
| ITF_MEN | 9,212 | 12.0 | 8.6 | 20.4 | 17.2 | 22.1 | 14.1 | 5.5 | 12.5 | 41.7% | 19.6% |
| ITF_WOMEN | 12,956 | 11.3 | 8.5 | 18.7 | 17.2 | 24.0 | 15.3 | 5.1 | 13.3 | 44.3% | 20.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,846 | 17.1 | 13.1 | 25.0 | 21.5 | 16.3 | 6.3 | 0.6 | 8.52 | 23.3% | 6.9% |
| WTA125 | 1,264 | 16.0 | 6.9 | 22.4 | 20.2 | 21.0 | 11.9 | 1.6 | 10.7 | 34.6% | 13.5% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,772 | 27.1 | 16.1 | 26.3 | 15.3 | 11.4 | 3.3 | 0.4 | 5.97 | 15.2% | 3.7% |
| CHALLENGER | 4,796 | 18.8 | 11.3 | 23.2 | 16.5 | 18.9 | 9.3 | 1.9 | 9.05 | 30.1% | 11.2% |
| ITF_MEN | 9,213 | 9.5 | 7.3 | 17.6 | 15.9 | 21.5 | 18.8 | 9.5 | 14.94 | 49.8% | 28.3% |
| ITF_WOMEN | 12,957 | 8.8 | 6.8 | 15.9 | 14.4 | 22.6 | 20.6 | 10.9 | 16.59 | 54.2% | 31.5% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,846 | 14.4 | 10.4 | 22.1 | 16.1 | 22.3 | 12.7 | 2.0 | 10.96 | 37.0% | 14.6% |
| WTA125 | 1,264 | 10.2 | 7.3 | 16.7 | 15.5 | 24.2 | 17.6 | 8.5 | 15.12 | 50.3% | 26.1% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,234 | 26.5 | 19.9 | 30.1 | 12.6 | 8.1 | 2.5 | 0.4 | 5.37 | 10.9% | 2.9% |
| CHALLENGER | 3,852 | 23.7 | 15.5 | 28.5 | 14.8 | 13.1 | 4.1 | 0.4 | 6.61 | 17.5% | 4.5% |
| DOUBLES | 2,256 | 5.0 | 4.5 | 12.7 | 10.8 | 20.3 | 24.8 | 22.0 | 23.54 | 67.0% | 46.8% |
| ITF_MEN | 8,017 | 13.7 | 10.1 | 22.6 | 16.3 | 21.5 | 11.7 | 4.1 | 11.04 | 37.3% | 15.8% |
| ITF_WOMEN | 9,704 | 14.0 | 9.7 | 21.0 | 16.2 | 21.5 | 14.0 | 3.6 | 11.5 | 39.1% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,650 | 24.6 | 16.5 | 30.9 | 16.7 | 9.2 | 2.1 | 0.1 | 6.43 | 11.3% | 2.2% |
| WTA125 | 1,099 | 26.3 | 13.8 | 22.5 | 20.0 | 12.2 | 4.7 | 0.5 | 7.23 | 17.4% | 5.2% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,399 | 5.1 | 4.4 | 12.5 | 10.6 | 20.5 | 24.9 | 22.1 | 23.61 | 67.4% | 46.9% |
| singles | 30,385 | 16.6 | 11.4 | 22.9 | 15.5 | 18.3 | 11.1 | 4.2 | 9.77 | 33.6% | 15.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 109 | 8.3 | 9.2 | 16.5 | 8.3 | 20.2 | 24.8 | 12.8 | 17.46 | 57.8% | 37.6% |
| Clay | 9,030 | 12.9 | 9.2 | 19.8 | 15.8 | 19.7 | 13.7 | 8.9 | 12.52 | 42.3% | 22.6% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 29,365 | 13.4 | 8.7 | 18.8 | 15.3 | 19.1 | 14.8 | 9.9 | 12.85 | 43.8% | 24.7% |
| UNKNOWN | 6,070 | 10.4 | 7.7 | 17.0 | 16.4 | 21.5 | 15.8 | 11.2 | 14.31 | 48.5% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 12,727 | 19.6 | 12.0 | 22.6 | 16.0 | 14.9 | 9.0 | 6.0 | 8.77 | 29.8% | 15.0% |
| B | 5,513 | 12.9 | 8.8 | 19.5 | 15.8 | 19.6 | 12.6 | 10.7 | 12.59 | 43.0% | 23.4% |
| C | 6,325 | 11.9 | 8.9 | 19.5 | 16.0 | 18.6 | 14.6 | 10.6 | 12.89 | 43.7% | 25.1% |
| D | 7,166 | 11.8 | 8.3 | 17.9 | 15.5 | 21.6 | 15.7 | 9.3 | 13.75 | 46.6% | 25.0% |
| F | 13,080 | 7.4 | 5.5 | 14.9 | 14.7 | 23.5 | 20.9 | 13.1 | 17.75 | 57.5% | 34.0% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,751 | 24.6 | 16.1 | 29.0 | 14.9 | 10.7 | 3.4 | 1.2 | 6.36 | 15.4% | 4.7% |
| B | 4,612 | 16.7 | 10.7 | 24.0 | 16.9 | 19.0 | 9.7 | 3.1 | 9.7 | 31.7% | 12.7% |
| C | 6,441 | 11.3 | 7.8 | 19.4 | 14.6 | 21.0 | 15.7 | 10.3 | 13.56 | 46.9% | 26.0% |
| D | 4,873 | 14.3 | 9.9 | 21.4 | 15.6 | 20.5 | 12.9 | 5.4 | 11.27 | 38.8% | 18.4% |
| F | 8,107 | 10.2 | 8.4 | 16.1 | 14.6 | 23.2 | 19.6 | 7.9 | 15.37 | 50.7% | 27.5% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 14,415 | 18.0 | 10.9 | 21.6 | 15.8 | 15.2 | 9.8 | 8.6 | 9.86 | 33.7% | 18.4% |
| LIMITED | 9,760 | 13.6 | 9.9 | 20.4 | 16.1 | 19.3 | 13.3 | 7.5 | 11.81 | 40.1% | 20.8% |
| POOR | 20,636 | 9.0 | 6.5 | 16.0 | 15.0 | 22.8 | 18.9 | 11.8 | 16.17 | 53.5% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,613 | 23.8 | 17.8 | 33.1 | 15.6 | 6.4 | 2.9 | 0.4 | 5.92 | 9.7% | 3.2% |
| GAME_SPREAD | 6,501 | 22.5 | 15.1 | 32.3 | 17.1 | 9.0 | 3.5 | 0.6 | 6.74 | 13.1% | 4.0% |
| MATCH_WINNER | 32,784 | 15.8 | 10.9 | 22.1 | 15.2 | 18.4 | 12.1 | 5.5 | 10.29 | 36.1% | 17.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 15,892 | 27.8 | 16.8 | 30.6 | 12.8 | 9.3 | 2.5 | 0.3 | 5.64 | 12.1% | 2.8% |
| TOTAL_GAMES | 10,866 | 9.9 | 10.8 | 35.3 | 26.1 | 10.6 | 4.3 | 3.0 | 9.23 | 17.8% | 7.3% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,868 | 24.5 | 28.9 | 33.2 | 8.1 | 4.0 | 1.0 | 0.3 | 4.79 | 5.3% | 1.3% |
| GAME_SPREAD | 9,028 | 46.7 | 16.2 | 24.8 | 7.5 | 2.3 | 1.9 | 0.6 | 3.31 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,165 | 6.5 | 9.8 | 40.2 | 30.3 | 7.4 | 3.4 | 2.4 | 9.23 | 13.2% | 5.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,903 | 23.9 | 16.6 | 34.8 | 14.6 | 6.9 | 2.6 | 0.5 | 6.05 | 10.0% | 3.1% |
| GAME_SPREAD | 9,037 | 20.5 | 13.5 | 28.2 | 20.1 | 12.1 | 4.5 | 1.2 | 7.64 | 17.7% | 5.7% |
| TOTAL_GAMES | 16,204 | 10.0 | 10.8 | 36.1 | 24.4 | 11.5 | 4.5 | 2.6 | 9.08 | 18.7% | 7.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 44,811 | 44.2% | 24.6% | 13.0 | 35.4% | 15.2% | 10.72 |
| gen1_elo | 44,811 | 43.8% | 24.3% | 12.76 | 35.0% | 15.1% | 10.51 |
| gen1_sr | 44,811 | 51.9% | 31.2% | 15.74 | 44.0% | 21.8% | 13.0 |
| gen2 | 44,811 | 50.8% | 31.4% | 15.38 | 43.9% | 23.3% | 12.86 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 19,722 | 15.5 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.3% | 15.3% |
| STALE | 25,089 | 10.8 | 7.3 | 16.7 | 14.1 | 19.2 | 17.0 | 14.9 | 15.45 | 51.1% | 31.9% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 26,252 | 16.4 | 11.2 | 22.7 | 15.3 | 17.9 | 11.6 | 4.9 | 9.91 | 34.4% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 77,595 | 26252 | 23194 | 28149 | 24.6 | 116.5 | 1451.1 |
| ge_15pp | 31,629 | 9035 | 8257 | 14337 | 27.9 | 421.8 | 1451.1 |
| ge_25pp | 16,818 | 4333 | 3603 | 8882 | 32.6 | 575.9 | 1431.1 |
| lt_10pp | 34,049 | 13211 | 10970 | 9868 | 22.6 | 47.3 | 1421.1 |

Current slate `SL-20261104T170609Z-f9b4a111`: 521 priced rows, quote age at build {'median': 16.1, 'max': 16.2}, freshness {'AGING': 521}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 49 | 0.0 | 0.0 | 36.7 | 6.1 | 32.6 | 20.4 | 4.1 | 18.34 | 57.1% | 24.5% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,427 | 19.2 | 10.9 | 25.5 | 18.0 | 18.0 | 7.4 | 0.9 | 8.81 | 26.3% | 8.4% |
| KALSHI_LONE_OUTLIER | 27 | 3.7 | 3.7 | 77.8 | 7.4 | 3.7 | 3.7 | 0.0 | 6.42 | 7.4% | 3.7% |
| MARKETS_AGREE | 910 | 66.0 | 34.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.2 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,976 | 0.0 | 2.3 | 37.0 | 26.3 | 24.3 | 9.2 | 0.9 | 11.85 | 34.4% | 10.1% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 44,811 | 7418 (16.6%) | 26.6% | 1.0% | {"EXTERNAL_STALE": 4427, "AGREES_WITH_KALSHI": 1976, "ALL_AGREE": 910, "SUPPORTS_MODEL_DIRECTION": 48, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 27, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 19,795 | 1876 (9.5%) | 36.2% | 1.6% | {"EXTERNAL_STALE": 1166, "AGREES_WITH_KALSHI": 680, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 11,023 | 583 (5.3%) | 34.1% | 2.2% | {"EXTERNAL_STALE": 371, "AGREES_WITH_KALSHI": 199, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,309 | 554 (10.4%) | 34.7% | 2.4% | {"EXTERNAL_STALE": 349, "AGREES_WITH_KALSHI": 192, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 18,069 | 4220 (23.4%) | 18.4% | 0.9% | {"EXTERNAL_STALE": 2463, "ALL_AGREE": 910, "AGREES_WITH_KALSHI": 777, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 23, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 8,722 | 10.4 | 7.7 | 19.4 | 14.8 | 21.6 | 16.1 | 9.9 | 14.02 | 47.6% | 26.0% |
| 4-10x | 5,975 | 11.2 | 8.5 | 18.6 | 15.4 | 22.1 | 14.3 | 10.0 | 13.74 | 46.4% | 24.3% |
| <2x | 22,965 | 15.0 | 9.8 | 19.7 | 16.1 | 17.5 | 13.1 | 8.8 | 11.52 | 39.3% | 21.8% |
| >=10x | 7,149 | 10.4 | 6.3 | 15.0 | 14.4 | 21.6 | 19.1 | 13.0 | 16.43 | 53.8% | 32.2% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 11,665 | 12.6 | 8.7 | 19.8 | 16.3 | 19.1 | 13.4 | 10.2 | 12.65 | 42.6% | 23.5% |
| 300-1000 | 9,649 | 11.8 | 8.8 | 17.7 | 15.5 | 20.7 | 16.2 | 9.4 | 13.63 | 46.2% | 25.6% |
| <300 | 14,149 | 8.3 | 5.7 | 15.1 | 14.7 | 23.1 | 20.0 | 13.1 | 17.14 | 56.1% | 33.1% |
| >=3000 | 9,348 | 21.4 | 13.0 | 24.0 | 15.7 | 13.8 | 7.1 | 5.0 | 7.69 | 25.9% | 12.1% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1337 | 0.5491 | 0.4097 | 0.4914 | +0.058 | -0.082 | -0.0001 ± 0.0042 |
| ratio 4-10x | 914 | 0.5807 | 0.4342 | 0.4891 | +0.092 | -0.055 | 0.0096 ± 0.0053 |
| ratio <2x | 3265 | 0.5373 | 0.4145 | 0.4398 | +0.098 | -0.025 | 0.0136 ± 0.0025 |
| ratio >=10x | 1111 | 0.5668 | 0.3932 | 0.4473 | +0.119 | -0.054 | 0.015 ± 0.0054 |
| thinner_sample 1000-3000 | 1840 | 0.5397 | 0.413 | 0.4516 | +0.088 | -0.039 | 0.0094 ± 0.0034 |
| thinner_sample 300-1000 | 1506 | 0.5664 | 0.4255 | 0.4807 | +0.086 | -0.055 | 0.0035 ± 0.004 |
| thinner_sample <300 | 2162 | 0.5597 | 0.391 | 0.4537 | +0.106 | -0.063 | 0.0138 ± 0.0038 |
| thinner_sample >=3000 | 1119 | 0.5299 | 0.4368 | 0.4477 | +0.082 | -0.011 | 0.0155 ± 0.0034 |
| data_status ADEQUATE | 1837 | 0.5317 | 0.4292 | 0.4409 | +0.091 | -0.012 | 0.0147 ± 0.0028 |
| data_status LIMITED | 1615 | 0.5495 | 0.4164 | 0.4724 | +0.077 | -0.056 | 0.0057 ± 0.0037 |
| data_status POOR | 3175 | 0.5622 | 0.4012 | 0.4611 | +0.101 | -0.060 | 0.0106 ± 0.0031 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 962 | 0.1985 | 0.199 | -0.0005 ± 0.0005 | 0.5771 | 0.5783 | 0.5019 | 0.4868 | 0.5031 | -0.093 ± 0.0152 | -0.0087 (8) |
| 3-5 | 607 | 0.2043 | 0.2036 | +0.0007 ± 0.0015 | 0.5918 | 0.5881 | 0.5051 | 0.4652 | 0.4761 | -0.105 ± 0.0188 | 0.01 (2) |
| 5-10 | 1419 | 0.2001 | 0.1996 | +0.0005 ± 0.0018 | 0.5855 | 0.582 | 0.5125 | 0.4387 | 0.4693 | -0.089 ± 0.0123 | -0.0143 (7) |
| 10-15 | 1153 | 0.2185 | 0.2092 | +0.0093 ± 0.0033 | 0.6294 | 0.602 | 0.5264 | 0.4028 | 0.4258 | -0.108 ± 0.0137 | -0.048 (5) |
| 15-25 | 1464 | 0.2245 | 0.2081 | +0.0164 ± 0.0047 | 0.6439 | 0.5996 | 0.5764 | 0.3813 | 0.4372 | -0.105 ± 0.0119 | -0.004 (10) |
| 25-40 | 842 | 0.2209 | 0.2045 | +0.0164 ± 0.0093 | 0.6305 | 0.59 | 0.6529 | 0.343 | 0.4715 | -0.070 ± 0.0142 | -0.06 (2) |
| 40+ | 180 | 0.2928 | 0.1795 | +0.1133 ± 0.0282 | 0.7908 | 0.5341 | 0.7331 | 0.2793 | 0.3889 | -0.080 ± 0.0275 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5078 | 0.1859 | 0.1868 | -0.0009 ± 0.0002 | 0.5476 | 0.5485 | 0.4878 | 0.4725 | 0.5024 | -0.023 ± 0.0062 | -0.01 (28) |
| 3-5 | 3394 | 0.1966 | 0.1949 | +0.0017 ± 0.0006 | 0.5721 | 0.5657 | 0.4809 | 0.4412 | 0.439 | -0.057 ± 0.0077 | 0.0 (3) |
| 5-10 | 7336 | 0.2004 | 0.1973 | +0.0031 ± 0.0008 | 0.5859 | 0.5752 | 0.4854 | 0.4118 | 0.4279 | -0.043 ± 0.0052 | -0.0114 (22) |
| 10-15 | 6087 | 0.2018 | 0.186 | +0.0158 ± 0.0014 | 0.5901 | 0.5459 | 0.4862 | 0.3623 | 0.3604 | -0.064 ± 0.0056 | -0.0281 (16) |
| 15-25 | 7618 | 0.206 | 0.1668 | +0.0391 ± 0.0018 | 0.604 | 0.4959 | 0.4995 | 0.304 | 0.3024 | -0.071 ± 0.0047 | -0.0027 (45) |
| 25-40 | 5886 | 0.2222 | 0.1262 | +0.0960 ± 0.0029 | 0.6385 | 0.3877 | 0.5266 | 0.2129 | 0.2212 | -0.058 ± 0.0045 | -0.0733 (3) |
| 40+ | 3905 | 0.3821 | 0.0454 | +0.3367 ± 0.0039 | 0.9953 | 0.1747 | 0.6315 | 0.1035 | 0.0607 | -0.076 ± 0.0032 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 772 | 0.2064 | 0.2068 | -0.0005 ± 0.0006 | 0.5942 | 0.5957 | 0.5077 | 0.4929 | 0.5194 | -0.101 ± 0.0177 | -0.0117 (6) |
| 3-5 | 547 | 0.2126 | 0.2096 | +0.0029 ± 0.0016 | 0.6083 | 0.602 | 0.5128 | 0.4732 | 0.4516 | -0.132 ± 0.021 | 0.01 (2) |
| 5-10 | 1215 | 0.2048 | 0.2024 | +0.0024 ± 0.0019 | 0.5952 | 0.5879 | 0.5408 | 0.4662 | 0.4905 | -0.095 ± 0.0133 | -0.01 (4) |
| 10-15 | 1067 | 0.212 | 0.2066 | +0.0054 ± 0.0035 | 0.6151 | 0.5989 | 0.5631 | 0.4388 | 0.4827 | -0.100 ± 0.0145 | -0.04 (5) |
| 15-25 | 1546 | 0.2311 | 0.2111 | +0.0200 ± 0.0046 | 0.6568 | 0.6061 | 0.5854 | 0.39 | 0.4386 | -0.103 ± 0.0119 | -0.012 (10) |
| 25-40 | 1087 | 0.2671 | 0.1981 | +0.0691 ± 0.0085 | 0.7452 | 0.5763 | 0.6595 | 0.3454 | 0.3947 | -0.125 ± 0.0135 | -0.008 (5) |
| 40+ | 393 | 0.367 | 0.1659 | +0.2010 ± 0.0205 | 1.0005 | 0.4994 | 0.736 | 0.2475 | 0.3003 | -0.081 ± 0.0197 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4379 | 0.1928 | 0.1931 | -0.0003 ± 0.0002 | 0.5616 | 0.562 | 0.5087 | 0.4936 | 0.5115 | -0.038 ± 0.0068 | -0.0154 (26) |
| 3-5 | 2979 | 0.1933 | 0.1924 | +0.0010 ± 0.0006 | 0.5632 | 0.56 | 0.51 | 0.4704 | 0.4773 | -0.045 ± 0.0082 | 0.01 (2) |
| 5-10 | 6543 | 0.1971 | 0.1935 | +0.0037 ± 0.0008 | 0.5785 | 0.5655 | 0.5078 | 0.4338 | 0.4487 | -0.043 ± 0.0055 | -0.0117 (6) |
| 10-15 | 5451 | 0.2018 | 0.191 | +0.0108 ± 0.0015 | 0.5928 | 0.5591 | 0.5123 | 0.3884 | 0.4076 | -0.046 ± 0.006 | -0.0189 (18) |
| 15-25 | 7611 | 0.2172 | 0.1804 | +0.0368 ± 0.0019 | 0.6311 | 0.5294 | 0.524 | 0.3289 | 0.3354 | -0.063 ± 0.0049 | -0.0084 (43) |
| 25-40 | 6932 | 0.2508 | 0.1373 | +0.1134 ± 0.0028 | 0.7075 | 0.4197 | 0.5596 | 0.2428 | 0.2255 | -0.082 ± 0.0045 | -0.0095 (20) |
| 40+ | 5409 | 0.3999 | 0.0603 | +0.3396 ± 0.0038 | 1.0544 | 0.2159 | 0.6542 | 0.1193 | 0.083 | -0.072 ± 0.0033 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 933 | 0.1967 | 0.1982 | -0.0016 ± 0.0005 | 0.5731 | 0.577 | 0.5007 | 0.4853 | 0.5338 | -0.050 ± 0.0152 | -0.012 (10) |
| 3-5 | 648 | 0.2066 | 0.2051 | +0.0015 ± 0.0014 | 0.5975 | 0.5919 | 0.4974 | 0.4578 | 0.4614 | -0.113 ± 0.0186 | -0.0 (4) |
| 5-10 | 1448 | 0.201 | 0.1976 | +0.0034 ± 0.0018 | 0.5865 | 0.5764 | 0.5121 | 0.4384 | 0.4503 | -0.106 ± 0.0121 | -0.01 (9) |
| 10-15 | 1166 | 0.211 | 0.203 | +0.0080 ± 0.0033 | 0.6123 | 0.5889 | 0.5401 | 0.4171 | 0.4477 | -0.106 ± 0.0132 | -0.0286 (7) |
| 15-25 | 1400 | 0.2304 | 0.2123 | +0.0181 ± 0.0048 | 0.6584 | 0.6086 | 0.5878 | 0.3934 | 0.4436 | -0.111 ± 0.0123 | -0.03 (1) |
| 25-40 | 842 | 0.2123 | 0.2098 | +0.0026 ± 0.0093 | 0.6125 | 0.6023 | 0.6617 | 0.3507 | 0.5 | -0.059 ± 0.0142 | -0.0267 (3) |
| 40+ | 190 | 0.3114 | 0.1827 | +0.1287 ± 0.0278 | 0.8427 | 0.5405 | 0.743 | 0.2893 | 0.3842 | -0.094 ± 0.0285 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4881 | 0.1841 | 0.1848 | -0.0007 ± 0.0002 | 0.5425 | 0.5434 | 0.4828 | 0.4674 | 0.487 | -0.032 ± 0.0062 | -0.0137 (41) |
| 3-5 | 3450 | 0.2047 | 0.203 | +0.0017 ± 0.0006 | 0.5935 | 0.5875 | 0.4808 | 0.4412 | 0.4406 | -0.056 ± 0.0078 | -0.01 (19) |
| 5-10 | 7515 | 0.1953 | 0.1904 | +0.0049 ± 0.0008 | 0.5735 | 0.5578 | 0.4875 | 0.4136 | 0.4176 | -0.054 ± 0.0051 | -0.0105 (37) |
| 10-15 | 6002 | 0.1933 | 0.179 | +0.0144 ± 0.0014 | 0.5712 | 0.5297 | 0.4955 | 0.3723 | 0.375 | -0.060 ± 0.0055 | -0.0146 (13) |
| 15-25 | 7732 | 0.2117 | 0.1722 | +0.0395 ± 0.0018 | 0.6175 | 0.5079 | 0.5138 | 0.3192 | 0.316 | -0.072 ± 0.0047 | -0.0533 (3) |
| 25-40 | 5865 | 0.2172 | 0.1275 | +0.0897 ± 0.0029 | 0.6276 | 0.3905 | 0.5297 | 0.2141 | 0.2319 | -0.050 ± 0.0045 | -0.02 (4) |
| 40+ | 3859 | 0.3921 | 0.0504 | +0.3417 ± 0.0041 | 1.0222 | 0.1875 | 0.6411 | 0.1097 | 0.0671 | -0.077 ± 0.0035 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1357 | 0.196 | 0.1961 | -0.0001 ± 0.0004 | 0.5699 | 0.5699 | 0.5065 | 0.4915 | 0.4967 | -0.068 ± 0.0123 | -0.0213 (54) |
| 3-5 | 963 | 0.1882 | 0.188 | +0.0003 ± 0.0011 | 0.5539 | 0.5519 | 0.4951 | 0.4552 | 0.4704 | -0.060 ± 0.0143 | -0.0194 (34) |
| 5-10 | 1960 | 0.1991 | 0.1945 | +0.0046 ± 0.0015 | 0.5861 | 0.5714 | 0.5068 | 0.4331 | 0.4388 | -0.076 ± 0.0102 | -0.005 (78) |
| 10-15 | 1347 | 0.2151 | 0.2021 | +0.0130 ± 0.003 | 0.6227 | 0.5879 | 0.5407 | 0.4179 | 0.4246 | -0.092 ± 0.0126 | 0.0014 (65) |
| 15-25 | 1751 | 0.2299 | 0.2068 | +0.0232 ± 0.0043 | 0.6568 | 0.5973 | 0.5892 | 0.3942 | 0.4352 | -0.088 ± 0.011 | -0.0214 (59) |
| 25-40 | 1069 | 0.2407 | 0.2098 | +0.0309 ± 0.0086 | 0.6878 | 0.6025 | 0.6862 | 0.374 | 0.4808 | -0.089 ± 0.0131 | -0.0252 (27) |
| 40+ | 378 | 0.3293 | 0.2023 | +0.1270 ± 0.0222 | 0.951 | 0.5889 | 0.8158 | 0.3388 | 0.4603 | -0.098 ± 0.0208 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4987 | 0.1769 | 0.1771 | -0.0002 ± 0.0002 | 0.5233 | 0.5233 | 0.512 | 0.4968 | 0.5081 | -0.038 ± 0.006 | -0.0145 (98) |
| 3-5 | 3421 | 0.1941 | 0.1932 | +0.0009 ± 0.0006 | 0.5661 | 0.5639 | 0.5009 | 0.4611 | 0.47 | -0.042 ± 0.0076 | -0.0204 (72) |
| 5-10 | 6956 | 0.1964 | 0.1899 | +0.0065 ± 0.0008 | 0.5784 | 0.5596 | 0.5008 | 0.4272 | 0.4212 | -0.063 ± 0.0053 | -0.0084 (134) |
| 10-15 | 4795 | 0.2101 | 0.1939 | +0.0162 ± 0.0016 | 0.6106 | 0.5687 | 0.5377 | 0.4147 | 0.409 | -0.072 ± 0.0064 | -0.0053 (106) |
| 15-25 | 5800 | 0.2298 | 0.1993 | +0.0305 ± 0.0023 | 0.6609 | 0.5778 | 0.5748 | 0.3794 | 0.4005 | -0.066 ± 0.0059 | -0.026 (108) |
| 25-40 | 3866 | 0.2576 | 0.1893 | +0.0683 ± 0.0044 | 0.7291 | 0.5518 | 0.6379 | 0.3253 | 0.3751 | -0.069 ± 0.0068 | -0.0246 (52) |
| 40+ | 1691 | 0.3732 | 0.1584 | +0.2149 ± 0.01 | 1.0552 | 0.4723 | 0.7441 | 0.2428 | 0.2898 | -0.068 ± 0.0092 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 6627 | 1.041 ± 0.034 | 1.115 | 0.1694 | 0.1679 | 0.214 | 0.2035 |
| gen2 | 6627 | 0.833 ± 0.031 | 1.084 | 0.1733 | 0.1682 | 0.2328 | 0.2034 |
| gen1_elo | 6627 | 1.014 ± 0.033 | 1.106 | 0.176 | 0.168 | 0.2135 | 0.2036 |
| gen1_sr | 6627 | 1.019 ± 0.041 | 1.146 | 0.1333 | 0.17 | 0.2289 | 0.2031 |
| gen1_ledger | 8825 | 0.871 ± 0.025 | 1.082 | 0.1894 | 0.1761 | 0.2166 | 0.1998 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 31,629)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 7,308 | 23.1% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,990 | 22.1% |
| BOOK_QUALITY | execution | 5,803 | 18.4% |
| POOR_DATA | data | 3,725 | 11.8% |
| LIMITED_DATA | data | 1,980 | 6.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,773 | 5.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,328 | 4.2% |
| IDENTITY_AMBIGUOUS | mapping | 1,305 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 887 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 529 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 23.1%, coverage 22.1%, execution 18.4%, data 18.0%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.2%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.4%, LOW_DATA_QUALITY 71.6%, THIN_PLAYER_HISTORY 60.0%, STALE_PLAYER_DATA 52.2%, STALE_KALSHI_QUOTE 45.3%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 24.5%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 15.4%, LEVEL_TRANSFER_RISK 10.2%, LOW_DISPLAYED_LIQUIDITY 8.3%, EVENT_MAPPING_RISK 7.3%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.5%, POST_SETTLEMENT_OBSERVATION 22.1%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 16,818)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,620 | 33.4% |
| STALE_QUOTE | market_freshness | 3,305 | 19.7% |
| BOOK_QUALITY | execution | 3,018 | 17.9% |
| POOR_DATA | data | 1,602 | 9.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 939 | 5.6% |
| IDENTITY_AMBIGUOUS | mapping | 718 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 582 | 3.5% |
| LIMITED_DATA | data | 577 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 325 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 131 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.4%, market_freshness 19.7%, execution 17.9%, data 13.0%, market_freshness/coverage 9.0%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 96.9%, LOW_DATA_QUALITY 75.1%, THIN_PLAYER_HISTORY 62.2%, STALE_KALSHI_QUOTE 52.8%, STALE_PLAYER_DATA 46.3%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 24.0%, MODEL_HIGH_UNCERTAINTY 19.2%, PLAYER_IDENTITY_RISK 18.5%, LEVEL_TRANSFER_RISK 9.1%, EVENT_MAPPING_RISK 8.9%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.4%, POST_SETTLEMENT_OBSERVATION 33.4%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 13390, "IDENTITY_AMBIGUOUS": 3428}; ticker orientation: {"VERIFIED": 16818}.

Checks: discipline:AMBIGUOUS 1126, discipline:PASS 15692, identity_confidence:AMBIGUOUS 3104, identity_confidence:PASS 13714, level_mapping:NA 1138, level_mapping:PASS 15680, market_pair:AMBIGUOUS 485, market_pair:NA 370, market_pair:PASS 15963, model_complement:NA 332, model_complement:PASS 16486, namesake:AMBIGUOUS 6, namesake:PASS 16812, physical_match_id:NA 5795, physical_match_id:PASS 11023, player_ids:PASS 16818, same_pair_other_event:PASS 16818, ticker_orientation:PASS 16818

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,176 | 3.8% | 3.3% | 1.4% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 21, "market_freshness/coverage": 17} | 5.56 | 0.2262 / 0.2211 (765) | 24.4% | 2.5% | 3.1% | 2.8% |
| CHALLENGER | 11,120 | 16.3% | 6.2% | 10.8% | {"coverage": 1057, "market_freshness/coverage": 213, "market_freshness": 210, "data": 157, "model_calibration_or_unknown": 77, "execution": 41, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.38 | 0.2207 / 0.2101 (2580) | 37.4% | 15.7% | 4.1% | 22.2% |
| DOUBLES | 2,399 | 46.9% | 46.8% | 6.7% | {"execution": 644, "mapping": 305, "market_freshness": 106, "market_freshness/coverage": 64, "coverage": 7} | 23.54 | 0.303 / 0.2359 (578) | 9.8% | 0.0% | 100.0% | 6.0% |
| ITF_MEN | 21,807 | 25.1% | 17.8% | 32.5% | {"coverage": 1868, "market_freshness": 1063, "execution": 963, "data": 831, "market_freshness/coverage": 525, "mapping": 205, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.8 | 0.215 / 0.1974 (4561) | 39.0% | 69.4% | 15.7% | 21.0% |
| ITF_WOMEN | 28,729 | 26.5% | 19.2% | 45.2% | {"coverage": 2613, "market_freshness": 1671, "execution": 1287, "data": 1092, "market_freshness/coverage": 646, "mapping": 185, "model_calibration_or_unknown": 87, "model_calibration": 22} | 12.56 | 0.2024 / 0.1931 (5440) | 40.4% | 57.4% | 9.9% | 21.1% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,666 | 6.1% | 5.2% | 1.7% | {"market_freshness": 107, "model_calibration_or_unknown": 51, "coverage": 39, "execution": 29, "data": 24, "model_calibration": 21, "market_freshness/coverage": 13, "mapping": 1} | 7.7 | 0.2307 / 0.223 (750) | 29.4% | 2.1% | 1.3% | 3.6% |
| WTA125 | 2,543 | 11.2% | 9.7% | 1.7% | {"market_freshness": 89, "model_calibration_or_unknown": 53, "market_freshness/coverage": 42, "data": 39, "execution": 24, "model_calibration": 19, "coverage": 14, "mapping": 4} | 9.21 | 0.2064 / 0.1905 (736) | 28.7% | 10.7% | 4.2% | 7.1% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.4h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 509 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 773 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 572 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 9 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 10 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 13 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 14 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 207 min (STALE); no external reference |
| 17 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 18 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 19 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 20 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 21 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 22 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 23 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 24 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 25 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 26 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 27 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 28 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 29 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 30 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 31 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 32 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 33 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 34 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 35 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 36 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 37 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 38 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 39 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 40 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 41 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 42 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 43 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 44 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 77 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 45 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 46 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 252 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |
| 47 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXATPCHALLENGERMATCH-26NOV02TOBSTO-TOB` | CHALLENGER | fair_v1 | 80% / 2% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 165 min (STALE); data POOR (grade F, thinner serve sample 159.0, ratio 20.58); no external reference |
| 49 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 50 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.969, "by_level_share_of_ge_25pp": {"ATP": 0.0141, "CHALLENGER": 0.1075, "DOUBLES": 0.067, "ITF_MEN": 0.3248, "ITF_WOMEN": 0.4521, "OTHER": 0.0007, "WTA": 0.0169, "WTA125": 0.0169}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5281, "share_primary_cause_market_settled_or_in_play": 0.4246, "share_primary_cause_stale_quote_only": 0.1965}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 16818, "identity_ambiguous_share": 0.2038, "ticker_orientation": {"VERIFIED": 16818}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 11023, "with_external": 583, "coverage": 0.0529, "external_status": {"EXTERNAL_STALE": 371, "AGREES_WITH_KALSHI": 199, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 371, "MODEL_LONE_OUTLIER": 199, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3413, "share_external_supports_model": 0.0223}, "pregame_clean_ge_25pp": {"n": 5309, "with_external": 554, "coverage": 0.1044, "external_status": {"EXTERNAL_STALE": 349, "AGREES_WITH_KALSHI": 192, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 349, "MODEL_LONE_OUTLIER": 192, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3466, "share_external_supports_model": 0.0235}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 476.0, "median_sample_ratio": 2.47, "median_min_matches": 18.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2101, "data_status": {"POOR": 9503, "LIMITED": 4346, "ADEQUATE": 2969}, "comparison_lt_10pp": {"median_thinner_serve_points": 1732.0, "median_sample_ratio": 1.7, "median_min_matches": 90.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1337, "model_minus_observed": 0.0577, "kalshi_minus_observed": -0.0817, "brier_diff_model_minus_kalshi": -0.0001}, "4-10x": {"n": 914, "model_minus_observed": 0.0916, "kalshi_minus_observed": -0.0549, "brier_diff_model_minus_kalshi": 0.0096}, "<2x": {"n": 3265, "model_minus_observed": 0.0975, "kalshi_minus_observed": -0.0253, "brier_diff_model_minus_kalshi": 0.0136}, ">=10x": {"n": 1111, "model_minus_observed": 0.1195, "kalshi_minus_observed": -0.0541, "brier_diff_model_minus_kalshi": 0.015}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 6627, "model": {"intercept": -0.559, "slope": 0.833, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.186, "slope": 1.084, "slope_se": 0.035}, "mean_extremity_model": 0.1733, "mean_extremity_kalshi": 0.1682, "model_brier": 0.2328, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": 0.0294, "brier_diff_se": 0.0023, "model_logloss": 0.6624, "kalshi_logloss": 0.5888}, "fair_v1": {"n": 6627, "model": {"intercept": -0.446, "slope": 1.041, "slope_se": 0.034}, "kalshi_mid_same_rows": {"intercept": 0.261, "slope": 1.115, "slope_se": 0.035}, "mean_extremity_model": 0.1694, "mean_extremity_kalshi": 0.1679, "model_brier": 0.214, "kalshi_brier": 0.2035, "brier_diff_model_minus_kalshi": 0.0105, "brier_diff_se": 0.0019, "model_logloss": 0.6167, "kalshi_logloss": 0.5891}, "gen1_elo": {"n": 6627, "model": {"intercept": -0.433, "slope": 1.014, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.264, "slope": 1.106, "slope_se": 0.035}, "mean_extremity_model": 0.176, "mean_extremity_kalshi": 0.168, "model_brier": 0.2135, "kalshi_brier": 0.2036, "brier_diff_model_minus_kalshi": 0.0099, "brier_diff_se": 0.0019, "model_logloss": 0.6161, "kalshi_logloss": 0.5893}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.246, "share_ge_15": 0.4417, "median_abs_gap": 13.0, "n": 44811}, "gen1_elo": {"share_ge_25": 0.2435, "share_ge_15": 0.4384, "median_abs_gap": 12.76, "n": 44811}, "gen1_sr": {"share_ge_25": 0.3122, "share_ge_15": 0.5186, "median_abs_gap": 15.74, "n": 44811}, "gen2": {"share_ge_25": 0.3137, "share_ge_15": 0.5084, "median_abs_gap": 15.38, "n": 44811}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1523, "share_ge_15": 0.3545, "median_abs_gap": 10.72, "n": 34852}, "gen1_elo": {"share_ge_25": 0.1509, "share_ge_15": 0.35, "median_abs_gap": 10.51, "n": 34852}, "gen1_sr": {"share_ge_25": 0.2181, "share_ge_15": 0.4401, "median_abs_gap": 13.0, "n": 34854}, "gen2": {"share_ge_25": 0.2329, "share_ge_15": 0.4393, "median_abs_gap": 12.86, "n": 34854}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.56, "share_ge_25_all": 0.0384, "share_ge_25_pregame_clean": 0.0331}, "WTA": {"median_abs_gap_pregame_clean": 7.7, "share_ge_25_all": 0.0611, "share_ge_25_pregame_clean": 0.0518}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2371, "share_within_10pp_all": 0.4388, "share_within_10pp_pregame_clean": 0.4903, "corr_model_vs_mid_pregame_clean": 0.8498}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 962, "model_brier": 0.1985, "kalshi_brier": 0.199, "brier_diff_model_minus_kalshi": -0.0005}, "10-15": {"n_settled": 1153, "model_brier": 0.2185, "kalshi_brier": 0.2092, "brier_diff_model_minus_kalshi": 0.0093}, "15-25": {"n_settled": 1464, "model_brier": 0.2245, "kalshi_brier": 0.2081, "brier_diff_model_minus_kalshi": 0.0164}, "25-40": {"n_settled": 842, "model_brier": 0.2209, "kalshi_brier": 0.2045, "brier_diff_model_minus_kalshi": 0.0164}, "3-5": {"n_settled": 607, "model_brier": 0.2043, "kalshi_brier": 0.2036, "brier_diff_model_minus_kalshi": 0.0007}, "40+": {"n_settled": 180, "model_brier": 0.2928, "kalshi_brier": 0.1795, "brier_diff_model_minus_kalshi": 0.1133}, "5-10": {"n_settled": 1419, "model_brier": 0.2001, "kalshi_brier": 0.1996, "brier_diff_model_minus_kalshi": 0.0005}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.559, "slope": 0.833, "slope_se": 0.031}, "kalshi_slope": {"intercept": 0.186, "slope": 1.084, "slope_se": 0.035}, "n": 6627}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.489, "slope": 0.871, "slope_se": 0.025}, "kalshi_slope": {"intercept": 0.176, "slope": 1.082, "slope_se": 0.029}, "n": 8825}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 578, "model_brier": 0.303, "kalshi_brier": 0.2359, "brier_diff_model_minus_kalshi": 0.0671, "brier_diff_se": 0.0124, "corr_model_outcome": 0.0791, "corr_kalshi_outcome": 0.2529}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
