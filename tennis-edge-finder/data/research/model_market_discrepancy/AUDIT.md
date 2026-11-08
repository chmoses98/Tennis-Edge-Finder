# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-08T07:33Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 81,861): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 19.1%, 25-40 13.6%, 40+ 8.1%; median gap 11.83 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.9%, Challenger 10.7%, doubles 6.8%). Main tour: ATP 3.8% and WTA 6.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 17,754): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.3%, STALE_QUOTE 19.4%, BOOK_QUALITY 17.4%, POOR_DATA 9.1%, POSSIBLY_IN_PLAY_QUOTE 5.8%, IDENTITY_AMBIGUOUS 4.4%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.3%, market_freshness 19.4%, execution 17.4%, data 12.6%, market_freshness/coverage 9.3%, mapping 4.4%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 53.6% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.6% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 17,754 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.7% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 492.0 points vs 1732.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.029, Gen-2 0.824, Gen-1 ledger 0.866 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 910 model 0.2221 vs Kalshi 0.2058; n 189 model 0.295 vs Kalshi 0.1767.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 346,850 model-market comparisons (568,384 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 115,634 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-08T07:13:07.587580+00:00'], shadow board 94,012 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-08T07:13:11.394559+00:00'], Model 4 42,666 rows, 28,943 settled tickers, 10,867 tickers with an external scan.
* By model: {"gen1_ledger": 77902, "gen1_elo": 47247, "fair_v1": 47247, "gen2": 47247, "gen1_sr": 47247, "model4_fundamental": 40022, "model4_conditioned": 39938}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 81,861 | 14.1 | 9.6 | 20.2 | 15.3 | 19.1 | 13.6 | 8.1 | 11.83 | 40.8% | 21.7% |
| MW fair_v1 | 47,247 | 12.9 | 8.7 | 18.7 | 15.4 | 19.6 | 14.8 | 10.0 | 13.04 | 44.4% | 24.8% |
| MW gen1_elo | 47,247 | 12.6 | 8.9 | 19.2 | 15.3 | 19.5 | 14.7 | 9.8 | 12.83 | 44.0% | 24.5% |
| MW gen1_ledger | 34,614 | 15.8 | 10.9 | 22.2 | 15.1 | 18.5 | 12.0 | 5.5 | 10.26 | 35.9% | 17.5% |
| MW gen1_sr | 47,247 | 10.1 | 7.3 | 16.7 | 13.9 | 20.7 | 18.7 | 12.6 | 15.81 | 52.0% | 31.3% |
| MW gen2 | 47,247 | 11.1 | 7.6 | 16.6 | 13.7 | 19.6 | 17.7 | 13.7 | 15.45 | 51.0% | 31.4% |
| all families model4_conditioned | 39,938 | 22.2 | 18.0 | 34.2 | 17.1 | 5.0 | 2.2 | 1.2 | 6.07 | 8.5% | 3.4% |
| all families model4_fundamental | 40,022 | 17.4 | 13.5 | 33.9 | 19.9 | 10.0 | 3.8 | 1.5 | 7.61 | 15.3% | 5.4% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.1%, >=15pp 40.8%, >=20pp 30.0%, >=25pp 21.7%, >=30pp 15.6%, >=40pp 8.1%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.38pp; >=10pp 45.0%, >=25pp 17.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,972 | 28.5 | 15.7 | 27.4 | 13.5 | 10.7 | 3.6 | 0.6 | 5.77 | 14.9% | 4.2% |
| CHALLENGER | 7,089 | 16.2 | 9.7 | 20.7 | 15.3 | 16.0 | 11.4 | 10.8 | 10.91 | 38.1% | 22.1% |
| ITF_MEN | 13,393 | 9.8 | 7.3 | 17.1 | 15.1 | 21.2 | 17.2 | 12.3 | 15.24 | 50.7% | 29.5% |
| ITF_WOMEN | 18,413 | 9.6 | 7.1 | 16.0 | 14.8 | 22.2 | 18.3 | 12.0 | 15.89 | 52.6% | 30.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,047 | 16.8 | 13.2 | 24.6 | 20.9 | 16.6 | 6.8 | 1.1 | 8.66 | 24.5% | 7.9% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,972 | 26.8 | 15.8 | 26.0 | 15.4 | 11.5 | 3.8 | 0.8 | 6.02 | 16.0% | 4.6% |
| CHALLENGER | 7,089 | 14.7 | 9.1 | 18.9 | 13.8 | 18.6 | 13.4 | 11.4 | 12.47 | 43.5% | 24.8% |
| ITF_MEN | 13,393 | 8.2 | 6.1 | 15.1 | 13.7 | 20.0 | 20.4 | 16.4 | 17.94 | 56.9% | 36.9% |
| ITF_WOMEN | 18,413 | 7.9 | 5.8 | 14.1 | 12.8 | 20.7 | 21.2 | 17.5 | 19.09 | 59.4% | 38.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,047 | 14.2 | 10.1 | 21.6 | 16.2 | 22.4 | 12.9 | 2.5 | 11.28 | 37.9% | 15.4% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,972 | 22.9 | 14.2 | 25.3 | 15.6 | 14.8 | 6.1 | 1.2 | 7.1 | 22.0% | 7.2% |
| CHALLENGER | 7,089 | 15.2 | 9.6 | 20.7 | 15.6 | 16.2 | 11.8 | 10.9 | 11.34 | 39.0% | 22.7% |
| ITF_MEN | 13,393 | 9.5 | 7.3 | 17.2 | 14.2 | 21.9 | 17.2 | 12.6 | 15.65 | 51.7% | 29.8% |
| ITF_WOMEN | 18,413 | 9.3 | 6.9 | 16.2 | 15.7 | 22.2 | 18.2 | 11.4 | 15.6 | 51.8% | 29.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,047 | 22.8 | 17.0 | 31.8 | 15.3 | 8.7 | 3.3 | 1.1 | 6.12 | 13.0% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,374 | 27.0 | 19.8 | 29.7 | 12.3 | 8.2 | 2.6 | 0.5 | 5.34 | 11.2% | 3.0% |
| CHALLENGER | 4,586 | 22.5 | 14.5 | 27.5 | 14.8 | 13.4 | 5.7 | 1.5 | 7.07 | 20.6% | 7.2% |
| DOUBLES | 2,579 | 4.8 | 4.5 | 12.8 | 11.0 | 20.3 | 24.4 | 22.0 | 23.31 | 66.8% | 46.5% |
| ITF_MEN | 9,920 | 12.9 | 9.6 | 21.5 | 15.7 | 21.6 | 12.9 | 5.8 | 11.75 | 40.3% | 18.7% |
| ITF_WOMEN | 11,958 | 13.4 | 9.3 | 19.9 | 15.6 | 21.4 | 14.9 | 5.5 | 12.24 | 41.8% | 20.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,792 | 23.8 | 16.1 | 31.4 | 17.0 | 9.0 | 2.6 | 0.2 | 6.54 | 11.8% | 2.8% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,853 | 28.9 | 15.9 | 27.8 | 13.4 | 10.5 | 3.2 | 0.3 | 5.64 | 14.0% | 3.5% |
| CHALLENGER | 5,015 | 20.9 | 12.0 | 25.7 | 18.0 | 16.0 | 5.9 | 1.6 | 8.23 | 23.5% | 7.5% |
| ITF_MEN | 9,763 | 12.0 | 8.7 | 20.7 | 17.3 | 22.0 | 14.0 | 5.2 | 12.35 | 41.3% | 19.2% |
| ITF_WOMEN | 13,535 | 11.4 | 8.6 | 18.9 | 17.1 | 24.1 | 15.1 | 4.8 | 13.18 | 44.1% | 20.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,933 | 17.1 | 13.2 | 25.0 | 21.2 | 16.6 | 6.3 | 0.6 | 8.49 | 23.5% | 6.9% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,853 | 27.1 | 16.1 | 26.2 | 15.3 | 11.4 | 3.4 | 0.4 | 5.96 | 15.2% | 3.8% |
| CHALLENGER | 5,015 | 18.4 | 11.5 | 23.8 | 16.2 | 19.1 | 9.2 | 1.8 | 8.99 | 30.1% | 11.0% |
| ITF_MEN | 9,764 | 9.7 | 7.2 | 17.6 | 16.0 | 21.8 | 18.7 | 9.1 | 14.86 | 49.5% | 27.8% |
| ITF_WOMEN | 13,536 | 8.9 | 6.9 | 16.1 | 14.4 | 22.6 | 20.5 | 10.7 | 16.49 | 53.8% | 31.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,933 | 14.4 | 10.3 | 21.8 | 16.4 | 22.6 | 12.6 | 1.9 | 11.03 | 37.1% | 14.5% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,312 | 27.2 | 19.9 | 29.7 | 12.5 | 7.9 | 2.4 | 0.3 | 5.3 | 10.7% | 2.8% |
| CHALLENGER | 4,054 | 23.8 | 15.4 | 28.6 | 15.0 | 12.8 | 4.0 | 0.4 | 6.59 | 17.2% | 4.3% |
| DOUBLES | 2,417 | 4.7 | 4.6 | 13.0 | 11.1 | 20.1 | 24.4 | 22.1 | 23.23 | 66.6% | 46.4% |
| ITF_MEN | 8,524 | 13.7 | 10.2 | 23.1 | 16.2 | 21.6 | 11.4 | 3.8 | 10.79 | 36.8% | 15.2% |
| ITF_WOMEN | 10,252 | 14.1 | 9.8 | 21.0 | 16.1 | 21.6 | 13.8 | 3.6 | 11.42 | 39.0% | 17.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,729 | 24.1 | 16.5 | 31.4 | 16.9 | 9.0 | 2.0 | 0.1 | 6.43 | 11.1% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,579 | 4.8 | 4.5 | 12.8 | 11.0 | 20.3 | 24.4 | 22.0 | 23.31 | 66.8% | 46.5% |
| singles | 32,035 | 16.6 | 11.4 | 23.0 | 15.5 | 18.3 | 11.0 | 4.2 | 9.72 | 33.5% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 9,749 | 12.7 | 9.1 | 20.0 | 15.5 | 19.6 | 13.9 | 9.2 | 12.6 | 42.7% | 23.1% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 30,727 | 13.4 | 8.7 | 18.7 | 15.2 | 19.2 | 14.8 | 9.9 | 12.9 | 44.0% | 24.7% |
| UNKNOWN | 6,358 | 10.5 | 7.6 | 17.1 | 16.3 | 21.5 | 16.0 | 11.1 | 14.32 | 48.5% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 13,445 | 19.6 | 11.9 | 22.3 | 15.9 | 14.9 | 9.2 | 6.3 | 8.89 | 30.3% | 15.4% |
| B | 5,774 | 12.6 | 8.7 | 19.7 | 15.6 | 19.8 | 12.8 | 10.9 | 12.72 | 43.5% | 23.6% |
| C | 6,689 | 12.0 | 8.8 | 19.5 | 15.6 | 18.7 | 14.6 | 10.8 | 12.99 | 44.1% | 25.4% |
| D | 7,665 | 11.7 | 8.3 | 17.9 | 15.3 | 21.7 | 15.7 | 9.4 | 13.85 | 46.8% | 25.1% |
| F | 13,674 | 7.4 | 5.6 | 14.8 | 14.7 | 23.5 | 20.8 | 13.1 | 17.79 | 57.4% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,309 | 24.6 | 16.1 | 29.1 | 15.0 | 10.6 | 3.4 | 1.2 | 6.36 | 15.2% | 4.6% |
| B | 4,838 | 16.6 | 10.8 | 24.2 | 16.9 | 18.9 | 9.6 | 3.0 | 9.67 | 31.5% | 12.7% |
| C | 6,820 | 11.0 | 7.8 | 19.6 | 14.6 | 21.0 | 15.7 | 10.4 | 13.64 | 47.1% | 26.1% |
| D | 5,181 | 14.5 | 10.1 | 21.4 | 15.3 | 20.8 | 12.5 | 5.3 | 11.19 | 38.6% | 17.8% |
| F | 8,466 | 10.2 | 8.3 | 16.2 | 14.6 | 23.4 | 19.5 | 7.8 | 15.34 | 50.6% | 27.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 15,173 | 17.8 | 10.9 | 21.4 | 15.7 | 15.2 | 10.1 | 8.9 | 9.98 | 34.2% | 18.9% |
| LIMITED | 10,345 | 13.6 | 9.7 | 20.4 | 15.8 | 19.5 | 13.3 | 7.7 | 11.89 | 40.4% | 20.9% |
| POOR | 21,729 | 9.0 | 6.6 | 16.0 | 14.9 | 22.8 | 18.9 | 11.8 | 16.17 | 53.4% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,875 | 23.7 | 17.8 | 33.1 | 15.6 | 6.4 | 2.9 | 0.4 | 5.92 | 9.8% | 3.4% |
| GAME_SPREAD | 6,660 | 22.8 | 15.4 | 32.0 | 16.9 | 8.9 | 3.4 | 0.7 | 6.69 | 13.0% | 4.0% |
| MATCH_WINNER | 34,614 | 15.8 | 10.9 | 22.2 | 15.1 | 18.5 | 12.0 | 5.5 | 10.26 | 35.9% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 16,482 | 27.9 | 16.8 | 30.8 | 12.7 | 9.1 | 2.4 | 0.3 | 5.63 | 11.8% | 2.7% |
| TOTAL_GAMES | 11,247 | 9.8 | 10.9 | 35.6 | 25.9 | 10.7 | 4.2 | 2.9 | 9.18 | 17.8% | 7.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,158 | 24.5 | 28.8 | 33.2 | 8.1 | 4.0 | 1.1 | 0.3 | 4.79 | 5.4% | 1.4% |
| GAME_SPREAD | 9,195 | 47.0 | 16.0 | 24.7 | 7.5 | 2.3 | 1.9 | 0.6 | 3.29 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,585 | 6.6 | 9.9 | 40.2 | 30.2 | 7.4 | 3.3 | 2.4 | 9.21 | 13.1% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,194 | 23.8 | 16.6 | 34.7 | 14.8 | 6.9 | 2.7 | 0.5 | 6.05 | 10.1% | 3.2% |
| GAME_SPREAD | 9,204 | 20.7 | 13.6 | 28.2 | 20.0 | 11.9 | 4.4 | 1.2 | 7.58 | 17.5% | 5.6% |
| TOTAL_GAMES | 16,624 | 10.1 | 10.8 | 36.3 | 24.2 | 11.5 | 4.5 | 2.6 | 9.04 | 18.6% | 7.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 47,247 | 44.4% | 24.8% | 13.04 | 35.3% | 15.0% | 10.67 |
| gen1_elo | 47,247 | 44.0% | 24.5% | 12.83 | 34.8% | 14.8% | 10.49 |
| gen1_sr | 47,247 | 52.0% | 31.3% | 15.81 | 43.9% | 21.5% | 12.97 |
| gen2 | 47,247 | 51.0% | 31.4% | 15.45 | 43.8% | 23.0% | 12.83 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,000 | 15.5 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 27,247 | 10.9 | 7.3 | 16.8 | 14.0 | 19.3 | 16.9 | 14.8 | 15.41 | 51.0% | 31.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 28,082 | 16.4 | 11.2 | 22.8 | 15.2 | 18.0 | 11.5 | 4.9 | 9.88 | 34.3% | 16.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 81,861 | 28082 | 23472 | 30307 | 24.8 | 126.9 | 1451.1 |
| ge_15pp | 33,419 | 9643 | 8361 | 15415 | 28.3 | 434.7 | 1451.1 |
| ge_25pp | 17,754 | 4591 | 3647 | 9516 | 33.1 | 581.7 | 1431.1 |
| lt_10pp | 35,939 | 14161 | 11105 | 10673 | 22.6 | 47.9 | 1421.1 |

