# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-13T07:47Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 91,510): 0-3 13.9%, 3-5 9.5%, 5-10 20.1%, 10-15 15.2%, 15-25 19.2%, 25-40 13.8%, 40+ 8.3%; median gap 11.94 pp.
* **Where the extremes live**: 97.3% of >=25 pp gaps are off the ATP/WTA main tour (ITF 78.4%, Challenger 11.0%, doubles 6.4%). Main tour: ATP 3.7% and WTA 5.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 20,225): MARKET_ALREADY_SETTLED_WHEN_PRICED 35.4%, STALE_QUOTE 20.1%, BOOK_QUALITY 16.2%, POOR_DATA 9.0%, POSSIBLY_IN_PLAY_QUOTE 5.9%, IDENTITY_AMBIGUOUS 4.2%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 1.7%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 35.4%, market_freshness 20.1%, execution 16.2%, data 12.3%, market_freshness/coverage 9.4%, mapping 4.2%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 55.7% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 44.7% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 20,225 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.8%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.9% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 483.5 points vs 1668.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.023, Gen-2 0.82, Gen-1 ledger 0.866 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 1035 model 0.2253 vs Kalshi 0.2035; n 213 model 0.3055 vs Kalshi 0.1669.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 379,459 model-market comparisons (628,545 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 124,833 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-13T07:33:43.033204+00:00'], shadow board 106,029 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-13T07:33:45.688011+00:00'], Model 4 44,220 rows, 31,487 settled tickers, 11,914 tickers with an external scan.
* By model: {"gen1_ledger": 83391, "gen1_elo": 53280, "fair_v1": 53280, "gen2": 53280, "gen1_sr": 53280, "model4_fundamental": 41516, "model4_conditioned": 41432}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 91,510 | 13.9 | 9.5 | 20.1 | 15.2 | 19.2 | 13.8 | 8.3 | 11.94 | 41.3% | 22.1% |
| MW fair_v1 | 53,280 | 12.5 | 8.6 | 18.7 | 15.2 | 19.6 | 15.1 | 10.4 | 13.22 | 45.0% | 25.4% |
| MW gen1_elo | 53,280 | 12.3 | 8.7 | 19.1 | 15.2 | 19.4 | 15.0 | 10.2 | 13.01 | 44.6% | 25.2% |
| MW gen1_ledger | 38,230 | 15.8 | 10.8 | 22.2 | 15.2 | 18.6 | 12.0 | 5.5 | 10.29 | 36.1% | 17.5% |
| MW gen1_sr | 53,280 | 9.9 | 7.1 | 16.5 | 13.9 | 20.9 | 18.8 | 12.8 | 16.0 | 52.5% | 31.7% |
| MW gen2 | 53,280 | 10.8 | 7.5 | 16.6 | 13.7 | 19.7 | 17.7 | 13.9 | 15.55 | 51.4% | 31.7% |
| all families model4_conditioned | 41,432 | 22.2 | 17.9 | 34.6 | 16.9 | 5.0 | 2.2 | 1.2 | 6.06 | 8.4% | 3.4% |
| all families model4_fundamental | 41,516 | 17.3 | 13.5 | 34.0 | 19.9 | 9.9 | 3.8 | 1.5 | 7.61 | 15.2% | 5.3% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.5%, >=15pp 41.3%, >=20pp 30.5%, >=25pp 22.1%, >=30pp 16.0%, >=40pp 8.3%, >=50pp 3.9%
Executable gap (model outside the book, before fees): median 8.59pp; >=10pp 45.7%, >=25pp 17.6%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,126 | 27.9 | 15.9 | 28.0 | 13.3 | 10.7 | 3.5 | 0.6 | 5.77 | 14.9% | 4.1% |
| CHALLENGER | 8,355 | 16.3 | 9.6 | 20.6 | 15.3 | 15.8 | 11.3 | 11.2 | 10.93 | 38.2% | 22.5% |
| ITF_MEN | 15,723 | 9.6 | 7.3 | 17.1 | 14.9 | 21.1 | 17.2 | 12.8 | 15.45 | 51.1% | 30.0% |
| ITF_WOMEN | 20,637 | 9.3 | 7.0 | 16.1 | 14.6 | 22.2 | 18.7 | 12.1 | 16.04 | 52.9% | 30.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,106 | 16.6 | 13.3 | 24.9 | 20.7 | 16.7 | 6.7 | 1.1 | 8.65 | 24.5% | 7.8% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,126 | 26.3 | 15.7 | 26.3 | 15.8 | 11.3 | 3.9 | 0.8 | 6.1 | 16.0% | 4.7% |
| CHALLENGER | 8,355 | 14.4 | 9.1 | 19.0 | 13.8 | 18.4 | 13.6 | 11.6 | 12.55 | 43.7% | 25.2% |
| ITF_MEN | 15,723 | 8.1 | 6.2 | 15.2 | 13.8 | 20.4 | 19.9 | 16.3 | 17.84 | 56.6% | 36.2% |
| ITF_WOMEN | 20,637 | 7.8 | 5.8 | 14.1 | 12.6 | 20.7 | 21.2 | 17.7 | 19.2 | 59.6% | 39.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,106 | 14.1 | 10.3 | 21.6 | 16.2 | 22.5 | 12.8 | 2.5 | 11.23 | 37.8% | 15.3% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,126 | 23.4 | 14.1 | 25.6 | 15.5 | 14.3 | 5.9 | 1.1 | 7.03 | 21.3% | 7.0% |
| CHALLENGER | 8,355 | 15.1 | 9.6 | 20.8 | 15.6 | 16.0 | 11.9 | 11.0 | 11.16 | 38.9% | 22.9% |
| ITF_MEN | 15,723 | 9.3 | 7.3 | 17.3 | 14.3 | 21.4 | 17.3 | 13.1 | 15.73 | 51.8% | 30.4% |
| ITF_WOMEN | 20,637 | 9.2 | 6.8 | 16.2 | 15.5 | 22.1 | 18.7 | 11.4 | 15.82 | 52.2% | 30.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,106 | 22.4 | 17.2 | 31.8 | 15.3 | 9.0 | 3.3 | 1.0 | 6.12 | 13.3% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,495 | 28.1 | 19.6 | 29.1 | 12.1 | 8.1 | 2.5 | 0.4 | 5.24 | 11.1% | 3.0% |
| CHALLENGER | 5,061 | 23.0 | 14.6 | 27.8 | 14.7 | 13.0 | 5.4 | 1.5 | 7.0 | 19.9% | 6.9% |
| DOUBLES | 2,808 | 4.8 | 4.5 | 12.8 | 11.1 | 20.6 | 24.8 | 21.6 | 23.23 | 66.9% | 46.3% |
| ITF_MEN | 11,358 | 12.8 | 9.5 | 21.5 | 15.7 | 21.6 | 12.9 | 6.0 | 11.78 | 40.5% | 18.9% |
| ITF_WOMEN | 13,274 | 13.4 | 9.3 | 19.9 | 15.8 | 21.7 | 14.6 | 5.4 | 12.17 | 41.6% | 20.0% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,829 | 23.9 | 15.9 | 31.8 | 16.8 | 8.9 | 2.5 | 0.2 | 6.57 | 11.6% | 2.7% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,997 | 28.4 | 16.1 | 28.4 | 13.2 | 10.5 | 3.1 | 0.3 | 5.64 | 13.9% | 3.4% |
| CHALLENGER | 5,869 | 21.0 | 12.1 | 25.7 | 18.0 | 15.8 | 5.5 | 1.8 | 8.21 | 23.2% | 7.4% |
| ITF_MEN | 11,381 | 11.8 | 8.7 | 20.6 | 17.2 | 22.1 | 14.0 | 5.5 | 12.44 | 41.6% | 19.4% |
| ITF_WOMEN | 14,981 | 11.3 | 8.6 | 19.1 | 17.0 | 24.1 | 15.3 | 4.6 | 13.14 | 44.0% | 19.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,992 | 16.9 | 13.3 | 25.2 | 21.1 | 16.7 | 6.2 | 0.6 | 8.46 | 23.5% | 6.8% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,997 | 26.6 | 16.0 | 26.6 | 15.7 | 11.2 | 3.4 | 0.4 | 6.02 | 15.0% | 3.8% |
| CHALLENGER | 5,869 | 18.1 | 11.7 | 23.9 | 16.3 | 19.0 | 9.0 | 2.1 | 8.99 | 30.1% | 11.0% |
| ITF_MEN | 11,383 | 9.6 | 7.4 | 17.8 | 16.0 | 22.3 | 17.9 | 9.0 | 14.71 | 49.2% | 26.9% |
| ITF_WOMEN | 14,983 | 8.9 | 7.0 | 16.1 | 14.2 | 22.6 | 20.6 | 10.7 | 16.52 | 53.8% | 31.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,992 | 14.3 | 10.5 | 21.8 | 16.4 | 22.7 | 12.5 | 1.9 | 11.03 | 37.0% | 14.4% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,425 | 28.4 | 19.8 | 29.1 | 12.3 | 7.8 | 2.3 | 0.3 | 5.2 | 10.4% | 2.6% |
| CHALLENGER | 4,479 | 24.4 | 15.4 | 28.9 | 14.9 | 12.3 | 3.7 | 0.4 | 6.53 | 16.4% | 4.1% |
| DOUBLES | 2,627 | 4.7 | 4.5 | 13.0 | 11.1 | 20.4 | 24.7 | 21.7 | 23.2 | 66.7% | 46.4% |
| ITF_MEN | 9,811 | 13.6 | 10.0 | 22.9 | 16.3 | 21.6 | 11.4 | 4.1 | 10.9 | 37.2% | 15.5% |
| ITF_WOMEN | 11,426 | 14.1 | 9.8 | 20.9 | 16.3 | 21.8 | 13.4 | 3.6 | 11.41 | 38.9% | 17.0% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,766 | 24.2 | 16.3 | 31.8 | 16.8 | 8.8 | 2.0 | 0.1 | 6.43 | 10.9% | 2.0% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,808 | 4.8 | 4.5 | 12.8 | 11.1 | 20.6 | 24.8 | 21.6 | 23.23 | 66.9% | 46.3% |
| singles | 35,422 | 16.6 | 11.3 | 22.9 | 15.5 | 18.4 | 10.9 | 4.3 | 9.76 | 33.6% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 11,573 | 12.7 | 9.0 | 19.2 | 15.0 | 19.6 | 14.4 | 10.1 | 13.0 | 44.1% | 24.5% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 34,652 | 12.9 | 8.6 | 18.8 | 15.1 | 19.2 | 15.1 | 10.3 | 13.04 | 44.6% | 25.3% |
| UNKNOWN | 6,642 | 10.4 | 7.5 | 17.1 | 16.6 | 21.5 | 15.8 | 11.1 | 14.32 | 48.4% | 26.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 14,773 | 19.0 | 11.8 | 22.4 | 15.8 | 14.9 | 9.5 | 6.6 | 9.04 | 31.0% | 16.1% |
| B | 6,339 | 13.0 | 8.5 | 19.5 | 15.2 | 19.7 | 12.4 | 11.6 | 12.81 | 43.7% | 24.0% |
| C | 7,589 | 11.9 | 8.5 | 19.3 | 15.9 | 19.3 | 14.7 | 10.3 | 13.02 | 44.3% | 25.0% |
| D | 8,813 | 11.2 | 8.4 | 17.8 | 15.2 | 21.7 | 15.7 | 10.0 | 14.1 | 47.4% | 25.7% |
| F | 15,766 | 7.3 | 5.7 | 15.0 | 14.3 | 23.0 | 21.1 | 13.7 | 18.05 | 57.7% | 34.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 10,014 | 24.9 | 15.9 | 29.0 | 14.9 | 10.6 | 3.4 | 1.3 | 6.36 | 15.2% | 4.7% |
| B | 5,205 | 16.7 | 11.0 | 24.1 | 17.0 | 18.9 | 9.4 | 2.9 | 9.6 | 31.1% | 12.3% |
| C | 7,555 | 11.0 | 7.8 | 19.5 | 15.0 | 21.0 | 15.7 | 10.1 | 13.49 | 46.7% | 25.7% |
| D | 5,847 | 14.4 | 9.9 | 21.1 | 15.4 | 21.1 | 12.8 | 5.3 | 11.38 | 39.2% | 18.1% |
| F | 9,609 | 10.2 | 8.4 | 16.7 | 14.4 | 23.4 | 18.8 | 8.0 | 15.09 | 50.2% | 26.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 16,741 | 17.5 | 10.9 | 21.3 | 15.5 | 15.2 | 10.2 | 9.3 | 10.03 | 34.7% | 19.5% |
| LIMITED | 11,563 | 13.5 | 9.4 | 20.4 | 15.9 | 19.9 | 13.4 | 7.6 | 11.98 | 40.8% | 20.9% |
| POOR | 24,976 | 8.8 | 6.7 | 16.1 | 14.6 | 22.4 | 19.1 | 12.4 | 16.36 | 53.9% | 31.4% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,330 | 23.8 | 18.0 | 33.0 | 15.4 | 6.4 | 3.0 | 0.4 | 5.89 | 9.8% | 3.4% |
| GAME_SPREAD | 6,969 | 22.8 | 15.3 | 32.0 | 16.8 | 9.1 | 3.3 | 0.7 | 6.69 | 13.0% | 4.0% |
| MATCH_WINNER | 38,230 | 15.8 | 10.8 | 22.2 | 15.2 | 18.6 | 12.0 | 5.5 | 10.29 | 36.1% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 17,159 | 28.3 | 16.8 | 30.7 | 12.7 | 8.8 | 2.3 | 0.3 | 5.58 | 11.4% | 2.6% |
| TOTAL_GAMES | 11,679 | 9.7 | 10.8 | 36.4 | 25.6 | 10.4 | 4.2 | 2.9 | 9.14 | 17.4% | 7.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,734 | 24.5 | 28.8 | 33.3 | 8.1 | 3.9 | 1.2 | 0.3 | 4.79 | 5.4% | 1.5% |
| GAME_SPREAD | 9,585 | 46.6 | 15.8 | 25.2 | 7.4 | 2.4 | 1.9 | 0.6 | 3.33 | 4.9% | 2.5% |
| TOTAL_GAMES | 17,113 | 6.5 | 9.8 | 41.0 | 29.8 | 7.2 | 3.3 | 2.3 | 9.15 | 12.9% | 5.6% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,770 | 23.8 | 16.6 | 34.7 | 14.8 | 6.9 | 2.7 | 0.5 | 6.05 | 10.1% | 3.2% |
| GAME_SPREAD | 9,594 | 20.3 | 13.4 | 28.4 | 20.2 | 12.2 | 4.3 | 1.1 | 7.71 | 17.6% | 5.5% |
| TOTAL_GAMES | 17,152 | 10.0 | 10.9 | 36.5 | 24.3 | 11.3 | 4.4 | 2.6 | 9.01 | 18.3% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 53,280 | 45.0% | 25.4% | 13.22 | 35.5% | 15.2% | 10.72 |
| gen1_elo | 53,280 | 44.6% | 25.2% | 13.01 | 34.9% | 15.0% | 10.51 |
| gen1_sr | 53,280 | 52.5% | 31.7% | 16.0 | 44.0% | 21.5% | 13.0 |
| gen2 | 53,280 | 51.4% | 31.7% | 15.55 | 43.9% | 23.0% | 12.84 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,471 | 15.4 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.72 | 35.4% | 15.3% |
| STALE | 32,809 | 10.7 | 7.4 | 17.0 | 13.9 | 19.3 | 17.0 | 14.7 | 15.41 | 51.0% | 31.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 31,698 | 16.3 | 11.1 | 22.7 | 15.3 | 18.2 | 11.5 | 5.0 | 9.98 | 34.7% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 91,510 | 31698 | 23943 | 35869 | 25.3 | 148.7 | 1451.1 |
| ge_15pp | 37,785 | 10995 | 8544 | 18246 | 29.1 | 453.0 | 1451.1 |
| ge_25pp | 20,225 | 5225 | 3732 | 11268 | 35.0 | 595.3 | 1431.1 |
| lt_10pp | 39,835 | 15866 | 11312 | 12657 | 22.8 | 49.7 | 1421.7 |

