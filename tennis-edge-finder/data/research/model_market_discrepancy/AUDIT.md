# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-08T23:29Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 82,471): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 19.1%, 25-40 13.7%, 40+ 8.1%; median gap 11.85 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.7%, Challenger 10.9%, doubles 6.7%). Main tour: ATP 3.8% and WTA 6.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 17,955): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.5%, STALE_QUOTE 19.4%, BOOK_QUALITY 17.3%, POOR_DATA 9.1%, POSSIBLY_IN_PLAY_QUOTE 5.8%, IDENTITY_AMBIGUOUS 4.3%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.5%, market_freshness 19.4%, execution 17.3%, data 12.5%, market_freshness/coverage 9.3%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 53.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 17,955 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.1% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.8% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 494.0 points vs 1736.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.027, Gen-2 0.819, Gen-1 ledger 0.866 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 919 model 0.2232 vs Kalshi 0.2061; n 189 model 0.295 vs Kalshi 0.1767.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 349,643 model-market comparisons (572,948 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 116,430 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-08T23:08:36.690016+00:00'], shadow board 94,816 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-08T23:08:41.391595+00:00'], Model 4 42,952 rows, 29,178 settled tickers, 10,919 tickers with an external scan.
* By model: {"gen1_ledger": 78493, "gen1_elo": 47658, "fair_v1": 47658, "gen2": 47658, "gen1_sr": 47658, "model4_fundamental": 40301, "model4_conditioned": 40217}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 82,471 | 14.1 | 9.6 | 20.2 | 15.3 | 19.1 | 13.7 | 8.1 | 11.85 | 40.9% | 21.8% |
| MW fair_v1 | 47,658 | 12.8 | 8.6 | 18.7 | 15.4 | 19.6 | 14.9 | 10.0 | 13.08 | 44.5% | 24.9% |
| MW gen1_elo | 47,658 | 12.6 | 8.9 | 19.2 | 15.3 | 19.5 | 14.7 | 9.9 | 12.86 | 44.1% | 24.6% |
| MW gen1_ledger | 34,813 | 15.8 | 10.9 | 22.2 | 15.1 | 18.5 | 12.0 | 5.5 | 10.26 | 36.0% | 17.5% |
| MW gen1_sr | 47,658 | 10.1 | 7.3 | 16.7 | 13.9 | 20.7 | 18.7 | 12.7 | 15.85 | 52.1% | 31.3% |
| MW gen2 | 47,658 | 11.0 | 7.5 | 16.6 | 13.7 | 19.6 | 17.7 | 13.7 | 15.48 | 51.1% | 31.4% |
| all families model4_conditioned | 40,217 | 22.2 | 17.9 | 34.2 | 17.1 | 5.0 | 2.2 | 1.2 | 6.07 | 8.5% | 3.4% |
| all families model4_fundamental | 40,301 | 17.3 | 13.5 | 33.9 | 20.0 | 10.0 | 3.8 | 1.5 | 7.62 | 15.3% | 5.4% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.2%, >=15pp 40.9%, >=20pp 30.1%, >=25pp 21.8%, >=30pp 15.7%, >=40pp 8.1%, >=50pp 3.9%
Executable gap (model outside the book, before fees): median 8.41pp; >=10pp 45.1%, >=25pp 17.2%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,003 | 28.4 | 15.7 | 27.5 | 13.4 | 10.7 | 3.6 | 0.6 | 5.82 | 15.0% | 4.3% |
| CHALLENGER | 7,207 | 15.9 | 9.6 | 20.5 | 15.4 | 16.0 | 11.5 | 11.0 | 11.01 | 38.6% | 22.5% |
| ITF_MEN | 13,466 | 9.8 | 7.3 | 17.0 | 15.1 | 21.2 | 17.2 | 12.4 | 15.29 | 50.7% | 29.6% |
| ITF_WOMEN | 18,590 | 9.5 | 7.1 | 16.0 | 14.8 | 22.2 | 18.4 | 12.0 | 15.93 | 52.7% | 30.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,059 | 16.7 | 13.2 | 24.8 | 20.9 | 16.6 | 6.8 | 1.1 | 8.65 | 24.5% | 7.9% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,003 | 26.8 | 15.7 | 26.0 | 15.5 | 11.4 | 3.9 | 0.8 | 6.07 | 16.1% | 4.7% |
| CHALLENGER | 7,207 | 14.5 | 9.0 | 18.8 | 13.8 | 18.8 | 13.6 | 11.6 | 12.65 | 43.9% | 25.2% |
| ITF_MEN | 13,466 | 8.2 | 6.1 | 15.1 | 13.7 | 20.0 | 20.4 | 16.5 | 17.94 | 56.9% | 36.9% |
| ITF_WOMEN | 18,590 | 7.9 | 5.8 | 14.1 | 12.8 | 20.7 | 21.2 | 17.5 | 19.08 | 59.4% | 38.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,059 | 14.1 | 10.1 | 21.6 | 16.3 | 22.5 | 12.8 | 2.5 | 11.28 | 37.9% | 15.4% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,003 | 23.1 | 14.1 | 25.2 | 15.6 | 14.7 | 6.1 | 1.1 | 7.1 | 22.0% | 7.2% |
| CHALLENGER | 7,207 | 15.0 | 9.6 | 20.5 | 15.6 | 16.1 | 12.1 | 11.1 | 11.41 | 39.3% | 23.1% |
| ITF_MEN | 13,466 | 9.5 | 7.3 | 17.2 | 14.2 | 21.8 | 17.2 | 12.7 | 15.66 | 51.7% | 29.9% |
| ITF_WOMEN | 18,590 | 9.3 | 6.9 | 16.2 | 15.7 | 22.2 | 18.4 | 11.4 | 15.62 | 51.9% | 29.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,059 | 22.7 | 17.0 | 31.9 | 15.4 | 8.7 | 3.3 | 1.1 | 6.12 | 13.0% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,401 | 27.4 | 19.7 | 29.4 | 12.4 | 8.1 | 2.6 | 0.5 | 5.3 | 11.2% | 3.0% |
| CHALLENGER | 4,641 | 22.4 | 14.5 | 27.5 | 14.8 | 13.4 | 5.7 | 1.6 | 7.08 | 20.7% | 7.3% |
| DOUBLES | 2,585 | 4.8 | 4.6 | 12.9 | 11.0 | 20.4 | 24.4 | 22.0 | 23.23 | 66.7% | 46.4% |
| ITF_MEN | 9,965 | 12.9 | 9.6 | 21.5 | 15.6 | 21.6 | 12.9 | 5.9 | 11.77 | 40.4% | 18.8% |
| ITF_WOMEN | 12,017 | 13.4 | 9.2 | 19.9 | 15.6 | 21.5 | 14.9 | 5.5 | 12.25 | 41.8% | 20.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,799 | 23.7 | 16.1 | 31.5 | 17.0 | 8.9 | 2.6 | 0.2 | 6.56 | 11.7% | 2.8% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,878 | 28.9 | 15.9 | 27.9 | 13.4 | 10.4 | 3.2 | 0.3 | 5.65 | 13.9% | 3.5% |
| CHALLENGER | 5,067 | 20.7 | 11.9 | 25.6 | 18.2 | 16.0 | 6.0 | 1.6 | 8.3 | 23.6% | 7.6% |
| ITF_MEN | 9,811 | 12.0 | 8.7 | 20.7 | 17.3 | 22.0 | 14.0 | 5.3 | 12.38 | 41.3% | 19.3% |
| ITF_WOMEN | 13,634 | 11.4 | 8.6 | 18.9 | 17.1 | 24.1 | 15.1 | 4.8 | 13.2 | 44.1% | 20.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,945 | 17.1 | 13.2 | 25.1 | 21.2 | 16.6 | 6.2 | 0.6 | 8.49 | 23.5% | 6.9% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,878 | 27.1 | 16.0 | 26.3 | 15.4 | 11.3 | 3.4 | 0.4 | 5.96 | 15.1% | 3.8% |
| CHALLENGER | 5,067 | 18.4 | 11.4 | 23.6 | 16.2 | 19.2 | 9.3 | 1.8 | 9.01 | 30.3% | 11.2% |
| ITF_MEN | 9,812 | 9.6 | 7.2 | 17.6 | 16.0 | 21.9 | 18.6 | 9.1 | 14.89 | 49.6% | 27.7% |
| ITF_WOMEN | 13,635 | 8.9 | 6.9 | 16.1 | 14.4 | 22.6 | 20.5 | 10.6 | 16.49 | 53.8% | 31.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,945 | 14.3 | 10.2 | 21.8 | 16.5 | 22.7 | 12.5 | 1.9 | 11.09 | 37.1% | 14.4% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,337 | 27.6 | 19.9 | 29.4 | 12.5 | 7.8 | 2.4 | 0.3 | 5.24 | 10.6% | 2.7% |
| CHALLENGER | 4,103 | 23.7 | 15.4 | 28.7 | 15.0 | 12.8 | 4.0 | 0.4 | 6.61 | 17.3% | 4.5% |
| DOUBLES | 2,420 | 4.7 | 4.6 | 13.1 | 11.1 | 20.2 | 24.3 | 22.0 | 23.21 | 66.5% | 46.4% |
| ITF_MEN | 8,566 | 13.7 | 10.2 | 23.1 | 16.1 | 21.6 | 11.4 | 3.9 | 10.82 | 36.9% | 15.3% |
| ITF_WOMEN | 10,304 | 14.0 | 9.8 | 21.0 | 16.1 | 21.6 | 13.8 | 3.6 | 11.43 | 39.1% | 17.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,736 | 24.0 | 16.5 | 31.4 | 17.0 | 8.9 | 2.0 | 0.1 | 6.43 | 11.0% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,585 | 4.8 | 4.6 | 12.9 | 11.0 | 20.4 | 24.4 | 22.0 | 23.23 | 66.7% | 46.4% |
| singles | 32,228 | 16.6 | 11.4 | 23.0 | 15.5 | 18.3 | 11.0 | 4.2 | 9.72 | 33.5% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 9,845 | 12.6 | 9.0 | 19.9 | 15.5 | 19.6 | 14.0 | 9.4 | 12.66 | 43.0% | 23.4% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 31,032 | 13.4 | 8.7 | 18.7 | 15.2 | 19.2 | 14.8 | 10.0 | 12.92 | 44.0% | 24.8% |
| UNKNOWN | 6,368 | 10.5 | 7.5 | 17.1 | 16.3 | 21.5 | 15.9 | 11.1 | 14.32 | 48.5% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 13,564 | 19.5 | 11.8 | 22.3 | 15.9 | 14.9 | 9.2 | 6.3 | 8.92 | 30.4% | 15.5% |
| B | 5,831 | 12.6 | 8.6 | 19.6 | 15.6 | 19.7 | 12.9 | 11.0 | 12.83 | 43.7% | 23.9% |
| C | 6,759 | 11.9 | 8.8 | 19.4 | 15.6 | 18.7 | 14.7 | 10.8 | 13.01 | 44.2% | 25.5% |
| D | 7,705 | 11.7 | 8.3 | 17.8 | 15.2 | 21.8 | 15.8 | 9.4 | 13.93 | 47.0% | 25.2% |
| F | 13,799 | 7.4 | 5.6 | 14.8 | 14.7 | 23.5 | 20.9 | 13.2 | 17.82 | 57.5% | 34.0% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,388 | 24.6 | 16.1 | 29.1 | 15.0 | 10.6 | 3.4 | 1.3 | 6.36 | 15.3% | 4.7% |
| B | 4,865 | 16.6 | 10.8 | 24.2 | 16.8 | 18.9 | 9.6 | 3.0 | 9.62 | 31.4% | 12.6% |
| C | 6,841 | 11.0 | 7.8 | 19.6 | 14.6 | 21.0 | 15.7 | 10.4 | 13.67 | 47.1% | 26.1% |
| D | 5,200 | 14.5 | 10.1 | 21.4 | 15.3 | 20.9 | 12.5 | 5.3 | 11.24 | 38.7% | 17.8% |
| F | 8,519 | 10.2 | 8.4 | 16.2 | 14.6 | 23.4 | 19.5 | 7.9 | 15.37 | 50.7% | 27.4% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 15,317 | 17.7 | 10.8 | 21.4 | 15.7 | 15.2 | 10.1 | 9.0 | 10.0 | 34.3% | 19.1% |
| LIMITED | 10,447 | 13.6 | 9.7 | 20.4 | 15.7 | 19.5 | 13.4 | 7.7 | 11.92 | 40.6% | 21.1% |
| POOR | 21,894 | 9.0 | 6.6 | 16.0 | 14.9 | 22.8 | 18.9 | 11.8 | 16.2 | 53.5% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,981 | 23.6 | 17.9 | 33.0 | 15.6 | 6.5 | 3.0 | 0.4 | 5.92 | 9.8% | 3.4% |
| GAME_SPREAD | 6,733 | 22.9 | 15.3 | 32.0 | 16.8 | 9.0 | 3.3 | 0.7 | 6.68 | 13.0% | 4.0% |
| MATCH_WINNER | 34,813 | 15.8 | 10.9 | 22.2 | 15.1 | 18.5 | 12.0 | 5.5 | 10.26 | 36.0% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 16,614 | 28.1 | 16.8 | 30.8 | 12.6 | 9.0 | 2.4 | 0.3 | 5.61 | 11.7% | 2.7% |
| TOTAL_GAMES | 11,328 | 9.8 | 10.8 | 35.8 | 25.9 | 10.6 | 4.2 | 2.9 | 9.18 | 17.7% | 7.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,277 | 24.5 | 28.6 | 33.3 | 8.2 | 4.0 | 1.2 | 0.3 | 4.8 | 5.5% | 1.4% |
| GAME_SPREAD | 9,268 | 47.0 | 16.0 | 24.8 | 7.5 | 2.3 | 1.9 | 0.6 | 3.29 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,672 | 6.6 | 9.9 | 40.3 | 30.2 | 7.4 | 3.3 | 2.4 | 9.2 | 13.1% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,313 | 23.8 | 16.6 | 34.6 | 14.8 | 6.9 | 2.7 | 0.5 | 6.06 | 10.2% | 3.2% |
| GAME_SPREAD | 9,277 | 20.6 | 13.5 | 28.2 | 20.1 | 12.0 | 4.4 | 1.2 | 7.63 | 17.5% | 5.5% |
| TOTAL_GAMES | 16,711 | 10.0 | 10.8 | 36.3 | 24.3 | 11.4 | 4.5 | 2.6 | 9.05 | 18.5% | 7.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 47,658 | 44.5% | 24.9% | 13.08 | 35.3% | 15.0% | 10.7 |
| gen1_elo | 47,658 | 44.1% | 24.6% | 12.86 | 34.8% | 14.8% | 10.49 |
| gen1_sr | 47,658 | 52.1% | 31.3% | 15.85 | 43.9% | 21.5% | 12.97 |
| gen2 | 47,658 | 51.1% | 31.4% | 15.48 | 43.9% | 23.1% | 12.85 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,034 | 15.5 | 10.5 | 21.3 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 27,624 | 10.8 | 7.3 | 16.8 | 14.0 | 19.3 | 17.0 | 14.8 | 15.47 | 51.2% | 31.9% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 28,281 | 16.4 | 11.2 | 22.8 | 15.2 | 18.0 | 11.5 | 4.9 | 9.88 | 34.4% | 16.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 82,471 | 28281 | 23506 | 30684 | 24.8 | 131.1 | 1451.1 |
| ge_15pp | 33,738 | 9722 | 8373 | 15643 | 28.3 | 439.8 | 1451.1 |
| ge_25pp | 17,955 | 4632 | 3655 | 9668 | 33.8 | 586.2 | 1431.1 |
| lt_10pp | 36,145 | 14258 | 11116 | 10771 | 22.6 | 47.9 | 1421.1 |

