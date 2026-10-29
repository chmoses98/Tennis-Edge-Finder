# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-29T10:33Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 67,623): 0-3 14.1%, 3-5 9.6%, 5-10 20.1%, 10-15 15.3%, 15-25 19.1%, 25-40 13.9%, 40+ 8.0%; median gap 11.87 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.8%, Challenger 10.9%, doubles 6.5%). Main tour: ATP 4.2% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 14,774): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.6%, STALE_QUOTE 18.7%, BOOK_QUALITY 18.7%, POOR_DATA 9.4%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IDENTITY_AMBIGUOUS 4.1%, LIMITED_DATA 3.5%, IN_PLAY_QUOTE 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.6%, market_freshness 18.7%, execution 18.7%, data 12.9%, market_freshness/coverage 9.0%, mapping 4.1%, model_calibration_or_unknown 2.1%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 51.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.7% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 14,774 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.7% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 458.0 points vs 1648.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.011, Gen-2 0.801, Gen-1 ledger 0.854 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 712 model 0.2236 vs Kalshi 0.2071; n 149 model 0.2799 vs Kalshi 0.1899.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA. Not implemented here.

## 1. Observations

* 288,781 model-market comparisons (471,120 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 96,803 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-29T10:16:52.921965+00:00'], shadow board 77,256 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-29T10:16:56.718023+00:00'], Model 4 36,349 rows, 23,373 settled tickers, 8,594 tickers with an external scan.
* By model: {"gen1_ledger": 65277, "gen1_elo": 38836, "fair_v1": 38836, "gen2": 38836, "gen1_sr": 38836, "model4_fundamental": 34102, "model4_conditioned": 34058}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 67,623 | 14.1 | 9.6 | 20.1 | 15.3 | 19.1 | 13.9 | 8.0 | 11.87 | 40.9% | 21.9% |
| MW fair_v1 | 38,836 | 13.0 | 8.7 | 18.6 | 15.4 | 19.5 | 15.0 | 9.8 | 13.02 | 44.3% | 24.8% |
| MW gen1_elo | 38,836 | 12.6 | 8.6 | 19.3 | 15.4 | 19.5 | 14.9 | 9.7 | 12.93 | 44.1% | 24.6% |
| MW gen1_ledger | 28,787 | 15.6 | 10.8 | 22.0 | 15.2 | 18.5 | 12.4 | 5.5 | 10.4 | 36.4% | 17.9% |
| MW gen1_sr | 38,836 | 10.1 | 7.2 | 16.9 | 13.8 | 20.7 | 18.6 | 12.8 | 15.86 | 52.0% | 31.3% |
| MW gen2 | 38,836 | 11.2 | 7.5 | 16.5 | 13.8 | 19.4 | 17.8 | 13.8 | 15.48 | 51.0% | 31.6% |
| all families model4_conditioned | 34,058 | 22.4 | 18.2 | 34.3 | 17.2 | 4.9 | 1.9 | 1.1 | 6.01 | 7.9% | 3.0% |
| all families model4_fundamental | 34,102 | 17.3 | 13.3 | 33.8 | 20.4 | 10.2 | 3.6 | 1.4 | 7.71 | 15.2% | 5.0% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.3%, >=15pp 40.9%, >=20pp 30.3%, >=25pp 21.9%, >=30pp 15.7%, >=40pp 8.0%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.28pp; >=10pp 44.7%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,385 | 27.2 | 15.5 | 27.5 | 13.5 | 11.7 | 4.1 | 0.6 | 5.93 | 16.4% | 4.7% |
| CHALLENGER | 5,834 | 16.2 | 9.8 | 20.8 | 15.3 | 15.4 | 11.9 | 10.7 | 10.91 | 37.9% | 22.5% |
| ITF_MEN | 10,826 | 9.8 | 7.4 | 17.0 | 15.2 | 21.1 | 17.6 | 12.0 | 15.21 | 50.7% | 29.5% |
| ITF_WOMEN | 15,305 | 9.7 | 7.1 | 15.8 | 15.1 | 22.1 | 18.2 | 12.0 | 15.69 | 52.3% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,420 | 18.3 | 13.7 | 24.5 | 20.1 | 16.1 | 6.5 | 0.9 | 8.25 | 23.4% | 7.3% |
| WTA125 | 1,060 | 16.0 | 7.7 | 22.6 | 19.2 | 20.2 | 12.6 | 1.7 | 10.7 | 34.4% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,385 | 26.0 | 15.4 | 25.4 | 16.3 | 12.0 | 4.1 | 0.8 | 6.23 | 16.9% | 4.9% |
| CHALLENGER | 5,834 | 15.1 | 8.9 | 18.3 | 14.3 | 18.1 | 13.7 | 11.6 | 12.59 | 43.4% | 25.2% |
| ITF_MEN | 10,826 | 8.0 | 6.2 | 15.0 | 13.7 | 19.6 | 20.6 | 16.9 | 18.03 | 57.2% | 37.6% |
| ITF_WOMEN | 15,305 | 8.1 | 5.8 | 14.0 | 12.6 | 20.6 | 21.3 | 17.5 | 19.21 | 59.5% | 38.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,420 | 15.2 | 11.0 | 21.9 | 15.5 | 22.0 | 12.6 | 1.8 | 10.59 | 36.4% | 14.4% |
| WTA125 | 1,060 | 9.6 | 6.3 | 16.3 | 16.8 | 24.3 | 17.6 | 9.0 | 15.37 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,385 | 22.3 | 13.0 | 24.4 | 16.0 | 16.2 | 6.7 | 1.3 | 7.58 | 24.2% | 8.1% |
| CHALLENGER | 5,834 | 15.0 | 9.3 | 21.1 | 15.9 | 15.6 | 12.2 | 10.9 | 11.25 | 38.6% | 23.1% |
| ITF_MEN | 10,826 | 9.2 | 7.1 | 17.4 | 14.4 | 21.6 | 17.9 | 12.2 | 15.68 | 51.8% | 30.2% |
| ITF_WOMEN | 15,305 | 9.5 | 6.8 | 16.3 | 15.8 | 22.1 | 18.1 | 11.3 | 15.5 | 51.5% | 29.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,420 | 23.6 | 16.6 | 31.7 | 14.7 | 9.4 | 2.8 | 1.3 | 6.08 | 13.5% | 4.1% |
| WTA125 | 1,060 | 22.1 | 13.0 | 26.5 | 16.9 | 14.9 | 6.2 | 0.4 | 7.99 | 21.5% | 6.6% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,971 | 24.4 | 18.9 | 31.2 | 12.9 | 9.0 | 3.0 | 0.5 | 5.82 | 12.5% | 3.5% |
| CHALLENGER | 3,956 | 22.5 | 14.6 | 27.0 | 14.6 | 13.7 | 6.0 | 1.6 | 7.13 | 21.3% | 7.6% |
| DOUBLES | 2,063 | 5.2 | 4.5 | 12.3 | 10.8 | 21.0 | 24.9 | 21.4 | 23.54 | 67.3% | 46.3% |
| ITF_MEN | 8,282 | 13.0 | 9.4 | 21.1 | 15.8 | 21.4 | 13.3 | 6.0 | 11.92 | 40.6% | 19.2% |
| ITF_WOMEN | 9,861 | 13.1 | 9.2 | 19.7 | 15.6 | 21.4 | 15.4 | 5.7 | 12.42 | 42.5% | 21.1% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,431 | 24.2 | 15.5 | 30.0 | 18.0 | 9.2 | 2.8 | 0.3 | 6.8 | 12.3% | 3.1% |
| WTA125 | 1,074 | 24.9 | 12.5 | 21.2 | 19.0 | 13.4 | 7.4 | 1.7 | 7.92 | 22.4% | 9.0% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,287 | 27.6 | 15.6 | 27.8 | 13.4 | 11.5 | 3.7 | 0.4 | 5.9 | 15.6% | 4.1% |
| CHALLENGER | 4,095 | 21.2 | 12.4 | 26.0 | 17.8 | 15.1 | 6.2 | 1.5 | 8.01 | 22.8% | 7.7% |
| ITF_MEN | 7,972 | 11.9 | 8.7 | 20.5 | 17.2 | 22.0 | 14.4 | 5.3 | 12.45 | 41.6% | 19.6% |
| ITF_WOMEN | 11,451 | 11.6 | 8.4 | 18.3 | 17.3 | 24.1 | 15.2 | 5.2 | 13.36 | 44.5% | 20.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,342 | 18.6 | 13.6 | 24.6 | 20.4 | 16.2 | 6.0 | 0.6 | 8.18 | 22.7% | 6.5% |
| WTA125 | 1,024 | 16.3 | 7.6 | 22.1 | 19.5 | 20.7 | 12.3 | 1.5 | 10.97 | 34.5% | 13.8% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,287 | 26.2 | 15.8 | 25.6 | 16.2 | 12.0 | 3.8 | 0.5 | 6.2 | 16.2% | 4.2% |
| CHALLENGER | 4,095 | 19.3 | 11.4 | 23.0 | 16.8 | 18.4 | 9.2 | 1.9 | 9.02 | 29.5% | 11.1% |
| ITF_MEN | 7,973 | 9.4 | 7.3 | 17.3 | 15.9 | 21.4 | 18.9 | 9.9 | 15.06 | 50.1% | 28.7% |
| ITF_WOMEN | 11,452 | 8.9 | 6.7 | 15.8 | 14.1 | 22.8 | 20.9 | 10.8 | 16.71 | 54.4% | 31.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,342 | 15.4 | 11.1 | 22.0 | 15.6 | 22.2 | 12.5 | 1.2 | 10.56 | 35.9% | 13.8% |
| WTA125 | 1,024 | 9.7 | 6.3 | 16.4 | 17.0 | 24.2 | 18.0 | 8.4 | 15.16 | 50.6% | 26.4% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,917 | 24.5 | 19.1 | 31.2 | 13.1 | 8.7 | 2.9 | 0.4 | 5.73 | 12.0% | 3.3% |
| CHALLENGER | 3,487 | 23.9 | 15.5 | 28.2 | 14.8 | 13.0 | 4.1 | 0.5 | 6.59 | 17.6% | 4.6% |
| DOUBLES | 1,935 | 5.1 | 4.5 | 12.5 | 10.9 | 20.9 | 24.8 | 21.3 | 23.31 | 66.9% | 46.1% |
| ITF_MEN | 7,083 | 13.9 | 9.9 | 22.8 | 16.5 | 21.3 | 11.8 | 3.9 | 11.0 | 37.0% | 15.7% |
| ITF_WOMEN | 8,402 | 13.7 | 9.7 | 20.9 | 16.2 | 21.5 | 14.4 | 3.6 | 11.61 | 39.5% | 17.9% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,377 | 24.6 | 15.9 | 30.0 | 18.1 | 9.2 | 2.2 | 0.1 | 6.68 | 11.5% | 2.2% |
| WTA125 | 950 | 26.2 | 13.3 | 22.3 | 20.2 | 12.3 | 5.2 | 0.5 | 7.36 | 18.0% | 5.7% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,063 | 5.2 | 4.5 | 12.3 | 10.8 | 21.0 | 24.9 | 21.4 | 23.54 | 67.3% | 46.3% |
| singles | 26,724 | 16.4 | 11.2 | 22.8 | 15.6 | 18.3 | 11.4 | 4.3 | 9.89 | 34.0% | 15.7% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,790 | 13.1 | 9.3 | 20.1 | 15.6 | 19.1 | 13.8 | 9.0 | 12.39 | 41.9% | 22.8% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 25,404 | 13.5 | 8.7 | 18.5 | 15.1 | 19.3 | 15.1 | 9.8 | 12.98 | 44.2% | 24.9% |
| UNKNOWN | 5,393 | 10.5 | 7.7 | 17.2 | 16.6 | 20.9 | 15.9 | 11.1 | 14.11 | 48.0% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 10,748 | 20.0 | 12.2 | 22.4 | 15.8 | 14.7 | 9.3 | 5.8 | 8.56 | 29.7% | 15.1% |
| B | 4,748 | 12.9 | 8.9 | 19.1 | 16.1 | 19.4 | 12.8 | 10.8 | 12.59 | 43.0% | 23.6% |
| C | 5,546 | 12.1 | 8.9 | 19.9 | 15.8 | 18.7 | 14.3 | 10.3 | 12.77 | 43.4% | 24.7% |
| D | 6,136 | 12.0 | 8.3 | 17.6 | 15.4 | 21.5 | 15.7 | 9.3 | 13.74 | 46.6% | 25.1% |
| F | 11,658 | 7.4 | 5.6 | 15.0 | 14.6 | 23.3 | 21.0 | 13.1 | 17.71 | 57.4% | 34.1% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,638 | 24.0 | 15.7 | 28.7 | 15.4 | 11.0 | 3.8 | 1.3 | 6.54 | 16.1% | 5.1% |
| B | 4,022 | 17.0 | 10.6 | 24.1 | 16.2 | 19.0 | 9.9 | 3.2 | 9.64 | 32.1% | 13.1% |
| C | 5,616 | 11.2 | 7.8 | 19.5 | 14.7 | 21.1 | 15.5 | 10.1 | 13.46 | 46.7% | 25.6% |
| D | 4,219 | 14.5 | 10.0 | 21.6 | 15.3 | 20.0 | 13.1 | 5.5 | 11.23 | 38.6% | 18.6% |
| F | 7,292 | 9.9 | 8.4 | 16.0 | 14.9 | 23.2 | 19.9 | 7.8 | 15.44 | 50.8% | 27.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 12,178 | 18.3 | 11.1 | 21.4 | 15.5 | 15.1 | 10.0 | 8.5 | 9.73 | 33.7% | 18.6% |
| LIMITED | 8,498 | 13.6 | 10.0 | 20.3 | 16.3 | 19.1 | 13.4 | 7.4 | 11.73 | 39.8% | 20.8% |
| POOR | 18,160 | 9.1 | 6.5 | 16.0 | 15.0 | 22.6 | 19.0 | 11.8 | 16.15 | 53.4% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,465 | 24.1 | 18.1 | 33.1 | 15.0 | 6.6 | 2.7 | 0.4 | 5.85 | 9.7% | 3.1% |
| GAME_SPREAD | 5,844 | 22.2 | 15.2 | 33.0 | 17.2 | 9.0 | 2.9 | 0.6 | 6.74 | 12.4% | 3.4% |
| MATCH_WINNER | 28,787 | 15.6 | 10.8 | 22.0 | 15.2 | 18.5 | 12.4 | 5.5 | 10.4 | 36.4% | 17.9% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 13,470 | 27.3 | 16.7 | 31.2 | 12.5 | 9.5 | 2.4 | 0.3 | 5.7 | 12.3% | 2.7% |
| TOTAL_GAMES | 9,687 | 9.5 | 10.3 | 36.1 | 26.8 | 10.5 | 4.0 | 2.8 | 9.29 | 17.3% | 6.8% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,067 | 24.4 | 30.1 | 32.9 | 7.4 | 4.0 | 0.9 | 0.2 | 4.7 | 5.1% | 1.1% |
| GAME_SPREAD | 7,976 | 47.3 | 16.0 | 25.4 | 7.3 | 2.2 | 1.2 | 0.6 | 3.27 | 4.0% | 1.8% |
| TOTAL_GAMES | 14,015 | 6.4 | 9.2 | 40.5 | 31.4 | 7.2 | 3.1 | 2.2 | 9.32 | 12.5% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,078 | 23.9 | 16.8 | 34.8 | 14.4 | 7.1 | 2.6 | 0.4 | 6.02 | 10.1% | 3.0% |
| GAME_SPREAD | 7,979 | 20.1 | 13.5 | 27.9 | 20.5 | 12.6 | 4.2 | 1.1 | 7.81 | 17.9% | 5.3% |
| TOTAL_GAMES | 14,045 | 9.9 | 10.2 | 36.3 | 25.4 | 11.5 | 4.2 | 2.4 | 9.2 | 18.1% | 6.6% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 38,836 | 44.3% | 24.8% | 13.02 | 35.6% | 15.4% | 10.77 |
| gen1_elo | 38,836 | 44.1% | 24.6% | 12.93 | 35.4% | 15.4% | 10.57 |
| gen1_sr | 38,836 | 52.0% | 31.3% | 15.86 | 44.2% | 21.9% | 13.03 |
| gen2 | 38,836 | 51.0% | 31.6% | 15.48 | 44.2% | 23.5% | 12.94 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 18,450 | 15.6 | 10.5 | 21.3 | 17.2 | 20.1 | 12.0 | 3.3 | 10.71 | 35.4% | 15.4% |
| STALE | 20,386 | 10.6 | 7.1 | 16.2 | 13.8 | 19.0 | 17.6 | 15.7 | 15.98 | 52.3% | 33.3% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 22,255 | 16.3 | 11.1 | 22.7 | 15.4 | 17.9 | 11.8 | 4.8 | 9.97 | 34.5% | 16.6% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 67,623 | 22255 | 21922 | 23446 | 24.3 | 121.3 | 1451.1 |
| ge_15pp | 27,672 | 7682 | 7823 | 12167 | 26.7 | 431.5 | 1451.1 |
| ge_25pp | 14,774 | 3693 | 3426 | 7655 | 31.6 | 581.5 | 1431.1 |
| lt_10pp | 29,581 | 11152 | 10382 | 8047 | 22.4 | 46.9 | 1421.1 |

