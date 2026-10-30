# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-30T23:15Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 70,519): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 19.0%, 25-40 13.8%, 40+ 8.1%; median gap 11.85 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.9%, Challenger 10.8%, doubles 6.6%). Main tour: ATP 4.1% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 15,382): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.2%, STALE_QUOTE 18.7%, BOOK_QUALITY 18.3%, POOR_DATA 9.3%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IDENTITY_AMBIGUOUS 4.1%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.2%, market_freshness 18.7%, execution 18.3%, data 12.7%, market_freshness/coverage 9.1%, mapping 4.1%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.4% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.3% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 15,382 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.4% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.3% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 476.0 points vs 1702.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.021, Gen-2 0.808, Gen-1 ledger 0.859 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 747 model 0.2232 vs Kalshi 0.2055; n 157 model 0.2855 vs Kalshi 0.1866.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 299,698 model-market comparisons (489,927 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 100,743 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-30T23:04:53.511357+00:00'], shadow board 80,594 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-30T23:04:56.705820+00:00'], Model 4 37,274 rows, 24,415 settled tickers, 8,921 tickers with an external scan.
* By model: {"gen1_ledger": 67808, "gen1_elo": 40507, "fair_v1": 40507, "gen2": 40507, "gen1_sr": 40507, "model4_fundamental": 34953, "model4_conditioned": 34909}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 70,519 | 14.1 | 9.6 | 20.2 | 15.3 | 19.0 | 13.8 | 8.1 | 11.85 | 40.8% | 21.8% |
| MW fair_v1 | 40,507 | 12.9 | 8.7 | 18.7 | 15.4 | 19.5 | 14.8 | 10.0 | 13.01 | 44.3% | 24.8% |
| MW gen1_elo | 40,507 | 12.5 | 8.6 | 19.3 | 15.4 | 19.5 | 14.8 | 9.9 | 12.93 | 44.1% | 24.6% |
| MW gen1_ledger | 30,012 | 15.6 | 10.8 | 22.2 | 15.3 | 18.4 | 12.3 | 5.5 | 10.34 | 36.2% | 17.8% |
| MW gen1_sr | 40,507 | 10.2 | 7.2 | 16.9 | 13.8 | 20.7 | 18.6 | 12.8 | 15.85 | 52.0% | 31.3% |
| MW gen2 | 40,507 | 11.1 | 7.6 | 16.6 | 13.8 | 19.3 | 17.8 | 13.8 | 15.44 | 50.9% | 31.6% |
| all families model4_conditioned | 34,909 | 22.5 | 18.3 | 34.1 | 17.1 | 4.9 | 1.9 | 1.1 | 5.98 | 8.0% | 3.1% |
| all families model4_fundamental | 34,953 | 17.4 | 13.4 | 33.9 | 20.2 | 10.1 | 3.6 | 1.4 | 7.65 | 15.2% | 5.0% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.2%, >=15pp 40.8%, >=20pp 30.2%, >=25pp 21.8%, >=30pp 15.7%, >=40pp 8.1%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.3pp; >=10pp 44.8%, >=25pp 17.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,469 | 27.4 | 15.4 | 27.9 | 13.4 | 11.4 | 4.0 | 0.6 | 5.92 | 16.0% | 4.5% |
| CHALLENGER | 6,004 | 16.2 | 9.7 | 20.9 | 15.1 | 15.4 | 11.7 | 11.0 | 10.91 | 38.0% | 22.7% |
| ITF_MEN | 11,396 | 9.8 | 7.4 | 17.0 | 15.1 | 21.2 | 17.6 | 12.0 | 15.24 | 50.7% | 29.5% |
| ITF_WOMEN | 15,963 | 9.7 | 7.1 | 15.9 | 15.1 | 22.0 | 18.1 | 12.2 | 15.67 | 52.2% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,535 | 18.4 | 13.6 | 25.0 | 19.9 | 15.9 | 6.2 | 1.1 | 8.18 | 23.2% | 7.3% |
| WTA125 | 1,134 | 16.5 | 7.3 | 22.4 | 19.1 | 21.0 | 11.9 | 1.9 | 10.73 | 34.7% | 13.8% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,469 | 26.0 | 15.4 | 26.1 | 16.0 | 11.8 | 4.0 | 0.8 | 6.22 | 16.6% | 4.8% |
| CHALLENGER | 6,004 | 15.1 | 9.0 | 18.2 | 14.2 | 18.1 | 13.5 | 11.8 | 12.51 | 43.4% | 25.3% |
| ITF_MEN | 11,396 | 8.0 | 6.2 | 15.1 | 13.9 | 19.4 | 20.8 | 16.6 | 17.95 | 56.8% | 37.4% |
| ITF_WOMEN | 15,963 | 8.0 | 5.8 | 14.0 | 12.8 | 20.6 | 21.1 | 17.6 | 19.09 | 59.4% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,535 | 15.3 | 11.1 | 22.2 | 15.2 | 21.9 | 12.5 | 1.9 | 10.53 | 36.3% | 14.4% |
| WTA125 | 1,134 | 9.9 | 6.6 | 16.9 | 15.9 | 24.2 | 17.7 | 8.8 | 15.21 | 50.7% | 26.5% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,469 | 22.1 | 13.4 | 24.6 | 15.9 | 16.1 | 6.6 | 1.3 | 7.58 | 24.0% | 7.9% |
| CHALLENGER | 6,004 | 15.0 | 9.3 | 20.9 | 16.1 | 15.6 | 12.1 | 11.1 | 11.34 | 38.8% | 23.2% |
| ITF_MEN | 11,396 | 9.3 | 7.2 | 17.4 | 14.2 | 21.8 | 17.7 | 12.4 | 15.73 | 51.9% | 30.1% |
| ITF_WOMEN | 15,963 | 9.4 | 6.9 | 16.4 | 15.8 | 22.0 | 17.9 | 11.5 | 15.49 | 51.5% | 29.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,535 | 23.6 | 16.5 | 32.2 | 14.4 | 9.1 | 3.0 | 1.3 | 6.08 | 13.3% | 4.3% |
| WTA125 | 1,134 | 21.6 | 12.9 | 26.8 | 17.6 | 15.0 | 5.8 | 0.3 | 7.99 | 21.2% | 6.2% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,045 | 24.6 | 19.2 | 31.1 | 12.8 | 9.1 | 2.9 | 0.5 | 5.73 | 12.4% | 3.4% |
| CHALLENGER | 4,058 | 22.6 | 14.6 | 27.4 | 14.5 | 13.5 | 5.9 | 1.6 | 7.08 | 21.0% | 7.5% |
| DOUBLES | 2,167 | 5.1 | 4.3 | 12.2 | 10.6 | 21.0 | 25.1 | 21.7 | 23.61 | 67.8% | 46.8% |
| ITF_MEN | 8,618 | 13.0 | 9.4 | 21.2 | 15.9 | 21.4 | 13.2 | 5.8 | 11.89 | 40.5% | 19.1% |
| ITF_WOMEN | 10,295 | 13.1 | 9.1 | 19.9 | 15.8 | 21.2 | 15.3 | 5.5 | 12.31 | 42.0% | 20.8% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,532 | 24.5 | 15.6 | 30.5 | 17.4 | 9.0 | 2.7 | 0.3 | 6.58 | 12.0% | 3.0% |
| WTA125 | 1,148 | 25.2 | 12.6 | 20.9 | 19.4 | 13.4 | 6.9 | 1.6 | 7.88 | 21.9% | 8.5% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,370 | 27.7 | 15.6 | 28.2 | 13.3 | 11.2 | 3.6 | 0.4 | 5.88 | 15.2% | 4.0% |
| CHALLENGER | 4,201 | 21.2 | 12.3 | 26.0 | 17.7 | 15.2 | 6.0 | 1.6 | 8.03 | 22.9% | 7.6% |
| ITF_MEN | 8,322 | 12.0 | 8.8 | 20.6 | 17.1 | 22.1 | 14.3 | 5.1 | 12.39 | 41.5% | 19.4% |
| ITF_WOMEN | 11,831 | 11.6 | 8.5 | 18.5 | 17.3 | 24.0 | 15.0 | 5.2 | 13.25 | 44.1% | 20.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,453 | 18.7 | 13.5 | 25.2 | 20.2 | 16.0 | 5.8 | 0.6 | 8.13 | 22.4% | 6.4% |
| WTA125 | 1,096 | 16.7 | 7.2 | 22.0 | 19.3 | 21.4 | 11.7 | 1.6 | 10.97 | 34.8% | 13.3% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,370 | 26.3 | 15.7 | 26.3 | 16.0 | 11.7 | 3.7 | 0.5 | 6.19 | 15.8% | 4.1% |
| CHALLENGER | 4,201 | 19.3 | 11.5 | 22.9 | 16.7 | 18.5 | 9.0 | 1.9 | 8.99 | 29.5% | 10.9% |
| ITF_MEN | 8,323 | 9.4 | 7.3 | 17.5 | 16.1 | 21.3 | 18.8 | 9.5 | 14.9 | 49.6% | 28.3% |
| ITF_WOMEN | 11,832 | 8.9 | 6.8 | 15.9 | 14.3 | 22.7 | 20.5 | 10.8 | 16.54 | 54.0% | 31.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,453 | 15.4 | 11.1 | 22.4 | 15.2 | 22.1 | 12.5 | 1.2 | 10.36 | 35.8% | 13.7% |
| WTA125 | 1,096 | 9.8 | 6.7 | 17.1 | 16.1 | 24.1 | 18.0 | 8.3 | 15.12 | 50.4% | 26.3% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,988 | 24.8 | 19.4 | 31.0 | 12.9 | 8.8 | 2.8 | 0.4 | 5.67 | 11.9% | 3.2% |
| CHALLENGER | 3,578 | 24.0 | 15.5 | 28.6 | 14.6 | 12.8 | 4.0 | 0.5 | 6.58 | 17.2% | 4.5% |
| DOUBLES | 2,031 | 5.0 | 4.4 | 12.4 | 10.8 | 20.8 | 25.0 | 21.6 | 23.54 | 67.4% | 46.6% |
| ITF_MEN | 7,357 | 13.8 | 10.0 | 22.9 | 16.4 | 21.4 | 11.7 | 3.8 | 10.94 | 36.9% | 15.5% |
| ITF_WOMEN | 8,769 | 13.7 | 9.6 | 21.1 | 16.5 | 21.3 | 14.3 | 3.5 | 11.5 | 39.0% | 17.7% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,478 | 24.9 | 16.0 | 30.5 | 17.4 | 9.0 | 2.2 | 0.1 | 6.44 | 11.2% | 2.2% |
| WTA125 | 1,020 | 26.5 | 13.4 | 22.0 | 20.5 | 12.3 | 4.8 | 0.5 | 7.32 | 17.6% | 5.3% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,167 | 5.1 | 4.3 | 12.2 | 10.6 | 21.0 | 25.1 | 21.7 | 23.61 | 67.8% | 46.8% |
| singles | 27,845 | 16.5 | 11.3 | 22.9 | 15.6 | 18.2 | 11.3 | 4.2 | 9.82 | 33.7% | 15.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 8,007 | 13.1 | 9.3 | 20.2 | 15.7 | 19.0 | 13.7 | 8.9 | 12.28 | 41.6% | 22.6% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 26,605 | 13.4 | 8.7 | 18.6 | 15.1 | 19.2 | 14.9 | 10.1 | 12.96 | 44.2% | 25.0% |
| UNKNOWN | 5,646 | 10.3 | 7.8 | 17.0 | 16.4 | 21.4 | 16.0 | 11.1 | 14.29 | 48.5% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 11,267 | 20.1 | 12.0 | 22.4 | 15.6 | 14.7 | 9.1 | 6.1 | 8.52 | 29.9% | 15.2% |
| B | 5,035 | 12.8 | 9.0 | 19.3 | 15.8 | 19.4 | 12.6 | 11.0 | 12.57 | 43.0% | 23.6% |
| C | 5,804 | 11.8 | 8.9 | 19.9 | 15.8 | 18.6 | 14.3 | 10.7 | 12.84 | 43.6% | 25.1% |
| D | 6,414 | 11.8 | 8.4 | 17.5 | 15.3 | 21.6 | 16.0 | 9.4 | 13.85 | 47.0% | 25.4% |
| F | 11,987 | 7.4 | 5.6 | 15.0 | 14.8 | 23.3 | 20.9 | 13.1 | 17.65 | 57.2% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,014 | 24.2 | 15.8 | 29.1 | 15.1 | 10.9 | 3.6 | 1.3 | 6.5 | 15.8% | 4.9% |
| B | 4,282 | 16.8 | 10.7 | 24.1 | 16.8 | 18.8 | 9.7 | 3.1 | 9.67 | 31.6% | 12.8% |
| C | 5,875 | 11.3 | 7.8 | 19.4 | 14.6 | 21.0 | 15.7 | 10.1 | 13.49 | 46.9% | 25.8% |
| D | 4,391 | 14.3 | 9.8 | 21.8 | 15.4 | 20.0 | 13.2 | 5.4 | 11.26 | 38.7% | 18.6% |
| F | 7,450 | 9.9 | 8.3 | 16.1 | 15.0 | 23.2 | 19.8 | 7.7 | 15.41 | 50.8% | 27.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 12,759 | 18.3 | 10.9 | 21.5 | 15.4 | 15.1 | 9.9 | 8.9 | 9.74 | 33.9% | 18.8% |
| LIMITED | 8,973 | 13.6 | 10.0 | 20.4 | 16.1 | 19.2 | 13.2 | 7.6 | 11.72 | 39.9% | 20.7% |
| POOR | 18,775 | 9.0 | 6.6 | 16.0 | 15.0 | 22.6 | 19.0 | 11.8 | 16.15 | 53.5% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,691 | 24.3 | 18.2 | 33.0 | 14.9 | 6.5 | 2.7 | 0.4 | 5.82 | 9.6% | 3.1% |
| GAME_SPREAD | 6,016 | 22.3 | 15.2 | 32.8 | 17.1 | 9.1 | 3.0 | 0.6 | 6.74 | 12.6% | 3.5% |
| MATCH_WINNER | 30,012 | 15.6 | 10.8 | 22.2 | 15.3 | 18.4 | 12.3 | 5.5 | 10.34 | 36.2% | 17.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 14,054 | 27.6 | 16.7 | 31.0 | 12.5 | 9.4 | 2.5 | 0.3 | 5.68 | 12.3% | 2.8% |
| TOTAL_GAMES | 10,011 | 9.9 | 10.7 | 35.6 | 26.6 | 10.4 | 4.0 | 2.8 | 9.25 | 17.2% | 6.8% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,335 | 24.6 | 30.1 | 32.8 | 7.3 | 4.1 | 0.9 | 0.3 | 4.7 | 5.2% | 1.2% |
| GAME_SPREAD | 8,170 | 47.5 | 16.0 | 25.1 | 7.2 | 2.2 | 1.4 | 0.6 | 3.25 | 4.1% | 1.9% |
| TOTAL_GAMES | 14,404 | 6.6 | 9.5 | 40.2 | 31.1 | 7.2 | 3.2 | 2.2 | 9.28 | 12.6% | 5.4% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,346 | 24.0 | 16.8 | 34.9 | 14.2 | 7.0 | 2.6 | 0.4 | 5.99 | 10.1% | 3.0% |
| GAME_SPREAD | 8,173 | 20.2 | 13.6 | 28.1 | 20.4 | 12.3 | 4.3 | 1.1 | 7.75 | 17.7% | 5.3% |
| TOTAL_GAMES | 14,434 | 10.2 | 10.3 | 36.3 | 25.2 | 11.5 | 4.2 | 2.4 | 9.16 | 18.1% | 6.6% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 40,507 | 44.3% | 24.8% | 13.01 | 35.4% | 15.2% | 10.71 |
| gen1_elo | 40,507 | 44.1% | 24.6% | 12.93 | 35.2% | 15.2% | 10.53 |
| gen1_sr | 40,507 | 52.0% | 31.3% | 15.85 | 44.0% | 21.7% | 12.99 |
| gen2 | 40,507 | 50.9% | 31.6% | 15.44 | 43.9% | 23.3% | 12.85 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 18,716 | 15.6 | 10.5 | 21.4 | 17.2 | 20.1 | 12.0 | 3.3 | 10.7 | 35.3% | 15.3% |
| STALE | 21,791 | 10.6 | 7.1 | 16.5 | 13.8 | 19.0 | 17.3 | 15.7 | 15.8 | 52.0% | 33.0% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 23,480 | 16.3 | 11.1 | 22.8 | 15.4 | 17.8 | 11.8 | 4.7 | 9.92 | 34.3% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 70,519 | 23480 | 22188 | 24851 | 24.4 | 125.9 | 1451.1 |
| ge_15pp | 28,797 | 8057 | 7899 | 12841 | 26.9 | 437.7 | 1451.1 |
| ge_25pp | 15,382 | 3868 | 3447 | 8067 | 32.2 | 588.0 | 1431.1 |
| lt_10pp | 30,919 | 11804 | 10525 | 8590 | 22.4 | 46.9 | 1421.1 |

