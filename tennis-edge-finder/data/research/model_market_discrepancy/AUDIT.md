# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-26T15:31Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 56,432): 0-3 14.0%, 3-5 9.6%, 5-10 19.9%, 10-15 15.4%, 15-25 19.2%, 25-40 13.9%, 40+ 8.1%; median gap 11.96 pp.
* **Where the extremes live**: 96.8% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.1%, Challenger 11.8%, doubles 7.0%). Main tour: ATP 4.4% and WTA 5.5% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 12,402): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.8%, STALE_QUOTE 18.9%, BOOK_QUALITY 18.9%, POOR_DATA 8.6%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.4%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.8%, market_freshness 18.9%, execution 18.9%, data 12.1%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 51.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.6% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 12,402 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.4% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 474.0 points vs 1774.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.035, Gen-2 0.832, Gen-1 ledger 0.863 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 597 model 0.2217 vs Kalshi 0.2093; n 116 model 0.2743 vs Kalshi 0.202.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 248,938 model-market comparisons (401,802 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 83,563 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-26T15:16:00.828044+00:00'], shadow board 64,990 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-26T15:16:05.103184+00:00'], Model 4 32,392 rows, 20,914 settled tickers, 7,420 tickers with an external scan.
* By model: {"gen1_ledger": 57276, "gen1_elo": 32681, "fair_v1": 32681, "gen2": 32681, "gen1_sr": 32681, "model4_fundamental": 30491, "model4_conditioned": 30447}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 56,432 | 14.0 | 9.6 | 19.9 | 15.4 | 19.2 | 13.9 | 8.1 | 11.96 | 41.2% | 22.0% |
| MW fair_v1 | 32,681 | 12.9 | 8.7 | 18.6 | 15.5 | 19.7 | 14.9 | 9.7 | 13.05 | 44.3% | 24.6% |
| MW gen1_elo | 32,681 | 12.8 | 8.6 | 19.2 | 15.3 | 19.9 | 14.8 | 9.5 | 12.95 | 44.2% | 24.3% |
| MW gen1_ledger | 23,751 | 15.5 | 10.8 | 21.6 | 15.1 | 18.5 | 12.6 | 5.8 | 10.5 | 36.9% | 18.4% |
| MW gen1_sr | 32,681 | 10.2 | 7.1 | 17.0 | 13.7 | 20.7 | 18.6 | 12.7 | 15.87 | 52.0% | 31.3% |
| MW gen2 | 32,681 | 11.1 | 7.4 | 16.4 | 13.9 | 19.4 | 17.9 | 13.9 | 15.5 | 51.1% | 31.7% |
| all families model4_conditioned | 30,447 | 21.9 | 18.4 | 34.5 | 17.6 | 4.8 | 1.8 | 1.1 | 6.06 | 7.7% | 2.9% |
| all families model4_fundamental | 30,491 | 16.7 | 13.1 | 34.1 | 20.7 | 10.4 | 3.7 | 1.4 | 7.83 | 15.4% | 5.0% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.5%, >=15pp 41.2%, >=20pp 30.6%, >=25pp 22.0%, >=30pp 15.8%, >=40pp 8.1%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.34pp; >=10pp 44.9%, >=25pp 17.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,054 | 27.1 | 15.0 | 26.6 | 14.7 | 11.7 | 4.3 | 0.7 | 6.06 | 16.6% | 4.9% |
| CHALLENGER | 5,187 | 15.9 | 10.0 | 20.2 | 15.6 | 15.7 | 12.1 | 10.5 | 11.02 | 38.3% | 22.6% |
| ITF_MEN | 8,694 | 10.0 | 7.2 | 16.7 | 14.6 | 21.5 | 17.6 | 12.4 | 15.53 | 51.5% | 29.9% |
| ITF_WOMEN | 12,737 | 9.5 | 6.9 | 15.9 | 15.1 | 22.4 | 18.3 | 11.8 | 15.78 | 52.5% | 30.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,172 | 16.9 | 13.9 | 25.3 | 20.4 | 16.9 | 6.1 | 0.6 | 8.36 | 23.5% | 6.7% |
| WTA125 | 831 | 14.2 | 7.6 | 22.1 | 21.8 | 19.7 | 12.5 | 2.0 | 11.13 | 34.3% | 14.6% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,054 | 24.5 | 15.1 | 25.7 | 17.4 | 12.2 | 4.3 | 0.8 | 6.5 | 17.3% | 5.1% |
| CHALLENGER | 5,187 | 15.1 | 8.9 | 18.1 | 14.5 | 18.2 | 14.0 | 11.3 | 12.67 | 43.4% | 25.3% |
| ITF_MEN | 8,694 | 8.1 | 5.8 | 14.3 | 12.9 | 19.6 | 21.3 | 17.9 | 18.84 | 58.8% | 39.2% |
| ITF_WOMEN | 12,737 | 8.1 | 5.6 | 13.8 | 12.9 | 20.7 | 21.2 | 17.7 | 19.28 | 59.7% | 38.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,172 | 14.3 | 10.6 | 22.6 | 16.0 | 22.4 | 13.0 | 1.1 | 10.77 | 36.6% | 14.2% |
| WTA125 | 831 | 7.6 | 6.5 | 16.1 | 18.6 | 24.3 | 17.8 | 9.0 | 15.49 | 51.1% | 26.8% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,054 | 23.0 | 12.3 | 24.5 | 16.2 | 16.1 | 6.5 | 1.3 | 7.58 | 23.9% | 7.8% |
| CHALLENGER | 5,187 | 14.3 | 9.2 | 21.1 | 15.8 | 16.2 | 12.7 | 10.7 | 11.42 | 39.5% | 23.4% |
| ITF_MEN | 8,694 | 9.6 | 7.3 | 16.7 | 13.8 | 22.1 | 17.9 | 12.6 | 16.01 | 52.6% | 30.5% |
| ITF_WOMEN | 12,737 | 9.3 | 6.6 | 16.3 | 15.9 | 22.7 | 18.2 | 11.0 | 15.59 | 51.9% | 29.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,172 | 23.9 | 16.8 | 31.1 | 15.2 | 9.5 | 2.6 | 1.0 | 6.05 | 13.1% | 3.6% |
| WTA125 | 831 | 22.6 | 11.9 | 26.1 | 16.6 | 16.5 | 5.9 | 0.4 | 8.01 | 22.7% | 6.3% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,823 | 24.9 | 19.4 | 30.0 | 12.9 | 9.3 | 3.2 | 0.3 | 5.67 | 12.8% | 3.5% |
| CHALLENGER | 3,608 | 21.4 | 14.2 | 26.7 | 15.0 | 14.6 | 6.5 | 1.7 | 7.4 | 22.8% | 8.1% |
| DOUBLES | 1,820 | 5.2 | 4.5 | 12.2 | 10.2 | 20.3 | 25.7 | 21.9 | 23.99 | 67.9% | 47.6% |
| ITF_MEN | 6,445 | 13.4 | 9.1 | 19.9 | 16.1 | 21.5 | 13.4 | 6.5 | 12.23 | 41.5% | 20.0% |
| ITF_WOMEN | 7,761 | 12.7 | 8.9 | 19.4 | 15.3 | 21.6 | 16.1 | 6.0 | 12.76 | 43.7% | 22.1% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,284 | 23.1 | 15.7 | 30.3 | 17.9 | 9.6 | 3.1 | 0.3 | 6.81 | 13.0% | 3.4% |
| WTA125 | 861 | 21.2 | 13.5 | 21.7 | 18.6 | 14.5 | 8.5 | 2.0 | 8.37 | 25.0% | 10.4% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,974 | 27.3 | 15.3 | 27.0 | 14.6 | 11.5 | 3.9 | 0.4 | 5.93 | 15.8% | 4.3% |
| CHALLENGER | 3,678 | 20.6 | 12.5 | 24.9 | 18.0 | 15.7 | 6.7 | 1.7 | 8.34 | 24.1% | 8.3% |
| ITF_MEN | 6,355 | 12.1 | 8.7 | 20.1 | 16.5 | 22.7 | 14.3 | 5.4 | 12.68 | 42.5% | 19.8% |
| ITF_WOMEN | 9,568 | 11.3 | 8.2 | 18.1 | 17.1 | 24.3 | 15.5 | 5.5 | 13.57 | 45.3% | 21.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,111 | 17.1 | 13.7 | 25.3 | 20.6 | 16.8 | 5.8 | 0.6 | 8.32 | 23.2% | 6.4% |
| WTA125 | 805 | 14.5 | 7.5 | 21.7 | 22.1 | 20.2 | 12.2 | 1.7 | 11.13 | 34.2% | 13.9% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,974 | 24.7 | 15.4 | 25.9 | 17.4 | 12.1 | 4.0 | 0.5 | 6.4 | 16.6% | 4.5% |
| CHALLENGER | 3,678 | 19.1 | 11.2 | 22.3 | 17.3 | 18.5 | 9.7 | 1.9 | 9.32 | 30.0% | 11.6% |
| ITF_MEN | 6,356 | 9.6 | 7.0 | 16.7 | 15.0 | 21.5 | 19.4 | 10.8 | 15.55 | 51.7% | 30.2% |
| ITF_WOMEN | 9,569 | 9.1 | 6.4 | 15.2 | 14.3 | 22.7 | 20.8 | 11.4 | 16.91 | 54.9% | 32.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,111 | 14.3 | 10.6 | 22.6 | 16.0 | 22.4 | 12.8 | 1.2 | 10.78 | 36.5% | 14.0% |
| WTA125 | 805 | 7.5 | 6.7 | 16.1 | 19.0 | 24.2 | 18.1 | 8.3 | 15.19 | 50.7% | 26.5% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,771 | 25.0 | 19.7 | 30.0 | 13.1 | 9.0 | 3.0 | 0.2 | 5.62 | 12.2% | 3.2% |
| CHALLENGER | 3,171 | 22.7 | 15.2 | 28.0 | 15.1 | 14.0 | 4.5 | 0.5 | 6.91 | 19.0% | 5.0% |
| DOUBLES | 1,700 | 5.2 | 4.6 | 12.5 | 10.3 | 20.2 | 25.6 | 21.7 | 23.88 | 67.5% | 47.3% |
| ITF_MEN | 5,416 | 14.6 | 9.7 | 21.6 | 16.9 | 21.4 | 11.8 | 4.1 | 11.32 | 37.3% | 15.9% |
| ITF_WOMEN | 6,493 | 13.6 | 9.5 | 20.6 | 16.1 | 21.8 | 14.9 | 3.5 | 11.78 | 40.2% | 18.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,231 | 23.6 | 16.1 | 30.3 | 17.9 | 9.6 | 2.4 | 0.1 | 6.69 | 12.1% | 2.5% |
| WTA125 | 749 | 23.0 | 14.7 | 23.0 | 19.8 | 13.1 | 6.0 | 0.5 | 7.74 | 19.6% | 6.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,820 | 5.2 | 4.5 | 12.2 | 10.2 | 20.3 | 25.7 | 21.9 | 23.99 | 67.9% | 47.6% |
| singles | 21,931 | 16.4 | 11.3 | 22.4 | 15.6 | 18.3 | 11.5 | 4.5 | 9.96 | 34.3% | 16.0% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,148 | 12.8 | 9.2 | 19.6 | 15.9 | 19.0 | 14.1 | 9.5 | 12.61 | 42.6% | 23.6% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 20,574 | 13.4 | 8.9 | 18.5 | 15.2 | 19.7 | 14.8 | 9.4 | 12.98 | 44.0% | 24.3% |
| UNKNOWN | 4,710 | 10.9 | 7.4 | 17.0 | 16.7 | 20.4 | 16.2 | 11.3 | 14.11 | 48.0% | 27.5% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,484 | 19.6 | 12.3 | 21.9 | 16.4 | 14.7 | 9.1 | 6.0 | 8.86 | 29.8% | 15.1% |
| B | 4,028 | 12.3 | 8.7 | 19.5 | 16.4 | 19.7 | 12.7 | 10.7 | 12.64 | 43.1% | 23.5% |
| C | 4,521 | 11.8 | 9.1 | 19.5 | 15.6 | 19.3 | 14.5 | 10.3 | 12.99 | 44.0% | 24.7% |
| D | 4,969 | 12.1 | 7.8 | 17.5 | 15.3 | 21.7 | 15.6 | 9.9 | 13.98 | 47.2% | 25.5% |
| F | 9,679 | 7.5 | 5.5 | 15.0 | 14.4 | 23.8 | 21.2 | 12.6 | 17.79 | 57.5% | 33.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,805 | 23.5 | 16.1 | 28.8 | 15.1 | 11.2 | 4.0 | 1.3 | 6.57 | 16.6% | 5.3% |
| B | 3,198 | 16.3 | 10.3 | 23.2 | 16.4 | 19.9 | 10.4 | 3.6 | 10.04 | 33.9% | 14.0% |
| C | 4,653 | 10.9 | 7.3 | 18.7 | 14.4 | 21.1 | 16.5 | 11.1 | 14.32 | 48.7% | 27.6% |
| D | 3,247 | 14.3 | 9.8 | 20.2 | 15.1 | 20.9 | 13.9 | 5.8 | 11.85 | 40.6% | 19.7% |
| F | 5,848 | 10.1 | 8.3 | 15.7 | 15.1 | 22.8 | 20.1 | 8.0 | 15.41 | 50.8% | 28.1% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 10,783 | 17.8 | 11.1 | 21.2 | 16.1 | 15.3 | 10.0 | 8.5 | 9.98 | 33.8% | 18.4% |
| LIMITED | 6,906 | 13.5 | 10.2 | 20.2 | 16.2 | 19.4 | 13.2 | 7.4 | 11.77 | 40.0% | 20.6% |
| POOR | 14,992 | 9.1 | 6.4 | 15.9 | 14.8 | 23.0 | 19.1 | 11.7 | 16.26 | 53.8% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,890 | 24.8 | 18.6 | 33.3 | 14.4 | 6.2 | 2.4 | 0.3 | 5.69 | 8.9% | 2.8% |
| GAME_SPREAD | 5,442 | 22.4 | 15.4 | 33.3 | 16.7 | 9.1 | 2.7 | 0.4 | 6.7 | 12.2% | 3.0% |
| MATCH_WINNER | 23,751 | 15.5 | 10.8 | 21.6 | 15.1 | 18.5 | 12.6 | 5.8 | 10.5 | 36.9% | 18.4% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 12,349 | 28.0 | 16.4 | 31.0 | 12.6 | 9.4 | 2.3 | 0.3 | 5.68 | 12.1% | 2.6% |
| TOTAL_GAMES | 8,820 | 9.0 | 10.2 | 36.5 | 27.2 | 10.5 | 3.9 | 2.8 | 9.33 | 17.2% | 6.7% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 10,885 | 24.5 | 31.1 | 32.8 | 6.7 | 3.9 | 0.8 | 0.2 | 4.66 | 4.9% | 1.0% |
| GAME_SPREAD | 7,136 | 46.4 | 16.5 | 26.0 | 7.7 | 1.9 | 1.1 | 0.5 | 3.37 | 3.4% | 1.6% |
| TOTAL_GAMES | 12,426 | 5.5 | 8.2 | 40.9 | 32.8 | 7.3 | 3.1 | 2.2 | 9.5 | 12.6% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 10,896 | 23.6 | 16.9 | 35.2 | 14.2 | 7.2 | 2.6 | 0.4 | 6.05 | 10.2% | 2.9% |
| GAME_SPREAD | 7,139 | 19.5 | 13.2 | 28.2 | 21.2 | 12.7 | 4.3 | 1.0 | 7.93 | 17.9% | 5.2% |
| TOTAL_GAMES | 12,456 | 9.0 | 9.8 | 36.5 | 26.2 | 11.8 | 4.3 | 2.4 | 9.37 | 18.5% | 6.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 32,681 | 44.3% | 24.6% | 13.05 | 35.9% | 15.5% | 10.85 |
| gen1_elo | 32,681 | 44.2% | 24.3% | 12.95 | 35.7% | 15.5% | 10.69 |
| gen1_sr | 32,681 | 52.0% | 31.3% | 15.87 | 44.3% | 22.1% | 13.0 |
| gen2 | 32,681 | 51.1% | 31.7% | 15.5 | 44.4% | 23.8% | 13.02 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 16,374 | 15.6 | 10.6 | 21.4 | 17.3 | 20.1 | 11.8 | 3.3 | 10.68 | 35.2% | 15.1% |
| STALE | 16,307 | 10.2 | 6.9 | 15.7 | 13.8 | 19.3 | 17.9 | 16.2 | 16.51 | 53.4% | 34.1% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 17,219 | 16.4 | 11.3 | 22.4 | 15.3 | 17.8 | 12.0 | 4.9 | 9.99 | 34.6% | 16.9% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 56,432 | 17219 | 19846 | 19367 | 24.1 | 131.5 | 1400.4 |
| ge_15pp | 23,232 | 5967 | 7054 | 10211 | 26.3 | 433.2 | 1380.4 |
| ge_25pp | 12,402 | 2911 | 3066 | 6425 | 31.6 | 574.8 | 1380.4 |
| lt_10pp | 24,528 | 8620 | 9410 | 6498 | 22.4 | 47.5 | 1341.5 |

