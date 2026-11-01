# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-01T07:17Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 72,201): 0-3 14.2%, 3-5 9.6%, 5-10 20.3%, 10-15 15.3%, 15-25 19.0%, 25-40 13.7%, 40+ 8.0%; median gap 11.77 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.7%, Challenger 10.8%, doubles 6.8%). Main tour: ATP 3.9% and WTA 5.8% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 15,667): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.0%, STALE_QUOTE 18.7%, BOOK_QUALITY 18.4%, POOR_DATA 9.3%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IDENTITY_AMBIGUOUS 4.2%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.0%, market_freshness 18.7%, execution 18.4%, data 12.8%, market_freshness/coverage 9.1%, mapping 4.2%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.3% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.2% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 15,667 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.7% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 485.0 points vs 1748.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.018, Gen-2 0.807, Gen-1 ledger 0.856 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 757 model 0.2234 vs Kalshi 0.2064; n 159 model 0.2822 vs Kalshi 0.1885.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 308,387 model-market comparisons (502,870 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 104,583 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-01T07:01:45.379921+00:00'], shadow board 82,312 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-01T07:01:49.180841+00:00'], Model 4 38,490 rows, 24,998 settled tickers, 9,204 tickers with an external scan.
* By model: {"gen1_ledger": 70759, "gen1_elo": 41367, "fair_v1": 41367, "gen2": 41367, "gen1_sr": 41367, "model4_fundamental": 36102, "model4_conditioned": 36058}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 72,201 | 14.2 | 9.6 | 20.3 | 15.3 | 19.0 | 13.7 | 8.0 | 11.77 | 40.7% | 21.7% |
| MW fair_v1 | 41,367 | 13.0 | 8.7 | 18.9 | 15.3 | 19.5 | 14.8 | 9.9 | 12.97 | 44.1% | 24.7% |
| MW gen1_elo | 41,367 | 12.5 | 8.7 | 19.4 | 15.4 | 19.5 | 14.7 | 9.8 | 12.85 | 44.0% | 24.5% |
| MW gen1_ledger | 30,834 | 15.7 | 10.9 | 22.2 | 15.2 | 18.3 | 12.2 | 5.5 | 10.28 | 36.0% | 17.7% |
| MW gen1_sr | 41,367 | 10.2 | 7.2 | 16.9 | 13.9 | 20.6 | 18.5 | 12.7 | 15.75 | 51.8% | 31.2% |
| MW gen2 | 41,367 | 11.2 | 7.6 | 16.6 | 13.8 | 19.4 | 17.7 | 13.7 | 15.38 | 50.8% | 31.4% |
| all families model4_conditioned | 36,058 | 22.4 | 18.2 | 34.1 | 17.1 | 5.0 | 2.1 | 1.2 | 6.0 | 8.2% | 3.3% |
| all families model4_fundamental | 36,102 | 17.4 | 13.3 | 33.9 | 20.2 | 10.1 | 3.8 | 1.4 | 7.67 | 15.2% | 5.2% |