Current slate `SL-20261108T232900Z-f93b8df9`: 192 priced rows, quote age at build {'median': 61.4, 'max': 81.4}, freshness {'STALE': 192}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 51 | 0.0 | 0.0 | 35.3 | 9.8 | 31.4 | 19.6 | 3.9 | 18.34 | 54.9% | 23.5% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,701 | 19.2 | 10.9 | 25.4 | 18.0 | 18.0 | 7.5 | 1.0 | 8.82 | 26.4% | 8.4% |
| KALSHI_LONE_OUTLIER | 30 | 6.7 | 6.7 | 73.3 | 6.7 | 3.3 | 3.3 | 0.0 | 6.16 | 6.7% | 3.3% |
| MARKETS_AGREE | 995 | 66.6 | 33.4 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,120 | 0.0 | 2.2 | 37.4 | 26.3 | 24.1 | 9.1 | 0.9 | 11.81 | 34.2% | 10.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 47,658 | 7926 (16.6%) | 26.8% | 1.0% | {"EXTERNAL_STALE": 4701, "AGREES_WITH_KALSHI": 2120, "ALL_AGREE": 995, "SUPPORTS_MODEL_DIRECTION": 49, "AGREES_WITH_MODEL": 30, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 21,217 | 1996 (9.4%) | 36.3% | 1.5% | {"EXTERNAL_STALE": 1242, "AGREES_WITH_KALSHI": 724, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 11,861 | 620 (5.2%) | 34.2% | 2.1% | {"EXTERNAL_STALE": 395, "AGREES_WITH_KALSHI": 212, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,512 | 589 (10.7%) | 34.8% | 2.2% | {"EXTERNAL_STALE": 371, "AGREES_WITH_KALSHI": 205, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 19,118 | 4520 (23.6%) | 18.6% | 0.9% | {"EXTERNAL_STALE": 2613, "ALL_AGREE": 995, "AGREES_WITH_KALSHI": 839, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 26, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 9,338 | 10.5 | 7.7 | 19.3 | 14.6 | 21.6 | 16.3 | 10.0 | 14.11 | 47.9% | 26.3% |
| 4-10x | 6,375 | 11.2 | 8.4 | 18.3 | 15.2 | 22.1 | 14.6 | 10.3 | 13.92 | 46.9% | 24.9% |
| <2x | 24,345 | 14.9 | 9.8 | 19.7 | 16.0 | 17.6 | 13.1 | 9.0 | 11.59 | 39.7% | 22.1% |
| >=10x | 7,600 | 10.3 | 6.4 | 15.1 | 14.4 | 21.8 | 18.9 | 13.1 | 16.43 | 53.8% | 32.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 12,520 | 12.4 | 8.6 | 19.7 | 16.2 | 19.1 | 13.6 | 10.5 | 12.8 | 43.1% | 24.1% |
| 300-1000 | 10,297 | 11.8 | 8.7 | 17.6 | 15.1 | 20.8 | 16.4 | 9.7 | 13.82 | 46.8% | 26.0% |
| <300 | 14,919 | 8.2 | 5.8 | 15.1 | 14.7 | 23.1 | 19.9 | 13.1 | 17.18 | 56.1% | 33.0% |
| >=3000 | 9,922 | 21.3 | 12.9 | 23.9 | 15.6 | 14.0 | 7.3 | 5.2 | 7.78 | 26.5% | 12.5% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1465 | 0.549 | 0.4101 | 0.4867 | +0.062 | -0.077 | 0.0017 ± 0.004 |
| ratio 4-10x | 994 | 0.5771 | 0.4329 | 0.4869 | +0.090 | -0.054 | 0.0086 ± 0.005 |
| ratio <2x | 3586 | 0.5361 | 0.4136 | 0.4375 | +0.099 | -0.024 | 0.0142 ± 0.0024 |
| ratio >=10x | 1226 | 0.5667 | 0.3936 | 0.4486 | +0.118 | -0.055 | 0.0141 ± 0.0051 |
| thinner_sample 1000-3000 | 2011 | 0.5395 | 0.4118 | 0.4475 | +0.092 | -0.036 | 0.0113 ± 0.0033 |
| thinner_sample 300-1000 | 1645 | 0.5644 | 0.4244 | 0.4736 | +0.091 | -0.049 | 0.0052 ± 0.0038 |
| thinner_sample <300 | 2343 | 0.5588 | 0.3912 | 0.4558 | +0.103 | -0.065 | 0.0125 ± 0.0037 |
| thinner_sample >=3000 | 1272 | 0.5288 | 0.4353 | 0.4473 | +0.082 | -0.012 | 0.0146 ± 0.0032 |
| data_status ADEQUATE | 2026 | 0.5314 | 0.4286 | 0.4408 | +0.091 | -0.012 | 0.015 ± 0.0027 |
| data_status LIMITED | 1779 | 0.5481 | 0.4151 | 0.4654 | +0.083 | -0.050 | 0.0077 ± 0.0036 |
| data_status POOR | 3466 | 0.5607 | 0.401 | 0.4602 | +0.101 | -0.059 | 0.0101 ± 0.0029 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1050 | 0.1978 | 0.1981 | -0.0002 ± 0.0005 | 0.5757 | 0.5763 | 0.5024 | 0.4872 | 0.499 | -0.094 ± 0.0145 | -0.0087 (8) |
| 3-5 | 671 | 0.2055 | 0.2055 | -0.0000 ± 0.0014 | 0.5958 | 0.5941 | 0.5045 | 0.4647 | 0.4844 | -0.093 ± 0.018 | 0.01 (3) |
| 5-10 | 1562 | 0.2026 | 0.2015 | +0.0011 ± 0.0017 | 0.5918 | 0.5868 | 0.5118 | 0.438 | 0.4648 | -0.092 ± 0.0118 | -0.0143 (7) |
| 10-15 | 1267 | 0.2182 | 0.2093 | +0.0089 ± 0.0032 | 0.6282 | 0.6023 | 0.5239 | 0.4004 | 0.4254 | -0.103 ± 0.0131 | -0.055 (6) |
| 15-25 | 1613 | 0.2259 | 0.2083 | +0.0175 ± 0.0044 | 0.6469 | 0.6002 | 0.576 | 0.3814 | 0.4334 | -0.104 ± 0.0114 | -0.0045 (11) |
| 25-40 | 919 | 0.2232 | 0.2061 | +0.0171 ± 0.0089 | 0.6363 | 0.5934 | 0.6516 | 0.342 | 0.469 | -0.067 ± 0.0138 | -0.06 (2) |
| 40+ | 189 | 0.295 | 0.1767 | +0.1183 ± 0.0274 | 0.7946 | 0.5268 | 0.7316 | 0.2768 | 0.381 | -0.081 ± 0.0265 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5461 | 0.1855 | 0.1864 | -0.0009 ± 0.0002 | 0.5472 | 0.5482 | 0.4905 | 0.4753 | 0.5069 | -0.021 ± 0.0059 | -0.01 (28) |
| 3-5 | 3641 | 0.1981 | 0.1964 | +0.0017 ± 0.0006 | 0.5767 | 0.5705 | 0.4829 | 0.4432 | 0.4416 | -0.056 ± 0.0074 | 0.005 (6) |
| 5-10 | 7899 | 0.2013 | 0.1978 | +0.0035 ± 0.0007 | 0.5884 | 0.5765 | 0.4843 | 0.4107 | 0.4239 | -0.045 ± 0.0051 | -0.0114 (22) |
| 10-15 | 6548 | 0.202 | 0.1861 | +0.0160 ± 0.0013 | 0.5908 | 0.5461 | 0.4856 | 0.3617 | 0.3597 | -0.064 ± 0.0054 | -0.0379 (19) |
| 15-25 | 8283 | 0.2064 | 0.1671 | +0.0393 ± 0.0018 | 0.6047 | 0.4964 | 0.4998 | 0.3043 | 0.3022 | -0.070 ± 0.0045 | -0.0043 (51) |
| 25-40 | 6407 | 0.2225 | 0.1257 | +0.0969 ± 0.0028 | 0.6392 | 0.3863 | 0.5262 | 0.2125 | 0.2191 | -0.058 ± 0.0043 | -0.0733 (3) |
| 40+ | 4282 | 0.3828 | 0.0434 | +0.3393 ± 0.0036 | 0.9966 | 0.1691 | 0.6308 | 0.1011 | 0.0574 | -0.076 ± 0.003 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 844 | 0.2057 | 0.206 | -0.0004 ± 0.0005 | 0.5922 | 0.5933 | 0.5059 | 0.4911 | 0.5142 | -0.101 ± 0.0168 | -0.0117 (6) |
| 3-5 | 598 | 0.2117 | 0.2086 | +0.0031 ± 0.0015 | 0.6066 | 0.5999 | 0.5137 | 0.4742 | 0.4515 | -0.132 ± 0.0201 | 0.01 (3) |
| 5-10 | 1344 | 0.207 | 0.2053 | +0.0017 ± 0.0019 | 0.6003 | 0.5956 | 0.5406 | 0.4661 | 0.4948 | -0.087 ± 0.0127 | -0.01 (4) |
| 10-15 | 1173 | 0.2131 | 0.2067 | +0.0064 ± 0.0033 | 0.619 | 0.5993 | 0.5619 | 0.4374 | 0.4766 | -0.101 ± 0.0138 | -0.04 (5) |
| 15-25 | 1699 | 0.232 | 0.2124 | +0.0195 ± 0.0044 | 0.6597 | 0.6094 | 0.5854 | 0.3899 | 0.4391 | -0.100 ± 0.0114 | -0.0183 (12) |
| 25-40 | 1192 | 0.2672 | 0.1992 | +0.0680 ± 0.0081 | 0.7452 | 0.5788 | 0.6603 | 0.3463 | 0.3968 | -0.117 ± 0.0129 | -0.008 (5) |
| 40+ | 421 | 0.3715 | 0.1626 | +0.2089 ± 0.0197 | 1.0133 | 0.4914 | 0.7364 | 0.2476 | 0.2922 | -0.087 ± 0.0189 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4686 | 0.1921 | 0.1923 | -0.0002 ± 0.0002 | 0.56 | 0.5601 | 0.5076 | 0.4925 | 0.5077 | -0.040 ± 0.0066 | -0.0154 (26) |
| 3-5 | 3191 | 0.1927 | 0.1915 | +0.0012 ± 0.0006 | 0.5622 | 0.5584 | 0.5115 | 0.4718 | 0.476 | -0.047 ± 0.0079 | 0.01 (5) |
| 5-10 | 7065 | 0.1968 | 0.1936 | +0.0033 ± 0.0008 | 0.5786 | 0.5664 | 0.5088 | 0.4347 | 0.4522 | -0.039 ± 0.0053 | -0.0117 (6) |
| 10-15 | 5863 | 0.2027 | 0.1913 | +0.0114 ± 0.0014 | 0.5947 | 0.5595 | 0.5099 | 0.3859 | 0.4029 | -0.048 ± 0.0058 | -0.0189 (18) |
| 15-25 | 8338 | 0.2171 | 0.1812 | +0.0359 ± 0.0018 | 0.6312 | 0.5315 | 0.5254 | 0.3299 | 0.3383 | -0.060 ± 0.0047 | -0.014 (52) |
| 25-40 | 7498 | 0.251 | 0.1378 | +0.1132 ± 0.0027 | 0.7089 | 0.4206 | 0.5603 | 0.2434 | 0.2269 | -0.080 ± 0.0043 | -0.0095 (20) |
| 40+ | 5880 | 0.4017 | 0.0579 | +0.3438 ± 0.0036 | 1.0584 | 0.2096 | 0.654 | 0.1178 | 0.0789 | -0.074 ± 0.0031 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1026 | 0.1961 | 0.1975 | -0.0013 ± 0.0005 | 0.5721 | 0.5753 | 0.5019 | 0.4865 | 0.5292 | -0.053 ± 0.0145 | -0.0191 (11) |
| 3-5 | 725 | 0.2074 | 0.2059 | +0.0015 ± 0.0014 | 0.6013 | 0.5959 | 0.4987 | 0.4591 | 0.4621 | -0.110 ± 0.0176 | 0.002 (5) |
| 5-10 | 1593 | 0.2031 | 0.1994 | +0.0036 ± 0.0017 | 0.5914 | 0.5812 | 0.5125 | 0.4388 | 0.4501 | -0.105 ± 0.0115 | -0.01 (10) |
| 10-15 | 1279 | 0.2116 | 0.203 | +0.0087 ± 0.0031 | 0.6137 | 0.5885 | 0.5372 | 0.4139 | 0.4425 | -0.105 ± 0.0127 | -0.0286 (7) |
| 15-25 | 1544 | 0.2311 | 0.2132 | +0.0179 ± 0.0046 | 0.6598 | 0.6109 | 0.5867 | 0.3926 | 0.443 | -0.106 ± 0.0118 | -0.03 (1) |
| 25-40 | 906 | 0.2127 | 0.2102 | +0.0025 ± 0.0089 | 0.614 | 0.6027 | 0.6594 | 0.3486 | 0.4978 | -0.054 ± 0.0138 | -0.0267 (3) |
| 40+ | 198 | 0.3082 | 0.1841 | +0.1242 ± 0.0273 | 0.8344 | 0.5426 | 0.7433 | 0.2886 | 0.3889 | -0.085 ± 0.028 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5268 | 0.1857 | 0.1864 | -0.0007 ± 0.0002 | 0.5471 | 0.5479 | 0.4858 | 0.4704 | 0.4899 | -0.032 ± 0.006 | -0.0189 (44) |
| 3-5 | 3769 | 0.2037 | 0.2019 | +0.0018 ± 0.0006 | 0.5925 | 0.5863 | 0.48 | 0.4405 | 0.438 | -0.057 ± 0.0074 | -0.0073 (22) |
| 5-10 | 8048 | 0.1959 | 0.1906 | +0.0054 ± 0.0007 | 0.5752 | 0.5585 | 0.4871 | 0.4131 | 0.414 | -0.057 ± 0.0049 | -0.0117 (42) |
| 10-15 | 6485 | 0.1938 | 0.1789 | +0.0149 ± 0.0013 | 0.5724 | 0.5292 | 0.4947 | 0.3713 | 0.3726 | -0.061 ± 0.0053 | -0.0136 (14) |
| 15-25 | 8360 | 0.2121 | 0.1728 | +0.0394 ± 0.0018 | 0.6182 | 0.5094 | 0.513 | 0.3185 | 0.3154 | -0.070 ± 0.0045 | -0.0533 (3) |
| 25-40 | 6367 | 0.216 | 0.1262 | +0.0899 ± 0.0028 | 0.6253 | 0.3869 | 0.528 | 0.2125 | 0.2298 | -0.049 ± 0.0043 | -0.02 (4) |
| 40+ | 4224 | 0.3917 | 0.0484 | +0.3433 ± 0.0038 | 1.0207 | 0.1816 | 0.6399 | 0.1073 | 0.0644 | -0.076 ± 0.0032 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1464 | 0.198 | 0.198 | +0.0000 ± 0.0004 | 0.5746 | 0.5745 | 0.5086 | 0.4936 | 0.4973 | -0.069 ± 0.0119 | -0.0221 (56) |
| 3-5 | 1051 | 0.1886 | 0.1885 | +0.0001 ± 0.0011 | 0.5554 | 0.5533 | 0.4975 | 0.4576 | 0.4748 | -0.057 ± 0.0137 | -0.0194 (34) |
| 5-10 | 2118 | 0.2 | 0.1951 | +0.0048 ± 0.0014 | 0.5897 | 0.5736 | 0.5078 | 0.4342 | 0.4386 | -0.077 ± 0.0098 | -0.005 (78) |
| 10-15 | 1454 | 0.2143 | 0.2022 | +0.0121 ± 0.0029 | 0.6222 | 0.588 | 0.5419 | 0.4191 | 0.4298 | -0.087 ± 0.0121 | 0.0012 (66) |
| 15-25 | 1903 | 0.2307 | 0.2077 | +0.0230 ± 0.0041 | 0.6585 | 0.5993 | 0.5918 | 0.3969 | 0.4372 | -0.088 ± 0.0105 | -0.0214 (59) |
| 25-40 | 1140 | 0.2404 | 0.2106 | +0.0298 ± 0.0083 | 0.6864 | 0.6042 | 0.6888 | 0.3769 | 0.4851 | -0.087 ± 0.0128 | -0.0252 (27) |
| 40+ | 409 | 0.3247 | 0.2019 | +0.1229 ± 0.0212 | 0.9346 | 0.5875 | 0.8182 | 0.3424 | 0.467 | -0.097 ± 0.0198 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5381 | 0.178 | 0.1781 | -0.0001 ± 0.0002 | 0.5265 | 0.5262 | 0.5119 | 0.4967 | 0.5051 | -0.040 ± 0.0058 | -0.0154 (103) |
| 3-5 | 3720 | 0.195 | 0.1942 | +0.0008 ± 0.0006 | 0.5691 | 0.5667 | 0.5016 | 0.4619 | 0.4723 | -0.040 ± 0.0073 | -0.0212 (73) |
| 5-10 | 7559 | 0.1965 | 0.1901 | +0.0065 ± 0.0008 | 0.5803 | 0.5604 | 0.5014 | 0.4279 | 0.422 | -0.062 ± 0.0051 | -0.0084 (134) |
| 10-15 | 5170 | 0.2096 | 0.1935 | +0.0161 ± 0.0015 | 0.6104 | 0.5676 | 0.537 | 0.414 | 0.4085 | -0.071 ± 0.0062 | -0.0057 (111) |
| 15-25 | 6296 | 0.2316 | 0.2 | +0.0316 ± 0.0022 | 0.6652 | 0.5794 | 0.5771 | 0.3817 | 0.3995 | -0.068 ± 0.0057 | -0.026 (108) |
| 25-40 | 4105 | 0.257 | 0.1906 | +0.0664 ± 0.0043 | 0.7273 | 0.5548 | 0.6407 | 0.3284 | 0.381 | -0.065 ± 0.0067 | -0.0277 (53) |
| 40+ | 1819 | 0.3696 | 0.1592 | +0.2104 ± 0.0097 | 1.0429 | 0.4743 | 0.7458 | 0.2451 | 0.2958 | -0.064 ± 0.0089 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7271 | 1.027 ± 0.033 | 1.099 | 0.1686 | 0.168 | 0.2151 | 0.2042 |
| gen2 | 7271 | 0.819 ± 0.03 | 1.07 | 0.1733 | 0.1684 | 0.2335 | 0.2041 |
| gen1_elo | 7271 | 1.011 ± 0.032 | 1.089 | 0.175 | 0.1681 | 0.214 | 0.2043 |
| gen1_sr | 7271 | 1.006 ± 0.039 | 1.128 | 0.1333 | 0.17 | 0.2295 | 0.2038 |
| gen1_ledger | 9539 | 0.866 ± 0.024 | 1.076 | 0.1896 | 0.1751 | 0.2169 | 0.2006 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 33,738)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 7,820 | 23.2% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,720 | 22.9% |
| BOOK_QUALITY | execution | 6,003 | 17.8% |
| POOR_DATA | data | 3,871 | 11.5% |
| LIMITED_DATA | data | 2,088 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,945 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 1,400 | 4.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,373 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 963 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 554 | 1.6% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 23.2%, coverage 22.9%, execution 17.8%, data 17.7%, market_freshness/coverage 8.6%, mapping 4.2%, model_calibration_or_unknown 4.1%, model_calibration 1.6%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.6%, LOW_DATA_QUALITY 71.4%, THIN_PLAYER_HISTORY 59.6%, STALE_PLAYER_DATA 51.9%, STALE_KALSHI_QUOTE 46.4%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 24.0%, MODEL_HIGH_UNCERTAINTY 18.7%, PLAYER_IDENTITY_RISK 15.3%, LEVEL_TRANSFER_RISK 9.9%, LOW_DISPLAYED_LIQUIDITY 8.3%, EVENT_MAPPING_RISK 7.2%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.3%, POST_SETTLEMENT_OBSERVATION 22.9%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 17,955)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,191 | 34.5% |
| STALE_QUOTE | market_freshness | 3,482 | 19.4% |
| BOOK_QUALITY | execution | 3,113 | 17.3% |
| POOR_DATA | data | 1,631 | 9.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,037 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 779 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 631 | 3.5% |
| LIMITED_DATA | data | 614 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 339 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 137 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.5%, market_freshness 19.4%, execution 17.3%, data 12.5%, market_freshness/coverage 9.3%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 74.7%, THIN_PLAYER_HISTORY 61.6%, STALE_KALSHI_QUOTE 53.8%, STALE_PLAYER_DATA 45.6%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 34.2%, WIDE_SPREAD 23.4%, MODEL_HIGH_UNCERTAINTY 19.4%, PLAYER_IDENTITY_RISK 18.3%, EVENT_MAPPING_RISK 8.8%, LEVEL_TRANSFER_RISK 8.7%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.5%, POST_SETTLEMENT_OBSERVATION 34.5%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 14341, "IDENTITY_AMBIGUOUS": 3614}; ticker orientation: {"VERIFIED": 17955}.

Checks: discipline:AMBIGUOUS 1199, discipline:PASS 16756, identity_confidence:AMBIGUOUS 3283, identity_confidence:PASS 14672, level_mapping:NA 1211, level_mapping:PASS 16744, market_pair:AMBIGUOUS 492, market_pair:NA 411, market_pair:PASS 17052, model_complement:NA 373, model_complement:PASS 17582, namesake:AMBIGUOUS 6, namesake:PASS 17949, physical_match_id:NA 6094, physical_match_id:PASS 11861, player_ids:PASS 17955, same_pair_other_event:PASS 17955, ticker_orientation:PASS 17955

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,404 | 3.8% | 3.2% | 1.4% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 24, "market_freshness/coverage": 21} | 5.51 | 0.2235 / 0.2191 (831) | 24.9% | 2.5% | 3.0% | 2.9% |
| CHALLENGER | 11,848 | 16.5% | 6.2% | 10.9% | {"coverage": 1168, "market_freshness": 229, "market_freshness/coverage": 225, "data": 163, "model_calibration_or_unknown": 78, "execution": 41, "model_calibration": 38, "mapping": 17, "possible_market_error": 1} | 7.39 | 0.221 / 0.2103 (2801) | 38.3% | 14.9% | 4.0% | 22.6% |
| DOUBLES | 2,585 | 46.4% | 46.4% | 6.7% | {"execution": 665, "mapping": 351, "market_freshness": 106, "market_freshness/coverage": 70, "coverage": 7} | 23.21 | 0.2973 / 0.232 (648) | 9.0% | 0.0% | 100.0% | 6.4% |
| ITF_MEN | 23,431 | 25.0% | 17.4% | 32.6% | {"coverage": 2060, "market_freshness": 1141, "execution": 991, "data": 856, "market_freshness/coverage": 591, "mapping": 206, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.66 | 0.2177 / 0.2 (4986) | 40.1% | 68.8% | 15.1% | 21.6% |
| ITF_WOMEN | 30,607 | 26.5% | 18.9% | 45.1% | {"coverage": 2877, "market_freshness": 1745, "execution": 1333, "data": 1125, "market_freshness/coverage": 704, "mapping": 199, "model_calibration_or_unknown": 94, "model_calibration": 23} | 12.51 | 0.2024 / 0.1941 (5936) | 41.4% | 57.1% | 9.9% | 21.8% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,858 | 6.0% | 5.1% | 1.6% | {"market_freshness": 111, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.68 | 0.2305 / 0.2205 (796) | 30.0% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.6% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 404 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.4h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 509 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 311 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 769 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 12 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 547 min (STALE); no external reference |
| 15 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 18 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
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
| 29 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 30 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 31 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 32 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 33 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 34 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 35 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 36 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 37 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 38 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 39 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 40 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 41 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 43 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 44 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 45 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 46 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.1h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 446 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 49 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 50 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 252 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9702, "by_level_share_of_ge_25pp": {"ATP": 0.0136, "CHALLENGER": 0.1092, "DOUBLES": 0.0668, "ITF_MEN": 0.3261, "ITF_WOMEN": 0.4511, "OTHER": 0.0007, "WTA": 0.0162, "WTA125": 0.0163}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5385, "share_primary_cause_market_settled_or_in_play": 0.4377, "share_primary_cause_stale_quote_only": 0.1939}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 17955, "identity_ambiguous_share": 0.2013, "ticker_orientation": {"VERIFIED": 17955}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 11861, "with_external": 620, "coverage": 0.0523, "external_status": {"EXTERNAL_STALE": 395, "AGREES_WITH_KALSHI": 212, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 395, "MODEL_LONE_OUTLIER": 212, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3419, "share_external_supports_model": 0.021}, "pregame_clean_ge_25pp": {"n": 5512, "with_external": 589, "coverage": 0.1069, "external_status": {"EXTERNAL_STALE": 371, "AGREES_WITH_KALSHI": 205, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 371, "MODEL_LONE_OUTLIER": 205, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.348, "share_external_supports_model": 0.0221}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 494.0, "median_sample_ratio": 2.45, "median_min_matches": 19.0, "median_max_days_since_last": 240.0, "share_severe_asymmetry": 0.2082, "data_status": {"POOR": 10032, "LIMITED": 4664, "ADEQUATE": 3259}, "comparison_lt_10pp": {"median_thinner_serve_points": 1736.0, "median_sample_ratio": 1.7, "median_min_matches": 91.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1465, "model_minus_observed": 0.0623, "kalshi_minus_observed": -0.0766, "brier_diff_model_minus_kalshi": 0.0017}, "4-10x": {"n": 994, "model_minus_observed": 0.0902, "kalshi_minus_observed": -0.054, "brier_diff_model_minus_kalshi": 0.0086}, "<2x": {"n": 3586, "model_minus_observed": 0.0986, "kalshi_minus_observed": -0.024, "brier_diff_model_minus_kalshi": 0.0142}, ">=10x": {"n": 1226, "model_minus_observed": 0.1181, "kalshi_minus_observed": -0.055, "brier_diff_model_minus_kalshi": 0.0141}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 7271, "model": {"intercept": -0.552, "slope": 0.819, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.182, "slope": 1.07, "slope_se": 0.033}, "mean_extremity_model": 0.1733, "mean_extremity_kalshi": 0.1684, "model_brier": 0.2335, "kalshi_brier": 0.2041, "brier_diff_model_minus_kalshi": 0.0294, "brier_diff_se": 0.0022, "model_logloss": 0.6644, "kalshi_logloss": 0.5907}, "fair_v1": {"n": 7271, "model": {"intercept": -0.447, "slope": 1.027, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.247, "slope": 1.099, "slope_se": 0.034}, "mean_extremity_model": 0.1686, "mean_extremity_kalshi": 0.168, "model_brier": 0.2151, "kalshi_brier": 0.2042, "brier_diff_model_minus_kalshi": 0.0109, "brier_diff_se": 0.0018, "model_logloss": 0.6193, "kalshi_logloss": 0.5909}, "gen1_elo": {"n": 7271, "model": {"intercept": -0.437, "slope": 1.011, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.248, "slope": 1.089, "slope_se": 0.033}, "mean_extremity_model": 0.175, "mean_extremity_kalshi": 0.1681, "model_brier": 0.214, "kalshi_brier": 0.2043, "brier_diff_model_minus_kalshi": 0.0098, "brier_diff_se": 0.0018, "model_logloss": 0.6175, "kalshi_logloss": 0.5911}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2489, "share_ge_15": 0.4452, "median_abs_gap": 13.08, "n": 47658}, "gen1_elo": {"share_ge_25": 0.2461, "share_ge_15": 0.4408, "median_abs_gap": 12.86, "n": 47658}, "gen1_sr": {"share_ge_25": 0.3134, "share_ge_15": 0.5208, "median_abs_gap": 15.85, "n": 47658}, "gen2": {"share_ge_25": 0.3144, "share_ge_15": 0.5109, "median_abs_gap": 15.48, "n": 47658}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1505, "share_ge_15": 0.3534, "median_abs_gap": 10.7, "n": 36619}, "gen1_elo": {"share_ge_25": 0.1485, "share_ge_15": 0.3481, "median_abs_gap": 10.49, "n": 36619}, "gen1_sr": {"share_ge_25": 0.215, "share_ge_15": 0.439, "median_abs_gap": 12.97, "n": 36621}, "gen2": {"share_ge_25": 0.2305, "share_ge_15": 0.4385, "median_abs_gap": 12.85, "n": 36621}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.51, "share_ge_25_all": 0.0381, "share_ge_25_pregame_clean": 0.032}, "WTA": {"median_abs_gap_pregame_clean": 7.68, "share_ge_25_all": 0.0599, "share_ge_25_pregame_clean": 0.0508}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2365, "share_within_10pp_all": 0.4383, "share_within_10pp_pregame_clean": 0.492, "corr_model_vs_mid_pregame_clean": 0.8503}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1050, "model_brier": 0.1978, "kalshi_brier": 0.1981, "brier_diff_model_minus_kalshi": -0.0002}, "10-15": {"n_settled": 1267, "model_brier": 0.2182, "kalshi_brier": 0.2093, "brier_diff_model_minus_kalshi": 0.0089}, "15-25": {"n_settled": 1613, "model_brier": 0.2259, "kalshi_brier": 0.2083, "brier_diff_model_minus_kalshi": 0.0175}, "25-40": {"n_settled": 919, "model_brier": 0.2232, "kalshi_brier": 0.2061, "brier_diff_model_minus_kalshi": 0.0171}, "3-5": {"n_settled": 671, "model_brier": 0.2055, "kalshi_brier": 0.2055, "brier_diff_model_minus_kalshi": -0.0}, "40+": {"n_settled": 189, "model_brier": 0.295, "kalshi_brier": 0.1767, "brier_diff_model_minus_kalshi": 0.1183}, "5-10": {"n_settled": 1562, "model_brier": 0.2026, "kalshi_brier": 0.2015, "brier_diff_model_minus_kalshi": 0.0011}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.552, "slope": 0.819, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.182, "slope": 1.07, "slope_se": 0.033}, "n": 7271}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.484, "slope": 0.866, "slope_se": 0.024}, "kalshi_slope": {"intercept": 0.175, "slope": 1.076, "slope_se": 0.028}, "n": 9539}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 648, "model_brier": 0.2973, "kalshi_brier": 0.232, "brier_diff_model_minus_kalshi": 0.0653, "brier_diff_se": 0.0115, "corr_model_outcome": 0.1062, "corr_kalshi_outcome": 0.2841}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