Current slate `SL-20261026T153140Z-dc3b1c42`: 542 priced rows, quote age at build {'median': 16.1, 'max': 16.1}, freshness {'AGING': 542}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 28 | 0.0 | 0.0 | 21.4 | 10.7 | 39.3 | 28.6 | 0.0 | 20.48 | 67.9% | 28.6% |
| EXTERNAL_LONE_OUTLIER | 18 | 77.8 | 22.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,167 | 19.5 | 11.3 | 24.9 | 18.9 | 17.8 | 7.0 | 0.7 | 8.75 | 25.4% | 7.6% |
| KALSHI_LONE_OUTLIER | 21 | 4.8 | 4.8 | 76.2 | 4.8 | 4.8 | 4.8 | 0.0 | 6.11 | 9.5% | 4.8% |
| MARKETS_AGREE | 647 | 65.2 | 34.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.21 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,391 | 0.0 | 2.6 | 35.1 | 26.7 | 24.9 | 10.1 | 0.7 | 12.02 | 35.6% | 10.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 32,681 | 5272 (16.1%) | 26.4% | 0.9% | {"EXTERNAL_STALE": 3167, "AGREES_WITH_KALSHI": 1391, "ALL_AGREE": 647, "SUPPORTS_MODEL_DIRECTION": 27, "AGREES_WITH_MODEL": 21, "EXTERNAL_OUTLIER": 18, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 14,466 | 1321 (9.1%) | 37.5% | 1.6% | {"EXTERNAL_STALE": 805, "AGREES_WITH_KALSHI": 495, "SUPPORTS_MODEL_DIRECTION": 19, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 8,029 | 399 (5.0%) | 37.3% | 2.3% | {"EXTERNAL_STALE": 241, "AGREES_WITH_KALSHI": 149, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,946 | 376 (9.5%) | 37.8% | 2.4% | {"EXTERNAL_STALE": 225, "AGREES_WITH_KALSHI": 142, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 13,139 | 2978 (22.7%) | 17.6% | 0.8% | {"EXTERNAL_STALE": 1765, "ALL_AGREE": 647, "AGREES_WITH_KALSHI": 524, "EXTERNAL_OUTLIER": 18, "AGREES_WITH_MODEL": 18, "SUPPORTS_MODEL_DIRECTION": 5, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 6,259 | 10.3 | 7.6 | 19.4 | 14.5 | 22.4 | 15.9 | 9.8 | 14.09 | 48.1% | 25.7% |
| 4-10x | 4,216 | 11.1 | 8.4 | 18.7 | 15.4 | 22.1 | 14.6 | 9.7 | 13.76 | 46.5% | 24.3% |
| <2x | 16,718 | 15.1 | 10.1 | 19.3 | 16.4 | 17.4 | 12.9 | 8.8 | 11.58 | 39.1% | 21.7% |
| >=10x | 5,488 | 10.6 | 6.2 | 15.1 | 14.2 | 21.9 | 19.8 | 12.3 | 16.51 | 53.9% | 32.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 8,322 | 12.7 | 8.6 | 19.3 | 16.2 | 19.0 | 13.7 | 10.5 | 12.82 | 43.2% | 24.2% |
| 300-1000 | 6,847 | 11.8 | 8.8 | 17.4 | 15.3 | 20.8 | 16.1 | 9.9 | 13.79 | 46.7% | 26.0% |
| <300 | 10,607 | 8.4 | 5.7 | 15.3 | 14.6 | 23.3 | 20.2 | 12.4 | 17.05 | 55.9% | 32.6% |
| >=3000 | 6,905 | 21.1 | 13.5 | 23.7 | 16.4 | 13.8 | 6.9 | 4.5 | 7.71 | 25.2% | 11.3% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 921 | 0.5518 | 0.4136 | 0.5049 | +0.047 | -0.091 | -0.0036 ± 0.0051 |
| ratio 4-10x | 620 | 0.5895 | 0.4442 | 0.5048 | +0.085 | -0.061 | 0.0085 ± 0.0064 |
| ratio <2x | 2271 | 0.5392 | 0.4161 | 0.4491 | +0.090 | -0.033 | 0.0112 ± 0.003 |
| ratio >=10x | 831 | 0.5709 | 0.3958 | 0.4609 | +0.110 | -0.065 | 0.0085 ± 0.0063 |
| thinner_sample 1000-3000 | 1260 | 0.5426 | 0.4158 | 0.4532 | +0.089 | -0.037 | 0.0088 ± 0.004 |
| thinner_sample 300-1000 | 1038 | 0.5683 | 0.4249 | 0.4933 | +0.075 | -0.068 | 0.0008 ± 0.005 |
| thinner_sample <300 | 1568 | 0.5628 | 0.3966 | 0.4688 | +0.094 | -0.072 | 0.0085 ± 0.0045 |
| thinner_sample >=3000 | 777 | 0.5361 | 0.442 | 0.4672 | +0.069 | -0.025 | 0.0121 ± 0.0041 |
| data_status ADEQUATE | 1341 | 0.538 | 0.4339 | 0.4526 | +0.085 | -0.019 | 0.0115 ± 0.0034 |
| data_status LIMITED | 1069 | 0.5517 | 0.4183 | 0.4883 | +0.063 | -0.070 | 0.0023 ± 0.0046 |
| data_status POOR | 2233 | 0.5649 | 0.4036 | 0.4711 | +0.094 | -0.068 | 0.0074 ± 0.0037 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 676 | 0.2016 | 0.2024 | -0.0009 ± 0.0006 | 0.5842 | 0.5861 | 0.5023 | 0.4875 | 0.5222 | -0.073 ± 0.0182 | -0.01 (5) |
| 3-5 | 425 | 0.2049 | 0.2042 | +0.0007 ± 0.0018 | 0.5928 | 0.5899 | 0.5049 | 0.4649 | 0.4753 | -0.106 ± 0.0226 | 0.02 (1) |
| 5-10 | 963 | 0.2022 | 0.2027 | -0.0005 ± 0.0022 | 0.5909 | 0.5892 | 0.5145 | 0.4406 | 0.4756 | -0.088 ± 0.015 | -0.0167 (6) |
| 10-15 | 811 | 0.2163 | 0.2076 | +0.0086 ± 0.004 | 0.6234 | 0.5978 | 0.5329 | 0.4088 | 0.4353 | -0.105 ± 0.016 | -0.048 (5) |
| 15-25 | 1055 | 0.2252 | 0.2135 | +0.0118 ± 0.0056 | 0.6465 | 0.6105 | 0.5781 | 0.3822 | 0.4502 | -0.095 ± 0.0142 | -0.0033 (9) |
| 25-40 | 597 | 0.2217 | 0.2093 | +0.0124 ± 0.0111 | 0.6327 | 0.6015 | 0.6584 | 0.3484 | 0.4807 | -0.073 ± 0.0171 | -0.01 (1) |
| 40+ | 116 | 0.2743 | 0.202 | +0.0723 ± 0.036 | 0.7526 | 0.5904 | 0.7587 | 0.3114 | 0.4569 | -0.070 ± 0.0354 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3490 | 0.1849 | 0.1858 | -0.0009 ± 0.0003 | 0.5455 | 0.5465 | 0.4914 | 0.4764 | 0.508 | -0.024 ± 0.0074 | -0.0129 (17) |
| 3-5 | 2320 | 0.2005 | 0.1989 | +0.0016 ± 0.0007 | 0.5821 | 0.5758 | 0.4867 | 0.4467 | 0.4461 | -0.058 ± 0.0094 | 0.0 (2) |
| 5-10 | 4994 | 0.1993 | 0.196 | +0.0034 ± 0.0009 | 0.5839 | 0.5718 | 0.4843 | 0.4104 | 0.4235 | -0.049 ± 0.0063 | -0.0119 (21) |
| 10-15 | 4255 | 0.1984 | 0.1807 | +0.0176 ± 0.0016 | 0.5825 | 0.5328 | 0.4891 | 0.3646 | 0.3561 | -0.073 ± 0.0065 | -0.0281 (16) |
| 15-25 | 5392 | 0.2082 | 0.1691 | +0.0392 ± 0.0022 | 0.61 | 0.4998 | 0.5036 | 0.307 | 0.3069 | -0.073 ± 0.0056 | -0.0025 (44) |
| 25-40 | 4197 | 0.2226 | 0.1285 | +0.0941 ± 0.0035 | 0.6394 | 0.3932 | 0.5312 | 0.2178 | 0.228 | -0.060 ± 0.0054 | -0.01 (1) |
| 40+ | 2684 | 0.379 | 0.0451 | +0.3340 ± 0.0046 | 0.9871 | 0.1735 | 0.6317 | 0.1062 | 0.0637 | -0.078 ± 0.0038 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 533 | 0.2086 | 0.2093 | -0.0007 ± 0.0007 | 0.5995 | 0.6012 | 0.5077 | 0.4926 | 0.5178 | -0.105 ± 0.0214 | -0.01 (3) |
| 3-5 | 384 | 0.2272 | 0.2243 | +0.0028 ± 0.0019 | 0.6408 | 0.635 | 0.5135 | 0.4737 | 0.4531 | -0.133 ± 0.0258 | 0.02 (1) |
| 5-10 | 832 | 0.2073 | 0.207 | +0.0004 ± 0.0024 | 0.6011 | 0.5998 | 0.5468 | 0.472 | 0.5108 | -0.083 ± 0.0163 | -0.01 (4) |
| 10-15 | 768 | 0.2152 | 0.2091 | +0.0061 ± 0.0041 | 0.6193 | 0.6037 | 0.5651 | 0.4409 | 0.4805 | -0.105 ± 0.0172 | -0.04 (5) |
| 15-25 | 1083 | 0.2296 | 0.2116 | +0.0180 ± 0.0055 | 0.6522 | 0.6058 | 0.5885 | 0.3929 | 0.4488 | -0.099 ± 0.0143 | -0.0133 (9) |
| 25-40 | 761 | 0.2647 | 0.1981 | +0.0666 ± 0.0101 | 0.7406 | 0.5773 | 0.6559 | 0.341 | 0.3955 | -0.120 ± 0.0159 | -0.0075 (4) |
| 40+ | 282 | 0.3529 | 0.1747 | +0.1782 ± 0.0245 | 0.9703 | 0.5206 | 0.734 | 0.2505 | 0.3227 | -0.066 ± 0.0238 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2973 | 0.1949 | 0.1951 | -0.0002 ± 0.0003 | 0.5665 | 0.5669 | 0.5131 | 0.4981 | 0.5116 | -0.045 ± 0.0084 | -0.0133 (15) |
| 3-5 | 1993 | 0.2019 | 0.2004 | +0.0015 ± 0.0008 | 0.5828 | 0.5786 | 0.5144 | 0.4745 | 0.4747 | -0.054 ± 0.0103 | 0.02 (1) |
| 5-10 | 4428 | 0.1976 | 0.1951 | +0.0025 ± 0.001 | 0.5812 | 0.5698 | 0.5116 | 0.4376 | 0.4607 | -0.038 ± 0.0067 | -0.0117 (6) |
| 10-15 | 3827 | 0.201 | 0.1892 | +0.0118 ± 0.0018 | 0.5899 | 0.5517 | 0.5147 | 0.3908 | 0.4058 | -0.055 ± 0.0071 | -0.0189 (18) |
| 15-25 | 5343 | 0.2158 | 0.1787 | +0.0371 ± 0.0023 | 0.6268 | 0.5249 | 0.5251 | 0.3293 | 0.3365 | -0.067 ± 0.0058 | -0.0086 (42) |
| 25-40 | 4905 | 0.2519 | 0.1369 | +0.1150 ± 0.0034 | 0.7088 | 0.4202 | 0.5589 | 0.242 | 0.2216 | -0.087 ± 0.0053 | -0.0044 (18) |
| 40+ | 3863 | 0.3926 | 0.0605 | +0.3322 ± 0.0045 | 1.0331 | 0.2159 | 0.6505 | 0.1187 | 0.0857 | -0.070 ± 0.0039 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 650 | 0.1995 | 0.2018 | -0.0023 ± 0.0006 | 0.5799 | 0.5855 | 0.5023 | 0.4871 | 0.5523 | -0.031 ± 0.0183 | -0.0137 (8) |
| 3-5 | 461 | 0.2022 | 0.2009 | +0.0014 ± 0.0017 | 0.5877 | 0.583 | 0.5075 | 0.4678 | 0.4729 | -0.117 ± 0.0218 | 0.0067 (3) |
| 5-10 | 990 | 0.203 | 0.2002 | +0.0027 ± 0.0021 | 0.5922 | 0.5826 | 0.5113 | 0.4373 | 0.4545 | -0.101 ± 0.0146 | -0.0071 (7) |
| 10-15 | 801 | 0.2082 | 0.205 | +0.0032 ± 0.004 | 0.6052 | 0.5923 | 0.5417 | 0.4182 | 0.4682 | -0.089 ± 0.0159 | -0.0317 (6) |
| 15-25 | 995 | 0.2319 | 0.2149 | +0.0169 ± 0.0057 | 0.6627 | 0.6135 | 0.5885 | 0.394 | 0.4472 | -0.108 ± 0.0147 | -0.03 (1) |
| 25-40 | 622 | 0.2142 | 0.2171 | -0.0029 ± 0.0109 | 0.6177 | 0.6195 | 0.6684 | 0.3575 | 0.5145 | -0.056 ± 0.0168 | 0.015 (2) |
| 40+ | 124 | 0.2877 | 0.2134 | +0.0743 ± 0.036 | 0.7955 | 0.6147 | 0.767 | 0.3181 | 0.4677 | -0.064 ± 0.038 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3419 | 0.1859 | 0.1867 | -0.0007 ± 0.0003 | 0.547 | 0.5482 | 0.4895 | 0.4743 | 0.4946 | -0.032 ± 0.0075 | -0.0163 (35) |
| 3-5 | 2332 | 0.1974 | 0.1954 | +0.0021 ± 0.0007 | 0.5782 | 0.5715 | 0.4895 | 0.4499 | 0.4447 | -0.065 ± 0.0093 | -0.0094 (18) |
| 5-10 | 5097 | 0.196 | 0.1906 | +0.0054 ± 0.0009 | 0.5761 | 0.5577 | 0.4846 | 0.4106 | 0.4116 | -0.059 ± 0.0061 | -0.01 (31) |
| 10-15 | 4127 | 0.192 | 0.177 | +0.0150 ± 0.0016 | 0.5678 | 0.5229 | 0.5008 | 0.3774 | 0.378 | -0.065 ± 0.0065 | -0.015 (12) |
| 15-25 | 5512 | 0.2107 | 0.1714 | +0.0393 ± 0.0022 | 0.6159 | 0.5056 | 0.5132 | 0.318 | 0.3157 | -0.074 ± 0.0056 | -0.03 (2) |
| 25-40 | 4224 | 0.2194 | 0.1318 | +0.0876 ± 0.0035 | 0.6331 | 0.4005 | 0.5357 | 0.2199 | 0.2408 | -0.051 ± 0.0054 | 0.01 (3) |
| 40+ | 2621 | 0.3932 | 0.0506 | +0.3426 ± 0.005 | 1.0274 | 0.1878 | 0.6444 | 0.1134 | 0.0702 | -0.080 ± 0.0042 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1036 | 0.1967 | 0.1968 | -0.0001 ± 0.0005 | 0.5731 | 0.5729 | 0.5017 | 0.4867 | 0.4913 | -0.064 ± 0.014 | -0.0224 (49) |
| 3-5 | 718 | 0.1927 | 0.192 | +0.0007 ± 0.0013 | 0.563 | 0.5601 | 0.4914 | 0.4516 | 0.461 | -0.061 ± 0.0167 | -0.0194 (34) |
| 5-10 | 1509 | 0.202 | 0.1963 | +0.0057 ± 0.0017 | 0.5932 | 0.5752 | 0.4973 | 0.4239 | 0.4228 | -0.074 ± 0.0116 | -0.005 (78) |
| 10-15 | 1020 | 0.2107 | 0.1989 | +0.0118 ± 0.0035 | 0.6121 | 0.58 | 0.5268 | 0.4038 | 0.4157 | -0.073 ± 0.0143 | 0.0014 (64) |
| 15-25 | 1350 | 0.2314 | 0.2108 | +0.0205 ± 0.0049 | 0.6605 | 0.6066 | 0.5793 | 0.3846 | 0.4311 | -0.075 ± 0.0125 | -0.0214 (59) |
| 25-40 | 822 | 0.2441 | 0.2091 | +0.0351 ± 0.0098 | 0.6965 | 0.5999 | 0.6776 | 0.3651 | 0.4647 | -0.084 ± 0.0148 | -0.0219 (26) |
| 40+ | 271 | 0.3456 | 0.2025 | +0.1432 ± 0.0268 | 0.9989 | 0.5923 | 0.8097 | 0.3291 | 0.4391 | -0.092 ± 0.0247 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3435 | 0.1822 | 0.1824 | -0.0002 ± 0.0003 | 0.5371 | 0.5366 | 0.5027 | 0.4874 | 0.4967 | -0.041 ± 0.0073 | -0.0157 (88) |
| 3-5 | 2399 | 0.1962 | 0.1943 | +0.0019 ± 0.0007 | 0.5717 | 0.5671 | 0.4989 | 0.4592 | 0.4552 | -0.055 ± 0.0091 | -0.0209 (69) |
| 5-10 | 4826 | 0.1962 | 0.1879 | +0.0082 ± 0.0009 | 0.5781 | 0.5534 | 0.4935 | 0.4199 | 0.4039 | -0.072 ± 0.0063 | -0.0082 (132) |
| 10-15 | 3382 | 0.2078 | 0.1919 | +0.0158 ± 0.0019 | 0.6062 | 0.5625 | 0.5301 | 0.4071 | 0.4036 | -0.066 ± 0.0076 | -0.0053 (105) |
| 15-25 | 4186 | 0.2304 | 0.2002 | +0.0302 ± 0.0027 | 0.6644 | 0.5798 | 0.5693 | 0.3736 | 0.3956 | -0.067 ± 0.0069 | -0.0253 (107) |
| 25-40 | 2846 | 0.2582 | 0.1861 | +0.0721 ± 0.0051 | 0.7326 | 0.5423 | 0.6339 | 0.3206 | 0.3644 | -0.076 ± 0.0079 | -0.0229 (51) |
| 40+ | 1237 | 0.3739 | 0.1468 | +0.2271 ± 0.0114 | 1.0591 | 0.4419 | 0.7325 | 0.2292 | 0.2684 | -0.069 ± 0.0102 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4643 | 1.035 ± 0.041 | 1.111 | 0.1683 | 0.1631 | 0.2144 | 0.2069 |
| gen2 | 4643 | 0.832 ± 0.038 | 1.076 | 0.1685 | 0.1638 | 0.2339 | 0.2067 |
| gen1_elo | 4643 | 1.007 ± 0.04 | 1.11 | 0.1749 | 0.1633 | 0.2133 | 0.2071 |
| gen1_sr | 4643 | 1.017 ± 0.05 | 1.141 | 0.1294 | 0.1657 | 0.2303 | 0.2062 |
| gen1_ledger | 6726 | 0.863 ± 0.029 | 1.067 | 0.184 | 0.177 | 0.2183 | 0.201 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 23,232)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,219 | 22.5% |
| STALE_QUOTE | market_freshness | 5,081 | 21.9% |
| BOOK_QUALITY | execution | 4,464 | 19.2% |
| POOR_DATA | data | 2,593 | 11.2% |
| LIMITED_DATA | data | 1,436 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,252 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,098 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 992 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 681 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 415 | 1.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.5%, market_freshness 21.9%, execution 19.2%, data 17.3%, market_freshness/coverage 8.3%, model_calibration_or_unknown 4.7%, mapping 4.3%, model_calibration 1.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 93.9%, LOW_DATA_QUALITY 70.9%, THIN_PLAYER_HISTORY 59.7%, STALE_PLAYER_DATA 50.1%, STALE_KALSHI_QUOTE 44.0%, MODEL_INTERNAL_DISAGREEMENT 42.6%, ASYMMETRIC_SAMPLE_SIZE 33.4%, WIDE_SPREAD 25.3%, MODEL_HIGH_UNCERTAINTY 17.8%, PLAYER_IDENTITY_RISK 16.6%, LEVEL_TRANSFER_RISK 10.6%, EVENT_MAPPING_RISK 8.1%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 3.9%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.0%, POST_SETTLEMENT_OBSERVATION 22.5%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 12,402)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,187 | 33.8% |
| STALE_QUOTE | market_freshness | 2,348 | 18.9% |
| BOOK_QUALITY | execution | 2,341 | 18.9% |
| POOR_DATA | data | 1,071 | 8.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 668 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 549 | 4.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 432 | 3.5% |
| LIMITED_DATA | data | 430 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 277 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 98 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.8%, market_freshness 18.9%, execution 18.9%, data 12.1%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.8%, LOW_DATA_QUALITY 74.3%, THIN_PLAYER_HISTORY 61.8%, STALE_KALSHI_QUOTE 51.8%, STALE_PLAYER_DATA 44.7%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 34.5%, WIDE_SPREAD 24.8%, PLAYER_IDENTITY_RISK 20.1%, MODEL_HIGH_UNCERTAINTY 18.2%, EVENT_MAPPING_RISK 9.9%, LEVEL_TRANSFER_RISK 9.5%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 5.1%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.8%, POST_SETTLEMENT_OBSERVATION 33.8%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 9607, "IDENTITY_AMBIGUOUS": 2795}; ticker orientation: {"VERIFIED": 12402}.

Checks: discipline:AMBIGUOUS 866, discipline:PASS 11536, identity_confidence:AMBIGUOUS 2487, identity_confidence:PASS 9915, level_mapping:NA 878, level_mapping:PASS 11524, market_pair:AMBIGUOUS 466, market_pair:NA 303, market_pair:PASS 11633, model_complement:NA 270, model_complement:PASS 12132, namesake:AMBIGUOUS 6, namesake:PASS 12396, physical_match_id:NA 4373, physical_match_id:PASS 8029, player_ids:PASS 12402, same_pair_other_event:PASS 12402, ticker_orientation:PASS 12402

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,877 | 4.4% | 3.9% | 1.7% | {"market_freshness": 55, "model_calibration_or_unknown": 49, "data": 36, "execution": 24, "model_calibration": 21, "market_freshness/coverage": 15, "coverage": 13} | 5.87 | 0.2233 / 0.2202 (543) | 20.3% | 3.2% | 3.3% | 2.7% |
| CHALLENGER | 8,795 | 16.7% | 6.8% | 11.8% | {"coverage": 823, "market_freshness/coverage": 179, "market_freshness": 164, "data": 144, "model_calibration_or_unknown": 69, "execution": 36, "model_calibration": 35, "mapping": 16, "possible_market_error": 1} | 7.59 | 0.2182 / 0.2089 (2055) | 34.3% | 17.2% | 4.1% | 22.1% |
| DOUBLES | 1,820 | 47.6% | 47.3% | 7.0% | {"execution": 481, "mapping": 217, "market_freshness": 106, "market_freshness/coverage": 55, "coverage": 7} | 23.88 | 0.3088 / 0.2362 (441) | 12.9% | 0.0% | 100.0% | 6.6% |
| ITF_MEN | 15,139 | 25.7% | 18.0% | 31.4% | {"coverage": 1437, "execution": 742, "market_freshness": 674, "data": 519, "market_freshness/coverage": 338, "mapping": 177, "model_calibration_or_unknown": 2, "model_calibration": 2} | 11.99 | 0.2165 / 0.1987 (3355) | 37.5% | 70.3% | 19.7% | 22.2% |
| ITF_WOMEN | 20,498 | 27.1% | 20.0% | 44.8% | {"coverage": 1882, "market_freshness": 1231, "execution": 1007, "data": 757, "market_freshness/coverage": 463, "mapping": 133, "model_calibration_or_unknown": 69, "model_calibration": 11} | 12.88 | 0.2034 / 0.196 (3888) | 39.6% | 57.3% | 10.4% | 21.6% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,456 | 5.5% | 5.0% | 1.5% | {"market_freshness": 68, "model_calibration_or_unknown": 39, "execution": 26, "model_calibration": 16, "data": 16, "coverage": 12, "market_freshness/coverage": 11, "mapping": 1} | 7.67 | 0.2318 / 0.2259 (541) | 25.2% | 1.2% | 1.5% | 3.3% |
| WTA125 | 1,692 | 12.5% | 10.4% | 1.7% | {"market_freshness": 48, "model_calibration_or_unknown": 47, "market_freshness/coverage": 38, "data": 29, "execution": 20, "model_calibration": 13, "coverage": 12, "mapping": 4} | 9.52 | 0.217 / 0.2036 (504) | 24.4% | 11.5% | 6.3% | 8.2% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 17.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1037 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 15 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 16 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 17 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 18 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 19 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 20 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 21 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 22 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 23 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 24 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 25 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 26 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 27 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 28 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 29 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 30 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 31 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 32 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 463 min (STALE); no external reference |
| 33 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 34 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 35 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 36 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 37 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 39 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 22.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1345 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 41 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 42 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 43 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 44 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 46 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 47 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 48 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 49 | `KXWTADOUBLES-26OCT25DABSTEBUCFER-BUCFER` | DOUBLES | gen1_ledger | 93% / 16% | +77 | BOOK_QUALITY | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 874 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9676, "by_level_share_of_ge_25pp": {"ATP": 0.0172, "CHALLENGER": 0.1183, "DOUBLES": 0.0698, "ITF_MEN": 0.3137, "ITF_WOMEN": 0.4478, "OTHER": 0.001, "WTA": 0.0152, "WTA125": 0.017}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5181, "share_primary_cause_market_settled_or_in_play": 0.4263, "share_primary_cause_stale_quote_only": 0.1893}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 12402, "identity_ambiguous_share": 0.2254, "ticker_orientation": {"VERIFIED": 12402}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 8029, "with_external": 399, "coverage": 0.0497, "external_status": {"EXTERNAL_STALE": 241, "AGREES_WITH_KALSHI": 149, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 241, "MODEL_LONE_OUTLIER": 149, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3734, "share_external_supports_model": 0.0226}, "pregame_clean_ge_25pp": {"n": 3946, "with_external": 376, "coverage": 0.0953, "external_status": {"EXTERNAL_STALE": 225, "AGREES_WITH_KALSHI": 142, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 225, "MODEL_LONE_OUTLIER": 142, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3777, "share_external_supports_model": 0.0239}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 474.0, "median_sample_ratio": 2.44, "median_min_matches": 20.0, "median_max_days_since_last": 231.0, "share_severe_asymmetry": 0.2167, "data_status": {"POOR": 6920, "LIMITED": 3223, "ADEQUATE": 2259}, "comparison_lt_10pp": {"median_thinner_serve_points": 1774.0, "median_sample_ratio": 1.67, "median_min_matches": 98.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 921, "model_minus_observed": 0.0469, "kalshi_minus_observed": -0.0913, "brier_diff_model_minus_kalshi": -0.0036}, "4-10x": {"n": 620, "model_minus_observed": 0.0847, "kalshi_minus_observed": -0.0607, "brier_diff_model_minus_kalshi": 0.0085}, "<2x": {"n": 2271, "model_minus_observed": 0.0901, "kalshi_minus_observed": -0.033, "brier_diff_model_minus_kalshi": 0.0112}, ">=10x": {"n": 831, "model_minus_observed": 0.11, "kalshi_minus_observed": -0.0651, "brier_diff_model_minus_kalshi": 0.0085}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4643, "model": {"intercept": -0.532, "slope": 0.832, "slope_se": 0.038}, "kalshi_mid_same_rows": {"intercept": 0.209, "slope": 1.076, "slope_se": 0.042}, "mean_extremity_model": 0.1685, "mean_extremity_kalshi": 0.1638, "model_brier": 0.2339, "kalshi_brier": 0.2067, "brier_diff_model_minus_kalshi": 0.0272, "brier_diff_se": 0.0028, "model_logloss": 0.6644, "kalshi_logloss": 0.5964}, "fair_v1": {"n": 4643, "model": {"intercept": -0.412, "slope": 1.035, "slope_se": 0.041}, "kalshi_mid_same_rows": {"intercept": 0.29, "slope": 1.111, "slope_se": 0.043}, "mean_extremity_model": 0.1683, "mean_extremity_kalshi": 0.1631, "model_brier": 0.2144, "kalshi_brier": 0.2069, "brier_diff_model_minus_kalshi": 0.0074, "brier_diff_se": 0.0023, "model_logloss": 0.6178, "kalshi_logloss": 0.5968}, "gen1_elo": {"n": 4643, "model": {"intercept": -0.384, "slope": 1.007, "slope_se": 0.04}, "kalshi_mid_same_rows": {"intercept": 0.315, "slope": 1.11, "slope_se": 0.042}, "mean_extremity_model": 0.1749, "mean_extremity_kalshi": 0.1633, "model_brier": 0.2133, "kalshi_brier": 0.2071, "brier_diff_model_minus_kalshi": 0.0062, "brier_diff_se": 0.0023, "model_logloss": 0.6162, "kalshi_logloss": 0.5971}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2457, "share_ge_15": 0.4426, "median_abs_gap": 13.05, "n": 32681}, "gen1_elo": {"share_ge_25": 0.2433, "share_ge_15": 0.4418, "median_abs_gap": 12.95, "n": 32681}, "gen1_sr": {"share_ge_25": 0.3133, "share_ge_15": 0.5201, "median_abs_gap": 15.87, "n": 32681}, "gen2": {"share_ge_25": 0.3173, "share_ge_15": 0.5115, "median_abs_gap": 15.5, "n": 32681}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1547, "share_ge_15": 0.3592, "median_abs_gap": 10.85, "n": 25497}, "gen1_elo": {"share_ge_25": 0.1552, "share_ge_15": 0.3573, "median_abs_gap": 10.69, "n": 25494}, "gen1_sr": {"share_ge_25": 0.2213, "share_ge_15": 0.4427, "median_abs_gap": 13.0, "n": 25498}, "gen2": {"share_ge_25": 0.2381, "share_ge_15": 0.444, "median_abs_gap": 13.02, "n": 25499}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.87, "share_ge_25_all": 0.0437, "share_ge_25_pregame_clean": 0.039}, "WTA": {"median_abs_gap_pregame_clean": 7.67, "share_ge_25_all": 0.0547, "share_ge_25_pregame_clean": 0.0497}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.236, "share_within_10pp_all": 0.4346, "share_within_10pp_pregame_clean": 0.4863, "corr_model_vs_mid_pregame_clean": 0.843}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 676, "model_brier": 0.2016, "kalshi_brier": 0.2024, "brier_diff_model_minus_kalshi": -0.0009}, "10-15": {"n_settled": 811, "model_brier": 0.2163, "kalshi_brier": 0.2076, "brier_diff_model_minus_kalshi": 0.0086}, "15-25": {"n_settled": 1055, "model_brier": 0.2252, "kalshi_brier": 0.2135, "brier_diff_model_minus_kalshi": 0.0118}, "25-40": {"n_settled": 597, "model_brier": 0.2217, "kalshi_brier": 0.2093, "brier_diff_model_minus_kalshi": 0.0124}, "3-5": {"n_settled": 425, "model_brier": 0.2049, "kalshi_brier": 0.2042, "brier_diff_model_minus_kalshi": 0.0007}, "40+": {"n_settled": 116, "model_brier": 0.2743, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0723}, "5-10": {"n_settled": 963, "model_brier": 0.2022, "kalshi_brier": 0.2027, "brier_diff_model_minus_kalshi": -0.0005}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.532, "slope": 0.832, "slope_se": 0.038}, "kalshi_slope": {"intercept": 0.209, "slope": 1.076, "slope_se": 0.042}, "n": 4643}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.496, "slope": 0.863, "slope_se": 0.029}, "kalshi_slope": {"intercept": 0.163, "slope": 1.067, "slope_se": 0.034}, "n": 6726}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 441, "model_brier": 0.3088, "kalshi_brier": 0.2362, "brier_diff_model_minus_kalshi": 0.0726, "brier_diff_se": 0.0144, "corr_model_outcome": 0.0389, "corr_kalshi_outcome": 0.2525}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
