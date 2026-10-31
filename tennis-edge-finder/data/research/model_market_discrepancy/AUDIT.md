# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-31T13:34Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 71,289): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 19.0%, 25-40 13.7%, 40+ 8.0%; median gap 11.81 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.8%, Challenger 10.8%, doubles 6.7%). Main tour: ATP 4.0% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 15,513): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.1%, STALE_QUOTE 18.8%, BOOK_QUALITY 18.2%, POOR_DATA 9.3%, POSSIBLY_IN_PLAY_QUOTE 5.7%, IDENTITY_AMBIGUOUS 4.2%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.1%, market_freshness 18.8%, execution 18.2%, data 12.8%, market_freshness/coverage 9.2%, mapping 4.2%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.4% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.3% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 15,513 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.6% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 479.5 points vs 1729.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.019, Gen-2 0.807, Gen-1 ledger 0.856 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 750 model 0.2236 vs Kalshi 0.2054; n 159 model 0.2822 vs Kalshi 0.1885.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 303,713 model-market comparisons (495,920 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 102,489 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-31T13:21:32.761541+00:00'], shadow board 81,401 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-31T13:21:36.049309+00:00'], Model 4 37,812 rows, 24,646 settled tickers, 9,033 tickers with an external scan.
* By model: {"gen1_ledger": 69165, "gen1_elo": 40911, "fair_v1": 40911, "gen2": 40911, "gen1_sr": 40911, "model4_fundamental": 35474, "model4_conditioned": 35430}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 71,289 | 14.1 | 9.6 | 20.2 | 15.3 | 19.0 | 13.7 | 8.0 | 11.81 | 40.7% | 21.8% |
| MW fair_v1 | 40,911 | 13.0 | 8.7 | 18.8 | 15.3 | 19.4 | 14.8 | 9.9 | 12.99 | 44.2% | 24.8% |
| MW gen1_elo | 40,911 | 12.5 | 8.7 | 19.3 | 15.4 | 19.5 | 14.8 | 9.8 | 12.92 | 44.1% | 24.6% |
| MW gen1_ledger | 30,378 | 15.7 | 10.8 | 22.1 | 15.2 | 18.4 | 12.3 | 5.5 | 10.31 | 36.1% | 17.7% |
| MW gen1_sr | 40,911 | 10.2 | 7.2 | 16.9 | 13.9 | 20.6 | 18.5 | 12.7 | 15.77 | 51.8% | 31.2% |
| MW gen2 | 40,911 | 11.1 | 7.6 | 16.6 | 13.8 | 19.3 | 17.7 | 13.8 | 15.39 | 50.8% | 31.5% |
| all families model4_conditioned | 35,430 | 22.5 | 18.3 | 34.1 | 17.1 | 4.9 | 2.0 | 1.1 | 5.98 | 8.1% | 3.2% |
| all families model4_fundamental | 35,474 | 17.4 | 13.4 | 33.9 | 20.1 | 10.1 | 3.7 | 1.4 | 7.64 | 15.2% | 5.1% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.0%, >=15pp 40.7%, >=20pp 30.1%, >=25pp 21.8%, >=30pp 15.7%, >=40pp 8.0%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.28pp; >=10pp 44.7%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,553 | 27.3 | 15.4 | 28.1 | 13.3 | 11.4 | 3.9 | 0.6 | 5.93 | 15.9% | 4.5% |
| CHALLENGER | 6,029 | 16.4 | 9.7 | 20.8 | 15.1 | 15.3 | 11.7 | 10.9 | 10.91 | 37.9% | 22.6% |
| ITF_MEN | 11,498 | 9.8 | 7.4 | 17.0 | 15.0 | 21.2 | 17.5 | 12.0 | 15.21 | 50.7% | 29.5% |
| ITF_WOMEN | 16,087 | 9.6 | 7.1 | 16.0 | 15.1 | 22.0 | 18.1 | 12.2 | 15.69 | 52.2% | 30.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,588 | 18.2 | 13.4 | 25.4 | 19.9 | 15.8 | 6.1 | 1.2 | 8.2 | 23.1% | 7.3% |
| WTA125 | 1,150 | 16.5 | 7.2 | 22.4 | 19.1 | 20.8 | 12.1 | 1.8 | 10.7 | 34.7% | 13.9% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,553 | 26.0 | 15.4 | 26.3 | 15.9 | 11.7 | 3.9 | 0.8 | 6.22 | 16.4% | 4.7% |
| CHALLENGER | 6,029 | 15.2 | 9.1 | 18.2 | 14.2 | 18.1 | 13.4 | 11.8 | 12.49 | 43.3% | 25.2% |
| ITF_MEN | 11,498 | 8.1 | 6.2 | 15.1 | 13.9 | 19.5 | 20.7 | 16.5 | 17.91 | 56.7% | 37.2% |
| ITF_WOMEN | 16,087 | 8.0 | 5.8 | 14.0 | 12.8 | 20.6 | 21.1 | 17.7 | 19.1 | 59.4% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,588 | 15.3 | 11.0 | 22.4 | 15.0 | 21.8 | 12.4 | 2.0 | 10.41 | 36.2% | 14.4% |
| WTA125 | 1,150 | 9.7 | 6.8 | 17.0 | 15.7 | 24.2 | 17.8 | 8.7 | 15.2 | 50.7% | 26.5% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,553 | 22.0 | 13.6 | 24.6 | 16.0 | 15.9 | 6.6 | 1.3 | 7.54 | 23.7% | 7.8% |
| CHALLENGER | 6,029 | 15.0 | 9.3 | 20.9 | 16.1 | 15.5 | 12.1 | 11.1 | 11.34 | 38.8% | 23.2% |
| ITF_MEN | 11,498 | 9.3 | 7.2 | 17.4 | 14.2 | 21.9 | 17.7 | 12.4 | 15.75 | 52.0% | 30.1% |
| ITF_WOMEN | 16,087 | 9.4 | 6.9 | 16.4 | 15.8 | 22.1 | 18.0 | 11.5 | 15.5 | 51.5% | 29.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,588 | 23.2 | 16.4 | 32.2 | 14.5 | 9.4 | 3.1 | 1.2 | 6.12 | 13.7% | 4.3% |
| WTA125 | 1,150 | 21.4 | 13.0 | 27.0 | 17.7 | 14.8 | 5.7 | 0.3 | 7.99 | 20.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,123 | 25.1 | 19.3 | 30.7 | 12.9 | 8.8 | 2.8 | 0.5 | 5.65 | 12.0% | 3.2% |
| CHALLENGER | 4,083 | 22.8 | 14.5 | 27.3 | 14.5 | 13.5 | 5.9 | 1.6 | 7.07 | 20.9% | 7.4% |
| DOUBLES | 2,205 | 5.2 | 4.3 | 12.0 | 10.6 | 20.9 | 25.2 | 21.8 | 23.65 | 67.9% | 47.0% |
| ITF_MEN | 8,683 | 13.0 | 9.5 | 21.3 | 15.8 | 21.4 | 13.2 | 5.8 | 11.87 | 40.5% | 19.1% |
| ITF_WOMEN | 10,389 | 13.1 | 9.1 | 19.9 | 15.8 | 21.2 | 15.3 | 5.5 | 12.32 | 42.0% | 20.8% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,580 | 24.2 | 16.1 | 30.3 | 17.1 | 9.0 | 2.9 | 0.2 | 6.53 | 12.2% | 3.2% |
| WTA125 | 1,166 | 24.9 | 12.9 | 21.1 | 19.6 | 13.3 | 6.8 | 1.5 | 7.88 | 21.6% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,454 | 27.7 | 15.6 | 28.4 | 13.3 | 11.2 | 3.5 | 0.3 | 5.91 | 15.1% | 3.9% |
| CHALLENGER | 4,220 | 21.4 | 12.2 | 25.9 | 17.7 | 15.2 | 6.0 | 1.6 | 8.01 | 22.8% | 7.6% |
| ITF_MEN | 8,393 | 12.1 | 8.8 | 20.6 | 17.1 | 22.0 | 14.2 | 5.2 | 12.34 | 41.3% | 19.4% |
| ITF_WOMEN | 11,926 | 11.5 | 8.5 | 18.6 | 17.2 | 24.0 | 15.0 | 5.1 | 13.25 | 44.1% | 20.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,501 | 18.6 | 13.4 | 25.6 | 20.2 | 15.8 | 5.7 | 0.7 | 8.13 | 22.2% | 6.4% |
| WTA125 | 1,111 | 16.7 | 7.1 | 22.0 | 19.4 | 21.2 | 11.9 | 1.6 | 10.77 | 34.7% | 13.5% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,454 | 26.3 | 15.7 | 26.5 | 15.9 | 11.7 | 3.6 | 0.4 | 6.19 | 15.7% | 4.0% |
| CHALLENGER | 4,220 | 19.4 | 11.7 | 22.9 | 16.7 | 18.5 | 9.0 | 1.9 | 8.98 | 29.4% | 10.9% |
| ITF_MEN | 8,394 | 9.6 | 7.4 | 17.6 | 16.1 | 21.3 | 18.7 | 9.4 | 14.84 | 49.4% | 28.1% |
| ITF_WOMEN | 11,927 | 8.9 | 6.8 | 15.9 | 14.3 | 22.8 | 20.6 | 10.8 | 16.55 | 54.1% | 31.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,501 | 15.6 | 11.0 | 22.6 | 15.1 | 21.9 | 12.4 | 1.3 | 10.21 | 35.7% | 13.7% |
| WTA125 | 1,111 | 9.7 | 6.8 | 17.2 | 15.8 | 24.1 | 18.1 | 8.2 | 15.13 | 50.4% | 26.3% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,066 | 25.2 | 19.5 | 30.7 | 13.1 | 8.5 | 2.7 | 0.4 | 5.58 | 11.5% | 3.0% |
| CHALLENGER | 3,600 | 24.2 | 15.4 | 28.5 | 14.6 | 12.8 | 4.0 | 0.4 | 6.58 | 17.2% | 4.4% |
| DOUBLES | 2,068 | 5.1 | 4.4 | 12.2 | 10.7 | 20.7 | 25.1 | 21.8 | 23.61 | 67.5% | 46.9% |
| ITF_MEN | 7,411 | 13.8 | 10.1 | 22.9 | 16.4 | 21.3 | 11.7 | 3.8 | 10.88 | 36.8% | 15.4% |
| ITF_WOMEN | 8,853 | 13.8 | 9.6 | 21.2 | 16.5 | 21.3 | 14.3 | 3.4 | 11.5 | 39.0% | 17.7% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,522 | 24.6 | 16.6 | 30.3 | 17.2 | 9.0 | 2.3 | 0.1 | 6.37 | 11.4% | 2.4% |
| WTA125 | 1,037 | 26.0 | 13.7 | 22.2 | 20.6 | 12.2 | 4.7 | 0.5 | 7.39 | 17.4% | 5.2% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,205 | 5.2 | 4.3 | 12.0 | 10.6 | 20.9 | 25.2 | 21.8 | 23.65 | 67.9% | 47.0% |
| singles | 28,173 | 16.5 | 11.3 | 22.9 | 15.6 | 18.2 | 11.2 | 4.2 | 9.79 | 33.6% | 15.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 8,044 | 13.2 | 9.4 | 20.2 | 15.8 | 18.9 | 13.7 | 8.9 | 12.26 | 41.5% | 22.5% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 26,927 | 13.4 | 8.7 | 18.7 | 15.0 | 19.2 | 14.9 | 10.1 | 12.95 | 44.1% | 24.9% |
| UNKNOWN | 5,691 | 10.5 | 7.8 | 17.1 | 16.3 | 21.3 | 16.1 | 11.1 | 14.26 | 48.4% | 27.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 11,455 | 20.1 | 12.0 | 22.6 | 15.5 | 14.7 | 9.0 | 6.1 | 8.51 | 29.8% | 15.1% |
| B | 5,110 | 12.9 | 8.9 | 19.4 | 15.8 | 19.5 | 12.5 | 10.9 | 12.54 | 42.9% | 23.5% |
| C | 5,861 | 11.8 | 8.9 | 19.9 | 15.7 | 18.5 | 14.5 | 10.8 | 12.88 | 43.7% | 25.2% |
| D | 6,458 | 11.8 | 8.4 | 17.6 | 15.2 | 21.6 | 15.9 | 9.5 | 13.85 | 47.0% | 25.4% |
| F | 12,027 | 7.4 | 5.6 | 15.0 | 14.8 | 23.3 | 20.9 | 13.0 | 17.65 | 57.2% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,175 | 24.4 | 15.9 | 29.0 | 15.1 | 10.8 | 3.6 | 1.3 | 6.43 | 15.6% | 4.9% |
| B | 4,345 | 16.7 | 10.7 | 24.1 | 16.9 | 18.8 | 9.7 | 3.1 | 9.68 | 31.5% | 12.8% |
| C | 5,951 | 11.3 | 7.8 | 19.3 | 14.6 | 21.0 | 15.8 | 10.2 | 13.6 | 47.0% | 26.0% |
| D | 4,433 | 14.2 | 9.9 | 21.6 | 15.5 | 20.1 | 13.3 | 5.4 | 11.26 | 38.8% | 18.7% |
| F | 7,474 | 9.9 | 8.3 | 16.0 | 14.9 | 23.2 | 19.9 | 7.7 | 15.41 | 50.8% | 27.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 12,955 | 18.3 | 10.9 | 21.8 | 15.3 | 15.1 | 9.8 | 8.8 | 9.7 | 33.7% | 18.7% |
| LIMITED | 9,093 | 13.7 | 10.0 | 20.4 | 16.0 | 19.1 | 13.2 | 7.6 | 11.76 | 40.0% | 20.8% |
| POOR | 18,863 | 9.0 | 6.6 | 16.0 | 15.0 | 22.6 | 19.0 | 11.8 | 16.14 | 53.4% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,991 | 24.1 | 18.2 | 33.2 | 15.1 | 6.4 | 2.7 | 0.4 | 5.85 | 9.4% | 3.0% |
| GAME_SPREAD | 6,095 | 22.3 | 15.1 | 32.6 | 16.9 | 9.1 | 3.3 | 0.6 | 6.75 | 13.0% | 3.9% |
| MATCH_WINNER | 30,378 | 15.7 | 10.8 | 22.1 | 15.2 | 18.4 | 12.3 | 5.5 | 10.31 | 36.1% | 17.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 14,549 | 27.6 | 16.8 | 30.9 | 12.5 | 9.4 | 2.5 | 0.3 | 5.65 | 12.2% | 2.9% |
| TOTAL_GAMES | 10,128 | 9.9 | 10.7 | 35.6 | 26.4 | 10.4 | 4.0 | 2.9 | 9.22 | 17.3% | 6.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,663 | 24.4 | 29.8 | 33.0 | 7.5 | 4.0 | 0.9 | 0.3 | 4.73 | 5.2% | 1.2% |
| GAME_SPREAD | 8,249 | 47.3 | 16.1 | 25.0 | 7.2 | 2.2 | 1.6 | 0.6 | 3.27 | 4.5% | 2.3% |
| TOTAL_GAMES | 14,518 | 6.6 | 9.5 | 40.2 | 31.0 | 7.2 | 3.2 | 2.2 | 9.27 | 12.6% | 5.4% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,674 | 24.0 | 16.7 | 34.9 | 14.4 | 7.0 | 2.6 | 0.4 | 6.0 | 10.0% | 3.0% |
| GAME_SPREAD | 8,252 | 20.2 | 13.6 | 28.0 | 20.2 | 12.3 | 4.5 | 1.1 | 7.75 | 18.0% | 5.6% |
| TOTAL_GAMES | 14,548 | 10.2 | 10.3 | 36.3 | 25.1 | 11.5 | 4.2 | 2.5 | 9.15 | 18.1% | 6.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 40,911 | 44.2% | 24.8% | 12.99 | 35.3% | 15.2% | 10.65 |
| gen1_elo | 40,911 | 44.1% | 24.6% | 12.92 | 35.1% | 15.2% | 10.53 |
| gen1_sr | 40,911 | 51.8% | 31.2% | 15.77 | 43.8% | 21.6% | 12.94 |
| gen2 | 40,911 | 50.8% | 31.5% | 15.39 | 43.8% | 23.2% | 12.79 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 18,801 | 15.7 | 10.5 | 21.4 | 17.2 | 20.0 | 11.9 | 3.3 | 10.68 | 35.3% | 15.2% |
| STALE | 22,110 | 10.7 | 7.2 | 16.6 | 13.8 | 18.9 | 17.3 | 15.6 | 15.66 | 51.8% | 32.9% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 23,846 | 16.4 | 11.2 | 22.8 | 15.4 | 17.8 | 11.8 | 4.7 | 9.89 | 34.2% | 16.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 71,289 | 23846 | 22273 | 25170 | 24.4 | 124.4 | 1451.1 |
| ge_15pp | 29,043 | 8161 | 7921 | 12961 | 26.9 | 435.5 | 1451.1 |
| ge_25pp | 15,513 | 3922 | 3457 | 8134 | 32.1 | 586.4 | 1431.1 |
| lt_10pp | 31,341 | 12016 | 10573 | 8752 | 22.4 | 46.9 | 1421.1 |

