# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-08T14:36Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 82,038): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 19.1%, 25-40 13.6%, 40+ 8.1%; median gap 11.83 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.8%, Challenger 10.8%, doubles 6.7%). Main tour: ATP 3.8% and WTA 6.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 17,803): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.3%, STALE_QUOTE 19.4%, BOOK_QUALITY 17.4%, POOR_DATA 9.1%, POSSIBLY_IN_PLAY_QUOTE 5.8%, IDENTITY_AMBIGUOUS 4.4%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.3%, market_freshness 19.4%, execution 17.4%, data 12.6%, market_freshness/coverage 9.3%, mapping 4.4%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 53.6% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.6% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 17,803 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.6% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 494.0 points vs 1733.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.029, Gen-2 0.822, Gen-1 ledger 0.867 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 914 model 0.222 vs Kalshi 0.2058; n 189 model 0.295 vs Kalshi 0.1767.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 347,652 model-market comparisons (569,653 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 115,925 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-08T14:16:02.690679+00:00'], shadow board 94,212 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-08T14:16:06.631182+00:00'], Model 4 42,757 rows, 29,034 settled tickers, 10,902 tickers with an external scan.
* By model: {"gen1_ledger": 78114, "gen1_elo": 47349, "fair_v1": 47349, "gen2": 47349, "gen1_sr": 47349, "model4_fundamental": 40113, "model4_conditioned": 40029}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 82,038 | 14.1 | 9.6 | 20.2 | 15.3 | 19.1 | 13.6 | 8.1 | 11.83 | 40.8% | 21.7% |
| MW fair_v1 | 47,349 | 12.8 | 8.7 | 18.7 | 15.4 | 19.6 | 14.8 | 10.0 | 13.04 | 44.4% | 24.8% |
| MW gen1_elo | 47,349 | 12.6 | 8.9 | 19.2 | 15.3 | 19.5 | 14.7 | 9.8 | 12.83 | 44.0% | 24.5% |
| MW gen1_ledger | 34,689 | 15.8 | 10.9 | 22.2 | 15.1 | 18.5 | 12.0 | 5.5 | 10.26 | 36.0% | 17.5% |
| MW gen1_sr | 47,349 | 10.1 | 7.3 | 16.7 | 13.9 | 20.7 | 18.7 | 12.6 | 15.82 | 52.0% | 31.3% |
| MW gen2 | 47,349 | 11.0 | 7.5 | 16.6 | 13.7 | 19.6 | 17.7 | 13.7 | 15.46 | 51.0% | 31.4% |
| all families model4_conditioned | 40,029 | 22.3 | 18.0 | 34.2 | 17.1 | 5.0 | 2.2 | 1.2 | 6.07 | 8.5% | 3.4% |
| all families model4_fundamental | 40,113 | 17.4 | 13.5 | 33.8 | 19.9 | 10.0 | 3.8 | 1.5 | 7.61 | 15.3% | 5.4% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.1%, >=15pp 40.8%, >=20pp 30.1%, >=25pp 21.7%, >=30pp 15.6%, >=40pp 8.1%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.38pp; >=10pp 45.0%, >=25pp 17.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,982 | 28.5 | 15.7 | 27.4 | 13.5 | 10.7 | 3.6 | 0.6 | 5.77 | 14.9% | 4.2% |
| CHALLENGER | 7,118 | 16.1 | 9.7 | 20.7 | 15.3 | 16.0 | 11.4 | 10.8 | 10.93 | 38.2% | 22.2% |
| ITF_MEN | 13,410 | 9.8 | 7.3 | 17.1 | 15.1 | 21.2 | 17.2 | 12.3 | 15.25 | 50.7% | 29.5% |
| ITF_WOMEN | 18,456 | 9.5 | 7.1 | 16.0 | 14.8 | 22.2 | 18.4 | 12.0 | 15.89 | 52.6% | 30.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,050 | 16.8 | 13.2 | 24.7 | 20.9 | 16.6 | 6.8 | 1.1 | 8.67 | 24.5% | 7.9% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,982 | 26.8 | 15.8 | 26.0 | 15.4 | 11.5 | 3.8 | 0.8 | 6.03 | 16.1% | 4.6% |
| CHALLENGER | 7,118 | 14.6 | 9.1 | 18.9 | 13.8 | 18.7 | 13.5 | 11.4 | 12.49 | 43.6% | 24.9% |
| ITF_MEN | 13,410 | 8.2 | 6.1 | 15.1 | 13.7 | 20.0 | 20.4 | 16.4 | 17.94 | 56.9% | 36.9% |
| ITF_WOMEN | 18,456 | 7.9 | 5.8 | 14.1 | 12.8 | 20.7 | 21.2 | 17.5 | 19.09 | 59.4% | 38.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,050 | 14.1 | 10.1 | 21.6 | 16.3 | 22.5 | 12.9 | 2.5 | 11.28 | 37.9% | 15.4% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,982 | 23.0 | 14.2 | 25.2 | 15.6 | 14.8 | 6.0 | 1.2 | 7.1 | 22.0% | 7.2% |
| CHALLENGER | 7,118 | 15.1 | 9.6 | 20.6 | 15.6 | 16.2 | 11.9 | 10.9 | 11.37 | 39.1% | 22.8% |
| ITF_MEN | 13,410 | 9.5 | 7.3 | 17.2 | 14.2 | 21.9 | 17.2 | 12.7 | 15.65 | 51.7% | 29.9% |
| ITF_WOMEN | 18,456 | 9.3 | 6.9 | 16.2 | 15.7 | 22.2 | 18.3 | 11.4 | 15.6 | 51.8% | 29.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,050 | 22.8 | 17.1 | 31.8 | 15.3 | 8.7 | 3.3 | 1.1 | 6.12 | 13.0% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,384 | 27.1 | 19.7 | 29.6 | 12.3 | 8.2 | 2.6 | 0.5 | 5.33 | 11.2% | 3.1% |
| CHALLENGER | 4,605 | 22.5 | 14.5 | 27.6 | 14.8 | 13.5 | 5.7 | 1.5 | 7.08 | 20.7% | 7.2% |
| DOUBLES | 2,581 | 4.8 | 4.5 | 12.8 | 11.0 | 20.3 | 24.4 | 22.0 | 23.31 | 66.8% | 46.5% |
| ITF_MEN | 9,931 | 12.9 | 9.6 | 21.5 | 15.7 | 21.6 | 12.9 | 5.8 | 11.76 | 40.3% | 18.7% |
| ITF_WOMEN | 11,988 | 13.4 | 9.2 | 19.9 | 15.6 | 21.5 | 14.9 | 5.5 | 12.24 | 41.8% | 20.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,795 | 23.7 | 16.1 | 31.4 | 17.0 | 9.0 | 2.6 | 0.2 | 6.53 | 11.8% | 2.8% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,863 | 28.9 | 15.8 | 27.8 | 13.4 | 10.5 | 3.2 | 0.3 | 5.64 | 14.0% | 3.5% |
| CHALLENGER | 5,032 | 20.8 | 12.0 | 25.6 | 18.1 | 16.0 | 6.0 | 1.6 | 8.25 | 23.5% | 7.6% |
| ITF_MEN | 9,773 | 12.1 | 8.7 | 20.7 | 17.3 | 22.0 | 14.0 | 5.2 | 12.35 | 41.3% | 19.2% |
| ITF_WOMEN | 13,561 | 11.4 | 8.6 | 18.9 | 17.1 | 24.1 | 15.1 | 4.8 | 13.18 | 44.1% | 20.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,936 | 17.1 | 13.2 | 25.0 | 21.2 | 16.6 | 6.3 | 0.6 | 8.5 | 23.5% | 6.9% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,863 | 27.1 | 16.1 | 26.2 | 15.3 | 11.4 | 3.4 | 0.4 | 5.96 | 15.2% | 3.8% |
| CHALLENGER | 5,032 | 18.4 | 11.4 | 23.7 | 16.2 | 19.1 | 9.3 | 1.8 | 8.99 | 30.2% | 11.1% |
| ITF_MEN | 9,774 | 9.6 | 7.2 | 17.6 | 16.0 | 21.8 | 18.7 | 9.1 | 14.86 | 49.5% | 27.7% |
| ITF_WOMEN | 13,562 | 8.9 | 6.9 | 16.1 | 14.4 | 22.6 | 20.5 | 10.7 | 16.49 | 53.8% | 31.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,936 | 14.4 | 10.2 | 21.8 | 16.4 | 22.6 | 12.6 | 1.9 | 11.08 | 37.1% | 14.5% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,322 | 27.4 | 19.9 | 29.6 | 12.5 | 7.9 | 2.5 | 0.3 | 5.29 | 10.7% | 2.8% |
| CHALLENGER | 4,072 | 23.8 | 15.3 | 28.7 | 15.0 | 12.8 | 4.0 | 0.4 | 6.6 | 17.2% | 4.4% |
| DOUBLES | 2,419 | 4.7 | 4.6 | 13.0 | 11.1 | 20.2 | 24.4 | 22.0 | 23.23 | 66.6% | 46.4% |
| ITF_MEN | 8,533 | 13.7 | 10.2 | 23.1 | 16.2 | 21.6 | 11.4 | 3.8 | 10.79 | 36.8% | 15.2% |
| ITF_WOMEN | 10,281 | 14.1 | 9.8 | 21.0 | 16.1 | 21.6 | 13.8 | 3.6 | 11.42 | 39.0% | 17.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,732 | 24.1 | 16.5 | 31.4 | 17.0 | 8.9 | 2.0 | 0.1 | 6.43 | 11.0% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,581 | 4.8 | 4.5 | 12.8 | 11.0 | 20.3 | 24.4 | 22.0 | 23.31 | 66.8% | 46.5% |
| singles | 32,108 | 16.6 | 11.4 | 23.0 | 15.5 | 18.3 | 11.0 | 4.2 | 9.72 | 33.5% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 9,771 | 12.7 | 9.1 | 19.9 | 15.6 | 19.6 | 13.9 | 9.2 | 12.6 | 42.8% | 23.2% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 30,804 | 13.4 | 8.7 | 18.7 | 15.2 | 19.2 | 14.8 | 9.9 | 12.9 | 44.0% | 24.8% |
| UNKNOWN | 6,361 | 10.5 | 7.6 | 17.1 | 16.3 | 21.5 | 16.0 | 11.1 | 14.32 | 48.5% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 13,477 | 19.6 | 11.9 | 22.3 | 15.9 | 14.9 | 9.2 | 6.3 | 8.9 | 30.3% | 15.4% |
| B | 5,788 | 12.6 | 8.6 | 19.6 | 15.6 | 19.8 | 12.8 | 10.9 | 12.75 | 43.5% | 23.7% |
| C | 6,707 | 11.9 | 8.8 | 19.5 | 15.6 | 18.7 | 14.6 | 10.8 | 13.0 | 44.1% | 25.4% |
| D | 7,675 | 11.7 | 8.3 | 17.9 | 15.3 | 21.7 | 15.7 | 9.4 | 13.88 | 46.9% | 25.1% |
| F | 13,702 | 7.4 | 5.6 | 14.8 | 14.7 | 23.5 | 20.8 | 13.1 | 17.79 | 57.4% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,339 | 24.6 | 16.1 | 29.1 | 15.0 | 10.6 | 3.4 | 1.2 | 6.36 | 15.3% | 4.7% |
| B | 4,849 | 16.6 | 10.8 | 24.2 | 16.8 | 18.9 | 9.6 | 3.0 | 9.67 | 31.5% | 12.6% |
| C | 6,830 | 11.0 | 7.8 | 19.5 | 14.6 | 21.0 | 15.7 | 10.4 | 13.67 | 47.1% | 26.1% |
| D | 5,189 | 14.5 | 10.1 | 21.4 | 15.3 | 20.9 | 12.5 | 5.3 | 11.23 | 38.7% | 17.8% |
| F | 8,482 | 10.2 | 8.3 | 16.2 | 14.6 | 23.4 | 19.5 | 7.8 | 15.34 | 50.7% | 27.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 15,208 | 17.8 | 10.9 | 21.4 | 15.7 | 15.2 | 10.1 | 8.9 | 9.98 | 34.2% | 18.9% |
| LIMITED | 10,374 | 13.6 | 9.7 | 20.4 | 15.8 | 19.5 | 13.3 | 7.6 | 11.89 | 40.5% | 21.0% |
| POOR | 21,767 | 9.0 | 6.6 | 16.0 | 14.9 | 22.8 | 18.9 | 11.8 | 16.17 | 53.4% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,913 | 23.7 | 17.9 | 33.1 | 15.6 | 6.4 | 3.0 | 0.4 | 5.92 | 9.8% | 3.4% |
| GAME_SPREAD | 6,684 | 22.8 | 15.4 | 32.0 | 16.8 | 8.9 | 3.4 | 0.7 | 6.68 | 13.0% | 4.0% |
| MATCH_WINNER | 34,689 | 15.8 | 10.9 | 22.2 | 15.1 | 18.5 | 12.0 | 5.5 | 10.26 | 36.0% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 16,530 | 28.0 | 16.8 | 30.8 | 12.7 | 9.0 | 2.4 | 0.3 | 5.62 | 11.7% | 2.7% |
| TOTAL_GAMES | 11,274 | 9.8 | 10.9 | 35.7 | 25.9 | 10.6 | 4.2 | 2.9 | 9.18 | 17.7% | 7.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,198 | 24.5 | 28.7 | 33.3 | 8.2 | 4.0 | 1.1 | 0.3 | 4.8 | 5.4% | 1.4% |
| GAME_SPREAD | 9,219 | 47.0 | 16.0 | 24.7 | 7.5 | 2.3 | 1.9 | 0.6 | 3.29 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,612 | 6.6 | 9.9 | 40.2 | 30.2 | 7.4 | 3.3 | 2.4 | 9.2 | 13.1% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,234 | 23.8 | 16.6 | 34.7 | 14.8 | 6.9 | 2.7 | 0.5 | 6.06 | 10.1% | 3.2% |
| GAME_SPREAD | 9,228 | 20.7 | 13.6 | 28.2 | 20.0 | 11.9 | 4.4 | 1.2 | 7.6 | 17.5% | 5.6% |
| TOTAL_GAMES | 16,651 | 10.0 | 10.8 | 36.3 | 24.3 | 11.5 | 4.5 | 2.6 | 9.04 | 18.6% | 7.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 47,349 | 44.4% | 24.8% | 13.04 | 35.3% | 15.0% | 10.68 |
| gen1_elo | 47,349 | 44.0% | 24.5% | 12.83 | 34.8% | 14.8% | 10.49 |
| gen1_sr | 47,349 | 52.0% | 31.3% | 15.82 | 43.9% | 21.5% | 12.97 |
| gen2 | 47,349 | 51.0% | 31.4% | 15.46 | 43.8% | 23.0% | 12.84 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,034 | 15.5 | 10.5 | 21.3 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 27,315 | 10.9 | 7.3 | 16.8 | 14.0 | 19.3 | 17.0 | 14.8 | 15.42 | 51.1% | 31.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 28,157 | 16.4 | 11.2 | 22.8 | 15.2 | 18.0 | 11.5 | 4.9 | 9.88 | 34.4% | 16.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 82,038 | 28157 | 23506 | 30375 | 24.8 | 127.1 | 1451.1 |
| ge_15pp | 33,506 | 9676 | 8373 | 15457 | 28.3 | 435.0 | 1451.1 |
| ge_25pp | 17,803 | 4604 | 3655 | 9544 | 33.1 | 581.7 | 1431.1 |
| lt_10pp | 36,000 | 14195 | 11116 | 10689 | 22.6 | 47.9 | 1421.1 |

