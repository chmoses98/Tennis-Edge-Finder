# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-13T20:53Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 92,315): 0-3 13.9%, 3-5 9.5%, 5-10 20.1%, 10-15 15.2%, 15-25 19.2%, 25-40 13.8%, 40+ 8.4%; median gap 11.95 pp.
* **Where the extremes live**: 97.4% of >=25 pp gaps are off the ATP/WTA main tour (ITF 78.4%, Challenger 11.1%, doubles 6.5%). Main tour: ATP 3.7% and WTA 5.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 20,456): MARKET_ALREADY_SETTLED_WHEN_PRICED 35.7%, STALE_QUOTE 19.9%, BOOK_QUALITY 16.1%, POOR_DATA 9.0%, POSSIBLY_IN_PLAY_QUOTE 5.9%, IDENTITY_AMBIGUOUS 4.3%, IN_PLAY_QUOTE 3.4%, LIMITED_DATA 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 1.7%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 35.7%, market_freshness 19.9%, execution 16.1%, data 12.3%, market_freshness/coverage 9.3%, mapping 4.3%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 55.9% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 45.0% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 20,456 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.7%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 27.0% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 490.0 points vs 1673.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.022, Gen-2 0.818, Gen-1 ledger 0.866 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 1043 model 0.2256 vs Kalshi 0.2037; n 214 model 0.307 vs Kalshi 0.1666.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 382,109 model-market comparisons (633,499 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 125,588 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-13T20:39:12.831621+00:00'], shadow board 107,040 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-13T20:39:15.921258+00:00'], Model 4 44,310 rows, 31,721 settled tickers, 11,944 tickers with an external scan.
* By model: {"gen1_ledger": 83839, "gen1_elo": 53789, "fair_v1": 53789, "gen2": 53789, "gen1_sr": 53789, "model4_fundamental": 41599, "model4_conditioned": 41515}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 92,315 | 13.9 | 9.5 | 20.1 | 15.2 | 19.2 | 13.8 | 8.4 | 11.95 | 41.3% | 22.2% |
| MW fair_v1 | 53,789 | 12.5 | 8.6 | 18.6 | 15.2 | 19.6 | 15.0 | 10.5 | 13.24 | 45.1% | 25.5% |
| MW gen1_elo | 53,789 | 12.3 | 8.7 | 19.1 | 15.2 | 19.4 | 15.0 | 10.3 | 13.03 | 44.7% | 25.3% |
| MW gen1_ledger | 38,526 | 15.8 | 10.8 | 22.1 | 15.2 | 18.6 | 11.9 | 5.5 | 10.29 | 36.1% | 17.5% |
| MW gen1_sr | 53,789 | 9.9 | 7.1 | 16.5 | 13.9 | 20.9 | 18.8 | 12.9 | 16.03 | 52.6% | 31.7% |
| MW gen2 | 53,789 | 10.8 | 7.5 | 16.6 | 13.7 | 19.7 | 17.7 | 14.0 | 15.57 | 51.4% | 31.7% |
| all families model4_conditioned | 41,515 | 22.2 | 17.9 | 34.6 | 16.9 | 5.0 | 2.2 | 1.2 | 6.06 | 8.4% | 3.4% |
| all families model4_fundamental | 41,599 | 17.3 | 13.6 | 34.0 | 19.9 | 9.9 | 3.8 | 1.5 | 7.6 | 15.2% | 5.3% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.5%, >=15pp 41.3%, >=20pp 30.6%, >=25pp 22.2%, >=30pp 16.1%, >=40pp 8.4%, >=50pp 3.9%
Executable gap (model outside the book, before fees): median 8.62pp; >=10pp 45.8%, >=25pp 17.7%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,135 | 27.9 | 16.0 | 28.0 | 13.2 | 10.7 | 3.5 | 0.6 | 5.77 | 14.8% | 4.1% |
| CHALLENGER | 8,442 | 16.3 | 9.6 | 20.6 | 15.2 | 15.7 | 11.4 | 11.3 | 10.94 | 38.3% | 22.7% |
| ITF_MEN | 15,964 | 9.6 | 7.3 | 17.0 | 14.9 | 21.0 | 17.1 | 13.0 | 15.46 | 51.1% | 30.1% |
| ITF_WOMEN | 20,800 | 9.3 | 7.0 | 16.1 | 14.6 | 22.2 | 18.6 | 12.1 | 16.05 | 53.0% | 30.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,115 | 16.6 | 13.2 | 24.9 | 20.7 | 16.8 | 6.7 | 1.1 | 8.65 | 24.6% | 7.8% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,135 | 26.3 | 15.7 | 26.4 | 15.7 | 11.3 | 3.9 | 0.8 | 6.09 | 15.9% | 4.7% |
| CHALLENGER | 8,442 | 14.4 | 9.1 | 19.0 | 13.7 | 18.4 | 13.7 | 11.7 | 12.55 | 43.7% | 25.4% |
| ITF_MEN | 15,964 | 8.2 | 6.2 | 15.2 | 13.8 | 20.3 | 19.9 | 16.4 | 17.85 | 56.6% | 36.3% |
| ITF_WOMEN | 20,800 | 7.8 | 5.8 | 14.1 | 12.7 | 20.7 | 21.2 | 17.8 | 19.23 | 59.7% | 39.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,115 | 14.1 | 10.3 | 21.5 | 16.3 | 22.6 | 12.8 | 2.5 | 11.28 | 37.8% | 15.2% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,135 | 23.5 | 14.2 | 25.6 | 15.4 | 14.3 | 5.9 | 1.1 | 7.02 | 21.3% | 7.0% |
| CHALLENGER | 8,442 | 15.2 | 9.5 | 20.7 | 15.5 | 16.0 | 11.9 | 11.1 | 11.18 | 39.0% | 23.0% |
| ITF_MEN | 15,964 | 9.3 | 7.2 | 17.2 | 14.3 | 21.4 | 17.3 | 13.3 | 15.76 | 51.9% | 30.6% |
| ITF_WOMEN | 20,800 | 9.2 | 6.8 | 16.2 | 15.5 | 22.1 | 18.7 | 11.5 | 15.85 | 52.2% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,115 | 22.4 | 17.2 | 31.9 | 15.2 | 9.1 | 3.3 | 1.0 | 6.12 | 13.4% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,504 | 28.1 | 19.6 | 29.1 | 12.1 | 8.1 | 2.5 | 0.4 | 5.24 | 11.0% | 3.0% |
| CHALLENGER | 5,108 | 23.3 | 14.7 | 27.6 | 14.6 | 12.9 | 5.4 | 1.5 | 6.94 | 19.8% | 6.9% |
| DOUBLES | 2,847 | 4.8 | 4.4 | 12.8 | 10.9 | 20.6 | 24.9 | 21.6 | 23.31 | 67.0% | 46.5% |
| ITF_MEN | 11,478 | 12.8 | 9.6 | 21.5 | 15.7 | 21.6 | 12.9 | 6.0 | 11.78 | 40.4% | 18.8% |
| ITF_WOMEN | 13,347 | 13.5 | 9.3 | 19.9 | 15.8 | 21.6 | 14.5 | 5.3 | 12.14 | 41.5% | 19.9% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,837 | 23.8 | 15.8 | 31.9 | 16.8 | 8.9 | 2.5 | 0.2 | 6.57 | 11.7% | 2.7% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,006 | 28.4 | 16.2 | 28.4 | 13.2 | 10.5 | 3.1 | 0.3 | 5.64 | 13.8% | 3.4% |
| CHALLENGER | 5,914 | 21.2 | 12.0 | 25.7 | 18.0 | 15.7 | 5.6 | 1.8 | 8.18 | 23.1% | 7.4% |
| ITF_MEN | 11,498 | 11.9 | 8.8 | 20.6 | 17.2 | 22.1 | 14.0 | 5.4 | 12.43 | 41.6% | 19.4% |
| ITF_WOMEN | 15,050 | 11.3 | 8.6 | 19.2 | 17.0 | 24.1 | 15.3 | 4.5 | 13.11 | 43.9% | 19.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,001 | 16.9 | 13.3 | 25.2 | 21.1 | 16.8 | 6.2 | 0.6 | 8.49 | 23.6% | 6.8% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,006 | 26.6 | 16.1 | 26.7 | 15.7 | 11.2 | 3.4 | 0.4 | 6.02 | 15.0% | 3.8% |
| CHALLENGER | 5,914 | 18.1 | 11.8 | 23.9 | 16.2 | 19.0 | 8.9 | 2.1 | 8.96 | 30.0% | 11.0% |
| ITF_MEN | 11,500 | 9.7 | 7.4 | 17.8 | 16.0 | 22.3 | 17.9 | 9.0 | 14.67 | 49.1% | 26.8% |
| ITF_WOMEN | 15,052 | 8.9 | 7.0 | 16.1 | 14.2 | 22.6 | 20.6 | 10.6 | 16.51 | 53.8% | 31.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,001 | 14.3 | 10.5 | 21.7 | 16.5 | 22.7 | 12.5 | 1.9 | 11.03 | 37.0% | 14.3% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,434 | 28.4 | 19.8 | 29.2 | 12.3 | 7.7 | 2.3 | 0.3 | 5.19 | 10.3% | 2.6% |
| CHALLENGER | 4,519 | 24.6 | 15.5 | 28.8 | 14.8 | 12.2 | 3.7 | 0.4 | 6.48 | 16.4% | 4.1% |
| DOUBLES | 2,666 | 4.7 | 4.5 | 13.1 | 10.9 | 20.4 | 24.8 | 21.7 | 23.23 | 66.9% | 46.5% |
| ITF_MEN | 9,915 | 13.6 | 10.1 | 22.9 | 16.3 | 21.7 | 11.4 | 4.1 | 10.94 | 37.2% | 15.5% |
| ITF_WOMEN | 11,492 | 14.1 | 9.8 | 21.0 | 16.4 | 21.8 | 13.4 | 3.5 | 11.37 | 38.7% | 17.0% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,774 | 24.1 | 16.2 | 32.0 | 16.7 | 8.9 | 2.0 | 0.1 | 6.43 | 10.9% | 2.0% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,847 | 4.8 | 4.4 | 12.8 | 10.9 | 20.6 | 24.9 | 21.6 | 23.31 | 67.0% | 46.5% |
| singles | 35,679 | 16.6 | 11.3 | 22.9 | 15.5 | 18.4 | 10.9 | 4.2 | 9.75 | 33.6% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 11,750 | 12.6 | 9.0 | 19.2 | 14.9 | 19.6 | 14.3 | 10.3 | 13.06 | 44.3% | 24.7% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 34,964 | 12.9 | 8.6 | 18.8 | 15.1 | 19.2 | 15.1 | 10.4 | 13.05 | 44.6% | 25.5% |
| UNKNOWN | 6,662 | 10.4 | 7.5 | 17.1 | 16.6 | 21.5 | 15.8 | 11.1 | 14.3 | 48.4% | 26.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 14,933 | 19.0 | 11.8 | 22.3 | 15.7 | 14.9 | 9.6 | 6.7 | 9.06 | 31.1% | 16.2% |
| B | 6,384 | 12.9 | 8.5 | 19.4 | 15.2 | 19.8 | 12.4 | 11.7 | 12.88 | 43.9% | 24.1% |
| C | 7,710 | 11.8 | 8.5 | 19.2 | 16.0 | 19.2 | 14.7 | 10.6 | 13.09 | 44.5% | 25.3% |
| D | 8,908 | 11.2 | 8.3 | 17.8 | 15.2 | 21.6 | 15.8 | 10.1 | 14.09 | 47.4% | 25.9% |
| F | 15,854 | 7.3 | 5.7 | 15.1 | 14.2 | 23.0 | 21.1 | 13.7 | 18.05 | 57.8% | 34.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 10,118 | 25.0 | 15.9 | 29.0 | 14.8 | 10.6 | 3.4 | 1.2 | 6.35 | 15.2% | 4.7% |
| B | 5,241 | 16.8 | 11.0 | 24.0 | 17.0 | 18.9 | 9.4 | 2.9 | 9.61 | 31.2% | 12.3% |
| C | 7,628 | 11.0 | 7.8 | 19.5 | 14.9 | 20.9 | 15.7 | 10.1 | 13.53 | 46.8% | 25.8% |
| D | 5,897 | 14.3 | 9.9 | 21.0 | 15.5 | 21.1 | 12.8 | 5.3 | 11.42 | 39.2% | 18.1% |
| F | 9,642 | 10.2 | 8.4 | 16.7 | 14.5 | 23.5 | 18.8 | 7.9 | 15.07 | 50.2% | 26.7% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 16,918 | 17.5 | 10.8 | 21.3 | 15.5 | 15.2 | 10.2 | 9.5 | 10.08 | 34.9% | 19.7% |
| LIMITED | 11,708 | 13.4 | 9.4 | 20.3 | 15.9 | 19.8 | 13.4 | 7.8 | 12.01 | 41.0% | 21.2% |
| POOR | 25,163 | 8.8 | 6.6 | 16.1 | 14.6 | 22.4 | 19.0 | 12.4 | 16.37 | 53.9% | 31.4% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,366 | 23.8 | 18.0 | 33.0 | 15.4 | 6.4 | 3.0 | 0.4 | 5.89 | 9.8% | 3.4% |
| GAME_SPREAD | 6,983 | 22.8 | 15.3 | 32.0 | 16.8 | 9.1 | 3.3 | 0.7 | 6.69 | 13.0% | 3.9% |
| MATCH_WINNER | 38,526 | 15.8 | 10.8 | 22.1 | 15.2 | 18.6 | 11.9 | 5.5 | 10.29 | 36.1% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 17,225 | 28.4 | 16.8 | 30.7 | 12.7 | 8.8 | 2.3 | 0.3 | 5.57 | 11.4% | 2.6% |
| TOTAL_GAMES | 11,715 | 9.7 | 10.8 | 36.5 | 25.6 | 10.4 | 4.2 | 2.8 | 9.12 | 17.4% | 7.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,764 | 24.5 | 28.8 | 33.3 | 8.1 | 3.9 | 1.2 | 0.3 | 4.79 | 5.4% | 1.5% |
| GAME_SPREAD | 9,599 | 46.6 | 15.8 | 25.2 | 7.4 | 2.4 | 1.9 | 0.6 | 3.33 | 4.9% | 2.5% |
| TOTAL_GAMES | 17,152 | 6.5 | 9.8 | 41.0 | 29.8 | 7.2 | 3.3 | 2.3 | 9.14 | 12.9% | 5.6% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,800 | 23.9 | 16.6 | 34.6 | 14.7 | 6.9 | 2.7 | 0.5 | 6.05 | 10.1% | 3.2% |
| GAME_SPREAD | 9,608 | 20.3 | 13.4 | 28.5 | 20.2 | 12.2 | 4.3 | 1.1 | 7.71 | 17.6% | 5.5% |
| TOTAL_GAMES | 17,191 | 10.1 | 11.0 | 36.5 | 24.3 | 11.3 | 4.4 | 2.6 | 9.01 | 18.2% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 53,789 | 45.1% | 25.5% | 13.24 | 35.5% | 15.1% | 10.71 |
| gen1_elo | 53,789 | 44.7% | 25.3% | 13.03 | 34.9% | 15.0% | 10.51 |
| gen1_sr | 53,789 | 52.6% | 31.7% | 16.03 | 43.9% | 21.4% | 12.98 |
| gen2 | 53,789 | 51.4% | 31.7% | 15.57 | 43.9% | 22.9% | 12.83 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,577 | 15.4 | 10.5 | 21.3 | 17.3 | 20.1 | 11.9 | 3.5 | 10.72 | 35.4% | 15.4% |
| STALE | 33,212 | 10.7 | 7.4 | 17.0 | 13.9 | 19.3 | 17.0 | 14.8 | 15.45 | 51.1% | 31.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 31,994 | 16.3 | 11.1 | 22.6 | 15.2 | 18.2 | 11.5 | 5.0 | 9.97 | 34.7% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 92,315 | 31994 | 24049 | 36272 | 25.3 | 155.4 | 1451.1 |
| ge_15pp | 38,154 | 11096 | 8582 | 18476 | 29.3 | 456.5 | 1451.1 |
| ge_25pp | 20,456 | 5270 | 3754 | 11432 | 35.0 | 599.9 | 1431.1 |
| lt_10pp | 40,153 | 16020 | 11364 | 12769 | 22.8 | 49.7 | 1421.7 |