Current slate `SL-20261113T074710Z-c006a4bc`: 264 priced rows, quote age at build {'median': 13.7, 'max': 13.8}, freshness {'AGING': 264}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 52 | 0.0 | 0.0 | 34.6 | 9.6 | 32.7 | 19.2 | 3.9 | 18.34 | 55.8% | 23.1% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 5,110 | 19.1 | 11.2 | 25.7 | 18.3 | 17.7 | 7.1 | 1.0 | 8.77 | 25.8% | 8.0% |
| KALSHI_LONE_OUTLIER | 32 | 6.2 | 6.2 | 75.0 | 6.2 | 3.1 | 3.1 | 0.0 | 6.16 | 6.2% | 3.1% |
| MARKETS_AGREE | 1,084 | 66.3 | 33.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,321 | 0.0 | 2.1 | 38.4 | 26.0 | 23.8 | 8.8 | 0.9 | 11.66 | 33.5% | 9.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 53,280 | 8628 (16.2%) | 26.9% | 0.9% | {"EXTERNAL_STALE": 5110, "AGREES_WITH_KALSHI": 2321, "ALL_AGREE": 1084, "SUPPORTS_MODEL_DIRECTION": 50, "AGREES_WITH_MODEL": 32, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 23,991 | 2124 (8.8%) | 36.6% | 1.5% | {"EXTERNAL_STALE": 1316, "AGREES_WITH_KALSHI": 777, "SUPPORTS_MODEL_DIRECTION": 29, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 13,538 | 648 (4.8%) | 34.6% | 2.0% | {"EXTERNAL_STALE": 411, "AGREES_WITH_KALSHI": 224, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 6,139 | 616 (10.0%) | 35.2% | 2.1% | {"EXTERNAL_STALE": 386, "AGREES_WITH_KALSHI": 217, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 21,200 | 4960 (23.4%) | 19.0% | 0.9% | {"EXTERNAL_STALE": 2860, "ALL_AGREE": 1084, "AGREES_WITH_KALSHI": 941, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 28, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 10,452 | 10.6 | 7.7 | 18.9 | 14.3 | 21.8 | 16.4 | 10.3 | 14.41 | 48.6% | 26.7% |
| 4-10x | 7,212 | 10.9 | 8.7 | 18.1 | 14.8 | 21.5 | 14.7 | 11.4 | 14.1 | 47.5% | 26.1% |
| <2x | 27,069 | 14.5 | 9.6 | 19.9 | 15.9 | 17.6 | 13.4 | 9.2 | 11.72 | 40.2% | 22.6% |
| >=10x | 8,547 | 10.1 | 6.5 | 15.2 | 14.2 | 21.8 | 18.9 | 13.3 | 16.52 | 54.0% | 32.2% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 14,018 | 12.4 | 8.6 | 19.6 | 16.0 | 19.2 | 13.7 | 10.5 | 12.84 | 43.4% | 24.2% |
| 300-1000 | 11,613 | 11.5 | 8.7 | 17.8 | 15.1 | 20.6 | 16.5 | 10.0 | 13.94 | 47.0% | 26.4% |
| <300 | 16,904 | 8.1 | 5.9 | 15.2 | 14.4 | 22.8 | 20.0 | 13.6 | 17.47 | 56.5% | 33.7% |
| >=3000 | 10,745 | 20.9 | 12.8 | 24.0 | 15.4 | 14.0 | 7.4 | 5.5 | 7.92 | 26.9% | 12.9% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1649 | 0.5469 | 0.4077 | 0.4773 | +0.070 | -0.070 | 0.0034 ± 0.0038 |
| ratio 4-10x | 1127 | 0.5714 | 0.4273 | 0.4854 | +0.086 | -0.058 | 0.0099 ± 0.0048 |
| ratio <2x | 4023 | 0.5343 | 0.4114 | 0.431 | +0.103 | -0.020 | 0.015 ± 0.0022 |
| ratio >=10x | 1396 | 0.5579 | 0.3864 | 0.4305 | +0.127 | -0.044 | 0.0184 ± 0.0047 |
| thinner_sample 1000-3000 | 2255 | 0.5396 | 0.4126 | 0.4421 | +0.098 | -0.029 | 0.013 ± 0.0031 |
| thinner_sample 300-1000 | 1866 | 0.5588 | 0.4186 | 0.4684 | +0.090 | -0.050 | 0.0061 ± 0.0036 |
| thinner_sample <300 | 2683 | 0.552 | 0.3852 | 0.4406 | +0.112 | -0.055 | 0.0159 ± 0.0034 |
| thinner_sample >=3000 | 1391 | 0.5272 | 0.4335 | 0.4428 | +0.084 | -0.009 | 0.014 ± 0.0031 |
| data_status ADEQUATE | 2214 | 0.5313 | 0.4287 | 0.4386 | +0.093 | -0.010 | 0.0151 ± 0.0026 |
| data_status LIMITED | 1993 | 0.5463 | 0.4137 | 0.4616 | +0.085 | -0.048 | 0.0076 ± 0.0034 |
| data_status POOR | 3988 | 0.5539 | 0.3948 | 0.4458 | +0.108 | -0.051 | 0.0136 ± 0.0027 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1177 | 0.1968 | 0.1968 | -0.0000 ± 0.0004 | 0.5732 | 0.5733 | 0.502 | 0.4869 | 0.4919 | -0.099 ± 0.0137 | -0.0087 (8) |
| 3-5 | 761 | 0.2085 | 0.2081 | +0.0004 ± 0.0013 | 0.6029 | 0.6004 | 0.5019 | 0.462 | 0.4757 | -0.097 ± 0.017 | 0.01 (3) |
| 5-10 | 1767 | 0.2025 | 0.2009 | +0.0016 ± 0.0016 | 0.5914 | 0.5853 | 0.5083 | 0.4344 | 0.459 | -0.090 ± 0.011 | -0.0143 (7) |
| 10-15 | 1425 | 0.2187 | 0.2094 | +0.0094 ± 0.003 | 0.6292 | 0.6023 | 0.5239 | 0.4005 | 0.4232 | -0.103 ± 0.0123 | -0.055 (6) |
| 15-25 | 1817 | 0.2258 | 0.2069 | +0.0189 ± 0.0042 | 0.6467 | 0.597 | 0.5704 | 0.376 | 0.4243 | -0.101 ± 0.0108 | -0.0045 (11) |
| 25-40 | 1035 | 0.2253 | 0.2035 | +0.0218 ± 0.0084 | 0.6408 | 0.5875 | 0.6432 | 0.3336 | 0.4522 | -0.066 ± 0.013 | -0.06 (2) |
| 40+ | 213 | 0.3055 | 0.1669 | +0.1386 ± 0.0254 | 0.8168 | 0.5024 | 0.724 | 0.2668 | 0.3521 | -0.087 ± 0.0245 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5954 | 0.1873 | 0.1882 | -0.0008 ± 0.0002 | 0.5512 | 0.5522 | 0.4913 | 0.476 | 0.5057 | -0.022 ± 0.0057 | -0.01 (28) |
| 3-5 | 4048 | 0.1991 | 0.1972 | +0.0019 ± 0.0006 | 0.5792 | 0.5726 | 0.4811 | 0.4413 | 0.437 | -0.058 ± 0.0071 | 0.005 (6) |
| 5-10 | 8866 | 0.2008 | 0.1966 | +0.0042 ± 0.0007 | 0.5874 | 0.5738 | 0.4819 | 0.4081 | 0.4168 | -0.049 ± 0.0048 | -0.0114 (22) |
| 10-15 | 7220 | 0.2017 | 0.1859 | +0.0158 ± 0.0013 | 0.5898 | 0.5455 | 0.4842 | 0.3603 | 0.3587 | -0.063 ± 0.0051 | -0.0379 (19) |
| 15-25 | 9315 | 0.2063 | 0.1669 | +0.0394 ± 0.0017 | 0.6044 | 0.4962 | 0.4977 | 0.3022 | 0.3002 | -0.067 ± 0.0042 | -0.0043 (51) |
| 25-40 | 7281 | 0.2227 | 0.1234 | +0.0993 ± 0.0026 | 0.6394 | 0.3808 | 0.5233 | 0.2092 | 0.2121 | -0.059 ± 0.004 | -0.0733 (3) |
| 40+ | 5005 | 0.3793 | 0.0442 | +0.3352 ± 0.0034 | 0.9886 | 0.1709 | 0.6277 | 0.1019 | 0.0577 | -0.076 ± 0.0028 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 943 | 0.2023 | 0.2027 | -0.0003 ± 0.0005 | 0.5849 | 0.5859 | 0.5092 | 0.4942 | 0.5186 | -0.095 ± 0.0157 | -0.0117 (6) |
| 3-5 | 687 | 0.2127 | 0.2099 | +0.0028 ± 0.0014 | 0.6091 | 0.6028 | 0.519 | 0.4794 | 0.4614 | -0.124 ± 0.0188 | 0.01 (3) |
| 5-10 | 1525 | 0.2044 | 0.2028 | +0.0016 ± 0.0017 | 0.5943 | 0.5901 | 0.5377 | 0.4632 | 0.4905 | -0.084 ± 0.0119 | -0.01 (4) |
| 10-15 | 1321 | 0.2155 | 0.2077 | +0.0077 ± 0.0031 | 0.6238 | 0.6012 | 0.5568 | 0.4324 | 0.4663 | -0.102 ± 0.0131 | -0.04 (5) |
| 15-25 | 1911 | 0.2326 | 0.2115 | +0.0211 ± 0.0041 | 0.6617 | 0.607 | 0.5831 | 0.3874 | 0.4333 | -0.098 ± 0.0108 | -0.0183 (12) |
| 25-40 | 1326 | 0.266 | 0.2 | +0.0660 ± 0.0077 | 0.742 | 0.5806 | 0.6584 | 0.3447 | 0.3982 | -0.108 ± 0.0123 | -0.008 (5) |
| 40+ | 482 | 0.3745 | 0.1593 | +0.2152 ± 0.0182 | 1.0169 | 0.4833 | 0.7316 | 0.2427 | 0.2801 | -0.088 ± 0.0176 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5119 | 0.1906 | 0.1908 | -0.0002 ± 0.0002 | 0.5566 | 0.5569 | 0.5067 | 0.4915 | 0.5067 | -0.039 ± 0.0063 | -0.0154 (26) |
| 3-5 | 3550 | 0.1945 | 0.1936 | +0.0009 ± 0.0006 | 0.5664 | 0.5637 | 0.5113 | 0.4716 | 0.4789 | -0.044 ± 0.0076 | 0.01 (5) |
| 5-10 | 7927 | 0.1956 | 0.1923 | +0.0033 ± 0.0007 | 0.5753 | 0.563 | 0.5065 | 0.4322 | 0.4497 | -0.038 ± 0.005 | -0.0117 (6) |
| 10-15 | 6546 | 0.2023 | 0.1902 | +0.0122 ± 0.0013 | 0.5942 | 0.5567 | 0.5064 | 0.3825 | 0.3963 | -0.050 ± 0.0055 | -0.0189 (18) |
| 15-25 | 9393 | 0.2156 | 0.1792 | +0.0364 ± 0.0017 | 0.6279 | 0.5266 | 0.5227 | 0.3271 | 0.3345 | -0.059 ± 0.0044 | -0.014 (52) |
| 25-40 | 8443 | 0.2499 | 0.1378 | +0.1121 ± 0.0026 | 0.7061 | 0.4204 | 0.5591 | 0.2418 | 0.2273 | -0.076 ± 0.004 | -0.0095 (20) |
| 40+ | 6711 | 0.4016 | 0.0594 | +0.3422 ± 0.0034 | 1.0579 | 0.2134 | 0.6544 | 0.1191 | 0.0806 | -0.073 ± 0.0029 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1156 | 0.1968 | 0.1979 | -0.0011 ± 0.0005 | 0.5734 | 0.576 | 0.5008 | 0.4853 | 0.5216 | -0.060 ± 0.0137 | -0.0191 (11) |
| 3-5 | 831 | 0.2091 | 0.2077 | +0.0014 ± 0.0013 | 0.6052 | 0.6006 | 0.4965 | 0.457 | 0.4609 | -0.106 ± 0.0165 | 0.002 (5) |
| 5-10 | 1770 | 0.2028 | 0.1987 | +0.0041 ± 0.0016 | 0.5912 | 0.5796 | 0.5098 | 0.436 | 0.4441 | -0.104 ± 0.0109 | -0.01 (10) |
| 10-15 | 1470 | 0.2117 | 0.2021 | +0.0096 ± 0.0029 | 0.6138 | 0.5866 | 0.5371 | 0.4138 | 0.4388 | -0.103 ± 0.0118 | -0.0286 (7) |
| 15-25 | 1721 | 0.2314 | 0.212 | +0.0194 ± 0.0043 | 0.6602 | 0.6081 | 0.5799 | 0.386 | 0.4329 | -0.103 ± 0.0112 | -0.03 (1) |
| 25-40 | 1019 | 0.2172 | 0.2061 | +0.0112 ± 0.0084 | 0.6243 | 0.593 | 0.6511 | 0.3415 | 0.476 | -0.058 ± 0.0131 | -0.0267 (3) |
| 40+ | 228 | 0.3079 | 0.1807 | +0.1272 ± 0.0253 | 0.8306 | 0.5329 | 0.7369 | 0.2804 | 0.3816 | -0.074 ± 0.0259 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5790 | 0.1868 | 0.1873 | -0.0005 ± 0.0002 | 0.5497 | 0.5501 | 0.487 | 0.4716 | 0.4857 | -0.037 ± 0.0058 | -0.0189 (44) |
| 3-5 | 4154 | 0.2049 | 0.2033 | +0.0017 ± 0.0006 | 0.5951 | 0.5895 | 0.4805 | 0.441 | 0.4401 | -0.055 ± 0.0071 | -0.0073 (22) |
| 5-10 | 8980 | 0.1958 | 0.1904 | +0.0053 ± 0.0007 | 0.5749 | 0.5581 | 0.4847 | 0.4107 | 0.4111 | -0.056 ± 0.0046 | -0.0117 (42) |
| 10-15 | 7243 | 0.1952 | 0.1797 | +0.0155 ± 0.0012 | 0.5757 | 0.5321 | 0.4952 | 0.3719 | 0.3707 | -0.062 ± 0.005 | -0.0136 (14) |
| 15-25 | 9328 | 0.2112 | 0.172 | +0.0393 ± 0.0017 | 0.616 | 0.5074 | 0.5097 | 0.315 | 0.3125 | -0.068 ± 0.0043 | -0.0533 (3) |
| 25-40 | 7270 | 0.2166 | 0.1233 | +0.0933 ± 0.0026 | 0.6264 | 0.3797 | 0.5249 | 0.2095 | 0.2209 | -0.052 ± 0.004 | -0.02 (4) |
| 40+ | 4924 | 0.3877 | 0.0481 | +0.3396 ± 0.0035 | 1.0109 | 0.1809 | 0.6365 | 0.1073 | 0.0638 | -0.076 ± 0.003 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1627 | 0.196 | 0.1956 | +0.0004 ± 0.0004 | 0.5701 | 0.5689 | 0.5068 | 0.4917 | 0.4862 | -0.077 ± 0.0112 | -0.0221 (56) |
| 3-5 | 1153 | 0.1894 | 0.1895 | -0.0001 ± 0.001 | 0.557 | 0.5562 | 0.498 | 0.4581 | 0.477 | -0.053 ± 0.0131 | -0.0194 (34) |
| 5-10 | 2331 | 0.1989 | 0.1938 | +0.0051 ± 0.0014 | 0.587 | 0.5704 | 0.5086 | 0.4349 | 0.4376 | -0.077 ± 0.0093 | -0.005 (78) |
| 10-15 | 1614 | 0.215 | 0.2027 | +0.0123 ± 0.0028 | 0.6239 | 0.5889 | 0.5451 | 0.4223 | 0.4325 | -0.087 ± 0.0115 | 0.0015 (67) |
| 15-25 | 2102 | 0.2325 | 0.2081 | +0.0244 ± 0.0039 | 0.6634 | 0.5999 | 0.5923 | 0.3973 | 0.4334 | -0.089 ± 0.01 | -0.0214 (59) |
| 25-40 | 1220 | 0.2419 | 0.2118 | +0.0301 ± 0.008 | 0.6903 | 0.6069 | 0.6887 | 0.377 | 0.4852 | -0.082 ± 0.0125 | -0.0243 (28) |
| 40+ | 453 | 0.3292 | 0.1971 | +0.1320 ± 0.02 | 0.9395 | 0.576 | 0.8072 | 0.3304 | 0.4459 | -0.093 ± 0.0188 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5875 | 0.1768 | 0.1767 | +0.0001 ± 0.0002 | 0.5237 | 0.523 | 0.5088 | 0.4936 | 0.4989 | -0.043 ± 0.0055 | -0.0154 (103) |
| 3-5 | 4044 | 0.1945 | 0.1937 | +0.0008 ± 0.0006 | 0.5676 | 0.5656 | 0.5014 | 0.4617 | 0.4713 | -0.040 ± 0.007 | -0.0212 (73) |
| 5-10 | 8252 | 0.1969 | 0.1904 | +0.0065 ± 0.0007 | 0.5809 | 0.5613 | 0.5024 | 0.4288 | 0.4226 | -0.061 ± 0.0049 | -0.0084 (134) |
| 10-15 | 5672 | 0.2109 | 0.1947 | +0.0162 ± 0.0015 | 0.6137 | 0.5704 | 0.5378 | 0.4149 | 0.4092 | -0.070 ± 0.0059 | -0.0054 (112) |
| 15-25 | 6959 | 0.2317 | 0.1995 | +0.0322 ± 0.0021 | 0.6663 | 0.5783 | 0.5768 | 0.3814 | 0.397 | -0.067 ± 0.0054 | -0.024 (112) |
| 25-40 | 4472 | 0.2581 | 0.1904 | +0.0677 ± 0.0041 | 0.7295 | 0.5544 | 0.6405 | 0.3284 | 0.3792 | -0.063 ± 0.0064 | -0.0267 (58) |
| 40+ | 2014 | 0.37 | 0.1591 | +0.2108 ± 0.0092 | 1.039 | 0.4745 | 0.7406 | 0.241 | 0.29 | -0.059 ± 0.0085 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 8195 | 1.023 ± 0.031 | 1.084 | 0.1678 | 0.171 | 0.2158 | 0.2032 |
| gen2 | 8195 | 0.82 ± 0.028 | 1.062 | 0.1739 | 0.1713 | 0.2332 | 0.2032 |
| gen1_elo | 8195 | 1.006 ± 0.03 | 1.074 | 0.1743 | 0.1712 | 0.2149 | 0.2033 |
| gen1_sr | 8195 | 1.005 ± 0.037 | 1.11 | 0.1334 | 0.1728 | 0.2293 | 0.2029 |
| gen1_ledger | 10500 | 0.866 ± 0.023 | 1.062 | 0.1904 | 0.1772 | 0.2172 | 0.2001 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 37,785)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 9,142 | 24.2% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 8,877 | 23.5% |
| BOOK_QUALITY | execution | 6,359 | 16.8% |
| POOR_DATA | data | 4,307 | 11.4% |
| LIMITED_DATA | data | 2,272 | 6.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 2,216 | 5.9% |
| IDENTITY_AMBIGUOUS | mapping | 1,544 | 4.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,429 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 1,060 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 578 | 1.5% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 24.2%, coverage 23.5%, data 17.4%, execution 16.8%, market_freshness/coverage 8.7%, mapping 4.1%, model_calibration_or_unknown 3.8%, model_calibration 1.5%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 95.1%, LOW_DATA_QUALITY 72.2%, THIN_PLAYER_HISTORY 60.2%, STALE_PLAYER_DATA 52.1%, STALE_KALSHI_QUOTE 48.3%, MODEL_INTERNAL_DISAGREEMENT 41.7%, ASYMMETRIC_SAMPLE_SIZE 33.2%, WIDE_SPREAD 23.3%, MODEL_HIGH_UNCERTAINTY 18.7%, PLAYER_IDENTITY_RISK 15.0%, LEVEL_TRANSFER_RISK 9.3%, LOW_DISPLAYED_LIQUIDITY 8.7%, EVENT_MAPPING_RISK 7.0%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.1%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.8%, POST_SETTLEMENT_OBSERVATION 23.5%, POSSIBLE_IN_PLAY_QUOTE 6.3%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 20,225)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,150 | 35.4% |
| STALE_QUOTE | market_freshness | 4,063 | 20.1% |
| BOOK_QUALITY | execution | 3,283 | 16.2% |
| POOR_DATA | data | 1,823 | 9.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,197 | 5.9% |
| IDENTITY_AMBIGUOUS | mapping | 854 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 697 | 3.5% |
| LIMITED_DATA | data | 671 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 347 | 1.7% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 139 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 35.4%, market_freshness 20.1%, execution 16.2%, data 12.3%, market_freshness/coverage 9.4%, mapping 4.2%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.2%, START_UNVERIFIABLE 97.3%, LOW_DATA_QUALITY 75.2%, THIN_PLAYER_HISTORY 62.3%, STALE_KALSHI_QUOTE 55.7%, STALE_PLAYER_DATA 45.3%, MODEL_INTERNAL_DISAGREEMENT 41.8%, ASYMMETRIC_SAMPLE_SIZE 34.4%, WIDE_SPREAD 22.5%, MODEL_HIGH_UNCERTAINTY 19.4%, PLAYER_IDENTITY_RISK 17.8%, LOW_DISPLAYED_LIQUIDITY 8.5%, EVENT_MAPPING_RISK 8.4%, LEVEL_TRANSFER_RISK 8.1%, MODEL_CALIBRATION_OUTLIER 4.6%, EXTERNAL_MARKET_REJECTION 1.7%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 38.2%, POST_SETTLEMENT_OBSERVATION 35.4%, POSSIBLE_IN_PLAY_QUOTE 6.5%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 16269, "IDENTITY_AMBIGUOUS": 3956}; ticker orientation: {"VERIFIED": 20225}.

Checks: discipline:AMBIGUOUS 1301, discipline:PASS 18924, identity_confidence:AMBIGUOUS 3603, identity_confidence:PASS 16622, level_mapping:NA 1313, level_mapping:PASS 18912, market_pair:AMBIGUOUS 518, market_pair:NA 428, market_pair:PASS 19279, model_complement:NA 390, model_complement:PASS 19835, namesake:AMBIGUOUS 6, namesake:PASS 20219, physical_match_id:NA 6687, physical_match_id:PASS 13538, player_ids:PASS 20225, same_pair_other_event:PASS 20225, ticker_orientation:PASS 20225

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,621 | 3.7% | 3.1% | 1.2% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 24, "market_freshness/coverage": 22} | 5.47 | 0.222 / 0.2181 (869) | 25.7% | 2.4% | 3.2% | 3.0% |
| CHALLENGER | 13,416 | 16.6% | 6.0% | 11.0% | {"coverage": 1367, "market_freshness": 275, "market_freshness/coverage": 243, "data": 164, "model_calibration_or_unknown": 81, "execution": 41, "model_calibration": 40, "mapping": 17, "possible_market_error": 1} | 7.33 | 0.2216 / 0.2113 (3122) | 41.7% | 13.6% | 4.0% | 22.9% |
| DOUBLES | 2,808 | 46.3% | 46.4% | 6.4% | {"execution": 722, "mapping": 390, "market_freshness": 106, "market_freshness/coverage": 76, "coverage": 7} | 23.2 | 0.2984 / 0.2316 (708) | 8.3% | 0.0% | 100.0% | 6.5% |
| ITF_MEN | 27,081 | 25.3% | 17.6% | 33.9% | {"coverage": 2423, "market_freshness": 1435, "execution": 1047, "data": 1014, "market_freshness/coverage": 699, "mapping": 231, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.74 | 0.2179 / 0.1979 (5743) | 42.4% | 69.9% | 14.4% | 21.8% |
| ITF_WOMEN | 33,911 | 26.5% | 18.6% | 44.5% | {"coverage": 3274, "market_freshness": 1986, "execution": 1390, "data": 1215, "market_freshness/coverage": 797, "mapping": 210, "model_calibration_or_unknown": 98, "model_calibration": 23} | 12.44 | 0.2034 / 0.1938 (6625) | 43.0% | 57.3% | 10.1% | 22.1% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,935 | 5.9% | 5.0% | 1.4% | {"market_freshness": 111, "model_calibration_or_unknown": 52, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.66 | 0.2311 / 0.2208 (816) | 30.3% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.5% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 523 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 17.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 1025 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFMATCH-26NOV12VALRAT-RAT` | ITF_MEN | gen1_ledger | 92% / 4% | +88 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 10 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1333.0, ratio 3.64); no external reference |
| 6 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 7 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 8 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 9 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 10 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 769 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 11 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 628 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 12 | `KXITFMATCH-26NOV10KOUPOR-POR` | ITF_MEN | fair_v1 | 87% / 2% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.1h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 493 min (STALE); data POOR (grade D, thinner serve sample 1554.0, ratio 1.02); no external reference |
| 13 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 14 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 899 min (STALE); no external reference |
| 17 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 18 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 19 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 20 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 22 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 23 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 24 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 25 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 26 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 27 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 454 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 28 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 29 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 30 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 31 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 32 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 33 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 34 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 35 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 36 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 37 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 38 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 39 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 40 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 41 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 42 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 43 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 44 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 45 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 46 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 47 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 48 | `KXITFWMATCH-26NOV11CORROJ-ROJ` | ITF_WOMEN | fair_v1 | 87% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 434 min (STALE); data POOR (grade D, thinner serve sample 531.0, ratio 1.04); no external reference |
| 49 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 50 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9734, "by_level_share_of_ge_25pp": {"ATP": 0.0121, "CHALLENGER": 0.1102, "DOUBLES": 0.0643, "ITF_MEN": 0.3392, "ITF_WOMEN": 0.4446, "OTHER": 0.0006, "WTA": 0.0144, "WTA125": 0.0145}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5571, "share_primary_cause_market_settled_or_in_play": 0.4472, "share_primary_cause_stale_quote_only": 0.2009}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 20225, "identity_ambiguous_share": 0.1956, "ticker_orientation": {"VERIFIED": 20225}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 13538, "with_external": 648, "coverage": 0.0479, "external_status": {"EXTERNAL_STALE": 411, "AGREES_WITH_KALSHI": 224, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 411, "MODEL_LONE_OUTLIER": 224, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3457, "share_external_supports_model": 0.0201}, "pregame_clean_ge_25pp": {"n": 6139, "with_external": 616, "coverage": 0.1003, "external_status": {"EXTERNAL_STALE": 386, "AGREES_WITH_KALSHI": 217, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 386, "MODEL_LONE_OUTLIER": 217, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3523, "share_external_supports_model": 0.0211}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 483.5, "median_sample_ratio": 2.45, "median_min_matches": 18.0, "median_max_days_since_last": 246.0, "share_severe_asymmetry": 0.2066, "data_status": {"POOR": 11515, "LIMITED": 5083, "ADEQUATE": 3627}, "comparison_lt_10pp": {"median_thinner_serve_points": 1668.0, "median_sample_ratio": 1.71, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1649, "model_minus_observed": 0.0696, "kalshi_minus_observed": -0.0696, "brier_diff_model_minus_kalshi": 0.0034}, "4-10x": {"n": 1127, "model_minus_observed": 0.0861, "kalshi_minus_observed": -0.0581, "brier_diff_model_minus_kalshi": 0.0099}, "<2x": {"n": 4023, "model_minus_observed": 0.1033, "kalshi_minus_observed": -0.0196, "brier_diff_model_minus_kalshi": 0.015}, ">=10x": {"n": 1396, "model_minus_observed": 0.1273, "kalshi_minus_observed": -0.0441, "brier_diff_model_minus_kalshi": 0.0184}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 8195, "model": {"intercept": -0.561, "slope": 0.82, "slope_se": 0.028}, "kalshi_mid_same_rows": {"intercept": 0.168, "slope": 1.062, "slope_se": 0.031}, "mean_extremity_model": 0.1739, "mean_extremity_kalshi": 0.1713, "model_brier": 0.2332, "kalshi_brier": 0.2032, "brier_diff_model_minus_kalshi": 0.03, "brier_diff_se": 0.0021, "model_logloss": 0.6637, "kalshi_logloss": 0.5886}, "fair_v1": {"n": 8195, "model": {"intercept": -0.469, "slope": 1.023, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.215, "slope": 1.084, "slope_se": 0.031}, "mean_extremity_model": 0.1678, "mean_extremity_kalshi": 0.171, "model_brier": 0.2158, "kalshi_brier": 0.2032, "brier_diff_model_minus_kalshi": 0.0126, "brier_diff_se": 0.0017, "model_logloss": 0.6208, "kalshi_logloss": 0.5887}, "gen1_elo": {"n": 8195, "model": {"intercept": -0.458, "slope": 1.006, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.217, "slope": 1.074, "slope_se": 0.031}, "mean_extremity_model": 0.1743, "mean_extremity_kalshi": 0.1712, "model_brier": 0.2149, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.0116, "brier_diff_se": 0.0017, "model_logloss": 0.6194, "kalshi_logloss": 0.5888}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2541, "share_ge_15": 0.4503, "median_abs_gap": 13.22, "n": 53280}, "gen1_elo": {"share_ge_25": 0.2518, "share_ge_15": 0.4457, "median_abs_gap": 13.01, "n": 53280}, "gen1_sr": {"share_ge_25": 0.3166, "share_ge_15": 0.5254, "median_abs_gap": 16.0, "n": 53280}, "gen2": {"share_ge_25": 0.3166, "share_ge_15": 0.5138, "median_abs_gap": 15.55, "n": 53280}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1515, "share_ge_15": 0.3551, "median_abs_gap": 10.72, "n": 40504}, "gen1_elo": {"share_ge_25": 0.15, "share_ge_15": 0.3492, "median_abs_gap": 10.51, "n": 40504}, "gen1_sr": {"share_ge_25": 0.2147, "share_ge_15": 0.4398, "median_abs_gap": 13.0, "n": 40507}, "gen2": {"share_ge_25": 0.2299, "share_ge_15": 0.4392, "median_abs_gap": 12.84, "n": 40508}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.47, "share_ge_25_all": 0.037, "share_ge_25_pregame_clean": 0.031}, "WTA": {"median_abs_gap_pregame_clean": 7.66, "share_ge_25_all": 0.0592, "share_ge_25_pregame_clean": 0.0502}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.234, "share_within_10pp_all": 0.4353, "share_within_10pp_pregame_clean": 0.4903, "corr_model_vs_mid_pregame_clean": 0.8501}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1177, "model_brier": 0.1968, "kalshi_brier": 0.1968, "brier_diff_model_minus_kalshi": -0.0}, "10-15": {"n_settled": 1425, "model_brier": 0.2187, "kalshi_brier": 0.2094, "brier_diff_model_minus_kalshi": 0.0094}, "15-25": {"n_settled": 1817, "model_brier": 0.2258, "kalshi_brier": 0.2069, "brier_diff_model_minus_kalshi": 0.0189}, "25-40": {"n_settled": 1035, "model_brier": 0.2253, "kalshi_brier": 0.2035, "brier_diff_model_minus_kalshi": 0.0218}, "3-5": {"n_settled": 761, "model_brier": 0.2085, "kalshi_brier": 0.2081, "brier_diff_model_minus_kalshi": 0.0004}, "40+": {"n_settled": 213, "model_brier": 0.3055, "kalshi_brier": 0.1669, "brier_diff_model_minus_kalshi": 0.1386}, "5-10": {"n_settled": 1767, "model_brier": 0.2025, "kalshi_brier": 0.2009, "brier_diff_model_minus_kalshi": 0.0016}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.561, "slope": 0.82, "slope_se": 0.028}, "kalshi_slope": {"intercept": 0.168, "slope": 1.062, "slope_se": 0.031}, "n": 8195}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.5, "slope": 0.866, "slope_se": 0.023}, "kalshi_slope": {"intercept": 0.15, "slope": 1.062, "slope_se": 0.027}, "n": 10500}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 708, "model_brier": 0.2984, "kalshi_brier": 0.2316, "brier_diff_model_minus_kalshi": 0.0667, "brier_diff_se": 0.011, "corr_model_outcome": 0.1094, "corr_kalshi_outcome": 0.2825}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