Current slate `SL-20261030T231557Z-a3156820`: 405 priced rows, quote age at build {'median': 11.3, 'max': 11.4}, freshness {'AGING': 405}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 45 | 0.0 | 0.0 | 31.1 | 6.7 | 35.6 | 22.2 | 4.4 | 20.19 | 62.2% | 26.7% |
| EXTERNAL_LONE_OUTLIER | 25 | 64.0 | 36.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.43 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,012 | 19.8 | 11.0 | 25.4 | 17.9 | 17.8 | 7.1 | 0.9 | 8.54 | 25.9% | 8.1% |
| KALSHI_LONE_OUTLIER | 27 | 3.7 | 3.7 | 77.8 | 7.4 | 3.7 | 3.7 | 0.0 | 6.42 | 7.4% | 3.7% |
| MARKETS_AGREE | 800 | 65.4 | 34.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.21 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,748 | 0.0 | 2.4 | 36.7 | 25.4 | 24.8 | 9.8 | 0.9 | 11.98 | 35.5% | 10.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 40,507 | 6657 (16.4%) | 26.3% | 1.1% | {"EXTERNAL_STALE": 4012, "AGREES_WITH_KALSHI": 1748, "ALL_AGREE": 800, "SUPPORTS_MODEL_DIRECTION": 44, "AGREES_WITH_MODEL": 27, "EXTERNAL_OUTLIER": 25, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 17,941 | 1687 (9.4%) | 36.8% | 1.8% | {"EXTERNAL_STALE": 1037, "AGREES_WITH_KALSHI": 620, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 10,052 | 523 (5.2%) | 35.8% | 2.5% | {"EXTERNAL_STALE": 323, "AGREES_WITH_KALSHI": 187, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,759 | 496 (10.4%) | 36.3% | 2.6% | {"EXTERNAL_STALE": 303, "AGREES_WITH_KALSHI": 180, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 16,346 | 3805 (23.3%) | 18.0% | 0.9% | {"EXTERNAL_STALE": 2259, "ALL_AGREE": 800, "AGREES_WITH_KALSHI": 684, "EXTERNAL_OUTLIER": 25, "AGREES_WITH_MODEL": 23, "SUPPORTS_MODEL_DIRECTION": 13, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 7,899 | 10.5 | 7.6 | 19.5 | 14.4 | 21.5 | 16.5 | 10.0 | 14.09 | 48.0% | 26.5% |
| 4-10x | 5,468 | 11.0 | 8.5 | 18.8 | 15.5 | 21.9 | 14.3 | 10.0 | 13.64 | 46.2% | 24.3% |
| <2x | 20,571 | 15.2 | 9.9 | 19.6 | 15.9 | 17.3 | 13.0 | 9.0 | 11.55 | 39.4% | 22.0% |
| >=10x | 6,569 | 10.4 | 6.4 | 15.0 | 14.5 | 21.7 | 19.1 | 12.8 | 16.36 | 53.7% | 32.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 10,523 | 12.8 | 8.9 | 19.6 | 15.9 | 19.0 | 13.4 | 10.4 | 12.66 | 42.8% | 23.8% |
| 300-1000 | 8,749 | 11.9 | 8.7 | 17.8 | 15.3 | 20.2 | 16.4 | 9.6 | 13.59 | 46.2% | 26.0% |
| <300 | 12,962 | 8.2 | 5.8 | 15.2 | 14.8 | 23.0 | 19.9 | 13.0 | 17.07 | 56.0% | 33.0% |
| >=3000 | 8,273 | 21.5 | 13.0 | 24.2 | 15.6 | 13.7 | 7.1 | 5.0 | 7.57 | 25.8% | 12.1% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1169 | 0.5494 | 0.4105 | 0.4953 | +0.054 | -0.085 | -0.0019 ± 0.0045 |
| ratio 4-10x | 810 | 0.5812 | 0.435 | 0.4938 | +0.087 | -0.059 | 0.0081 ± 0.0056 |
| ratio <2x | 2825 | 0.5376 | 0.4149 | 0.4453 | +0.092 | -0.030 | 0.0127 ± 0.0027 |
| ratio >=10x | 1001 | 0.5678 | 0.3929 | 0.4496 | +0.118 | -0.057 | 0.0147 ± 0.0058 |
| thinner_sample 1000-3000 | 1591 | 0.5393 | 0.4126 | 0.4494 | +0.090 | -0.037 | 0.0101 ± 0.0036 |
| thinner_sample 300-1000 | 1323 | 0.5678 | 0.426 | 0.486 | +0.082 | -0.060 | 0.0025 ± 0.0044 |
| thinner_sample <300 | 1926 | 0.5594 | 0.3917 | 0.4585 | +0.101 | -0.067 | 0.0118 ± 0.0041 |
| thinner_sample >=3000 | 965 | 0.532 | 0.4387 | 0.4622 | +0.070 | -0.024 | 0.0131 ± 0.0037 |
| data_status ADEQUATE | 1579 | 0.534 | 0.4316 | 0.449 | +0.085 | -0.017 | 0.0133 ± 0.0031 |
| data_status LIMITED | 1424 | 0.5492 | 0.4163 | 0.4712 | +0.078 | -0.055 | 0.0068 ± 0.004 |
| data_status POOR | 2802 | 0.562 | 0.4009 | 0.4665 | +0.096 | -0.066 | 0.0086 ± 0.0033 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 850 | 0.1988 | 0.1991 | -0.0003 ± 0.0005 | 0.5772 | 0.5782 | 0.5049 | 0.4897 | 0.5082 | -0.089 ± 0.0163 | -0.01 (5) |
| 3-5 | 532 | 0.2047 | 0.205 | -0.0003 ± 0.0016 | 0.5917 | 0.5912 | 0.5043 | 0.4644 | 0.4868 | -0.097 ± 0.02 | 0.02 (1) |
| 5-10 | 1223 | 0.2016 | 0.2016 | +0.0000 ± 0.0019 | 0.5895 | 0.5868 | 0.5104 | 0.4367 | 0.471 | -0.088 ± 0.0133 | -0.0167 (6) |
| 10-15 | 1012 | 0.2199 | 0.2114 | +0.0085 ± 0.0036 | 0.6322 | 0.6079 | 0.5275 | 0.4038 | 0.4298 | -0.108 ± 0.0146 | -0.048 (5) |
| 15-25 | 1284 | 0.2255 | 0.2116 | +0.0139 ± 0.005 | 0.6468 | 0.6072 | 0.5761 | 0.3808 | 0.4431 | -0.102 ± 0.0129 | -0.0033 (9) |
| 25-40 | 747 | 0.2232 | 0.2055 | +0.0178 ± 0.0099 | 0.6365 | 0.5927 | 0.6547 | 0.3446 | 0.4712 | -0.077 ± 0.0152 | -0.01 (1) |
| 40+ | 157 | 0.2855 | 0.1866 | +0.0989 ± 0.0302 | 0.7765 | 0.5515 | 0.7369 | 0.2888 | 0.4076 | -0.078 ± 0.0298 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4638 | 0.1843 | 0.1852 | -0.0009 ± 0.0002 | 0.5433 | 0.5444 | 0.4875 | 0.4723 | 0.5024 | -0.023 ± 0.0064 | -0.0129 (17) |
| 3-5 | 3131 | 0.1947 | 0.1928 | +0.0018 ± 0.0006 | 0.5682 | 0.5615 | 0.4831 | 0.4433 | 0.4392 | -0.059 ± 0.0079 | 0.0 (2) |
| 5-10 | 6649 | 0.202 | 0.1983 | +0.0037 ± 0.0008 | 0.5899 | 0.5778 | 0.4855 | 0.412 | 0.4249 | -0.047 ± 0.0055 | -0.0119 (21) |
| 10-15 | 5502 | 0.2015 | 0.1857 | +0.0158 ± 0.0014 | 0.5889 | 0.5457 | 0.4842 | 0.3603 | 0.3579 | -0.066 ± 0.0058 | -0.0281 (16) |
| 15-25 | 6922 | 0.2065 | 0.1677 | +0.0388 ± 0.0019 | 0.6057 | 0.4976 | 0.499 | 0.3032 | 0.3029 | -0.070 ± 0.0049 | -0.0025 (44) |
| 25-40 | 5406 | 0.2216 | 0.1248 | +0.0968 ± 0.003 | 0.6374 | 0.3843 | 0.5256 | 0.2115 | 0.2185 | -0.060 ± 0.0047 | -0.01 (1) |
| 40+ | 3590 | 0.3841 | 0.0444 | +0.3396 ± 0.004 | 1.0005 | 0.1724 | 0.6327 | 0.1039 | 0.0593 | -0.078 ± 0.0033 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 670 | 0.2059 | 0.2066 | -0.0007 ± 0.0006 | 0.5934 | 0.5953 | 0.5078 | 0.4929 | 0.5239 | -0.099 ± 0.019 | -0.01 (3) |
| 3-5 | 478 | 0.2186 | 0.2163 | +0.0023 ± 0.0017 | 0.6213 | 0.6166 | 0.5143 | 0.4746 | 0.4603 | -0.124 ± 0.0226 | 0.02 (1) |
| 5-10 | 1069 | 0.2074 | 0.2061 | +0.0013 ± 0.0021 | 0.6013 | 0.597 | 0.5408 | 0.466 | 0.4967 | -0.091 ± 0.0143 | -0.01 (4) |
| 10-15 | 938 | 0.2157 | 0.2097 | +0.0059 ± 0.0037 | 0.6221 | 0.6065 | 0.5639 | 0.4396 | 0.4808 | -0.105 ± 0.0156 | -0.04 (5) |
| 15-25 | 1348 | 0.23 | 0.2136 | +0.0165 ± 0.0049 | 0.6547 | 0.6114 | 0.583 | 0.3877 | 0.4451 | -0.097 ± 0.0128 | -0.0133 (9) |
| 25-40 | 949 | 0.2683 | 0.1974 | +0.0709 ± 0.009 | 0.7491 | 0.5752 | 0.6592 | 0.3451 | 0.392 | -0.132 ± 0.0144 | -0.0075 (4) |
| 40+ | 353 | 0.3649 | 0.1652 | +0.1996 ± 0.0215 | 0.9986 | 0.4977 | 0.732 | 0.2469 | 0.2975 | -0.084 ± 0.0209 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3983 | 0.1903 | 0.1906 | -0.0003 ± 0.0002 | 0.556 | 0.5564 | 0.5084 | 0.4934 | 0.5104 | -0.039 ± 0.0071 | -0.0133 (15) |
| 3-5 | 2714 | 0.195 | 0.1939 | +0.0011 ± 0.0007 | 0.5665 | 0.5631 | 0.5117 | 0.472 | 0.4764 | -0.047 ± 0.0086 | 0.02 (1) |
| 5-10 | 5942 | 0.1985 | 0.195 | +0.0034 ± 0.0009 | 0.5823 | 0.5697 | 0.5096 | 0.4355 | 0.4524 | -0.042 ± 0.0058 | -0.0117 (6) |
| 10-15 | 4955 | 0.2036 | 0.1916 | +0.0120 ± 0.0016 | 0.5962 | 0.5602 | 0.511 | 0.3872 | 0.4016 | -0.052 ± 0.0063 | -0.0189 (18) |
| 15-25 | 6907 | 0.2171 | 0.1806 | +0.0365 ± 0.002 | 0.6314 | 0.5302 | 0.5223 | 0.3271 | 0.3346 | -0.063 ± 0.0051 | -0.0086 (42) |
| 25-40 | 6344 | 0.2513 | 0.1357 | +0.1156 ± 0.0029 | 0.709 | 0.4161 | 0.5578 | 0.241 | 0.2205 | -0.085 ± 0.0046 | -0.0044 (18) |
| 40+ | 4993 | 0.3989 | 0.0587 | +0.3402 ± 0.004 | 1.0527 | 0.2115 | 0.6529 | 0.1177 | 0.0813 | -0.073 ± 0.0034 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 805 | 0.1952 | 0.1974 | -0.0022 ± 0.0006 | 0.5691 | 0.5748 | 0.5009 | 0.4855 | 0.5478 | -0.036 ± 0.0164 | -0.0137 (8) |
| 3-5 | 572 | 0.2047 | 0.2026 | +0.0020 ± 0.0015 | 0.5921 | 0.5856 | 0.4954 | 0.4558 | 0.451 | -0.123 ± 0.0195 | 0.0067 (3) |
| 5-10 | 1269 | 0.2032 | 0.2012 | +0.0020 ± 0.0019 | 0.5921 | 0.5852 | 0.5117 | 0.438 | 0.4594 | -0.098 ± 0.013 | -0.0071 (7) |
| 10-15 | 1016 | 0.2087 | 0.2038 | +0.0049 ± 0.0035 | 0.6073 | 0.5911 | 0.5397 | 0.4164 | 0.4596 | -0.096 ± 0.0142 | -0.0317 (6) |
| 15-25 | 1215 | 0.2343 | 0.2165 | +0.0178 ± 0.0052 | 0.6678 | 0.6179 | 0.5875 | 0.3933 | 0.4444 | -0.113 ± 0.0134 | -0.03 (1) |
| 25-40 | 762 | 0.213 | 0.2122 | +0.0008 ± 0.0098 | 0.6145 | 0.6085 | 0.6624 | 0.352 | 0.5039 | -0.059 ± 0.015 | 0.015 (2) |
| 40+ | 166 | 0.3035 | 0.1944 | +0.1091 ± 0.0302 | 0.8261 | 0.5695 | 0.7484 | 0.2986 | 0.4096 | -0.084 ± 0.0315 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4438 | 0.1836 | 0.1843 | -0.0007 ± 0.0002 | 0.5406 | 0.5419 | 0.4829 | 0.4676 | 0.4887 | -0.030 ± 0.0065 | -0.0163 (35) |
| 3-5 | 3098 | 0.2019 | 0.1996 | +0.0022 ± 0.0006 | 0.5869 | 0.5797 | 0.4811 | 0.4416 | 0.4338 | -0.064 ± 0.0082 | -0.0094 (18) |
| 5-10 | 6815 | 0.194 | 0.19 | +0.0040 ± 0.0008 | 0.571 | 0.5575 | 0.4871 | 0.4131 | 0.4238 | -0.048 ± 0.0053 | -0.01 (31) |
| 10-15 | 5493 | 0.1924 | 0.1791 | +0.0133 ± 0.0014 | 0.5689 | 0.5301 | 0.495 | 0.3716 | 0.3788 | -0.056 ± 0.0057 | -0.015 (12) |
| 15-25 | 7040 | 0.2132 | 0.1727 | +0.0405 ± 0.0019 | 0.621 | 0.5088 | 0.5119 | 0.3175 | 0.3119 | -0.075 ± 0.0049 | -0.03 (2) |
| 25-40 | 5395 | 0.2162 | 0.1281 | +0.0881 ± 0.0031 | 0.6255 | 0.3919 | 0.5291 | 0.2135 | 0.2339 | -0.049 ± 0.0047 | 0.01 (3) |
| 40+ | 3559 | 0.3939 | 0.0499 | +0.3439 ± 0.0042 | 1.0271 | 0.1866 | 0.6422 | 0.1106 | 0.066 | -0.079 ± 0.0036 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1211 | 0.1954 | 0.1955 | -0.0001 ± 0.0004 | 0.5692 | 0.5693 | 0.505 | 0.4899 | 0.4946 | -0.069 ± 0.013 | -0.0224 (49) |
| 3-5 | 862 | 0.1866 | 0.1858 | +0.0008 ± 0.0012 | 0.5476 | 0.5451 | 0.4975 | 0.4577 | 0.4664 | -0.067 ± 0.015 | -0.0194 (34) |
| 5-10 | 1792 | 0.2014 | 0.1968 | +0.0046 ± 0.0016 | 0.5916 | 0.577 | 0.502 | 0.4283 | 0.4342 | -0.076 ± 0.0107 | -0.005 (78) |
| 10-15 | 1226 | 0.2163 | 0.2035 | +0.0128 ± 0.0032 | 0.625 | 0.5909 | 0.5386 | 0.4158 | 0.4233 | -0.089 ± 0.0132 | 0.0014 (64) |
| 15-25 | 1566 | 0.2321 | 0.2106 | +0.0215 ± 0.0046 | 0.6613 | 0.606 | 0.5837 | 0.3889 | 0.4342 | -0.085 ± 0.0117 | -0.0214 (59) |
| 25-40 | 985 | 0.2435 | 0.2105 | +0.0329 ± 0.009 | 0.696 | 0.6036 | 0.6843 | 0.3722 | 0.4761 | -0.094 ± 0.0137 | -0.0219 (26) |
| 40+ | 330 | 0.3355 | 0.2029 | +0.1325 ± 0.0239 | 0.9729 | 0.5911 | 0.8162 | 0.3398 | 0.4545 | -0.101 ± 0.0224 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4568 | 0.1756 | 0.1759 | -0.0003 ± 0.0002 | 0.5207 | 0.5208 | 0.51 | 0.4948 | 0.5077 | -0.037 ± 0.0063 | -0.0157 (88) |
| 3-5 | 3145 | 0.193 | 0.1917 | +0.0013 ± 0.0006 | 0.5626 | 0.56 | 0.5044 | 0.4647 | 0.4684 | -0.047 ± 0.0079 | -0.0209 (69) |
| 5-10 | 6461 | 0.1985 | 0.192 | +0.0065 ± 0.0008 | 0.5835 | 0.5645 | 0.4985 | 0.4249 | 0.419 | -0.063 ± 0.0055 | -0.0082 (132) |
| 10-15 | 4478 | 0.2107 | 0.1946 | +0.0161 ± 0.0016 | 0.6121 | 0.5701 | 0.5371 | 0.4142 | 0.4087 | -0.071 ± 0.0067 | -0.0053 (105) |
| 15-25 | 5379 | 0.2307 | 0.2008 | +0.0299 ± 0.0024 | 0.6633 | 0.581 | 0.571 | 0.3756 | 0.3982 | -0.065 ± 0.0062 | -0.0253 (107) |
| 25-40 | 3637 | 0.2598 | 0.1878 | +0.0719 ± 0.0045 | 0.735 | 0.5478 | 0.6364 | 0.3239 | 0.3679 | -0.076 ± 0.007 | -0.0229 (51) |
| 40+ | 1557 | 0.3748 | 0.1566 | +0.2182 ± 0.0104 | 1.062 | 0.4666 | 0.7419 | 0.2401 | 0.2839 | -0.069 ± 0.0096 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5805 | 1.021 ± 0.037 | 1.096 | 0.169 | 0.1664 | 0.215 | 0.2056 |
| gen2 | 5805 | 0.808 ± 0.033 | 1.064 | 0.1714 | 0.1668 | 0.2343 | 0.2054 |
| gen1_elo | 5805 | 0.997 ± 0.035 | 1.093 | 0.1755 | 0.1665 | 0.2139 | 0.2057 |
| gen1_sr | 5805 | 0.994 ± 0.044 | 1.122 | 0.1316 | 0.1687 | 0.2302 | 0.2051 |
| gen1_ledger | 7972 | 0.859 ± 0.026 | 1.063 | 0.1877 | 0.1757 | 0.218 | 0.2011 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 28,797)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,509 | 22.6% |
| STALE_QUOTE | market_freshness | 6,344 | 22.0% |
| BOOK_QUALITY | execution | 5,411 | 18.8% |
| POOR_DATA | data | 3,353 | 11.6% |
| LIMITED_DATA | data | 1,788 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,645 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,234 | 4.3% |
| IDENTITY_AMBIGUOUS | mapping | 1,188 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 831 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 493 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.6%, market_freshness 22.0%, execution 18.8%, data 17.8%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.3%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.4%, START_UNVERIFIABLE 94.5%, LOW_DATA_QUALITY 71.7%, THIN_PLAYER_HISTORY 60.2%, STALE_PLAYER_DATA 52.2%, STALE_KALSHI_QUOTE 44.6%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 33.4%, WIDE_SPREAD 24.9%, MODEL_HIGH_UNCERTAINTY 18.2%, PLAYER_IDENTITY_RISK 15.6%, LEVEL_TRANSFER_RISK 10.5%, LOW_DISPLAYED_LIQUIDITY 8.1%, EVENT_MAPPING_RISK 7.5%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.4%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.1%, POST_SETTLEMENT_OBSERVATION 22.6%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 15,382)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,262 | 34.2% |
| STALE_QUOTE | market_freshness | 2,880 | 18.7% |
| BOOK_QUALITY | execution | 2,813 | 18.3% |
| POOR_DATA | data | 1,437 | 9.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 862 | 5.6% |
| IDENTITY_AMBIGUOUS | mapping | 637 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 537 | 3.5% |
| LIMITED_DATA | data | 523 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 307 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 123 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.2%, market_freshness 18.7%, execution 18.3%, data 12.7%, market_freshness/coverage 9.1%, mapping 4.1%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 75.0%, THIN_PLAYER_HISTORY 62.4%, STALE_KALSHI_QUOTE 52.4%, STALE_PLAYER_DATA 46.2%, MODEL_INTERNAL_DISAGREEMENT 42.5%, ASYMMETRIC_SAMPLE_SIZE 34.4%, WIDE_SPREAD 24.3%, MODEL_HIGH_UNCERTAINTY 19.0%, PLAYER_IDENTITY_RISK 18.3%, LEVEL_TRANSFER_RISK 9.3%, EVENT_MAPPING_RISK 9.0%, LOW_DISPLAYED_LIQUIDITY 8.0%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.2%, POST_SETTLEMENT_OBSERVATION 34.2%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 12238, "IDENTITY_AMBIGUOUS": 3144}; ticker orientation: {"VERIFIED": 15382}.

Checks: discipline:AMBIGUOUS 1013, discipline:PASS 14369, identity_confidence:AMBIGUOUS 2821, identity_confidence:PASS 12561, level_mapping:NA 1025, level_mapping:PASS 14357, market_pair:AMBIGUOUS 482, market_pair:NA 352, market_pair:PASS 14548, model_complement:NA 315, model_complement:PASS 15067, namesake:AMBIGUOUS 6, namesake:PASS 15376, physical_match_id:NA 5330, physical_match_id:PASS 10052, player_ids:PASS 15382, same_pair_other_event:PASS 15382, ticker_orientation:PASS 15382

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,514 | 4.1% | 3.7% | 1.5% | {"market_freshness": 56, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 17, "coverage": 13} | 5.83 | 0.22 / 0.2151 (651) | 21.9% | 2.9% | 3.2% | 2.8% |
| CHALLENGER | 10,062 | 16.6% | 6.2% | 10.8% | {"coverage": 986, "market_freshness/coverage": 198, "market_freshness": 172, "data": 145, "model_calibration_or_unknown": 74, "execution": 37, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.24 | 0.2206 / 0.2113 (2299) | 35.7% | 15.5% | 4.1% | 22.7% |
| DOUBLES | 2,167 | 46.8% | 46.6% | 6.6% | {"execution": 568, "mapping": 272, "market_freshness": 106, "market_freshness/coverage": 60, "coverage": 7} | 23.54 | 0.306 / 0.2396 (526) | 10.8% | 0.0% | 100.0% | 6.3% |
| ITF_MEN | 20,014 | 25.0% | 17.6% | 32.6% | {"coverage": 1775, "market_freshness": 917, "execution": 915, "data": 733, "market_freshness/coverage": 479, "mapping": 184, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.71 | 0.2165 / 0.1995 (4126) | 38.1% | 69.3% | 16.4% | 21.7% |
| ITF_WOMEN | 26,258 | 26.5% | 19.1% | 45.3% | {"coverage": 2438, "market_freshness": 1476, "execution": 1215, "data": 988, "market_freshness/coverage": 592, "mapping": 158, "model_calibration_or_unknown": 82, "model_calibration": 21} | 12.54 | 0.2036 / 0.1947 (4836) | 39.8% | 57.1% | 9.9% | 21.6% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,067 | 5.7% | 4.8% | 1.5% | {"market_freshness": 80, "model_calibration_or_unknown": 43, "coverage": 30, "execution": 28, "data": 20, "model_calibration": 18, "market_freshness/coverage": 11, "mapping": 1} | 7.44 | 0.2368 / 0.2307 (621) | 26.9% | 1.4% | 1.4% | 3.3% |
| WTA125 | 2,282 | 11.1% | 9.4% | 1.6% | {"market_freshness": 71, "model_calibration_or_unknown": 51, "market_freshness/coverage": 41, "data": 38, "execution": 21, "model_calibration": 15, "coverage": 12, "mapping": 4} | 9.17 | 0.2123 / 0.1929 (676) | 26.5% | 10.7% | 4.7% | 7.3% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 725 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 117 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 9 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 10 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); no external reference |
| 13 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 14 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 151 min (STALE); no external reference |
| 17 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 18 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 19 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 20 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 21 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 22 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 23 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 24 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 25 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 26 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 27 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 28 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 29 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 30 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 31 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 32 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 33 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 34 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 35 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 36 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 37 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 38 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 39 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 40 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 41 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 42 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 43 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 379 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 44 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 45 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 163 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |
| 46 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 47 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 48 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 49 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 12.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 768 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 50 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9702, "by_level_share_of_ge_25pp": {"ATP": 0.0148, "CHALLENGER": 0.1082, "DOUBLES": 0.0659, "ITF_MEN": 0.3258, "ITF_WOMEN": 0.4531, "OTHER": 0.0008, "WTA": 0.015, "WTA125": 0.0164}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5244, "share_primary_cause_market_settled_or_in_play": 0.433, "share_primary_cause_stale_quote_only": 0.1872}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 15382, "identity_ambiguous_share": 0.2044, "ticker_orientation": {"VERIFIED": 15382}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 10052, "with_external": 523, "coverage": 0.052, "external_status": {"EXTERNAL_STALE": 323, "AGREES_WITH_KALSHI": 187, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 323, "MODEL_LONE_OUTLIER": 187, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3576, "share_external_supports_model": 0.0249}, "pregame_clean_ge_25pp": {"n": 4759, "with_external": 496, "coverage": 0.1042, "external_status": {"EXTERNAL_STALE": 303, "AGREES_WITH_KALSHI": 180, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 303, "MODEL_LONE_OUTLIER": 180, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3629, "share_external_supports_model": 0.0262}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 476.0, "median_sample_ratio": 2.48, "median_min_matches": 19.0, "median_max_days_since_last": 238.0, "share_severe_asymmetry": 0.2097, "data_status": {"POOR": 8699, "LIMITED": 3980, "ADEQUATE": 2703}, "comparison_lt_10pp": {"median_thinner_serve_points": 1702.0, "median_sample_ratio": 1.71, "median_min_matches": 90.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1169, "model_minus_observed": 0.0541, "kalshi_minus_observed": -0.0847, "brier_diff_model_minus_kalshi": -0.0019}, "4-10x": {"n": 810, "model_minus_observed": 0.0874, "kalshi_minus_observed": -0.0588, "brier_diff_model_minus_kalshi": 0.0081}, "<2x": {"n": 2825, "model_minus_observed": 0.0923, "kalshi_minus_observed": -0.0304, "brier_diff_model_minus_kalshi": 0.0127}, ">=10x": {"n": 1001, "model_minus_observed": 0.1182, "kalshi_minus_observed": -0.0567, "brier_diff_model_minus_kalshi": 0.0147}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 5805, "model": {"intercept": -0.535, "slope": 0.808, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.195, "slope": 1.064, "slope_se": 0.037}, "mean_extremity_model": 0.1714, "mean_extremity_kalshi": 0.1668, "model_brier": 0.2343, "kalshi_brier": 0.2054, "brier_diff_model_minus_kalshi": 0.0289, "brier_diff_se": 0.0025, "model_logloss": 0.6661, "kalshi_logloss": 0.5937}, "fair_v1": {"n": 5805, "model": {"intercept": -0.424, "slope": 1.021, "slope_se": 0.037}, "kalshi_mid_same_rows": {"intercept": 0.272, "slope": 1.096, "slope_se": 0.038}, "mean_extremity_model": 0.169, "mean_extremity_kalshi": 0.1664, "model_brier": 0.215, "kalshi_brier": 0.2056, "brier_diff_model_minus_kalshi": 0.0094, "brier_diff_se": 0.002, "model_logloss": 0.6191, "kalshi_logloss": 0.594}, "gen1_elo": {"n": 5805, "model": {"intercept": -0.4, "slope": 0.997, "slope_se": 0.035}, "kalshi_mid_same_rows": {"intercept": 0.292, "slope": 1.093, "slope_se": 0.037}, "mean_extremity_model": 0.1755, "mean_extremity_kalshi": 0.1665, "model_brier": 0.2139, "kalshi_brier": 0.2057, "brier_diff_model_minus_kalshi": 0.0081, "brier_diff_se": 0.0021, "model_logloss": 0.617, "kalshi_logloss": 0.5943}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2482, "share_ge_15": 0.4429, "median_abs_gap": 13.01, "n": 40507}, "gen1_elo": {"share_ge_25": 0.2463, "share_ge_15": 0.4414, "median_abs_gap": 12.93, "n": 40507}, "gen1_sr": {"share_ge_25": 0.3132, "share_ge_15": 0.5199, "median_abs_gap": 15.85, "n": 40507}, "gen2": {"share_ge_25": 0.316, "share_ge_15": 0.5093, "median_abs_gap": 15.44, "n": 40507}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1521, "share_ge_15": 0.3542, "median_abs_gap": 10.71, "n": 31279}, "gen1_elo": {"share_ge_25": 0.152, "share_ge_15": 0.3516, "median_abs_gap": 10.53, "n": 31278}, "gen1_sr": {"share_ge_25": 0.2167, "share_ge_15": 0.4397, "median_abs_gap": 12.99, "n": 31281}, "gen2": {"share_ge_25": 0.2329, "share_ge_15": 0.4389, "median_abs_gap": 12.85, "n": 31281}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.83, "share_ge_25_all": 0.0412, "share_ge_25_pregame_clean": 0.0368}, "WTA": {"median_abs_gap_pregame_clean": 7.44, "share_ge_25_all": 0.0568, "share_ge_25_pregame_clean": 0.0483}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2366, "share_within_10pp_all": 0.4384, "share_within_10pp_pregame_clean": 0.4913, "corr_model_vs_mid_pregame_clean": 0.8506}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 850, "model_brier": 0.1988, "kalshi_brier": 0.1991, "brier_diff_model_minus_kalshi": -0.0003}, "10-15": {"n_settled": 1012, "model_brier": 0.2199, "kalshi_brier": 0.2114, "brier_diff_model_minus_kalshi": 0.0085}, "15-25": {"n_settled": 1284, "model_brier": 0.2255, "kalshi_brier": 0.2116, "brier_diff_model_minus_kalshi": 0.0139}, "25-40": {"n_settled": 747, "model_brier": 0.2232, "kalshi_brier": 0.2055, "brier_diff_model_minus_kalshi": 0.0178}, "3-5": {"n_settled": 532, "model_brier": 0.2047, "kalshi_brier": 0.205, "brier_diff_model_minus_kalshi": -0.0003}, "40+": {"n_settled": 157, "model_brier": 0.2855, "kalshi_brier": 0.1866, "brier_diff_model_minus_kalshi": 0.0989}, "5-10": {"n_settled": 1223, "model_brier": 0.2016, "kalshi_brier": 0.2016, "brier_diff_model_minus_kalshi": 0.0}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.535, "slope": 0.808, "slope_se": 0.033}, "kalshi_slope": {"intercept": 0.195, "slope": 1.064, "slope_se": 0.037}, "n": 5805}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.49, "slope": 0.859, "slope_se": 0.026}, "kalshi_slope": {"intercept": 0.166, "slope": 1.063, "slope_se": 0.031}, "n": 7972}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 526, "model_brier": 0.306, "kalshi_brier": 0.2396, "brier_diff_model_minus_kalshi": 0.0664, "brier_diff_se": 0.013, "corr_model_outcome": 0.0621, "corr_kalshi_outcome": 0.2211}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