Current slate `SL-20261108T073322Z-de92232d`: 225 priced rows, quote age at build {'median': 51.1, 'max': 91.1}, freshness {'STALE': 225}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 50 | 0.0 | 0.0 | 36.0 | 8.0 | 32.0 | 20.0 | 4.0 | 18.34 | 56.0% | 24.0% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,665 | 19.2 | 10.9 | 25.4 | 17.9 | 18.1 | 7.4 | 1.0 | 8.82 | 26.5% | 8.4% |
| KALSHI_LONE_OUTLIER | 30 | 6.7 | 6.7 | 73.3 | 6.7 | 3.3 | 3.3 | 0.0 | 6.16 | 6.7% | 3.3% |
| MARKETS_AGREE | 990 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,097 | 0.0 | 2.2 | 37.3 | 26.4 | 24.0 | 9.2 | 0.9 | 11.81 | 34.1% | 10.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 47,247 | 7861 (16.6%) | 26.7% | 1.0% | {"EXTERNAL_STALE": 4665, "AGREES_WITH_KALSHI": 2097, "ALL_AGREE": 990, "SUPPORTS_MODEL_DIRECTION": 48, "AGREES_WITH_MODEL": 30, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 20,977 | 1980 (9.4%) | 36.1% | 1.5% | {"EXTERNAL_STALE": 1236, "AGREES_WITH_KALSHI": 714, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 11,701 | 614 (5.2%) | 34.2% | 2.1% | {"EXTERNAL_STALE": 391, "AGREES_WITH_KALSHI": 210, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,467 | 584 (10.7%) | 34.8% | 2.2% | {"EXTERNAL_STALE": 368, "AGREES_WITH_KALSHI": 203, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 19,009 | 4486 (23.6%) | 18.5% | 1.0% | {"EXTERNAL_STALE": 2593, "ALL_AGREE": 990, "AGREES_WITH_KALSHI": 830, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 26, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 9,260 | 10.5 | 7.7 | 19.4 | 14.6 | 21.6 | 16.2 | 9.9 | 14.09 | 47.7% | 26.1% |
| 4-10x | 6,327 | 11.2 | 8.5 | 18.4 | 15.2 | 22.1 | 14.3 | 10.2 | 13.85 | 46.7% | 24.5% |
| <2x | 24,122 | 14.9 | 9.8 | 19.7 | 16.0 | 17.6 | 13.1 | 8.9 | 11.57 | 39.6% | 22.0% |
| >=10x | 7,538 | 10.4 | 6.5 | 15.0 | 14.4 | 21.7 | 18.9 | 13.1 | 16.41 | 53.8% | 32.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 12,391 | 12.4 | 8.6 | 19.8 | 16.2 | 19.0 | 13.6 | 10.4 | 12.77 | 43.0% | 24.0% |
| 300-1000 | 10,237 | 11.8 | 8.7 | 17.7 | 15.1 | 20.8 | 16.2 | 9.6 | 13.75 | 46.6% | 25.9% |
| <300 | 14,786 | 8.3 | 5.8 | 15.1 | 14.7 | 23.1 | 19.9 | 13.1 | 17.12 | 56.0% | 32.9% |
| >=3000 | 9,833 | 21.4 | 12.9 | 23.9 | 15.6 | 13.9 | 7.3 | 5.1 | 7.75 | 26.3% | 12.4% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1452 | 0.5486 | 0.4099 | 0.4876 | +0.061 | -0.078 | 0.0011 ± 0.004 |
| ratio 4-10x | 986 | 0.5772 | 0.4327 | 0.4868 | +0.090 | -0.054 | 0.0089 ± 0.0051 |
| ratio <2x | 3548 | 0.5362 | 0.4136 | 0.4369 | +0.099 | -0.023 | 0.0144 ± 0.0024 |
| ratio >=10x | 1215 | 0.566 | 0.3928 | 0.4486 | +0.117 | -0.056 | 0.0141 ± 0.0051 |
| thinner_sample 1000-3000 | 1991 | 0.5396 | 0.4121 | 0.4485 | +0.091 | -0.036 | 0.0113 ± 0.0033 |
| thinner_sample 300-1000 | 1637 | 0.564 | 0.4239 | 0.4734 | +0.091 | -0.050 | 0.0049 ± 0.0038 |
| thinner_sample <300 | 2321 | 0.5585 | 0.3907 | 0.4554 | +0.103 | -0.065 | 0.0126 ± 0.0037 |
| thinner_sample >=3000 | 1252 | 0.5287 | 0.4354 | 0.4457 | +0.083 | -0.010 | 0.0152 ± 0.0032 |
| data_status ADEQUATE | 2000 | 0.5316 | 0.4288 | 0.44 | +0.092 | -0.011 | 0.0154 ± 0.0027 |
| data_status LIMITED | 1761 | 0.5478 | 0.4151 | 0.4673 | +0.080 | -0.052 | 0.0072 ± 0.0036 |
| data_status POOR | 3440 | 0.5605 | 0.4005 | 0.4593 | +0.101 | -0.059 | 0.0103 ± 0.0029 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1043 | 0.1975 | 0.1978 | -0.0003 ± 0.0005 | 0.575 | 0.5757 | 0.5022 | 0.487 | 0.5005 | -0.092 ± 0.0146 | -0.0087 (8) |
| 3-5 | 663 | 0.205 | 0.2049 | +0.0001 ± 0.0014 | 0.5948 | 0.5927 | 0.5049 | 0.4651 | 0.4827 | -0.096 ± 0.018 | 0.01 (3) |
| 5-10 | 1549 | 0.2021 | 0.201 | +0.0010 ± 0.0017 | 0.5907 | 0.5858 | 0.5117 | 0.438 | 0.4655 | -0.091 ± 0.0118 | -0.0143 (7) |
| 10-15 | 1250 | 0.2182 | 0.2093 | +0.0089 ± 0.0032 | 0.6283 | 0.6022 | 0.5234 | 0.3999 | 0.4248 | -0.103 ± 0.0131 | -0.055 (6) |
| 15-25 | 1597 | 0.2261 | 0.208 | +0.0181 ± 0.0044 | 0.6473 | 0.5995 | 0.5756 | 0.381 | 0.4314 | -0.105 ± 0.0115 | -0.0045 (11) |
| 25-40 | 910 | 0.2221 | 0.2058 | +0.0163 ± 0.009 | 0.6339 | 0.5926 | 0.6516 | 0.3418 | 0.4703 | -0.065 ± 0.0138 | -0.06 (2) |
| 40+ | 189 | 0.295 | 0.1767 | +0.1183 ± 0.0274 | 0.7946 | 0.5268 | 0.7316 | 0.2768 | 0.381 | -0.081 ± 0.0265 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5440 | 0.1853 | 0.1862 | -0.0009 ± 0.0002 | 0.5466 | 0.5477 | 0.4902 | 0.4749 | 0.5072 | -0.020 ± 0.0059 | -0.01 (28) |
| 3-5 | 3625 | 0.1978 | 0.1961 | +0.0017 ± 0.0006 | 0.5762 | 0.5699 | 0.4828 | 0.4431 | 0.4414 | -0.056 ± 0.0074 | 0.005 (6) |
| 5-10 | 7860 | 0.2013 | 0.1978 | +0.0034 ± 0.0007 | 0.5884 | 0.5767 | 0.4847 | 0.411 | 0.4248 | -0.045 ± 0.0051 | -0.0114 (22) |
| 10-15 | 6486 | 0.2021 | 0.1862 | +0.0159 ± 0.0013 | 0.5908 | 0.5462 | 0.4854 | 0.3614 | 0.3597 | -0.063 ± 0.0054 | -0.0379 (19) |
| 15-25 | 8220 | 0.2064 | 0.1669 | +0.0395 ± 0.0018 | 0.6048 | 0.496 | 0.4996 | 0.3041 | 0.3015 | -0.070 ± 0.0045 | -0.0043 (51) |
| 25-40 | 6334 | 0.2226 | 0.1264 | +0.0962 ± 0.0028 | 0.6393 | 0.3883 | 0.527 | 0.2133 | 0.221 | -0.058 ± 0.0043 | -0.0733 (3) |
| 40+ | 4222 | 0.3829 | 0.0438 | +0.3391 ± 0.0037 | 0.9974 | 0.1703 | 0.6311 | 0.1016 | 0.058 | -0.076 ± 0.003 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 834 | 0.205 | 0.2053 | -0.0003 ± 0.0005 | 0.5907 | 0.5918 | 0.5068 | 0.492 | 0.5132 | -0.103 ± 0.0168 | -0.0117 (6) |
| 3-5 | 594 | 0.2116 | 0.2086 | +0.0029 ± 0.0015 | 0.6062 | 0.5998 | 0.5138 | 0.4743 | 0.4529 | -0.130 ± 0.0201 | 0.01 (3) |
| 5-10 | 1334 | 0.2066 | 0.2046 | +0.0020 ± 0.0019 | 0.5994 | 0.5941 | 0.5403 | 0.4658 | 0.4925 | -0.089 ± 0.0128 | -0.01 (4) |
| 10-15 | 1159 | 0.2132 | 0.2071 | +0.0061 ± 0.0034 | 0.6192 | 0.6003 | 0.5626 | 0.4382 | 0.4789 | -0.100 ± 0.014 | -0.04 (5) |
| 15-25 | 1683 | 0.232 | 0.2122 | +0.0198 ± 0.0044 | 0.6598 | 0.6089 | 0.5849 | 0.3894 | 0.4379 | -0.100 ± 0.0115 | -0.0183 (12) |
| 25-40 | 1178 | 0.2658 | 0.1984 | +0.0675 ± 0.0081 | 0.7419 | 0.5769 | 0.6597 | 0.3455 | 0.3973 | -0.116 ± 0.013 | -0.008 (5) |
| 40+ | 419 | 0.3714 | 0.1626 | +0.2088 ± 0.0197 | 1.0125 | 0.4913 | 0.7356 | 0.2469 | 0.2912 | -0.087 ± 0.0189 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4652 | 0.192 | 0.1921 | -0.0002 ± 0.0002 | 0.5597 | 0.5598 | 0.5075 | 0.4924 | 0.5073 | -0.040 ± 0.0066 | -0.0154 (26) |
| 3-5 | 3180 | 0.1928 | 0.1917 | +0.0011 ± 0.0006 | 0.5623 | 0.5587 | 0.5116 | 0.472 | 0.4767 | -0.047 ± 0.008 | 0.01 (5) |
| 5-10 | 7016 | 0.1969 | 0.1935 | +0.0034 ± 0.0008 | 0.5788 | 0.5663 | 0.5088 | 0.4347 | 0.4513 | -0.040 ± 0.0053 | -0.0117 (6) |
| 10-15 | 5821 | 0.2029 | 0.1917 | +0.0112 ± 0.0014 | 0.5953 | 0.5606 | 0.5105 | 0.3866 | 0.4044 | -0.047 ± 0.0058 | -0.0189 (18) |
| 15-25 | 8275 | 0.2172 | 0.1814 | +0.0357 ± 0.0018 | 0.6314 | 0.532 | 0.5255 | 0.33 | 0.3389 | -0.059 ± 0.0047 | -0.014 (52) |
| 25-40 | 7437 | 0.2507 | 0.1378 | +0.1129 ± 0.0027 | 0.7082 | 0.4208 | 0.5604 | 0.2434 | 0.2274 | -0.079 ± 0.0043 | -0.0095 (20) |
| 40+ | 5806 | 0.4017 | 0.0583 | +0.3434 ± 0.0037 | 1.0586 | 0.2106 | 0.6542 | 0.1183 | 0.0794 | -0.074 ± 0.0031 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1016 | 0.1957 | 0.1971 | -0.0014 ± 0.0005 | 0.5712 | 0.5746 | 0.5027 | 0.4873 | 0.5325 | -0.051 ± 0.0145 | -0.0191 (11) |
| 3-5 | 716 | 0.2078 | 0.2063 | +0.0016 ± 0.0014 | 0.6024 | 0.5969 | 0.4982 | 0.4587 | 0.4609 | -0.110 ± 0.0177 | 0.002 (5) |
| 5-10 | 1580 | 0.2026 | 0.199 | +0.0036 ± 0.0017 | 0.5903 | 0.5802 | 0.5126 | 0.4388 | 0.4506 | -0.104 ± 0.0116 | -0.01 (10) |
| 10-15 | 1263 | 0.2113 | 0.2024 | +0.0090 ± 0.0031 | 0.6132 | 0.5872 | 0.537 | 0.4137 | 0.441 | -0.106 ± 0.0127 | -0.0286 (7) |
| 15-25 | 1529 | 0.2319 | 0.2126 | +0.0192 ± 0.0046 | 0.6614 | 0.6096 | 0.586 | 0.3919 | 0.4388 | -0.109 ± 0.0118 | -0.03 (1) |
| 25-40 | 899 | 0.2117 | 0.21 | +0.0017 ± 0.009 | 0.6118 | 0.6024 | 0.6595 | 0.3486 | 0.4994 | -0.053 ± 0.0138 | -0.0267 (3) |
| 40+ | 198 | 0.3082 | 0.1841 | +0.1242 ± 0.0273 | 0.8344 | 0.5426 | 0.7433 | 0.2886 | 0.3889 | -0.085 ± 0.028 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5242 | 0.1853 | 0.186 | -0.0007 ± 0.0002 | 0.5462 | 0.547 | 0.486 | 0.4707 | 0.4903 | -0.032 ± 0.006 | -0.0189 (44) |
| 3-5 | 3744 | 0.2039 | 0.2022 | +0.0018 ± 0.0006 | 0.593 | 0.5868 | 0.4798 | 0.4403 | 0.4383 | -0.056 ± 0.0075 | -0.0073 (22) |
| 5-10 | 8004 | 0.1959 | 0.1906 | +0.0053 ± 0.0007 | 0.5751 | 0.5587 | 0.4875 | 0.4135 | 0.4153 | -0.056 ± 0.0049 | -0.0117 (42) |
| 10-15 | 6434 | 0.1938 | 0.1787 | +0.0151 ± 0.0013 | 0.5725 | 0.5288 | 0.4947 | 0.3713 | 0.3716 | -0.062 ± 0.0053 | -0.0136 (14) |
| 15-25 | 8309 | 0.2123 | 0.1725 | +0.0397 ± 0.0018 | 0.6185 | 0.5088 | 0.5126 | 0.3181 | 0.314 | -0.071 ± 0.0045 | -0.0533 (3) |
| 25-40 | 6279 | 0.2163 | 0.1273 | +0.0890 ± 0.0028 | 0.6259 | 0.3899 | 0.5292 | 0.2136 | 0.2325 | -0.048 ± 0.0043 | -0.02 (4) |
| 40+ | 4175 | 0.3918 | 0.0488 | +0.3430 ± 0.0039 | 1.0211 | 0.1828 | 0.6402 | 0.1078 | 0.0649 | -0.076 ± 0.0033 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1451 | 0.1979 | 0.1979 | -0.0000 ± 0.0004 | 0.5744 | 0.5743 | 0.5082 | 0.4931 | 0.4969 | -0.069 ± 0.0119 | -0.0221 (56) |
| 3-5 | 1043 | 0.1881 | 0.1881 | +0.0000 ± 0.0011 | 0.5542 | 0.5524 | 0.4971 | 0.4572 | 0.4756 | -0.055 ± 0.0137 | -0.0194 (34) |
| 5-10 | 2100 | 0.1996 | 0.1948 | +0.0048 ± 0.0014 | 0.589 | 0.5729 | 0.5077 | 0.4341 | 0.439 | -0.076 ± 0.0099 | -0.005 (78) |
| 10-15 | 1448 | 0.2144 | 0.2019 | +0.0125 ± 0.0029 | 0.6223 | 0.5873 | 0.5424 | 0.4195 | 0.4289 | -0.089 ± 0.0121 | 0.0012 (66) |
| 15-25 | 1882 | 0.2313 | 0.2073 | +0.0240 ± 0.0041 | 0.66 | 0.5985 | 0.5911 | 0.3962 | 0.4341 | -0.089 ± 0.0106 | -0.0214 (59) |
| 25-40 | 1134 | 0.2397 | 0.2105 | +0.0292 ± 0.0083 | 0.6848 | 0.6039 | 0.6887 | 0.3767 | 0.4859 | -0.086 ± 0.0128 | -0.0252 (27) |
| 40+ | 406 | 0.3251 | 0.2014 | +0.1237 ± 0.0213 | 0.9355 | 0.5865 | 0.8176 | 0.3414 | 0.4655 | -0.097 ± 0.0198 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5347 | 0.1778 | 0.1779 | -0.0001 ± 0.0002 | 0.5261 | 0.5258 | 0.5116 | 0.4963 | 0.5057 | -0.039 ± 0.0058 | -0.0154 (103) |
| 3-5 | 3701 | 0.1948 | 0.194 | +0.0007 ± 0.0006 | 0.5684 | 0.5662 | 0.5016 | 0.4618 | 0.4731 | -0.039 ± 0.0073 | -0.0212 (73) |
| 5-10 | 7516 | 0.1963 | 0.1898 | +0.0064 ± 0.0008 | 0.5797 | 0.5599 | 0.5015 | 0.4279 | 0.4223 | -0.061 ± 0.0051 | -0.0084 (134) |
| 10-15 | 5145 | 0.2099 | 0.1935 | +0.0164 ± 0.0015 | 0.611 | 0.5677 | 0.5373 | 0.4144 | 0.408 | -0.072 ± 0.0062 | -0.0057 (111) |
| 15-25 | 6257 | 0.2316 | 0.1999 | +0.0318 ± 0.0022 | 0.6653 | 0.5792 | 0.5767 | 0.3813 | 0.3986 | -0.068 ± 0.0057 | -0.026 (108) |
| 25-40 | 4087 | 0.2566 | 0.1906 | +0.0660 ± 0.0043 | 0.7263 | 0.5548 | 0.6407 | 0.3282 | 0.3817 | -0.064 ± 0.0067 | -0.0277 (53) |
| 40+ | 1810 | 0.3703 | 0.1593 | +0.2111 ± 0.0097 | 1.0448 | 0.4745 | 0.7458 | 0.2448 | 0.295 | -0.064 ± 0.0089 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7201 | 1.029 ± 0.033 | 1.1 | 0.169 | 0.1686 | 0.2148 | 0.2039 |
| gen2 | 7201 | 0.824 ± 0.03 | 1.071 | 0.1735 | 0.1689 | 0.2331 | 0.2037 |
| gen1_elo | 7201 | 1.011 ± 0.032 | 1.09 | 0.1754 | 0.1687 | 0.2139 | 0.2039 |
| gen1_sr | 7201 | 1.01 ± 0.039 | 1.129 | 0.1334 | 0.1706 | 0.2292 | 0.2034 |
| gen1_ledger | 9464 | 0.866 ± 0.024 | 1.077 | 0.1898 | 0.1756 | 0.2168 | 0.2003 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 33,419)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 7,728 | 23.1% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,587 | 22.7% |
| BOOK_QUALITY | execution | 5,969 | 17.9% |
| POOR_DATA | data | 3,855 | 11.5% |
| LIMITED_DATA | data | 2,076 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,929 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 1,396 | 4.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,372 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 956 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 550 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 23.1%, coverage 22.7%, execution 17.9%, data 17.8%, market_freshness/coverage 8.6%, mapping 4.2%, model_calibration_or_unknown 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.6%, LOW_DATA_QUALITY 71.5%, THIN_PLAYER_HISTORY 59.7%, STALE_PLAYER_DATA 52.0%, STALE_KALSHI_QUOTE 46.1%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 24.1%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 15.3%, LEVEL_TRANSFER_RISK 10.0%, LOW_DISPLAYED_LIQUIDITY 8.3%, EVENT_MAPPING_RISK 7.2%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.1%, POST_SETTLEMENT_OBSERVATION 22.7%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 17,754)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,082 | 34.3% |
| STALE_QUOTE | market_freshness | 3,440 | 19.4% |
| BOOK_QUALITY | execution | 3,096 | 17.4% |
| POOR_DATA | data | 1,621 | 9.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,028 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 776 | 4.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 627 | 3.5% |
| LIMITED_DATA | data | 609 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 339 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 135 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.3%, market_freshness 19.4%, execution 17.4%, data 12.6%, market_freshness/coverage 9.3%, mapping 4.4%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 74.8%, THIN_PLAYER_HISTORY 61.6%, STALE_KALSHI_QUOTE 53.6%, STALE_PLAYER_DATA 45.7%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 34.2%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 19.3%, PLAYER_IDENTITY_RISK 18.4%, EVENT_MAPPING_RISK 8.9%, LEVEL_TRANSFER_RISK 8.8%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.3%, POST_SETTLEMENT_OBSERVATION 34.3%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 14162, "IDENTITY_AMBIGUOUS": 3592}; ticker orientation: {"VERIFIED": 17754}.

Checks: discipline:AMBIGUOUS 1198, discipline:PASS 16556, identity_confidence:AMBIGUOUS 3261, identity_confidence:PASS 14493, level_mapping:NA 1210, level_mapping:PASS 16544, market_pair:AMBIGUOUS 492, market_pair:NA 397, market_pair:PASS 16865, model_complement:NA 359, model_complement:PASS 17395, namesake:AMBIGUOUS 6, namesake:PASS 17748, physical_match_id:NA 6053, physical_match_id:PASS 11701, player_ids:PASS 17754, same_pair_other_event:PASS 17754, ticker_orientation:PASS 17754

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,346 | 3.8% | 3.2% | 1.4% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 21, "market_freshness/coverage": 19} | 5.52 | 0.2235 / 0.2186 (817) | 24.8% | 2.5% | 3.1% | 2.9% |
| CHALLENGER | 11,675 | 16.2% | 6.1% | 10.7% | {"coverage": 1125, "market_freshness": 221, "market_freshness/coverage": 220, "data": 158, "model_calibration_or_unknown": 78, "execution": 41, "model_calibration": 36, "mapping": 17, "possible_market_error": 1} | 7.36 | 0.2205 / 0.2101 (2752) | 38.0% | 15.1% | 4.0% | 22.3% |
| DOUBLES | 2,579 | 46.5% | 46.4% | 6.8% | {"execution": 665, "mapping": 351, "market_freshness": 106, "market_freshness/coverage": 69, "coverage": 7} | 23.23 | 0.298 / 0.2322 (644) | 9.1% | 0.0% | 100.0% | 6.3% |
| ITF_MEN | 23,313 | 24.9% | 17.3% | 32.7% | {"coverage": 2043, "market_freshness": 1124, "execution": 981, "data": 849, "market_freshness/coverage": 589, "mapping": 204, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.64 | 0.2175 / 0.1995 (4956) | 40.0% | 68.7% | 15.1% | 21.6% |
| ITF_WOMEN | 30,371 | 26.4% | 18.9% | 45.2% | {"coverage": 2831, "market_freshness": 1728, "execution": 1326, "data": 1122, "market_freshness/coverage": 701, "mapping": 198, "model_calibration_or_unknown": 94, "model_calibration": 23} | 12.5 | 0.2023 / 0.1938 (5892) | 41.1% | 57.1% | 9.9% | 21.7% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,839 | 6.0% | 5.1% | 1.6% | {"market_freshness": 111, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.67 | 0.2296 / 0.2199 (792) | 29.9% | 2.0% | 1.3% | 3.7% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.7% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 404 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 519 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 17.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 1025 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 852 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 164 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 12 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 899 min (STALE); no external reference |
| 15 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 18 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 17.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1037 min (STALE); no external reference |
| 19 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 20 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 21 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 22 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 23 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 24 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 25 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 454 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 26 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 27 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 28 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 29 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 30 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 31 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 32 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 33 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 34 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 35 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 36 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 37 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 38 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 39 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 40 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 41 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 43 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 44 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 45 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 46 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 77 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 49 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 50 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.3h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 748 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9701, "by_level_share_of_ge_25pp": {"ATP": 0.0135, "CHALLENGER": 0.1068, "DOUBLES": 0.0675, "ITF_MEN": 0.3267, "ITF_WOMEN": 0.4519, "OTHER": 0.0007, "WTA": 0.0164, "WTA125": 0.0165}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.536, "share_primary_cause_market_settled_or_in_play": 0.4358, "share_primary_cause_stale_quote_only": 0.1938}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 17754, "identity_ambiguous_share": 0.2023, "ticker_orientation": {"VERIFIED": 17754}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 11701, "with_external": 614, "coverage": 0.0525, "external_status": {"EXTERNAL_STALE": 391, "AGREES_WITH_KALSHI": 210, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 391, "MODEL_LONE_OUTLIER": 210, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.342, "share_external_supports_model": 0.0212}, "pregame_clean_ge_25pp": {"n": 5467, "with_external": 584, "coverage": 0.1068, "external_status": {"EXTERNAL_STALE": 368, "AGREES_WITH_KALSHI": 203, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 368, "MODEL_LONE_OUTLIER": 203, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3476, "share_external_supports_model": 0.0223}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 492.0, "median_sample_ratio": 2.46, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2088, "data_status": {"POOR": 9931, "LIMITED": 4614, "ADEQUATE": 3209}, "comparison_lt_10pp": {"median_thinner_serve_points": 1732.0, "median_sample_ratio": 1.7, "median_min_matches": 90.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1452, "model_minus_observed": 0.061, "kalshi_minus_observed": -0.0777, "brier_diff_model_minus_kalshi": 0.0011}, "4-10x": {"n": 986, "model_minus_observed": 0.0904, "kalshi_minus_observed": -0.0541, "brier_diff_model_minus_kalshi": 0.0089}, "<2x": {"n": 3548, "model_minus_observed": 0.0994, "kalshi_minus_observed": -0.0233, "brier_diff_model_minus_kalshi": 0.0144}, ">=10x": {"n": 1215, "model_minus_observed": 0.1175, "kalshi_minus_observed": -0.0557, "brier_diff_model_minus_kalshi": 0.0141}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 7201, "model": {"intercept": -0.556, "slope": 0.824, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.18, "slope": 1.071, "slope_se": 0.033}, "mean_extremity_model": 0.1735, "mean_extremity_kalshi": 0.1689, "model_brier": 0.2331, "kalshi_brier": 0.2037, "brier_diff_model_minus_kalshi": 0.0294, "brier_diff_se": 0.0022, "model_logloss": 0.6636, "kalshi_logloss": 0.59}, "fair_v1": {"n": 7201, "model": {"intercept": -0.449, "slope": 1.029, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.247, "slope": 1.1, "slope_se": 0.034}, "mean_extremity_model": 0.169, "mean_extremity_kalshi": 0.1686, "model_brier": 0.2148, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0109, "brier_diff_se": 0.0018, "model_logloss": 0.6187, "kalshi_logloss": 0.5902}, "gen1_elo": {"n": 7201, "model": {"intercept": -0.439, "slope": 1.011, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.247, "slope": 1.09, "slope_se": 0.033}, "mean_extremity_model": 0.1754, "mean_extremity_kalshi": 0.1687, "model_brier": 0.2139, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.01, "brier_diff_se": 0.0018, "model_logloss": 0.6173, "kalshi_logloss": 0.5903}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2477, "share_ge_15": 0.444, "median_abs_gap": 13.04, "n": 47247}, "gen1_elo": {"share_ge_25": 0.2448, "share_ge_15": 0.44, "median_abs_gap": 12.83, "n": 47247}, "gen1_sr": {"share_ge_25": 0.3131, "share_ge_15": 0.52, "median_abs_gap": 15.81, "n": 47247}, "gen2": {"share_ge_25": 0.3138, "share_ge_15": 0.5102, "median_abs_gap": 15.45, "n": 47247}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1502, "share_ge_15": 0.353, "median_abs_gap": 10.67, "n": 36383}, "gen1_elo": {"share_ge_25": 0.1482, "share_ge_15": 0.3481, "median_abs_gap": 10.49, "n": 36383}, "gen1_sr": {"share_ge_25": 0.2154, "share_ge_15": 0.4387, "median_abs_gap": 12.97, "n": 36385}, "gen2": {"share_ge_25": 0.2303, "share_ge_15": 0.4382, "median_abs_gap": 12.83, "n": 36385}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.52, "share_ge_25_all": 0.0377, "share_ge_25_pregame_clean": 0.0323}, "WTA": {"median_abs_gap_pregame_clean": 7.67, "share_ge_25_all": 0.0601, "share_ge_25_pregame_clean": 0.0511}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.237, "share_within_10pp_all": 0.439, "share_within_10pp_pregame_clean": 0.4922, "corr_model_vs_mid_pregame_clean": 0.851}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1043, "model_brier": 0.1975, "kalshi_brier": 0.1978, "brier_diff_model_minus_kalshi": -0.0003}, "10-15": {"n_settled": 1250, "model_brier": 0.2182, "kalshi_brier": 0.2093, "brier_diff_model_minus_kalshi": 0.0089}, "15-25": {"n_settled": 1597, "model_brier": 0.2261, "kalshi_brier": 0.208, "brier_diff_model_minus_kalshi": 0.0181}, "25-40": {"n_settled": 910, "model_brier": 0.2221, "kalshi_brier": 0.2058, "brier_diff_model_minus_kalshi": 0.0163}, "3-5": {"n_settled": 663, "model_brier": 0.205, "kalshi_brier": 0.2049, "brier_diff_model_minus_kalshi": 0.0001}, "40+": {"n_settled": 189, "model_brier": 0.295, "kalshi_brier": 0.1767, "brier_diff_model_minus_kalshi": 0.1183}, "5-10": {"n_settled": 1549, "model_brier": 0.2021, "kalshi_brier": 0.201, "brier_diff_model_minus_kalshi": 0.001}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.556, "slope": 0.824, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.18, "slope": 1.071, "slope_se": 0.033}, "n": 7201}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.486, "slope": 0.866, "slope_se": 0.024}, "kalshi_slope": {"intercept": 0.174, "slope": 1.077, "slope_se": 0.028}, "n": 9464}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 644, "model_brier": 0.298, "kalshi_brier": 0.2322, "brier_diff_model_minus_kalshi": 0.0658, "brier_diff_se": 0.0115, "corr_model_outcome": 0.1011, "corr_kalshi_outcome": 0.2821}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