Current slate `SL-20261108T143633Z-6dbff883`: 293 priced rows, quote age at build {'median': 59.7, 'max': 69.6}, freshness {'STALE': 293}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 50 | 0.0 | 0.0 | 36.0 | 8.0 | 32.0 | 20.0 | 4.0 | 18.34 | 56.0% | 24.0% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,689 | 19.2 | 11.0 | 25.4 | 18.0 | 18.1 | 7.4 | 1.0 | 8.82 | 26.4% | 8.4% |
| KALSHI_LONE_OUTLIER | 30 | 6.7 | 6.7 | 73.3 | 6.7 | 3.3 | 3.3 | 0.0 | 6.16 | 6.7% | 3.3% |
| MARKETS_AGREE | 990 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,098 | 0.0 | 2.2 | 37.3 | 26.4 | 24.1 | 9.2 | 0.9 | 11.81 | 34.1% | 10.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 47,349 | 7886 (16.7%) | 26.6% | 1.0% | {"EXTERNAL_STALE": 4689, "AGREES_WITH_KALSHI": 2098, "ALL_AGREE": 990, "SUPPORTS_MODEL_DIRECTION": 48, "AGREES_WITH_MODEL": 30, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 21,031 | 1985 (9.4%) | 36.0% | 1.5% | {"EXTERNAL_STALE": 1240, "AGREES_WITH_KALSHI": 715, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 11,737 | 616 (5.2%) | 34.1% | 2.1% | {"EXTERNAL_STALE": 393, "AGREES_WITH_KALSHI": 210, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,481 | 586 (10.7%) | 34.6% | 2.2% | {"EXTERNAL_STALE": 370, "AGREES_WITH_KALSHI": 203, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 19,036 | 4499 (23.6%) | 18.4% | 1.0% | {"EXTERNAL_STALE": 2606, "ALL_AGREE": 990, "AGREES_WITH_KALSHI": 830, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 26, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 9,281 | 10.5 | 7.7 | 19.4 | 14.6 | 21.6 | 16.3 | 9.9 | 14.09 | 47.8% | 26.2% |
| 4-10x | 6,338 | 11.2 | 8.5 | 18.4 | 15.2 | 22.1 | 14.4 | 10.2 | 13.86 | 46.7% | 24.6% |
| <2x | 24,177 | 14.9 | 9.8 | 19.7 | 16.0 | 17.6 | 13.1 | 8.9 | 11.57 | 39.6% | 22.0% |
| >=10x | 7,553 | 10.4 | 6.5 | 15.0 | 14.4 | 21.7 | 18.9 | 13.1 | 16.42 | 53.8% | 32.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 12,424 | 12.4 | 8.6 | 19.8 | 16.2 | 19.1 | 13.6 | 10.4 | 12.78 | 43.0% | 24.0% |
| 300-1000 | 10,252 | 11.8 | 8.7 | 17.7 | 15.1 | 20.8 | 16.3 | 9.6 | 13.76 | 46.7% | 25.9% |
| <300 | 14,816 | 8.3 | 5.8 | 15.1 | 14.8 | 23.1 | 19.9 | 13.1 | 17.13 | 56.0% | 32.9% |
| >=3000 | 9,857 | 21.4 | 12.9 | 23.8 | 15.6 | 13.9 | 7.3 | 5.1 | 7.75 | 26.3% | 12.4% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1459 | 0.5488 | 0.4101 | 0.4873 | +0.061 | -0.077 | 0.0011 ± 0.004 |
| ratio 4-10x | 991 | 0.577 | 0.4327 | 0.4874 | +0.090 | -0.055 | 0.0086 ± 0.005 |
| ratio <2x | 3563 | 0.5364 | 0.4137 | 0.4367 | +0.100 | -0.023 | 0.0144 ± 0.0024 |
| ratio >=10x | 1221 | 0.5668 | 0.3936 | 0.4505 | +0.116 | -0.057 | 0.0136 ± 0.0051 |
| thinner_sample 1000-3000 | 2002 | 0.5398 | 0.4121 | 0.4486 | +0.091 | -0.036 | 0.0112 ± 0.0033 |
| thinner_sample 300-1000 | 1639 | 0.5643 | 0.4243 | 0.4735 | +0.091 | -0.049 | 0.0049 ± 0.0038 |
| thinner_sample <300 | 2335 | 0.5588 | 0.391 | 0.4565 | +0.102 | -0.066 | 0.0123 ± 0.0037 |
| thinner_sample >=3000 | 1258 | 0.529 | 0.4356 | 0.4452 | +0.084 | -0.009 | 0.0151 ± 0.0032 |
| data_status ADEQUATE | 2009 | 0.5318 | 0.4288 | 0.44 | +0.092 | -0.011 | 0.0151 ± 0.0027 |
| data_status LIMITED | 1770 | 0.5481 | 0.4154 | 0.4667 | +0.082 | -0.051 | 0.0073 ± 0.0036 |
| data_status POOR | 3455 | 0.5607 | 0.4008 | 0.4602 | +0.101 | -0.059 | 0.0101 ± 0.0029 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1047 | 0.1977 | 0.198 | -0.0002 ± 0.0005 | 0.5756 | 0.5762 | 0.5022 | 0.487 | 0.4986 | -0.094 ± 0.0145 | -0.0087 (8) |
| 3-5 | 665 | 0.2047 | 0.2045 | +0.0002 ± 0.0014 | 0.594 | 0.5919 | 0.5053 | 0.4655 | 0.4827 | -0.096 ± 0.018 | 0.01 (3) |
| 5-10 | 1554 | 0.2025 | 0.2014 | +0.0011 ± 0.0017 | 0.5916 | 0.5865 | 0.512 | 0.4382 | 0.4653 | -0.091 ± 0.0118 | -0.0143 (7) |
| 10-15 | 1256 | 0.2184 | 0.2096 | +0.0087 ± 0.0032 | 0.6286 | 0.6031 | 0.5239 | 0.4003 | 0.426 | -0.103 ± 0.0131 | -0.055 (6) |
| 15-25 | 1609 | 0.2259 | 0.2083 | +0.0176 ± 0.0044 | 0.6469 | 0.6001 | 0.576 | 0.3814 | 0.4332 | -0.104 ± 0.0114 | -0.0045 (11) |
| 25-40 | 914 | 0.222 | 0.2058 | +0.0162 ± 0.0089 | 0.6336 | 0.5926 | 0.6514 | 0.3417 | 0.4705 | -0.065 ± 0.0137 | -0.06 (2) |
| 40+ | 189 | 0.295 | 0.1767 | +0.1183 ± 0.0274 | 0.7946 | 0.5268 | 0.7316 | 0.2768 | 0.381 | -0.081 ± 0.0265 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5449 | 0.1854 | 0.1863 | -0.0009 ± 0.0002 | 0.5469 | 0.5479 | 0.4903 | 0.4751 | 0.5069 | -0.020 ± 0.0059 | -0.01 (28) |
| 3-5 | 3630 | 0.1977 | 0.196 | +0.0017 ± 0.0006 | 0.576 | 0.5697 | 0.483 | 0.4433 | 0.4413 | -0.056 ± 0.0074 | 0.005 (6) |
| 5-10 | 7875 | 0.2013 | 0.1978 | +0.0035 ± 0.0007 | 0.5884 | 0.5766 | 0.4847 | 0.411 | 0.4244 | -0.045 ± 0.0051 | -0.0114 (22) |
| 10-15 | 6499 | 0.2021 | 0.1862 | +0.0159 ± 0.0013 | 0.5908 | 0.5463 | 0.4856 | 0.3616 | 0.3599 | -0.064 ± 0.0054 | -0.0379 (19) |
| 15-25 | 8246 | 0.2063 | 0.1671 | +0.0393 ± 0.0018 | 0.6046 | 0.4963 | 0.4997 | 0.3042 | 0.3022 | -0.070 ± 0.0045 | -0.0043 (51) |
| 25-40 | 6352 | 0.2224 | 0.1262 | +0.0962 ± 0.0028 | 0.639 | 0.3878 | 0.5268 | 0.2131 | 0.2207 | -0.058 ± 0.0043 | -0.0733 (3) |
| 40+ | 4234 | 0.383 | 0.0437 | +0.3393 ± 0.0037 | 0.9974 | 0.17 | 0.6311 | 0.1015 | 0.0579 | -0.076 ± 0.003 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 837 | 0.205 | 0.2053 | -0.0003 ± 0.0005 | 0.5907 | 0.5918 | 0.5063 | 0.4915 | 0.5137 | -0.102 ± 0.0168 | -0.0117 (6) |
| 3-5 | 595 | 0.2114 | 0.2084 | +0.0030 ± 0.0015 | 0.606 | 0.5995 | 0.5136 | 0.474 | 0.4521 | -0.130 ± 0.0201 | 0.01 (3) |
| 5-10 | 1340 | 0.207 | 0.2051 | +0.0019 ± 0.0019 | 0.6003 | 0.5952 | 0.5405 | 0.466 | 0.4933 | -0.088 ± 0.0128 | -0.01 (4) |
| 10-15 | 1164 | 0.2132 | 0.2073 | +0.0059 ± 0.0033 | 0.6191 | 0.6006 | 0.5626 | 0.4382 | 0.4794 | -0.099 ± 0.0139 | -0.04 (5) |
| 15-25 | 1692 | 0.2321 | 0.2124 | +0.0197 ± 0.0044 | 0.6599 | 0.6093 | 0.5853 | 0.3898 | 0.4385 | -0.100 ± 0.0115 | -0.0183 (12) |
| 25-40 | 1185 | 0.2661 | 0.1987 | +0.0674 ± 0.0081 | 0.7425 | 0.5777 | 0.6599 | 0.3457 | 0.3975 | -0.116 ± 0.013 | -0.008 (5) |
| 40+ | 421 | 0.3715 | 0.1626 | +0.2089 ± 0.0197 | 1.0133 | 0.4914 | 0.7364 | 0.2476 | 0.2922 | -0.087 ± 0.0189 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4665 | 0.1919 | 0.1921 | -0.0002 ± 0.0002 | 0.5596 | 0.5597 | 0.5074 | 0.4923 | 0.5078 | -0.040 ± 0.0066 | -0.0154 (26) |
| 3-5 | 3183 | 0.1927 | 0.1916 | +0.0012 ± 0.0006 | 0.5622 | 0.5585 | 0.5115 | 0.4718 | 0.4763 | -0.047 ± 0.008 | 0.01 (5) |
| 5-10 | 7034 | 0.1969 | 0.1935 | +0.0034 ± 0.0008 | 0.5788 | 0.5663 | 0.5088 | 0.4347 | 0.4512 | -0.041 ± 0.0053 | -0.0117 (6) |
| 10-15 | 5831 | 0.2029 | 0.1917 | +0.0111 ± 0.0014 | 0.5953 | 0.5606 | 0.5105 | 0.3866 | 0.4044 | -0.047 ± 0.0058 | -0.0189 (18) |
| 15-25 | 8292 | 0.2171 | 0.1814 | +0.0357 ± 0.0018 | 0.6313 | 0.532 | 0.5256 | 0.33 | 0.339 | -0.060 ± 0.0047 | -0.014 (52) |
| 25-40 | 7456 | 0.2507 | 0.1378 | +0.1129 ± 0.0027 | 0.7082 | 0.4208 | 0.5603 | 0.2434 | 0.2273 | -0.079 ± 0.0043 | -0.0095 (20) |
| 40+ | 5824 | 0.4017 | 0.0582 | +0.3436 ± 0.0037 | 1.0588 | 0.2104 | 0.6543 | 0.1183 | 0.0793 | -0.074 ± 0.0031 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1017 | 0.1957 | 0.1971 | -0.0014 ± 0.0005 | 0.5711 | 0.5744 | 0.5025 | 0.4872 | 0.532 | -0.052 ± 0.0145 | -0.0191 (11) |
| 3-5 | 720 | 0.2077 | 0.2062 | +0.0015 ± 0.0014 | 0.602 | 0.5966 | 0.499 | 0.4595 | 0.4625 | -0.110 ± 0.0177 | 0.002 (5) |
| 5-10 | 1587 | 0.2029 | 0.1993 | +0.0036 ± 0.0017 | 0.5911 | 0.5809 | 0.5127 | 0.439 | 0.4505 | -0.104 ± 0.0116 | -0.01 (10) |
| 10-15 | 1271 | 0.2117 | 0.203 | +0.0088 ± 0.0031 | 0.6139 | 0.5886 | 0.5373 | 0.414 | 0.4422 | -0.106 ± 0.0127 | -0.0286 (7) |
| 15-25 | 1539 | 0.2312 | 0.2129 | +0.0183 ± 0.0046 | 0.66 | 0.6102 | 0.5866 | 0.3925 | 0.4418 | -0.107 ± 0.0118 | -0.03 (1) |
| 25-40 | 902 | 0.2118 | 0.21 | +0.0019 ± 0.009 | 0.6122 | 0.6023 | 0.6591 | 0.3483 | 0.4989 | -0.053 ± 0.0138 | -0.0267 (3) |
| 40+ | 198 | 0.3082 | 0.1841 | +0.1242 ± 0.0273 | 0.8344 | 0.5426 | 0.7433 | 0.2886 | 0.3889 | -0.085 ± 0.028 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5243 | 0.1853 | 0.1859 | -0.0007 ± 0.0002 | 0.5462 | 0.547 | 0.486 | 0.4707 | 0.4902 | -0.032 ± 0.006 | -0.0189 (44) |
| 3-5 | 3753 | 0.2038 | 0.2021 | +0.0018 ± 0.0006 | 0.5928 | 0.5867 | 0.4802 | 0.4407 | 0.4391 | -0.056 ± 0.0075 | -0.0073 (22) |
| 5-10 | 8024 | 0.196 | 0.1907 | +0.0053 ± 0.0007 | 0.5753 | 0.5587 | 0.4875 | 0.4135 | 0.4149 | -0.056 ± 0.0049 | -0.0117 (42) |
| 10-15 | 6448 | 0.1939 | 0.1788 | +0.0150 ± 0.0013 | 0.5726 | 0.5291 | 0.4948 | 0.3715 | 0.3721 | -0.062 ± 0.0053 | -0.0136 (14) |
| 15-25 | 8331 | 0.2121 | 0.1726 | +0.0394 ± 0.0018 | 0.6181 | 0.509 | 0.5128 | 0.3183 | 0.315 | -0.071 ± 0.0045 | -0.0533 (3) |
| 25-40 | 6300 | 0.2162 | 0.127 | +0.0891 ± 0.0028 | 0.6255 | 0.3892 | 0.5288 | 0.2133 | 0.2319 | -0.048 ± 0.0043 | -0.02 (4) |
| 40+ | 4186 | 0.3918 | 0.0487 | +0.3431 ± 0.0039 | 1.0211 | 0.1825 | 0.6402 | 0.1076 | 0.0647 | -0.076 ± 0.0033 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1454 | 0.1981 | 0.1981 | +0.0000 ± 0.0004 | 0.5748 | 0.5746 | 0.5081 | 0.4931 | 0.4966 | -0.069 ± 0.0119 | -0.0221 (56) |
| 3-5 | 1046 | 0.188 | 0.188 | +0.0000 ± 0.0011 | 0.554 | 0.5521 | 0.4971 | 0.4572 | 0.4751 | -0.055 ± 0.0137 | -0.0194 (34) |
| 5-10 | 2108 | 0.1999 | 0.195 | +0.0049 ± 0.0014 | 0.5897 | 0.5734 | 0.5083 | 0.4348 | 0.4388 | -0.077 ± 0.0098 | -0.005 (78) |
| 10-15 | 1451 | 0.2146 | 0.2023 | +0.0123 ± 0.0029 | 0.6227 | 0.5882 | 0.542 | 0.4192 | 0.4294 | -0.088 ± 0.0121 | 0.0012 (66) |
| 15-25 | 1896 | 0.2307 | 0.2075 | +0.0233 ± 0.0041 | 0.6587 | 0.5989 | 0.5915 | 0.3966 | 0.4362 | -0.088 ± 0.0105 | -0.0214 (59) |
| 25-40 | 1136 | 0.2397 | 0.2105 | +0.0292 ± 0.0083 | 0.6847 | 0.6039 | 0.6887 | 0.3768 | 0.4859 | -0.086 ± 0.0128 | -0.0252 (27) |
| 40+ | 407 | 0.3243 | 0.2016 | +0.1228 ± 0.0212 | 0.9334 | 0.5868 | 0.8178 | 0.3418 | 0.4668 | -0.097 ± 0.0197 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5354 | 0.1778 | 0.1779 | -0.0001 ± 0.0002 | 0.5261 | 0.5258 | 0.5115 | 0.4962 | 0.5054 | -0.040 ± 0.0058 | -0.0154 (103) |
| 3-5 | 3708 | 0.1947 | 0.1939 | +0.0008 ± 0.0006 | 0.5683 | 0.566 | 0.5014 | 0.4616 | 0.4725 | -0.039 ± 0.0073 | -0.0212 (73) |
| 5-10 | 7531 | 0.1965 | 0.19 | +0.0065 ± 0.0008 | 0.5801 | 0.5602 | 0.5018 | 0.4282 | 0.4221 | -0.062 ± 0.0051 | -0.0084 (134) |
| 10-15 | 5155 | 0.2099 | 0.1936 | +0.0163 ± 0.0015 | 0.611 | 0.5679 | 0.5372 | 0.4142 | 0.4081 | -0.072 ± 0.0062 | -0.0057 (111) |
| 15-25 | 6278 | 0.2314 | 0.1999 | +0.0315 ± 0.0022 | 0.6647 | 0.5791 | 0.5767 | 0.3814 | 0.3992 | -0.067 ± 0.0057 | -0.026 (108) |
| 25-40 | 4089 | 0.2566 | 0.1906 | +0.0660 ± 0.0043 | 0.7263 | 0.5548 | 0.6407 | 0.3282 | 0.3818 | -0.064 ± 0.0067 | -0.0277 (53) |
| 40+ | 1814 | 0.3699 | 0.1592 | +0.2106 ± 0.0097 | 1.0435 | 0.4744 | 0.7457 | 0.2449 | 0.2955 | -0.064 ± 0.0089 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7234 | 1.029 ± 0.033 | 1.099 | 0.1688 | 0.1683 | 0.2149 | 0.2041 |
| gen2 | 7234 | 0.822 ± 0.03 | 1.071 | 0.1735 | 0.1686 | 0.2332 | 0.2039 |
| gen1_elo | 7234 | 1.011 ± 0.032 | 1.089 | 0.1752 | 0.1684 | 0.2139 | 0.2041 |
| gen1_sr | 7234 | 1.008 ± 0.039 | 1.129 | 0.1334 | 0.1703 | 0.2293 | 0.2036 |
| gen1_ledger | 9498 | 0.867 ± 0.024 | 1.076 | 0.1897 | 0.1753 | 0.2168 | 0.2004 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 33,506)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 7,743 | 23.1% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,614 | 22.7% |
| BOOK_QUALITY | execution | 5,987 | 17.9% |
| POOR_DATA | data | 3,861 | 11.5% |
| LIMITED_DATA | data | 2,086 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,931 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 1,399 | 4.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,377 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 957 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 550 | 1.6% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 23.1%, coverage 22.7%, execution 17.9%, data 17.8%, market_freshness/coverage 8.6%, mapping 4.2%, model_calibration_or_unknown 4.1%, model_calibration 1.6%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.6%, LOW_DATA_QUALITY 71.5%, THIN_PLAYER_HISTORY 59.7%, STALE_PLAYER_DATA 52.1%, STALE_KALSHI_QUOTE 46.1%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 24.1%, MODEL_HIGH_UNCERTAINTY 18.7%, PLAYER_IDENTITY_RISK 15.3%, LEVEL_TRANSFER_RISK 10.0%, LOW_DISPLAYED_LIQUIDITY 8.3%, EVENT_MAPPING_RISK 7.2%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.2%, POST_SETTLEMENT_OBSERVATION 22.7%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 17,803)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,104 | 34.3% |
| STALE_QUOTE | market_freshness | 3,446 | 19.4% |
| BOOK_QUALITY | execution | 3,105 | 17.4% |
| POOR_DATA | data | 1,623 | 9.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,029 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 778 | 4.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 627 | 3.5% |
| LIMITED_DATA | data | 613 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 342 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 135 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.3%, market_freshness 19.4%, execution 17.4%, data 12.6%, market_freshness/coverage 9.3%, mapping 4.4%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 74.7%, THIN_PLAYER_HISTORY 61.6%, STALE_KALSHI_QUOTE 53.6%, STALE_PLAYER_DATA 45.7%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 34.2%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 19.3%, PLAYER_IDENTITY_RISK 18.4%, EVENT_MAPPING_RISK 8.9%, LEVEL_TRANSFER_RISK 8.8%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.3%, POST_SETTLEMENT_OBSERVATION 34.3%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 14204, "IDENTITY_AMBIGUOUS": 3599}; ticker orientation: {"VERIFIED": 17803}.

Checks: discipline:AMBIGUOUS 1199, discipline:PASS 16604, identity_confidence:AMBIGUOUS 3268, identity_confidence:PASS 14535, level_mapping:NA 1211, level_mapping:PASS 16592, market_pair:AMBIGUOUS 492, market_pair:NA 400, market_pair:PASS 16911, model_complement:NA 362, model_complement:PASS 17441, namesake:AMBIGUOUS 6, namesake:PASS 17797, physical_match_id:NA 6066, physical_match_id:PASS 11737, player_ids:PASS 17803, same_pair_other_event:PASS 17803, ticker_orientation:PASS 17803

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,366 | 3.8% | 3.2% | 1.4% | {"market_freshness": 57, "model_calibration_or_unknown": 55, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 21, "market_freshness/coverage": 19} | 5.52 | 0.2236 / 0.2187 (821) | 24.8% | 2.5% | 3.1% | 2.8% |
| CHALLENGER | 11,723 | 16.3% | 6.2% | 10.8% | {"coverage": 1133, "market_freshness": 223, "market_freshness/coverage": 220, "data": 161, "model_calibration_or_unknown": 79, "execution": 43, "model_calibration": 36, "mapping": 17, "possible_market_error": 1} | 7.37 | 0.2206 / 0.2102 (2766) | 38.0% | 15.0% | 4.0% | 22.3% |
| DOUBLES | 2,581 | 46.5% | 46.4% | 6.7% | {"execution": 665, "mapping": 352, "market_freshness": 106, "market_freshness/coverage": 69, "coverage": 7} | 23.23 | 0.2978 / 0.232 (645) | 9.1% | 0.0% | 100.0% | 6.3% |
| ITF_MEN | 23,341 | 24.9% | 17.3% | 32.6% | {"coverage": 2048, "market_freshness": 1126, "execution": 983, "data": 850, "market_freshness/coverage": 590, "mapping": 204, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.64 | 0.2176 / 0.1998 (4982) | 40.0% | 68.7% | 15.1% | 21.6% |
| ITF_WOMEN | 30,444 | 26.4% | 18.9% | 45.2% | {"coverage": 2840, "market_freshness": 1730, "execution": 1331, "data": 1124, "market_freshness/coverage": 701, "mapping": 199, "model_calibration_or_unknown": 94, "model_calibration": 23} | 12.51 | 0.2022 / 0.194 (5912) | 41.2% | 57.1% | 9.9% | 21.7% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,845 | 6.0% | 5.1% | 1.6% | {"market_freshness": 111, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.67 | 0.2304 / 0.2206 (794) | 29.9% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.7% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 404 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 638 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 725 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 773 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 20.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 1252 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 12 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 899 min (STALE); no external reference |
| 15 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 18 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 19 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 20 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 21 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 22 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 23 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 24 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 25 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 454 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 26 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 27 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 28 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 29 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 30 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 31 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 32 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 33 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 34 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 35 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 36 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 37 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 38 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 39 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 40 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 41 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 768 min (STALE); no external reference |
| 43 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 44 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 45 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 46 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.1h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 446 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 49 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 50 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.3h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 748 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9702, "by_level_share_of_ge_25pp": {"ATP": 0.0135, "CHALLENGER": 0.1075, "DOUBLES": 0.0673, "ITF_MEN": 0.3265, "ITF_WOMEN": 0.4517, "OTHER": 0.0007, "WTA": 0.0163, "WTA125": 0.0165}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5361, "share_primary_cause_market_settled_or_in_play": 0.4359, "share_primary_cause_stale_quote_only": 0.1936}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 17803, "identity_ambiguous_share": 0.2022, "ticker_orientation": {"VERIFIED": 17803}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 11737, "with_external": 616, "coverage": 0.0525, "external_status": {"EXTERNAL_STALE": 393, "AGREES_WITH_KALSHI": 210, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 393, "MODEL_LONE_OUTLIER": 210, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3409, "share_external_supports_model": 0.0211}, "pregame_clean_ge_25pp": {"n": 5481, "with_external": 586, "coverage": 0.1069, "external_status": {"EXTERNAL_STALE": 370, "AGREES_WITH_KALSHI": 203, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 370, "MODEL_LONE_OUTLIER": 203, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3464, "share_external_supports_model": 0.0222}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 494.0, "median_sample_ratio": 2.46, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2087, "data_status": {"POOR": 9952, "LIMITED": 4632, "ADEQUATE": 3219}, "comparison_lt_10pp": {"median_thinner_serve_points": 1733.0, "median_sample_ratio": 1.7, "median_min_matches": 90.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1459, "model_minus_observed": 0.0615, "kalshi_minus_observed": -0.0772, "brier_diff_model_minus_kalshi": 0.0011}, "4-10x": {"n": 991, "model_minus_observed": 0.0897, "kalshi_minus_observed": -0.0547, "brier_diff_model_minus_kalshi": 0.0086}, "<2x": {"n": 3563, "model_minus_observed": 0.0997, "kalshi_minus_observed": -0.023, "brier_diff_model_minus_kalshi": 0.0144}, ">=10x": {"n": 1221, "model_minus_observed": 0.1163, "kalshi_minus_observed": -0.0569, "brier_diff_model_minus_kalshi": 0.0136}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 7234, "model": {"intercept": -0.554, "slope": 0.822, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.181, "slope": 1.071, "slope_se": 0.033}, "mean_extremity_model": 0.1735, "mean_extremity_kalshi": 0.1686, "model_brier": 0.2332, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0293, "brier_diff_se": 0.0022, "model_logloss": 0.664, "kalshi_logloss": 0.5904}, "fair_v1": {"n": 7234, "model": {"intercept": -0.448, "slope": 1.029, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.248, "slope": 1.099, "slope_se": 0.034}, "mean_extremity_model": 0.1688, "mean_extremity_kalshi": 0.1683, "model_brier": 0.2149, "kalshi_brier": 0.2041, "brier_diff_model_minus_kalshi": 0.0108, "brier_diff_se": 0.0018, "model_logloss": 0.6188, "kalshi_logloss": 0.5906}, "gen1_elo": {"n": 7234, "model": {"intercept": -0.437, "slope": 1.011, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.249, "slope": 1.089, "slope_se": 0.033}, "mean_extremity_model": 0.1752, "mean_extremity_kalshi": 0.1684, "model_brier": 0.2139, "kalshi_brier": 0.2041, "brier_diff_model_minus_kalshi": 0.0098, "brier_diff_se": 0.0018, "model_logloss": 0.6173, "kalshi_logloss": 0.5908}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2479, "share_ge_15": 0.4442, "median_abs_gap": 13.04, "n": 47349}, "gen1_elo": {"share_ge_25": 0.245, "share_ge_15": 0.4401, "median_abs_gap": 12.83, "n": 47349}, "gen1_sr": {"share_ge_25": 0.3131, "share_ge_15": 0.5201, "median_abs_gap": 15.82, "n": 47349}, "gen2": {"share_ge_25": 0.3139, "share_ge_15": 0.5103, "median_abs_gap": 15.46, "n": 47349}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1503, "share_ge_15": 0.3531, "median_abs_gap": 10.68, "n": 36449}, "gen1_elo": {"share_ge_25": 0.1483, "share_ge_15": 0.348, "median_abs_gap": 10.49, "n": 36449}, "gen1_sr": {"share_ge_25": 0.2153, "share_ge_15": 0.4388, "median_abs_gap": 12.97, "n": 36451}, "gen2": {"share_ge_25": 0.2304, "share_ge_15": 0.4384, "median_abs_gap": 12.84, "n": 36451}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.52, "share_ge_25_all": 0.0379, "share_ge_25_pregame_clean": 0.0325}, "WTA": {"median_abs_gap_pregame_clean": 7.67, "share_ge_25_all": 0.0601, "share_ge_25_pregame_clean": 0.051}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2368, "share_within_10pp_all": 0.4388, "share_within_10pp_pregame_clean": 0.492, "corr_model_vs_mid_pregame_clean": 0.8508}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1047, "model_brier": 0.1977, "kalshi_brier": 0.198, "brier_diff_model_minus_kalshi": -0.0002}, "10-15": {"n_settled": 1256, "model_brier": 0.2184, "kalshi_brier": 0.2096, "brier_diff_model_minus_kalshi": 0.0087}, "15-25": {"n_settled": 1609, "model_brier": 0.2259, "kalshi_brier": 0.2083, "brier_diff_model_minus_kalshi": 0.0176}, "25-40": {"n_settled": 914, "model_brier": 0.222, "kalshi_brier": 0.2058, "brier_diff_model_minus_kalshi": 0.0162}, "3-5": {"n_settled": 665, "model_brier": 0.2047, "kalshi_brier": 0.2045, "brier_diff_model_minus_kalshi": 0.0002}, "40+": {"n_settled": 189, "model_brier": 0.295, "kalshi_brier": 0.1767, "brier_diff_model_minus_kalshi": 0.1183}, "5-10": {"n_settled": 1554, "model_brier": 0.2025, "kalshi_brier": 0.2014, "brier_diff_model_minus_kalshi": 0.0011}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.554, "slope": 0.822, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.181, "slope": 1.071, "slope_se": 0.033}, "n": 7234}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.485, "slope": 0.867, "slope_se": 0.024}, "kalshi_slope": {"intercept": 0.174, "slope": 1.076, "slope_se": 0.028}, "n": 9498}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 645, "model_brier": 0.2978, "kalshi_brier": 0.232, "brier_diff_model_minus_kalshi": 0.0658, "brier_diff_se": 0.0115, "corr_model_outcome": 0.1036, "corr_kalshi_outcome": 0.2831}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