Current slate `SL-20261031T133455Z-e32a4ded`: 535 priced rows, quote age at build {'median': 13.7, 'max': 13.8}, freshness {'AGING': 535}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 47 | 0.0 | 0.0 | 34.0 | 6.4 | 34.0 | 21.3 | 4.3 | 19.92 | 59.6% | 25.5% |
| EXTERNAL_LONE_OUTLIER | 25 | 64.0 | 36.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.43 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,051 | 19.8 | 11.0 | 25.5 | 17.8 | 17.9 | 7.2 | 0.9 | 8.56 | 25.9% | 8.1% |
| KALSHI_LONE_OUTLIER | 27 | 3.7 | 3.7 | 77.8 | 7.4 | 3.7 | 3.7 | 0.0 | 6.42 | 7.4% | 3.7% |
| MARKETS_AGREE | 836 | 66.2 | 33.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.2 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,802 | 0.0 | 2.3 | 37.2 | 25.7 | 24.2 | 9.7 | 0.9 | 11.87 | 34.7% | 10.5% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 40,911 | 6788 (16.6%) | 26.6% | 1.1% | {"EXTERNAL_STALE": 4051, "AGREES_WITH_KALSHI": 1802, "ALL_AGREE": 836, "SUPPORTS_MODEL_DIRECTION": 46, "AGREES_WITH_MODEL": 27, "EXTERNAL_OUTLIER": 25, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 18,083 | 1707 (9.4%) | 36.7% | 1.8% | {"EXTERNAL_STALE": 1051, "AGREES_WITH_KALSHI": 626, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 10,129 | 531 (5.2%) | 35.8% | 2.5% | {"EXTERNAL_STALE": 328, "AGREES_WITH_KALSHI": 190, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,795 | 504 (10.5%) | 36.3% | 2.6% | {"EXTERNAL_STALE": 308, "AGREES_WITH_KALSHI": 183, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 16,556 | 3892 (23.5%) | 18.3% | 1.0% | {"EXTERNAL_STALE": 2279, "ALL_AGREE": 836, "AGREES_WITH_KALSHI": 713, "EXTERNAL_OUTLIER": 25, "AGREES_WITH_MODEL": 23, "SUPPORTS_MODEL_DIRECTION": 15, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 7,951 | 10.6 | 7.6 | 19.4 | 14.4 | 21.5 | 16.5 | 10.0 | 14.09 | 48.0% | 26.5% |
| 4-10x | 5,487 | 11.0 | 8.5 | 18.8 | 15.5 | 21.9 | 14.3 | 10.0 | 13.63 | 46.2% | 24.3% |
| <2x | 20,871 | 15.2 | 9.9 | 19.8 | 15.9 | 17.3 | 12.9 | 9.0 | 11.51 | 39.2% | 21.9% |
| >=10x | 6,602 | 10.4 | 6.4 | 15.0 | 14.5 | 21.7 | 19.1 | 12.9 | 16.35 | 53.6% | 32.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 10,687 | 12.8 | 8.8 | 19.8 | 15.8 | 19.0 | 13.3 | 10.4 | 12.64 | 42.8% | 23.7% |
| 300-1000 | 8,793 | 11.9 | 8.8 | 17.8 | 15.3 | 20.2 | 16.4 | 9.6 | 13.59 | 46.2% | 26.0% |
| <300 | 13,015 | 8.2 | 5.8 | 15.2 | 14.8 | 23.0 | 20.0 | 13.0 | 17.07 | 56.0% | 33.0% |
| >=3000 | 8,416 | 21.6 | 12.9 | 24.2 | 15.5 | 13.6 | 7.1 | 5.0 | 7.57 | 25.7% | 12.1% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1180 | 0.5493 | 0.4109 | 0.4941 | +0.055 | -0.083 | -0.0016 ± 0.0045 |
| ratio 4-10x | 814 | 0.5815 | 0.4355 | 0.4939 | +0.088 | -0.058 | 0.0085 ± 0.0056 |
| ratio <2x | 2862 | 0.5372 | 0.4147 | 0.443 | +0.094 | -0.028 | 0.013 ± 0.0027 |
| ratio >=10x | 1007 | 0.5684 | 0.3932 | 0.4508 | +0.117 | -0.058 | 0.0141 ± 0.0058 |
| thinner_sample 1000-3000 | 1621 | 0.539 | 0.4125 | 0.4473 | +0.092 | -0.035 | 0.0105 ± 0.0036 |
| thinner_sample 300-1000 | 1330 | 0.5684 | 0.4267 | 0.4857 | +0.083 | -0.059 | 0.0028 ± 0.0043 |
| thinner_sample <300 | 1933 | 0.5597 | 0.3918 | 0.4589 | +0.101 | -0.067 | 0.0116 ± 0.0041 |
| thinner_sample >=3000 | 979 | 0.531 | 0.4377 | 0.4586 | +0.072 | -0.021 | 0.0135 ± 0.0036 |
| data_status ADEQUATE | 1609 | 0.5329 | 0.4306 | 0.4456 | +0.087 | -0.015 | 0.0135 ± 0.003 |
| data_status LIMITED | 1440 | 0.5495 | 0.4166 | 0.4701 | +0.079 | -0.053 | 0.0074 ± 0.0039 |
| data_status POOR | 2814 | 0.5624 | 0.4013 | 0.4666 | +0.096 | -0.065 | 0.0086 ± 0.0033 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 858 | 0.1993 | 0.1996 | -0.0003 ± 0.0005 | 0.5789 | 0.5799 | 0.5041 | 0.489 | 0.507 | -0.089 ± 0.0162 | -0.01 (5) |
| 3-5 | 537 | 0.205 | 0.2052 | -0.0002 ± 0.0016 | 0.5922 | 0.5915 | 0.5052 | 0.4654 | 0.486 | -0.099 ± 0.02 | 0.02 (1) |
| 5-10 | 1239 | 0.2014 | 0.2012 | +0.0001 ± 0.0019 | 0.589 | 0.586 | 0.5099 | 0.4361 | 0.4697 | -0.089 ± 0.0132 | -0.0167 (6) |
| 10-15 | 1022 | 0.2205 | 0.2114 | +0.0091 ± 0.0036 | 0.6335 | 0.6079 | 0.5278 | 0.4042 | 0.4276 | -0.109 ± 0.0145 | -0.048 (5) |
| 15-25 | 1298 | 0.2257 | 0.2112 | +0.0145 ± 0.005 | 0.6471 | 0.6063 | 0.576 | 0.3809 | 0.4414 | -0.103 ± 0.0128 | -0.0033 (9) |
| 25-40 | 750 | 0.2236 | 0.2054 | +0.0182 ± 0.0099 | 0.6374 | 0.5926 | 0.655 | 0.3449 | 0.4707 | -0.077 ± 0.0151 | -0.01 (1) |
| 40+ | 159 | 0.2822 | 0.1885 | +0.0938 ± 0.03 | 0.7687 | 0.5556 | 0.7384 | 0.2904 | 0.4151 | -0.073 ± 0.0297 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4678 | 0.1846 | 0.1855 | -0.0009 ± 0.0002 | 0.5443 | 0.5454 | 0.4869 | 0.4717 | 0.5017 | -0.023 ± 0.0064 | -0.0129 (17) |
| 3-5 | 3149 | 0.1945 | 0.1927 | +0.0018 ± 0.0006 | 0.5678 | 0.5611 | 0.4828 | 0.443 | 0.4389 | -0.059 ± 0.0079 | 0.0 (2) |
| 5-10 | 6713 | 0.2018 | 0.198 | +0.0038 ± 0.0008 | 0.5894 | 0.577 | 0.4852 | 0.4116 | 0.4237 | -0.048 ± 0.0055 | -0.0119 (21) |
| 10-15 | 5572 | 0.202 | 0.1857 | +0.0163 ± 0.0014 | 0.5903 | 0.5459 | 0.4848 | 0.3608 | 0.3562 | -0.067 ± 0.0058 | -0.0281 (16) |
| 15-25 | 6981 | 0.2069 | 0.1678 | +0.0391 ± 0.0019 | 0.6064 | 0.498 | 0.499 | 0.3033 | 0.3022 | -0.071 ± 0.0049 | -0.0025 (44) |
| 25-40 | 5433 | 0.2219 | 0.1247 | +0.0972 ± 0.003 | 0.6381 | 0.3842 | 0.5255 | 0.2114 | 0.2177 | -0.061 ± 0.0046 | -0.01 (1) |
| 40+ | 3616 | 0.3839 | 0.0448 | +0.3391 ± 0.004 | 1.0001 | 0.173 | 0.633 | 0.1041 | 0.0603 | -0.077 ± 0.0033 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 681 | 0.2062 | 0.2068 | -0.0006 ± 0.0006 | 0.5945 | 0.5964 | 0.509 | 0.4942 | 0.5242 | -0.100 ± 0.0188 | -0.01 (3) |
| 3-5 | 483 | 0.2178 | 0.2155 | +0.0023 ± 0.0017 | 0.6193 | 0.6148 | 0.515 | 0.4754 | 0.4617 | -0.123 ± 0.0225 | 0.02 (1) |
| 5-10 | 1080 | 0.2076 | 0.206 | +0.0017 ± 0.0021 | 0.6017 | 0.5967 | 0.5409 | 0.466 | 0.4944 | -0.093 ± 0.0142 | -0.01 (4) |
| 10-15 | 948 | 0.2156 | 0.21 | +0.0056 ± 0.0037 | 0.6221 | 0.607 | 0.5638 | 0.4395 | 0.4821 | -0.103 ± 0.0155 | -0.04 (5) |
| 15-25 | 1361 | 0.2301 | 0.213 | +0.0170 ± 0.0049 | 0.6549 | 0.6102 | 0.5831 | 0.3876 | 0.4438 | -0.098 ± 0.0127 | -0.0133 (9) |
| 25-40 | 956 | 0.2692 | 0.1979 | +0.0713 ± 0.009 | 0.7517 | 0.5765 | 0.6603 | 0.3461 | 0.3923 | -0.133 ± 0.0144 | -0.0075 (4) |
| 40+ | 354 | 0.3652 | 0.1649 | +0.2002 ± 0.0214 | 0.999 | 0.4971 | 0.7319 | 0.2469 | 0.2966 | -0.084 ± 0.0209 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4016 | 0.1907 | 0.1909 | -0.0002 ± 0.0002 | 0.557 | 0.5573 | 0.5084 | 0.4933 | 0.5095 | -0.040 ± 0.0071 | -0.0133 (15) |
| 3-5 | 2740 | 0.1943 | 0.1932 | +0.0011 ± 0.0007 | 0.5648 | 0.5614 | 0.5113 | 0.4716 | 0.4763 | -0.047 ± 0.0086 | 0.02 (1) |
| 5-10 | 6006 | 0.1985 | 0.1949 | +0.0036 ± 0.0009 | 0.5823 | 0.5693 | 0.5094 | 0.4353 | 0.451 | -0.043 ± 0.0058 | -0.0117 (6) |
| 10-15 | 4998 | 0.2042 | 0.1923 | +0.0118 ± 0.0016 | 0.5977 | 0.5624 | 0.511 | 0.3871 | 0.4022 | -0.051 ± 0.0063 | -0.0189 (18) |
| 15-25 | 6983 | 0.2172 | 0.1802 | +0.0370 ± 0.002 | 0.6318 | 0.5292 | 0.5225 | 0.3272 | 0.3331 | -0.065 ± 0.0051 | -0.0086 (42) |
| 25-40 | 6377 | 0.2517 | 0.1358 | +0.1159 ± 0.0029 | 0.7102 | 0.4164 | 0.5581 | 0.2413 | 0.2203 | -0.086 ± 0.0046 | -0.0044 (18) |
| 40+ | 5022 | 0.3993 | 0.0585 | +0.3408 ± 0.004 | 1.0538 | 0.211 | 0.6531 | 0.1177 | 0.0808 | -0.073 ± 0.0033 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 811 | 0.1958 | 0.198 | -0.0022 ± 0.0005 | 0.5711 | 0.5767 | 0.5017 | 0.4864 | 0.5487 | -0.036 ± 0.0163 | -0.0137 (8) |
| 3-5 | 578 | 0.2039 | 0.2018 | +0.0021 ± 0.0015 | 0.5904 | 0.5838 | 0.4964 | 0.4568 | 0.4516 | -0.122 ± 0.0194 | 0.0067 (3) |
| 5-10 | 1290 | 0.2034 | 0.2009 | +0.0025 ± 0.0019 | 0.5924 | 0.5846 | 0.5109 | 0.4372 | 0.4558 | -0.100 ± 0.0129 | -0.0071 (7) |
| 10-15 | 1022 | 0.2086 | 0.2036 | +0.0050 ± 0.0035 | 0.607 | 0.5905 | 0.5395 | 0.4161 | 0.4589 | -0.097 ± 0.0141 | -0.0317 (6) |
| 15-25 | 1228 | 0.2356 | 0.217 | +0.0187 ± 0.0052 | 0.6707 | 0.619 | 0.5884 | 0.3942 | 0.443 | -0.115 ± 0.0133 | -0.03 (1) |
| 25-40 | 766 | 0.2125 | 0.2118 | +0.0008 ± 0.0097 | 0.6134 | 0.6074 | 0.6624 | 0.3521 | 0.5039 | -0.059 ± 0.015 | 0.015 (2) |
| 40+ | 168 | 0.3002 | 0.1961 | +0.1040 ± 0.0301 | 0.8181 | 0.5732 | 0.7497 | 0.3001 | 0.4167 | -0.080 ± 0.0314 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4474 | 0.1839 | 0.1846 | -0.0007 ± 0.0002 | 0.5415 | 0.5428 | 0.4825 | 0.4672 | 0.4882 | -0.030 ± 0.0065 | -0.0163 (35) |
| 3-5 | 3127 | 0.2014 | 0.1991 | +0.0023 ± 0.0006 | 0.5859 | 0.5785 | 0.4808 | 0.4413 | 0.4327 | -0.064 ± 0.0081 | -0.0094 (18) |
| 5-10 | 6893 | 0.194 | 0.1896 | +0.0043 ± 0.0008 | 0.5709 | 0.5566 | 0.4864 | 0.4124 | 0.4206 | -0.050 ± 0.0053 | -0.01 (31) |
| 10-15 | 5530 | 0.1923 | 0.1789 | +0.0134 ± 0.0014 | 0.569 | 0.5298 | 0.4949 | 0.3715 | 0.3783 | -0.056 ± 0.0057 | -0.015 (12) |
| 15-25 | 7101 | 0.2141 | 0.1733 | +0.0407 ± 0.0019 | 0.6229 | 0.5106 | 0.5128 | 0.3183 | 0.3124 | -0.075 ± 0.0049 | -0.03 (2) |
| 25-40 | 5432 | 0.2163 | 0.1279 | +0.0884 ± 0.0031 | 0.6257 | 0.3915 | 0.5289 | 0.2133 | 0.2332 | -0.049 ± 0.0047 | 0.01 (3) |
| 40+ | 3585 | 0.3934 | 0.0502 | +0.3432 ± 0.0042 | 1.0261 | 0.1871 | 0.6423 | 0.1107 | 0.0669 | -0.078 ± 0.0036 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1228 | 0.1949 | 0.195 | -0.0001 ± 0.0004 | 0.568 | 0.5681 | 0.5059 | 0.4908 | 0.4967 | -0.068 ± 0.0129 | -0.0224 (49) |
| 3-5 | 867 | 0.1875 | 0.1868 | +0.0007 ± 0.0012 | 0.551 | 0.5479 | 0.4979 | 0.458 | 0.4671 | -0.067 ± 0.015 | -0.0194 (34) |
| 5-10 | 1807 | 0.2012 | 0.1967 | +0.0045 ± 0.0016 | 0.5911 | 0.5767 | 0.5027 | 0.429 | 0.4355 | -0.075 ± 0.0107 | -0.005 (78) |
| 10-15 | 1231 | 0.2168 | 0.2036 | +0.0132 ± 0.0032 | 0.6262 | 0.5912 | 0.5388 | 0.416 | 0.4216 | -0.091 ± 0.0132 | 0.0014 (64) |
| 15-25 | 1582 | 0.2321 | 0.2101 | +0.0220 ± 0.0045 | 0.6613 | 0.6049 | 0.5837 | 0.3889 | 0.433 | -0.086 ± 0.0117 | -0.0214 (59) |
| 25-40 | 986 | 0.244 | 0.2106 | +0.0333 ± 0.009 | 0.6972 | 0.6038 | 0.6845 | 0.3724 | 0.4757 | -0.094 ± 0.0137 | -0.0219 (26) |
| 40+ | 334 | 0.3367 | 0.2039 | +0.1328 ± 0.0238 | 0.9776 | 0.5933 | 0.8173 | 0.341 | 0.4551 | -0.103 ± 0.0225 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4625 | 0.1753 | 0.1755 | -0.0002 ± 0.0002 | 0.5197 | 0.5198 | 0.5105 | 0.4953 | 0.5079 | -0.037 ± 0.0062 | -0.0157 (88) |
| 3-5 | 3172 | 0.193 | 0.1916 | +0.0013 ± 0.0006 | 0.5633 | 0.56 | 0.5033 | 0.4636 | 0.4663 | -0.048 ± 0.0079 | -0.0209 (69) |
| 5-10 | 6530 | 0.1987 | 0.1921 | +0.0066 ± 0.0008 | 0.584 | 0.5648 | 0.499 | 0.4253 | 0.4193 | -0.063 ± 0.0055 | -0.0082 (132) |
| 10-15 | 4510 | 0.2109 | 0.1948 | +0.0161 ± 0.0016 | 0.6125 | 0.5709 | 0.5364 | 0.4134 | 0.408 | -0.071 ± 0.0066 | -0.0053 (105) |
| 15-25 | 5437 | 0.2307 | 0.2004 | +0.0302 ± 0.0024 | 0.6632 | 0.5803 | 0.5712 | 0.3758 | 0.3976 | -0.065 ± 0.0061 | -0.0253 (107) |
| 25-40 | 3652 | 0.2602 | 0.1881 | +0.0721 ± 0.0045 | 0.7363 | 0.5489 | 0.6369 | 0.3244 | 0.368 | -0.076 ± 0.007 | -0.0229 (51) |
| 40+ | 1575 | 0.3764 | 0.157 | +0.2194 ± 0.0104 | 1.0669 | 0.4675 | 0.7433 | 0.241 | 0.2844 | -0.070 ± 0.0095 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5863 | 1.019 ± 0.036 | 1.096 | 0.169 | 0.1662 | 0.2152 | 0.2055 |
| gen2 | 5863 | 0.807 ± 0.033 | 1.064 | 0.1714 | 0.1666 | 0.2344 | 0.2054 |
| gen1_elo | 5863 | 0.997 ± 0.035 | 1.092 | 0.1755 | 0.1664 | 0.214 | 0.2057 |
| gen1_sr | 5863 | 0.992 ± 0.043 | 1.121 | 0.1316 | 0.1685 | 0.2304 | 0.205 |
| gen1_ledger | 8035 | 0.856 ± 0.026 | 1.064 | 0.1878 | 0.1756 | 0.2181 | 0.2011 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 29,043)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,556 | 22.6% |
| STALE_QUOTE | market_freshness | 6,411 | 22.1% |
| BOOK_QUALITY | execution | 5,430 | 18.7% |
| POOR_DATA | data | 3,384 | 11.7% |
| LIMITED_DATA | data | 1,817 | 6.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,668 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,240 | 4.3% |
| IDENTITY_AMBIGUOUS | mapping | 1,199 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 839 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 498 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.6%, market_freshness 22.1%, execution 18.7%, data 17.9%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.3%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.4%, START_UNVERIFIABLE 94.5%, LOW_DATA_QUALITY 71.6%, THIN_PLAYER_HISTORY 60.0%, STALE_PLAYER_DATA 52.2%, STALE_KALSHI_QUOTE 44.6%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 33.2%, WIDE_SPREAD 24.7%, MODEL_HIGH_UNCERTAINTY 18.3%, PLAYER_IDENTITY_RISK 15.6%, LEVEL_TRANSFER_RISK 10.5%, LOW_DISPLAYED_LIQUIDITY 8.1%, EVENT_MAPPING_RISK 7.5%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.4%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.1%, POST_SETTLEMENT_OBSERVATION 22.6%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 15,513)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,295 | 34.1% |
| STALE_QUOTE | market_freshness | 2,909 | 18.8% |
| BOOK_QUALITY | execution | 2,827 | 18.2% |
| POOR_DATA | data | 1,449 | 9.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 876 | 5.7% |
| IDENTITY_AMBIGUOUS | mapping | 646 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 544 | 3.5% |
| LIMITED_DATA | data | 534 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 308 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 124 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.1%, market_freshness 18.8%, execution 18.2%, data 12.8%, market_freshness/coverage 9.2%, mapping 4.2%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 75.0%, THIN_PLAYER_HISTORY 62.2%, STALE_KALSHI_QUOTE 52.4%, STALE_PLAYER_DATA 46.1%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 24.2%, MODEL_HIGH_UNCERTAINTY 19.0%, PLAYER_IDENTITY_RISK 18.4%, LEVEL_TRANSFER_RISK 9.3%, EVENT_MAPPING_RISK 9.1%, LOW_DISPLAYED_LIQUIDITY 8.0%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.2%, POST_SETTLEMENT_OBSERVATION 34.1%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 12334, "IDENTITY_AMBIGUOUS": 3179}; ticker orientation: {"VERIFIED": 15513}.

Checks: discipline:AMBIGUOUS 1037, discipline:PASS 14476, identity_confidence:AMBIGUOUS 2855, identity_confidence:PASS 12658, level_mapping:NA 1049, level_mapping:PASS 14464, market_pair:AMBIGUOUS 483, market_pair:NA 352, market_pair:PASS 14678, model_complement:NA 315, model_complement:PASS 15198, namesake:AMBIGUOUS 6, namesake:PASS 15507, physical_match_id:NA 5384, physical_match_id:PASS 10129, player_ids:PASS 15513, same_pair_other_event:PASS 15513, ticker_orientation:PASS 15513

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,676 | 4.0% | 3.6% | 1.5% | {"market_freshness": 56, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 17, "coverage": 13} | 5.78 | 0.2201 / 0.2152 (657) | 22.5% | 2.8% | 3.1% | 2.8% |
| CHALLENGER | 10,112 | 16.5% | 6.1% | 10.8% | {"coverage": 987, "market_freshness/coverage": 200, "market_freshness": 172, "data": 144, "model_calibration_or_unknown": 74, "execution": 37, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.24 | 0.2213 / 0.2118 (2317) | 35.7% | 15.4% | 4.1% | 22.7% |
| DOUBLES | 2,205 | 47.0% | 46.9% | 6.7% | {"execution": 582, "mapping": 281, "market_freshness": 106, "market_freshness/coverage": 61, "coverage": 7} | 23.61 | 0.3067 / 0.2393 (532) | 10.6% | 0.0% | 100.0% | 6.2% |
| ITF_MEN | 20,181 | 25.0% | 17.5% | 32.5% | {"coverage": 1788, "market_freshness": 925, "execution": 915, "data": 739, "market_freshness/coverage": 486, "mapping": 183, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.67 | 0.2163 / 0.1996 (4151) | 38.2% | 69.0% | 16.2% | 21.7% |
| ITF_WOMEN | 26,476 | 26.6% | 19.1% | 45.3% | {"coverage": 2457, "market_freshness": 1491, "execution": 1215, "data": 1002, "market_freshness/coverage": 602, "mapping": 159, "model_calibration_or_unknown": 83, "model_calibration": 21} | 12.53 | 0.2044 / 0.195 (4866) | 39.9% | 56.9% | 9.9% | 21.5% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,168 | 5.7% | 4.9% | 1.5% | {"market_freshness": 83, "model_calibration_or_unknown": 43, "coverage": 30, "execution": 28, "data": 24, "model_calibration": 18, "market_freshness/coverage": 12, "mapping": 1} | 7.4 | 0.2308 / 0.2246 (651) | 27.2% | 1.7% | 1.4% | 3.5% |
| WTA125 | 2,316 | 11.1% | 9.5% | 1.7% | {"market_freshness": 74, "model_calibration_or_unknown": 51, "market_freshness/coverage": 41, "data": 38, "execution": 21, "model_calibration": 16, "coverage": 12, "mapping": 4} | 9.16 | 0.2123 / 0.1926 (682) | 26.6% | 10.6% | 4.6% | 7.2% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 725 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 19.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 1173 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 9 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 10 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 194 min (STALE); no external reference |
| 13 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 14 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 17.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1037 min (STALE); no external reference |
| 17 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 18 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 19 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 20 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 21 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 22 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 23 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 24 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 25 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 26 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 27 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 28 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 29 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 30 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 31 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 365 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 32 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 33 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 34 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 35 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 36 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 37 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 38 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 39 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 768 min (STALE); no external reference |
| 40 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 41 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 42 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 43 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.1h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 446 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 44 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 45 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 82 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |
| 46 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 47 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 48 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 49 | `KXITFWMATCH-26OCT31KUHDEK-KUH` | ITF_WOMEN | fair_v1 | 84% / 6% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 224 min (STALE); data LIMITED (grade C, thinner serve sample 1253.0, ratio 1.41); no external reference |
| 50 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.97, "by_level_share_of_ge_25pp": {"ATP": 0.0146, "CHALLENGER": 0.1075, "DOUBLES": 0.0668, "ITF_MEN": 0.3251, "ITF_WOMEN": 0.4532, "OTHER": 0.0008, "WTA": 0.0154, "WTA125": 0.0166}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5243, "share_primary_cause_market_settled_or_in_play": 0.4329, "share_primary_cause_stale_quote_only": 0.1875}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 15513, "identity_ambiguous_share": 0.2049, "ticker_orientation": {"VERIFIED": 15513}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 10129, "with_external": 531, "coverage": 0.0524, "external_status": {"EXTERNAL_STALE": 328, "AGREES_WITH_KALSHI": 190, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 328, "MODEL_LONE_OUTLIER": 190, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3578, "share_external_supports_model": 0.0245}, "pregame_clean_ge_25pp": {"n": 4795, "with_external": 504, "coverage": 0.1051, "external_status": {"EXTERNAL_STALE": 308, "AGREES_WITH_KALSHI": 183, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 308, "MODEL_LONE_OUTLIER": 183, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3631, "share_external_supports_model": 0.0258}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 479.5, "median_sample_ratio": 2.48, "median_min_matches": 19.0, "median_max_days_since_last": 237.0, "share_severe_asymmetry": 0.2089, "data_status": {"POOR": 8742, "LIMITED": 4049, "ADEQUATE": 2722}, "comparison_lt_10pp": {"median_thinner_serve_points": 1729.0, "median_sample_ratio": 1.7, "median_min_matches": 91.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1180, "model_minus_observed": 0.0552, "kalshi_minus_observed": -0.0832, "brier_diff_model_minus_kalshi": -0.0016}, "4-10x": {"n": 814, "model_minus_observed": 0.0877, "kalshi_minus_observed": -0.0584, "brier_diff_model_minus_kalshi": 0.0085}, "<2x": {"n": 2862, "model_minus_observed": 0.0942, "kalshi_minus_observed": -0.0283, "brier_diff_model_minus_kalshi": 0.013}, ">=10x": {"n": 1007, "model_minus_observed": 0.1175, "kalshi_minus_observed": -0.0577, "brier_diff_model_minus_kalshi": 0.0141}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 5863, "model": {"intercept": -0.535, "slope": 0.807, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.192, "slope": 1.064, "slope_se": 0.037}, "mean_extremity_model": 0.1714, "mean_extremity_kalshi": 0.1666, "model_brier": 0.2344, "kalshi_brier": 0.2054, "brier_diff_model_minus_kalshi": 0.029, "brier_diff_se": 0.0025, "model_logloss": 0.6664, "kalshi_logloss": 0.5937}, "fair_v1": {"n": 5863, "model": {"intercept": -0.427, "slope": 1.019, "slope_se": 0.036}, "kalshi_mid_same_rows": {"intercept": 0.267, "slope": 1.096, "slope_se": 0.037}, "mean_extremity_model": 0.169, "mean_extremity_kalshi": 0.1662, "model_brier": 0.2152, "kalshi_brier": 0.2055, "brier_diff_model_minus_kalshi": 0.0096, "brier_diff_se": 0.002, "model_logloss": 0.6195, "kalshi_logloss": 0.5939}, "gen1_elo": {"n": 5863, "model": {"intercept": -0.404, "slope": 0.997, "slope_se": 0.035}, "kalshi_mid_same_rows": {"intercept": 0.286, "slope": 1.092, "slope_se": 0.037}, "mean_extremity_model": 0.1755, "mean_extremity_kalshi": 0.1664, "model_brier": 0.214, "kalshi_brier": 0.2057, "brier_diff_model_minus_kalshi": 0.0083, "brier_diff_se": 0.002, "model_logloss": 0.6174, "kalshi_logloss": 0.5943}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2476, "share_ge_15": 0.442, "median_abs_gap": 12.99, "n": 40911}, "gen1_elo": {"share_ge_25": 0.2459, "share_ge_15": 0.4409, "median_abs_gap": 12.92, "n": 40911}, "gen1_sr": {"share_ge_25": 0.3123, "share_ge_15": 0.5183, "median_abs_gap": 15.77, "n": 40911}, "gen2": {"share_ge_25": 0.3149, "share_ge_15": 0.5083, "median_abs_gap": 15.39, "n": 40911}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1517, "share_ge_15": 0.3531, "median_abs_gap": 10.65, "n": 31611}, "gen1_elo": {"share_ge_25": 0.1516, "share_ge_15": 0.3512, "median_abs_gap": 10.53, "n": 31610}, "gen1_sr": {"share_ge_25": 0.2159, "share_ge_15": 0.4379, "median_abs_gap": 12.94, "n": 31613}, "gen2": {"share_ge_25": 0.2319, "share_ge_15": 0.4377, "median_abs_gap": 12.79, "n": 31613}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.78, "share_ge_25_all": 0.04, "share_ge_25_pregame_clean": 0.0357}, "WTA": {"median_abs_gap_pregame_clean": 7.4, "share_ge_25_all": 0.0573, "share_ge_25_pregame_clean": 0.049}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2374, "share_within_10pp_all": 0.4396, "share_within_10pp_pregame_clean": 0.4927, "corr_model_vs_mid_pregame_clean": 0.8504}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 858, "model_brier": 0.1993, "kalshi_brier": 0.1996, "brier_diff_model_minus_kalshi": -0.0003}, "10-15": {"n_settled": 1022, "model_brier": 0.2205, "kalshi_brier": 0.2114, "brier_diff_model_minus_kalshi": 0.0091}, "15-25": {"n_settled": 1298, "model_brier": 0.2257, "kalshi_brier": 0.2112, "brier_diff_model_minus_kalshi": 0.0145}, "25-40": {"n_settled": 750, "model_brier": 0.2236, "kalshi_brier": 0.2054, "brier_diff_model_minus_kalshi": 0.0182}, "3-5": {"n_settled": 537, "model_brier": 0.205, "kalshi_brier": 0.2052, "brier_diff_model_minus_kalshi": -0.0002}, "40+": {"n_settled": 159, "model_brier": 0.2822, "kalshi_brier": 0.1885, "brier_diff_model_minus_kalshi": 0.0938}, "5-10": {"n_settled": 1239, "model_brier": 0.2014, "kalshi_brier": 0.2012, "brier_diff_model_minus_kalshi": 0.0001}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.535, "slope": 0.807, "slope_se": 0.033}, "kalshi_slope": {"intercept": 0.192, "slope": 1.064, "slope_se": 0.037}, "n": 5863}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.489, "slope": 0.856, "slope_se": 0.026}, "kalshi_slope": {"intercept": 0.165, "slope": 1.064, "slope_se": 0.031}, "n": 8035}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 532, "model_brier": 0.3067, "kalshi_brier": 0.2393, "brier_diff_model_minus_kalshi": 0.0674, "brier_diff_se": 0.013, "corr_model_outcome": 0.0569, "corr_kalshi_outcome": 0.2246}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