Configurable thresholds (primary): >=5pp 76.2%, >=10pp 55.9%, >=15pp 40.7%, >=20pp 30.1%, >=25pp 21.7%, >=30pp 15.7%, >=40pp 8.0%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.22pp; >=10pp 44.6%, >=25pp 16.9%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,634 | 27.6 | 15.2 | 28.2 | 13.3 | 11.4 | 3.8 | 0.6 | 5.93 | 15.7% | 4.3% |
| CHALLENGER | 6,129 | 16.3 | 9.7 | 21.0 | 15.1 | 15.5 | 11.6 | 10.8 | 10.86 | 37.9% | 22.4% |
| ITF_MEN | 11,545 | 9.8 | 7.4 | 17.0 | 15.0 | 21.2 | 17.6 | 12.0 | 15.22 | 50.7% | 29.5% |
| ITF_WOMEN | 16,254 | 9.6 | 7.1 | 16.1 | 15.1 | 22.0 | 18.0 | 12.1 | 15.67 | 52.2% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,637 | 18.2 | 13.3 | 25.1 | 20.1 | 15.8 | 6.3 | 1.1 | 8.24 | 23.2% | 7.4% |
| WTA125 | 1,162 | 16.4 | 7.1 | 22.5 | 19.1 | 20.9 | 12.1 | 1.8 | 10.7 | 34.8% | 13.9% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,634 | 26.1 | 15.5 | 26.3 | 15.8 | 11.7 | 3.9 | 0.7 | 6.2 | 16.3% | 4.6% |
| CHALLENGER | 6,129 | 15.1 | 9.1 | 18.3 | 14.2 | 18.3 | 13.4 | 11.6 | 12.49 | 43.3% | 25.0% |
| ITF_MEN | 11,545 | 8.1 | 6.2 | 15.1 | 13.8 | 19.6 | 20.6 | 16.5 | 17.92 | 56.7% | 37.2% |
| ITF_WOMEN | 16,254 | 8.0 | 5.8 | 14.0 | 12.7 | 20.6 | 21.1 | 17.7 | 19.11 | 59.5% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,637 | 15.3 | 10.9 | 22.1 | 15.2 | 21.7 | 12.7 | 1.9 | 10.59 | 36.4% | 14.6% |
| WTA125 | 1,162 | 9.6 | 6.7 | 17.1 | 15.6 | 24.4 | 17.9 | 8.7 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,634 | 22.3 | 13.5 | 24.9 | 16.0 | 15.7 | 6.4 | 1.2 | 7.5 | 23.3% | 7.7% |
| CHALLENGER | 6,129 | 15.1 | 9.2 | 20.9 | 16.0 | 15.7 | 12.1 | 11.0 | 11.33 | 38.8% | 23.0% |
| ITF_MEN | 11,545 | 9.3 | 7.2 | 17.3 | 14.2 | 21.8 | 17.7 | 12.4 | 15.75 | 52.0% | 30.1% |
| ITF_WOMEN | 16,254 | 9.4 | 6.9 | 16.5 | 15.8 | 22.1 | 17.9 | 11.4 | 15.49 | 51.4% | 29.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,637 | 23.0 | 16.3 | 32.2 | 14.6 | 9.4 | 3.3 | 1.2 | 6.17 | 13.9% | 4.5% |
| WTA125 | 1,162 | 21.2 | 12.9 | 27.0 | 17.8 | 15.0 | 5.8 | 0.3 | 8.01 | 21.1% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,204 | 25.4 | 19.5 | 30.8 | 12.6 | 8.6 | 2.7 | 0.5 | 5.55 | 11.8% | 3.1% |
| CHALLENGER | 4,182 | 22.6 | 14.5 | 27.4 | 14.4 | 13.6 | 6.0 | 1.6 | 7.08 | 21.1% | 7.5% |
| DOUBLES | 2,251 | 5.2 | 4.3 | 11.8 | 10.5 | 20.7 | 25.4 | 22.2 | 23.85 | 68.2% | 47.6% |
| ITF_MEN | 8,708 | 13.0 | 9.5 | 21.3 | 15.8 | 21.4 | 13.2 | 5.8 | 11.87 | 40.4% | 19.1% |
| ITF_WOMEN | 10,532 | 13.2 | 9.1 | 20.0 | 15.8 | 21.2 | 15.3 | 5.5 | 12.3 | 42.0% | 20.8% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,627 | 24.1 | 16.3 | 30.4 | 17.0 | 9.1 | 2.8 | 0.2 | 6.53 | 12.2% | 3.1% |
| WTA125 | 1,181 | 24.9 | 12.9 | 21.1 | 19.4 | 13.5 | 6.8 | 1.5 | 7.88 | 21.8% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,535 | 27.9 | 15.4 | 28.5 | 13.3 | 11.2 | 3.5 | 0.3 | 5.9 | 14.9% | 3.8% |
| CHALLENGER | 4,309 | 21.2 | 12.2 | 26.0 | 17.6 | 15.4 | 6.0 | 1.6 | 8.04 | 22.9% | 7.5% |
| ITF_MEN | 8,412 | 12.1 | 8.9 | 20.6 | 17.1 | 21.9 | 14.2 | 5.2 | 12.33 | 41.3% | 19.4% |
| ITF_WOMEN | 12,065 | 11.5 | 8.5 | 18.7 | 17.2 | 24.1 | 15.0 | 5.1 | 13.22 | 44.1% | 20.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,545 | 18.5 | 13.3 | 25.4 | 20.5 | 15.8 | 5.8 | 0.7 | 8.18 | 22.3% | 6.5% |
| WTA125 | 1,123 | 16.6 | 7.0 | 22.0 | 19.4 | 21.4 | 11.9 | 1.6 | 10.97 | 34.9% | 13.5% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,535 | 26.3 | 15.8 | 26.5 | 15.8 | 11.7 | 3.5 | 0.4 | 6.14 | 15.6% | 3.9% |
| CHALLENGER | 4,309 | 19.2 | 11.6 | 22.9 | 16.7 | 18.7 | 9.0 | 1.9 | 8.99 | 29.6% | 10.9% |
| ITF_MEN | 8,413 | 9.6 | 7.4 | 17.5 | 16.1 | 21.4 | 18.7 | 9.4 | 14.86 | 49.5% | 28.1% |
| ITF_WOMEN | 12,066 | 8.9 | 6.8 | 15.9 | 14.3 | 22.8 | 20.6 | 10.8 | 16.58 | 54.1% | 31.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,545 | 15.5 | 11.0 | 22.4 | 15.4 | 21.9 | 12.6 | 1.3 | 10.4 | 35.8% | 13.9% |
| WTA125 | 1,123 | 9.6 | 6.8 | 17.3 | 15.7 | 24.3 | 18.2 | 8.2 | 15.19 | 50.7% | 26.4% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,147 | 25.5 | 19.7 | 30.7 | 12.8 | 8.3 | 2.6 | 0.4 | 5.53 | 11.3% | 2.9% |
| CHALLENGER | 3,695 | 23.9 | 15.4 | 28.6 | 14.5 | 12.9 | 4.1 | 0.4 | 6.6 | 17.5% | 4.6% |
| DOUBLES | 2,113 | 5.1 | 4.3 | 12.0 | 10.7 | 20.4 | 25.3 | 22.1 | 23.84 | 67.9% | 47.5% |
| ITF_MEN | 7,431 | 13.8 | 10.1 | 22.9 | 16.4 | 21.3 | 11.7 | 3.8 | 10.86 | 36.7% | 15.4% |
| ITF_WOMEN | 8,992 | 13.8 | 9.6 | 21.2 | 16.4 | 21.3 | 14.2 | 3.5 | 11.47 | 39.0% | 17.7% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,567 | 24.5 | 16.7 | 30.4 | 17.0 | 9.1 | 2.2 | 0.1 | 6.37 | 11.4% | 2.3% |
| WTA125 | 1,050 | 26.1 | 13.6 | 22.1 | 20.5 | 12.5 | 4.8 | 0.5 | 7.38 | 17.7% | 5.2% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,251 | 5.2 | 4.3 | 11.8 | 10.5 | 20.7 | 25.4 | 22.2 | 23.85 | 68.2% | 47.6% |
| singles | 28,583 | 16.6 | 11.4 | 23.0 | 15.5 | 18.1 | 11.2 | 4.2 | 9.75 | 33.5% | 15.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 8,091 | 13.2 | 9.3 | 20.2 | 15.8 | 19.0 | 13.6 | 8.8 | 12.27 | 41.5% | 22.5% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 27,297 | 13.5 | 8.7 | 18.8 | 15.0 | 19.2 | 14.8 | 10.0 | 12.91 | 44.0% | 24.8% |
| UNKNOWN | 5,730 | 10.4 | 7.7 | 17.2 | 16.3 | 21.3 | 16.1 | 11.1 | 14.27 | 48.4% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 11,641 | 20.1 | 11.9 | 22.6 | 15.6 | 14.8 | 8.9 | 6.1 | 8.52 | 29.8% | 15.0% |
| B | 5,170 | 12.9 | 8.9 | 19.5 | 15.8 | 19.4 | 12.6 | 10.9 | 12.54 | 42.8% | 23.5% |
| C | 5,911 | 11.7 | 8.8 | 19.9 | 15.7 | 18.5 | 14.5 | 10.7 | 12.89 | 43.8% | 25.3% |
| D | 6,549 | 11.8 | 8.4 | 17.7 | 15.2 | 21.6 | 15.8 | 9.4 | 13.79 | 46.9% | 25.2% |
| F | 12,096 | 7.4 | 5.6 | 15.1 | 14.8 | 23.3 | 20.9 | 13.0 | 17.63 | 57.2% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,356 | 24.4 | 16.0 | 29.2 | 14.9 | 10.7 | 3.5 | 1.2 | 6.41 | 15.5% | 4.8% |
| B | 4,394 | 16.7 | 10.7 | 24.1 | 16.9 | 18.8 | 9.7 | 3.1 | 9.7 | 31.7% | 12.8% |
| C | 6,043 | 11.3 | 7.8 | 19.1 | 14.5 | 21.0 | 15.9 | 10.4 | 13.69 | 47.2% | 26.3% |
| D | 4,518 | 14.2 | 9.9 | 21.7 | 15.5 | 19.9 | 13.3 | 5.4 | 11.26 | 38.7% | 18.8% |
| F | 7,523 | 10.0 | 8.3 | 16.0 | 14.8 | 23.2 | 19.8 | 7.7 | 15.4 | 50.7% | 27.5% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 13,150 | 18.3 | 10.9 | 21.8 | 15.4 | 15.1 | 9.8 | 8.8 | 9.7 | 33.7% | 18.6% |
| LIMITED | 9,193 | 13.6 | 9.9 | 20.5 | 16.0 | 19.2 | 13.2 | 7.6 | 11.77 | 40.0% | 20.8% |
| POOR | 19,024 | 9.0 | 6.6 | 16.1 | 15.0 | 22.6 | 19.0 | 11.8 | 16.09 | 53.4% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,303 | 24.0 | 17.9 | 33.1 | 15.7 | 6.3 | 2.6 | 0.4 | 5.89 | 9.3% | 3.0% |
| GAME_SPREAD | 6,217 | 22.3 | 15.1 | 32.7 | 16.9 | 9.0 | 3.3 | 0.6 | 6.74 | 12.9% | 3.9% |
| MATCH_WINNER | 30,834 | 15.7 | 10.9 | 22.2 | 15.2 | 18.3 | 12.2 | 5.5 | 10.28 | 36.0% | 17.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 15,055 | 27.8 | 16.7 | 30.7 | 12.7 | 9.4 | 2.5 | 0.3 | 5.65 | 12.2% | 2.8% |
| TOTAL_GAMES | 10,326 | 9.9 | 10.7 | 35.5 | 26.4 | 10.4 | 4.1 | 2.9 | 9.25 | 17.5% | 7.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,975 | 24.3 | 29.4 | 33.0 | 8.0 | 4.1 | 0.9 | 0.3 | 4.78 | 5.3% | 1.2% |
| GAME_SPREAD | 8,367 | 47.1 | 16.0 | 25.1 | 7.2 | 2.2 | 1.8 | 0.6 | 3.29 | 4.6% | 2.4% |
| TOTAL_GAMES | 14,716 | 6.7 | 9.6 | 40.1 | 30.8 | 7.3 | 3.3 | 2.3 | 9.27 | 12.9% | 5.6% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,986 | 23.8 | 16.6 | 34.9 | 14.8 | 7.0 | 2.6 | 0.4 | 6.05 | 9.9% | 2.9% |
| GAME_SPREAD | 8,370 | 20.2 | 13.6 | 28.1 | 20.2 | 12.3 | 4.5 | 1.1 | 7.75 | 17.9% | 5.7% |
| TOTAL_GAMES | 14,746 | 10.2 | 10.3 | 36.2 | 25.0 | 11.5 | 4.3 | 2.5 | 9.16 | 18.3% | 6.8% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 41,367 | 44.1% | 24.7% | 12.97 | 35.2% | 15.1% | 10.64 |
| gen1_elo | 41,367 | 44.0% | 24.5% | 12.85 | 35.0% | 15.1% | 10.51 |
| gen1_sr | 41,367 | 51.8% | 31.2% | 15.75 | 43.8% | 21.5% | 12.95 |
| gen2 | 41,367 | 50.8% | 31.4% | 15.38 | 43.8% | 23.2% | 12.79 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 18,963 | 15.6 | 10.5 | 21.4 | 17.2 | 20.1 | 11.9 | 3.3 | 10.68 | 35.2% | 15.2% |
| STALE | 22,404 | 10.7 | 7.2 | 16.7 | 13.8 | 19.0 | 17.2 | 15.5 | 15.64 | 51.7% | 32.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 24,302 | 16.4 | 11.2 | 22.9 | 15.3 | 17.7 | 11.7 | 4.7 | 9.85 | 34.2% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 72,201 | 24302 | 22435 | 25464 | 24.4 | 121.6 | 1451.1 |
| ge_15pp | 29,360 | 8306 | 7971 | 13083 | 26.9 | 435.0 | 1451.1 |
| ge_25pp | 15,667 | 4004 | 3471 | 8192 | 31.9 | 586.7 | 1431.1 |
| lt_10pp | 31,818 | 12280 | 10650 | 8888 | 22.4 | 47.0 | 1421.1 |