Current slate `SL-20261113T205325Z-6b8fc3f4`: 162 priced rows, quote age at build {'median': 14.4, 'max': 14.5}, freshness {'AGING': 162}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 52 | 0.0 | 0.0 | 34.6 | 9.6 | 32.7 | 19.2 | 3.9 | 18.34 | 55.8% | 23.1% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 5,113 | 19.2 | 11.1 | 25.7 | 18.3 | 17.7 | 7.1 | 1.0 | 8.76 | 25.7% | 8.1% |
| KALSHI_LONE_OUTLIER | 32 | 6.2 | 6.2 | 75.0 | 6.2 | 3.1 | 3.1 | 0.0 | 6.16 | 6.2% | 3.1% |
| MARKETS_AGREE | 1,105 | 66.2 | 33.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,343 | 0.0 | 2.2 | 38.4 | 25.9 | 23.9 | 8.7 | 0.9 | 11.65 | 33.5% | 9.6% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 53,789 | 8674 (16.1%) | 27.0% | 0.9% | {"EXTERNAL_STALE": 5113, "AGREES_WITH_KALSHI": 2343, "ALL_AGREE": 1105, "SUPPORTS_MODEL_DIRECTION": 50, "AGREES_WITH_MODEL": 32, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 24,259 | 2131 (8.8%) | 36.8% | 1.5% | {"EXTERNAL_STALE": 1316, "AGREES_WITH_KALSHI": 784, "SUPPORTS_MODEL_DIRECTION": 29, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 13,724 | 649 (4.7%) | 34.5% | 2.0% | {"EXTERNAL_STALE": 412, "AGREES_WITH_KALSHI": 224, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 6,166 | 617 (10.0%) | 35.2% | 2.1% | {"EXTERNAL_STALE": 387, "AGREES_WITH_KALSHI": 217, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 21,364 | 4993 (23.4%) | 19.1% | 0.9% | {"EXTERNAL_STALE": 2862, "ALL_AGREE": 1105, "AGREES_WITH_KALSHI": 951, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 28, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 10,559 | 10.5 | 7.7 | 18.9 | 14.3 | 21.7 | 16.4 | 10.4 | 14.41 | 48.6% | 26.9% |
| 4-10x | 7,284 | 10.8 | 8.6 | 18.1 | 14.9 | 21.5 | 14.7 | 11.4 | 14.1 | 47.6% | 26.1% |
| <2x | 27,363 | 14.4 | 9.6 | 19.8 | 15.9 | 17.6 | 13.4 | 9.3 | 11.77 | 40.3% | 22.7% |
| >=10x | 8,583 | 10.2 | 6.4 | 15.2 | 14.2 | 21.8 | 18.9 | 13.3 | 16.53 | 54.0% | 32.2% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 14,222 | 12.2 | 8.5 | 19.6 | 16.1 | 19.2 | 13.7 | 10.7 | 12.89 | 43.6% | 24.4% |
| 300-1000 | 11,734 | 11.4 | 8.6 | 17.8 | 15.1 | 20.5 | 16.4 | 10.2 | 13.94 | 47.1% | 26.6% |
| <300 | 16,984 | 8.1 | 5.9 | 15.1 | 14.4 | 22.9 | 20.0 | 13.7 | 17.46 | 56.5% | 33.6% |
| >=3000 | 10,849 | 20.9 | 12.8 | 23.9 | 15.3 | 14.1 | 7.5 | 5.5 | 7.92 | 27.1% | 13.0% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1672 | 0.5471 | 0.4084 | 0.4767 | +0.070 | -0.068 | 0.0041 ± 0.0038 |
| ratio 4-10x | 1142 | 0.571 | 0.4269 | 0.4851 | +0.086 | -0.058 | 0.0095 ± 0.0047 |
| ratio <2x | 4072 | 0.5344 | 0.4115 | 0.431 | +0.103 | -0.019 | 0.0149 ± 0.0022 |
| ratio >=10x | 1402 | 0.5581 | 0.3868 | 0.4301 | +0.128 | -0.043 | 0.0185 ± 0.0047 |
| thinner_sample 1000-3000 | 2292 | 0.5396 | 0.4129 | 0.4424 | +0.097 | -0.030 | 0.0129 ± 0.003 |
| thinner_sample 300-1000 | 1891 | 0.5593 | 0.4191 | 0.468 | +0.091 | -0.049 | 0.0068 ± 0.0036 |
| thinner_sample <300 | 2700 | 0.5518 | 0.3852 | 0.4396 | +0.112 | -0.054 | 0.0157 ± 0.0034 |
| thinner_sample >=3000 | 1405 | 0.5274 | 0.4338 | 0.4434 | +0.084 | -0.010 | 0.0136 ± 0.003 |
| data_status ADEQUATE | 2236 | 0.5318 | 0.4295 | 0.4396 | +0.092 | -0.010 | 0.0148 ± 0.0026 |
| data_status LIMITED | 2028 | 0.5462 | 0.4134 | 0.461 | +0.085 | -0.048 | 0.0078 ± 0.0034 |
| data_status POOR | 4024 | 0.5538 | 0.395 | 0.4451 | +0.109 | -0.050 | 0.0137 ± 0.0027 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1189 | 0.196 | 0.196 | +0.0000 ± 0.0004 | 0.5715 | 0.5716 | 0.5027 | 0.4875 | 0.492 | -0.099 ± 0.0136 | -0.0087 (8) |
| 3-5 | 776 | 0.2084 | 0.2079 | +0.0006 ± 0.0013 | 0.6028 | 0.6002 | 0.5003 | 0.4605 | 0.4729 | -0.097 ± 0.0168 | 0.01 (3) |
| 5-10 | 1784 | 0.2022 | 0.2003 | +0.0019 ± 0.0016 | 0.5906 | 0.5841 | 0.5093 | 0.4353 | 0.4585 | -0.091 ± 0.0109 | -0.0143 (7) |
| 10-15 | 1443 | 0.2201 | 0.2104 | +0.0097 ± 0.003 | 0.6329 | 0.6046 | 0.5239 | 0.4006 | 0.422 | -0.103 ± 0.0123 | -0.055 (6) |
| 15-25 | 1839 | 0.2256 | 0.2074 | +0.0182 ± 0.0041 | 0.6462 | 0.5982 | 0.5707 | 0.3762 | 0.4263 | -0.098 ± 0.0107 | -0.0045 (11) |
| 25-40 | 1043 | 0.2256 | 0.2037 | +0.0219 ± 0.0084 | 0.6416 | 0.5879 | 0.6428 | 0.3333 | 0.4516 | -0.065 ± 0.013 | -0.06 (2) |
| 40+ | 214 | 0.307 | 0.1666 | +0.1404 ± 0.0253 | 0.8206 | 0.5019 | 0.7244 | 0.2671 | 0.3505 | -0.089 ± 0.0244 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 6001 | 0.187 | 0.1878 | -0.0008 ± 0.0002 | 0.5504 | 0.5513 | 0.492 | 0.4767 | 0.5057 | -0.023 ± 0.0057 | -0.01 (28) |
| 3-5 | 4088 | 0.1993 | 0.1975 | +0.0018 ± 0.0006 | 0.5798 | 0.5735 | 0.4805 | 0.4407 | 0.4379 | -0.056 ± 0.007 | 0.005 (6) |
| 5-10 | 8951 | 0.2003 | 0.196 | +0.0043 ± 0.0007 | 0.5861 | 0.5723 | 0.482 | 0.4082 | 0.4162 | -0.049 ± 0.0047 | -0.0114 (22) |
| 10-15 | 7311 | 0.2021 | 0.1859 | +0.0162 ± 0.0013 | 0.5912 | 0.5455 | 0.4839 | 0.36 | 0.3569 | -0.064 ± 0.0051 | -0.0379 (19) |
| 15-25 | 9410 | 0.2062 | 0.1671 | +0.0391 ± 0.0017 | 0.6041 | 0.4966 | 0.4976 | 0.3021 | 0.3007 | -0.067 ± 0.0042 | -0.0043 (51) |
| 25-40 | 7363 | 0.2225 | 0.1234 | +0.0991 ± 0.0026 | 0.639 | 0.3807 | 0.523 | 0.2087 | 0.212 | -0.059 ± 0.004 | -0.0733 (3) |
| 40+ | 5120 | 0.3795 | 0.0437 | +0.3357 ± 0.0033 | 0.9889 | 0.1702 | 0.6272 | 0.1016 | 0.0566 | -0.077 ± 0.0028 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 954 | 0.202 | 0.2023 | -0.0003 ± 0.0005 | 0.5841 | 0.5851 | 0.5085 | 0.4934 | 0.5178 | -0.094 ± 0.0155 | -0.0117 (6) |
| 3-5 | 697 | 0.2114 | 0.2085 | +0.0029 ± 0.0014 | 0.6063 | 0.6 | 0.5188 | 0.4792 | 0.4605 | -0.124 ± 0.0186 | 0.01 (3) |
| 5-10 | 1542 | 0.2044 | 0.2027 | +0.0016 ± 0.0017 | 0.594 | 0.59 | 0.5385 | 0.464 | 0.4916 | -0.083 ± 0.0118 | -0.01 (4) |
| 10-15 | 1338 | 0.2153 | 0.2073 | +0.0080 ± 0.0031 | 0.6231 | 0.6003 | 0.5573 | 0.4329 | 0.4656 | -0.102 ± 0.0129 | -0.04 (5) |
| 15-25 | 1936 | 0.2332 | 0.2124 | +0.0208 ± 0.0041 | 0.6643 | 0.6091 | 0.5841 | 0.3884 | 0.4349 | -0.097 ± 0.0107 | -0.0183 (12) |
| 25-40 | 1335 | 0.2663 | 0.2001 | +0.0662 ± 0.0077 | 0.7429 | 0.5807 | 0.6581 | 0.3444 | 0.3978 | -0.108 ± 0.0123 | -0.008 (5) |
| 40+ | 486 | 0.3749 | 0.1598 | +0.2151 ± 0.0182 | 1.0178 | 0.4849 | 0.7318 | 0.2426 | 0.2798 | -0.088 ± 0.0175 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5168 | 0.1899 | 0.1901 | -0.0002 ± 0.0002 | 0.555 | 0.5553 | 0.506 | 0.4909 | 0.5062 | -0.039 ± 0.0062 | -0.0154 (26) |
| 3-5 | 3591 | 0.1934 | 0.1924 | +0.0010 ± 0.0006 | 0.564 | 0.5611 | 0.5107 | 0.471 | 0.4776 | -0.044 ± 0.0075 | 0.01 (5) |
| 5-10 | 8000 | 0.1953 | 0.192 | +0.0033 ± 0.0007 | 0.5748 | 0.5624 | 0.5066 | 0.4323 | 0.4495 | -0.038 ± 0.005 | -0.0117 (6) |
| 10-15 | 6623 | 0.2016 | 0.1894 | +0.0122 ± 0.0013 | 0.5924 | 0.5548 | 0.5052 | 0.3813 | 0.395 | -0.049 ± 0.0054 | -0.0189 (18) |
| 15-25 | 9498 | 0.2164 | 0.1804 | +0.0360 ± 0.0017 | 0.6305 | 0.5293 | 0.5238 | 0.3282 | 0.3364 | -0.058 ± 0.0044 | -0.014 (52) |
| 25-40 | 8534 | 0.2497 | 0.1375 | +0.1122 ± 0.0026 | 0.7055 | 0.4196 | 0.5585 | 0.2411 | 0.2266 | -0.075 ± 0.004 | -0.0095 (20) |
| 40+ | 6830 | 0.4019 | 0.059 | +0.3429 ± 0.0034 | 1.059 | 0.2122 | 0.6542 | 0.1187 | 0.0796 | -0.074 ± 0.0029 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1167 | 0.1961 | 0.1972 | -0.0011 ± 0.0005 | 0.5719 | 0.5746 | 0.5019 | 0.4864 | 0.5227 | -0.060 ± 0.0136 | -0.0191 (11) |
| 3-5 | 841 | 0.209 | 0.2075 | +0.0016 ± 0.0013 | 0.6055 | 0.6003 | 0.4956 | 0.4561 | 0.4578 | -0.108 ± 0.0164 | 0.002 (5) |
| 5-10 | 1794 | 0.2032 | 0.1991 | +0.0041 ± 0.0016 | 0.592 | 0.5805 | 0.5097 | 0.4359 | 0.4443 | -0.103 ± 0.0108 | -0.01 (10) |
| 10-15 | 1488 | 0.2124 | 0.2029 | +0.0095 ± 0.0029 | 0.6157 | 0.5884 | 0.5371 | 0.4138 | 0.4388 | -0.103 ± 0.0118 | -0.0286 (7) |
| 15-25 | 1741 | 0.2312 | 0.2119 | +0.0193 ± 0.0043 | 0.6597 | 0.6079 | 0.5795 | 0.3856 | 0.4325 | -0.102 ± 0.0111 | -0.03 (1) |
| 25-40 | 1028 | 0.2177 | 0.2059 | +0.0118 ± 0.0084 | 0.6253 | 0.5928 | 0.6509 | 0.3414 | 0.4747 | -0.058 ± 0.0131 | -0.0267 (3) |
| 40+ | 229 | 0.3093 | 0.1804 | +0.1289 ± 0.0253 | 0.8338 | 0.5323 | 0.7372 | 0.2806 | 0.3799 | -0.075 ± 0.0258 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5833 | 0.1865 | 0.1871 | -0.0005 ± 0.0002 | 0.549 | 0.5495 | 0.4871 | 0.4717 | 0.486 | -0.037 ± 0.0057 | -0.0189 (44) |
| 3-5 | 4186 | 0.2046 | 0.2029 | +0.0017 ± 0.0006 | 0.5944 | 0.5886 | 0.4803 | 0.4407 | 0.4393 | -0.055 ± 0.0071 | -0.0073 (22) |
| 5-10 | 9088 | 0.1963 | 0.1908 | +0.0055 ± 0.0007 | 0.5764 | 0.5589 | 0.4849 | 0.411 | 0.41 | -0.057 ± 0.0046 | -0.0117 (42) |
| 10-15 | 7316 | 0.1952 | 0.1795 | +0.0157 ± 0.0012 | 0.5759 | 0.5316 | 0.4945 | 0.3711 | 0.3692 | -0.063 ± 0.005 | -0.0136 (14) |
| 15-25 | 9424 | 0.2108 | 0.1717 | +0.0392 ± 0.0017 | 0.615 | 0.5065 | 0.5091 | 0.3144 | 0.3122 | -0.067 ± 0.0043 | -0.0533 (3) |
| 25-40 | 7365 | 0.2164 | 0.1232 | +0.0932 ± 0.0026 | 0.6259 | 0.3794 | 0.5245 | 0.209 | 0.2205 | -0.051 ± 0.004 | -0.02 (4) |
| 40+ | 5032 | 0.3881 | 0.0477 | +0.3404 ± 0.0035 | 1.0116 | 0.1802 | 0.6362 | 0.1071 | 0.0626 | -0.077 ± 0.003 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1647 | 0.196 | 0.1956 | +0.0003 ± 0.0004 | 0.5701 | 0.5691 | 0.5064 | 0.4914 | 0.4882 | -0.075 ± 0.0111 | -0.0311 (57) |
| 3-5 | 1162 | 0.1895 | 0.1896 | -0.0001 ± 0.001 | 0.5571 | 0.5564 | 0.4986 | 0.4587 | 0.4776 | -0.053 ± 0.0131 | -0.0194 (34) |
| 5-10 | 2358 | 0.1987 | 0.1936 | +0.0051 ± 0.0014 | 0.5863 | 0.57 | 0.51 | 0.4363 | 0.4389 | -0.077 ± 0.0093 | -0.005 (78) |
| 10-15 | 1627 | 0.2156 | 0.2033 | +0.0123 ± 0.0028 | 0.6258 | 0.5903 | 0.5445 | 0.4217 | 0.4321 | -0.087 ± 0.0115 | 0.0015 (67) |
| 15-25 | 2118 | 0.2325 | 0.2076 | +0.0249 ± 0.0039 | 0.6632 | 0.5989 | 0.5924 | 0.3974 | 0.4325 | -0.090 ± 0.01 | -0.0214 (59) |
| 25-40 | 1234 | 0.2419 | 0.2121 | +0.0298 ± 0.008 | 0.6904 | 0.6075 | 0.6884 | 0.3768 | 0.4854 | -0.081 ± 0.0124 | -0.0243 (28) |
| 40+ | 457 | 0.3282 | 0.1985 | +0.1298 ± 0.02 | 0.937 | 0.5788 | 0.8071 | 0.3305 | 0.4486 | -0.089 ± 0.0188 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5932 | 0.1772 | 0.1771 | +0.0000 ± 0.0002 | 0.5247 | 0.5241 | 0.509 | 0.4937 | 0.5 | -0.042 ± 0.0055 | -0.0204 (104) |
| 3-5 | 4073 | 0.1943 | 0.1935 | +0.0008 ± 0.0006 | 0.5673 | 0.5653 | 0.5019 | 0.4622 | 0.4721 | -0.039 ± 0.007 | -0.022 (74) |
| 5-10 | 8323 | 0.1969 | 0.1904 | +0.0065 ± 0.0007 | 0.5809 | 0.5615 | 0.5032 | 0.4295 | 0.4234 | -0.061 ± 0.0048 | -0.0085 (136) |
| 10-15 | 5728 | 0.2109 | 0.1948 | +0.0161 ± 0.0014 | 0.6141 | 0.5707 | 0.5377 | 0.4148 | 0.4096 | -0.070 ± 0.0059 | -0.0054 (112) |
| 15-25 | 7008 | 0.2318 | 0.1993 | +0.0325 ± 0.0021 | 0.6664 | 0.5778 | 0.5769 | 0.3815 | 0.3964 | -0.068 ± 0.0054 | -0.024 (112) |
| 25-40 | 4514 | 0.2576 | 0.1912 | +0.0664 ± 0.0041 | 0.7282 | 0.556 | 0.6408 | 0.3287 | 0.3813 | -0.060 ± 0.0064 | -0.0267 (58) |
| 40+ | 2023 | 0.37 | 0.1595 | +0.2105 ± 0.0091 | 1.0389 | 0.4753 | 0.7407 | 0.2412 | 0.2907 | -0.058 ± 0.0085 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 8288 | 1.022 ± 0.031 | 1.08 | 0.1677 | 0.1712 | 0.2159 | 0.2033 |
| gen2 | 8288 | 0.818 ± 0.028 | 1.061 | 0.174 | 0.1714 | 0.2331 | 0.2032 |
| gen1_elo | 8288 | 1.004 ± 0.03 | 1.072 | 0.1741 | 0.1714 | 0.2151 | 0.2034 |
| gen1_sr | 8288 | 1.005 ± 0.036 | 1.107 | 0.1336 | 0.1729 | 0.2292 | 0.2029 |
| gen1_ledger | 10603 | 0.866 ± 0.023 | 1.062 | 0.1903 | 0.1772 | 0.2172 | 0.2001 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 38,154)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 9,188 | 24.1% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 9,057 | 23.7% |
| BOOK_QUALITY | execution | 6,396 | 16.8% |
| POOR_DATA | data | 4,336 | 11.4% |
| LIMITED_DATA | data | 2,282 | 6.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 2,232 | 5.9% |
| IDENTITY_AMBIGUOUS | mapping | 1,570 | 4.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,439 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 1,070 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 583 | 1.5% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 24.1%, coverage 23.7%, data 17.3%, execution 16.8%, market_freshness/coverage 8.6%, mapping 4.1%, model_calibration_or_unknown 3.8%, model_calibration 1.5%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 95.1%, LOW_DATA_QUALITY 72.2%, THIN_PLAYER_HISTORY 60.0%, STALE_PLAYER_DATA 51.8%, STALE_KALSHI_QUOTE 48.4%, MODEL_INTERNAL_DISAGREEMENT 41.6%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 23.2%, MODEL_HIGH_UNCERTAINTY 18.8%, PLAYER_IDENTITY_RISK 15.0%, LEVEL_TRANSFER_RISK 9.2%, LOW_DISPLAYED_LIQUIDITY 8.7%, EVENT_MAPPING_RISK 7.0%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.1%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 26.0%, POST_SETTLEMENT_OBSERVATION 23.7%, POSSIBLE_IN_PLAY_QUOTE 6.3%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 20,456)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,299 | 35.7% |
| STALE_QUOTE | market_freshness | 4,077 | 19.9% |
| BOOK_QUALITY | execution | 3,301 | 16.1% |
| POOR_DATA | data | 1,834 | 9.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,204 | 5.9% |
| IDENTITY_AMBIGUOUS | mapping | 871 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 704 | 3.4% |
| LIMITED_DATA | data | 675 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 350 | 1.7% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 140 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 35.7%, market_freshness 19.9%, execution 16.1%, data 12.3%, market_freshness/coverage 9.3%, mapping 4.3%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.2%, START_UNVERIFIABLE 97.4%, LOW_DATA_QUALITY 75.2%, THIN_PLAYER_HISTORY 62.0%, STALE_KALSHI_QUOTE 55.9%, STALE_PLAYER_DATA 45.0%, MODEL_INTERNAL_DISAGREEMENT 41.6%, ASYMMETRIC_SAMPLE_SIZE 34.2%, WIDE_SPREAD 22.4%, MODEL_HIGH_UNCERTAINTY 19.5%, PLAYER_IDENTITY_RISK 17.8%, LOW_DISPLAYED_LIQUIDITY 8.6%, EVENT_MAPPING_RISK 8.5%, LEVEL_TRANSFER_RISK 8.1%, MODEL_CALIBRATION_OUTLIER 4.6%, EXTERNAL_MARKET_REJECTION 1.7%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 38.6%, POST_SETTLEMENT_OBSERVATION 35.7%, POSSIBLE_IN_PLAY_QUOTE 6.4%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 16469, "IDENTITY_AMBIGUOUS": 3987}; ticker orientation: {"VERIFIED": 20456}.

Checks: discipline:AMBIGUOUS 1323, discipline:PASS 19133, identity_confidence:AMBIGUOUS 3634, identity_confidence:PASS 16822, level_mapping:NA 1335, level_mapping:PASS 19121, market_pair:AMBIGUOUS 518, market_pair:NA 435, market_pair:PASS 19503, model_complement:NA 397, model_complement:PASS 20059, namesake:AMBIGUOUS 6, namesake:PASS 20450, physical_match_id:NA 6732, physical_match_id:PASS 13724, player_ids:PASS 20456, same_pair_other_event:PASS 20456, ticker_orientation:PASS 20456

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,639 | 3.7% | 3.1% | 1.2% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 24, "market_freshness/coverage": 22} | 5.47 | 0.222 / 0.2184 (873) | 25.7% | 2.4% | 3.2% | 3.0% |
| CHALLENGER | 13,550 | 16.7% | 6.0% | 11.1% | {"coverage": 1396, "market_freshness": 276, "market_freshness/coverage": 245, "data": 164, "model_calibration_or_unknown": 84, "execution": 41, "model_calibration": 41, "mapping": 17, "possible_market_error": 1} | 7.29 | 0.2213 / 0.2112 (3150) | 41.8% | 13.5% | 4.0% | 23.0% |
| DOUBLES | 2,847 | 46.5% | 46.5% | 6.5% | {"execution": 730, "mapping": 404, "market_freshness": 106, "market_freshness/coverage": 76, "coverage": 7} | 23.23 | 0.2967 / 0.2316 (718) | 8.2% | 0.0% | 100.0% | 6.4% |
| ITF_MEN | 27,442 | 25.4% | 17.6% | 34.1% | {"coverage": 2488, "market_freshness": 1447, "execution": 1056, "data": 1025, "market_freshness/coverage": 709, "mapping": 233, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.74 | 0.2183 / 0.1979 (5841) | 42.5% | 69.6% | 14.2% | 22.0% |
| ITF_WOMEN | 34,147 | 26.5% | 18.6% | 44.3% | {"coverage": 3329, "market_freshness": 1987, "execution": 1391, "data": 1219, "market_freshness/coverage": 799, "mapping": 211, "model_calibration_or_unknown": 98, "model_calibration": 23} | 12.42 | 0.2035 / 0.194 (6681) | 43.1% | 57.2% | 10.0% | 22.3% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,952 | 5.9% | 5.0% | 1.4% | {"market_freshness": 111, "model_calibration_or_unknown": 52, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.68 | 0.2311 / 0.2208 (816) | 30.3% | 2.0% | 1.2% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.4% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 404 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.4h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 509 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFMATCH-26NOV12VALRAT-RAT` | ITF_MEN | gen1_ledger | 92% / 4% | +88 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 10 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1333.0, ratio 3.64); no external reference |
| 6 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 7 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 8 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 9 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 172 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 10 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 769 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 11 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 869 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 12 | `KXITFMATCH-26NOV10KOUPOR-POR` | ITF_MEN | fair_v1 | 87% / 2% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.1h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 493 min (STALE); data POOR (grade D, thinner serve sample 1554.0, ratio 1.02); no external reference |
| 13 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 14 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 899 min (STALE); no external reference |
| 17 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 18 | `KXITFMATCH-26NOV13ALMJAD-ALM` | ITF_MEN | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 385 min (STALE); data LIMITED (grade C, thinner serve sample 691.0, ratio 3.98); no external reference |
| 19 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 20 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 21 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 22 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 23 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 24 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 25 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 26 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 27 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 28 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 573 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 29 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 30 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 31 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 32 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 33 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 34 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 35 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 36 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 37 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 38 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 39 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 40 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 41 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 42 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 43 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 44 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 45 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 46 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 47 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 48 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 49 | `KXITFWMATCH-26NOV11CORROJ-ROJ` | ITF_WOMEN | fair_v1 | 87% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 375 min (STALE); data POOR (grade D, thinner serve sample 531.0, ratio 1.04); no external reference |
| 50 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9738, "by_level_share_of_ge_25pp": {"ATP": 0.012, "CHALLENGER": 0.1107, "DOUBLES": 0.0647, "ITF_MEN": 0.3407, "ITF_WOMEN": 0.4428, "OTHER": 0.0006, "WTA": 0.0143, "WTA125": 0.0143}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5589, "share_primary_cause_market_settled_or_in_play": 0.4501, "share_primary_cause_stale_quote_only": 0.1993}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 20456, "identity_ambiguous_share": 0.1949, "ticker_orientation": {"VERIFIED": 20456}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 13724, "with_external": 649, "coverage": 0.0473, "external_status": {"EXTERNAL_STALE": 412, "AGREES_WITH_KALSHI": 224, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 412, "MODEL_LONE_OUTLIER": 224, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3451, "share_external_supports_model": 0.02}, "pregame_clean_ge_25pp": {"n": 6166, "with_external": 617, "coverage": 0.1001, "external_status": {"EXTERNAL_STALE": 387, "AGREES_WITH_KALSHI": 217, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 387, "MODEL_LONE_OUTLIER": 217, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3517, "share_external_supports_model": 0.0211}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 490.0, "median_sample_ratio": 2.43, "median_min_matches": 18.0, "median_max_days_since_last": 246.0, "share_severe_asymmetry": 0.2052, "data_status": {"POOR": 11592, "LIMITED": 5169, "ADEQUATE": 3695}, "comparison_lt_10pp": {"median_thinner_serve_points": 1673.0, "median_sample_ratio": 1.71, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1672, "model_minus_observed": 0.0705, "kalshi_minus_observed": -0.0683, "brier_diff_model_minus_kalshi": 0.0041}, "4-10x": {"n": 1142, "model_minus_observed": 0.0859, "kalshi_minus_observed": -0.0582, "brier_diff_model_minus_kalshi": 0.0095}, "<2x": {"n": 4072, "model_minus_observed": 0.1034, "kalshi_minus_observed": -0.0195, "brier_diff_model_minus_kalshi": 0.0149}, ">=10x": {"n": 1402, "model_minus_observed": 0.128, "kalshi_minus_observed": -0.0433, "brier_diff_model_minus_kalshi": 0.0185}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 8288, "model": {"intercept": -0.56, "slope": 0.818, "slope_se": 0.028}, "kalshi_mid_same_rows": {"intercept": 0.168, "slope": 1.061, "slope_se": 0.031}, "mean_extremity_model": 0.174, "mean_extremity_kalshi": 0.1714, "model_brier": 0.2331, "kalshi_brier": 0.2032, "brier_diff_model_minus_kalshi": 0.0299, "brier_diff_se": 0.0021, "model_logloss": 0.6639, "kalshi_logloss": 0.5887}, "fair_v1": {"n": 8288, "model": {"intercept": -0.471, "slope": 1.022, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.211, "slope": 1.08, "slope_se": 0.031}, "mean_extremity_model": 0.1677, "mean_extremity_kalshi": 0.1712, "model_brier": 0.2159, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.0126, "brier_diff_se": 0.0017, "model_logloss": 0.6211, "kalshi_logloss": 0.5889}, "gen1_elo": {"n": 8288, "model": {"intercept": -0.459, "slope": 1.004, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.214, "slope": 1.072, "slope_se": 0.031}, "mean_extremity_model": 0.1741, "mean_extremity_kalshi": 0.1714, "model_brier": 0.2151, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": 0.0117, "brier_diff_se": 0.0017, "model_logloss": 0.6198, "kalshi_logloss": 0.5891}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2551, "share_ge_15": 0.451, "median_abs_gap": 13.24, "n": 53789}, "gen1_elo": {"share_ge_25": 0.2529, "share_ge_15": 0.4467, "median_abs_gap": 13.03, "n": 53789}, "gen1_sr": {"share_ge_25": 0.3174, "share_ge_15": 0.526, "median_abs_gap": 16.03, "n": 53789}, "gen2": {"share_ge_25": 0.3173, "share_ge_15": 0.5142, "median_abs_gap": 15.57, "n": 53789}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1513, "share_ge_15": 0.3547, "median_abs_gap": 10.71, "n": 40753}, "gen1_elo": {"share_ge_25": 0.1497, "share_ge_15": 0.3489, "median_abs_gap": 10.51, "n": 40753}, "gen1_sr": {"share_ge_25": 0.2142, "share_ge_15": 0.4392, "median_abs_gap": 12.98, "n": 40756}, "gen2": {"share_ge_25": 0.2294, "share_ge_15": 0.4388, "median_abs_gap": 12.83, "n": 40757}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.47, "share_ge_25_all": 0.0369, "share_ge_25_pregame_clean": 0.0309}, "WTA": {"median_abs_gap_pregame_clean": 7.68, "share_ge_25_all": 0.059, "share_ge_25_pregame_clean": 0.0501}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2338, "share_within_10pp_all": 0.435, "share_within_10pp_pregame_clean": 0.4906, "corr_model_vs_mid_pregame_clean": 0.8499}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1189, "model_brier": 0.196, "kalshi_brier": 0.196, "brier_diff_model_minus_kalshi": 0.0}, "10-15": {"n_settled": 1443, "model_brier": 0.2201, "kalshi_brier": 0.2104, "brier_diff_model_minus_kalshi": 0.0097}, "15-25": {"n_settled": 1839, "model_brier": 0.2256, "kalshi_brier": 0.2074, "brier_diff_model_minus_kalshi": 0.0182}, "25-40": {"n_settled": 1043, "model_brier": 0.2256, "kalshi_brier": 0.2037, "brier_diff_model_minus_kalshi": 0.0219}, "3-5": {"n_settled": 776, "model_brier": 0.2084, "kalshi_brier": 0.2079, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 214, "model_brier": 0.307, "kalshi_brier": 0.1666, "brier_diff_model_minus_kalshi": 0.1404}, "5-10": {"n_settled": 1784, "model_brier": 0.2022, "kalshi_brier": 0.2003, "brier_diff_model_minus_kalshi": 0.0019}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.56, "slope": 0.818, "slope_se": 0.028}, "kalshi_slope": {"intercept": 0.168, "slope": 1.061, "slope_se": 0.031}, "n": 8288}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.5, "slope": 0.866, "slope_se": 0.023}, "kalshi_slope": {"intercept": 0.15, "slope": 1.062, "slope_se": 0.026}, "n": 10603}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 718, "model_brier": 0.2967, "kalshi_brier": 0.2316, "brier_diff_model_minus_kalshi": 0.0652, "brier_diff_se": 0.0109, "corr_model_outcome": 0.1168, "corr_kalshi_outcome": 0.2838}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