Current slate `SL-20261029T103349Z-046f8bf2`: 572 priced rows, quote age at build {'median': 17.4, 'max': 17.5}, freshness {'AGING': 572}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 44 | 0.0 | 0.0 | 31.8 | 6.8 | 34.1 | 22.7 | 4.5 | 20.33 | 61.4% | 27.3% |
| EXTERNAL_LONE_OUTLIER | 23 | 69.6 | 30.4 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.3 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,831 | 19.7 | 11.2 | 25.2 | 18.0 | 17.9 | 7.2 | 0.9 | 8.63 | 25.9% | 8.0% |
| KALSHI_LONE_OUTLIER | 26 | 3.9 | 3.9 | 76.9 | 7.7 | 3.9 | 3.9 | 0.0 | 6.31 | 7.7% | 3.9% |
| MARKETS_AGREE | 751 | 65.1 | 34.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,619 | 0.0 | 2.5 | 35.9 | 25.8 | 24.6 | 10.4 | 0.9 | 12.12 | 35.9% | 11.2% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 38,836 | 6294 (16.2%) | 25.7% | 1.1% | {"EXTERNAL_STALE": 3831, "AGREES_WITH_KALSHI": 1619, "ALL_AGREE": 751, "SUPPORTS_MODEL_DIRECTION": 43, "AGREES_WITH_MODEL": 26, "EXTERNAL_OUTLIER": 23, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 17,191 | 1602 (9.3%) | 36.3% | 1.8% | {"EXTERNAL_STALE": 992, "AGREES_WITH_KALSHI": 581, "SUPPORTS_MODEL_DIRECTION": 27, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 9,619 | 502 (5.2%) | 36.2% | 2.6% | {"EXTERNAL_STALE": 307, "AGREES_WITH_KALSHI": 182, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,645 | 477 (10.3%) | 36.7% | 2.7% | {"EXTERNAL_STALE": 289, "AGREES_WITH_KALSHI": 175, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 15,660 | 3580 (22.9%) | 17.3% | 1.0% | {"EXTERNAL_STALE": 2149, "ALL_AGREE": 751, "AGREES_WITH_KALSHI": 621, "EXTERNAL_OUTLIER": 23, "AGREES_WITH_MODEL": 22, "SUPPORTS_MODEL_DIRECTION": 13, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 7,615 | 10.4 | 7.4 | 19.8 | 14.3 | 21.6 | 16.6 | 9.9 | 14.12 | 48.1% | 26.5% |
| 4-10x | 5,239 | 11.2 | 8.6 | 18.5 | 15.6 | 21.8 | 14.4 | 9.9 | 13.64 | 46.2% | 24.3% |
| <2x | 19,592 | 15.2 | 10.0 | 19.4 | 16.1 | 17.4 | 13.1 | 8.8 | 11.56 | 39.3% | 21.9% |
| >=10x | 6,390 | 10.6 | 6.4 | 15.2 | 14.4 | 21.5 | 19.1 | 12.7 | 16.2 | 53.4% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 9,857 | 12.7 | 8.7 | 19.6 | 16.1 | 19.0 | 13.6 | 10.3 | 12.69 | 42.9% | 23.9% |
| 300-1000 | 8,382 | 12.1 | 8.7 | 17.8 | 15.3 | 20.3 | 16.3 | 9.5 | 13.58 | 46.1% | 25.8% |
| <300 | 12,660 | 8.3 | 5.8 | 15.2 | 14.8 | 23.0 | 20.0 | 12.9 | 17.05 | 55.9% | 32.9% |
| >=3000 | 7,937 | 21.6 | 13.3 | 23.9 | 15.7 | 13.7 | 7.2 | 4.6 | 7.53 | 25.5% | 11.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1107 | 0.55 | 0.4112 | 0.4959 | +0.054 | -0.085 | -0.0016 ± 0.0046 |
| ratio 4-10x | 759 | 0.5796 | 0.4336 | 0.4954 | +0.084 | -0.062 | 0.0077 ± 0.0058 |
| ratio <2x | 2648 | 0.5376 | 0.4141 | 0.4502 | +0.087 | -0.036 | 0.011 ± 0.0028 |
| ratio >=10x | 963 | 0.5659 | 0.3908 | 0.4455 | +0.120 | -0.055 | 0.0145 ± 0.0059 |
| thinner_sample 1000-3000 | 1473 | 0.5392 | 0.4126 | 0.4535 | +0.086 | -0.041 | 0.0086 ± 0.0038 |
| thinner_sample 300-1000 | 1247 | 0.5678 | 0.4257 | 0.4876 | +0.080 | -0.062 | 0.0024 ± 0.0045 |
| thinner_sample <300 | 1857 | 0.558 | 0.3901 | 0.4593 | +0.099 | -0.069 | 0.0107 ± 0.0041 |
| thinner_sample >=3000 | 900 | 0.5321 | 0.4381 | 0.4633 | +0.069 | -0.025 | 0.0129 ± 0.0038 |
| data_status ADEQUATE | 1498 | 0.5342 | 0.431 | 0.4499 | +0.084 | -0.019 | 0.0126 ± 0.0032 |
| data_status LIMITED | 1308 | 0.5489 | 0.416 | 0.4786 | +0.070 | -0.063 | 0.0046 ± 0.0042 |
| data_status POOR | 2671 | 0.5612 | 0.3997 | 0.4665 | +0.095 | -0.067 | 0.0083 ± 0.0034 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 807 | 0.1989 | 0.1995 | -0.0005 ± 0.0006 | 0.5772 | 0.5787 | 0.5029 | 0.4878 | 0.5105 | -0.085 ± 0.0167 | -0.01 (5) |
| 3-5 | 494 | 0.2059 | 0.2062 | -0.0003 ± 0.0017 | 0.5952 | 0.5944 | 0.5026 | 0.4627 | 0.4858 | -0.097 ± 0.0209 | 0.02 (1) |
| 5-10 | 1145 | 0.2013 | 0.2016 | -0.0003 ± 0.002 | 0.5884 | 0.5862 | 0.5107 | 0.4369 | 0.4734 | -0.088 ± 0.0137 | -0.0167 (6) |
| 10-15 | 958 | 0.2219 | 0.2132 | +0.0087 ± 0.0037 | 0.6369 | 0.6124 | 0.5263 | 0.4027 | 0.428 | -0.109 ± 0.015 | -0.048 (5) |
| 15-25 | 1212 | 0.2246 | 0.2126 | +0.0120 ± 0.0052 | 0.6448 | 0.6096 | 0.5751 | 0.3795 | 0.4472 | -0.098 ± 0.0133 | -0.0033 (9) |
| 25-40 | 712 | 0.2236 | 0.2071 | +0.0165 ± 0.0102 | 0.6372 | 0.5961 | 0.6555 | 0.3447 | 0.4733 | -0.074 ± 0.0156 | -0.01 (1) |
| 40+ | 149 | 0.2799 | 0.1899 | +0.0900 ± 0.0311 | 0.7641 | 0.5593 | 0.7421 | 0.2932 | 0.4228 | -0.074 ± 0.0308 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4352 | 0.1834 | 0.1842 | -0.0008 ± 0.0002 | 0.5412 | 0.5422 | 0.4859 | 0.4706 | 0.5005 | -0.024 ± 0.0066 | -0.0129 (17) |
| 3-5 | 2929 | 0.1954 | 0.1931 | +0.0023 ± 0.0007 | 0.57 | 0.5622 | 0.4819 | 0.4421 | 0.4329 | -0.064 ± 0.0082 | 0.0 (2) |
| 5-10 | 6192 | 0.2011 | 0.1976 | +0.0035 ± 0.0008 | 0.5877 | 0.5756 | 0.4839 | 0.4102 | 0.4247 | -0.046 ± 0.0057 | -0.0119 (21) |
| 10-15 | 5197 | 0.2029 | 0.1869 | +0.0160 ± 0.0015 | 0.5923 | 0.5486 | 0.4832 | 0.3592 | 0.356 | -0.067 ± 0.006 | -0.0281 (16) |
| 15-25 | 6464 | 0.2065 | 0.1687 | +0.0377 ± 0.002 | 0.6056 | 0.5003 | 0.4994 | 0.3032 | 0.3058 | -0.069 ± 0.0051 | -0.0025 (44) |
| 25-40 | 5164 | 0.2224 | 0.1263 | +0.0961 ± 0.0031 | 0.6392 | 0.3878 | 0.5267 | 0.2125 | 0.221 | -0.059 ± 0.0048 | -0.01 (1) |
| 40+ | 3349 | 0.3831 | 0.0446 | +0.3385 ± 0.0041 | 0.998 | 0.1729 | 0.632 | 0.104 | 0.06 | -0.078 ± 0.0035 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 627 | 0.2056 | 0.2063 | -0.0007 ± 0.0006 | 0.5932 | 0.595 | 0.5086 | 0.4935 | 0.5199 | -0.103 ± 0.0197 | -0.01 (3) |
| 3-5 | 443 | 0.224 | 0.221 | +0.0030 ± 0.0018 | 0.6334 | 0.6273 | 0.5136 | 0.4739 | 0.4515 | -0.135 ± 0.0238 | 0.02 (1) |
| 5-10 | 997 | 0.2083 | 0.2081 | +0.0001 ± 0.0022 | 0.6028 | 0.6013 | 0.5458 | 0.4709 | 0.5095 | -0.084 ± 0.0149 | -0.01 (4) |
| 10-15 | 897 | 0.2174 | 0.21 | +0.0073 ± 0.0038 | 0.6259 | 0.6069 | 0.5652 | 0.4408 | 0.476 | -0.112 ± 0.016 | -0.04 (5) |
| 15-25 | 1275 | 0.2301 | 0.2146 | +0.0155 ± 0.0051 | 0.655 | 0.6135 | 0.5819 | 0.3866 | 0.4471 | -0.096 ± 0.0132 | -0.0133 (9) |
| 25-40 | 902 | 0.2678 | 0.1963 | +0.0715 ± 0.0093 | 0.7478 | 0.5732 | 0.6557 | 0.3416 | 0.388 | -0.131 ± 0.0147 | -0.0075 (4) |
| 40+ | 336 | 0.3602 | 0.1683 | +0.1919 ± 0.0222 | 0.9902 | 0.5046 | 0.7329 | 0.248 | 0.3065 | -0.080 ± 0.0216 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3714 | 0.1893 | 0.1895 | -0.0003 ± 0.0002 | 0.5538 | 0.5541 | 0.5085 | 0.4935 | 0.5081 | -0.042 ± 0.0074 | -0.0133 (15) |
| 3-5 | 2524 | 0.1976 | 0.1961 | +0.0015 ± 0.0007 | 0.5727 | 0.5682 | 0.5134 | 0.4738 | 0.4731 | -0.053 ± 0.009 | 0.02 (1) |
| 5-10 | 5502 | 0.1988 | 0.1952 | +0.0036 ± 0.0009 | 0.583 | 0.5696 | 0.5122 | 0.438 | 0.4542 | -0.043 ± 0.006 | -0.0117 (6) |
| 10-15 | 4671 | 0.2059 | 0.193 | +0.0129 ± 0.0016 | 0.6017 | 0.563 | 0.5127 | 0.3888 | 0.3993 | -0.057 ± 0.0065 | -0.0189 (18) |
| 15-25 | 6525 | 0.2174 | 0.1817 | +0.0357 ± 0.0021 | 0.6324 | 0.5327 | 0.523 | 0.3276 | 0.3372 | -0.062 ± 0.0053 | -0.0086 (42) |
| 25-40 | 5982 | 0.2513 | 0.136 | +0.1153 ± 0.003 | 0.7089 | 0.4175 | 0.5563 | 0.2396 | 0.2193 | -0.086 ± 0.0048 | -0.0044 (18) |
| 40+ | 4729 | 0.3966 | 0.0588 | +0.3378 ± 0.0041 | 1.0461 | 0.2117 | 0.6505 | 0.1169 | 0.0808 | -0.073 ± 0.0035 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 771 | 0.1958 | 0.1979 | -0.0021 ± 0.0006 | 0.5702 | 0.5757 | 0.5001 | 0.4848 | 0.5447 | -0.037 ± 0.0167 | -0.0137 (8) |
| 3-5 | 535 | 0.2056 | 0.2038 | +0.0018 ± 0.0016 | 0.5947 | 0.5883 | 0.4941 | 0.4545 | 0.4523 | -0.122 ± 0.0203 | 0.0067 (3) |
| 5-10 | 1180 | 0.2033 | 0.2013 | +0.0020 ± 0.002 | 0.5925 | 0.5854 | 0.5086 | 0.4348 | 0.4585 | -0.096 ± 0.0135 | -0.0071 (7) |
| 10-15 | 954 | 0.2097 | 0.2055 | +0.0042 ± 0.0036 | 0.6093 | 0.5953 | 0.5391 | 0.4158 | 0.4612 | -0.095 ± 0.0147 | -0.0317 (6) |
| 15-25 | 1152 | 0.2325 | 0.217 | +0.0154 ± 0.0053 | 0.6629 | 0.6194 | 0.5867 | 0.3923 | 0.4505 | -0.107 ± 0.0138 | -0.03 (1) |
| 25-40 | 726 | 0.2136 | 0.2143 | -0.0006 ± 0.0101 | 0.6162 | 0.6128 | 0.6648 | 0.3535 | 0.5083 | -0.058 ± 0.0155 | 0.015 (2) |
| 40+ | 159 | 0.2959 | 0.197 | +0.0989 ± 0.031 | 0.8067 | 0.5752 | 0.7484 | 0.2975 | 0.4214 | -0.073 ± 0.0322 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4208 | 0.1833 | 0.1839 | -0.0006 ± 0.0002 | 0.5399 | 0.5409 | 0.4816 | 0.4663 | 0.4843 | -0.033 ± 0.0067 | -0.0163 (35) |
| 3-5 | 2877 | 0.2007 | 0.1985 | +0.0021 ± 0.0007 | 0.5841 | 0.5765 | 0.4818 | 0.4423 | 0.4355 | -0.064 ± 0.0084 | -0.0094 (18) |
| 5-10 | 6346 | 0.1944 | 0.1904 | +0.0039 ± 0.0008 | 0.5719 | 0.558 | 0.4834 | 0.4094 | 0.4203 | -0.048 ± 0.0055 | -0.01 (31) |
| 10-15 | 5146 | 0.192 | 0.1789 | +0.0130 ± 0.0015 | 0.5674 | 0.5299 | 0.4929 | 0.3695 | 0.3778 | -0.056 ± 0.0059 | -0.015 (12) |
| 15-25 | 6609 | 0.2123 | 0.1736 | +0.0387 ± 0.002 | 0.6182 | 0.5116 | 0.5122 | 0.3174 | 0.3171 | -0.070 ± 0.0051 | -0.03 (2) |
| 25-40 | 5137 | 0.2164 | 0.1301 | +0.0863 ± 0.0032 | 0.6262 | 0.3962 | 0.5304 | 0.2146 | 0.2383 | -0.046 ± 0.0049 | 0.01 (3) |
| 40+ | 3324 | 0.3947 | 0.0499 | +0.3448 ± 0.0044 | 1.0293 | 0.1871 | 0.6424 | 0.1112 | 0.0659 | -0.080 ± 0.0037 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1163 | 0.1961 | 0.1963 | -0.0002 ± 0.0005 | 0.571 | 0.5713 | 0.5051 | 0.49 | 0.4979 | -0.065 ± 0.0132 | -0.0224 (49) |
| 3-5 | 818 | 0.188 | 0.1872 | +0.0008 ± 0.0012 | 0.5507 | 0.5481 | 0.4984 | 0.4586 | 0.4658 | -0.067 ± 0.0155 | -0.0194 (34) |
| 5-10 | 1702 | 0.2011 | 0.1963 | +0.0048 ± 0.0016 | 0.5913 | 0.5759 | 0.5011 | 0.4275 | 0.4324 | -0.074 ± 0.0109 | -0.005 (78) |
| 10-15 | 1168 | 0.2162 | 0.2042 | +0.0119 ± 0.0033 | 0.6244 | 0.5926 | 0.5352 | 0.4125 | 0.4238 | -0.084 ± 0.0136 | 0.0014 (64) |
| 15-25 | 1507 | 0.2314 | 0.2115 | +0.0199 ± 0.0046 | 0.6596 | 0.6081 | 0.5809 | 0.3863 | 0.4346 | -0.080 ± 0.012 | -0.0214 (59) |
| 25-40 | 942 | 0.2451 | 0.2101 | +0.0351 ± 0.0091 | 0.7002 | 0.6022 | 0.6821 | 0.3703 | 0.4703 | -0.095 ± 0.014 | -0.0219 (26) |
| 40+ | 315 | 0.338 | 0.2016 | +0.1364 ± 0.0244 | 0.9757 | 0.5884 | 0.8133 | 0.3362 | 0.4476 | -0.100 ± 0.0228 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4300 | 0.1759 | 0.1762 | -0.0003 ± 0.0002 | 0.5209 | 0.5213 | 0.5108 | 0.4955 | 0.5088 | -0.036 ± 0.0064 | -0.0157 (88) |
| 3-5 | 2935 | 0.1941 | 0.1927 | +0.0014 ± 0.0007 | 0.5648 | 0.5622 | 0.506 | 0.4662 | 0.4678 | -0.050 ± 0.0082 | -0.0209 (69) |
| 5-10 | 5978 | 0.1985 | 0.1914 | +0.0071 ± 0.0009 | 0.5841 | 0.5634 | 0.4963 | 0.4226 | 0.413 | -0.067 ± 0.0057 | -0.0082 (132) |
| 10-15 | 4204 | 0.2115 | 0.1961 | +0.0154 ± 0.0017 | 0.6139 | 0.5736 | 0.5332 | 0.4102 | 0.4082 | -0.068 ± 0.0069 | -0.0053 (105) |
| 15-25 | 5086 | 0.2292 | 0.2019 | +0.0274 ± 0.0025 | 0.6597 | 0.5833 | 0.5669 | 0.3716 | 0.3995 | -0.060 ± 0.0063 | -0.0253 (107) |
| 25-40 | 3452 | 0.2607 | 0.1871 | +0.0736 ± 0.0046 | 0.7378 | 0.5458 | 0.6354 | 0.3226 | 0.3641 | -0.080 ± 0.0072 | -0.0229 (51) |
| 40+ | 1485 | 0.3796 | 0.1508 | +0.2288 ± 0.0105 | 1.0712 | 0.4531 | 0.737 | 0.2364 | 0.2694 | -0.079 ± 0.0096 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5477 | 1.011 ± 0.037 | 1.087 | 0.169 | 0.1663 | 0.2152 | 0.2066 |
| gen2 | 5477 | 0.801 ± 0.034 | 1.047 | 0.1707 | 0.1667 | 0.2349 | 0.2064 |
| gen1_elo | 5477 | 0.992 ± 0.036 | 1.085 | 0.1755 | 0.1665 | 0.2138 | 0.2067 |
| gen1_sr | 5477 | 0.981 ± 0.045 | 1.109 | 0.1309 | 0.1687 | 0.2308 | 0.206 |
| gen1_ledger | 7615 | 0.854 ± 0.027 | 1.054 | 0.187 | 0.1766 | 0.2183 | 0.2015 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 27,672)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,150 | 22.2% |
| STALE_QUOTE | market_freshness | 6,045 | 21.9% |
| BOOK_QUALITY | execution | 5,302 | 19.2% |
| POOR_DATA | data | 3,269 | 11.8% |
| LIMITED_DATA | data | 1,741 | 6.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,550 | 5.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,217 | 4.4% |
| IDENTITY_AMBIGUOUS | mapping | 1,130 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 797 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 470 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.2%, market_freshness 21.9%, execution 19.2%, data 18.1%, market_freshness/coverage 8.5%, model_calibration_or_unknown 4.4%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.4%, LOW_DATA_QUALITY 72.0%, THIN_PLAYER_HISTORY 60.8%, STALE_PLAYER_DATA 52.6%, STALE_KALSHI_QUOTE 44.0%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 33.5%, WIDE_SPREAD 25.1%, MODEL_HIGH_UNCERTAINTY 17.9%, PLAYER_IDENTITY_RISK 15.6%, LEVEL_TRANSFER_RISK 10.4%, LOW_DISPLAYED_LIQUIDITY 8.0%, EVENT_MAPPING_RISK 7.4%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.8%, POST_SETTLEMENT_OBSERVATION 22.2%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 14,774)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,969 | 33.6% |
| STALE_QUOTE | market_freshness | 2,769 | 18.7% |
| BOOK_QUALITY | execution | 2,761 | 18.7% |
| POOR_DATA | data | 1,394 | 9.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 821 | 5.6% |
| IDENTITY_AMBIGUOUS | mapping | 601 | 4.1% |
| LIMITED_DATA | data | 515 | 3.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 514 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 307 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 122 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.6%, market_freshness 18.7%, execution 18.7%, data 12.9%, market_freshness/coverage 9.0%, mapping 4.1%, model_calibration_or_unknown 2.1%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.8%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 75.2%, THIN_PLAYER_HISTORY 63.0%, STALE_KALSHI_QUOTE 51.8%, STALE_PLAYER_DATA 46.7%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 34.6%, WIDE_SPREAD 24.5%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 18.5%, LEVEL_TRANSFER_RISK 9.3%, EVENT_MAPPING_RISK 9.0%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.7%, POST_SETTLEMENT_OBSERVATION 33.6%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 11724, "IDENTITY_AMBIGUOUS": 3050}; ticker orientation: {"VERIFIED": 14774}.

Checks: discipline:AMBIGUOUS 956, discipline:PASS 13818, identity_confidence:AMBIGUOUS 2731, identity_confidence:PASS 12043, level_mapping:NA 968, level_mapping:PASS 13806, market_pair:AMBIGUOUS 478, market_pair:NA 347, market_pair:PASS 13949, model_complement:NA 311, model_complement:PASS 14463, namesake:AMBIGUOUS 6, namesake:PASS 14768, physical_match_id:NA 5155, physical_match_id:PASS 9619, player_ids:PASS 14774, same_pair_other_event:PASS 14774, ticker_orientation:PASS 14774

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,356 | 4.2% | 3.8% | 1.5% | {"market_freshness": 56, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 17, "coverage": 13} | 5.84 | 0.22 / 0.2173 (611) | 21.6% | 2.9% | 3.3% | 2.8% |
| CHALLENGER | 9,790 | 16.5% | 6.2% | 10.9% | {"coverage": 948, "market_freshness/coverage": 195, "market_freshness": 165, "data": 144, "model_calibration_or_unknown": 74, "execution": 37, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.26 | 0.2192 / 0.2102 (2243) | 35.2% | 15.8% | 4.1% | 22.6% |
| DOUBLES | 2,063 | 46.3% | 46.1% | 6.5% | {"execution": 542, "mapping": 243, "market_freshness": 106, "market_freshness/coverage": 58, "coverage": 7} | 23.31 | 0.308 / 0.2377 (497) | 11.3% | 0.0% | 100.0% | 6.2% |
| ITF_MEN | 19,108 | 25.1% | 17.8% | 32.4% | {"coverage": 1665, "execution": 900, "market_freshness": 871, "data": 713, "market_freshness/coverage": 451, "mapping": 183, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.76 | 0.2168 / 0.1997 (3906) | 37.3% | 70.1% | 16.9% | 21.2% |
| ITF_WOMEN | 25,166 | 26.6% | 19.4% | 45.4% | {"coverage": 2297, "market_freshness": 1426, "execution": 1205, "data": 959, "market_freshness/coverage": 561, "mapping": 152, "model_calibration_or_unknown": 82, "model_calibration": 21} | 12.64 | 0.2049 / 0.1967 (4562) | 39.3% | 57.7% | 10.1% | 21.1% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,851 | 5.7% | 5.0% | 1.5% | {"market_freshness": 76, "model_calibration_or_unknown": 43, "execution": 27, "coverage": 26, "data": 19, "model_calibration": 18, "market_freshness/coverage": 11, "mapping": 1} | 7.58 | 0.2372 / 0.2303 (599) | 26.2% | 1.1% | 1.4% | 3.4% |
| WTA125 | 2,134 | 11.6% | 9.9% | 1.7% | {"market_freshness": 67, "model_calibration_or_unknown": 51, "market_freshness/coverage": 41, "data": 38, "execution": 21, "model_calibration": 14, "coverage": 12, "mapping": 4} | 9.21 | 0.2094 / 0.192 (632) | 25.4% | 11.5% | 5.0% | 7.5% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 286 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 117 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 769 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 628 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 9 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 10 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 899 min (STALE); no external reference |
| 13 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 14 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
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
| 31 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 32 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 33 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 34 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 35 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 36 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 37 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 38 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 39 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 768 min (STALE); no external reference |
| 40 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 41 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 42 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 43 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 77 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 44 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 45 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 46 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 12.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 768 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 49 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 50 | `KXATPDOUBLES-26OCT29MICVANARROLI-MICVAN` | DOUBLES | gen1_ledger | 98% / 20% | +77 | BOOK_QUALITY | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9697, "by_level_share_of_ge_25pp": {"ATP": 0.0154, "CHALLENGER": 0.1094, "DOUBLES": 0.0647, "ITF_MEN": 0.3243, "ITF_WOMEN": 0.4537, "OTHER": 0.0008, "WTA": 0.015, "WTA125": 0.0168}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5181, "share_primary_cause_market_settled_or_in_play": 0.4267, "share_primary_cause_stale_quote_only": 0.1874}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 14774, "identity_ambiguous_share": 0.2064, "ticker_orientation": {"VERIFIED": 14774}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 9619, "with_external": 502, "coverage": 0.0522, "external_status": {"EXTERNAL_STALE": 307, "AGREES_WITH_KALSHI": 182, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 307, "MODEL_LONE_OUTLIER": 182, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3625, "share_external_supports_model": 0.0259}, "pregame_clean_ge_25pp": {"n": 4645, "with_external": 477, "coverage": 0.1027, "external_status": {"EXTERNAL_STALE": 289, "AGREES_WITH_KALSHI": 175, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 289, "MODEL_LONE_OUTLIER": 175, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3669, "share_external_supports_model": 0.0273}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 458.0, "median_sample_ratio": 2.5, "median_min_matches": 18.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2122, "data_status": {"POOR": 8426, "LIMITED": 3790, "ADEQUATE": 2558}, "comparison_lt_10pp": {"median_thinner_serve_points": 1648.0, "median_sample_ratio": 1.73, "median_min_matches": 88.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1107, "model_minus_observed": 0.0541, "kalshi_minus_observed": -0.0848, "brier_diff_model_minus_kalshi": -0.0016}, "4-10x": {"n": 759, "model_minus_observed": 0.0842, "kalshi_minus_observed": -0.0618, "brier_diff_model_minus_kalshi": 0.0077}, "<2x": {"n": 2648, "model_minus_observed": 0.0874, "kalshi_minus_observed": -0.036, "brier_diff_model_minus_kalshi": 0.011}, ">=10x": {"n": 963, "model_minus_observed": 0.1204, "kalshi_minus_observed": -0.0547, "brier_diff_model_minus_kalshi": 0.0145}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 5477, "model": {"intercept": -0.532, "slope": 0.801, "slope_se": 0.034}, "kalshi_mid_same_rows": {"intercept": 0.192, "slope": 1.047, "slope_se": 0.038}, "mean_extremity_model": 0.1707, "mean_extremity_kalshi": 0.1667, "model_brier": 0.2349, "kalshi_brier": 0.2064, "brier_diff_model_minus_kalshi": 0.0285, "brier_diff_se": 0.0026, "model_logloss": 0.6677, "kalshi_logloss": 0.5959}, "fair_v1": {"n": 5477, "model": {"intercept": -0.409, "slope": 1.011, "slope_se": 0.037}, "kalshi_mid_same_rows": {"intercept": 0.284, "slope": 1.087, "slope_se": 0.039}, "mean_extremity_model": 0.169, "mean_extremity_kalshi": 0.1663, "model_brier": 0.2152, "kalshi_brier": 0.2066, "brier_diff_model_minus_kalshi": 0.0086, "brier_diff_se": 0.0021, "model_logloss": 0.6194, "kalshi_logloss": 0.5962}, "gen1_elo": {"n": 5477, "model": {"intercept": -0.385, "slope": 0.992, "slope_se": 0.036}, "kalshi_mid_same_rows": {"intercept": 0.306, "slope": 1.085, "slope_se": 0.038}, "mean_extremity_model": 0.1755, "mean_extremity_kalshi": 0.1665, "model_brier": 0.2138, "kalshi_brier": 0.2067, "brier_diff_model_minus_kalshi": 0.0071, "brier_diff_se": 0.0021, "model_logloss": 0.6167, "kalshi_logloss": 0.5965}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2477, "share_ge_15": 0.4427, "median_abs_gap": 13.02, "n": 38836}, "gen1_elo": {"share_ge_25": 0.2461, "share_ge_15": 0.441, "median_abs_gap": 12.93, "n": 38836}, "gen1_sr": {"share_ge_25": 0.3132, "share_ge_15": 0.5202, "median_abs_gap": 15.86, "n": 38836}, "gen2": {"share_ge_25": 0.3163, "share_ge_15": 0.5104, "median_abs_gap": 15.48, "n": 38836}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1539, "share_ge_15": 0.356, "median_abs_gap": 10.77, "n": 30177}, "gen1_elo": {"share_ge_25": 0.1543, "share_ge_15": 0.3535, "median_abs_gap": 10.57, "n": 30176}, "gen1_sr": {"share_ge_25": 0.2193, "share_ge_15": 0.4424, "median_abs_gap": 13.03, "n": 30178}, "gen2": {"share_ge_25": 0.2355, "share_ge_15": 0.4418, "median_abs_gap": 12.94, "n": 30179}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.84, "share_ge_25_all": 0.0424, "share_ge_25_pregame_clean": 0.0379}, "WTA": {"median_abs_gap_pregame_clean": 7.58, "share_ge_25_all": 0.0574, "share_ge_25_pregame_clean": 0.0495}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2367, "share_within_10pp_all": 0.4374, "share_within_10pp_pregame_clean": 0.4891, "corr_model_vs_mid_pregame_clean": 0.8503}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 807, "model_brier": 0.1989, "kalshi_brier": 0.1995, "brier_diff_model_minus_kalshi": -0.0005}, "10-15": {"n_settled": 958, "model_brier": 0.2219, "kalshi_brier": 0.2132, "brier_diff_model_minus_kalshi": 0.0087}, "15-25": {"n_settled": 1212, "model_brier": 0.2246, "kalshi_brier": 0.2126, "brier_diff_model_minus_kalshi": 0.012}, "25-40": {"n_settled": 712, "model_brier": 0.2236, "kalshi_brier": 0.2071, "brier_diff_model_minus_kalshi": 0.0165}, "3-5": {"n_settled": 494, "model_brier": 0.2059, "kalshi_brier": 0.2062, "brier_diff_model_minus_kalshi": -0.0003}, "40+": {"n_settled": 149, "model_brier": 0.2799, "kalshi_brier": 0.1899, "brier_diff_model_minus_kalshi": 0.09}, "5-10": {"n_settled": 1145, "model_brier": 0.2013, "kalshi_brier": 0.2016, "brier_diff_model_minus_kalshi": -0.0003}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'NO_SKILL:gen2|WTA', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.532, "slope": 0.801, "slope_se": 0.034}, "kalshi_slope": {"intercept": 0.192, "slope": 1.047, "slope_se": 0.038}, "n": 5477}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.487, "slope": 0.854, "slope_se": 0.027}, "kalshi_slope": {"intercept": 0.166, "slope": 1.054, "slope_se": 0.031}, "n": 7615}, "NO_SKILL:gen2|WTA": {"n_settled": 239, "model_brier": 0.2598, "kalshi_brier": 0.239, "brier_diff_model_minus_kalshi": 0.0208, "brier_diff_se": 0.0101, "corr_model_outcome": 0.2021, "corr_kalshi_outcome": 0.2371}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 497, "model_brier": 0.308, "kalshi_brier": 0.2377, "brier_diff_model_minus_kalshi": 0.0703, "brier_diff_se": 0.0134, "corr_model_outcome": 0.0616, "corr_kalshi_outcome": 0.2343}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