Current slate `SL-20261101T071753Z-8b9034ba`: 712 priced rows, quote age at build {'median': 16.6, 'max': 16.6}, freshness {'AGING': 712}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 47 | 0.0 | 0.0 | 34.0 | 6.4 | 34.0 | 21.3 | 4.3 | 19.92 | 59.6% | 25.5% |
| EXTERNAL_LONE_OUTLIER | 25 | 64.0 | 36.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.43 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,101 | 19.6 | 11.0 | 25.4 | 18.0 | 17.9 | 7.1 | 0.9 | 8.64 | 26.0% | 8.1% |
| KALSHI_LONE_OUTLIER | 27 | 3.7 | 3.7 | 77.8 | 7.4 | 3.7 | 3.7 | 0.0 | 6.42 | 7.4% | 3.7% |
| MARKETS_AGREE | 854 | 66.4 | 33.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.18 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,837 | 0.0 | 2.3 | 37.3 | 25.8 | 24.1 | 9.6 | 0.9 | 11.81 | 34.6% | 10.5% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 41,367 | 6891 (16.7%) | 26.7% | 1.1% | {"EXTERNAL_STALE": 4101, "AGREES_WITH_KALSHI": 1837, "ALL_AGREE": 854, "SUPPORTS_MODEL_DIRECTION": 46, "AGREES_WITH_MODEL": 27, "EXTERNAL_OUTLIER": 25, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 18,255 | 1730 (9.5%) | 36.7% | 1.7% | {"EXTERNAL_STALE": 1065, "AGREES_WITH_KALSHI": 635, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 10,201 | 537 (5.3%) | 35.9% | 2.4% | {"EXTERNAL_STALE": 331, "AGREES_WITH_KALSHI": 193, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,825 | 510 (10.6%) | 36.5% | 2.5% | {"EXTERNAL_STALE": 311, "AGREES_WITH_KALSHI": 186, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 16,769 | 3944 (23.5%) | 18.5% | 1.0% | {"EXTERNAL_STALE": 2298, "ALL_AGREE": 854, "AGREES_WITH_KALSHI": 728, "EXTERNAL_OUTLIER": 25, "AGREES_WITH_MODEL": 23, "SUPPORTS_MODEL_DIRECTION": 15, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 8,028 | 10.5 | 7.5 | 19.5 | 14.4 | 21.6 | 16.5 | 10.0 | 14.1 | 48.0% | 26.5% |
| 4-10x | 5,539 | 11.1 | 8.6 | 18.9 | 15.4 | 21.8 | 14.2 | 10.0 | 13.57 | 46.1% | 24.3% |
| <2x | 21,145 | 15.2 | 9.9 | 19.8 | 15.9 | 17.3 | 12.9 | 8.9 | 11.5 | 39.1% | 21.8% |
| >=10x | 6,655 | 10.4 | 6.4 | 15.1 | 14.5 | 21.8 | 19.0 | 12.8 | 16.3 | 53.6% | 31.8% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 10,819 | 12.7 | 8.8 | 19.8 | 15.8 | 19.1 | 13.4 | 10.3 | 12.67 | 42.8% | 23.7% |
| 300-1000 | 8,888 | 11.9 | 8.8 | 17.9 | 15.3 | 20.2 | 16.4 | 9.6 | 13.57 | 46.2% | 25.9% |
| <300 | 13,105 | 8.2 | 5.8 | 15.2 | 14.8 | 23.1 | 19.9 | 12.9 | 17.05 | 55.9% | 32.9% |
| >=3000 | 8,555 | 21.6 | 12.9 | 24.3 | 15.6 | 13.6 | 7.0 | 5.0 | 7.57 | 25.6% | 12.0% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1188 | 0.5497 | 0.4115 | 0.4941 | +0.056 | -0.083 | -0.0019 ± 0.0045 |
| ratio 4-10x | 818 | 0.5818 | 0.4359 | 0.4951 | +0.087 | -0.059 | 0.0082 ± 0.0056 |
| ratio <2x | 2922 | 0.5371 | 0.4152 | 0.4432 | +0.094 | -0.028 | 0.0127 ± 0.0026 |
| ratio >=10x | 1012 | 0.5679 | 0.3927 | 0.4506 | +0.117 | -0.058 | 0.0141 ± 0.0057 |
| thinner_sample 1000-3000 | 1653 | 0.5386 | 0.4126 | 0.4489 | +0.090 | -0.036 | 0.0096 ± 0.0035 |
| thinner_sample 300-1000 | 1337 | 0.5685 | 0.4272 | 0.4854 | +0.083 | -0.058 | 0.0029 ± 0.0043 |
| thinner_sample <300 | 1942 | 0.5596 | 0.3918 | 0.4588 | +0.101 | -0.067 | 0.0114 ± 0.004 |
| thinner_sample >=3000 | 1008 | 0.5314 | 0.4383 | 0.4573 | +0.074 | -0.019 | 0.014 ± 0.0036 |
| data_status ADEQUATE | 1647 | 0.5329 | 0.4309 | 0.4444 | +0.088 | -0.013 | 0.0137 ± 0.003 |
| data_status LIMITED | 1464 | 0.5494 | 0.417 | 0.472 | +0.077 | -0.055 | 0.0065 ± 0.0039 |
| data_status POOR | 2829 | 0.5623 | 0.4015 | 0.4666 | +0.096 | -0.065 | 0.0084 ± 0.0033 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 873 | 0.2003 | 0.2007 | -0.0004 ± 0.0005 | 0.5811 | 0.5822 | 0.5027 | 0.4875 | 0.5063 | -0.088 ± 0.0161 | -0.01 (5) |
| 3-5 | 546 | 0.2044 | 0.2044 | +0.0000 ± 0.0016 | 0.5905 | 0.5894 | 0.5052 | 0.4654 | 0.4835 | -0.102 ± 0.0199 | 0.02 (1) |
| 5-10 | 1265 | 0.2021 | 0.2015 | +0.0006 ± 0.0019 | 0.5906 | 0.5869 | 0.5105 | 0.4368 | 0.4672 | -0.092 ± 0.0131 | -0.0167 (6) |
| 10-15 | 1032 | 0.2202 | 0.2111 | +0.0091 ± 0.0036 | 0.6327 | 0.6071 | 0.5284 | 0.4047 | 0.4283 | -0.109 ± 0.0144 | -0.048 (5) |
| 15-25 | 1308 | 0.2259 | 0.2119 | +0.0140 ± 0.005 | 0.6476 | 0.6079 | 0.5763 | 0.3812 | 0.4434 | -0.101 ± 0.0128 | -0.0033 (9) |
| 25-40 | 757 | 0.2234 | 0.2064 | +0.0171 ± 0.0099 | 0.637 | 0.5946 | 0.6551 | 0.3451 | 0.4729 | -0.074 ± 0.0151 | -0.01 (1) |
| 40+ | 159 | 0.2822 | 0.1885 | +0.0938 ± 0.03 | 0.7687 | 0.5556 | 0.7384 | 0.2904 | 0.4151 | -0.073 ± 0.0297 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4743 | 0.1853 | 0.1862 | -0.0009 ± 0.0002 | 0.5458 | 0.5469 | 0.487 | 0.4718 | 0.5028 | -0.022 ± 0.0064 | -0.0129 (17) |
| 3-5 | 3181 | 0.1953 | 0.1934 | +0.0019 ± 0.0006 | 0.5692 | 0.5624 | 0.483 | 0.4432 | 0.4379 | -0.060 ± 0.0079 | 0.0 (2) |
| 5-10 | 6833 | 0.2019 | 0.1982 | +0.0036 ± 0.0008 | 0.5897 | 0.5778 | 0.4856 | 0.4121 | 0.4248 | -0.047 ± 0.0055 | -0.0119 (21) |
| 10-15 | 5617 | 0.2019 | 0.1858 | +0.0161 ± 0.0014 | 0.59 | 0.546 | 0.4854 | 0.3615 | 0.3578 | -0.066 ± 0.0058 | -0.0281 (16) |
| 15-25 | 7041 | 0.207 | 0.1685 | +0.0385 ± 0.0019 | 0.6066 | 0.4997 | 0.4996 | 0.3039 | 0.3044 | -0.069 ± 0.0049 | -0.0025 (44) |
| 25-40 | 5488 | 0.2217 | 0.1253 | +0.0964 ± 0.003 | 0.6377 | 0.3854 | 0.5258 | 0.2118 | 0.2196 | -0.059 ± 0.0046 | -0.01 (1) |
| 40+ | 3645 | 0.3839 | 0.0451 | +0.3388 ± 0.004 | 1.0003 | 0.1736 | 0.6332 | 0.1041 | 0.0609 | -0.077 ± 0.0033 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 692 | 0.2068 | 0.2074 | -0.0007 ± 0.0006 | 0.5958 | 0.5976 | 0.5061 | 0.4913 | 0.5231 | -0.097 ± 0.0187 | -0.01 (3) |
| 3-5 | 493 | 0.2178 | 0.2155 | +0.0023 ± 0.0017 | 0.6192 | 0.6149 | 0.5156 | 0.476 | 0.4625 | -0.125 ± 0.0224 | 0.02 (1) |
| 5-10 | 1101 | 0.2076 | 0.2055 | +0.0021 ± 0.0021 | 0.6014 | 0.5956 | 0.5416 | 0.4668 | 0.4923 | -0.096 ± 0.0141 | -0.01 (4) |
| 10-15 | 959 | 0.2148 | 0.2099 | +0.0049 ± 0.0037 | 0.6202 | 0.6068 | 0.5653 | 0.441 | 0.487 | -0.100 ± 0.0154 | -0.04 (5) |
| 15-25 | 1374 | 0.23 | 0.2135 | +0.0165 ± 0.0049 | 0.6547 | 0.6116 | 0.5832 | 0.3879 | 0.4454 | -0.097 ± 0.0127 | -0.0133 (9) |
| 25-40 | 965 | 0.2687 | 0.1996 | +0.0691 ± 0.009 | 0.7505 | 0.5801 | 0.6602 | 0.3463 | 0.3959 | -0.128 ± 0.0144 | -0.0075 (4) |
| 40+ | 356 | 0.3672 | 0.1647 | +0.2025 ± 0.0213 | 1.004 | 0.4966 | 0.7325 | 0.2473 | 0.2949 | -0.086 ± 0.0208 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4076 | 0.1916 | 0.1918 | -0.0003 ± 0.0002 | 0.5589 | 0.5592 | 0.5075 | 0.4925 | 0.5103 | -0.038 ± 0.0071 | -0.0133 (15) |
| 3-5 | 2787 | 0.1947 | 0.1936 | +0.0011 ± 0.0007 | 0.5656 | 0.5623 | 0.5115 | 0.4718 | 0.4765 | -0.047 ± 0.0085 | 0.02 (1) |
| 5-10 | 6080 | 0.1988 | 0.1953 | +0.0035 ± 0.0009 | 0.5828 | 0.5702 | 0.5099 | 0.4358 | 0.4521 | -0.042 ± 0.0057 | -0.0117 (6) |
| 10-15 | 5052 | 0.2034 | 0.1921 | +0.0113 ± 0.0015 | 0.5961 | 0.5619 | 0.5122 | 0.3884 | 0.4056 | -0.049 ± 0.0063 | -0.0189 (18) |
| 15-25 | 7064 | 0.2169 | 0.1807 | +0.0361 ± 0.002 | 0.6308 | 0.5306 | 0.5227 | 0.3275 | 0.3356 | -0.062 ± 0.0051 | -0.0086 (42) |
| 25-40 | 6431 | 0.2512 | 0.1367 | +0.1145 ± 0.0029 | 0.7092 | 0.4183 | 0.5583 | 0.2416 | 0.2227 | -0.084 ± 0.0046 | -0.0044 (18) |
| 40+ | 5058 | 0.4001 | 0.0586 | +0.3415 ± 0.0039 | 1.0559 | 0.2113 | 0.6537 | 0.1179 | 0.0809 | -0.073 ± 0.0033 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 823 | 0.1956 | 0.1977 | -0.0021 ± 0.0005 | 0.5704 | 0.5757 | 0.5033 | 0.488 | 0.548 | -0.038 ± 0.0162 | -0.0137 (8) |
| 3-5 | 588 | 0.2055 | 0.2035 | +0.0020 ± 0.0015 | 0.5946 | 0.5886 | 0.4975 | 0.4579 | 0.4541 | -0.121 ± 0.0194 | 0.0067 (3) |
| 5-10 | 1307 | 0.2036 | 0.2009 | +0.0027 ± 0.0019 | 0.5929 | 0.5845 | 0.5111 | 0.4373 | 0.4545 | -0.102 ± 0.0128 | -0.0071 (7) |
| 10-15 | 1037 | 0.209 | 0.2036 | +0.0055 ± 0.0035 | 0.6079 | 0.5905 | 0.5406 | 0.4173 | 0.4581 | -0.098 ± 0.014 | -0.0317 (6) |
| 15-25 | 1244 | 0.236 | 0.2176 | +0.0183 ± 0.0051 | 0.6713 | 0.6205 | 0.5891 | 0.3949 | 0.4445 | -0.113 ± 0.0133 | -0.03 (1) |
| 25-40 | 773 | 0.2129 | 0.2123 | +0.0006 ± 0.0097 | 0.6142 | 0.6085 | 0.6629 | 0.3527 | 0.5045 | -0.059 ± 0.0149 | 0.015 (2) |
| 40+ | 168 | 0.3002 | 0.1961 | +0.1040 ± 0.0301 | 0.8181 | 0.5732 | 0.7497 | 0.3001 | 0.4167 | -0.080 ± 0.0314 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4527 | 0.1842 | 0.1849 | -0.0007 ± 0.0002 | 0.5421 | 0.5433 | 0.4826 | 0.4673 | 0.4891 | -0.029 ± 0.0065 | -0.0163 (35) |
| 3-5 | 3169 | 0.2023 | 0.2001 | +0.0023 ± 0.0006 | 0.5882 | 0.581 | 0.4814 | 0.4419 | 0.4336 | -0.064 ± 0.0081 | -0.0094 (18) |
| 5-10 | 6969 | 0.1943 | 0.1898 | +0.0045 ± 0.0008 | 0.5716 | 0.557 | 0.4875 | 0.4135 | 0.4206 | -0.051 ± 0.0053 | -0.01 (31) |
| 10-15 | 5597 | 0.1924 | 0.179 | +0.0134 ± 0.0014 | 0.5691 | 0.5301 | 0.4959 | 0.3725 | 0.3793 | -0.056 ± 0.0057 | -0.015 (12) |
| 15-25 | 7186 | 0.2143 | 0.1745 | +0.0399 ± 0.0019 | 0.6233 | 0.5131 | 0.5141 | 0.3196 | 0.3158 | -0.072 ± 0.0049 | -0.03 (2) |
| 25-40 | 5491 | 0.2164 | 0.1282 | +0.0883 ± 0.003 | 0.6261 | 0.392 | 0.5292 | 0.2137 | 0.2337 | -0.049 ± 0.0047 | 0.01 (3) |
| 40+ | 3609 | 0.3934 | 0.0506 | +0.3428 ± 0.0042 | 1.0261 | 0.1879 | 0.6425 | 0.1108 | 0.0676 | -0.077 ± 0.0036 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1242 | 0.1951 | 0.1952 | -0.0001 ± 0.0004 | 0.5685 | 0.5685 | 0.5065 | 0.4914 | 0.496 | -0.069 ± 0.0128 | -0.0224 (49) |
| 3-5 | 879 | 0.1891 | 0.1887 | +0.0004 ± 0.0012 | 0.555 | 0.5529 | 0.4963 | 0.4565 | 0.4699 | -0.062 ± 0.015 | -0.0194 (34) |
| 5-10 | 1829 | 0.2012 | 0.1966 | +0.0046 ± 0.0016 | 0.5908 | 0.5764 | 0.504 | 0.4303 | 0.4363 | -0.076 ± 0.0106 | -0.005 (78) |
| 10-15 | 1244 | 0.2174 | 0.2038 | +0.0135 ± 0.0032 | 0.6272 | 0.5918 | 0.5394 | 0.4166 | 0.4212 | -0.093 ± 0.0132 | 0.0014 (64) |
| 15-25 | 1599 | 0.2319 | 0.2102 | +0.0217 ± 0.0045 | 0.6609 | 0.6052 | 0.5847 | 0.3899 | 0.4346 | -0.086 ± 0.0116 | -0.0214 (59) |
| 25-40 | 992 | 0.2435 | 0.2113 | +0.0322 ± 0.0089 | 0.6961 | 0.6052 | 0.6849 | 0.3728 | 0.4778 | -0.092 ± 0.0137 | -0.0219 (26) |
| 40+ | 334 | 0.3367 | 0.2039 | +0.1328 ± 0.0238 | 0.9776 | 0.5933 | 0.8173 | 0.341 | 0.4551 | -0.103 ± 0.0225 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4681 | 0.1757 | 0.1759 | -0.0002 ± 0.0002 | 0.5205 | 0.5206 | 0.5107 | 0.4955 | 0.5078 | -0.037 ± 0.0062 | -0.0157 (88) |
| 3-5 | 3231 | 0.1946 | 0.1936 | +0.0010 ± 0.0006 | 0.5669 | 0.5646 | 0.5022 | 0.4624 | 0.4695 | -0.044 ± 0.0078 | -0.0209 (69) |
| 5-10 | 6609 | 0.1986 | 0.1921 | +0.0065 ± 0.0008 | 0.5837 | 0.5647 | 0.5001 | 0.4264 | 0.4205 | -0.063 ± 0.0055 | -0.0082 (132) |
| 10-15 | 4564 | 0.2116 | 0.1956 | +0.0160 ± 0.0016 | 0.6141 | 0.5727 | 0.537 | 0.414 | 0.4089 | -0.071 ± 0.0066 | -0.0053 (105) |
| 15-25 | 5491 | 0.2303 | 0.2007 | +0.0297 ± 0.0024 | 0.6623 | 0.5809 | 0.5721 | 0.3766 | 0.3999 | -0.064 ± 0.0061 | -0.0253 (107) |
| 25-40 | 3685 | 0.2598 | 0.1885 | +0.0713 ± 0.0045 | 0.7353 | 0.5497 | 0.6368 | 0.3242 | 0.3691 | -0.075 ± 0.007 | -0.0229 (51) |
| 40+ | 1582 | 0.3771 | 0.1567 | +0.2204 ± 0.0103 | 1.0681 | 0.4668 | 0.7432 | 0.241 | 0.2832 | -0.071 ± 0.0095 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5940 | 1.018 ± 0.036 | 1.091 | 0.1688 | 0.1659 | 0.2153 | 0.2059 |
| gen2 | 5940 | 0.807 ± 0.033 | 1.062 | 0.1714 | 0.1663 | 0.2342 | 0.2057 |
| gen1_elo | 5940 | 0.995 ± 0.035 | 1.085 | 0.1755 | 0.166 | 0.2144 | 0.206 |
| gen1_sr | 5940 | 0.992 ± 0.043 | 1.121 | 0.1317 | 0.1682 | 0.2302 | 0.2054 |
| gen1_ledger | 8119 | 0.856 ± 0.026 | 1.061 | 0.1876 | 0.1752 | 0.2182 | 0.2014 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 29,360)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,606 | 22.5% |
| STALE_QUOTE | market_freshness | 6,480 | 22.1% |
| BOOK_QUALITY | execution | 5,533 | 18.9% |
| POOR_DATA | data | 3,403 | 11.6% |
| LIMITED_DATA | data | 1,850 | 6.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,679 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,249 | 4.2% |
| IDENTITY_AMBIGUOUS | mapping | 1,210 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 846 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 503 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.5%, market_freshness 22.1%, execution 18.9%, data 17.9%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.2%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.4%, START_UNVERIFIABLE 94.4%, LOW_DATA_QUALITY 71.5%, THIN_PLAYER_HISTORY 59.8%, STALE_PLAYER_DATA 52.2%, STALE_KALSHI_QUOTE 44.6%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 24.9%, MODEL_HIGH_UNCERTAINTY 18.3%, PLAYER_IDENTITY_RISK 15.6%, LEVEL_TRANSFER_RISK 10.4%, LOW_DISPLAYED_LIQUIDITY 8.1%, EVENT_MAPPING_RISK 7.6%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 3.4%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.0%, POST_SETTLEMENT_OBSERVATION 22.5%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 15,667)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,333 | 34.0% |
| STALE_QUOTE | market_freshness | 2,926 | 18.7% |
| BOOK_QUALITY | execution | 2,886 | 18.4% |
| POOR_DATA | data | 1,457 | 9.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 883 | 5.6% |
| IDENTITY_AMBIGUOUS | mapping | 658 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 548 | 3.5% |
| LIMITED_DATA | data | 542 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 308 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 125 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.0%, market_freshness 18.7%, execution 18.4%, data 12.8%, market_freshness/coverage 9.1%, mapping 4.2%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 75.0%, THIN_PLAYER_HISTORY 62.0%, STALE_KALSHI_QUOTE 52.3%, STALE_PLAYER_DATA 46.1%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 34.2%, WIDE_SPREAD 24.4%, MODEL_HIGH_UNCERTAINTY 19.0%, PLAYER_IDENTITY_RISK 18.5%, LEVEL_TRANSFER_RISK 9.3%, EVENT_MAPPING_RISK 9.2%, LOW_DISPLAYED_LIQUIDITY 8.0%, MODEL_CALIBRATION_OUTLIER 5.0%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.1%, POST_SETTLEMENT_OBSERVATION 34.0%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 12446, "IDENTITY_AMBIGUOUS": 3221}; ticker orientation: {"VERIFIED": 15667}.

Checks: discipline:AMBIGUOUS 1071, discipline:PASS 14596, identity_confidence:AMBIGUOUS 2897, identity_confidence:PASS 12770, level_mapping:NA 1083, level_mapping:PASS 14584, market_pair:AMBIGUOUS 483, market_pair:NA 352, market_pair:PASS 14832, model_complement:NA 315, model_complement:PASS 15352, namesake:AMBIGUOUS 6, namesake:PASS 15661, physical_match_id:NA 5466, physical_match_id:PASS 10201, player_ids:PASS 15667, same_pair_other_event:PASS 15667, ticker_orientation:PASS 15667

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,838 | 3.9% | 3.5% | 1.5% | {"market_freshness": 56, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 17, "coverage": 13} | 5.74 | 0.2217 / 0.2167 (687) | 22.9% | 2.7% | 3.1% | 2.7% |
| CHALLENGER | 10,311 | 16.4% | 6.2% | 10.8% | {"coverage": 991, "market_freshness/coverage": 202, "market_freshness": 174, "data": 152, "model_calibration_or_unknown": 74, "execution": 40, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.26 | 0.2213 / 0.2117 (2337) | 35.5% | 15.7% | 4.1% | 22.4% |
| DOUBLES | 2,251 | 47.6% | 47.5% | 6.8% | {"execution": 606, "mapping": 291, "market_freshness": 106, "market_freshness/coverage": 61, "coverage": 7} | 23.84 | 0.307 / 0.2392 (538) | 10.4% | 0.0% | 100.0% | 6.1% |
| ITF_MEN | 20,253 | 25.0% | 17.5% | 32.4% | {"coverage": 1801, "market_freshness": 928, "execution": 915, "data": 742, "market_freshness/coverage": 491, "mapping": 183, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.66 | 0.2163 / 0.2001 (4182) | 38.2% | 68.8% | 16.2% | 21.8% |
| ITF_WOMEN | 26,786 | 26.5% | 19.1% | 45.3% | {"coverage": 2477, "market_freshness": 1501, "execution": 1243, "data": 1007, "market_freshness/coverage": 606, "mapping": 161, "model_calibration_or_unknown": 82, "model_calibration": 21} | 12.52 | 0.2046 / 0.1954 (4910) | 39.8% | 57.1% | 9.9% | 21.4% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,264 | 5.8% | 4.9% | 1.6% | {"market_freshness": 85, "model_calibration_or_unknown": 44, "coverage": 31, "execution": 29, "data": 24, "model_calibration": 19, "market_freshness/coverage": 12, "mapping": 1} | 7.46 | 0.2298 / 0.223 (669) | 27.1% | 1.7% | 1.5% | 3.6% |
| WTA125 | 2,343 | 11.1% | 9.5% | 1.7% | {"market_freshness": 74, "model_calibration_or_unknown": 51, "market_freshness/coverage": 41, "data": 38, "execution": 24, "model_calibration": 16, "coverage": 12, "mapping": 4} | 9.17 | 0.2118 / 0.1931 (694) | 26.6% | 10.6% | 4.6% | 7.3% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 17.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 1025 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 769 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 869 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 9 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 10 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); no external reference |
| 13 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 14 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 207 min (STALE); no external reference |
| 17 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 18 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
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
| 30 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 31 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 32 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 33 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 34 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 35 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 36 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 37 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 38 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 39 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 463 min (STALE); no external reference |
| 40 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 41 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 42 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 43 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 44 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 379 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 45 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 46 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.3h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 748 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |
| 47 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 49 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFWMATCH-26OCT31KUHDEK-KUH` | ITF_WOMEN | fair_v1 | 84% / 6% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 224 min (STALE); data LIMITED (grade C, thinner serve sample 1253.0, ratio 1.41); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.97, "by_level_share_of_ge_25pp": {"ATP": 0.0145, "CHALLENGER": 0.1076, "DOUBLES": 0.0684, "ITF_MEN": 0.3235, "ITF_WOMEN": 0.4531, "OTHER": 0.0008, "WTA": 0.0156, "WTA125": 0.0166}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5229, "share_primary_cause_market_settled_or_in_play": 0.4318, "share_primary_cause_stale_quote_only": 0.1868}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 15667, "identity_ambiguous_share": 0.2056, "ticker_orientation": {"VERIFIED": 15667}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 10201, "with_external": 537, "coverage": 0.0526, "external_status": {"EXTERNAL_STALE": 331, "AGREES_WITH_KALSHI": 193, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 331, "MODEL_LONE_OUTLIER": 193, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3594, "share_external_supports_model": 0.0242}, "pregame_clean_ge_25pp": {"n": 4825, "with_external": 510, "coverage": 0.1057, "external_status": {"EXTERNAL_STALE": 311, "AGREES_WITH_KALSHI": 186, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 311, "MODEL_LONE_OUTLIER": 186, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3647, "share_external_supports_model": 0.0255}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 485.0, "median_sample_ratio": 2.48, "median_min_matches": 20.0, "median_max_days_since_last": 237.0, "share_severe_asymmetry": 0.208, "data_status": {"POOR": 8801, "LIMITED": 4117, "ADEQUATE": 2749}, "comparison_lt_10pp": {"median_thinner_serve_points": 1748.0, "median_sample_ratio": 1.69, "median_min_matches": 92.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1188, "model_minus_observed": 0.0555, "kalshi_minus_observed": -0.0826, "brier_diff_model_minus_kalshi": -0.0019}, "4-10x": {"n": 818, "model_minus_observed": 0.0867, "kalshi_minus_observed": -0.0592, "brier_diff_model_minus_kalshi": 0.0082}, "<2x": {"n": 2922, "model_minus_observed": 0.0939, "kalshi_minus_observed": -0.028, "brier_diff_model_minus_kalshi": 0.0127}, ">=10x": {"n": 1012, "model_minus_observed": 0.1173, "kalshi_minus_observed": -0.0579, "brier_diff_model_minus_kalshi": 0.0141}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 5940, "model": {"intercept": -0.528, "slope": 0.807, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.196, "slope": 1.062, "slope_se": 0.037}, "mean_extremity_model": 0.1714, "mean_extremity_kalshi": 0.1663, "model_brier": 0.2342, "kalshi_brier": 0.2057, "brier_diff_model_minus_kalshi": 0.0285, "brier_diff_se": 0.0024, "model_logloss": 0.666, "kalshi_logloss": 0.5945}, "fair_v1": {"n": 5940, "model": {"intercept": -0.425, "slope": 1.018, "slope_se": 0.036}, "kalshi_mid_same_rows": {"intercept": 0.264, "slope": 1.091, "slope_se": 0.037}, "mean_extremity_model": 0.1688, "mean_extremity_kalshi": 0.1659, "model_brier": 0.2153, "kalshi_brier": 0.2059, "brier_diff_model_minus_kalshi": 0.0094, "brier_diff_se": 0.002, "model_logloss": 0.6197, "kalshi_logloss": 0.5947}, "gen1_elo": {"n": 5940, "model": {"intercept": -0.407, "slope": 0.995, "slope_se": 0.035}, "kalshi_mid_same_rows": {"intercept": 0.279, "slope": 1.085, "slope_se": 0.037}, "mean_extremity_model": 0.1755, "mean_extremity_kalshi": 0.166, "model_brier": 0.2144, "kalshi_brier": 0.206, "brier_diff_model_minus_kalshi": 0.0083, "brier_diff_se": 0.002, "model_logloss": 0.6181, "kalshi_logloss": 0.5951}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2466, "share_ge_15": 0.4413, "median_abs_gap": 12.97, "n": 41367}, "gen1_elo": {"share_ge_25": 0.245, "share_ge_15": 0.44, "median_abs_gap": 12.85, "n": 41367}, "gen1_sr": {"share_ge_25": 0.3116, "share_ge_15": 0.5181, "median_abs_gap": 15.75, "n": 41367}, "gen2": {"share_ge_25": 0.3143, "share_ge_15": 0.5081, "median_abs_gap": 15.38, "n": 41367}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1508, "share_ge_15": 0.3524, "median_abs_gap": 10.64, "n": 31995}, "gen1_elo": {"share_ge_25": 0.1507, "share_ge_15": 0.3503, "median_abs_gap": 10.51, "n": 31994}, "gen1_sr": {"share_ge_25": 0.2153, "share_ge_15": 0.4379, "median_abs_gap": 12.95, "n": 31997}, "gen2": {"share_ge_25": 0.2315, "share_ge_15": 0.4376, "median_abs_gap": 12.79, "n": 31997}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.74, "share_ge_25_all": 0.0389, "share_ge_25_pregame_clean": 0.0347}, "WTA": {"median_abs_gap_pregame_clean": 7.46, "share_ge_25_all": 0.0575, "share_ge_25_pregame_clean": 0.0491}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2378, "share_within_10pp_all": 0.4407, "share_within_10pp_pregame_clean": 0.4936, "corr_model_vs_mid_pregame_clean": 0.8511}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 873, "model_brier": 0.2003, "kalshi_brier": 0.2007, "brier_diff_model_minus_kalshi": -0.0004}, "10-15": {"n_settled": 1032, "model_brier": 0.2202, "kalshi_brier": 0.2111, "brier_diff_model_minus_kalshi": 0.0091}, "15-25": {"n_settled": 1308, "model_brier": 0.2259, "kalshi_brier": 0.2119, "brier_diff_model_minus_kalshi": 0.014}, "25-40": {"n_settled": 757, "model_brier": 0.2234, "kalshi_brier": 0.2064, "brier_diff_model_minus_kalshi": 0.0171}, "3-5": {"n_settled": 546, "model_brier": 0.2044, "kalshi_brier": 0.2044, "brier_diff_model_minus_kalshi": 0.0}, "40+": {"n_settled": 159, "model_brier": 0.2822, "kalshi_brier": 0.1885, "brier_diff_model_minus_kalshi": 0.0938}, "5-10": {"n_settled": 1265, "model_brier": 0.2021, "kalshi_brier": 0.2015, "brier_diff_model_minus_kalshi": 0.0006}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.528, "slope": 0.807, "slope_se": 0.033}, "kalshi_slope": {"intercept": 0.196, "slope": 1.062, "slope_se": 0.037}, "n": 5940}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.486, "slope": 0.856, "slope_se": 0.026}, "kalshi_slope": {"intercept": 0.164, "slope": 1.061, "slope_se": 0.031}, "n": 8119}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 538, "model_brier": 0.307, "kalshi_brier": 0.2392, "brier_diff_model_minus_kalshi": 0.0677, "brier_diff_se": 0.0129, "corr_model_outcome": 0.0537, "corr_kalshi_outcome": 0.2246}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
